"""Independent finite-state exact checks for the majority hyperstar theorem.
All arithmetic for probabilities is rational; no third-party dependencies.
"""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict


def stats(state,k):
    hub=state&1
    a=b=m=0
    for j in range(k):
        v=(state>>(2*j+1))&1
        w=(state>>(2*j+2))&1
        if v==w==1:a+=1
        elif v==w==0:b+=1
        else:m+=1
    return a,b,m,hub


def update(state,k,j):
    idx=(0,2*j+1,2*j+2)
    bit=sum((state>>i)&1 for i in idx)
    maj=int(bit>=2)
    for i in idx:
        if maj:state|=1<<i
        else:state&=~(1<<i)
    return state


def predicted(a,b,m,hub):
    if a and b:return Q(0)
    if not a and not b:return Q(1)
    if a:return Q(1) if hub==1 else Q(a,a+m)
    return Q(1) if hub==0 else Q(b,b+m)


@lru_cache(None)
def recurrence(a,b,m):
    if not m:
        t=Q(int(a*b==0))
        return t,t
    # First-step recursion for the full CTMC aggregated by petal classes.
    nxt_a=recurrence(a+1,b,m-1)[0]
    nxt_b=recurrence(a,b+1,m-1)[1]
    A0=Q(m,m+b)*nxt_a
    B0=Q(m,m+a)*nxt_b
    c=Q(b,m+b)
    d=Q(a,m+a)
    A=(A0+c*B0)/(1-c*d)
    B=B0+d*A
    return A,B


def kosaraju_sinks(n,k):
    out=[[] for _ in range(n)]
    rev=[[] for _ in range(n)]
    for state in range(n):
        for j in range(k):
            v=update(state,k,j)
            if v!=state:
                out[state].append(v)
                rev[v].append(state)
    seen=set()
    order=[]
    for root in range(n):
        if root in seen:continue
        seen.add(root)
        stack=[(root,0)]
        while stack:
            v,i=stack[-1]
            if i==len(out[v]):
                order.append(v);stack.pop();continue
            stack[-1]=(v,i+1)
            w=out[v][i]
            if w not in seen:
                seen.add(w);stack.append((w,0))
    comp=[-1]*n; parts=[]
    for root in reversed(order):
        if comp[root]!=-1:continue
        idx=len(parts)
        comp[root]=idx
        stack=[root];vertices=[]
        while stack:
            v=stack.pop();vertices.append(v)
            for w in rev[v]:
                if comp[w]<0:comp[w]=idx;stack.append(w)
        parts.append(vertices)
    sinks=[]
    for i,part in enumerate(parts):
        if all(comp[w]==i for v in part for w in out[v]):sinks.append(part)
    return sinks


def main():
    count=0
    for k in range(1,6):
        n=1<<(2*k+1)
        sinks=kosaraju_sinks(n,k)
        assert len(sinks)==2**k,(k,len(sinks))
        assert sum(len(s)==1 for s in sinks)==2
        assert sum(len(s)==2 for s in sinks)==2**k-2
        count+=3
        for sink in sinks:
            classes=[stats(v,k) for v in sink]
            assert all(m==0 for a,b,m,h in classes)
            if len(sink)==1:
                assert (classes[0][0]==k and classes[0][3]==1) or (classes[0][1]==k and classes[0][3]==0)
            else:
                assert all(a>0 and b>0 for a,b,m,h in classes)
                assert sorted([x[3] for x in classes])==[0,1]
            count+=1
        for state in range(n):
            a,b,m,h=stats(state,k)
            r=recurrence(a,b,m)[0 if h else 1]
            assert r==predicted(a,b,m,h),(k,state,r,predicted(a,b,m,h))
            count+=1
        for q in (Q(1,5),Q(1,3),Q(1,2),Q(2,3),Q(4,5)):
            total=Q(0)
            for state in range(n):
                ones=state.bit_count()
                a,b,m,h=stats(state,k)
                total+=q**ones*(1-q)**(2*k+1-ones)*recurrence(a,b,m)[0 if h else 1]
            closed=q*q*(3-2*q)*(2*q-q*q)**(k-1)+(1-q)**2*(1+2*q)*(1-q*q)**(k-1)
            assert total==closed,(k,q,total,closed)
            count+=1
        assert (Q(3,4)**(k-1))==Q(1,2)**2*(3-1)*(Q(3,4)**(k-1)) + Q(1,2)**2*(1+1)*(Q(3,4)**(k-1))
        count+=1
    print(f'PASS: {count} exact certificates, all reachable states through k=5, recurrent classes and iid formula verified')

if __name__=='__main__':main()
