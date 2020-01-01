import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("contacts")

header_font = xlwt.Font()
header_font.name = 'Arial'
header_font.bold = True

header_style = xlwt.XFStyle()
header_style.font = header_font

sheet.write(0, 0, 'Name', header_style)
sheet.write(0, 1, 'Email', header_style)

sheet.write(1, 0, 'Julie Scott')
sheet.write(1, 1, 'julie@toricode.com')

sheet.write(2, 0, 'Harry Hernandez')
sheet.write(2, 1, 'harry@toricode.com')

workbook.save('contacts.xls')