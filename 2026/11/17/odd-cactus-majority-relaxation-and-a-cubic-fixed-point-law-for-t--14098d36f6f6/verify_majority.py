"""Independent labelled-bit brute-force dynamics for vertex-glued triangular chains.
Run: python verify_majority.py
"""
from itertools import product


def neighbours(n):
    N=[set() for _ in range(2*n+1)]
    for i in range(1,n+1):
        for a,b in ((i-1,i),(i-1,n+i),(i,n+i)):
            N[a].add(b);N[b].add(a)
    return [tuple(a) for a in N]


def update(x,N):
    z=0
    for v,neighbours in enumerate(N):
        ones=sum((x>>w)&1 for w in neighbours)
        current=(x>>v)&1
        if 2*ones>len(neighbours): new=1
        elif 2*ones<len(neighbours): new=0
        else: new=current
        z |= new<<v
    return z


def recurrence(n):
    p=[0,2,6,12]
    for j in range(4,n+1):p.append(p[-1]+2*p[-2]+p[-3])
    return p[n]


def test():
    total=0
    for n in range(1,9):
        adj=neighbours(n)
        fixed=return2=0
        for x in range(1<<(2*n+1)):
            y=update(x,adj)
            fixed+=(y==x)
            return2+=(update(y,adj)==x)
        predicted=recurrence(n)
        assert fixed==return2==predicted,(n,fixed,return2,predicted)
        total+=1<<(2*n+1)
        print('n=',n,'vertices=',2*n+1,'fixed=',fixed,'two-step=',return2,'expected=',predicted)
    print('PASS total labelled initial configurations examined:',total)

if __name__=='__main__':test()
