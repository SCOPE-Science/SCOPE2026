"""Independent finite-geometric and equation-based census of Schroeter configuration V.
Run: python3 CHECKER.py. Uses only the Python standard library.
"""
from itertools import combinations
from pathlib import Path
import csv

TRIPLES = {tuple(sorted(t)) for t in ((1,2,4),(1,3,8),(1,7,9),(2,3,7),
 (2,5,9),(0,3,5),(4,5,6),(0,4,8),(6,7,8),(0,6,9))}

class Field:
    def __init__(self, p, m=1):
        self.p,self.m,self.q=p,m,p**m
        self.irred = {(2,1):(0,1),(3,1):(0,1),(5,1):(0,1),
                      (7,1):(0,1),(2,2):(1,1,1)}[(p,m)]
        self.add_table=[[self._add(a,b) for b in range(self.q)] for a in range(self.q)]
        self.mul_table=[[self._mul(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inv=[None]+[next(b for b in range(1,self.q) if self.mul_table[a][b]==1)
                         for a in range(1,self.q)]
    def digits(self,n):return [(n//self.p**k)%self.p for k in range(self.m)]
    def enc(self,co):return sum((x%self.p)*self.p**k for k,x in enumerate(co))
    def _add(self,a,b):return self.enc([(u+v)%self.p for u,v in zip(self.digits(a),self.digits(b))])
    def _mul(self,a,b):
        z=[0]*(2*self.m-1)
        for i,u in enumerate(self.digits(a)):
            for j,v in enumerate(self.digits(b)):z[i+j]=(z[i+j]+u*v)%self.p
        for k in range(2*self.m-2,self.m-1,-1):
            for j in range(self.m):z[k-self.m+j]=(z[k-self.m+j]-z[k]*self.irred[j])%self.p
        return self.enc(z[:self.m])
    def add(self,u,v):return self.add_table[u][v]
    def mul(self,u,v):return self.mul_table[u][v]
    def neg(self,u):return self.enc([-x for x in self.digits(u)])
    def sub(self,u,v):return self.add(u,self.neg(v))
    def cross(self,u,v):
        M,S=self.mul,self.sub
        return (S(M(u[1],v[2]),M(u[2],v[1])),
                S(M(u[2],v[0]),M(u[0],v[2])),
                S(M(u[0],v[1]),M(u[1],v[0])))
    def dot(self,u,v):
        return self.add(self.add(self.mul(u[0],v[0]),self.mul(u[1],v[1])),self.mul(u[2],v[2]))
    def norm(self,u):
        if not any(u):return None
        pivot=next(k for k,x in enumerate(u) if x)
        return tuple(self.mul(x,self.inv[u[pivot]]) for x in u)
    def projective_points(self):
        return sorted({self.norm((x,y,z)) for x in range(self.q)
                     for y in range(self.q) for z in range(self.q) if (x,y,z)!=(0,0,0)})

O=(1,0,0); P=(0,1,0); Q=(0,0,1); R=(1,1,1)
def build(F, six, seven):
    cross,norm=F.cross,F.norm
    def intersection(a,b,c,d):return norm(cross(cross(a,b),cross(c,d)))
    arr={1:O,2:P,3:Q,5:R,6:six,7:seven}
    arr[4]=intersection(O,P,R,six)
    arr[8]=intersection(O,Q,six,seven)
    arr[9]=intersection(O,seven,P,R)
    if any(arr[k] is None for k in (4,8,9)):return None
    arr[0]=intersection(Q,R,arr[4],arr[8])
    if arr[0] is None or len(set(arr.values()))!=10:return None
    return tuple(arr[k] for k in range(10))

def incidence(F,points):
    return {tri for tri in combinations(range(10),3)
            if F.dot(F.cross(points[tri[0]],points[tri[1]]),points[tri[2]])==0}

def geometric_enumeration(F):
    result=[]
    for six in F.projective_points():
        for seven in F.projective_points():
            if seven[0]!=0:continue  # point 7 lies on the line through 2 and 3
            points=build(F,six,seven)
            if points is not None and incidence(F,points)==TRIPLES:
                result.append(points)
    return result

def sturmfels_polynomial(F,a,b,t):
    M,A,N=F.mul,F.add,F.neg
    t2,a2,b2=M(t,t),M(a,a),M(b,b)
    terms=(b,N(M(t,b)),N(M(t2,M(a2,a))), M(M(t,a2),b),
           M(t2,a2),N(M(M(t,a),b)),M(t,b2),N(b2))
    v=0
    for x in terms:v=A(v,x)
    return v

def equation_enumeration(F):
    roots=distinct=0; good=[]
    for a in range(F.q):
        for b in range(F.q):
            for t in range(1,F.q):
                if sturmfels_polynomial(F,a,b,t)!=0:continue
                roots+=1
                points=build(F,(1,a,b),(0,1,t))
                if points is None:continue
                distinct+=1
                triples=incidence(F,points)
                assert TRIPLES.issubset(triples), ('derived cubic failed',F.q,a,b,t)
                if triples==TRIPLES:good.append((a,b,t,points))
    return roots,distinct,good

def check(output='CENSUS.csv'):
    records=[]
    for p,m in [(2,1),(3,1),(2,2),(5,1),(7,1)]:
        F=Field(p,m)
        roots,distinct,good=equation_enumeration(F)
        geometric=geometric_enumeration(F)
        assert sorted([x[3] for x in good])==sorted(geometric)
        row=(F.q,roots,distinct,len(good))
        records.append(row)
        print('q=%d: equation roots=%d; distinct candidates=%d; strict realizations=%d'%row)
        if F.q==7:
            expected=(5,6,6,((1,1,5),(1,0,0),(0,1,0),(0,0,1),(1,3,0),
                              (1,1,1),(1,5,6),(0,1,6),(1,0,4),(1,6,1)))
            assert good==[expected]
            assert len(incidence(F,good[0][3]))==10
    assert records==[(2,4,0,0),(3,13,0,0),(4,22,0,0),(5,31,0,0),(7,50,1,1)]
    path=Path(output)
    if path.exists():
        with path.open('r',encoding='utf-8',newline='') as existing:
            prior=list(csv.reader(existing))
        assert prior==[['field_order','sturmfels_roots','distinct_candidates','strict_realizations']]+[list(map(str,row)) for row in records], 'existing certificate mismatch'
    with open(output,'w',encoding='utf-8',newline='') as fh:
        writer=csv.writer(fh,lineterminator='\n')
        writer.writerow(['field_order','sturmfels_roots','distinct_candidates','strict_realizations'])
        writer.writerows(records)
    print('CERTIFIED_MINIMUM_Q_7_UNIQUE_LABELED_ORBIT')
if __name__=='__main__':check()
