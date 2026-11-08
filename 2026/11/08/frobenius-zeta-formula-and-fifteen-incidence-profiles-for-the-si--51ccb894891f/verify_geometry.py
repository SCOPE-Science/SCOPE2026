"""Independent direct rational-point counts off the exceptional locus for
split and one nonsplit blow-up model, using exact prime-field arithmetic."""
from itertools import combinations

def normalize(v,p):
 for c in v:
  if c%p:
   r=pow(c,-1,p)
   return tuple((z*r)%p for z in v)
 raise ValueError('zero vector')

def cross(a,b,p):
 return normalize((a[1]*b[2]-a[2]*b[1],
                   a[2]*b[0]-a[0]*b[2],
                   a[0]*b[1]-a[1]*b[0]),p)

def points(p):
 return {normalize((x,y,z),p) for x in range(p)
         for y in range(p) for z in range(p) if x or y or z}

for p in (5,7,11,13,17,19):
 pts=points(p)
 base=[normalize((1,t,t*t),p) for t in range(4)]+[(0,0,1)]
 chords={cross(a,b,p) for a,b in combinations(base,2)}
 assert len(chords)==10
 complement={P for P in pts if (P[0]*P[2]-P[1]**2)%p!=0 and
             all(sum(u*v for u,v in zip(P,L))%p!=0 for L in chords)}
 assert len(complement)==(p-5)**2
 assert len(pts)==p*p+p+1

# Nonsplit form: blow up 3 Fp-rational conic points and one degree-two
# closed conic point. The Frobenius on the 5 blown-up geometric points
# transposes one pair, hence its W(D5) element is a coordinate transposition
# (no sign changes), with profile (4,8,12,0).
# Field F_{p^2} = Fp[A]/(A^2-d), d any nonsquare; elements are (a,b).
def add(x,y,p):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def mul(x,y,p,d):return ((x[0]*y[0]+d*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def sub(x,y,p):return ((x[0]-y[0])%p,(x[1]-y[1])%p)
def cx(a,b,p,d):
 return tuple(sub(mul(a[(i+1)%3],b[(i+2)%3],p,d),
                  mul(a[(i+2)%3],b[(i+1)%3],p,d),p) for i in range(3))

def conic(t,p,d):
 one=(1,0)
 return (one,t,mul(t,t,p,d))

def membership(P,L,p):
 return (sum(P[i]*L[i][0] for i in range(3))%p==0 and
         sum(P[i]*L[i][1] for i in range(3))%p==0)

for p in (5,7,11,13):
 d=next(z for z in range(2,p) if pow(z,(p-1)//2,p)==p-1)
 base=[conic((t,0),p,d) for t in (0,1,2)]
 base += [conic((0,1),p,d), conic((0,p-1),p,d)]
 secants=[cx(a,b,p,d) for a,b in combinations(base,2)]
 assert len(secants)==10
 rest={P for P in points(p) if (P[0]*P[2]-P[1]**2)%p!=0 and
       all(not membership(P,L,p) for L in secants)}
 assert len(rest)==p*p-4*p+5,(p,len(rest),p*p-4*p+5)
print('VERIFY_BLOWUP_GEOMETRY_OK')
