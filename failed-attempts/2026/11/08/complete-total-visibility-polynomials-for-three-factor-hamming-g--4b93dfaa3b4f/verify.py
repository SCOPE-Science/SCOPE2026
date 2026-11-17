"""Exact independent enumeration of total-visibility polynomials on three-coordinate Hamming graphs.

Run using python3 verify.py. Uses only the Python standard library.
"""
from collections import Counter, deque
from itertools import product
from math import comb


def add(a, b, scale=1):
    out = a[:]
    if len(out) < len(b):
        out += [0] * (len(b) - len(out))
    for i, value in enumerate(b):
        out[i] += scale * value
    return out


def mult(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def power(s, exponent):
    r = [1]
    for _ in range(exponent):
        r = mult(r,s)
    return r


def mon(k, value=1):
    return [0]*k+[value]


def predicted(b,n):
    w = [1]
    w = add(w, add(power([1,1],b),[1],-1),2*n)
    w = add(w, mon(2,b*n))
    w = add(w, add(add(power([1,1],n),[1],-1),mon(1,n),-1),2*b)
    t11 = add(add(power([1,2],b),power([1,1],b),-2),[1])
    w = add(w,t11,n*(n-1))
    p = add(power([1,1],b-1),[1],-1)
    q = add(add(power([1,1],n-1),[1],-1),mon(1,n-1),-1)
    w = add(w,mult(p,q),2*n*b)
    t22 = add(add(power([1,2],n),power([1,1],n),-2),[1])
    t22 = add(t22, mult(mon(1,-2*n),add(power([1,1],n-1),[1],-1)))
    t22 = add(t22,mon(2,n*(n-1)))
    w = add(w,t22,b*(b-1))
    while len(w)>1 and w[-1]==0: w.pop()
    return w


def graph(b,n):
    v=list(product(range(2),range(b),range(n)))
    d=[[sum(x!=y for x,y in zip(v[i],v[j])) for j in range(len(v))] for i in range(len(v))]
    return v,d


def enumerate_valid(b,n):
    v,d=graph(b,n)
    size=len(v)
    forb=[sum(1<<j for j in range(size) if d[i][j]==2) for i in range(size)]
    c=Counter()
    maximal=Counter()
    examples=[]
    def rec(i, mask, used):
        if i == size:
            c[used]+=1
            if not any(mask&(1<<j)==0 and mask&forb[j]==0 for j in range(size)):
                maximal[used]+=1
            if len(examples)<30: examples.append(mask)
            return
        rec(i+1,mask,used)
        if not (mask & forb[i]):
            rec(i+1,mask | (1<<i),used+1)
    rec(0,0,0)
    return [c[i] for i in range(max(c)+1)],maximal,examples


def total_visible_by_literal_paths(v,d,mask):
    # For every source and target, ask whether a geodesic avoiding selected interior vertices exists.
    # Every permitted edge changes one coordinate; the remaining Hamming distance decreases on a geodesic.
    N=len(v)
    for s in range(N):
        for t in range(s+1,N):
            visited={s}; stack=[s]
            while stack:
                cur=stack.pop()
                if cur==t: break
                for nxt in range(N):
                    if d[cur][nxt]==1 and d[nxt][t]==d[cur][t]-1 and nxt not in visited:
                        if nxt==t or not(mask>>nxt&1):
                            visited.add(nxt)
                            stack.append(nxt)
            if t not in visited: return False
    return True


def literal_small(b,n):
    v,d=graph(b,n)
    N=len(v)
    bad=0
    for mask in range(1<<N):
        has_dist_two=any((mask>>i&1) and (mask>>j&1) and d[i][j]==2 for i in range(N) for j in range(i+1,N))
        truth=total_visible_by_literal_paths(v,d,mask)
        assert truth == (not has_dist_two),(b,n,mask,has_dist_two,truth)
        bad+=1
    return bad


def run():
    profiles=[(2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(3,5),(5,3),(4,5),(5,4),(2,6)]
    count=0
    for b,n in profiles:
        expected=predicted(b,n)
        actual,maximals,ex=enumerate_valid(b,n)
        assert actual==expected,(b,n,actual,expected)
        if b>=3 and n>=3: assert len(actual)-1==b+n-2 and actual[-1]==2*b*n,(b,n,actual)
        if min(b,n)==2 and max(b,n)>=3: assert actual[-1]==2**(max(b,n)+1),(b,n,actual)
        if b==n==2: assert actual[-1]==16
        print('POLY_OK',b,n,'coefs',actual,'maximal_size_counts',dict(maximals))
        count+=1
    for b,n in [(2,2),(2,3)]:
        total=literal_small(b,n)
        print('LITERAL_OK',b,n,'all_subsets',total)
    print('VERIFY_OK', 'profiles',count,'full_literal_subsets',2**8+2**12,'classification_and_polynomial=PASS','unrestricted_proof_not_replaced_by_finite_check')


if __name__=='__main__':
    run()
