def temperatur_konverterare():

    print("1. Celsius till Fahrenheit") # vad vill du konvertera
    print("2. Fahrenheit till Celsius")
    print("3. Kelvin till Celsius")
    print("4. Celsius till Kelvin")

    val = input("Vad vill man konvertera: ") #Inputs

    if val == "1": # Vilken input
        celsius = float(input("Skriv temp i Celsius: ")) # Vilken temperatur vill du konverta (I detta fall Celsius)
        fahrenheit = (celsius * 9/5) + 32 #beräkningen till konvertion som jag bara plockade på en konvertion sida
        print(f"{celsius}°C = {fahrenheit}°F") # Svaret
    elif val == "2":
        fahrenheit = float(input("Skriv temp i Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
    elif val == "3":
        kelvin = float(input("Skriv temp i Kelvin: "))
        celsius = kelvin - 273.15
        print(f"{kelvin}K = {celsius}°C")
    elif val == "4":
        celsius = float(input("Skriv temp i Celsius: "))
        kelvin = celsius + 273.15 
        print(f"{celsius}°C = {kelvin}K")
    else:
        print("🐛") # om du valde någon annan garga input som it e 1-4 (din lilla downy pöjk) 

temperatur_konverterare()