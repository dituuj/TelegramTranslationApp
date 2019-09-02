from translate import Translator

class AbstractTranslator:
    def translate(self, text):
        raise NotImplementedError

class PythonTranslator(AbstractTranslator):
    def __init__(self):
        self.translator = Translator(to_lang="en", from_lang='zh')

    def translate(self, text):
        result = self.translator.translate(text)
        return result if "MYMEMORY" not in result else None

