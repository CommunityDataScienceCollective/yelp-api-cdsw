from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example business query. Look at
# http://www.yelp.com/developers/documentation/v2/business for more
# information.

business = yelp_api.business_query(id='amys-ice-creams-austin-3')
print(business)


