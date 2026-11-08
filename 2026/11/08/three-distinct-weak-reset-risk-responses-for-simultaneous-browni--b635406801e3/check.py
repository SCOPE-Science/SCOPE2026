"""Conservative elementary-integral enclosures for collective Brownian search.
Run with Python 3 standard library: python check.py
"""
from decimal import Decimal as D, getcontext
from math import factorial
import json
getcontext().prec = 75
PI = D('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899')
C = D(2) / PI.sqrt()
K = 110
COEF = [D((-1)**j) / D(factorial(j)*(2*j+1)) for j in range(K+1)]
H=D('0.0001'); U=D(4); M=40000; ERR=D('1e-40'); TAIL_E=D('2e-8')
NS=(7,8,9,10,11,12)
def erf_interval(x):
    v=x*x
    s=COEF[-1]
    for c in reversed(COEF[:-1]):s=c+v*s
    center=C*x*s
    # The alternating-power tail is decreasing from index 111 for 0<=x<=4.
    # At x=4 the first omitted term is <1e-44; 75-digit arithmetic
    # throughout entails <1e-50 rounding at these arguments.
    return max(D(0),center-ERR),min(D(1),center+ERR)
last=[D(0),D(0)]
acc={n:[[D(0),D(0)] for k in range(1,4)] for n in NS}
for j in range(1,M+1):
    x=H*j
    cur=erf_interval(x)
    if j>1:
        a=x-H;b=x
        for k in range(1,4):
            w=a**(-2*k)-b**(-2*k)
            for n in NS:
                acc[n][k-1][0]+=w*last[0]**n
                acc[n][k-1][1]+=w*cur[1]**n
    last=cur
for n in NS:
    for k in range(1,4):
        lower,upper=acc[n][k-1]
        tail=U**(-2*k)
        lower+=(D(1)-D(n)*TAIL_E)*tail
        upper+=tail + D(2*k)/(D(n-2*k))*(C+ERR)**n * H**(n-2*k)
        acc[n][k-1]=[lower,upper]
def lower_upper(n):
    (al,au),(bl,bu),(cl,cu)=acc[n]
    mean=[al*al-bu/2,au*au-bl/2]
    var=[-D(2)*cu/3+D(3)*al*bl-D(2)*au**3,
         -D(2)*cl/3+D(3)*au*bu-D(2)*al**3]
    # same sign as the derivative of squared CV
    cv=[bl*bl-D(2)*au*cu/3,bu*bu-D(2)*al*cl/3]
    return mean,var,cv
results={}
for n in NS:
    m,v,c=lower_upper(n)
    results[str(n)]={'moments':[[str(p) for p in bounds] for bounds in acc[n]],
                    'mean_response':[str(x) for x in m],
                    'variance_response':[str(x) for x in v],
                    'squared_cv_response_numerator':[str(x) for x in c]}
    print('N',n,'mean',*(round(float(x),7) for x in m),
          'variance',*(round(float(x),7) for x in v),
          'cv-numerator',*(round(float(x),7) for x in c))
# All sign claims rest on integral enclosures, not midpoint estimates.
assert all(lower_upper(n)[0][0]>0 for n in NS)
assert all(lower_upper(n)[1][1]<0 for n in (7,8,9))
assert all(lower_upper(n)[1][0]>0 for n in (10,11,12))
assert all(lower_upper(n)[2][1]<0 for n in (7,8,9,10,11))
assert lower_upper(12)[2][0]>0
print('All interval sign checks PASS')
with open('enclosures.json','w',encoding='utf-8') as f:
    json.dump({'integration_interval':[str(H),str(U)],'subintervals':M,
               'erf_enclosure_error':str(ERR),'tail_erfc_bound_at_4':str(TAIL_E),
               'results':results},f,indent=2)
