class Plant:
    name: str
    height: float
    days: int

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1):.1f}cm, {self.days} days old")

    def age(self) -> None:
        self.days = self.days + 1

    def grow(self) -> None:
        self.height = self.height + 0.8


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.days = 30
    initial_height = rose.height
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age()
        rose.show()
    total_growth = round(rose.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()

