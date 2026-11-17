import numpy as np,itertools,math
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from collections import Counter

def enumerate_facets(q):
 n=q+2
 e=np.eye(n)
 vertices=np.array([sig*(e[i]-e[j]) for i in (0,1) for j in range(2,n) for sig in (1,-1)])
 potentials=[('A+',np.r_[1,-1,np.zeros(q)]),('A-',np.r_[-1,1,np.zeros(q)])]
 for s in itertools.product((-1,1),repeat=q): potentials.append((('B',s),np.r_[0,0,s]))
 idxs=[]
 for label,pot in potentials:
  vs=np.flatnonzero(np.isclose(vertices@pot,1.0))
  assert np.all(vertices@pot<=1+1e-10),(q,label)
  assert len(vs)==2*q,(q,label,len(vs))
  idxs.append(vs)
  assert np.linalg.matrix_rank(vertices[vs[1:]]-vertices[vs[0]],tol=1e-9)==q
 expected=Counter()
 for a,(label,pot) in enumerate(potentials):
  for b in range(a+1,len(potentials)):
   label2,pot2=potentials[b]
   share=np.intersect1d(idxs[a],idxs[b])
   dim=np.linalg.matrix_rank(vertices[share[1:]]-vertices[share[0]],tol=1e-9) if len(share)>1 else 0 if len(share)==1 else -1
   if dim!=q-1: continue
   w1=pot-np.mean(pot); w2=pot2-np.mean(pot2)
   cosine=np.dot(w1,w2)/(np.linalg.norm(w1)*np.linalg.norm(w2))
   if str(label).startswith('A') or str(label2).startswith('A'):
    assert abs(cosine)<1e-10
    expected['AB']+=1
   else:
    s=label[1]; t=label2[1]
    assert sum(x!=y for x,y in zip(s,t))==1
    r=max(sum(x>0 for x in s),sum(x>0 for x in t))
    m=2*r-q
    c=((q-2)*(q+2)-m*(m-2))/np.sqrt((q*(q+2)-m*m)*(q*(q+2)-(m-2)**2))
    assert abs(c-cosine)<1e-10, (q,label,label2,c,cosine)
    expected[r]+=1
 assert expected['AB']==2**(q+1)
 for r in range(1,q+1): assert expected[r]==r*math.comb(q,r), (q,r,expected[r])
 return vertices,idxs,expected

for q in range(2,7):
 vs,fs,counts=enumerate_facets(q)
 U=null_space(np.ones((1,q+2)))
 hull=ConvexHull(vs@U)
 # Each triangulated hull facet hyperplane must equal a predicted facet plane (normal up to scaling)
 predicted=[]
 for l in fs:
  pts=vs[l]@U
  p=np.linalg.svd(pts[1:]-pts[0])[2][-1]
  if np.max((vs@U-pts[0])@p)>1e-8: p=-p
  predicted.append((p,-p@pts[0]))
 for eq in hull.equations:
  assert any(np.linalg.norm(eq[:q+1]-np.r_[p])<1e-8 and abs(eq[-1]-h)<1e-8 for p,h in predicted),(q,eq)
 print('q=',q,'facets=',len(fs),'ridges=',sum(counts.values()),'hull_simplices=',len(hull.simplices),'PASS')
for q in range(2,301):
    assert sum(r*math.comb(q,r) for r in range(1,q+1))==q*2**(q-1)
    prev=None
    for r in range(1,q+1):
        h=2*r-q-1
        ab=(q*(q+2)-(h+1)**2)*(q*(q+2)-(h-1)**2)
        d=q*q-3-h*h
        assert ab-d*d==4*(q+2)*(q*q-1-h*h)
        if q>=3:
            assert d>0
            cur=2*math.sqrt((q+2)*(q*q-1-h*h))/d
            if r<=q//2:
                if prev is not None: assert cur<prev+1e-12
                prev=cur
print('K2Q_RIDGE_SPECTRUM_PASS q_hull=2..6 q_algebra=2..300')
