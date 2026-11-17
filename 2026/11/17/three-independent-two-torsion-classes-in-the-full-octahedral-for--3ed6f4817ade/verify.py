"""Exact integer chain computation for a symmetric octahedral forest complex.

Uses Python standard library only. The cellular quotient is obtained from
strict chains of nonempty forest faces. All algebraic cancellations use
integer unit pivots; the remaining matrix is checked by its integral minors.
"""
from collections import defaultdict
from itertools import combinations, permutations, product
from math import gcd
from functools import reduce
import heapq


def data():
    vertices=range(6)
    edges=tuple((i,j) for i in vertices for j in range(i+1,6)
                if i//2 != j//2)
    perms=[]
    for a in permutations(range(3)):
        for s in product(range(2),repeat=3):
            p=[2*a[i//2]+((i%2)^s[i//2]) for i in vertices]
            perms.append(tuple(edges.index(tuple(sorted((p[i],p[j]))))
                               for i,j in edges))
    faces=[]
    for k in range(1,6):
        for f in combinations(range(len(edges)),k):
            parent=list(vertices)
            def root(u):
                while parent[u]!=u: u=parent[u]
                return u
            for e in f:
                u,v=edges[e]
                u,v=root(u),root(v)
                if u==v: break
                parent[u]=v
            else: faces.append(f)
    assert len(edges)==12 and len(perms)==len(set(perms))==48
    assert [sum(len(f)==k for f in faces) for k in range(1,6)]==[12,66,212,408,384]
    return edges,perms,faces


def quotient_complex(faces,group):
    faceidx={f:i for i,f in enumerate(faces)}
    actions=[[faceidx[tuple(sorted(g[v] for v in f))]
              for f in faces] for g in group]
    supers={f:[q for q in faces if len(q)>len(f) and set(f).issubset(q)]
            for f in faces}
    flags=set()
    def grow(chain):
        flags.add(tuple(faceidx[f] for f in chain))
        for q in supers[chain[-1]]: grow(chain+[q])
    for f in faces: grow([f])
    bydim=defaultdict(list)
    for flag in flags: bydim[len(flag)-1].append(flag)
    reps=[]
    orbit_id={}
    for d in sorted(bydim):
        remaining=set(bydim[d]); res=[]
        while remaining:
            flag=min(remaining)
            orbit={tuple(a[v] for v in flag) for a in actions}
            for item in orbit:orbit_id[item]=len(res)
            remaining.difference_update(orbit)
            res.append(flag)
        reps.append(res)
    bd=[]
    for d in range(1,len(reps)):
        matrix={}
        for j,flag in enumerate(reps[d]):
            for i in range(d+1):
                row=orbit_id[flag[:i]+flag[i+1:]]
                matrix[row,j]=matrix.get((row,j),0)+(-1)**i
        bd.append({k:v for k,v in matrix.items() if v})
    assert [len(q) for q in reps]==[38,441,1594,2148,960]
    # Independently check that every consecutive boundary composes to zero.
    cols=[None]+[{j:{} for j in range(len(reps[d]))}
                 for d in range(1,len(reps))]
    for d,mat in enumerate(bd,1):
        for (r,c),v in mat.items(): cols[d][c][r]=v
    for d in range(2,len(reps)):
        for c,rvals in cols[d].items():
            result={}
            for k,v in rvals.items():
                for r,w in cols[d-1][k].items():
                    result[r]=result.get(r,0)+v*w
            assert all(v==0 for v in result.values())
    return reps,bd


def modular_rank(ncols,matrix,p):
    columns=[{} for _ in range(ncols)]
    for (r,c),v in matrix.items():
        if v%p: columns[c][r]=v%p
    piv={}
    for original in columns:
        col=dict(original)
        while col:
            k=max(col)
            u=col[k]
            if k not in piv:
                inv=pow(u,-1,p)
                piv[k]={r:v*inv%p for r,v in col.items()}
                break
            for r,v in piv[k].items():
                x=(col.get(r,0)-u*v)%p
                if x: col[r]=x
                else:col.pop(r,None)
    return len(piv)


class IntegerReduction:
    def __init__(self,reps,boundaries):
        self.top=len(reps)-1
        self.cells=[set(range(len(q))) for q in reps]
        self.B=[None]
        self.R=[None]
        self.pivots=[]
        self.count=0
        for d in range(1,self.top+1):
            B={c:{} for c in self.cells[d]}
            R={r:{} for r in self.cells[d-1]}
            for (r,c),v in boundaries[d-1].items():
                B[c][r]=v; R[r][c]=v
            self.B.append(B);self.R.append(R)
        for d in range(1,self.top+1):
            for c,col in self.B[d].items():
                for r,v in col.items():
                    if abs(v)==1: self.add(d,c,r)

    def add(self,d,c,r):
        if c not in self.cells[d] or r not in self.cells[d-1]:return
        if abs(self.B[d][c].get(r,0))!=1:return
        score=(len(self.B[d][c])-1)*(len(self.R[d][r])-1)
        heapq.heappush(self.pivots,(score,d,c,r))

    def cancel(self,d,c,r):
        v=self.B[d][c][r]
        assert abs(v)==1
        column=dict(self.B[d][c]); row=dict(self.R[d][r])
        for x,w in row.items():
            if x==c:continue
            other=self.B[d][x]
            for y,u in column.items():
                if y==r:continue
                z=other.get(y,0)-u*w//v
                if z:
                    other[y]=z;self.R[d][y][x]=z
                else:
                    other.pop(y,None);self.R[d][y].pop(x,None)
            del other[r]
            for y,z in other.items():
                if abs(z)==1:self.add(d,x,y)
        for y in column:del self.R[d][y][c]
        del self.B[d][c];del self.R[d][r]
        self.cells[d].remove(c);self.cells[d-1].remove(r)
        if d>1:
            for y in self.B[d-1][r]:del self.R[d-1][y][r]
            del self.B[d-1][r]
        if d<self.top:
            for x in list(self.R[d+1][c]):
                del self.B[d+1][x][c]
                for y,z in self.B[d+1][x].items():
                    if abs(z)==1:self.add(d+1,x,y)
            del self.R[d+1][c]
        for x in row:
            if x!=c:
                for y,z in self.B[d][x].items():
                    if abs(z)==1:self.add(d,x,y)
        self.count+=1

    def execute(self):
        while self.pivots:
            score,d,c,r=heapq.heappop(self.pivots)
            if c not in self.cells[d] or r not in self.cells[d-1]:continue
            if abs(self.B[d][c].get(r,0))!=1:continue
            actual=(len(self.B[d][c])-1)*(len(self.R[d][r])-1)
            if actual!=score:
                self.add(d,c,r);continue
            self.cancel(d,c,r)
        assert self.count==2586
        assert [len(x) for x in self.cells]==[1,0,0,3,5]
        rows=sorted(self.cells[3]); columns=sorted(self.cells[4])
        a=[[self.B[4][c].get(r,0) for c in columns] for r in rows]
        return a


def determinant(a):
    n=len(a)
    if n==1:return a[0][0]
    return sum((-1)**j*a[0][j]*determinant([row[:j]+row[j+1:] for row in a[1:]])
               for j in range(n))


def invariant_factors(a):
    divisors=[1]
    for size in range(1,4):
        g=0
        for rs in combinations(range(len(a)),size):
            for cs in combinations(range(len(a[0])),size):
                m=[[a[r][c] for c in cs] for r in rs]
                g=gcd(g,abs(determinant(m)))
        divisors.append(g)
    return [divisors[i]//divisors[i-1] for i in range(1,4)]


def main():
    edges,group,faces=data()
    reps,bd=quotient_complex(faces,group)
    mod2=[modular_rank(len(reps[d+1]),mat,2) for d,mat in enumerate(bd)]
    mod3=[modular_rank(len(reps[d+1]),mat,3) for d,mat in enumerate(bd)]
    assert mod2==[37,404,1190,955]
    assert mod3==[37,404,1190,958]
    reducer=IntegerReduction(reps,bd)
    a=reducer.execute()
    assert invariant_factors(a)==[2,2,2]
    assert all(all(v==0 for v in reducer.B[d][c].values())
               for d in range(1,4) for c in reducer.B[d])
    print('graph_edges',len(edges),'group_order',len(group))
    print('forest_faces',len(faces),'forest_face_vector',[12,66,212,408,384])
    print('quotient_cells',[len(q) for q in reps])
    print('boundary_square_zero',True)
    print('mod2_boundary_ranks',mod2)
    print('mod3_boundary_ranks',mod3)
    print('unit_cancellations',reducer.count)
    print('residual_cells',[len(c) for c in reducer.cells])
    print('residual_d4',a)
    print('smith_nonzero_factors',invariant_factors(a))
    print('homology','H0=Z,H1=0,H2=0,H3=(Z/2)^3,H4=Z^2')

if __name__=='__main__':main()
