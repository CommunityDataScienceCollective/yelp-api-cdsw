from yelpapi import YelpAPI
from yelp_authentication import CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET

yelp_api = YelpAPI(CONSUMER_KEY, CONSUMER_SECRET, TOKEN, TOKEN_SECRET)

# Example search by location text and term. Take a look at
# http://www.yelp.com/developers/documentation/v2/search_api for
# the various options available.

print('***** 5 best rated ice cream places in Austin, TX *****')

response = yelp_api.search_query(term='ice cream', location='austin, tx', sort=2, limit=5)

print('region center (lat,long): {},{}\n'.format(response['region']['center']['latitude'], response['region']['center']['longitude']))

for business in response['businesses']:
    print('{}\n\tYelp ID: {}\n\trating: {} ({} reviews)\n\taddress: {}'.format(business['name'], business['id'], business['rating'], business['review_count'], business['location']['display_address']))

