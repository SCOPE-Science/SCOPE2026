#!/usr/bin/env python3
"""Exact rational witnesses for the three-point metric numerical-index theorem.
This is a finite consistency diagnostic, not a proof of the universal statement.
"""
from fractions import Fraction as Q

def formula(w):
    out=[]
    for i in range(3):
        j,k=[t for t in range(3) if t!=i]
        t,u,v=w[i],w[j],w[k]
        out.append(min((u+v)/t,1+(t+u-v)*(t+v-u)/(t*(u+v-t))))
    return out

def det(x,y): return x[0]*y[1]-x[1]*y[0]
def coords(u,v,vector):
    denominator=det(u,v)
    return (det(vector,v)/denominator,det(u,vector)/denominator)

def check(w):
    a,b,c=w
    assert all(t>0 for t in w)
    assert a+b>c and b+c>a and c+a>b
    v=[(Q(1),Q(-1)),(Q(1),(c-a)/b),((c-b)/a,Q(1))]
    missed=[2,1,0]
    psi=[(Q(1),Q(0)),(Q(0),Q(1)),(-a/c,-b/c)]
    def evaluation(phi,x): return phi[0]*x[0]+phi[1]*x[1]
    predicted=formula(w)
    for h,i in enumerate(missed):
        other=[j for j in range(3) if j!=h]
        coeff=coords(v[other[0]],v[other[1]],v[h])
        B=sum(abs(z) for z in coeff)
        wi=w[i]; j,k=[t for t in range(3) if t!=i]
        assert B==1+(wi+w[j]-w[k])*(wi+w[k]-w[j])/(wi*(w[j]+w[k]-wi))
        R=predicted[i]
        signs=tuple(Q(1) if z>0 else Q(-1) for z in coeff)
        mat=(v[other[0]],v[other[1]])
        # Solve functional values at two independent vertices.
        p=(signs[0]*mat[1][1]-signs[1]*mat[0][1])/det(*mat)
        q=(mat[0][0]*signs[1]-mat[1][0]*signs[0])/det(*mat)
        p*=R/B; q*=R/B
        out=[-wi/(w[j]+w[k])]*3
        out[i]=Q(1)
        def Tx(x):
            val=p*x[0]+q*x[1]
            return (out[0]*val,out[1]*val,out[2]*val)
        vals=[Tx(vertex) for vertex in v]
        numerical=max(abs(vals[t][k]) for t in range(3) for k in range(3) if k!=missed[t])
        operator=max(abs(vals[t][k]) for t in range(3) for k in range(3))
        assert numerical<=1 and operator==R, (w,i,numerical,operator,R)
    return 3

if __name__=='__main__':
    count=0
    for x in range(1,8):
        for y in range(1,8):
            for z in range(1,8):
                w=tuple(map(Q,(y+z,x+z,x+y)))
                count+=check(w)
    for w in ((Q(1),Q(1),Q(3,2)),(Q(2),Q(3),Q(4)),(Q(1),Q(1),Q(19,10))):
        count+=check(w)
    print('TRIANGLE_NUMERICAL_INDEX_EXACT_WITNESS_OK',count)
