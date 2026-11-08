"""Exact, exhaustive rational affine-cell certificate for two source rays."""
from fractions import Fraction as F
B=F(3,2)
P={(F(-7,2),F(-1)),(F(7,2),F(-3)),(F(11,2),F(2)),(F(5,2),F(5))}
Q={(F(-7,2),F(-1)),(F(-3,2),F(1)),(F(5,2),F(-2))}

def T(z):
 x,y=z
 return(abs(x)-y-1,x-abs(y)+B)

# A cell is (X-slope,X-intercept,Y-slope,Y-intercept,left,right),
# with the parameter running over the strictly open interval (left,right).
def certify(label,initial,expected_alive):
 cells=[initial]
 endpoints=[]
 found=set()
 for n in range(1,11):
  next_cells=[]
  for ax,cx,ay,cy,lo,hi in cells:
   roots=[]
   for a,c in ((ax,cx),(ay,cy)):
    if a:
     z=-c/a
     if lo<z<hi: roots.append(z)
   knots=[lo]+sorted(set(roots))+[hi]
   for L,R in zip(knots[:-1],knots[1:]):
    if L==float('-inf'): t=R-1 if R!=float('inf') else F(0)
    elif R==float('inf'): t=L+1
    else: t=(L+R)/2
    sx=1 if ax*t+cx>=0 else -1
    sy=1 if ay*t+cy>=0 else -1
    bx=sx*ax-ay; dx=sx*cx-cy-1
    by=ax-sy*ay; dy=cx-sy*cy+B
    if bx==0 and by==0:
     found.add((dx,dy))
    else:
     next_cells.append((bx,dx,by,dy,L,R))
  cells=next_cells
  endpoints.append((n,len(cells),len(found)))
 assert [x[1] for x in endpoints]==expected_alive,(label,endpoints)
 assert found==Q,(label,found,Q)
 assert all(any((lambda v: v in P)(v) for v in orbit(z,15)) for z in Q)
 print(label,'nonconstant cell counts',','.join(str(x[1]) for x in endpoints))
 print(label,'constant outputs',sorted(found))
 print(label,'all constant outputs enter the four-cycle')

def orbit(z,depth):
 out=[z]
 for _ in range(depth):out.append(T(out[-1]))
 return out

assert len(P)==4
assert all(T(p) in P for p in P)
certify('quadrant I first-image ray',(F(1),F(0),F(1),F(5,2),float('-inf'),float('inf')),[2,3,3,4,4,5,7,8,10,11])
certify('quadrant III first-image ray',(F(-1),F(-1),F(1),F(3,2),float('-inf'),F(0)),[3,5,6,9,10,13,15,17,22,26])
print('PASS: all exact-rational affine-cell certificates')
