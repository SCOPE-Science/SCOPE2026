from fractions import Fraction as Q

def xnodes(k):
    return [Q(1,2**(k+1-j)) for j in range(k+1)] + [1-Q(1,2**j) for j in range(2,k+1)]

def maps(k,x):
    delta=Q(1,2**(k+2))
    c=4*delta
    def f0(x): return x/2 if x < Q(1,2)+delta else 2*x-1
    def f1(x): return 2*x if x < Q(1,2)-delta else (x+1)/2
    assert c/2<=x<1-c/2
    if x<c: return (f1(x),f1(x))
    if x<1-c: return (f0(x),f1(x))
    return (f0(x),f0(x))

ncheck=0
for k in range(2,151):
    X=xnodes(k)
    assert len(X)==2*k and len(set(X))==2*k
    idx={x:i for i,x in enumerate(X)}
    weights=[Q(1,2) if i in (0,2*k-1) else Q(1) for i in range(2*k)]
    weights=[w/Q(2*k-1) for w in weights]
    assert sum(weights)==1
    incoming=[Q(0) for _ in X]
    for i,x in enumerate(X):
        h0,h1=maps(k,x)
        expected=(1,1) if i==0 else ((2*k-2,2*k-2) if i==2*k-1 else (i-1,i+1))
        assert (idx[h0],idx[h1])==expected,(k,i,h0,h1,expected)
        incoming[idx[h0]]+=weights[i]/2
        incoming[idx[h1]]+=weights[i]/2
        ncheck+=1
    assert incoming==weights
    assert weights[0]==weights[-1]==Q(1,2*(2*k-1))
print('PASS: exact rational graph, transition, and invariant law; k=2..150; node states:',ncheck)

# Direct physical-time two-sided dyadic walk, independent of the accelerated core.
def lattice(j):
    return Q(2)**(j-1) if j<=0 else 1-Q(1,2**(j+1))
for delta in [Q(1,6),Q(1,8),Q(1,16),Q(1,100),Q(1,1000)]:
    for j in range(-70,71):
        x=lattice(j)
        physical0=x/2 if x<Q(1,2)+delta else 2*x-1
        physical1=2*x if x<Q(1,2)-delta else (x+1)/2
        assert physical0==lattice(j-1)
        assert physical1==lattice(j+1)
print('PASS: exact physical dyadic left/right walk, five perturbations and 705 nodes')
