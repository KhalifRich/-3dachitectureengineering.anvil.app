from ._anvil_designer import Sign_InTemplate
from anvil import open_form, alert
from anvil.tables import app_tables
from anvil.users import hash_password

class Sign_In(Sign_InTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def sign_in_clicked(self, email, password):
        # Validate email and password (e.g., check for empty fields)
        if not email or not password:
            alert("Please enter both email and password.")
            return

        # Implement authentication logic (e.g., using Anvil Users service)
        try:
            user = app_tables.users.get(email=email)
            if user['password'] == hash_password(password):
                # Successful login
                open_form('UploadForm')  # Open the home form upon successful login
            else:
                alert("Incorrect email or password.")
        except:
            alert("User does not exist.")

    def button_register_click(self, **event_args):
        # Open the registration form
        open_form('RegistrationForm')
