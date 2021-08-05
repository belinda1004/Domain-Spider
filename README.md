# Domain-Spider
 
Inquery data from Domain.com.au via the API.

I wrote this script to crawl the preperty rent data in my nearby surburbs, do some simple analyse, and record the result into a file. You can also use it for buy and sold records in your surburbs by some simple modificiations of the configuration.


### Authentication 

You will first need to [sign up for a Domain developer account](https://developer.domain.com.au/).
Then you will be able to [create an application](https://developer.domain.com.au/applications) and get a Client ID and Client Secret. 
These will be used for authentication.

Note that the Domain API has multiple [Packages and Plans](https://developer.domain.com.au/docs/packages-and-plans) 
that give access to different end points of their API. You can sign up for the following packages and plans for free:

- Agents and Listings - Innovation Plan
- Property and Location - Innovation Plan 

Each package/plan combination will grant you a different Client ID and Client
Secret, which can make it a little difficult to know when to use which one.
Thankfully, this Python client takes care of all of that for you. 

Enter your credentials into a file (e.g. called client_credentials.yaml) in the
following format:

````yaml
- client_id: <AGENTS_AND_LISTINGS_ID>
  client_secret: <AGENTS_AND_LISTINGS_SECRET>
  package_and_plan: AgentsAndListingsInnovationPlan 
- client_id: <PROPERTY_AND_INNOVATION_ID>
  client_secret: <PROPERTY_AND_INNOVATION_SECRET>
  package_and_plan: PropertyAndLocationInnovationPlan
````
Now you can use those credentials (or any number of Client ID/Client Secret pairs)
to authenticate and use the API from Python:

````python
from domain import DomainClient

dc = DomainClient("client_credentials.yaml")
````

That's it! 

### To Use

Modify the configurations on the top of my_search.py to fit your requirements.

````python
LISTING_TYPE = "Rent"   # Buy / Rent/ Sold
PROPERTY_TYPE = ["House",]
MIN_BEDROOMS = 3
MIN_BATHROOMS = 2
MIN_CARSPACES = 2

SURBURBS = ["Surburb1", "Surburb2"]  # You can add as much as you want.
````

Run daily_task.py

### Find the result

Find the result from rent_history.xlsx.

To change the file name, modify the configuration on the top of record.py

````python
FILE_NAME = 'rent_history.xlsx'
````
