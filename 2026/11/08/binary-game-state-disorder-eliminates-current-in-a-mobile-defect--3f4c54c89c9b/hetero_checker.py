"""Exact finite-state tests for binary-environment public-goods imitation on cycles.
Uses only Python standard library; tests are evidence supplements, not a proof.
"""
from fractions import Fraction as F
from itertools import product

def payoff(state, rates, i):
    n=len(state)
    x=state[i]
    return -x+(rates[(i-1)%n]*(state[(i-1)%n]+x)+rates[i]*(x+state[(i+1)%n]))/2

def outcomes(state, rates):
    n=len(state)
    # Each global asynchronous update chooses the focal vertex and one neighbor.
    # This fixed normalizer bounds every positive payoff difference.
    D=F(10)
    output={}
    for i in range(n):
        for j in ((i-1)%n,(i+1)%n):
            if state[i]==state[j]:continue
            d=payoff(state,rates,j)-payoff(state,rates,i)
            if d>0:
                other=list(state);other[i]=state[j];other=tuple(other)
                output[other]=output.get(other,F(0))+d/(2*n*D)
    return output

def single(n,j):
    z=[1]*n;z[j]=0;return tuple(z)
def pair(n,j):
    z=[1]*n;z[j]=z[(j+1)%n]=0;return tuple(z)

def rates_predicted(rates,j):
    n=len(rates)
    a_right=1+rates[(j-1)%n]/2-rates[(j+1)%n]
    a_left=1+rates[j]/2-rates[(j-2)%n]
    b_to_sj=rates[(j+2)%n]-1
    b_to_sj1=rates[(j-2)%n]-1
    fac=F(1,2*n*10)
    return a_right*fac,a_left*fac,b_to_sj*fac,b_to_sj1*fac

def exact_test():
    cases=states=0
    for n in range(4,10):
        lo,hi=F(11,10),F(7,5)  # 1<lo<hi<1+lo/2<2
        for pattern in product((lo,hi),repeat=n):
            rates=tuple(pattern)
            wS=[F(0)]*n;wE=[F(0)]*n;wS[0]=F(1)
            for j in range(n):
                ar,al,b0,b1=rates_predicted(rates,j)
                assert min(ar,al,b0,b1)>0
                assert outcomes(single(n,j),rates)=={
                    pair(n,j):ar,pair(n,(j-1)%n):al}
                assert outcomes(pair(n,j),rates)=={
                    single(n,j):b0,single(n,(j+1)%n):b1}
                wE[j]=wS[j]*ar/b0
                next_weight=wE[j]*b1/rates_predicted(rates,(j+1)%n)[1]
                if j<n-1:wS[j+1]=next_weight
                else:assert next_weight==1,(n,pattern,next_weight)
            Z=sum(wS)+sum(wE)
            assert Z>0
            weights={single(n,j):wS[j]/Z for j in range(n)}
            weights.update({pair(n,j):wE[j]/Z for j in range(n)})
            inp={s:F(0) for s in weights}
            for s,weight in weights.items():
                moves=outcomes(s,rates)
                tot=sum(moves.values(),F(0))
                assert tot<F(1)
                inp[s]+=weight*(1-tot)
                for t,q in moves.items():inp[t]+=weight*q
            assert inp==weights,(n,pattern)
            assert sum(weights.values())==1
            cases+=1;states+=2*n
    print('PASS: exact transition rates, cycle detailed balance and stationarity on',cases,'binary environments and',states,'states')
    for n in range(5,10):
        lo,hi=F(11,10),F(17,10)
        # Force a defector at j=2 with a right-hand high C-C and opposing low edge.
        rates=[lo]*n;rates[0]=hi;rates[2]=lo
        initial=single(n,2)
        out=outcomes(initial,tuple(rates))
        assert tuple([1]*n) in out and out[tuple([1]*n)]>0
    print('PASS: sharp upper threshold counterexamples for n=5..9')
    for n in range(4,10):
        r=F(7,5);rates=(r,)*n
        w1=F(1)
        ar,al,b0,b1=rates_predicted(rates,0)
        w2=ar/b0
        assert (1+2*w2)/(1+w2)==2/r
    print('PASS: homogeneous mean defect formula = 2/r')
    rates=(F(11,10), F(11,10), F(6,5), F(11,10), F(13,10))
    ratio=F(1)
    for j in range(5):
        ar,al,b0,b1=rates_predicted(rates,j)
        an=rates_predicted(rates,(j+1)%5)[1]
        ratio*=ar*b1/(an*b0)
    assert ratio==F(77,75),ratio
    print('PASS: three-level environment has nonzero ring affinity, cycle ratio 77/75')
if __name__=='__main__':exact_test()
