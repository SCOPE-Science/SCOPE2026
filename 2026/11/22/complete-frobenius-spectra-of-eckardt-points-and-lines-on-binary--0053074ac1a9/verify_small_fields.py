from verify_cubic_spectra import *
from itertools import product
MOD.update({1:0b11,3:0b1011,5:0b100101})
reps=[0x1468,0x126b,0x1486,0x1469,0x126c,0x1249,0x128d,0x128c,0x124a,0x1248]
orders=[3,2,5,3,4,1,6,3,2,1]
for a,o in zip(reps,orders):
 cyc,_=spectrum(a,2*o)
 for n in range(1,6):
  q=1<<n
  pts=[]
  for i in range(4):
   for tail in product(range(q),repeat=3-i):
    pts.append((0,)*i+(1,)+tail)
  total=0
  At=transpose(a)
  for u in pts:
   if polyF(a,u,n):continue
   ap=matv(a,u)
   v=matv(At,tuple(fourth(z,n) for z in u))
   if all(mul(ap[i],v[j],n)==mul(ap[j],v[i],n) for i in range(4) for j in range(i+1,4)):
    total+=1
  expected=sum(k*v for k,v in cyc.items() if n%k==0)
  assert total==expected,(hex(a),n,total,expected)
 print('direct passed',hex(a))
print('DIRECT_FROBENIUS_STAR_POINT_ENUMERATION_VERIFIED')
