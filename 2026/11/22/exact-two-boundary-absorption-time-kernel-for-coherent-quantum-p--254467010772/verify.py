"""Exact recurrence and independent numerical checks for a two-boundary absorbing quantum path."""

def matrices(n):
    g = [[min(i+1, j+1) * (n - max(i, j)) if (i-j)%2 == 0 else 0
          for j in range(n)] for i in range(n)]
    b = [[min(i, j) * (n-1-max(i, j)) if (i-j)%2 == 0 else 0
          for j in range(n)] for i in range(n)]
    c = [[(1 if j>i else -1 if j<i else 0)*(n-1-i-j)
          if (i-j)%2 else 0 for j in range(n)] for i in range(n)]
    return g,b,c

def neigh(i,n):
    if i>0: yield i-1
    if i+1<n: yield i+1

def comm_adjacency(x,i,j,n):
    # (A X - X A)_{ij} for the path adjacency matrix A.
    return sum(x[k][j] for k in neigh(i,n)) - sum(x[i][k] for k in neigh(j,n))

def exact():
    positions=0
    for n in range(2,101):
        g,b,c=matrices(n)
        for i in range(n):
            for j in range(n):
                p_i=int(i in (0,n-1));p_j=int(j in (0,n-1))
                assert comm_adjacency(g,i,j,n)==0
                assert (p_i+p_j)*b[i][j]==0
                assert (p_i+p_j)*c[i][j]==comm_adjacency(b,i,j,n)
                # P G + G P - (C A - A C) = 4 I.
                assert (p_i+p_j)*g[i][j]+comm_adjacency(c,i,j,n)==(4 if i==j else 0)
                positions+=1
    return positions

def numeric():
    try:
        import numpy as np
        from scipy.linalg import solve_sylvester
    except ImportError:
        return 'not available (optional NumPy/SciPy check)'
    cases=0
    for n in (2,3,4,5,7,10,15):
        g,b,c=matrices(n)
        for J,kappa in ((1.,.7),(1.3,2.2),(0.75,4.25)):
            a=np.zeros((n,n))
            for j in range(n-1):
                a[j,j+1]=a[j+1,j]=1
            p=np.zeros((n,n));p[0,0]=p[-1,-1]=1
            k=.5*kappa*p+1j*J*a
            x=solve_sylvester(k.conj().T,k,np.eye(n))
            target=np.array(g,dtype=complex)/(2*kappa)+kappa*np.array(b)/(8*J*J)+1j*np.array(c)/(4*J)
            assert np.max(np.abs(x-target)) < 2e-9,(n,J,kappa)
            assert np.linalg.norm(k.conj().T@target+target@k-np.eye(n)) < 2e-9
            cases+=1
    return cases

if __name__=='__main__':
    print('EXACT_IDENTITIES_PASSED', exact())
    print('INDEPENDENT_LYAPUNOV_CASES', numeric())
