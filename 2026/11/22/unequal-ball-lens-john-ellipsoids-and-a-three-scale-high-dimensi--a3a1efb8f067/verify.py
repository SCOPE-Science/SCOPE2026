import math, random

def find(R,r,L,d):
    g=R/r
    Lc=d*(R*R-r*r)/(R*(d-1))
    if g>=d or L<=Lc:
        lo=max(0.,R-L)
        hi=r
        def F(a):
            v=a+L-R
            return (a+d*v)*(a+v/d)-r*r
        assert F(lo)<1e-9 and F(hi)>-1e-9,(R,r,L,d,F(lo),F(hi))
        for _ in range(110):
            a=(lo+hi)/2
            if F(a)>0:hi=a
            else:lo=a
        a=(lo+hi)/2;v=a+L-R
        q=d*a*v
        b=math.sqrt(a*a+q);z=R-a
        return ('tip',z,a,b,1.,-1/d)
    else:
        umin=math.sqrt(g/d)
        def calc(u):
            k=(u*u-g*g/(d*d*u*u))/(g*g-1)
            D=u+1/(d*u)
            H=r/math.sqrt((k+1)*(k+1/(d*d*u*u)))
            return H*D,H,k
        low=umin;high=1.
        assert calc(low)[0]>L and calc(high)[0]<L,(R,r,L,d,calc(low)[0],calc(high)[0])
        for _ in range(110):
            mid=(low+high)/2
            if calc(mid)[0]>L:low=mid
            else:high=mid
        u=(low+high)/2
        Lv,H,k=calc(u)
        a=k*H; b=H*math.sqrt(k*(k+1));z=H*u
        return ('interior',z,a,b,u,-1/(d*u))

random.seed(4455)
max_contain=max_iso=max_formula=0
n_cases=0
for dim in (4,5,6,10,20):
 for ratio in (1.01,1.2,1.8,2.2,2.99,3.1,5.5,12.0):
  R=ratio;r=1.
  for sep_frac in (0.0001,0.03,0.2,0.48,0.6,0.8,0.93,0.9999):
   L=R-r+2*r*sep_frac
   branch,z,a,b,up,um=find(R,r,L,dim)
   assert a>0 and b>0 and b>a,(dim,ratio,sep_frac,branch,z,a,b)
   def max_f(cx):
    h=z-cx;q=b*b-a*a
    v=a*h/q
    t=max(-1.,min(1.,v))
    return h*h+b*b+2*a*h*t-q*t*t
   e=max(max_f(0)-R*R,max_f(L)-r*r)
   max_contain=max(max_contain,e)
   # numerical checks at 250 points / ball, independent
   for j in range(251):
    t=-1+2*j/250
    fs=(z+a*t)**2+b*b*(1-t*t)
    ft=(z+a*t-L)**2+b*b*(1-t*t)
    assert fs<=R*R+1e-9 and ft<=r*r+1e-9,(dim,ratio,sep_frac,branch,t,fs-R*R,ft-r*r)
   wplus=-um/(up-um); wminus=up/(up-um)
   max_iso=max(max_iso,abs(wplus*up+wminus*um),abs(wplus*up*up+wminus*um*um-1/dim))
   n_cases+=1
assert n_cases==320 and max_contain<1e-9 and max_iso<1e-12
print('cases',n_cases,'max_containment_excess',max_contain,'max_isotropy_residual',max_iso)
print('sample: R=2,r=1,L=1.8,dim4 ->',find(2,1,1.8,4))
print('sample: R=1.2,r=1,L=0.5,dim4 ->',find(1.2,1,0.5,4))
print('sample: R=10,r=1,L=10.7,dim4 ->',find(10,1,10.7,4))

# The dimension asymptotics are analytic; the following are finite diagnostics only.
A=3.0
for lam, power, target in ((1.6,0.0,math.sqrt(A*(A/1.6**2-1))), (math.sqrt(A),0.25,(2*A)**.25), (2.4,0.5,math.sqrt((2.4**2+A)/(2.4**2-A)))):
    vals=[find(2,1,lam,d)[4]*d**power for d in (1000,10000,100000)]
    assert abs(vals[-1]-target)<0.002, (lam,power,vals,target)
    print('asymptotic',lam,'power',power,'estimates',vals,'limit',target)
print('VERIFY_OK')
