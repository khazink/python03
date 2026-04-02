import sys

def sort_inventory(inventory):
    items = list(inventory.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items

def main(args):
    inventory = {}
    for arg in args:
        item, count = arg.split(':')
        inventory[item] = int(count)
    total = sum(inventory.values())
    print(f"Total items in inventory: {total}")
    unique = len(inventory)
    print(f"Unique item types: {unique}")
    print()
    print("=== Current Inventory ===")
    sorted_items = sort_inventory(inventory)
    for item, count in sorted_items:
        unit_word = "unit" if count == 1 else "units"
        percent = count / total * 100
        print(f"{item}: {count} {unit_word} ({percent:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    top_item, top_count = sorted_items[0]
    least_item, least_count = sorted_items[-1]
    print(f"Most abundant: {top_item} ({top_count} units)")
    print(f"Least abundant: {least_item} ({least_count} unit)")
    print()
    print("=== Item Categories ===")
    moderate = {k: v for k, v in inventory.items() if v > 3}
    scarce = {k: v for k, v in inventory.items() if v <= 3}
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")
    print()
    print("=== Management Suggestions ===")
    restock = [k for k, v in inventory.items() if v == 1]
    print(f"Restock needed: {', '.join(restock)}")
    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print(f"Dictionary values: {', '.join(map(str, inventory.values()))}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    main(sys.argv[1:])