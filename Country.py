# Importing the required module.
from countryinfo import CountryInfo

# Getting a country name from the user.
count=input("Enter Country Name : ")
country = CountryInfo(count)
print("Alias : ",country.alt_spellings())
print("Capital : ",country.capital())
print("Currency : ",country.currencies())