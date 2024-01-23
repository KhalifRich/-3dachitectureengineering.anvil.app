from ._anvil_designer import UploadTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from anvil import js

class Upload(UploadTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    {
    'Upload':forms.FileInputs(attrs = {'accept':'.fbx, .stl, .iges, .obj, .collada, .step, .3ds'})
    }
    pass

  def subscribe_click(self, **event_args):
    """This method is called when the button is clicked"""
    def subscribe_button_click(self, **event_args):
        stripe_token = js.stripe.createToken(self.card_number, {})
        amount = self.amount_box.text
        result = anvil.server.call('process_payment', stripe_token['token']['id'], amount)
        if 'client_secret' in result:
            self.show_success_message()
        else:
            self.show_error_message(result)

    def show_success_message(self):
        # Implement success message handling
        pass

    def show_error_message(self, error):
        # Implement error message handling
        pass

    pass
