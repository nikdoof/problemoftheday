# Vigenere Cipher brute forcer
#
# Solution to http://www.problemotd.com/problem/vigenere-cipher/
# By Andrew Williams (github.com/nikdoof)
 
import itertools, string
 
alpha = string.ascii_lowercase
 
def vigenere_encode(text, key):
    k = key * (int(len(text) / len(key)) + 1)
    k = k[:len(text)]
    return ''.join([alpha[(alpha.index(x) + alpha.index(y)) % 26] for x, y in zip(text, k)])
 
 
def vigenere_decode(cypher, key):
    k = key * (int(len(cypher) / len(key)) + 1)
    k = k[:len(cypher)]
    return ''.join([alpha[(alpha.index(x) - alpha.index(y)) % 26] for x, y in zip(cypher, k)])
 
 
freq = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 
    'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 
    'R': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 
    'F': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 
    'J': 0.07
}
 
def count_letters(s):
    count = dict([(c, 0) for c in alpha])
    for l in s:
        count[l] += 1
    return count
 
def score_letters(s):
    score = 0
    c = count_letters(s)
    for x in c:
        if x.upper() in freq:
            score += (c[x] * freq[x.upper()])
    return score
 
if __name__ == '__main__':
    # Self test
    print 'Encode Test Passed? {}'.format(vigenere_encode('todayismybirthday', 'reddit') == 'KSGDGBJQBEQKKLGDG'.lower())
    print 'Decode Test Passed? {}'.format(vigenere_decode('KSGDGBJQBEQKKLGDG'.lower(), 'reddit') == 'todayismybirthday')
 
    # Source
    ct = 'ZEJFOKHTMSRMELCPODWHCGAW'.lower()
 
    # Process the keys and store the results
    res = []
    for i in range(1,5):
        for p in itertools.product(string.ascii_lowercase, repeat=i):
            c = 0
            p = ''.join(p)
            dec = vigenere_decode(ct, p)
            res.append((p, dec, score_letters(dec)))
 
    # Show the top 200 scoring results
    for x, y, z in sorted(res, key=lambda tup: tup[2])[-200:]:
        print '{} - {} ({})'.format(x, y, z)
