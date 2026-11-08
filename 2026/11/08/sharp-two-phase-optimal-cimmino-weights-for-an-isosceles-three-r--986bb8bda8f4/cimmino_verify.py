"""Independent standard-library numerical checks for the three-row Cimmino formula.
Run: python3 cimmino_standalone.py. Numerical sampling does not prove optimality.
"""
import math
import random


def eigenvalues_symmetric_3x3(a):
    m = [list(row) for row in a]
    for _ in range(50):
        p, q = max(((0,1),(0,2),(1,2)), key=lambda ij: abs(m[ij[0]][ij[1]]))
        if abs(m[p][q]) < 1e-14:
            return sorted(m[i][i] for i in range(3))
        tau = (m[q][q]-m[p][p])/(2*m[p][q])
        t = math.copysign(1.0, tau)/(abs(tau)+math.hypot(1,tau))
        cosine = 1/math.hypot(1,t)
        sine = t*cosine
        app, aqq, apq = m[p][p],m[q][q],m[p][q]
        m[p][p] = app-t*apq
        m[q][q] = aqq+t*apq
        m[p][q]=m[q][p]=0.0
        for r in range(3):
            if r!=p and r!=q:
                x,y=m[r][p],m[r][q]
                m[r][p]=m[p][r]=cosine*x-sine*y
                m[r][q]=m[q][r]=sine*x+cosine*y
    raise AssertionError('Jacobi iteration did not converge')


def spectral_rate(weights,c,d):
    a,b,e=weights
    v=eigenvalues_symmetric_3x3([[a,math.sqrt(a*b)*c,math.sqrt(a*e)*c],
           [math.sqrt(a*b)*c,b,math.sqrt(b*e)*d],
           [math.sqrt(a*e)*c,math.sqrt(b*e)*d,e]])
    return max(abs(1-v[0]),abs(1-v[2]))


def optimal(d,c):
    assert 0<d<1 and 0<c and 2*c*c<1+d
    if (1+d)*c*c < 2*d*d:
        q=d*(1-d)/(d-c*c)
        rho=(q+3*d-1)/(q+1+d)
        b=2/(q+1+d)
    else:
        q=1+d
        rho=math.sqrt(2/(1+d))*c
        b=1/(1+d)
    return (q*b,b,b),rho


def check():
    random.seed(341196)
    count=0
    for j in range(320):
        d=random.uniform(.02,.98)
        c=random.uniform(.001,.995*math.sqrt((1+d)/2))
        best, rate=optimal(d,c)
        assert abs(spectral_rate(best,c,d)-rate) < 3e-11, (j,d,c,best,rate)
        for _ in range(75):
            ws=[math.exp(random.uniform(-2,2)) for k in range(3)]
            assert spectral_rate(ws,c,d) >= rate-1e-10, (j,d,c,ws,rate)
            count += 1
    for d in [.05,.25,.5,.75,.95]:
        c=math.sqrt(2*d*d/(1+d))
        w,r=optimal(d,c)
        assert abs(spectral_rate(w,c,d)-r)<3e-11
        count+=1
    weights,rate=optimal(.5,.25)
    assert abs(rate-15/29)<1e-14
    assert all(abs(w-v)<1e-14 for w,v in zip(weights,[16/29,28/29,28/29]))
    assert abs(spectral_rate(weights,.25,.5)-15/29)<3e-11
    assert abs(spectral_rate([1,1,1],.25,.5)-(1+math.sqrt(3))/4)<3e-11
    print(f'PASS {count} randomized and boundary comparisons across 320 parameter sets; exact-rational example matched')

if __name__=='__main__':
    check()
