from domain.client import DomainClient
import record
from datetime import date, datetime


def check_history():
    dc = DomainClient("client_credentials.yaml")

    record.init()
    records = record.get_all_records()

    for i, single_record in enumerate(records):
        if single_record['Leased Date'] is not None:
            continue

        id = single_record['ID']
        listing = dc.listings(id)
        if listing['status'] == 'leased':
            record.update_cell(str(i+2), 'Leased Date', str(date.today()))
            list_date = datetime.strptime(record.get_cell_value(str(i + 2), 'List Date'), "%Y-%m-%d")
            days = (datetime.now()-list_date).days
            record.update_cell(str(i + 2), 'Days on Market', str(days))




