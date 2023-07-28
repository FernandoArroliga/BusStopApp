# Importing the necessary kivy libraries and modules
from kivymd.app import MDApp
from kivy.lang import Builder

# Importing the application modules
from pages.home_page import HomePage
from pages.first_page import FirstPage
from pages.second_page import SecondPage
from pages.window_manager import WindowManager

# Defining the application class
class Application(MDApp):
    """
    Application main class.
    
    Parameters
    ----------
    Args: MDApp (kivymd.app.MDApp)
        Inherits from kivymd.
        
    Attributes
    ----------
    None
    """
    def build(self):
        """
        Creates and returns the application root widget.

        Returns
        -------
        manager_style: 
            The kivy file containing the window manager kivy style
        """
        # uploading the page styles
        Builder.load_file("pages/home_page.kv")
        Builder.load_file("pages/first_page.kv")
        Builder.load_file("pages/second_page.kv")
        
        # uploading the window manager style
        manager_style = Builder.load_file("style.kv")
        
        return manager_style
    
# Running the application
if __name__ == "__main__":
    my_app = Application()
    my_app.run()