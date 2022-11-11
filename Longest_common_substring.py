import math
class TrieNode:
    def __init__(self):
        """
        Create a Trie Node object, storing the index of that character in term of the index of that character
        appear in the string. and there children node.
        :Input:
        :Output, return or postcondition: A trie Node
        :Time complexity: O(1), initialise the node cost constant in time
        :Aux space complexity: O(1) initialise the node cost constant in space
        """
        self.children = [None] * 29
        self.index = None
class Trie:
    def __init__(self):
        """
            init a trie, with a starting trie node
            :Input:
            :Output, return or postcondition: A suffix trie
            :Time complexity: O(1), initialise the node cost constant in time
            :Aux space complexity: O(1) initialise the node cost constant in space
        """
        self.root = self.get_node()

    def get_node(self):
        """
        create and return a trie Node
        :Input:
        :Output, return or postcondition: A trie Node
        :Time complexity: O(1), initialise the node cost constant in time
        :Aux space complexity: O(1) initialise the node cost constant in space
        """
        return TrieNode()

    def char_to_index(self, ch):
        """
        find the ascii value of that character, then calculate index
        :Input: a character
        :Output, return or postcondition: index of that character
        :Time complexity: O(1)
        :Aux space complexity: O(1)
        """
        return ord(ch) - ord('a')

    def insert(self, key ,i):
        """
        inserting the a given string(suffix) into the trie, looping through the nodes by order from the top down,
        if that character in the string already there, then take the path and go to the next node, until reach the
        end of it-self(string), if there is a differentiation, add another branch to the trie and add character as a node
        into the trie until reach the end of that string
        :Input: a string(suffix) and the starting_index of the first character compare to the original string
        argv1: a string(suffix)
        argv2: integer , starting index
        :Output, return or postcondition: adding the given suffix into the trie
        :Time complexity: O(n) where n is the length of the string
        :Aux space complexity: O(n) where n is the length of string
        """
        root = self.root
        for a in range(len(key)):
            index = self.char_to_index(key[a])
            i += 1
            if not root.children[index]:
                root.children[index] = self.get_node()
                root.children[index].index = i
            root = root.children[index]
class TreeNode:
    def __init__(self):
        """
        Create a tree Node object, storing it children, parent, starting index, length, parent string, depth
        :Input:
        :Output, return or postcondition: A tree Node
        :Time complexity: O(1), initialise the node cost constant in time
        :Aux space complexity: O(1) initialise the node cost constant in space
        """
        self.children = []
        self.parent = None
        self.starting_index = None
        self.lenght = 1
        self.parent_string = None
        self.depth = 0

    def make_parent(self, parent):
        """
        assign the parent of this node, take the input as another treenode object
        :Input: parent node(Tree_node)
        :Output, return or postcondition: assign the parent of this node, take the input as another treenode object
        :Time complexity: O(1), assigning the node cost constant in time
        :Aux space complexity: O(1) assigning the node cost constant in space
        """
        self.parent = parent

    def have_children(self, children):
        """
        assign the children of this node, take the input as another treenode object
        :Input: children node(Tree_node)
        :Output, return or postcondition: assign the children of this node, take the input as another treenode object
        :Time complexity: O(1), assigning the node cost constant in time
        :Aux space complexity: O(1) assigning the node cost constant in space
        """
        self.children.append(children)

    def return_children(self):
        """
        return the children of this node
        :Input:
        :Output, return or postcondition: return the children of this node
        :Time complexity: O(1), return the node cost constant in time
        :Aux space complexity: O(1) return the node cost constant in space
        """
        return self.children

    def return_parent(self):
        """
         return the parent of this node
        :Input:
        :Output, return or postcondition: return the parent of this node
        :Time complexity: O(1), return the node cost constant in time
        :Aux space complexity: O(1) return the node cost constant in space
        """
        return self.parent
def compress_dfs(trie, tree_node, stack):
    """
    implement and use of dfs to compress a trie in to a suffix tree by travel through every node until reach dead end.
    if you encounter a node with more then 2 children in the suffix trie, you will create n more node according to the
    amount of children that it have in the suffix trie, get the index of the children in the suffix trie to indicate
    the starting index of the new node in the suffix tree(compare to the string)
    , then you continue to traverse through the entire a tree,
    any node with one children been traverse in the suffix trie will result as a increment in the node length in the
    suffix tree, you will traverse until you reach the dead end, then stop a traverse to another branch in the suffix
    trie. And also you will record all
    :Input: a suffix trie, starting node for the suffix tree(or a suffix tree), and a stack
    argv1: a suffix trie
    argv2: suffix tree
    argv3: a stack
    :Output, return or postcondition: create a compressed form of the suffix trie(suffix tree) every node represented
                                      as [starting_index,length], which will reduce the space of the trie from
                                      O((n+m)^2) where m is the length of string 1 and m is the length of string 2, to O(m+n)
    :Time complexity: because there are (m+n)^2 of node where m,n is the length of both input string, so to traverse to the
                      entire suffix trie, it required O((n+m)^2) time -> the overall complexity will be O((m+n)^2)
                      where m is the length of string 1 and m is the length of string 2
    :Aux space complexity: it required O(m+n) space to create a new suffix tree, because after compress the trie,
                            There are exactly n+1 leaves ,There are at most n internal nodes, and every node was
                           represented as (starting_index,length)
                           -> they required O(m+n) space for create suffix tree
                            where m is the length of string 1 and n is the length of string 2
    :Overall space complexity: although Aux space complexity is O(m+n) but we still have to consider the input size which
                               is O((n+m)^2), where m is the length of string 1 and n is the length of string 2
    """

    counter = 0
    for i in range(len(trie.children)):
        if trie.children[i]  :# counting how many children does this node have
            counter += 1
    for i in range(len(trie.children)):  # loop through the trie again
        if counter > 1:                 # if this node have more then 1 children
            if trie.children[i]:        # create new node according to the number of children it have
                new_tree_node = TreeNode()
                new_tree_node.make_parent(tree_node)
                tree_node.have_children(new_tree_node)
                new_tree_node.starting_index = trie.children[i].index
                stack.append(new_tree_node)
                compress_dfs(trie.children[i], new_tree_node, stack)
        if counter <= 1:  # if there only one, then increase the length of the node
            if trie.children[i]:
                tree_node.lenght = tree_node.lenght +1
                compress_dfs(trie.children[i], tree_node, stack)
def marking_common_parent(tree ,e1):
    """
    Marking the node which is common for both string, I doing this by using dfs traverse until reach the leaf node
    then check which string does this node belonging to, is it the first string or the second string, mark it as
    1 for the fist string and 2 for the second string, after reaching the leaf, travel back up, during the travel back
    up process, mark every internal nodes it encounter as 1,2,3 which 1 is for belonging to string1, 2 for belonging to
    string 2 and 3 mean common for both string.
    :Input: a suffix tree, and the position of the indicator(for the seperation of 2 strings)
    argv1: suffix tree for both string
    argv2: the indicator
    :Output, return or postcondition: modifying the tree, mark every nodes it encounter as 1,2,3 which 1 is for
                                      belonging to string1, 2 for belonging to string 2 and 3 mean common for both string.
    :Time complexity: because we have to traverse to every node in the entire tree, where there are m+n number of nodes
                      inside the this suffix tree, so the total complexity it took to traverse all the node will be
                      -> O(m+n) where m is the length of string 1 and n is the length of string 2
    :Aux space complexity: marking the position for every nodes will cost an extra O(n+m) space, and also the space
                            complexity of the input tree is O(m+n)
                            -> the overall space complexity will be O(m+n)
                             where m is the length of string 1 and n is the length of string 2
    """
    # marking the leaf
    if tree.starting_index <= e1:
        tree.parent_string = 1
    if tree.starting_index > e1:
        tree.parent_string = 2
    # dfs traverse
    for i in tree.children:
        marking_common_parent(i ,e1)
    # marking for the internal nodes
    if len(tree.children) == 1:
        tree.parent_string = tree.children[0].parent_string
    elif len(tree.children) >1:
        a = False
        b = False
        c = False
        for i in tree.children:
            if i.parent_string == 1:
                a = True
            elif i.parent_string == 2:
                b = True
            elif i.parent_string == 3:
                c = True
        if a == True and b == False and c == False:
            tree.parent_string = 1
        elif a == False and b == True and c == False:
            tree.parent_string = 2
        elif a == True and b == True:
            tree.parent_string = 3
        elif c == True:
            tree.parent_string = 3


def combine_letter(s1, s2):
    """
    combine two input string together, and replace every space with a '{', mark the end of string 1 is '|', the
    end of string 2 as '}'
    :Input: 2 string
    argv1:  string 1
    argv2:  string 2
    :Output, return or postcondition: a combination of 2 string,replace every space with a
                                    '{', mark the end of string 1 is '|', the end of string 2 as '}'
    :Time complexity: it will took O(m+n) time to traverse through both string and replace all the space with '{'
                         where m is the length of string 1 and n is the length of string 2
    :Aux space complexity:  It will required O(m+n) space for creating a new string with the combination of string 1
                            and string 2, and the size of the input is O(m+n)
                            -> O(m+n)
                             where m is the length of string 1 and n is the length of string 2
    """
    s = s1 + '|' + s2 + '}'
    new_s = ''
    for i in range(len(s)):
        if s[i] != " ":
            new_s += s[i]
        elif s[i] == " ":
            new_s += '{'
    return new_s


def deepest(lst):
    """
    this function will find out the deepest node in the suffix tree which belong to both string 1 and string 2 by
    traverse through a list of all tree_node, checking there compare there depth and recorded the deepest one
    belong to both string, or will return None if there isn't any
    :Input: a list of all tree_node in the suffix tree
    argv1: a list of all tree_node in the suffix tree
    :Output, return or postcondition: return the deepest node which belong to both string, or None of there isn't any
    :Time complexity: traverse through all the node which will cause O(m+n) because the suffix tree we have
                        containing m+n nodes
                        -> overally complexity will be O(m+n)
                        where m is the length of string 1 and n is the length of string 2
    :Aux space complexity: the size of a nodes is really small which can counted as O(1),
                            but the input size of the list which is O(m+n) because the suffix tree we have
                        containing m+n nodes
                        -> the overall space complexity will be O(m+n)
                        where m is the length of string 1 and n is the length of string 2
    """
    deepest_num = 0
    deepest_node = None
    for i in lst:
        if i.depth > deepest_num and i.parent_string == 3:
            deepest_num = i.depth
            deepest_node = i
    return deepest_node


def depth_cal(node):
    """
    this function will traverse though the entire tree, using an implementation of dfs, calculating the depth in term
    of how far away from the source node. and adding the depth information to every nodes in the tree to the tree.
    :Input: suffix tree(the source node)
    argv1: suffix tree(the source node)
    :Output, return or postcondition: adding the depth information to every nodes in the tree to the tree
    :Time complexity: traverse through all the node which will cause O(m+n) because the suffix tree we have
                        containing m+n nodes
                        -> overall time complexity is O(m+n)
                        where m is the length of string 1 and n is the length of string 2
    :Aux space complexity: adding depth information which may cost for every nodes will cost O(m+n) extra space
                        and the input size of the list which is O(m+n) because the suffix tree we have
                        containing m+n nodes
                        -> the overall space complexity will be O(m+n)
                        where m is the length of string 1 and n is the length of string 2
    """
    for i in node.children:
        i.depth = node.depth + i.lenght
        depth_cal(i)


def longest_common_substring(node, sub, string):
    """
    Tracing back to al the parent of the given node, taking the information about the string store in all the nodes,
    combine it together to from a string by the stating index and the length of the nodes to figure out the
    string that each nodes store, add altogether.
    :Input: The deepest node of the tree with have common parent in the tree, a empty string to add all the substring
    into, and the combination of string1 and string2
    argv1:The deepest node of the tree with have common parent in the tree
    argv2: a empty string to add all the substring into
    argv3: and the combination of string1 and string2
    :Output, return or postcondition: return longest common substring in the entire suffix tree, or a empty string
    if there isn't any
    :Time complexity: worst case when every nodes in the suffix tree connect together and, our deepest node is
                      at the end of the suffix tree, then we have to traverse through every node to the start
                      still because the longest common substring will always < length of both string combine
                      so at most we are doing O(m+n) iteration
                      -> overally complexity will be O(m+n)
                        where m is the length of string 1 and n is the length of string 2
    :Aux space complexity: longest_common_substring as most take O(m+n) space and the input string take up to
                            O(m+n) space
                            -> overall space complexity O(m+n)
                            where m is the length of string 1 and n is the length of string 2
    """
    while node.parent != None:
        sub = string[(node.starting_index - 1):(node.starting_index - 1 + node.lenght)] + sub
        node = node.parent
    return sub


def build_suffix_tree(string):
    """
    Building a suffix tree for a given string, starting with building a suffix trie by using Trie class, then
    compress the trie into tree by calling compress_dfs() function and store all the node in the Tree_node class,
    after that marking the parent for all the nodes in the tree by using marking_common_parent() function
    , and adding the depth for each node in the tree by calling depth_cal() function. Also create a list to store
    all the Tree_node object in. and deleting the trie after making the new compress tree to reduce the space complexity
    :Input: a string which is a combination of string1 and string 2
    argv1: a string which is a combination of string1 and string 2
    :Output, return or postcondition:
    :Time complexity: the biggest time complexity of this function is making the trie which cost : O((m+n)^2)
                        where m is the length of string 1 and n is the length of string 2
    :Aux space complexity: the biggest space complexity of this function is making the tree which cost : O(m+n)
                        where m is the length of string 1 and n is the length of string 2
                        because we already deleting the trie so now the biggest space will be the tree.
    """
    # building the suffix trie
    trie = Trie()
    for i in range(len(string)):
        ## i-1 for starting at 0
        trie.insert(string[i:len(string)], i)
    # initialise the suffix tree
    tree_node = TreeNode()
    # initialise the source node index at 0
    tree_node.starting_index = 0
    stack = []
    # compressing the trie into a new tree
    compress_dfs(trie.root, tree_node, stack)
    e1 = string.index('|') + 1
    # marking the parent for all the node
    marking_common_parent(tree_node, e1)
    # calculate depth of every node in the tree
    depth_cal(tree_node)
    del trie
    return stack


def final_string(a):
    """
    After getting the string from longest_common_substring(), re-modify it, change all '{' back in to space
    by traverse through the string fromm longest_common_substring(), append all the character into new string, every
    time see '{', instead of append '{', we change it to a ' '. and return the final string.
    :Input: a string to modify
    argv1: a string to modify
    argv2:
    :Output, return or postcondition: a string which already removed '{' and replace with ' '
    :Time complexity: traverse through the entire string in the worst case where the len(a) = len of either string 1
    or string 2
    ->so the complexity will be O(n) where n is the length of the bigger string

    :Aux space complexity: the string input will have the size = to either string 1 or string 2, and the final string
    also requried the same amount of space
                            -> so the overall space complexity will be O(n)
                            where n is the length of the bigger string.
    """
    sub = ''
    for i in a:
        if i == '{':
            sub += ' '
        else:
            sub += i
    return sub


def round(number):
    """
    taking the given number, round up if the number decimal's part is >= .5
    round down if the given number decimal's part < .5
    :Input: a number
    argv1: a integer number
    :Output, return or postcondition: a rounded to the nearest integer,round up if the number decimal's part is >= .5
    round down if the given number decimal's part < .5
    :Time complexity: time complexity to execute this is O(1)
    :Aux space complexity: the only space this function took is the space from the number, which O(1) in this case
    """
    if number - math.floor(number) < 0.5:
        return math.floor(number)
    return math.ceil(number)


def compare_subs(submission1, submission2):
    """
    The function findings with three elements:
    -the longest common substring between submission1 and submission2
    -the similarity score for submission1, expressed as the percentage of submission1 that belongs to the longest common
     substring (rounded to the nearest integer1),
    - And the similarity score for submission2,expressed as the percentage of submission2 that belongs to the longest
    common substring (rounded to the nearest integer)
    firstly, we combining 2 input string together by combine_letter(submission1, submission2)
    then build a tree and received a list of all the tree nodes by using build_suffix_tree(),
    find the deepest node in the tree which belong to both submission1 and submission2 by deepest(),
    trace back the deepest node to print out all the string using longest_common_substring()
    then reformat the string using final_string(), and finally calculate similarity score with the help of round()
    :Input: taking 2 string that we want to find
    argv1: submission1 : string 1
    argv2: submission2 : string 2
    :Output, return or postcondition: the function will return a list of three elements:
    -the longest common substring between submission1 and submission2
    -the similarity score for submission1, expressed as the percentage of submission1 that belongs to the longest common
     substring (rounded to the nearest integer1),
    - And the similarity score for submission2,expressed as the percentage of submission2 that belongs to the longest
    common substring (rounded to the nearest integer)
    ** I will analyze the complexity of 2 part in this function, first part is building the tree, second part is
    computing the comparison between the two strings **

    First part (building the suffix tree):
    :Time complexity: the biggest time complexity of this part is making the trie which cost : O((m+n)^2)
                        where m is the length of string 1 and n is the length of string 2
    :Aux space complexity: the biggest space complexity of this function is making the tree which cost : O(m+n)
                        where m is the length of string 1 and n is the length of string 2
                        because we already deleting the trie so now the biggest space will be the tree.
    Second part (computing the comparison between the two strings):
    :Time complexity: all the computing the comparison function which are deepest() and longest_common_substring
                        all run in O(m+n) time complexity
                        -> overall time complexity is O(m+n)

    :Aux space complexity:all the computing the comparison function which are deepest() and longest_common_substring
                         all required O(m+n) space
                        -> overall time complexity is O(m+n)

    """
    # combining 2 input string together
    string = combine_letter(submission1, submission2)
    # build a tree and received a list of all the tree nodes
    stack = build_suffix_tree(string)
    # find the deepest node in the tree which belong to both submission1 and submission2
    deepest_node = deepest(stack)
    # init a subsequence string
    sub = ''
    # if there is a  deepest node in the tree which belong to both submission1 and submission2
    # then find th string
    if deepest_node:
        # trace back to print out all the string
        sub = longest_common_substring(deepest_node, sub, string)
        # reformat the string
        sub = final_string(sub)
    # calculate the percentage for similarity score that each longest_common_substring for each submission
    per1 = round(len(sub) / len(submission1) * 100)
    per2 = round(len(sub) / len(submission2) * 100)

    return [sub, per1, per2]


if __name__ == '__main__':
    print(compare_subs('the quick brown fox jumped over the lazy dog', 'my lazy dog has eaten my homework'))