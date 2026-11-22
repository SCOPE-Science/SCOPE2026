"""Supplementary finite-section checks of two-rate weighted Hardy leakage.
Requires only Python standard library. Numerical sampling is not the proof.
"""
import math

def g(beta, alpha, n, cutoff):
    c=2*alpha-beta+1; delta=beta-alpha
    lo=[]; hi=[]
    for k in range(n+1):
        val=math.sqrt(2*k+beta+1)*math.exp(math.lgamma(k+alpha+1)-math.lgamma(k+delta+1)-c*math.log(n))
        lo.append(val)
    for k in range(n+1, cutoff+1):
        val=math.sqrt(2*k+beta+1)*math.exp(math.lgamma(k+delta)-math.lgamma(k+alpha+2)+c*math.log(n))
        hi.append(val)
    return lo,hi

def dot(v,w): return sum(x*y for x,y in zip(v,w))

def compute(n, cutoff):
    beta=3.; a=[2.,2.5]
    parts=[g(beta,x,n,cutoff) for x in a]
    H=[[dot(parts[i][0],parts[j][0]) for j in range(2)] for i in range(2)]
    R=[[dot(parts[i][1],parts[j][1]) for j in range(2)] for i in range(2)]
    tr=H[0][0]*R[0][0]+H[1][1]*R[1][1]-2*H[0][1]*R[0][1]
    de=(H[0][0]*H[1][1]-H[0][1]**2)*(R[0][0]*R[1][1]-R[0][1]**2)
    rad=max(0,tr*tr-4*de)**.5
    return ((tr+rad)/2)**.5, ((tr-rad)/2)**.5, H, R

def main():
    target=(1/5,1/30)
    print('Target limiting singular values:',target)
    for n in [5,20,80,300,1000]:
        s1,s2,H,R=compute(n, max(50000,n*70))
        print('n=',n,'numerical=',round(s1,10),round(s2,10),'errors=',round(abs(s1-target[0]),10),round(abs(s2-target[1]),10))
        assert s1>s2>0
        if n>=300:
            assert abs(s1-target[0])<.005 and abs(s2-target[1])<.005
    print('Finite-section checks passed; infinite assertion is proved analytically.')
if __name__=='__main__':main()
