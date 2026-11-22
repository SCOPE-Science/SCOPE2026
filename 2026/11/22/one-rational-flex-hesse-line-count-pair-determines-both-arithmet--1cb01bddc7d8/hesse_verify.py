"""Exact, standalone verification of the nine-flex/twelve-line Frobenius table.
Only the Python standard library is required. No curve-specific arithmetic is assumed.
"""
from itertools import product, combinations
from collections import defaultdict, Counter
import csv
import io

F3 = range(3)
POINTS = tuple(product(F3, repeat=2))
POINT_INDEX = {p: i for i, p in enumerate(POINTS)}

# Independent constructions of the twelve triples: linear equations and
# three-point cosets of one-dimensional additive subgroups.
LINES_EQ = {
    tuple(sorted(i for i, (x, y) in enumerate(POINTS)
                 if (a*x + b*y) % 3 == c))
    for a,b in POINTS if (a,b)!=(0,0) for c in F3
}
LINES_COSET = {
    tuple(sorted((i, POINT_INDEX[((x+u)%3,(y+v)%3)],
                     POINT_INDEX[((x+2*u)%3,(y+2*v)%3)])))
    for i,(x,y) in enumerate(POINTS)
    for u,v in POINTS if (u,v)!=(0,0)
}
assert LINES_EQ == LINES_COSET and len(LINES_EQ) == 12
LINES = tuple(sorted(LINES_EQ))
LINE_INDEX = {line: i for i, line in enumerate(LINES)}
assert Counter(x for line in LINES for x in line) == Counter({i:4 for i in range(9)})

def cycles(p):
    seen=set(); parts=[]
    for x in range(len(p)):
        if x in seen: continue
        y=x; count=0
        while y not in seen:
            seen.add(y); y=p[y]; count+=1
        parts.append(count)
    return tuple(sorted(parts))

def fixed(p):
    return sum(x==i for i,x in enumerate(p))

def part_text(t):
    return ' '.join('%s^%s'%(k,m) for k,m in sorted(Counter(t).items()))

def affine_action(A,b):
    a,c,d,e=A
    bp,bq=b
    p=tuple(POINT_INDEX[((a*x+c*y+bp)%3,(d*x+e*y+bq)%3)] for x,y in POINTS)
    # independent affine line-action test via image sets
    l=tuple(LINE_INDEX[tuple(sorted(p[i] for i in line))] for line in LINES)
    assert sorted(p)==list(range(9)) and sorted(l)==list(range(12))
    # Independent fixed-line formula: for a fixed one-dimensional subgroup
    # H and coset representative v, A(H)=H and (A-I)v+b belongs to H.
    fixed_by_formula = 0
    for line in LINES:
        base=POINTS[line[0]]
        H={( (POINTS[i][0]-base[0])%3,
             (POINTS[i][1]-base[1])%3) for i in line}
        stable={((a*u+c*v)%3,(d*u+e*v)%3) for u,v in H}==H
        disp=((a*base[0]+c*base[1]+bp-base[0])%3,
              (d*base[0]+e*base[1]+bq-base[1])%3)
        fixed_by_formula += bool(stable and disp in H)
    assert fixed_by_formula == fixed(l)
    return p,l

SPECTRA=defaultdict(list)
ELEMENTS=[]
for A in product(F3,repeat=4):
    a,b,c,d=A
    det=(a*d-b*c)%3
    if det==0: continue
    for translation in POINTS:
        p,l=affine_action(A,translation)
        key=(det,cycles(p),cycles(l))
        SPECTRA[key].append((A,translation))
        ELEMENTS.append((A,translation,det,p,l))
assert len(ELEMENTS)==432 and len(SPECTRA)==10

# All spectra in the same determinant class have different single-field
# counts. In different determinant classes coincidences are permitted.
TABLE=[]
for (det,point_cycle,line_cycle),group in SPECTRA.items():
    f=point_cycle.count(1)
    h=line_cycle.count(1)
    TABLE.append((det,f,h,point_cycle,line_cycle,len(group)))
for det,n in ((1,7),(2,3)):
    t=[row for row in TABLE if row[0]==det]
    assert len(t)==n
    assert len({(row[1],row[2]) for row in t})==n
assert sum(row[5] for row in TABLE)==432
assert any(row[0]==1 and row[1:3]==(1,0) for row in TABLE)
assert any(row[0]==2 and row[1:3]==(1,0) for row in TABLE)
assert all(row[0]!=2 or row[1] in (0,1,3) for row in TABLE)

# An independent group-conjugacy census confirms that some matrix classes
# have coincident joint spectra, and confirms class sizes, not just 432 elements.
G=[(*A,*b) for A,b,_,_,_ in ELEMENTS]
def inv(g):
    a,b,c,d,u,v=g
    det=(a*d-b*c)%3
    i=(d*det%3,-b*det%3,-c*det%3,a*det%3)
    return (*i,(-i[0]*u-i[1]*v)%3,(-i[2]*u-i[3]*v)%3)
def mul(g,h):
    a,b,c,d,u,v=g;A,B,C,D,U,V=h
    return ((a*A+b*C)%3,(a*B+b*D)%3,(c*A+d*C)%3,(c*B+d*D)%3,
            (a*U+b*V+u)%3,(c*U+d*V+v)%3)
seen=set(); classes=[]
for g in G:
    if g in seen: continue
    cls={mul(mul(h,g),inv(h)) for h in G}
    assert not (cls&seen)
    classes.append(cls)
    seen.update(cls)
assert len(seen)==432 and len(classes)==11
assert sorted(len(c) for c in classes)==sorted([1,8,9,24,36,48,54,54,54,72,72])

# Exact finite-field sample verification. Each curve has a rational flex at
# infinity and its rational flexes equal E(F_7)[3]. If group order is prime
# to 3, exactly one flex is rational. The four roots of psi3 detect rational
# cyclic order-three subgroups (stable lines in E[3]), yielding h values.
p=7
def point_count(a,b):
    return 1+sum(sum(y*y%p==(x*x*x+a*x+b)%p for y in range(p)) for x in range(p))
def division_roots(a,b):
    return tuple(x for x in range(p) if (3*x**4+6*a*x*x+12*b*x-a*a)%p==0)
examples=[]
for a,b,h_expect,order in [(1,1,0,5),(0,3,1,13),(0,5,4,7)]:
    assert (4*a*a*a+27*b*b)%p!=0
    nr=division_roots(a,b)
    assert len(nr)==h_expect and point_count(a,b)==order and order%3!=0
    examples.append((a,b,order,nr))

TABLE.sort(key=lambda row:(row[0],-row[1],-row[2]))
output=io.StringIO()
writer=csv.writer(output,lineterminator='\n')
writer.writerow(['det_mod_3','rational_flexes','rational_hesse_lines',
                 'flex_cycles','hesse_line_cycles','affine_element_count'])
for d,f,h,pcy,lcy,size in TABLE:
    writer.writerow([d,f,h,part_text(pcy),part_text(lcy),size])
if __name__=='__main__':
    print(output.getvalue(),end='')
    print('VERIFIED: 9 flexes, 12 lines, 432 affine maps, 11 conjugacy classes, 10 spectra, 7/3 determinant split, all count pairs distinguish, F7 sharpness examples',flush=True)
