from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
site_name = "CDs for Sale"

# Integer data type
No_of_CDs = 5

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Spaghetti Carbonara", "Garlic Bread", "Caesar Salad"]
beverages = ["Iced Tea", "Sparkling Water"]

# Tuple data type
business_hours = ("11:00 AM", "10:00 PM")

# Dictionary data type
menu = {
    "Spaghetti Carbonara": 79.99,
    "Caesar Salad": 150.00,
    "Garlic Bread": 50.00,
    "Iced Tea": 30.00,
    "Sparkling Water": 20.00
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(site_name, target="sitename")
display(f"Since {No_of_CDs}", target="available")
display(f"Pricelist", target="Pricelist")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Spaghetti Carbonara']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Garlic Bread']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Caesar Salad']:.2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['Iced Tea']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Sparkling Water']:.2f}", target="price5")

# Display additional information
display(f"Message us at: 555-7324 for any inquiries.", target="openingHours")


# Display order type
display(f"CD Restock on 10/14/2025", target="orderType")







