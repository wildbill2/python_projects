class User():
    """Model for user profiles."""

    def __init__(self, first_name, last_name, location, job_title):
        """Initialization for first and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.job_title = job_title
        self.login_attempts = 0

    
    def describe_user(self):
        print("User Profile:")
        print("\t -First Name: " + self.first_name.title())
        print("\t -Last Name: " + self.last_name.title())
        print("\t -Location: " + self.location.title())
        print("\t -Job Title: " + self.job_title.title())

    
    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title() + ", how are you today?")


    def get_login_attempts(self):
        print("Login Attempts: " + str(self.login_attempts))


    def increment_login_attempts(self):
        """Increases log in attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts back to 0."""
        self.login_attempts = 0


class AdminUser(User):
    
    def __init__(self, first_name, last_name, location, job_title):
        """Initialize attributes of the parent class."""
        """Then initialize attributes of the child class."""

        super().__init__(first_name, last_name, location, job_title)
        self.permissions = 'root'

    def get_permissions(self):
        print("This user has " + self.permissions + " access.")

    

    


user1 = User("brian", "billock", "maryland", "isso")
user2 = User("angela", "billock", "maryland", "human resources")
user3 = User("olivia", "billock", "maryland", "developer")
user4 = AdminUser("brian", "billock", "maryland", "system administrator")


user4.describe_user()
user4.get_permissions()
