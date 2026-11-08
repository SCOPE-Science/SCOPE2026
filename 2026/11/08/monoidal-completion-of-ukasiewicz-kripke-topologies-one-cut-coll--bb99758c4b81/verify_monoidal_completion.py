"""Exact finite-grid verification of the monoidal-completion theorem.
Run: python verify_monoidal_completion.py
No external packages required. All values are grid integers, not floating point.
"""
from itertools import product


def dot(a,b,m): return max(0,a+b-m)

def transitive(R,m,n):
    return all(dot(R[i*n+j],R[j*n+k],m)<=R[i*n+k]
               for i in range(n) for j in range(n) for k in range(n))

def open_sets(R,m,n):
    return {u for u in product(range(m+1),repeat=n)
            if all(dot(R[i*n+j],u[i],m)<=u[j]
                   for i in range(n) for j in range(n))}

def upward_sets(R,m,n):
    return {u for u in product(range(m+1),repeat=n)
            if all(u[i]<=u[j] for i in range(n) for j in range(n)
                   if R[i*n+j]==m)}

def completion(opens,m):
    s=set(opens)
    while True:
        new=set(s)
        for a in s:
            for b in s:
                new.add(tuple(dot(x,y,m) for x,y in zip(a,b)))
                new.add(tuple(min(x,y) for x,y in zip(a,b)))
                new.add(tuple(max(x,y) for x,y in zip(a,b)))
        if len(new)==len(s):return s
        s=new

def check(n,m):
    tested=0; strictly_grown=0
    for off in product(range(m+1),repeat=n*(n-1)):
        it=iter(off)
        R=tuple(m if i==j else next(it) for i in range(n) for j in range(n))
        if not transitive(R,m,n):continue
        A=open_sets(R,m,n)
        C=completion(A,m)
        S=upward_sets(R,m,n)
        assert C==S,(n,m,R,len(A),len(C),len(S),sorted(C^S)[:3])
        # Exact maximum of pointwise necessity-operator increase after completion.
        maximum=0
        for u in product(range(m+1),repeat=n):
            for i in range(n):
                box_s=min(u[j] for j in range(n) if R[i*n+j]==m)
                box_r=min(min(m,m-R[i*n+j]+u[j]) for j in range(n))
                assert 0<=box_r<=box_s
                maximum=max(maximum,box_s-box_r)
        predicted=max((r for r in R if r<m), default=0)
        assert maximum==predicted,(n,m,R,maximum,predicted)
        tested+=1
        strictly_grown+=(A!=S)
    print(f'worlds={n}, grid=0..{m}/{m}, valid_frames={tested}, proper_enlargements={strictly_grown}')

if __name__=='__main__':
    for n,m in [(1,1),(2,1),(2,2),(2,3),(2,4),(3,2),(3,3)]: check(n,m)
    for m in range(2,20):
        r=m-1
        power=r
        for k in range(2,m): power=dot(power,r,m)
        assert power>0,(m,power)
        assert dot(power,r,m)==0
    print('Grid cutoff m is sharp for every m=2..19 on an edge of degree 1-1/m.')
