import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def get_phone_info(number):
    try:
        # Parse the phone number
        phone = phonenumbers.parse(number, None)

        # Get the location
        location = geocoder.description_for_number(phone, "en")

        # Get the carrier
        carrier_name = carrier.name_for_number(phone, "en")

        # Get the time zones
        time_zones = timezone.time_zones_for_number(phone)

        # Get the number type
        number_type = phonenumbers.number_type(phone)
        types = {
            0: "FIXED_LINE",
            1: "MOBILE", 
            2: "FIXED_LINE_OR_MOBILE",
            3: "TOLL_FREE",
            4: "PREMIUM_RATE", 
            5: "SHARED_COST",
            6: "VOIP",
            7: "PERSONAL_NUMBER",
            8: "PAGER",
            9: "UAN",
            10: "UNKNOWN"
        }

        print(f"\nDetailed information for number {number}:")
        print(f"Country/Region: {location}")
        print(f"Carrier: {carrier_name if carrier_name else 'Not available'}")
        print(f"Is valid number: {phonenumbers.is_valid_number(phone)}")
        print(f"Country code: +{phone.country_code}")
        print(f"National number: {phone.national_number}")
        print(f"Time zone(s): {', '.join(time_zones)}")
        print(f"Number type: {types.get(number_type, 'Unknown')}")
        print(f"Is possible number: {phonenumbers.is_possible_number(phone)}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
number = input("Enter the phone number (with country code, e.g., +12025550123): ")
get_phone_info(number)