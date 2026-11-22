"""Independent exhaustive count of cyclic binary no-11 reversal covers, n=2..6."""
from itertools import product

def legal(w):
    return all(not(w[i]=='1' and w[(i+1)%len(w)]=='1') for i in range(len(w)))

def covers(w,n,classes):
    return {min(t,t[::-1]) for t in (''.join(w[(i+j)%len(w)] for j in range(n)) for i in range(len(w)))} >= classes

def allwords(n):
    return {min(t,t[::-1]) for t in (''.join(a) for a in product('01',repeat=n) if '11' not in ''.join(a))}

target=[3,6,10,17,23]
for n,L in zip(range(2,7),target):
    classes=allwords(n)
    # Exhaust all circular no-11 words shorter than L: no possible witnesses.
    for ell in range(1,L):
        for bits in product('01',repeat=ell):
            w=''.join(bits)
            if legal(w) and covers(w,n,classes):
                raise AssertionError((n,ell,w))
    # Explicit witness; these independently reconstruct the minimum length.
    witness={2:'010',3:'010100',4:'0100101000',5:'01000100101010000',6:'01000010001001010100000'}[n]
    assert len(witness)==L and legal(witness) and covers(witness,n,classes)
    print(n,L,len(classes),'PASS')
