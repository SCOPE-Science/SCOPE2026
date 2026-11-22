"""Finite sanity checks for run-capped modular scattered 001 languages."""
from collections import deque, defaultdict
from itertools import product

def period(m):
    return m if m%2 else 2*m

def charge(x,m):
    return (x*(x-1)//2)%m

def step(s,c,m,r):
    if s is None:return None
    z,t,j=s
    if c=='0':return ((z+1)%period(m),t,0)
    if j==r-1:return None
    return (z,(t+charge(z,m))%m,j+1)

def process(s,w,m,r):
    for c in w:s=step(s,c,m,r)
    return s

def accepts(s):return s is not None and s[1]==0

def direct(w,m,r):
    if '1'*r in w:return False
    z=t=0
    for c in w:
        if c=='0':z+=1
        else:t+=z*(z-1)//2
    return t %m ==0

def exact_min(m,r):
    P=period(m)
    all_states=[(z,t,j) for z in range(P) for t in range(m) for j in range(r)]+[None]
    index={s:i for i,s in enumerate(all_states)}
    transitions=[[index[step(s,c,m,r)] for c in '01'] for s in all_states]
    st=index[(0,0,0)]; seen={st};stack=[st]
    for v in stack:
        for w in transitions[v]:
            if w not in seen:seen.add(w);stack.append(w)
    acc={index[s] for s in all_states if accepts(s)}
    blocks=[seen&acc,seen-acc]
    blocks=[b for b in blocks if b]
    while True:
        bix={s:i for i,b in enumerate(blocks) for s in b};new=[]
        for b in blocks:
            splits=defaultdict(set)
            for v in b:splits[tuple(bix[w] for w in transitions[v])].add(v)
            new+=list(splits.values())
        if len(new)==len(blocks):break
        blocks=new
    return len(seen),len(blocks)

def witness(s1,s2,m,r):
    P=period(m)
    z,t,j=s1;Z,T,J=s2
    if j != J:
        if j>J:
            s1,s2=s2,s1
            z,t,j=s1;Z,T,J=s2
        ell=r-J
        a=next(a for a in range(1,P+1) if (z+a)%P==2%P)
        q=(-t-ell*charge(z,m))%m
        w='1'*ell+'0'*a+('1'+'0'*P)*q
        assert accepts(process(s1,w,m,r)) and not accepts(process(s2,w,m,r))
        return w
    if z==Z:
        assert t!=T
        a=next(a for a in range(1,P+1) if (z+a)%P==2%P)
        q=(-t)%m
        w='0'*a+('1'+'0'*P)*q
        assert accepts(process(s1,w,m,r)) != accepts(process(s2,w,m,r))
        return w
    B0=next(B for B in range(1,P+1) if (z+B)%P==2%P)
    c=charge(Z+B0,m)
    b=next(b for b in range(1,P+1) if (charge(Z+b,m)-charge(z+b,m)*c)%m)
    B=B0
    while B<=b:B+=P
    for u in (0,1):
        q=(-t-u*charge(z+b,m))%m
        w='0'*b+('1'+'0'*P)*u+'0'*(B-b)+('1'+'0'*P)*q
        if accepts(process(s1,w,m,r))!=accepts(process(s2,w,m,r)):
            return w
    raise AssertionError((s1,s2,m,r))

def run():
    cases=0; total_states=0; pairs=0; direct_cases=0
    for m in range(2,13):
        for r in range(2,6):
            reach,minimal=exact_min(m,r)
            expected=r*m*period(m)+1
            assert (reach,minimal)==(expected,expected),(m,r,reach,minimal,expected)
            cases+=1;total_states+=reach
    for m in range(2,6):
        for r in range(2,5):
            P=period(m)
            states=list(product(range(P),range(m),range(r)))
            for i,a in enumerate(states):
                for b in states[i+1:]:
                    w=witness(a,b,m,r)
                    assert accepts(process(a,w,m,r))!=accepts(process(b,w,m,r))
                    pairs+=1
            for length in range(0,13):
                for tup in product('01',repeat=length):
                    w=''.join(tup)
                    assert direct(w,m,r)==accepts(process((0,0,0),w,m,r))
                    direct_cases+=1
    print('PASS',cases,'fully minimized automata,',total_states,'states,',pairs,'constructive distinguishability pairs,',direct_cases,'direct word comparisons')
if __name__=='__main__':run()
