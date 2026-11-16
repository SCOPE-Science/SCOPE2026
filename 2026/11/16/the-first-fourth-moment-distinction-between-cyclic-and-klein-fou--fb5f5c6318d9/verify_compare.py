"""Exact finite census of the first cyclic/Klein spectral divergence.
Run: python verify_compare.py. Uses only standard-library integer arithmetic.
Every onto word and every Fourier coefficient is included, not sampled.
"""
from collections import Counter
from itertools import product

EXPECTED = {
 4: {0:192,8:60,24:4},
 5: {0:828,16:90,32:60,48:45,240:1},
}
EXPECTED_CYCLIC_6={0:3072,8:510,24:110,40:192,88:15,104:150,120:1,200:45,1560:1}
EXPECTED_KLEIN_6={0:3072,8:540,40:270,88:45,104:120,120:3,200:45,1560:1}

H4=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1))
# We avoid floating numbers below: Gaussian integers are (real, imaginary).
C4_PAIRS=(
 ((1,0),(1,0),(1,0),(1,0)),
 ((1,0),(0,-1),(-1,0),(0,1)),
 ((1,0),(-1,0),(1,0),(-1,0)),
 ((1,0),(0,1),(-1,0),(0,-1)),
)

def transform(n, cyclic):
    N=4**n
    data=[(0,0)]*N
    for word in product(range(4),repeat=n):
        if len(set(word))==4:
            key=sum(x*4**i for i,x in enumerate(word))
            data[key]=(1,0)
    local=C4_PAIRS if cyclic else tuple(tuple((v,0) for v in row) for row in H4)
    # Tensor-power Fourier transform, one four-coordinate DFT at a time.
    for coordinate in range(n):
        stride=4**coordinate
        for base in range(0,N,4*stride):
            for offset in range(stride):
                ix=[base+offset+j*stride for j in range(4)]
                v=[data[j] for j in ix]
                for k in range(4):
                    rr=ii=0
                    for t in range(4):
                        a,b=local[k][t]
                        x,y=v[t]
                        rr+=a*x-b*y
                        ii+=a*y+b*x
                    data[ix[k]]=(rr,ii)
    hist=Counter()
    for r,i in data:
        assert i==0 # On the balanced support, conjugation symmetry makes all coefficients real.
        hist[abs(r)]+=1
    return dict(hist),data

def check():
 for n in (4,5,6):
    H,dH=transform(n,False)
    C,dC=transform(n,True)
    assert H==(EXPECTED_KLEIN_6 if n==6 else EXPECTED[n]),(n,H)
    assert C==(EXPECTED_CYCLIC_6 if n==6 else EXPECTED[n]),(n,C)
    assert sum(H.values())==sum(C.values())==4**n
    onto=4**n-4*3**n+6*2**n-4
    assert dH[0]==dC[0]==(onto,0)
    for data in (dH,dC):
        assert sum(r*r+i*i for r,i in data)==4**n*onto
    fourthH=sum(v*abs(k)**4 for k,v in H.items())
    fourthC=sum(v*abs(k)**4 for k,v in C.items())
    if n in (4,5): assert fourthH==fourthC and H==C
    else:
        assert fourthC==6013593845760 and fourthH==6012461383680
        assert fourthC-fourthH==1132462080
        assert H!=C
    print(f'n={n} onto={onto} rank={sum(v for k,v in C.items() if k)} cyclic_fourth={fourthC} klein_fourth={fourthH} difference={fourthC-fourthH}: PASS')
if __name__=='__main__':check()
