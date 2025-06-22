class Book:
    def __init__(self,title,authour,year):
        self.title = title
        self.authour = authour
        self.year = year
    
    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.authour}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.authour}',{self.year})"
    