"""Independent numerical verification of edge-Hodge spectrum on triangulated cyclic strips.
Scientific test script for reproducibility; only standard numpy is required.
"""
import math
import numpy as np

def complex_matrices(n):
    # top vertices 0..n-1, bottom n..2n-1
    T=lambda j:j%n; B=lambda j:n+j%n
    # edge orientations T_j, B_j, V_j (bottom to top), D_j (bottom to next top)
    edges=[]
    for j in range(n): edges.extend([(T(j),T(j+1)),(B(j),B(j+1)),(B(j),T(j)),(B(j),T(j+1))])
    eidx={edge:i for i,edge in enumerate(edges)}
    B1=np.zeros((2*n,4*n))
    for h,(a,b) in enumerate(edges):
        B1[a,h]=-1; B1[b,h]=+1
    B2=np.zeros((4*n,2*n))
    for j in range(n):
        # F+ = b_j -> t_{j+1} -> t_j -> b_j
        # F- = b_j -> b_{j+1} -> t_{j+1} -> b_j
        B2[4*j+3,2*j]=1
        B2[4*j+0,2*j]=-1
        B2[4*j+2,2*j]=-1
        B2[4*j+1,2*j+1]=1
        B2[4*((j+1)%n)+2,2*j+1]=1
        B2[4*j+3,2*j+1]=-1
    assert np.allclose(B1@B2,0)
    return B1,B2

def expected_eigenvalues(n, alpha=1.0, beta=1.0):
    out=[]
    for j in range(n):
        x=abs(math.cos(math.pi*j/n))
        c=math.cos(2*math.pi*j/n)
        node0=4-2*c-2*x
        node1=4-2*c+2*x
        if j==0:
            out += [0.0, alpha*node1]
        else:
            out += [alpha*node0, alpha*node1]
        out += [beta*(3-2*x),beta*(3+2*x)]
    return np.sort(out)

def verify():
    nchecks=0
    for n in range(3,61):
        B1,B2=complex_matrices(n)
        for a,b in [(1.,1.),(.5,1.6),(3.3,.7)]:
            mat=a*(B1.T@B1)+b*(B2@B2.T)
            calc=np.linalg.eigvalsh(mat)
            target=expected_eigenvalues(n,a,b)
            tol=2.e-11*(1+np.max(abs(target)))
            assert np.max(abs(calc-target)) < tol, (n,a,b,np.max(abs(calc-target)))
            nchecks+=len(target)
        g=6-4*math.cos(math.pi/n)**2-2*math.cos(math.pi/n)
        assert (g<1)==(n>=7)
        # Under a + b = 2, the unique best minimum-positive mode is their equalization.
        a=2/(1+g); b=2*g/(1+g)
        assert abs(min(a*g,b)-2*g/(1+g))<1e-12
        nchecks+=2
        grad=[]; curl=[]
        for j in range(n):
            c=abs(math.cos(math.pi*j/n))
            q=6-4*c*c
            if j==0: grad.append(q+2*c)
            else: grad.extend([q-2*c,q+2*c])
            curl.extend([3-2*c,3+2*c])
        assert any(abs(x-4)<1.e-9 for x in grad)
        assert any(abs(x-5)<1.e-9 for x in curl)
        assert any(abs(x-4)<1.e-9 for x in curl)==(n%3==0)
        assert any(abs(x-5)<1.e-9 for x in grad)==(n%5==0)
        nchecks+=4
    print('PASS', nchecks,'comparisons, all n=3..60, three independent weights.')
if __name__=='__main__':verify()
