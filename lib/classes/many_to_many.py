class Article:

#stores article objects
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("author must be an Author")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine")
        if not isinstance(title, str):
            raise Exception("title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise Exception("title must be 5–50 characters")
        #attributes
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        if len(name.strip()) == 0:
            raise Exception("name cannot be empty")
        self.name = name

    @property
    def name(self):
        return self._name    
    
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self,magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()})

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass