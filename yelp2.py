from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by bounding box and category. See
# http://www.yelp.com/developers/documentation/v2/all_category_list
# for an official list of Yelp categories. The bounding box definition
# comes from
# http://isithackday.com/geoplanet-explorer/index.php?woeid=12587707.

print('***** 5 bike rentals in San Francisco county *****')

response = yelp_api.search_query(category_filter='bikerentals', bounds='37.678799,-123.125740|37.832371,-122.356979', limit=5)
    
for business in response['businesses']:
    print('{}\n\tYelp ID: {}\n\trating: {} ({} reviews)\n\taddress: {}'.format(business['name'], business['id'], business['rating'],
                                                                               business['review_count'], business['location']['display_address']))
