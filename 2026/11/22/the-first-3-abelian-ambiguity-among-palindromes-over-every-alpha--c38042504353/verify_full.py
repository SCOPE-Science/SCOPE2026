"""Exhaustive exact first-collision check for palindromic 3-gram reconstruction."""
from collections import Counter, defaultdict
from itertools import product, combinations

Q = 5
alphabet = range(Q)

def palindrome(half, n):
    return half + (half[::-1] if n % 2 == 0 else half[-2::-1])

def full_profile(w):
    return tuple(tuple(sorted(Counter(tuple(w[i:i+k]) for i in range(len(w)-k+1)).items()))
                 for k in range(1, min(3,len(w))+1))

def predicted(q):
    pairs = set()
    for a in range(q):
        for b in range(q):
            if a == b:
                continue
            s = (a,a,a,b,a,a,b,a,a,a)
            t = (a,a,b,a,a,a,a,b,a,a)
            pairs.add(frozenset((s,t)))
        for b,c in combinations((x for x in range(q) if x != a), 2):
            s = (a,a,b,c,a,a,c,b,a,a)
            t = (a,a,c,b,a,a,b,c,a,a)
            pairs.add(frozenset((s,t)))
    return pairs

def main():
    total_words = 0
    for n in range(1,11):
        classes = defaultdict(list)
        for half in product(alphabet, repeat=(n+1)//2):
            w = palindrome(half,n)
            classes[full_profile(w)].append(w)
            total_words += 1
        sizes = Counter(map(len, classes.values()))
        if n < 10:
            assert sizes == {1: Q**((n+1)//2)}, (n, sizes)
        else:
            assert sizes == {1: Q**5-2*50,2:50}, sizes
            actual = {frozenset(words) for words in classes.values() if len(words)>1}
            assert actual == predicted(Q)
            assert len(actual)==50
            assert len(classes)==Q**5-50
    for q in range(2,Q+1):
        pairs=predicted(q)
        assert len(pairs)==q*q*(q-1)//2
        assert all(all(w==w[::-1] for w in p) for p in pairs)
        assert all(len({full_profile(w) for w in p})==1 for p in pairs)
    print('VERIFY_FULL_OK', 'alphabet=5','lengths=1..10', 'words=',total_words,
          'length10_pairs=50','two_isomorphism_families')
if __name__=='__main__':main()
