global_variable = "I'm outside!"

def my_function():
    local_variable = "I'm inside!"
    print(f"Inside the function, I can see: {local_variable}")
    print(f"I can also see the global variable: {global_variable}")

my_function()

print(f"\nOutside the function, I can see: {global_variable}")
# The next line will cause an error!
# print(f"Can I see the local variable? {local_variable}")
# NameError: name 'local_variable' is not defined