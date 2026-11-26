"""Independent exact-rational checks for short periodic orbits of a farthest-line projection map.

Run: python3 verify_cycles.py
No third-party dependencies; this finite check supports but does not substitute for the proof.
"""
from fractions import Fraction as F
from itertools import product


def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def mul(t,a): return (t*a[0],t*a[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]


def geometry(v):
    A=(F(0),F(0)); B=(F(1),F(0)); C=(F(1,2),v)
    lines=((A,B),(B,C),(C,A))
    return lines


def on_line(p,line):
    start,end=line
    return cross(sub(p,start),sub(end,start))==0


def coord(p,line):
    start,end=line
    d=sub(end,start)
    return dot(sub(p,start),d)/dot(d,d)


def point(t,line):
    start,end=line
    return add(start,mul(t,sub(end,start)))


def project(p,line):
    return point(coord(p,line),line)


def distance2(p,line):
    start,end=line
    d=sub(end,start)
    z=cross(sub(p,start),d)
    return z*z/dot(d,d)


def T(p,lines):
    containing=[i for i,line in enumerate(lines) if on_line(p,line)]
    assert containing, 'point not in union of lines'
    # If the point is a vertex it lies on two lines; both offer the same sole
    # nontrivial projection to the third supporting line.
    others=[i for i in range(3) if i not in containing]
    if len(others)==1:
        return project(p,lines[others[0]])
    if len(others)==2:
        a,b=others
        da,db=distance2(p,lines[a]),distance2(p,lines[b])
        if da==db:
            return p  # equality: fixed by the map's definition
        return project(p,lines[a if da>db else b])
    raise AssertionError('No point lies on all three lines')


def enumerate_cycles(v,n):
    lines=geometry(v)
    cycles=set()
    for seq in product(range(3),repeat=n):
        if any(seq[i]==seq[(i+1)%n] for i in range(n)):
            continue
        # Compose projections in the source/target line parameter by
        # evaluating the affine return map at t=0,1; avoid numerical solves.
        def return_t(t):
            p=point(t,lines[seq[0]])
            for j in range(n):
                target=seq[(j+1)%n]
                p=project(p,lines[target])
            return coord(p,lines[seq[0]])
        b=return_t(F(0)); aa=return_t(F(1))-b
        if aa==1: continue
        start=point(b/(1-aa),lines[seq[0]])
        orbit=[start]
        for _ in range(n):
            orbit.append(T(orbit[-1],lines))
        if orbit[-1]!=start: continue
        if any(orbit[j]==start for j in range(1,n)):continue
        # Compare physical coordinates, not itineraries: a point can be
        # represented by two sides if it is a vertex.
        key=min(tuple(orbit[j:n]+orbit[:j]) for j in range(n))
        cycles.add(key)
    return cycles


def verify(v,expected3,expected4):
    lines=geometry(v)
    cyc3=enumerate_cycles(v,3)
    cyc4=enumerate_cycles(v,4)
    assert len(cyc3)==expected3,(v,'period3',len(cyc3))
    assert len(cyc4)==expected4,(v,'period4',len(cyc4))
    # Direct closed-form candidates, independently replayed under T.
    s2=v*v+F(1,4)
    D=v*v+F(1,2)
    x=F(1)/(4*D); h=v/(2*D)
    four=((x,F(0)),(F(1)-x,h),(F(1)-x,F(0)),(x,h))
    is_four=all(T(four[i],lines)==four[(i+1)%4] for i in range(4))
    assert is_four==(expected4==1)
    m=F(1)/(1+2*s2)
    tri=((m,F(0)),(1-m/F(2),m*v),(m,2*m*v))
    is_tri=all(T(tri[i],lines)==tri[(i+1)%3] for i in range(3))
    assert is_tri==(expected3==2)
    print(f'v={v}: primitive period-3 orbits={len(cyc3)}, period-4 orbits={len(cyc4)}; exact branch checks OK')


if __name__=='__main__':
    for v,e3,e4 in [
        (F(51,100),2,1),(F(11,20),2,1),
        (F(3,5),2,1),(F(63,100),2,1),
        (F(16,25),2,0),(F(2,3),2,0),
        (F(4,5),2,0),(F(1),2,0),
        (F(5,4),2,0),(F(13,10),0,0),
        (F(3,2),0,0),(F(2),0,0),
    ]:
        verify(v,e3,e4)
    print('PASS: exact-rational enumeration and independent branch checks across 12 parameter samples.')
