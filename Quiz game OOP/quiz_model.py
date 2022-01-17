class QuizQuestion:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
    
    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def answer(self):
        return self.__answer
    
    @answer.setter
    def answer(self, answer):
        self.__answer = answer

