# lib/classes/many_to_many.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Author name must be a string")
        if len(name.strip()) == 0:
            raise Exception("Author name cannot be empty")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name  # immutable, no setter

    @property
    def articles(self):
        return self._articles

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({mag.category for mag in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("name must be a string")
        if not (2 <= len(new_name) <= 16):
            raise Exception("name must be 2–16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise Exception("category must be a string")
        if len(new_category.strip()) == 0:
            raise Exception("category cannot be empty")
        self._category = new_category

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return [author for author in self.contributors()
                if len([a for a in self._articles if a.author == author]) > 2]


class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        # link automatically
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title  # immutable

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str):
            raise Exception("title must be a string")
        if not (5 <= len(new_title) <= 50):
            raise Exception("title must be 5–50 characters")
        if hasattr(self, "_title"):  # prevents resetting
            raise AttributeError("title cannot be changed")
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise Exception("author must be an Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise Exception("magazine must be a Magazine")
        self._magazine = new_magazine
