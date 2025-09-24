class Note:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

    def __str__(self):
        return (f"{self.title} \t {self.date}"
                f"{self.content} \n"
                )

    def changeContent(self, content):
        self.content = content

    def changeTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def getContent(self):
        return self.content

    def getDate(self):
        return self.date