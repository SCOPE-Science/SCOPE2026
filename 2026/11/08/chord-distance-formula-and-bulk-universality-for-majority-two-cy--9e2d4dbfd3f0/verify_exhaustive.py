#!/usr/bin/env python3
"""Independent exhaustive two-step majority check on all one-chord cycles up to n=16."""

def fib(t):
    a,b=0,1
    for _ in range(t):a,b=b,a+b
    return a

def a(m):
    return 1 if m==1 else fib(m-1)

def delta(m):
    return 1 if m==1 else (1,1,0,-1,-1,0)[(m-2)%6]

def prediction(n,d):
    u,v=d-1,n-d-1
    return (2*(a(u)*a(v)+delta(u)*delta(v))
          +4*((d%2)*a(v)+((n-d)%2)*a(u))
          +2*(n%2==0))

def count_direct(n,d):
    neigh=[]
    for i in range(n):
        s={(i-1)%n,(i+1)%n}
        if i==0:s.add(d)
        if i==d:s.add(0)
        neigh.append(sorted(s))
    # This implementation uses explicit neighbor-opinion lists, not the run classification.
    def update(x):
        z=0
        for i,nb in enumerate(neigh):
            ones=sum((x>>j)&1 for j in nb)
            nxt= int(2*ones>len(nb)) if 2*ones!=len(nb) else (x>>i)&1
            z |= nxt<<i
        return z
    c=0
    for x in range(1<<n):
        y=update(x)
        if y!=x and update(y)==x:
            c+=1
            # A structural prediction separately checked for every example.
            assert ((x^y)&1) and ((x^y)&(1<<d)),(n,d,x,y)
    return c

def main():
    cases=0; states=0
    for n in range(5,17):
        data=[]
        for d in range(2,n//2+1):
            actual=count_direct(n,d)
            expected=prediction(n,d)
            assert actual==expected,(n,d,actual,expected)
            cases+=1; states+=1<<n
            data.append((d,actual))
        print(f'n={n}: '+', '.join(f'd={d}:P={p}' for d,p in data))
    print(f'PASS: {cases} chord geometries and {states} initial configurations exhausted')
if __name__=='__main__':main()
