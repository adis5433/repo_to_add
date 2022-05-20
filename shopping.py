shopping = {
    "warzywniak": ["kapusta", "cebula", "czosnek", "szczypiorek"],
    "piekarnia": ["cheb", "bulki", "bagietka"],
    "miesny": ["lopatka", "piers z kurczaka", "stek", "mielonka"],
    "cukiernia": ["ptysie", "krówki", "crosaint", "pączek"],
    "papierniczy": ["papier do pakowania prezentów", "ryza papieru A4", " zeszyt w linie"]

}

sum_of_product = 0

for shop in shopping:
    shopping_list = [product.capitalize() for product in shopping[shop]]
    print("Ide do", shop.capitalize(), "aby zakupic:", shopping_list)
    sum_of_product += len(shopping[shop])

print("Do kupienia mam", sum_of_product, "produktów")


print("Pozdrowienia dla mentora Jacka")
