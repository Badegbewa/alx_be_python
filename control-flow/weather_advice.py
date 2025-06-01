
#This script asks users for about weather and give clothing recommendations.

weather = input("What's the waether like today? (sunny/rainy/cold): ").lower()
print()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses. ")
elif weather == "rainy":
    print("Dont forget your umbrella and a raincoat. ")
elif weather == "cold":
    print("Make sure to wear a warm coat and scarf. ")
else:
    print("Sorry, i don't have recommendations for this weather.")





