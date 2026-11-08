"""Independent exhaustive ternary tour check and integer tree check.

Python standard library only; exact integers. Fixing one distinguished length-four
window removes the rotational normalization without dividing by symmetry sizes.
"""
from itertools import product
from math import factorial


def valid(w):
    a,b,c,d=w
    return a!=b and b!=c and c!=d and (a,b)!=(c,d)


def exhaustive_ternary():
    edges=sorted(w for w in product(range(3),repeat=4) if valid(w))
    assert len(edges)==18
    out={}
    for i,e in enumerate(edges):
        out.setdefault(e[:3],[]).append((e[1:],i,e[3]))
    root=edges[0]
    full=(1<<18)-1
    found=[]
    letters=list(root)
    def rec(state,used):
        if used==full:
            if state==root[:3]:
                w=''.join(map(str,letters[:-3]))
                found.append(w)
            return
        for next_state,i,last in out.get(state,()):
            if not(used>>i & 1):
                letters.append(last)
                rec(next_state,used|(1<<i))
                letters.pop()
    rec(root[1:],1)
    assert len(found)==12
    all_edges=set(edges)
    for w in found:
        assert len(w)==18
        assert set(tuple(map(int,(w+w[:3])[i:i+4])) for i in range(18))==all_edges
    assert len(set(found))==12
    return found


def bareiss(A):
    A=[row[:] for row in A]
    n=len(A)
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]!=0),None)
            if j is None:return 0
            A[k],A[j]=A[j],A[k]
            sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numer=A[i][j]*piv-A[i][k]*A[k][j]
                assert numer%prev==0
                A[i][j]=numer//prev
            A[i][k]=0
        prev=piv
    return sign*A[-1][-1]


def tree_count(q):
    V=[(a,b,c) for a,b,c in product(range(q),repeat=3) if a!=b and b!=c]
    ix={v:i for i,v in enumerate(V)}
    L=[[0]*len(V) for _ in V]
    for v in V:
        i=ix[v]
        for d in range(q):
            if valid(v+(d,)):
                L[i][i]+=1
                L[i][ix[(v[1],v[2],d)]]-=1
    return bareiss([row[1:] for row in L[1:]])


def main():
    found=exhaustive_ternary()
    print('TERNARY_TOURS=12, sample=',found[0])
    for q in (3,4,5):
        t=tree_count(q)
        target=(q**(q-2)*(q-1)**(q*(q*q-3*q+1)-2)
                *(q-2)**(2*(q-1))*((q-2)**2+1)**((q-1)*(q-2)//2))
        assert t==target,(q,t,target)
        print('q=',q,'exact_arborescences=',t)
    print('TOUR_AND_BAREISS_VERIFY_OK')

if __name__=='__main__': main()
