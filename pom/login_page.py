class LoginPage:

    def __init__(self, page):
        self.login_button = page.locator("button:has-text('Login')")
        self.signup_button = page.locator("button:has-text('SignUp')")
