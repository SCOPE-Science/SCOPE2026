"""Exact-rational cell certificate for the crystallographic greedy planar walk.
Run: python3 verify.py  (Python 3.9+, standard library only).

All arithmetic in the finite certificate uses fractions, never floating point.
"""
from fractions import Fraction as Q
from itertools import combinations
from collections import Counter

# Rectangular fundamental-coordinate boundaries, then all actual switching lines.
LINES = ((1,0,0),(1,0,1),(0,1,0),(0,1,1),
         (2,-1,0),(2,-1,1),(-1,2,0),(-1,2,1),(1,1,1))
CUTS = LINES[4:]


def eval_line(p, line):
    a,b,c=line
    return a*p[0]+b*p[1]-c


def sign(x):
    return (x>0)-(x<0)


def polygon_area2(poly):
    return sum(p[0]*q[1]-q[0]*p[1]
               for p,q in zip(poly, poly[1:]+poly[:1]))


def clipped(poly, line, orientation):
    out=[]
    for p,q in zip(poly, poly[1:]+poly[:1]):
        v=orientation*eval_line(p,line)
        w=orientation*eval_line(q,line)
        if v>=0:
            out.append(p)
        if v*w<0:
            out.append(tuple((w*x-v*y)/(w-v) for x,y in zip(p,q)))
        elif v<0 and w==0:
            out.append(q)
    unique=[]
    for p in out:
        if p not in unique:
            unique.append(p)
    return unique if len(unique)>=3 and polygon_area2(unique)!=0 else []


def arrangement():
    square=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    polygons=[square]
    for line in CUTS:
        polygons=[piece for poly in polygons for orientation in (1,-1)
                  if (piece:=clipped(poly,line,orientation))]
        assert sum(map(polygon_area2,polygons))==2
    assert len(polygons)==10
    faces=[]
    for poly in polygons:
        p=tuple(sum((vertex[i] for vertex in poly),Q(0))/len(poly) for i in (0,1))
        assert all(eval_line(p,l)!=0 for l in CUTS)
        faces.append(p)
    signatures={tuple(sign(eval_line(p,l)) for l in CUTS) for p in faces}
    assert len(signatures)==10
    vertices=set()
    for (a,b,c),(d,e,f) in combinations(LINES,2):
        det=a*e-b*d
        if det:
            p=(Q(c*e-b*f,det),Q(a*f-c*d,det))
            if 0<=p[0]<=1 and 0<=p[1]<=1:
                vertices.add(p)
    edges=set()
    for line in LINES:
        pts=sorted(p for p in vertices if eval_line(p,line)==0)
        for p,q in zip(pts,pts[1:]):
            midpoint=((p[0]+q[0])/2,(p[1]+q[1])/2)
            if 0<=midpoint[0]<=1 and 0<=midpoint[1]<=1:
                edges.add(midpoint)
    assert (len(faces),len(edges),len(vertices))==(10,19,10)
    # Distinct open-face, open-edge and vertex strata; exact line-sign signatures
    allpoints=faces+list(edges)+list(vertices)
    fullsignatures={tuple(sign(eval_line(p,l)) for l in LINES) for p in allpoints}
    assert len(fullsignatures)==39
    return [('face',p) for p in faces]+[('edge',p) for p in sorted(edges)]+[('vertex',p) for p in sorted(vertices)]


def step(r,s,state,phase,denom):
    # Triangular-lattice basis (1,omega), omega=exp(2*pi*i/3).
    directions={3:((1,0),(0,1),(-1,-1)),
                6:((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))}[denom]
    u,v=directions[phase]
    m,n=state
    a,b=r+m,s+n
    twice_dot=2*a*u+2*b*v-a*v-b*u
    if twice_dot==0:
        return None  # equal distances: trajectory stops
    z=sign(twice_dot)
    return (m-z*u,n-z*v)


def iterate_block(r,s,state,denom,length=None):
    if length is None:
        length=denom
    for phase in range(length):
        state=step(r,s,state,phase,denom)
        if state is None:
            return None
    return state


def certify(denom):
    # All eventual phase-zero states of radius <=6 or <=12 are included in
    # these fixed offset squares (not just states sampled at representatives).
    bound=8 if denom==3 else 15
    tally=Counter()
    max_precycle=0
    union=set()
    for kind,(r,s) in arrangement():
        done={}
        local=set()
        for m in range(-bound,bound+1):
            for n in range(-bound,bound+1):
                start=(m,n)
                state=start
                path=[]
                positions={}
                while state is not None and state not in done and state not in positions:
                    positions[state]=len(path)
                    path.append(state)
                    state=iterate_block(r,s,state,denom)
                    assert len(path)<=1000
                if state is None:
                    fate=0  # terminates on a tie
                elif state in done:
                    fate=done[state]
                else:
                    cyc=path[positions[state]:]
                    if denom==3:
                        assert len(cyc) in (1,2)
                        fate=3*len(cyc)
                    else:
                        assert len(cyc)==1
                        half=iterate_block(r,s,cyc[0],6,3)
                        fate=3 if half==cyc[0] else 6
                    for node in cyc:
                        done[node]=fate
                for node in reversed(path):
                    done[node]=fate
                assert fate in (0,3,6)
                if fate:
                    local.add(fate)
                    union.add(fate)
                max_precycle=max(max_precycle,len(path))
        tally[(kind,tuple(sorted(local)))]+=1
    assert union=={3,6}
    assert max_precycle<=6
    print('denominator',denom,'strata',dict(sorted(tally.items())),
          'max_new_block_states_on_path',max_precycle)
    return tally


def witnesses():
    # Strict non-terminating examples show both possible minimal periods occur.
    for q,r,s,period in ((3,Q(1,9),Q(1,9),3),
                         (3,Q(1,9),Q(2,3),6),
                         (6,Q(1,9),Q(1,9),3),
                         (6,Q(5,9),Q(5,9),6)):
        state=(0,0)
        seq=[]
        for k in range(48):
            seq.append(state)
            state=step(r,s,state,k%q,q)
            assert state is not None
        assert all(seq[k]==seq[k+period] for k in range(24,40))
        if period==6:
            assert any(seq[k]!=seq[k+3] for k in range(24,40))
        print('witness',q,str(r),str(s),period)

if __name__=='__main__':
    certify(3)
    certify(6)
    witnesses()
    print('EXHAUSTIVE_RATIONAL_STRATA_CERTIFICATE_OK')
