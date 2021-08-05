
import os
from domain.client import DomainClient
import record

LISTING_TYPE = "Rent"   # Buy / Rent/ Sold
PROPERTY_TYPE = ["House",]
MIN_BEDROOMS = 3
MIN_BATHROOMS = 2
MIN_CARSPACES = 2

SURBURBS = ["Mooroolbark", "CHIRNSIDE PARK"]

dc = None

def init():
    global dc
    dc = DomainClient("client_credentials.yaml")
    record.init()

def get_list():
    records = []
    for surburb in SURBURBS:
        terms = {
          "listingType": LISTING_TYPE,
          "propertyTypes": PROPERTY_TYPE,
          "minBedrooms": MIN_BEDROOMS,
          "minBathrooms": MIN_BATHROOMS,
          "minCarspaces": MIN_CARSPACES,
          "locations":[
            {
              "state":"VIC",
              "region":"",
              "area":"",
              "suburb": surburb,
              "postCode":"",
              "includeSurroundingSuburbs":False
            }
          ]
        }

        results = dc.residential_search(terms=terms)
        print("Get %d results for %s" % (len(results), surburb))

        for i in range(len(results)):
            result = results[i]['listing']
            property_details = result['propertyDetails']
            price_details = result['priceDetails']
            id = result['id']

            if record.is_in_records(id):
                continue

            listing = dc.listings(id)
            single_record = {
                      'ID': id,
                      'Address': listing['addressParts']['displayAddress'],
                      'Surburb': property_details['suburb'],
                      'Property Type': property_details['propertyType'],
                      'Bathrooms': property_details['bathrooms'],
                      'Bedrooms': property_details['bedrooms'],
                      'Car Spaces': property_details['carspaces'],
                      'Price': price_details['displayPrice'],
                      'URL': 'https://www.domain.com.au/' + result['listingSlug'],
                      'List Date': listing['dateListed'][:10],
                      'Leased Date': '',
                      'Date Available': listing['dateAvailable'],
                      'Description': listing['description'],
                      'Days on Market': '',
                       }

            records.append(single_record)

    print("Get %d new records" % len(records))
    record.add_records(records)




if __name__ == '__main__':
    init()
    list = get_list()