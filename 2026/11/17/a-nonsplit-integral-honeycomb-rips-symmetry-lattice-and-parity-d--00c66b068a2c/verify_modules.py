#!/usr/bin/env python3
"""Exact cellular action and coinvariant Smith forms for periodic honeycomb Rips spaces.
Requires SymPy for Smith normal forms; all geometric action checks are integral.
"""
from verify import graph,cycles6,lift_orientation,rot,refl,shift,orientation_sign
from sympy import eye,zeros,ZZ
from sympy.matrices.normalforms import smith_normal_form

def check(L):
    V,A=graph(L); F=lift_orientation(L,A,cycles6(L,A))
    keys=list(F); q=len(keys); loc={f:i for i,f in enumerate(keys)}
    # Relative cellular chains have two generators per face, B and W.
    # X=(T,s_0,...,s_{q-1}) has q+1 degree-two cycles with:
    # T=sum(W_faces), s_f=B_face-W_face.
    def basis(j):
        a=[0]*(2*q)
        if j==0:
            for i in range(q):a[2*i+1]=1
        else:
            a[2*(j-1)]=1;a[2*(j-1)+1]=-1
        return a
    def image(a,fn):
        ans=[0]*(2*q)
        for f,i in loc.items():
            mapped=tuple(fn(v,L) for v in F[f]);g=frozenset(mapped)
            sign=orientation_sign(mapped,F[g]);k=loc[g]
            color_swapped=fn(V[0],L)[0]!=V[0][0]
            for color in (0,1):
                ans[2*k+(1-color if color_swapped else color)]+=sign*a[2*i+color]
        return ans
    cols=[basis(j) for j in range(q+1)]
    matrices=[]
    for name,fn in [('shift',shift),('rot',rot),('reflect',refl)]:
        delta=orientation_sign(tuple(fn(v,L) for v in F[keys[0]]),F[frozenset(fn(v,L) for v in keys[0])])
        eps=1 if fn(V[0],L)[0]==V[0][0] else -1
        M=zeros(q+1,q+1);M[0,0]=delta
        if eps==-1:
            for i in range(1,q+1): M[i,0]=delta
        for f,j in loc.items():
            g=frozenset(fn(v,L) for v in f)
            M[loc[g]+1,j+1]=delta*eps
        # Independently apply graph symmetries to the 2q oriented 2-cells.
        for j in range(q+1):
            expected=[sum(int(M[i,j])*cols[i][h] for i in range(q+1)) for h in range(2*q)]
            assert image(cols[j],fn)==expected, (L,name,j)
        matrices.append(M)
    rel=(matrices[0]-eye(q+1)).row_join(matrices[1]-eye(q+1)).row_join(matrices[2]-eye(q+1))
    diagonal=smith_normal_form(rel,domain=ZZ)
    factors=[abs(int(diagonal[i,i])) for i in range(q+1)]
    assert all(f>0 for f in factors)
    torsion=[f for f in factors if f>1]
    assert torsion==([2] if L%2 else [2,2]),torsion
    print(f'L={L}: exact relative cellular action validated on {q+1} generators for each of 3 graph symmetries; coinvariant SNF torsion factors {torsion}, rank 0')

if __name__=='__main__':
    for L in (5,6,7,8):check(L)
