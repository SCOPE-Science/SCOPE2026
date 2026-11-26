from fractions import Fraction


def beta(T,b,t):
    return b*Fraction(T-t,1)/(Fraction(T,1)-b*t)


def direct_tail(T,b,t):
    prod=Fraction(1,1)
    total=Fraction(0,1)
    for k in range(t,T):
        prod *= beta(T,b,k)
        total += prod
    return total


def closed_tail(T,b,t):
    return b*Fraction(T-t,1)/(T*(1-b)+b)

for T in (1,2,3,5,10,37,100):
    for b in (Fraction(1,10),Fraction(1,2),Fraction(9,10),Fraction(99,100)):
        C=T*(1-b)+b
        for t in range(T+1):
            d=direct_tail(T,b,t)
            c=closed_tail(T,b,t)
            assert d == c
            if t<T:
                bt=beta(T,b,t)
                proxy=bt/(1-bt)
                gamma=T*(1-b)/C
                assert c == gamma*proxy
                assert (proxy-c)/proxy == b/C
                # A newly injected gradient at t uses the next-state tail.
                assert closed_tail(T,b,t+1) == b*Fraction(T-t-1,1)/C

# Source-style common momentum example.
b=Fraction(9,10)
for T,target in ((100,0.08256880733944954),(1000,0.0089197224975223),(10000,0.00089919072834449)):
    err=float(b/(T*(1-b)+b))
    assert abs(err-target) < 5e-15

print('verification passed')
