# key value pairs
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    9: "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversion["Dec"])
print(monthConversion.get("Nov"))
print(monthConversion.get("Luv", "Not a valid key"))
print(monthConversion.get(9))

