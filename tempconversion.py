#!/usr/bin/env python
Fahrenheit = int(raw_input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0

print "Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C"

#!/usr/bin/env python
Celsius = int(raw_input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print "Temperature:", Celsius, "Celsius = ", Fahrenheit, " F"