items = ["apple","banana","orange","banana","apple","mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("duplicate:",item)
        # break
    unique_item.add(item)