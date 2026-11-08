"""Independent fourth-moment Gram test for two equatorial traces on harmonic quadratics.
Requires numpy; execute `python two_equator_checker.py`."""
import math
import numpy as np


def traceless_basis(d):
    arr=[]
    for j in range(1,d):
        x=np.zeros((d,d),dtype=float)
        for k in range(j): x[k,k]=1/math.sqrt(j*(j+1))
        x[j,j]=-j/math.sqrt(j*(j+1))
        arr.append(x)
    for i in range(d):
        for j in range(i+1,d):
            x=np.zeros((d,d),dtype=float)
            x[i,j]=x[j,i]=1/math.sqrt(2)
            arr.append(x)
    return arr

def equator_fourth_bilinear(A,B,n):
    P=np.eye(len(n))-np.outer(n,n)
    X=P@A@P;Y=P@B@P
    return (2*np.trace(X@Y)+np.trace(X)*np.trace(Y))/((len(n)-1)*(len(n)+1))

def reference_spectrum(d,c):
    K=d*(d+2)/(d*d-1)
    T=3*(1+c*c)/4+1/(2*d)
    D=c*c*(d+1)/(2*d)
    disc=max(0,T*T-4*D)
    ep=(T+math.sqrt(disc))/2;em=(T-math.sqrt(disc))/2
    vals=[ep,em,3*(1-c*c)/4]+[(1-c)/2]*(d-2)+[(1+c)/2]*(d-2)
    if d>=4: vals += [1]*((d-2)*(d-1)//2-1)
    return np.sort(K*np.array(vals))


def actual_spectrum(d,c):
    A=traceless_basis(d);u=np.zeros(d);u[0]=1
    v=np.zeros(d);v[0]=c;v[1]=math.sqrt(1-c*c)
    gram=np.array([[sum(equator_fourth_bilinear(X,Y,n) for n in (u,v))/2 for Y in A] for X in A])
    norm=2/(d*(d+2))
    return np.linalg.eigvalsh(gram/norm)

def run():
    count=0
    for d in range(3,12):
        for c in [0,1e-4,.1,.25,.45,.5,.555,.6,.72,.85,.9999,1.]:
            q=actual_spectrum(d,c)
            r=reference_spectrum(d,c)
            assert len(q)==len(r)
            assert np.allclose(q,r,rtol=6e-10,atol=2e-10),(d,c,q,r)
            count+=1
    for d in range(3,100):
        cstar=(math.sqrt(3*d*d+6*d+4)-2)/(3*d)
        K=d*(d+2)/(d*d-1)
        opt=reference_spectrum(d,cstar)
        assert abs(opt[0]-K*(1-cstar)/2)<1e-10
        for c in (cstar*.7,cstar*.97,cstar+(1-cstar)*.03,cstar+(1-cstar)*.3):
            assert reference_spectrum(d,c)[0]<opt[0]+1e-12
            count+=1
        if d>=4:
            assert abs(opt[-1]-K)<1e-10
        else:
            assert abs((opt[-1]/opt[0])-25/6)<1e-10
        count+=1
    print('TWO_EQUATOR_CHECKS_PASS',count)

if __name__=='__main__':run()
