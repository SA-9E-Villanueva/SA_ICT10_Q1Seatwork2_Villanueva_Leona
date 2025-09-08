from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
site_name = "CDs for Sale"

# Integer data type
No_of_CDs = 5

# Float data type
tax_rate = 0.10  # 10% tax

# Boolean data type
free_shipping = True
all_minted = False
all_secondhand = False

# List data type
minted = ["Smashing Pumpkins - Siamese Dream (Minted)", "Usher - 8701 (Minted)", "Cher - Believe (Minted)"]
slightly_damaged = ["Elton John - Something About The Way You Look Tonight", "Miles Davis - Kind of Blue: 50th Anniversary Legacy Edition"]

# Tuple data type
openhours = ("7:00 AM", "3:00 PM")

# Dictionary data type
cds = {
    "Smashing Pumpkins - Siamese Dream (Minted)": 5.03,
    "Usher - 8701 (Minted)": 5.30,
    "Cher - Believe (Minted)": 2.65,
    "Elton John - Something About The Way You Look Tonight": 4.41,
    "Miles Davis - Kind of Blue: 50th Anniversary Legacy Edition": 18
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(site_name, target="sitename")
display(f"Available CDs: {No_of_CDs}", target="available")
display(f"Pricelist", target="Pricelist")

# Display menu items
display(minted[0], target="cd1")
display(f"${cds['˚⟡ Smashing Pumpkins - Siamese Dream (Minted)']:.2f}", target="price1")
display(minted[1], target="cd2")
display(f"${cds['˚⟡ Usher - 8701 (Minted)']:.2f}", target="price2")
display(minted[2], target="cd3")
display(f"${cds['˚⟡ Cher - Believe (Minted)']:.2f}", target="price3")
display(slightly_damaged[0], target="cd4")
display(f"${cds['˚⟡ Elton John - Something About The Way You Look Tonight']:.2f}", target="price4")
display(slightly_damaged[1], target="cd5")
display(f"${cds['˚⟡ Miles Davis - Kind of Blue: 50th Anniversary Legacy Edition']:.2f}", target="price5")

# Display additional information
display(f"Store is open from {openhours[0]} to {openhours[1]}", target="opentime")
display(f"Message us at 555-7324 for any inquiries.", target="messageus")


# Display order type
display(f"CD Restock on 10/14/2025", target="restock")















