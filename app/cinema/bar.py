class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer: object) -> str:
        print(f"Cinema bar sold {product} to {customer.name}.")
