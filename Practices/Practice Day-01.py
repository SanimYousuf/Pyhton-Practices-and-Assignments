class Product:
    def __init__(self, item, quantity, price) -> None:
        self.item = item
        self.quantity = quantity
        self.price = price

class Shop:
    def __init__(self, name) -> None:
        self.name = name
        self.cart = []

    def add_product(self, product : Product):

        product_info = {'Item' : product.item, 'Quantity' : product.quantity, 'Price' : product.price}
        self.cart.append(product_info)

    def buy_product(self, item, quantity, price, amount):
        total = 0

        for product in self.cart:
            total += quantity * price

        if total > amount:
            print(f'Insufficient balance. Add {total - amount}')

        else:
            print(f'Transaction successful. Here is your extra: {amount - total}')

shop = Shop('DIU Mall')

product = Product('Juice', 3, 30)
shop.add_product(product)

shop.buy_product('Juice', 3, 30, 100)