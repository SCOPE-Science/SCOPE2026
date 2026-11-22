"""Directly enumerate synchronous Greenberg-Hastings configurations on chorded cycles.

Run: python3 verify_bruteforce.py
"""
from itertools import product


def h(k, L, delta=1):
    return L + (int((-L - delta) % k == 0)) - sum((2*j - L + delta + 2) % k == 0 for j in range(L))


def predicted(k, n, a):
    b=n-a
    c0 = int(n % k == 0)
    c1 = int((a+1) % k == 0)
    c2 = int((b+1) % k == 0)
    return 2*k*(c0+c1*h(k,b)+c2*h(k,a)-c0*c1-c0*c2-c1*c2)


def update(s, neighbors, k):
    return tuple((v+1) % k if v else int(any(s[j]==1 for j in neighbors[i])) for i,v in enumerate(s))


def check(k,n,a):
    neighbors=[{(i-1)%n,(i+1)%n} for i in range(n)]
    neighbors[0].add(a); neighbors[a].add(0)
    actual=0
    for s in product(range(k), repeat=n):
        q=s
        for _ in range(k):
            q=update(q,neighbors,k)
        if q==s and update(s,neighbors,k)!=s:
            actual+=1
    expected=predicted(k,n,a)
    assert actual == expected, (k,n,a,actual,expected)
    return actual


def main():
    cases=0; states=0
    for k, max_n in [(3,9),(4,9),(5,7)]:
        for n in range(4,max_n+1):
            for a in range(2,n//2+1):
                check(k,n,a)
                cases+=1; states+=k**n
    print('PASS direct update: %d chorded graph cases; %d input states examined'%(cases,states))
    print('Example k=4,n=6,a=3: %d primitive four-orbits'%(predicted(4,6,3)//4))

if __name__=='__main__':main()
