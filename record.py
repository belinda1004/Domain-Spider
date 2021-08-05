

from openpyxl import load_workbook


sheet = None
wb = None
records = []
head = []
row_count = 2
FILE_NAME = 'rent_history.xlsx'

def init():
    global sheet, records, head, wb
    # 默认可读写，若有需要可以指定write_only和read_only为True
    wb = load_workbook(FILE_NAME)
    sheet = wb.worksheets[0]
    head = get_head()
    records = read_sheet_get_all_record()


def get_head():
    head = [cell.value for cell in list(sheet.rows)[0]]
    return head


def read_sheet_get_all_record():
    global row_count
    rows = list(sheet.rows)
    row_count = len(rows) + 1

    records = []
    for row in rows[1:]:
        record = {}
        for i, key in enumerate(head):
            record[key] = row[i].value
        records.append(record)
    return records


def get_all_records():
    return records


def is_in_records(id):
    for record in records:
        if record['ID'] == id:
            return True
    return False


def get_col_name(index):
    res = ''
    if index > 25:
        res = get_col_name(index // 26 - 1)
        index = index % 26
    res += chr(ord('A') + index)
    return res


def add_records(new_records):
    global row_count
    for record in new_records:
        for col_index in range(len(head)):
            cell_name = get_col_name(col_index) + str(row_count)
            sheet[cell_name] = record[head[col_index]]
        row_count += 1

    wb.save(FILE_NAME)


def update_cell(row_index, col_name, value):
    col_index = head.index(col_name)
    cell_name = get_col_name(col_index) + str(row_index)
    sheet[cell_name] = value
    wb.save(FILE_NAME)


def get_cell_value(row_index, col_name):
    col_index = head.index(col_name)
    cell_name = get_col_name(col_index) + str(row_index)
    return sheet[cell_name].value
