import csv

with open("grocery_products.txt", "rb") as f:
    products = f.readlines()


def clean_text(products):
    products = [product.decode("utf-8").replace("\uf06f", "").strip()
                for product in products]
    return products


def stratify_products(products):
    product_category = dict()
    print(products)
    i = 0

    while(i < len(products)):
        # Find category
        if products[i] == "________________":
            cur_category = products[i+2]
            product_category[products[i+2]] = []
            i += 1
        else:
            if products[i] in product_category:
                pass
            else:
                product_category[cur_category].append(products[i])
        i += 1

    return product_category


def write_csv(product_dict):
    with open("products.csv", "w", newline='') as csvfile:
        product_writer = csv.writer(
            csvfile, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        product_writer.writerow(["Item", "Category", "SameAs", "Material"])
        for category in product_dict.keys():
            for product in product_dict[category]:
                product_writer.writerow([f"{product}", f"{category}", "", ""])


products = clean_text(products)
product_dict = stratify_products(products)
write_csv(product_dict)
