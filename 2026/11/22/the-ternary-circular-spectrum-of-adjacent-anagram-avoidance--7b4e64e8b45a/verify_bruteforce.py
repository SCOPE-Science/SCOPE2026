"""Independent direct exhaustive enumeration of ternary indexed periodic words.
Run: python3 verify_bruteforce.py . No third-party packages required.
"""
from itertools import product
from math import gcd
from collections import Counter
expected=[0,0,6,60,90,216,462,1332,3282,7980,18876]
for n,want in enumerate(expected,start=1):
    good=[]
    for w in product(range(3),repeat=n):
        if all(sorted((w[i%n],w[(i+1)%n]))!=sorted((w[(i+2)%n],w[(i+3)%n])) for i in range(n)):
            good.append(w)
    assert len(good)==want,(n,len(good),want)
    if n<=9:
        necklaces={min(w[i:]+w[:i] for i in range(n)) for w in good}
        periods={w:min(d for d in range(1,n+1) if n%d==0 and w==w[d:]+w[:d]) for w in necklaces}
        # Number of primitive necklaces = primitive indexed words / n
        primitive=sum(1 for w in good if all(w!=w[d:]+w[:d] for d in range(1,n) if n%d==0))
        assert sum(v==n for v in periods.values())==primitive//n
    print('n',n,'indexed',len(good))
print('Exhaustive direct word comparison OK')
