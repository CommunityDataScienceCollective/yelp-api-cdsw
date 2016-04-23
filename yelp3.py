from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example business query. Look at
# http://www.yelp.com/developers/documentation/v2/business for more
# information.

print("***** selected reviews for Amy's on 6th St. *****")

business = yelp_api.business_query(id='amys-ice-creams-austin-3')

for review in business['reviews']:
    print('rating: {}\nexcerpt: {}\n'.format(review['rating'], review['excerpt']))

