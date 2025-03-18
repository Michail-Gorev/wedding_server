from django.contrib import admin
from .models import Guest
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.styles import Alignment


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'alcohol', 'hot', 'car')
    actions = ['export_as_xlsx']

    def export_as_xlsx(self, request, queryset):
        """
        Кастомное действие для экспорта выбранных гостей в Excel.
        """
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=guests.xlsx'

        # Создаем книгу Excel
        wb = Workbook()
        ws = wb.active

        # Заголовки столбцов
        headers = [
            'Имя', 'Номер телефона', 'Алкоголь', 'Свой вариант алкоголя',
            'Горячее', 'Музыка', 'На машине', 'Комментарий'
        ]
        ws.append(headers)

        # Данные
        for guest in queryset:
            ws.append([
                guest.name,
                guest.phone,
                guest.alcohol,
                guest.custom_alcohol,
                guest.hot,
                guest.music,
                'Да' if guest.car else 'Нет',
                guest.comment
            ])

        # Настройка ширины столбцов
        for col in ws.columns:
            max_length = 0
            column = col[0].column_letter  # Получаем букву столбца
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            ws.column_dimensions[column].width = adjusted_width

        # Выравнивание заголовков по центру
        for cell in ws[1]:
            cell.alignment = Alignment(horizontal='center')

        # Сохраняем книгу в ответ
        wb.save(response)
        return response

    export_as_xlsx.short_description = "Экспортировать выбранных гостей в Excel"