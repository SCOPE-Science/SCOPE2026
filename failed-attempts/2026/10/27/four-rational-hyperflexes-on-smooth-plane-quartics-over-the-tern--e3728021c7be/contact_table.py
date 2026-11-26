import json,itertools
M=json.load(open('hyperflex_flags.json'))['monomials']

def norm(v):
 a=next(x for x in v if x);return tuple(x*pow(a,-1,3)%3 for x in v)
vs=sorted(set(norm(v) for v in itertools.product(range(3),repeat=3) if any(v)))
def F_eval(c,p):return sum(a*__import__('math').prod(p[i]**m[i] for i in range(3)) for a,m in zip(c,M))%3
def der_eval(c,p,j):return sum(a*m[j]*__import__('math').prod(p[i]**(m[i]-(i==j)) for i in range(3)) for a,m in zip(c,M) if m[j]>0)%3
out={}
for code in [83262,78741,78754]:
 n=code;c=[]
 for _ in M:c.append(n%3);n//=3
 contact=[]
 for p in vs:
  if F_eval(c,p):continue
  g=tuple(der_eval(c,p,j) for j in range(3));assert any(g)
  t=[q for q in vs if sum(g[i]*q[i] for i in range(3))%3==0 and q!=p]
  q=t[0]
  poly=[F_eval(c,tuple((p[i]+u*q[i])%3 for i in range(3))) for u in range(3)]
  # evaluate coefficients in u homogeneous by multi expansion using finite differences or flags
  h=next((flag for flag in json.load(open('hyperflex_flags.json'))['flags'] if tuple(flag['P'])==p and tuple(flag['R']) not in [] and sum(g[i]*flag['Q'][i] for i in range(3))%3==0),None)
  coeff=[sum(a*b for a,b in zip(row,c))%3 for row in h['rows']] if h else None
  hyper=(coeff==[0,0,0,0])
  if hyper:contact.append({'point':p,'tangent':norm(g),'contact_coefficient':F_eval(c,tuple(h['Q'])),'coeffs0to3':coeff})
 out[str(code)]=contact
 print('REP',code,'hyperflex',len(contact),'data',contact)
open('representative_contacts.json','w').write(json.dumps(out,indent=2)+'\n')
