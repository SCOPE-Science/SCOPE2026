"""Finite-state signed matching transfer for geometric symmetries of three-row strips."""
from collections import defaultdict, deque
from functools import lru_cache
V=(0,3,6)
FULL=7

@lru_cache(None)
def pnext(pmask, mi, vert, mo):
    occupied=mi|vert|mo
    new=0
    for pin in range(8):
        if not (pmask>>pin)&1 or pin & occupied:continue
        for pv in V:
            if pv & (pin|occupied):continue
            po=FULL ^ (occupied|pin|pv)
            new |= 1<<po
    return new

def flip(mask):return ((mask&1)<<2)|(mask&2)|((mask&4)>>2)

def terminal(m,p,half=False):
    val=0
    for vm in V:
        if vm&m:continue
        p2=pnext(p,m,vm,0)
        if not p2:continue
        if half:
            q=p2 & sum(1<<t for t in range(8) if p2>>flip(t)&1)
            possibilities=((0,0),(2,1),(5,1),(7,2))
        else:
            q=p2
            possibilities=tuple((b,b.bit_count()) for b in range(8))
        score=0
        for b,orbitcount in possibilities:
            if b&(m|vm):continue
            if any((q>>t)&1 and (t&b)==b for t in range(8)):
                score+=(-1)**orbitcount
        val+=(-1)**bool(vm)*score
    return val

def build(kind):
    start=(0,1)
    seen={start:0};q=deque([start]);edges={}
    while q:
        s=q.popleft();mi,pm=s;w=defaultdict(int)
        if kind=='left':
            choices=((v,o) for v in V if not v&mi for o in range(8) if not o&(v|mi))
        else:
            choices=((0,o) for o in (0,2,5,7) if not o&mi)
        for vm,mo in choices:
            p=pnext(pm,mi,vm,mo)
            if not p:continue
            t=(mo,p)
            exponent=(bool(vm)+mo.bit_count()) if kind=='left' else (bool(mo&2)+bool(mo&5))
            w[t]+=(-1)**exponent
            if t not in seen:
                seen[t]=len(seen);q.append(t)
        edges[s]={t:c for t,c in w.items() if c}
    return start,seen,edges

def apply(edges,v):
    return {s:sum(c*v.get(t,0) for t,c in out.items()) for s,out in edges.items()}

def evaluate(start,edges,b,n):
    x=b
    for _ in range(n):x=apply(edges,x)
    return x[start]

def fib(k):
    a,b=0,1
    for _ in range(k):a,b=b,a+b
    return a

def expected(n):
    k=n//2
    row={0:1,1:0,2:-1,3:-1,4:0,5:1}[n%6]
    if n&1:
        col=(-1)**k*fib(k); half=-col
    else:
        col=(1 if k==1 else (-1)**(k-1)*fib(k-2))
        half=(-1)**k*fib(k+1)
    return row,col,half

def verify():
    start,states,edges=build('left')
    assert len(states)==24
    assert sum(map(len,edges.values()))==112
    bs=[{s:terminal(*s,half=h) for s in states} for h in (False,True)]
    # By Cayley-Hamilton for the 24 x 24 integer transfer, checking the first
    # 24 terms of the error sequence proves the recurrence for all indices.
    for b in bs:
        arr=[evaluate(start,edges,b,j) for j in range(28)]
        assert all(arr[i+4]+arr[i+2]-arr[i]==0 for i in range(24))
    rs,rstates,redges=build('row')
    rb={s:int(s[0]==0 and bool(s[1]&1)) for s in rstates}
    d=len(rstates)
    # The row trace has period six in half-width; T^6-I is the error
    # operator on the full-column transfer. T^2 acts on d states.
    rowseq=[evaluate(rs,redges,rb,2*j) for j in range(d+3)]
    assert all(rowseq[j+3]==rowseq[j] for j in range(d))
    for n in range(1,41):
        col=(-1)**n*evaluate(start,edges,bs[0],n-1)
        half=(-1)**n*evaluate(start,edges,bs[1],n-1)
        row=(-1)**n*evaluate(rs,redges,rb,2*n)
        assert (row,col,half)==expected(n),(n,(row,col,half),expected(n))
        if n>=2:
            h=fib(n-1)
            assert all((h+a*row+b*col+a*b*half)%4==0 for a in (1,-1) for b in (1,-1))
            assert all((h+a*row+b*col+a*b*half)>=0 for a in (1,-1) for b in (1,-1))
    print('left states',len(states),'transitions',sum(map(len,edges.values())))
    print('row states',d,'transitions',sum(map(len,redges.values())))
    print('Cayley-Hamilton recurrence certificate: 24 left-strip error bases and',d,'row-strip error bases PASS')
    print('Closed character formulas and nonnegative integral symmetry multiplicities through n=40 PASS')
    from direct_check import direct
    for n in (2,3,4):
        _,_,faces,t=direct(n)
        assert tuple(map(int,t))==expected(n)
        print('direct face enumeration n=',n,'faces=',faces,'PASS')

if __name__=='__main__':verify()
