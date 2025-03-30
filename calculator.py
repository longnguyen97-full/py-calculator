class Calculator:
    def __init__(self):
        self.result = 0
        self.current_operation = None
        self.first_number = None
        self.second_number = None

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def clear(self):
        """Reset calculator state."""
        self.result = 0
        self.current_operation = None
        self.first_number = None
        self.second_number = None

    def calculate(self, operation, a, b):
        """Perform calculation based on operation."""
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        
        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")
            
        return operations[operation](a, b) 