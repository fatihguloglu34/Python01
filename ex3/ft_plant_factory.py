class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        formatted_height = f"{round(self.height, 1):.1f}cm"
        print(f"{self.name}: {formatted_height}, {self.age} days old")


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    plant = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]
    for p in plant:
        print("Created: ", end="")
        p.show()


if __name__ == "__main__":
    ft_plant_factory()

