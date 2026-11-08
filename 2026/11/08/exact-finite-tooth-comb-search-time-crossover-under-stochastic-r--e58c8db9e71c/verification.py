"""Reproduce finite-comb reset search identities and mesoscopic convergence.
All jump rates along an edge equal one; a separate resetting clock has rate r.
No graph libraries or external packages required.
"""
import math


def formula(L,H,r):
    th=math.acosh(1+r/2)
    # Stable tooth impedance through exp form
    e=math.exp(-th)
    ah=(e + math.exp(-2*H*th))/(1+math.exp(-(2*H+1)*th))
    gamma=math.acosh((r+3-ah)/2)
    return math.expm1(L*gamma)/r


def gauss(A,b):
    n=len(b)
    for i in range(n):
        k=max(range(i,n),key=lambda j:abs(A[j][i]))
        A[i],A[k]=A[k],A[i]; b[i],b[k]=b[k],b[i]
        c=A[i][i]
        assert abs(c)>1e-13
        for j in range(i+1,n):
            t=A[j][i]/c
            A[j][i]=0
            for v in range(i+1,n): A[j][v]-=t*A[i][v]
            b[j]-=t*b[i]
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        x[i]=(b[i]-sum(A[i][j]*x[j] for j in range(i+1,n)))/A[i][i]
    return x


def truncation_expected_time(L,H,r,B):
    # independent backward Poisson equation for a graph truncated at x=-B
    # with reflecting left endpoint. Reset at rate r in every nonabsorbing state.
    states=[(x,y) for x in range(-B,L) for y in range(H+1)]
    pos={s:i for i,s in enumerate(states)}
    A=[[0.]*len(states) for _ in states]
    b=[1.]*len(states)
    for (x,y), i in pos.items():
        nbr=[]
        if y==0:
            if x>-B: nbr.append((x-1,0))
            nbr.append((x+1,0))  # x+1=L is absorbing
            nbr.append((x,1))
        else:
            nbr.append((x,y-1))
            if y<H: nbr.append((x,y+1))
        A[i][i]=len(nbr)+r
        for v in nbr:
            if v in pos: A[i][pos[v]]-=1
        A[i][pos[(0,0)]]-=r
    return gauss(A,b)[pos[(0,0)]]


def limit(k,u):
    f=u**.25*math.sqrt(math.tanh(k*math.sqrt(u)))
    return math.expm1(f)/u


def verify():
    checks=0
    # exact finite graph backward equation with controlled left boundary
    for L,H,r,B,tol in [(1,1,.4,12,2e-7), (2,2,.3,14,8e-7), (2,3,1.0,11,2e-8), (3,1,.7,12,2e-7)]:
        v=formula(L,H,r)
        w=truncation_expected_time(L,H,r,B)
        assert abs(v-w)/v<tol,(L,H,r,v,w,abs(v-w)/v)
        checks+=1
    # exact independent tooth recurrence using one-step continued fractions
    for H,r in [(1,.2),(2,.5),(4,.1),(7,2.),(20,.4)]:
        th=math.acosh(1+r/2)
        a=(math.exp(-th)+math.exp(-2*H*th))/(1+math.exp(-(2*H+1)*th))
        d=1/(1+r)
        for _ in range(H-1): d=1/(2+r-d)
        assert abs(a-d)<1e-12,(H,r,a,d)
        checks+=1
    for k,u in [(.2,.5),(.5,1.),(1.,.1),(1.,1.),(1.,5.),(2.,3.)]:
        errors=[]
        for L in (20,40,80,160):
            H=max(1,round(k*L*L))
            t=formula(L,H,u/L**4)/L**4
            errors.append(abs(t-limit(k,u)))
        assert errors[-1]<.012,(k,u,errors)
        assert errors[-1]<errors[1],(k,u,errors)
        checks+=1
    for v in (.25,1,4):
        k=.0001
        t=limit(k,v/k)/k
        bench=math.expm1(math.sqrt(v))/v
        assert abs(t-bench)/bench<.005,(v,t,bench)
        checks+=1
    for u in (.2,1,20):
        t=limit(100,u)
        bench=math.expm1(u**.25)/u
        assert abs(t-bench)<1e-12
        checks+=1
    print(f'PASS {checks} independent finite and asymptotic checks')
    for k,u in [(.25,1.),(1.,1.),(2.,3.)]:
        print('k,u',k,u,'lim',limit(k,u),'sample',formula(80,round(k*80**2),u/80**4)/80**4)

if __name__=='__main__':verify()
