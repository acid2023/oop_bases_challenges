"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""


class TextProcessor:
    def __init__(self, text):
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def summarize(self):
        return f'Total text length: {len(self.text)}'


class AdvancedTextProcessor(TextProcessor):
    def summarize(self):
        return f'Total text length: {len(self.text)}, total number of words in the text: {len(self.text.split())}'


if __name__ == '__main__':
    lena = TextProcessor('Lena is a lazy girl studying Python on weekends')
    print(lena.to_upper(), lena.summarize())

    julya = AdvancedTextProcessor('Julya is a self-motivated girl studying Python everyday')
    print(julya.to_upper(), julya.summarize())
