"""Exact outward-rounded integer certificate for five EOS Farey-parent cycles.
Uses no third-party libraries. All transcendental bounds are proved below.
"""
from fractions import Fraction as Q
S=10**55
A=Q(833,10)
PERIOD={1:10,2:6,3:7,4:8,5:9}
NUMERATOR={1:1,2:1,3:2,4:3,5:4}
SEED={
 1:Q("0.0259590514290001113607894"),
 2:Q("0.0526797410255004507704518"),
 3:Q("0.2077771717296020928651274"),
 4:Q("0.2986863240202197734575438"),
 5:Q("-0.4805045058691037711644633"),
}
CRITICAL_CENTER=Q("0.052797055092220912165465066376786927")

def floorq(x): return x.numerator//x.denominator
def ceilq(x): return -(-x.numerator//x.denominator)
def fromq(x): return (floorq(x*S),ceilq(x*S))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 t=[i*j for i in x for j in y]
 return(min(t)//S,-(-max(t)//S))
def div(x,y):
 assert y[0]>0
 nums=[Q(i*S,j) for i in x for j in y]
 return floorq(min(nums)),ceilq(max(nums))
def scal(x,t):return mul(x,fromq(Q(t)))
def mid(x):return Q(x[0]+x[1],2*S)
def contain(i,j):return i[0]>=j[0] and i[1]<=j[1]
def show(x):return (float(Q(x[0],S)),float(Q(x[1],S)))

def exp_pos(z):
 assert z>=0
 k=0
 while z>Q(1,2)*(2**k):k+=1
 # e^(z/2^k)=sum_{0..55}(z/2^k)^j/j! + remainder < 1/S.
 # For 0<=w<=1/2, remainder < 2*(1/2)^56/56! < 10^-55.
 w=fromq(z/(2**k)); term=fromq(Q(1));res=term
 for j in range(1,56):
  term=div(mul(term,w),fromq(Q(j)))
  res=add(res,term)
 res=(res[0],res[1]+1)
 for j in range(k):res=mul(res,res)
 return res

def exp_neg(z):
 assert z>=0
 return div(fromq(Q(1)),exp_pos(z))
def sig(z):
 if z>=0:
  v=exp_neg(z)
  return div(fromq(Q(1)),add(fromq(Q(1)),v))
 v=exp_neg(-z)
 return div(v,add(fromq(Q(1)),v))

def sig_bounds(x):
 return sig(A*Q(x[0],S))[0],sig(A*Q(x[1],S))[1]
def derivative(x):
 # q(t)=sig(at)(1-sig(at)); increasing for t<0, decreasing for t>0.
 l,h=Q(x[0],S),Q(x[1],S)
 def tval(z):
  v=sig(A*z)
  return mul(v,sub(fromq(Q(1)),v))
 if h<=0:
  qlo=tval(l)[0];qhi=tval(h)[1]
 elif l>=0:
  qlo=tval(h)[0];qhi=tval(l)[1]
 else:
  qlo=min(tval(l)[0],tval(h)[0]);qhi=ceilq(Q(S,4))
 return sub(fromq(Q(1)),scal((qlo,qhi),A))

def F_point(x,b):
 return sub(fromq(x+b),sig(A*x))
def F(x,b):
 c=mid(x)
 fc=F_point(c,b)
 delta=sub(x,fromq(c))
 return add(fc,mul(derivative(x),delta))

def cycle(k):
 c=SEED[k]
 r=Q(1,10**13)
 box=fromq(c-r)[0],fromq(c+r)[1]
 n=PERIOD[k];b=Q(k,11)
 orbit=[box]
 for t in range(1,n): orbit.append(F(orbit[-1],b))
 out=F(orbit[-1],b)
 assert out[0]>box[0] and out[1]<box[1],(k,'not strictly invariant',show(out),show(box))
 for i in range(n):
  for z in orbit[i+1:]:
   assert not (orbit[i][0]<=z[1] and z[0]<=orbit[i][1]),(k,'nonprimitive')
 positives=sum(J[0]>0 for J in orbit)
 assert all(J[0]>0 or J[1]<0 for J in orbit)
 assert positives==NUMERATOR[k]
 assert abs(11*positives-k*n)==1
 assert n>11-n # Farey parent with larger denominator.
 d=fromq(Q(1))
 for o in orbit:d=mul(d,derivative(o))
 assert -S<d[0] and d[1]<S,(k,'nonhyperbolic',show(d))
 return box,orbit,d

def critical_brackets():
 # Derivative 1-a*sigma(ax)*(1-sigma(ax)) has one simple root
 # in each half-line. Bracket both roots by rational intervals.
 c=CRITICAL_CENTER;r=Q(1,10**35)
 v=[(fromq(-c-r)[0],fromq(-c+r)[1]),(fromq(c-r)[0],fromq(c+r)[1])]
 for h in v:
  dl=derivative((h[0],h[0]));du=derivative((h[1],h[1]))
  assert (dl[0]>0 and du[1]<0) or (dl[1]<0 and du[0]>0),(show(h),show(dl),show(du))
 return v

def locate(x,orbit):
 for idx,J in enumerate(orbit):
  if contain(x,J):return idx
 return None

def verify():
 cb=critical_brackets()
 outputs=[]
 for k in PERIOD:
  box,orbit,d=cycle(k);b=Q(k,11)
  # calculate critical + boundary images and place into any phase trapping interval.
  times=[]
  for name,x in [('crit-',cb[0]),('crit+',cb[1])]:
   found=locate(x,orbit)
   for t in range(1,600):
    if found is not None:break
    x=F(x,b)
    found=locate(x,orbit)
    if x[1]-x[0]>S*10:
     raise RuntimeError((k,name,'wide',t,show(x)))
   assert found is not None,(k,name,'not captured',show(x),t)
   times.append((name,t-1,found))
  outputs.append((k,PERIOD[k],show(box),show(d),times))
 for row in outputs:print('CERT',row)
 print('FIVE_FAREY_PARENT_CYCLES_AND_SINGER_BASINS_CERTIFIED')
if __name__=='__main__':verify()
