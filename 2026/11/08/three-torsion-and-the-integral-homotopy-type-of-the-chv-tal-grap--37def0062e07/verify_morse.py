"""Reproducible exact integral Morse certificate for the Chvatal matching complex.
Python 3 standard library only. Invoke: python3 verify_morse.py
"""
from collections import Counter,defaultdict,deque
from functools import lru_cache

EDGES=((0,1),(0,4),(0,6),(0,9),(1,2),(1,5),(1,7),(2,3),(2,6),(2,8),(3,4),(3,7),(3,9),(4,5),(4,8),(5,10),(5,11),(6,10),(6,11),(7,8),(7,11),(8,10),(9,10),(9,11))
M=len(EDGES)


def faces():
    result=[]
    def visit(i,vertices,mask):
        if i==M:
            result.append(mask)
            return
        visit(i+1,vertices,mask)
        a,b=EDGES[i]
        occupied=(1<<a)|(1<<b)
        if not(vertices&occupied):
            visit(i+1,vertices|occupied,mask|(1<<i))
    visit(0,0,0)
    return set(result)


def rank_mod(a,p):
    rows=[[(int(x)%p) for x in row] for row in a]
    if not rows:return 0
    nr,nc=len(rows),len(rows[0]);r=0
    for c in range(nc):
        pivot=next((i for i in range(r,nr) if rows[i][c]),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        inv=pow(rows[r][c],-1,p)
        rows[r]=[(x*inv)%p for x in rows[r]]
        for i in range(r+1,nr):
            f=rows[i][c]
            if f:rows[i]=[(x-f*y)%p for x,y in zip(rows[i],rows[r])]
        r+=1
        if r==nr:break
    return r


def determinant_bareiss(a):
    a=[list(map(int,row)) for row in a]
    n=len(a);sign=1;den=1
    if n==0:return 1
    for k in range(n-1):
        if a[k][k]==0:
            other=next((i for i in range(k+1,n) if a[i][k]),None)
            if other is None:return 0
            a[k],a[other]=a[other],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%den==0
                a[i][j]=numerator//den
        for i in range(k+1,n):a[i][k]=0
        den=pivot
    return sign*a[-1][-1]


def main():
    assert len(EDGES)==24 and len(set(EDGES))==24
    assert all(a<b and 0<=a<b<12 for a,b in EDGES)
    assert all(sum(v in edge for edge in EDGES)==4 for v in range(12))
    assert all(not set(((i,j),(j,k),(i,k)))<=set(EDGES) for i in range(12) for j in range(i+1,12) for k in range(j+1,12))
    F=faces()
    counts=Counter(x.bit_count()-1 for x in F)
    assert [counts[k] for k in range(-1,6)]==[1,24,204,752,1175,628,52]
    # For each edge index, perform every currently available toggle in the nonempty poset.
    U=F-{0}
    paired={}
    for k in range(M):
        for lower in sorted((x for x in U if not(x>>k&1)),key=lambda x:(x.bit_count(),x)):
            upper=lower|(1<<k)
            if lower in U and upper in U:
                paired[lower]=upper
                U.remove(lower);U.remove(upper)
    assert len(paired)==1385
    assert Counter(x.bit_count()-1 for x in U)=={0:1,3:46,4:18}
    indeg={x:0 for x in F if x};adj={x:[] for x in indeg}
    incidence_count=0
    for upper in indeg:
        for i in range(M):
            if upper>>i&1:
                lower=upper^(1<<i)
                if not lower:continue
                if paired.get(lower)==upper:a,b=lower,upper
                else:a,b=upper,lower
                adj[a].append(b);indeg[b]+=1;incidence_count+=1
    queue=deque(x for x in indeg if indeg[x]==0)
    seen=0
    while queue:
        x=queue.popleft();seen+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:queue.append(y)
    assert seen==len(F)-1==2835
    assert incidence_count==10816

    critical_three=sorted(x for x in U if x.bit_count()==4)
    critical_four=sorted(x for x in U if x.bit_count()==5)
    @lru_cache(None)
    def project(face):
        # Reduction to critical 3-faces via gradient paths in dimensions (3,4).
        if face in U:
            return {face:1} if face.bit_count()==4 else {}
        if face not in paired:
            # An upper simplex paired with a 2-face contributes zero to C_3^Morse.
            return {}
        upper=paired[face]
        bits=[j for j in range(M) if upper>>j&1]
        i=bits.index((upper^face).bit_length()-1)
        unit=(-1)**i
        out=defaultdict(int)
        for k,j in enumerate(bits):
            g=upper^(1<<j)
            if g==face:continue
            for h,c in project(g).items():
                out[h]-=unit*((-1)**k)*c
        return {h:c for h,c in out.items() if c}
    B=[]
    for upper in critical_four:
        coefficients=defaultdict(int)
        for i,j in enumerate(k for k in range(M) if upper>>k&1):
            for h,c in project(upper^(1<<j)).items():
                coefficients[h]+=(-1)**i*c
        B.append([coefficients.get(h,0) for h in critical_three])
    B=[list(row) for row in zip(*B)]
    assert (len(B),len(B[0]))==(46,18)
    assert max(abs(x) for row in B for x in row)==1
    selected=(0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,17,18,26)
    determinant=determinant_bareiss([B[i] for i in selected])
    assert abs(determinant)==3
    assert (rank_mod(B,2),rank_mod(B,3),rank_mod(B,5))==(18,17,18)
    # All maximal minors vanish mod 3, and an actual determinant is +/-3.
    # Hence the gcd of maximal minors is exactly 3 and Smith factors are 1^17,3.
    assert sum(bool(a) for row in B for a in row)==118
    print('vertices=12 graph_edges=24 degree=4 triangles=0')
    print('matching_complex_faces_nonempty=2835')
    print('face_vector_0_to_5=24,204,752,1175,628,52')
    print('morse_pairs=1385 critical_0=1 critical_3=46 critical_4=18')
    print('hasse_covers=10816 topologically_sorted=2835 acyclic=True')
    print('morse_matrix_rows=46 cols=18 nonzero=118 max_abs=1')
    print('selected_minor_rows='+','.join(map(str,selected))+' determinant='+str(determinant))
    print('morse_boundary_ranks_F2_F3_F5=18,17,18')
    print('smith_nonzero_diagonal=17x1,1x3')
    print('reduced_H3_integral=Z^28+Z/3 all_other_reduced_H=0')
    print('CHVATAL_MATCHING_THREE_TORSION_MORSE_PASS')

if __name__=='__main__':main()
