import abc
from abc import ABC, abstractmethod
import copy

# Creational Design Patterns
# Prototype pattern
class Prototype:
    def clone(self):
        return copy.deepcopy(self)
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self._value = value
# Builder pattern
class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        #Memory of computer
        self.memory = None  
        # Hard disk of computer
        self.hdd = None  
        # Gpu Of Computer
        self.gpu = None

    def __str__(self):
        info = (
            f"Memory: {self.memory}GB\n"
            f"Hard Disk: {self.hdd}GB\n"
            f"Graphics Card: {self.gpu}"
        )
        return info
# Abstract Builder
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("AG231241")

    def get_computer(self):
        return self.computer
# Concrete Builder
class GamingComputerBuilder(ComputerBuilder):
    def build_memory(self, amount):
        self.computer.memory = amount

    def build_hdd(self, amount):
        self.computer.hdd = amount

    def build_gpu(self, gpu_model):
        self.computer.gpu = gpu_model
# Director
class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = GamingComputerBuilder()
        [step for step in (self.builder.build_memory(memory),
                           self.builder.build_hdd(hdd),
                           self.builder.build_gpu(gpu))]

# Structural Design Patterns

# Adapter pattern
class FahrenheitThermometer:
    def __init__(self):
        self.temperature = 0

    def get_temperature(self):
        return self.temperature
# Target interface
class CelsiusThermometer:
    def __init__(self):
        self.temperature = 0

    def set_temperature(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature
# Adapter class
class FahrenheitCelsiusAdapter(CelsiusThermometer):
    def __init__(self, thermometer):
        self.thermometer = thermometer

    def set_temperature(self, temperature):
        self.thermometer.temperature = (temperature * 9 / 5) + 32

    def get_temperature(self):
        return (self.thermometer.temperature - 32) * 5 / 9
# Decorator pattern
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass
# Concrete components provide default implementations of the component interface.
class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent perform operation")
class Decorator(Component, ABC):
    def __init__(self, component: Component):
        self._component = component
    @abstractmethod
    def operation(self):
        self._component.operation()
# Concrete decorators call the wrapped object and alter its result in some way.
class ConcreteDecoratorA(Decorator):
    def operation(self):
        print("ConcreteDecoratorA perform operation")
        self._component.operation()
# Decorators can execute their behavior either before or after the call to a wrapped object.
class ConcreteDecoratorB(Decorator):
    def operation(self):
        print("ConcreteDecoratorB perform operation")
        self._component.operation()
        print("ConcreteDecoratorB perform operation")

# Client code works with all objects using the component interface. This way it can stay
# independent of the concrete classes of components it works with.
def client_code(component: Component):
    print("RESULT:", end=" ")
    component.operation()

# Behavioral Design Patterns
# Observer pattern
class Subject(abc.ABC):

    def __init__(self):
        self.observers = []
    def attach(self, observer):
        self.observers.append(observer)
    def detach(self, observer):
        self.observers.remove(observer)
    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)
class Observer:
    def update(self, *args, **kwargs):
        pass
# Command pattern code 
class Command:
    def execute(self):
        pass
# Concrete Command code 
class HelloCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.write("I HAVE RECEIVED ANOTHER NEW GENERATION PC")
# Receiver class code
class ConsoleOutput:
    def write(self, text):
        print(text)
# Client class code 
class TextEditor:
    def __init__(self):
        self.history = []

    def execute(self, command):
        self.history.append(command)
        command.execute()

#CALLING ALL CLASSES WITH FUNCTIONS IN MAIN
if __name__ == "__main__":
    # CALLING CREATIONAL PATTERNS
    prototype = ConcretePrototype("CORE I9 GENERATION COMPUTERS ARE GREAT")
    prototype_copy = prototype.clone()
    print(prototype_copy._value)

    engineer = HardwareEngineer()
    engineer.construct_computer(16, 512, "GeForce RTX 3080")
    computer = engineer.builder.get_computer()
    print(computer)

    # CALLING STRUCTURAL PATTERNS
    print("After the PC HEAT UP")
    f = FahrenheitThermometer()
    f.temperature = 100
    print(f"Fahrenheit temperature: {f.get_temperature()}")
    a = FahrenheitCelsiusAdapter(f)
    print(f"Celsius temperature: {a.get_temperature()}")

    simple = ConcreteComponent()
    print("Client: I've got an issue in my pc:")
    client_code(simple)
    print("")
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Client: Now I've solved my issue after consulting with a pc repair shop:")
    client_code(decorator2)

    # CALLING BEHAVIOR PATTERNS
    console_output = ConsoleOutput()
    hello_command = HelloCommand(console_output)
    text_editor = TextEditor()
    text_editor.execute(hello_command)