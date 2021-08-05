from xlrd import open_workbook
# import xlwt import op


file_name = 'rent_history.xls'
# sheets = ['Sheet1', 'Sheet2']

GET_SHEET_BY_NAME = 0
GET_SHEET_BY_INDEX = 1

def get_sheet(file, get_type, get_value):
    try:
        if get_type == GET_SHEET_BY_NAME:
            worksheet = file.sheet_by_name(get_value)
            return worksheet
        elif get_type == GET_SHEET_BY_INDEX:
            worksheet = file.sheet_by_index(get_value)
            return worksheet
        else:
            print("Invalid get sheet method %d" % get_type)
            return None
        if worksheet is None:
            return None
    except:
        return None


def get_sheet_data(file_name, get_type, get_value):
    with open_workbook(file_name) as workbook:
        worksheet = get_sheet(file_name, get_type, get_value)
        if not worksheet:
            print("Get find sheet(method: %d, value: %s) in %s." % (get_type, str(get_value), file_name))
            return None

        row_count = worksheet.nrows
        col_count = worksheet.ncols
        head = [worksheet.cell_value(0,col_index) for col_index in range(col_count)]
        data = []

        for row_index in range(1, row_count):
            single_data = {}
            for col_index in range(col_count):
                single_data[head[col_index]] = worksheet.cell_value(row_index,col_index)
            data.append(single_data)
    return data


def insert_new_records(file_name, get_type, get_value, records):
    with open_workbook(file_name) as workbook:
        worksheet = get_sheet(workbook, get_type, get_value)
        if not worksheet:
            print("Get find sheet(method: %d, value: %s) in %s." % (get_type, str(get_value), file_name))
            return None
        row_count = worksheet.nrows
        col_count = worksheet.ncols
        head = [worksheet.cell_value(0, col_index) for col_index in range(col_count)]

        for record in records:
            row_count += 1
            for col_count in range(len(head)):
                worksheet.write(row_count, col_count, record[head[col_count]])

        workbook.save()
        return True



