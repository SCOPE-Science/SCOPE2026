"""Independent exact checks of the theta-network bridge laws.

No dependencies beyond Python's standard library. Run: python verify_theta.py
"""
from fractions import Fraction
from itertools import product
from math import comb


def theta_edges(a,b,c):
    # The two terminals are 0 and 1; other vertices are path specific.
    edges=[]; nxt=2
    for length in (a,b,c):
        vertices=[0]+list(range(nxt,nxt+length-1))+[1]
        nxt+=length-1
        edges.extend((vertices[j],vertices[j+1]) for j in range(length))
    return edges, nxt


def bridge_count(edges, mask, vertex_count):
    present=[edges[j] for j in range(len(edges)) if mask>>j&1]
    def connected(u,v, skip):
        adj=[[] for _ in range(vertex_count)]
        for j,(x,y) in enumerate(present):
            if j!=skip:
                adj[x].append(y);adj[y].append(x)
        stack=[u]; seen={u}
        while stack:
            for w in adj[stack.pop()]:
                if w not in seen:
                    seen.add(w);stack.append(w)
        return v in seen
    return sum(not connected(u,v,j) for j,(u,v) in enumerate(present))


def conditional_mean(a,b,c,k):
    m=a+b+c
    return Fraction(k)-sum(Fraction(d*comb(k,d),comb(m,d)) if k>=d else 0
                           for d in (a+b,a+c,b+c))+m*int(k==m)


def theoretical_pgf_counts(a,b,c):
    # Coefficients of s^k t^b in the explicit pair-cycle formula.
    m=a+b+c; out={}
    for k in range(m+1):
        for mask in range(1<<m):
            if mask.bit_count()!=k:continue
            complete=[all(mask>>j&1 for j in range(st,st+l))
                      for st,l in ((0,a),(a,b),(a+b,c))]
            open_count=k
            number_full=sum(complete)
            bcount=open_count-sum(l for l,full in zip((a,b,c),complete) if full) if number_full>=2 else open_count
            out[k,bcount]=out.get((k,bcount),0)+1
    return out


def closed_joint_counts(a,b,c):
    # Independent exact convolution of the PGF correction formula.
    m=a+b+c; ans={}
    def add(k,b,v): ans[k,b]=ans.get((k,b),0)+v
    # Base (1-p+p s t)^m, counting subsets grouped by degree.
    for k in range(m+1): add(k,k,comb(m,k))
    # Pair complete, third incomplete: Q-third not including its top term.
    for d,other in ((a+b,c),(a+c,b),(b+c,a)):
        for h in range(other):
            n=comb(other,h)
            add(d+h,h,n)  # corrected case: full pair not bridges
            add(d+h,d+h,-n)  # cancel base case
    # All three full: base replaced by B=0.
    add(m,0,1);add(m,m,-1)
    return {key:v for key,v in ans.items() if v}


def main():
    cases=[(2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,2,5),(2,2,6),
           (2,3,5),(2,4,4),(2,3,6),(3,4,4)]
    assertions=0; subgraphs=0
    for a,b,c in cases:
        edges,nv=theta_edges(a,b,c);m=len(edges)
        joint={}; by_k={}
        for mask in range(1<<m):
            k=mask.bit_count();bval=bridge_count(edges,mask,nv)
            joint[k,bval]=joint.get((k,bval),0)+1
            by_k[k]=by_k.get(k,0)+bval
            subgraphs+=1
        assert joint==closed_joint_counts(a,b,c);assertions+=1
        assert joint==theoretical_pgf_counts(a,b,c);assertions+=1
        for k in range(m+1):
            assert Fraction(by_k[k],comb(m,k))==conditional_mean(a,b,c,k)
            assertions+=1
        # Exact checks of Bernoulli covariance, using no differentiation.
        for p in (Fraction(1,5),Fraction(2,5),Fraction(3,4)):
            Ex=Eb=Exb=Fraction(0)
            for (k,bval),count in joint.items():
                prob=count*p**k*(1-p)**(m-k)
                Ex+=k*prob;Eb+=bval*prob;Exb+=k*bval*prob
            expected=p*(1-p)*(m-sum(d*d*p**(d-1) for d in (a+b,a+c,b+c))
                                     +m*m*p**(m-1))
            assert Exb-Ex*Eb==expected;assertions+=1
        # Last 3 values test the curvature criterion.
        dlast=conditional_mean(a,b,c,m)-2*conditional_mean(a,b,c,m-1)+conditional_mean(a,b,c,m-2)
        numerator=6*a*b*c-sum(x*x*(x-1) for x in (a,b,c))
        assert dlast==Fraction(numerator,m*(m-1)); assertions+=1
    assert 6*2*2*5-sum(x*x*(x-1) for x in (2,2,5))>0
    assert 6*2*2*6-sum(x*x*(x-1) for x in (2,2,6))<0
    print(f"PASS: {assertions+2} exact comparisons, {subgraphs} exhaustive edge subsets, {len(cases)} theta graphs")

if __name__=='__main__':main()
