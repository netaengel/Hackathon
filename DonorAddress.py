import geopandas
import geopy

from geopy.geocoders import Nominatim  # locator that holds the Geocoding service

# calculate each address coordinate using geopy.
# checking whether an address is in israel + which area is it (south/ center/ north)

locator = Nominatim(user_agent="myGeocoder")
address = input("Please enter the donor address in the format (street line (optional), city, country)")
location = locator.geocode(address)
print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
center_south_y = locator.geocode("Ashkelon, Israel")  # Ashkelon will separate between y center and y south
print("center south Latitude = {}".format(center_south_y.latitude))
center_north_y = locator.geocode(
    "Zikhron Ya'akov, Israel")  # Zichron Ya'akov will separate between y center and y north
print("center north Latitude = {}".format(center_north_y.latitude))
north_limit_y = (33.3084738447906, 35.772599778631104)
print("north limit Latitude = " + " " + str(north_limit_y[0]))
south_limit_y = (29.491721947366308, 34.903419761981326)
print("south limit Latitude = " + " " + str(south_limit_y[0]))


def check_in_israel(location_str):  # is in Israel (cant be israel)
    location_list = location_str.split(", ")
    location_country = location_list[-1]
    if location_country == "Israel":
        print("In Israel")
        return True
    return False


def check_in_center(location):
    if center_south_y.latitude < location.latitude < center_north_y.latitude:
        print("In Center")
        return True
    return False


def check_in_south(location):
    if south_limit_y[0] <= location.latitude <= center_south_y.latitude:
        print("In South")
        return True
    return False


def check_in_north(location):
    if north_limit_y[0] >= location.latitude >= center_north_y.latitude:
        print("In North")
        return True
    return False


check_in_israel(address)
check_in_center(location)
check_in_north(location)
check_in_south(location)
