"""Independent integer-programming check for binary 3x3 bibifix code capacity."""
from itertools import product
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix


def p2(w):return w[0],w[1],w[3],w[4]
def s2(w):return w[4],w[5],w[7],w[8]

def run(a,b):
    W=[w for w in product(range(2),repeat=9) if w[0]==a and w[8]==b]
    I=[];J=[];D=[];k=0
    for i,x in enumerate(W):
        for j in range(i+1,len(W)):
            y=W[j]
            if p2(x)==s2(y) or p2(y)==s2(x):
                I.extend([k,k]);J.extend([i,j]);D.extend([1,1]);k+=1
    E=coo_matrix((D,(I,J)),shape=(k,len(W))).tocsr()
    result=milp(-np.ones(len(W)),integrality=np.ones(len(W)),
      bounds=Bounds(np.zeros(len(W)),np.ones(len(W))),
      constraints=LinearConstraint(E,-np.inf*np.ones(k),np.ones(k)),
      options={'time_limit':60})
    assert result.success, result.message
    assert round(-result.fun)==64
    assert max(abs(result.x-np.rint(result.x)))<1e-6
    return len(W),k,round(-result.fun)
if __name__=='__main__':
    for a,b in ((0,1),(1,0)):
        print(a,b,run(a,b))
    print('MILP_INDEPENDENT_PASSES')
