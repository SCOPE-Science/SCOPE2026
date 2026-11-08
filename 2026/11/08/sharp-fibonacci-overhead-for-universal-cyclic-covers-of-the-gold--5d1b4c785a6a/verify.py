"""Finite checks of constrained cyclic universal covers, using only Python's standard library."""
from collections import Counter, defaultdict
from itertools import product

def fib(k):
    a,b=0,1
    for _ in range(k): a,b=b,a+b
    return a

def allowed(k):
    return [''.join(p) for p in product('01',repeat=k) if '11' not in ''.join(p)]

def pot(v):
    return v.rfind('1')+1

def inspect(n):
    E=allowed(n)
    V=allowed(n-1)
    extra=['0'+u+'0' for u in allowed(n-2) if '1' in u]
    assert len(E)==fib(n+2)
    assert len(extra)==fib(n)-1
    outgoing=Counter();incoming=Counter()
    base_drop=0
    for e in E:
        a,b=e[:-1],e[1:]
        outgoing[a]+=1;incoming[b]+=1
        d=pot(a)-pot(b)
        assert d<=1
        base_drop+=d
    assert base_drop==-(fib(n)-1)
    for e in extra:
        outgoing[e[:-1]]+=1;incoming[e[1:]]+=1
    assert all(outgoing[v]==incoming[v] for v in V)
    return E,extra

def euler_cycle(n):
    E,extra=inspect(n)
    out=defaultdict(list)
    for e in E+extra:
        out[e[:-1]].append((e[1:],e))
    root='0'*(n-1)
    stack=[(root,None)]; circuit=[]
    while stack:
        v,_=stack[-1]
        if out[v]:
            w,e=out[v].pop()
            stack.append((w,e))
        else:
            _,e=stack.pop()
            if e is not None: circuit.append(e)
    circuit.reverse()
    assert len(circuit)==len(E)+len(extra)
    assert all(circuit[i][1:]==circuit[(i+1)%len(circuit)][:-1] for i in range(len(circuit)))
    s=''.join(e[-1] for e in circuit)
    cyc=[(s+s)[i:i+n] if i+n<=2*len(s) else (s*((i+n)//len(s)+1))[i:i+n] for i in range(len(s))]
    assert len(s)==fib(n+2)+fib(n)-1
    assert '11' not in s+s[:1]
    assert Counter(cyc)==Counter(E+extra)
    return s

def main():
    for n in range(2,13):
        s=euler_cycle(n)
        print('n',n,'length',len(s),'required',fib(n+2),'repeated',fib(n)-1)
    print('VERIFY_OK')

if __name__=='__main__':main()
