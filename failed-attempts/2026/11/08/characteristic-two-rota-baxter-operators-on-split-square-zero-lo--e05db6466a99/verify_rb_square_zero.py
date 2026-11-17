#!/usr/bin/env python3
"""Independent finite-field checks for radical-square-zero Rota--Baxter operators.
Run with Python 3, standard library only."""
from itertools import product
from math import prod

def add(a,b,q): return tuple((x+y)%q for x,y in zip(a,b))
def mul(a,b,q):
    return (a[0]*b[0]%q,) + tuple((a[0]*b[j]+b[0]*a[j])%q for j in range(1,len(a)))
def lin(cols,x,q):
    out=[0]*len(x)
    for a,col in zip(x,cols):
        for j,y in enumerate(col):out[j]=(out[j]+a*y)%q
    return tuple(out)
def mm(A,B,q): return tuple(lin(A,col,q) for col in B)
def rank(A,q):
    if not A: return 0
    n=len(A[0]);mat=[[A[j][i]%q for j in range(len(A))] for i in range(n)]
    r=0
    for j in range(len(A)):
        piv=next((i for i in range(r,n) if mat[i][j]),None)
        if piv is None: continue
        mat[r],mat[piv]=mat[piv],mat[r]
        inv=pow(mat[r][j],-1,q)
        mat[r]=[(z*inv)%q for z in mat[r]]
        for i in range(n):
            if i!=r and mat[i][j]:
                fac=mat[i][j];mat[i]=[(u-fac*v)%q for u,v in zip(mat[i],mat[r])]
        r+=1
        if r==n: break
    return r

def rb(cols,q):
    dim=len(cols)
    e=[tuple(int(i==j) for i in range(dim)) for j in range(dim)]
    for x in e:
        for y in e:
            rx=lin(cols,x,q);ry=lin(cols,y,q)
            lhs=mul(rx,ry,q)
            z=add(mul(rx,y,q),mul(x,ry,q),q)
            if lhs!=lin(cols,z,q):return False
    return True

def inv_matrix(A,q):
    n=len(A); rows=[[A[j][i] for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        piv=next((i for i in range(j,n) if rows[i][j]),None)
        if piv is None:return None
        rows[j],rows[piv]=rows[piv],rows[j]
        z=pow(rows[j][j],-1,q);rows[j]=[(t*z)%q for t in rows[j]]
        for i in range(n):
            if i!=j and rows[i][j]:
                a=rows[i][j];rows[i]=[(x-a*y)%q for x,y in zip(rows[i],rows[j])]
    return tuple(tuple(rows[i][n+j] for i in range(n)) for j in range(n))

def all_cols(n,q):
    vec=list(product(range(q),repeat=n))
    return product(vec,repeat=n)

def enumerate_case(m,q):
    dim=m+1
    total=0;indices={1:0,2:0,3:0}; by_s={}; pairs=set()
    z=(0,)*m
    for cols in all_cols(dim,q):
        good=rb(cols,q)
        v=cols[0][1:];T=tuple(x[1:] for x in cols[1:])
        T2=mm(T,T,q)
        predicted=(cols[0][0]==0 and all(x[0]==0 for x in cols[1:]) and all(c==z for c in T2) and (q==2 or lin(T,v,q)==z))
        assert good==predicted,(m,q,cols,good,predicted)
        if good:
            s=rank(T,q);by_s[s]=by_s.get(s,0)+1
            R2=mm(cols,cols,q)
            ind=3 if any(any(c) for c in R2) else (1 if not any(any(c) for c in cols) else 2)
            indices[ind]+=1;total+=1
            pairs.add((T,v))
    return total,indices,by_s,pairs

def verify_orbits(m,pairs):
    q=2
    GL=[(A,inv_matrix(A,q)) for A in all_cols(m,q)]
    GL=[p for p in GL if p[1] is not None]
    rem=set(pairs);orbits=[]
    while rem:
        T,v=next(iter(rem));orb=set()
        for A,Ainv in GL:
            A_T_Ainv=mm(mm(A,T,q),Ainv,q)
            Av=lin(A,v,q)
            orb.add((A_T_Ainv,Av))
        assert orb<=pairs
        rem-=orb;orbits.append(orb)
    return len(orbits), sorted(len(x) for x in orbits)

def number_square_zero(m,q):
    out={}
    for T in all_cols(m,q):
        if all(c==(0,)*m for c in mm(T,T,q)):
            s=rank(T,q);out[s]=out.get(s,0)+1
    return out

def main():
    for m,q in ((2,2),(3,2),(2,3)):
        total,inds,by_s,pairs=enumerate_case(m,q)
        c=number_square_zero(m,q)
        assert by_s=={s:n*(q**m if q==2 else q**(m-s)) for s,n in c.items()}
        expected3=(sum(n*(q**m-q**(m-s)) for s,n in c.items()) if q==2 else 0)
        assert total==sum(by_s.values()) and inds[3]==expected3
        msg=f"q={q} m={m} total={total} indices={inds} T_ranks={by_s}"
        if q==2:
            num,sizes=verify_orbits(m,pairs)
            assert num==(2*m+1 if m%2==0 else 2*m)
            msg+=f" conjugacy_orbits={num} sizes={sizes}"
        print(msg)
    assert number_square_zero(4,2)=={0:1,1:105,2:210}
    print("CHAR_TWO_ROTA_BAXTER_INDEX_AND_ORBIT_CHECK_PASS")
if __name__=='__main__':main()
