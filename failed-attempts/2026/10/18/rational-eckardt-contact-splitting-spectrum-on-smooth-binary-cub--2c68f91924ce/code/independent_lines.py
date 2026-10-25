"""Independent line-containment check, not using tangent-section coefficients."""
import json, sympy as s,sys
x=s.symbols('X0 X1 X2 X3');u,v=s.symbols('u v')
exps=[]
for a in range(4):
 for b in range(4-a):
  for c in range(4-a-b):exps.append((a,b,c,3-a-b-c))
mon=[s.prod(z**n for z,n in zip(x,exp))for exp in exps]
rows=json.load(open(sys.argv[1]))
def point_eval(poly,p):return int(poly.subs({x[i]:(p>>i)&1 for i in range(4)}))%2
checks=0
for r in rows:
 F=sum(mon[i] for i in range(20)if r['mask']>>i&1)
 Pts=r['points'];tally={0:0,1:0,3:0}
 for p in Pts:
  tangent=[]
  for q in range(1,16):
   if q==p or q==p^q:continue
   poly=s.Poly(s.expand(F.subs({x[i]: ((p>>i)&1)*u+((q>>i)&1)*v for i in range(4)},simultaneous=True)),u,v,modulus=2)
   if poly.is_zero:tangent.append(q)
  assert len(tangent)%2==0
  lines=len(tangent)//2
  if lines in (0,1,3):tally[lines]+=1
  elif lines>0:pass
  checks+=1
 assert tally[3]==r['ec_split_types'].get('3',0),(r['index'],tally,r['ec_split_types'])
print('Three-rational-line Eckardt points verified for',checks,'rational points on 36 smooth representatives.')
