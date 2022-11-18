class Trie:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, word: str) -> None:
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        curr = self

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        