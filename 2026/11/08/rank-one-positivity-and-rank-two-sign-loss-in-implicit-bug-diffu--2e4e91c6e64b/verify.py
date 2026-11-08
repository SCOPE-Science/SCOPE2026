"""Exact-rational reproduction of a two-dimensional low-rank diffusion BUG step.

Requires Python 3 standard library only. The computation implements the K, L
and Galerkin coefficient equations without normalizing bases; the output is
basis-invariant and identical to the QR-based update in exact arithmetic.
"""
from fractions import Fraction as Q

def mat(rows): return [[Q(x) for x in row] for row in rows]
def shape(A):return len(A),len(A[0])
def tr(A):return [list(x) for x in zip(*A)]
def mm(A,B):
    assert len(A[0])==len(B)
    BT=tr(B)
    return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in BT] for row in A]
def add(A,B):return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def sub(A,B):return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]
def scale(t,A):return [[t*x for x in row] for row in A]
def eye(n):return [[Q(int(i==j)) for j in range(n)] for i in range(n)]
def flat(A):return [v for row in A for v in row]
def unflat(v,n,r):return [v[i*r:(i+1)*r] for i in range(n)]
def solve_linear(A,b):
    n=len(b)
    T=[list(A[i])+[b[i]] for i in range(n)]
    for c in range(n):
        pivot=next((r for r in range(c,n) if T[r][c]),None)
        assert pivot is not None,'nonsingular Galerkin system required'
        T[c],T[pivot]=T[pivot],T[c]
        a=T[c][c];T[c]=[v/a for v in T[c]]
        for r in range(n):
            if r==c:continue
            a=T[r][c]
            if a:T[r]=[x-a*y for x,y in zip(T[r],T[c])]
    return [T[i][-1] for i in range(n)]
def solve_matrix_operator(n,r,op,rhs):
    columns=[]
    for i in range(n):
        for j in range(r):
            E=[[Q(int(i==x and j==y)) for y in range(r)] for x in range(n)]
            columns.append(flat(op(E)))
    A=tr(columns)
    result=unflat(solve_linear(A,flat(rhs)),n,r)
    assert op(result)==rhs
    return result

def bug_update(W,F,G,Lx,Ly,h):
    # W=F G^T; F and G need not be orthonormal.
    n,m=shape(W); r=shape(F)[1]
    assert mm(F,tr(G))==W
    MF=mm(tr(F),F);MG=mm(tr(G),G)
    NF=mm(mm(tr(F),Lx),F);NG=mm(mm(tr(G),Ly),G)
    # K/L-step: project implicit equation onto old right/left spaces.
    K=solve_matrix_operator(n,r,lambda X:sub(mm(mm(sub(eye(n),scale(h,Lx)),X),MG),scale(h,mm(X,NG))),mm(W,G))
    L=solve_matrix_operator(m,r,lambda X:sub(mm(mm(sub(eye(m),scale(h,Ly)),X),MF),scale(h,mm(X,NF))),mm(tr(W),F))
    GK=mm(tr(K),K);GL=mm(tr(L),L)
    AK=mm(mm(tr(K),Lx),K);AL=mm(mm(tr(L),Ly),L)
    # Implicit S-step projected into span(K) times span(L).
    rhs=mm(mm(tr(K),W),L)
    C=solve_matrix_operator(r,r,lambda X:sub(sub(mm(mm(GK,X),GL),scale(h,mm(mm(AK,X),GL))),scale(h,mm(mm(GK,X),AL))),rhs)
    return mm(mm(K,C),tr(L))

def full_backward_euler(W,Lx,Ly,h):
    n,m=shape(W)
    return solve_matrix_operator(n,m,lambda X:sub(sub(X,scale(h,mm(Lx,X))),scale(h,mm(X,Ly))),W)

def main():
    h=Q(20)
    F=mat([[3,0],[14,3],[0,7]])
    G=mat([[13,3],[1,0],[5,3]])
    Lx=mat([[-3,3,0],[3,-4,1],[0,1,-1]])
    Ly=mat([[-12,12,0],[12,-32,20],[0,20,-20]])
    W=mm(F,tr(G))
    assert W==mat([[39,3,15],[191,14,79],[21,0,21]])
    assert all(v>=0 for v in flat(W))
    assert all(sum(row)==0 for row in Lx+Ly)
    assert all(Lx[i][j]>=0 and Ly[i][j]>=0 for i in range(3) for j in range(3) if i!=j)
    assert F[0][0]*F[1][1]-F[0][1]*F[1][0]!=0
    assert G[0][0]*G[1][1]-G[0][1]*G[1][0]!=0
    result=bug_update(W,F,G,Lx,Ly,h)
    z=result[2][2]
    assert Q(-9,100)<z<Q(-8,100),z
    assert z<0
    assert result[2][0]<0 and result[2][1]<0
    # Original full backward Euler solves a nonsingular M-matrix and is positive.
    full=full_backward_euler(W,Lx,Ly,h)
    assert all(v>0 for v in flat(full))
    # Independent direct scalar check: on rank one the exact same subspace
    # equations preserve nonnegative data on an irreducible diffusion graph.
    checks=0
    for h2 in [Q(1,20),Q(1,2),Q(1),Q(20)]:
        for u in [mat([[1],[0],[0]]),mat([[0],[5],[0]]),mat([[3],[0],[7]])]:
            for v in [mat([[0],[1],[0]]),mat([[0],[0],[2]])]:
                W1=mm(u,tr(v))
                B=bug_update(W1,u,v,Lx,Ly,h2)
                assert all(x>0 for x in flat(B))
                checks+=1
    print('VERIFY_OK exact rational: rank-two output[3,3] =',str(z))
    print('Exact interval: -0.09 < output[3,3] < -0.08')
    print('Full backward Euler has 9 strictly positive entries')
    print('Rank-one strict positivity tests:',checks)
if __name__=='__main__':main()
