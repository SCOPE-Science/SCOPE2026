"""Finite checks for the four-generator exterior algebra odd-commuting graph.

Run: python3 check_odd_commuting_spectrum.py
Requires numpy; uses exact integer arithmetic for incidence and exterior multiplication.
"""
import itertools
import random
import numpy as np


def projective_points(q):
    seen=set(); reps=[]
    for x in itertools.product(range(q),repeat=4):
        if not any(x): continue
        k=next(i for i,z in enumerate(x) if z)
        inv=pow(x[k],-1,q)
        u=tuple((a*inv)%q for a in x)
        if u not in seen:
            seen.add(u); reps.append(u)
    return sorted(reps)


def dot(u,v,q):return sum(a*b for a,b in zip(u,v))%q


def exterior_product_odd(v,p,w,r,q):
    # p,r are degree-three components identified with V* by the volume pairing.
    two_form=tuple((v[i]*w[j]-v[j]*w[i])%q for i in range(4) for j in range(i+1,4))
    top=(dot(v,r,q)-dot(w,p,q))%q
    return two_form+(top,)


def label(v,p,q):
    if not any(v): return ('A',p)
    k=next(i for i,x in enumerate(v) if x)
    a=v[k]
    u=tuple((x*pow(a,-1,q))%q for x in v)
    t=(dot(u,p,q)*pow(a,-1,q))%q
    return ('B',u,t)


def check(q, full=False):
    P=projective_points(q)
    L=len(P); K=q*q+q+1; s=(q-1)*q**3
    assert L==q**3+q**2+q+1
    N=np.asarray([[int(dot(p,u,q)==0) for u in P] for p in P],dtype=np.int64)
    gram=N.T@N
    assert np.array_equal(gram,q*q*np.eye(L,dtype=np.int64)+(q+1)*np.ones((L,L),dtype=np.int64))
    # Direct exterior multiplication checks versus the class/incidence rule.
    rng=random.Random(700+q)
    for _ in range(30000):
        v=tuple(rng.randrange(q) for _ in range(4)); w=tuple(rng.randrange(q) for _ in range(4))
        p=tuple(rng.randrange(q) for _ in range(4)); r=tuple(rng.randrange(q) for _ in range(4))
        l1=label(v,p,q);l2=label(w,r,q)
        if l1[0]=='A' and l2[0]=='A': rule=True
        elif l1[0]=='B' and l2[0]=='B':rule=l1[1:]==l2[1:]
        elif l1[0]=='A':rule=dot(l1[1],l2[1],q)==0
        else:rule=dot(l2[1],l1[1],q)==0
        algebra=not any(exterior_product_odd(v,p,w,r,q))
        assert rule==algebra,(q,v,p,w,r,rule,algebra)
    a=q**4-1;c=q**4*a
    Q=np.array([[0,a,c],[1,a-1,K*q*s],[1,q**3-1,s-1]],dtype=np.int64)
    assert np.linalg.det(Q)!=0
    if full:
        assert q==3
        # All q^8 elements; exhaustively recover every block's cardinality.
        V=list(itertools.product(range(q),repeat=4))
        classes={}
        for v in V:
            for p in V:
                classes[label(v,p,q)]=classes.get(label(v,p,q),0)+1
        assert len(classes)==q**4+L*q
        assert sum(classes.values())==q**8
        assert sum(key[0]=='A' for key in classes)==q**4
        assert all(n==1 for key,n in classes.items() if key[0]=='A')
        assert all(n==s for key,n in classes.items() if key[0]=='B')
        # Compressed class adjacency (orthonormal class indicator vectors).
        alpha=V
        M=np.array([[int(dot(p,u,q)==0) for u in P for t in range(q)] for p in alpha],dtype=np.float64)
        H=np.zeros((q**4+L*q,q**4+L*q),dtype=np.float64)
        H[:q**4,:q**4]=np.ones((q**4,q**4))-np.eye(q**4)
        H[:q**4,q**4:]=np.sqrt(s)*M
        H[q**4:,:q**4]=np.sqrt(s)*M.T
        H[q**4:,q**4:]=(s-1)*np.eye(q*L)
        eig=np.linalg.eigvalsh(H)
        golden=[(s-2-s*np.sqrt(5))/2,(s-2+s*np.sqrt(5))/2]
        expected=[-1.0]*(L*(q-2))+[float(s-1)]*(L*(q-1))
        expected+= [golden[0]]*(L-1)+[golden[1]]*(L-1)
        expected+=list(np.linalg.eigvals(Q.astype(float)).real)
        assert len(eig)==len(expected)
        assert np.max(np.abs(eig-np.sort(expected)))<2e-9
        # Reconstruct the full characteristic polynomial roots by adding
        # the (s-1)-dimensional sum-zero subspaces within each B clique.
        assert len(expected)+L*q*(s-1)==q**8
        print(f'q={q} full compressed eigencheck PASS; max discrepancy {np.max(np.abs(eig-np.sort(expected))):.2e}')
    print(f'q={q}, projective points={L}, design Gram PASS, exterior checks=30000 PASS, quotient det={round(np.linalg.det(Q))}, q-classes={q*L}, clique-size={s}')


if __name__=='__main__':
    for q in (3,5,7):check(q,full=(q==3))
    print('EXTERIOR4_ODD_GRAPH_SPECTRUM_OK')
