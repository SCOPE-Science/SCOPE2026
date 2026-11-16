"""Exact integer checks for the signed independence sums of squared cycles."""
from itertools import product

IDENTITY=(1,0,0,0,1,0,0,0,1)

def step(a,t):
    return tuple(v for i in range(3) for v in
                 (a[3*i]+a[3*i+2],t*a[3*i],a[3*i+1]))

def matmul(a,b):
    return tuple(sum(a[3*i+k]*b[3*k+j] for k in range(3))
                 for i in range(3) for j in range(3))

def product_matrix(word):
    a=IDENTITY
    for t in word:
        a=step(a,t)
    return a

def signed_sum(n,negative_indices):
    word=[-1 if i in negative_indices else 1 for i in range(n)]
    a=product_matrix(word)
    return a[0]+a[4]+a[8]

def independently_count(n,negative_indices):
    total=0
    for mask in range(1<<n):
        if any((mask>>i)&1 and ((mask>>((i+1)%n))&1 or (mask>>((i+2)%n))&1)
               for i in range(n)):
            continue
        parity=sum((mask>>i)&1 for i in negative_indices)%2
        total+=(-1 if parity else 1)
    return total

ZERO_BASES={3:(0,1),5:(0,1,2),10:(0,2,4),12:(0,2,4),13:(0,2,4)}
POSITIVE_BASES={
 3:(0,),4:(0,1),5:(0,1),6:(0,1),7:(0,1,3),8:(0,1,3),
 9:(0,2,4),10:(0,1,2,5),11:(0,2,4),12:(0,1,2,5),
 13:(0,1,2,5),14:(0,2,4),15:(0,2,4),16:(0,2,4)
}
EXPECTED_GAPS={3:2,4:1,5:2,6:2,7:1,8:1,9:1,10:2,11:1,12:2,13:4,14:1,15:1,16:1}

for n,neg in ZERO_BASES.items():
    assert signed_sum(n,neg)==0,(n,neg)
for n,neg in POSITIVE_BASES.items():
    assert abs(signed_sum(n,neg))==EXPECTED_GAPS[n],(n,neg)

# Independent constructions: direct graph enumeration versus transfer traces.
for n in range(3,11):
    for bitmask in range(1<<n):
        neg=tuple(i for i in range(n) if bitmask & (1<<i))
        assert signed_sum(n,neg)==independently_count(n,neg)

# An independent full Hadamard transform of all squared-cycle support indicators.
for n in range(3,17):
    N=1<<n
    a=[0]*N
    for mask in range(N):
        if all(not ((mask>>i)&1 and (((mask>>((i+1)%n))&1) or ((mask>>((i+2)%n))&1)))
               for i in range(n)):
            a[mask]=1
    h=1
    while h<N:
        for b in range(0,N,2*h):
            for j in range(b,b+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    gap=min(abs(v) for v in a if v)
    assert gap==EXPECTED_GAPS[n],(n,gap)
    assert (0 in a)==(n%14 in {3,5,10,12,13})

# The finite transfer identities used to obtain global period and congruences.
a=IDENTITY
for _ in range(7):
    a=step(a,1)
assert tuple(v%2 for v in a)==IDENTITY
for _ in range(7):
    a=step(a,1)
assert tuple(v%4 for v in a)==IDENTITY

# The path-square recurrence state matrix is 7-periodic modulo two.
r=(1,0,1,1,0,0,0,1,0)
a=IDENTITY
for _ in range(7):
    a=matmul(a,r)
assert tuple(v%2 for v in a)==IDENTITY

# All fourteen distinct 7-sign involution words yield 14-sign identity blocks.
involution_words=[]
for s in product((1,-1),repeat=7):
    b=product_matrix(s)
    if matmul(b,b)==IDENTITY:
        involution_words.append(s)
assert len(involution_words)==14
assert len(set(involution_words))==14
for s in involution_words:
    assert product_matrix(s+s)==IDENTITY
    for n,neg in ZERO_BASES.items():
        base=[-1 if i in neg else 1 for i in range(n)]
        assert sum(product_matrix(tuple(base)+s+s)[i] for i in (0,4,8))==0
    for n,neg in POSITIVE_BASES.items():
        base=[-1 if i in neg else 1 for i in range(n)]
        assert sum(product_matrix(tuple(base)+s+s)[i] for i in (0,4,8))==signed_sum(n,neg)

# Modulo-four obstruction for the two 14-residue classes with even marginals.
for n in (6,13,20,27,34,41):
    unweighted=signed_sum(n,())
    expected=(2 if n%14==6 else 0)
    assert unweighted%4==expected,(n,unweighted)
    p=[1,2,3]
    for j in range(3,n-4):
        p.append(p[j-1]+p[j-3])
    assert p[n-5]%2==0

print('CYCLE_SQUARE_FOURIER_EXACT_PASS: direct n=3..10; all Walsh n=3..16; 14 involution blocks; modular certificates')
