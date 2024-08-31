import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QLineEdit,
    QPushButton, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class RaffleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Robot Raffler")
        self.setMinimumSize(200, 400)
        self.init_ui()

    def init_ui(self):
        # Main widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Instruction Label
        header_label = QLabel("Enter names (separated by lines or commas):")
        header_label.setFont(QFont("San Francisco", 11))
        layout.addWidget(header_label)

        # Names input area
        self.names_input = QTextEdit()
        self.names_input.setFont(QFont("San Francisco", 12))
        layout.addWidget(self.names_input)

        # Number of winners input
        winners_layout = QHBoxLayout()
        winners_label = QLabel("Number of winners:")
        winners_label.setFont(QFont("San Francisco", 11))
        winners_layout.addWidget(winners_label)

        self.winners_input = QLineEdit()
        self.winners_input.setFont(QFont("San Francisco", 12))
        self.winners_input.setFixedWidth(100)
        winners_layout.addWidget(self.winners_input)
        layout.addLayout(winners_layout)

        # Button to pick winners
        pick_button = QPushButton("Pick Winners")
        pick_button.setFont(QFont("San Francisco", 12))
        pick_button.clicked.connect(self.pick_winners)
        layout.addWidget(pick_button)

        # Output area to display winners
        self.output_text = QTextEdit()
        self.output_text.setFont(QFont("San Francisco", 12))
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

    def pick_winners(self):
        names = self.get_cleaned_names()
        if not names:
            self.show_error("Please enter at least one valid name.")
            return

        try:
            number_of_winners = self.get_number_of_winners(len(names))
        except ValueError as e:
            self.show_error(str(e))
            return

        winners = self.select_random_winners(names, number_of_winners)
        self.display_winners(winners)

    def get_cleaned_names(self):
        """Get and clean the list of names from the input field."""
        names = self.names_input.toPlainText().strip()
        return [name.strip() for name in names.replace(',', '\n').splitlines() if name.strip()]

    def get_number_of_winners(self, max_winners):
        """Get and validate the number of winners input."""
        try:
            number_of_winners = int(self.winners_input.text())
            if not (0 < number_of_winners <= max_winners):
                raise ValueError(f"Please enter a valid number of winners (1-{max_winners}).")
            return number_of_winners
        except ValueError:
            raise ValueError(f"Please enter a valid number of winners (1-{max_winners}).")

    def select_random_winners(self, names, number_of_winners):
        """Select a specified number of random winners from the list of names."""
        return random.sample(names, number_of_winners)

    def display_winners(self, winners):
        """Display the list of winners in the output text area."""
        result = "\n".join(f"{i + 1}. {winner}" for i, winner in enumerate(winners))
        self.output_text.setPlainText(f"Winning Names:\n{result}")

    def show_error(self, message):
        """Show an error message dialog."""
        QMessageBox.warning(self, 'Invalid Input', message)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use a clean style that matches modern standards
    window = RaffleApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
