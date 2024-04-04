import csv
import matplotlib.pyplot as plt
from collections import Counter

class Record:
    """
    Represents a record object with attributes corresponding to column names in the dataset.
    """
    def __init__(self, source, latin_name, english_name, french_name, year, month, number_otoliths):
        self.source = source
        self.latin_name = latin_name
        self.english_name = english_name
        self.french_name = french_name
        self.year = year
        self.month = month
        self.number_otoliths = number_otoliths

class RecordFormatter:
    """
    Superclass for formatting record output.
    """
    def format_record(self, record):
        """Format record output."""
        raise NotImplementedError("Subclasses must implement format_record method")

class DefaultRecordFormatter(RecordFormatter):
    """
    Subclass implementing default record formatting.
    """
    def format_record(self, record):
        """Format record output with default formatting."""
        return f"Source: {record.source}, Latin Name: {record.latin_name}, English Name: {record.english_name}, " \
            f"French Name: {record.french_name}, Year: {record.year}, Month: {record.month}, " \
            f"Number of Otoliths: {record.number_otoliths}"

class BusinessLayer:
    """
    Business layer responsible for managing data operations and business logic.
    """
    def __init__(self, filename, formatter):
        self.filename = filename
        self.records = []
        self.formatter = formatter
        self.load_records()

    def load_records(self):
        """Read records from CSV file and initialize record objects."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    record = Record(
                        row['source'],
                        row['latin.name_nom.latin'],
                        row['english.name_nom.anglais'],
                        row['french.name_nom.français'],
                        row['year_année'],
                        row['month_mois'],
                        row['number.otoliths_nombre.otolithes']
                    )
                    self.records.append(record)
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_records(self, filename):
        """Save records to a new CSV file."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["source", "latin.name_nom.latin", "english.name_nom.anglais", 
                                "french.name_nom.français", "year_année", "month_mois", 
                                "number.otoliths_nombre.otolithes"])
                for record in self.records:
                    writer.writerow([record.source, record.latin_name, record.english_name,
                                    record.french_name, record.year, record.month, record.number_otoliths])
                print("Records saved successfully")
        except Exception as e:
            print(f"An error occurred while saving records: {e}")

    def display_record(self, index):
        """Display a single record."""
        if 0 <= index < len(self.records):
            record = self.records[index]
            formatted_record = self.formatter.format_record(record)  # Polymorphic method call
            print(formatted_record)
        else:
            print("Invalid record index.")

    def display_records(self):
        """Display all records."""
        for index, record in enumerate(self.records):
            print(f"Record {index + 1}")
            self.display_record(index)
            if (index + 1) % 10 == 0:
                print("Program by Ben Nguyen")

    def add_record(self, record):
        """Add a new record."""
        self.records.append(record)
        print("Record added successfully.")

    def edit_record(self, index, new_record):
        """Edit an existing record."""
        if 0 <= index < len(self.records):
            self.records[index] = new_record
            print("Record edited successfully.")
        else:
            print("Invalid record index.")

    def delete_record(self, index):
        """Delete a record."""
        if 0 <= index < len(self.records):
            del self.records[index]
            print("Record deleted successfully.")
        else:
            print("Invalid record index.")



    def generate_bar_chart(self):
        """Generate a vertical bar chart based on user input."""

        # Dictionary mapping column names to display names
        column_display_names = {
        'source': 'Source',
        'latin_name': 'Latin Name',
        'english_name': 'English Name',
        'french_name': 'French Name',
        'year': 'Year',
        'month': 'Month',
        'number_otoliths': 'Number of Otoliths'
    }
        
        try:
            x_column = input("Enter the column name for the x-axis (e.g., 'source', 'latin_name', 'english_name', 'french_name', 'year', 'month', 'number_otoliths'): ")

            x_values = []
            
            for record in self.records:
                x_values.append(getattr(record, x_column))

            x_counts = Counter(x_values)
            unique_x_values = list(x_counts.keys())
            y_values = list(x_counts.values())

            # Get the display name for the x-axis label
            x_label = column_display_names.get(x_column.lower(), x_column)
                
            plt.figure(figsize=(10, 6))
            plt.bar(unique_x_values, y_values, color='skyblue')
            plt.xlabel(x_label)  # Use the provided column name as the x-axis label
            plt.ylabel('Count')
            plt.title(f'Count of {x_label}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while generating the bar chart: {e}")


class PresentationLayer:
    """
    Presentation layer responsible for user interactions.
    """
    def __init__(self, business_layer):
        self.business_layer = business_layer
        self.full_name = "Ben Nguyen"

    def display_menu(self):
        """Display menu options."""
        print("Menu:")
        print("1. Reload data from dataset")
        print("2. Display all records")
        print("3. Add a new record")
        print("4. Select, display, and edit a record")
        print("5. Delete a record")
        print("6. Generate vertical bar chart")
        print("7. Exit")

    def start(self):
        """Start the presentation layer."""
        while True:
            print(f"Full Name: {self.full_name}")
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.business_layer.load_records()
            elif choice == '2':
                self.business_layer.display_records()
            elif choice == '3':
                record = self.create_record()
                self.business_layer.add_record(record)
            elif choice == '4':
                self.select_display_edit_record()
            elif choice == '5':
                self.delete_record()
            elif choice == '6':
                self.business_layer.generate_bar_chart()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

    def create_record(self):
        """Create a new record based on user input."""
        source = input("Enter Source: ")
        latin_name = input("Enter Latin Name: ")
        english_name = input("Enter English Name: ")
        french_name = input("Enter French Name: ")
        year = input("Enter Year: ")
        month = input("Enter Month: ")
        number_otoliths = input("Enter Number of Otoliths: ")
        return Record(source, latin_name, english_name, french_name, year, month, number_otoliths)

    def select_display_edit_record(self):
        """Select, display, and edit a record."""
        index = int(input("Enter record index to select: ")) -1
        if 0 <= index < len(self.business_layer.records):
            self.business_layer.display_record(index)
            choice = input("Do you want to edit this record? (yes/no): ")
            if choice.lower() == 'yes':
                new_record = self.create_record()
                self.business_layer.edit_record(index, new_record)
        else:
            print("Invalid record index.")

    def delete_record(self):
        """Delete a record."""
        index = int(input("Enter record index to delete: ")) -1
        self.business_layer.delete_record(index)

if __name__ == "__main__":
    dataset_filename = "NAFO-4T-Yellowtail-Flounder-otoliths.csv"
    formatter = DefaultRecordFormatter()  # Create an instance of the formatter class
    business_layer = BusinessLayer(dataset_filename, formatter)  # Pass formatter as an argument
    presentation_layer = PresentationLayer(business_layer)
    presentation_layer.start()
