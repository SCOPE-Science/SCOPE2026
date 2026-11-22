"""Finite independent checks for the connected zero-forcing broom root theorem.
Requires numpy for numerical roots. These checks are not the infinite proof.
"""
import numpy as np


def make_broom(h, r):
    # Hub 0; r-1 direct leaves; last branch is a path of h edges.
    n = r + h
    graph = [set() for _ in range(n)]
    for leaf in range(1, r):
        graph[0].add(leaf); graph[leaf].add(0)
    last = 0
    for vertex in range(r, n):
        graph[last].add(vertex); graph[vertex].add(last)
        last=vertex
    return graph


def naive_polynomial(graph):
    n=len(graph)
    out=[0]*(n+1)
    for bits in range(1,1<<n):
        blue={i for i in range(n) if bits>>i&1}
        frontier=[next(iter(blue))]; seen=set(frontier)
        for v in frontier:
            for w in graph[v]:
                if w in blue and w not in seen:
                    seen.add(w);frontier.append(w)
        if seen!=blue:continue
        colored=set(blue)
        while len(colored)<n:
            forced=set()
            for v in colored:
                white=graph[v]-colored
                if len(white)==1:forced.update(white)
            if not forced:break
            colored.update(forced)
        if len(colored)==n:out[len(blue)]+=1
    return out


def expected_polynomial(h,r):
    n=h+r
    out=[0]*(n+1)
    for k in range(r,r+h):out[k]=r
    out[r+h]=1
    return out


def right_count(h):return 2*(h//4)

def negative_count(h,r):
    if h%2:return 1
    lhs=h**h*(r-1)**(h+1)
    rhs=r*(h+1)**(h+1)
    return 0 if lhs<rhs else 2


def run():
    brute_count=0
    for h in range(1,8):
        for r in range(3,8):
            if r+h>12:continue
            got=naive_polynomial(make_broom(h,r))
            exp=expected_polynomial(h,r)
            assert got==exp,(h,r,got,exp)
            brute_count+=1
    numerical_count=0
    for h in range(1,25):
        for r in range(3,13):
            roots=np.roots([1]+[r]*h)
            right=sum(z.real>1e-5 for z in roots)
            negative=sum(z.real<0 and abs(z.imag)<1e-4 for z in roots)
            assert right==right_count(h),(h,r,right)
            assert negative==negative_count(h,r),(h,r,negative)
            assert all(abs(z.real)>1e-5 for z in roots)
            numerical_count+=1
    print('EXHAUSTIVE_BROOM_POLYNOMIALS',brute_count)
    print('NUMERICAL_ROOT_CENSUS',numerical_count, 'h=1..24 r=3..12')
    print('RIGHT_HALF_PLANE_EXAMPLES', [(h,right_count(h)) for h in range(1,13)])
    print('DOUBLE_NEGATIVE_ROOT h=2 r=4 root=-2')
    print('VERIFY_OK')

if __name__=='__main__':run()
