from abc import ABC, abstractmethod

# Product
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Concrete Products
class Truck(Transport):
    def deliver(self):
        return "Доставка вантажівкою"

class Ship(Transport):
    def deliver(self):
        return "Доставка кораблем"

# Creator
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()

# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


# Демонстрація
road = RoadLogistics()
sea = SeaLogistics()

print(road.plan_delivery())
print(sea.plan_delivery())
