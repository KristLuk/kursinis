"""
Roman Numeral Converter System
Demonstrates OOP principles, Singleton pattern, and file operations
"""

from abc import ABC, abstractmethod
import csv

# ==============================================
# OOP Pillar 1: Abstraction (ABC)
# ==============================================
class NumeralConverter(ABC):
    """Abstract base class defining the converter interface"""
    @abstractmethod
    def convert(self, value):
        pass

# ==============================================
# OOP Pillar 2: Inheritance
# ==============================================
class RomanToDecimalConverter(NumeralConverter):
    """Converts Roman numerals to decimal"""
    _roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

    def convert(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self._roman_values[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

class DecimalToRomanConverter(NumeralConverter):
    """Converts decimal numbers to Roman numerals"""
    _value_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                 (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                 (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    def convert(self, num):
        if not 0 < num < 4000:
            raise ValueError("Number must be between 1 and 3999")
        result = []
        for value, numeral in self._value_map:
            while num >= value:
                result.append(numeral)
                num -= value
        return ''.join(result)

# ==============================================
# OOP Pillar 3: Polymorphism
# ==============================================
def print_conversion(converter, value):
    """Demonstrates polymorphism - works with any NumeralConverter"""
    print(f"Converted value: {converter.convert(value)}")

# ==============================================
# OOP Pillar 4: Encapsulation
# ==============================================
class ConversionHistory:
    """Manages conversion history with encapsulated data"""
    def __init__(self):
        self._history = []

    def add_record(self, from_val, to_val, direction):
        """Add a conversion record"""
        self._history.append({
            'input': from_val,
            'output': to_val,
            'type': direction
        })

    def get_history(self):
        """Get conversion history (protected data)"""
        return self._history.copy()

# ==============================================
# Design Pattern: Singleton
# ==============================================
class ConverterFactory:
    """Singleton factory for creating converters"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.converters = {
                'roman': RomanToDecimalConverter(),
                'decimal': DecimalToRomanConverter()
            }
        return cls._instance

    def get_converter(self, converter_type):
        """Factory method to get converter"""
        return self.converters.get(converter_type)

# ==============================================
# Composition/Agregation
# ==============================================
# Add these new methods to the ConversionSystem class
class ConversionSystem:
    # ... (existing methods remain the same)
    """Main system that coordinates conversions and history"""
    def __init__(self):
        self.factory = ConverterFactory()
        self.history = ConversionHistory()

    def convert(self, value, conversion_type):
        """Convert between number systems and record history"""
        converter = self.factory.get_converter(conversion_type)
        if not converter:
            raise ValueError(f"Invalid conversion type: {conversion_type}")
        
        result = converter.convert(value)
        
        # Record the conversion
        if conversion_type == "roman":
            self.history.add_record(value, result, "roman")
        else:
            self.history.add_record(value, result, "decimal")
        
        return result

    # ... (keep all the existing save/load methods)

    def save_to_csv(self, filename="conversions.csv"):
        """Save history to CSV file"""
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['input', 'output', 'type'])
            writer.writeheader()
            writer.writerows(self.history.get_history())
        print(f"History saved to {filename}")

    def save_to_txt(self, filename="conversions.txt"):
        """Save history to human-readable TXT file"""
        with open(filename, 'w') as file:
            file.write("Conversion History:\n")
            file.write("==================\n")
            for record in self.history.get_history():
                direction = "Roman→Decimal" if record['type'] == 'roman' else "Decimal→Roman"
                file.write(f"{record['input']} → {record['output']} ({direction})\n")
        print(f"History saved to {filename}")

    def load_from_csv(self, filename="conversions.csv"):
        """Load history from CSV file"""
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.history.add_record(row['input'], row['output'], row['type'])
            print(f"History loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: {filename} not found")

    def load_from_txt(self, filename="conversions.txt"):
        """Load history from TXT file (basic implementation)"""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    if '→' in line:  # Simple pattern matching
                        parts = line.strip().split(' → ')
                        if len(parts) == 2:
                            input_val, rest = parts
                            output_val, conv_type = rest.split(' (')
                            conv_type = conv_type.rstrip(')')
                            # Determine conversion direction
                            if 'Roman→Decimal' in conv_type:
                                self.history.add_record(input_val, output_val, 'roman')
                            else:
                                self.history.add_record(output_val, input_val, 'decimal')
            print(f"History loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: {filename} not found")

# ==============================================
# Demonstration
# ==============================================
if __name__ == "__main__":
    system = ConversionSystem()
    
    while True:
        print("\nRoman-Decimal Converter")
        print("1. Roman → Decimal")
        print("2. Decimal → Roman")
        print("3. View History")
        print("4. Save History (CSV)")
        print("5. Save History (TXT)")
        print("6. Load History (CSV)")
        print("7. Load History (TXT)")
        print("8. Exit")
        
        choice = input("Select an option (1-8): ")
        
        if choice == "1":
            roman = input("Enter Roman numeral (e.g., MCMXCIV): ").strip().upper()
            try:
                decimal = system.convert(roman, "roman")
                print(f"{roman} = {decimal}")
            except KeyError:
                print("Invalid Roman numeral! Use only I, V, X, L, C, D, M.")
        
        elif choice == "2":
            try:
                num = int(input("Enter decimal number (1-3999): "))
                roman = system.convert(num, "decimal")
                print(f"{num} = {roman}")
            except ValueError:
                print("Invalid number! Enter an integer between 1 and 3999.")
        
        elif choice == "3":
            print("\nConversion History:")
            for record in system.history.get_history():
                direction = "Roman→Decimal" if record['type'] == 'roman' else "Decimal→Roman"
                print(f"{record['input']} → {record['output']} ({direction})")
        
        elif choice == "4":
            filename = input("Enter CSV filename (default: conversions.csv): ") or "conversions.csv"
            system.save_to_csv(filename)
        
        elif choice == "5":
            filename = input("Enter TXT filename (default: conversions.txt): ") or "conversions.txt"
            system.save_to_txt(filename)
        
        elif choice == "6":
            filename = input("Enter CSV filename to load (default: conversions.csv): ") or "conversions.csv"
            system.load_from_csv(filename)
        
        elif choice == "7":
            filename = input("Enter TXT filename to load (default: conversions.txt): ") or "conversions.txt"
            system.load_from_txt(filename)
        
        elif choice == "8":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Try again.")