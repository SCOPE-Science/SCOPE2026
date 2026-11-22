from itertools import combinations
from math import pi,cos
import numpy as np

def boundary_2(tris):
    edges=sorted(set(tuple(sorted(e)) for t in tris for e in combinations(t,2)))
    pos={e:i for i,e in enumerate(edges)}
    B=np.zeros((len(edges),len(tris)),dtype=int)
    for j,(a,b,c) in enumerate(tris):
        a,b,c=sorted((a,b,c))
        for edge,coeff in (((b,c),1),((a,c),-1),((a,b),1)):
            B[pos[edge],j]=coeff
    return edges,B

def verify(n):
    m=2*n-1
    fan=[(0,1,k) for k in range(2,m+2)]
    rim=list(range(2,n+2))
    tris=[]
    for i in range(n):
        j=(i+1)%n
        tris.extend([(0,rim[i],rim[j]),(1,rim[i],rim[j])])
    tris.remove((0,rim[0],rim[1]))
    e1,B1=boundary_2(fan); e2,B2=boundary_2(tris)
    G1=B1.T@B1;G2=B2.T@B2
    vals1=np.linalg.eigvalsh(G1);vals2=np.linalg.eigvalsh(G2)
    assert len(e1)==2*m+1 and len(e2)==3*n
    assert np.array_equal(G1,2*np.eye(m,dtype=int)+np.ones((m,m),dtype=int))
    assert abs(vals1[0]-2)<1e-8 and abs(vals1[-1]-(m+2))<1e-8
    assert vals2[0]>-1e-9 and vals2[0]<=2*(1-cos(pi/n))+1e-8
    assert vals2[0]>=1/(n*(2*n-1))-1e-8
    assert vals2[-1]<=6+1e-8
    assert np.linalg.matrix_rank(B1)==m and np.linalg.matrix_rank(B2)==m
    return n,m,len(e1),len(e2),round(vals2[0],8),round(vals2[-1],8)
if __name__=='__main__':
 for n in range(3,13):print(verify(n))
