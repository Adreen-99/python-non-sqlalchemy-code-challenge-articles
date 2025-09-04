# classes/many_to_many.py
        
class Author:
    def __init__(self, name: str):
        if not isinstance(name, str):
            return "name must be of type str"
        if len(name) == 0:
            return "name must be longer than 0 characters"
        
        if len(name.strip()) == 0:
            raise Exception("Author name cannot be empty")
        self._name = name
    
        self._articles = []

    @property
    def name(self):
        return self._name
    

    @name.setter
    def title(self,value):
        if hasattr(self,"_name"):
            return "name cannot be changed after instanciation"
        if not isinstance(value,str):
            return "name must be a string"
        if (2 <= len(value) <= 16):
            return "name must be a string of more than one character"
        
        self._name = value
    def name(self, value):
        raise Exception("Author name is immutable and cannot be changed")


    def articles(self):
        [article for article in Article.all if article.author == self]
        return 
        return self._articles

    def magazines(self):
        pass
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        pass
        return Article(self, magazine, title)

    def topic_areas(self):
        pass
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name: str, category: str):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value.strip()) <= 16:
            self._name = value
        else:
            raise Exception("Magazine name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value: str):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._category = value

    def articles(self):
        pass
        return self._articles

    def contributors(self):
        pass
        return list({article.author for article in self._articles})

    def article_titles(self):
        pass
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        pass
        authors = {}
        for article in self._articles:
            authors.setdefault(article.author, 0)
            authors[article.author] += 1
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None   


class Article:
    all = []   

    def __init__(self, author, magazine, title: str):
        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be a Magazine instance")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be 5-50 characters long")

        self._author = author
        self._magazine = magazine
        self._title = title

        # link back
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)  

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, value):
        raise Exception("Title is immutable and cannot be changed")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value