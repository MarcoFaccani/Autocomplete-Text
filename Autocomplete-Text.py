# Helper function
def find_suffixes(node, output, word=""):
    
    # note: "and len(word)"" is needed so to not add an empty string when input is same as a single word
    if node is None or len(node.children) == 0 and len(word) > 0: 
        output.append(word)
        return
    elif node.is_word and len(word) > 0:
        output.append(word)
    
    for key in node.children.keys():
        find_suffixes(node.children[key], output, word+key)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        self.children[char] = TrieNode() #add to node a new key:value (char : TrieNode) 
        
    def suffixes(self, suffix = ''):
        output = []
        find_suffixes(self, output)
        print(output)
        return output
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Adds a word to the Trie
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.insert(char) # add char: { }
            current = current.children[char]

        current.is_word = True

    # Find the Trie node that represents this prefix
    def find_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char in current.children:
                current = current.children[char]
            else:
                break
            
        # Edge case
        if current == self.root and len(prefix) > 0:
            return None

        return current # node with specific prefix




# ========== Tests definitions and execution ==========

MyTrie = Trie()
wordList = [
            "ant", "anthology", "antagonist", "antonym", 
            "fun", "function", "factory", 
            "trie", "trigger", "trigonometry", "tripod"
            ]
for word in wordList:
    MyTrie.insert(word)


MyTrie.find_prefix("a").suffixes() #expect ['nt', 'nthology', 'ntagonist', 'ntonym']
MyTrie.find_prefix("f").suffixes() #expect ['un', 'unction', 'actory']
MyTrie.find_prefix("t").suffixes() #expect ['rie', 'rigger', 'rigonometry', 'ripod']

MyTrie.find_prefix("ant").suffixes() #expect ['hology', 'agonist', 'onym']
MyTrie.find_prefix("fun").suffixes() #expect ['ction']
MyTrie.find_prefix("trie").suffixes() #expect [] 

MyTrie.find_prefix("").suffixes() #expect all words contained: ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
print(MyTrie.find_prefix("z")) #expect None; (there are no words that begin with 'z', so I chose to return None in these cases)

