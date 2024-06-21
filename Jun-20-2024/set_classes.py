# Set
a = [1, 2, 3, 4, 5, 6, 1, 2, 3]
set_a = set(a)

print(f"a: {a}")
print(f"Second element of a: {a[1]}")

print(f"set_a: {set_a}")

try:
    print(f"Second element of set_a: {set_a[1]}")
except Exception as e:
    print("Cannot retrieve the second element of set_a")
    print(e)

# Class


class SampleClasses:
    value = 0
    disabled = 0

    def __init__(self, value=0, disabled=0):
        print("Initializing new instance of SampleClasses")
        self.value = value
        self.disabled = disabled

    def getValue(self):
        print(f"The value is {self.value}")
    
    def addValue(self):
        self.value += 1

    def canRun(self):
        if self.disabled == 0:
            print("Can run")
        else:
            print("Cannot run")


new_instance = SampleClasses()
new_instance_1 = SampleClasses(value=1, disabled=1)

new_instance.getValue()
new_instance_1.getValue()

new_instance.canRun()
new_instance_1.canRun()
