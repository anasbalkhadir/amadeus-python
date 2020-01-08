from amadeus import Client, ResponseError

amadeus = Client()

print('Trip Purpose Prediction')
try:
    '''
    The passenger is travelling for leisure or business?
    '''
    response = amadeus.travel.predictions.trip_purpose.get(originLocationCode='ATH', destinationLocationCode='MAD',
                                                           departureDate='2020-08-01', returnDate='2020-08-12',
                                                           searchDate='2020-06-11')
    print(response.data)
except ResponseError as error:
    print(error)
