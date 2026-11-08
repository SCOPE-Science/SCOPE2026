"""Exact classification of smooth F_2-plane-filling quintic pencils.

Python 3.10+ and SymPy 1.14.0. Usage:
  python verify_pencils_groebner.py
  python verify_pencils_groebner.py --write-csv
  python verify_pencils_groebner.py --verify-csv pencil_orbits.csv

The polynomial mask has 21 bits, one per monomial X^a Y^b Z^c with
(a,b,c) enumerated by descending a, then descending b, a+b+c=5.
All arithmetic in the Jacobian Gröbner tests is exactly modulo 2.
"""
from __future__ import annotations
import argparse
import csv
import itertools
from collections import Counter
import sympy as sp

MON = tuple((a,b,5-a-b) for a in range(5,-1,-1) for b in range(5-a,-1,-1))
assert len(MON) == 21
POINTS = list(itertools.product((0,1), repeat=3))[1:]
X,Y,Z = sp.symbols('X Y Z')


def nullspace_basis():
    rows=[]
    for p in POINTS:
        rows.append(sum((1 << j) for j,(a,b,c) in enumerate(MON)
                        if (not a or p[0]) and (not b or p[1]) and (not c or p[2])))
    pivot={}
    for row in rows:
        v=row
        while v:
            j=(v & -v).bit_length()-1
            if j in pivot: v ^= pivot[j]
            else:
                pivot[j]=v
                break
    free=tuple(j for j in range(21) if j not in pivot)
    basis=[]
    for j in free:
        v=1 << j
        for i in sorted(pivot, reverse=True):
            if (v & pivot[i]).bit_count() % 2: v ^= 1 << i
        basis.append(v)
    assert len(basis)==14
    assert all((b & row).bit_count()%2==0 for b in basis for row in rows)
    return free,tuple(basis)


def multiply_poly(A,B):
    out=set()
    for a in A:
        for b in B:
            e=tuple(a[i]+b[i] for i in range(3))
            if e in out:out.remove(e)
            else:out.add(e)
    return out


def substitute(poly_mask,m):
    linear=[{tuple(1 if j==i else 0 for j in range(3))
             for i in range(3) if (m[t] >> i) & 1} for t in range(3)]
    powers=[[{(0,0,0)}] for _ in range(3)]
    for i in range(3):
        for _ in range(5):powers[i].append(multiply_poly(powers[i][-1],linear[i]))
    out=set()
    for j,e in enumerate(MON):
        if (poly_mask >> j)&1:
            term=multiply_poly(multiply_poly(powers[0][e[0]],powers[1][e[1]]),powers[2][e[2]])
            out.symmetric_difference_update(term)
    return sum(1 << MON.index(e) for e in out)


def make_group_actions(free,basis):
    def coord(mask):return sum(((mask >> j)&1) << i for i,j in enumerate(free))
    actions=[]
    # These elementary substitutions generate GL_3(F_2) of order 168.
    for mat in ((3,2,4),(2,1,4),(2,4,1)):
        columns=[coord(substitute(v,mat)) for v in basis]
        action=[0]*16384
        for i in range(1,16384):
            b=i & -i
            action[i]=action[i ^ b] ^ columns[b.bit_length()-1]
        actions.append(action)
    return actions


def orbits_of_nonzero_vectors(actions):
    seen=set();orbits=[]
    for x in range(1,16384):
        if x in seen:continue
        Q={x};stack=[x];seen.add(x)
        while stack:
            a=stack.pop()
            for action in actions:
                b=action[a]
                if b not in seen:
                    seen.add(b);stack.append(b);Q.add(b)
        orbits.append((min(Q),Q))
    assert len(seen)==16383 and len(orbits)==139
    return orbits


def geometrically_smooth(mask):
    F=sum((X**a*Y**b*Z**c for i,(a,b,c) in enumerate(MON) if (mask >> i)&1),sp.S.Zero)
    grad=[sp.diff(F,v) for v in (X,Y,Z)]
    for unit,variables in ((X,(Y,Z)),(Y,(X,Z)),(Z,(X,Y))):
        loc=[h.subs(unit,1) for h in (F,*grad)]
        ideal=sp.groebner(loc,*variables,modulus=2,order='lex')
        if not any(p.is_one for p in ideal.polys):return False
    return True


def classify():
    free,basis=nullspace_basis()
    masks=[0]*16384
    for k in range(1,16384):
        low=k & -k
        masks[k]=masks[k ^ low] ^ basis[low.bit_length()-1]
    acts=make_group_actions(free,basis)
    orbits=orbits_of_nonzero_vectors(acts)
    smooth=set();types={};curve_reps=[]
    for rep,orb in orbits:
        if geometrically_smooth(masks[rep]):
            idx=len(curve_reps)
            curve_reps.append((masks[rep],len(orb)))
            smooth.update(orb)
            for k in orb:types[k]=idx
    assert len(smooth)==1512 and len(curve_reps)==10
    pencils=set()
    for u in smooth:
        for v in smooth:
            if u<v:
                w=u^v
                if w in smooth and v<w:pencils.add((u,v,w))
    assert len(pencils)==16800
    # Independent Walsh–Hadamard cubic-moment count of ordered triples
    # (u,v,u+v) in the smooth set. Each pencil contributes six triples.
    wh=[int(i in smooth) for i in range(16384)]
    for stride in (1 << j for j in range(14)):
        for origin in range(0,16384,2*stride):
            for j in range(stride):
                a,b=wh[origin+j],wh[origin+j+stride]
                wh[origin+j]=a+b
                wh[origin+j+stride]=a-b
    assert sum(h**3 for h in wh)==1_651_507_200
    assert sum(h**3 for h in wh)//16384==6*len(pencils)==100_800
    seen=set();classes=[]
    for p in sorted(pencils):
        if p in seen:continue
        Q={p};stack=[p];seen.add(p)
        while stack:
            abc=stack.pop()
            for act in acts:
                s=tuple(sorted(act[a] for a in abc))
                if s not in seen:
                    seen.add(s);stack.append(s);Q.add(s)
        sz=len(Q)
        assert sz in (168,56)
        member_types=tuple(sorted(types[u] for u in p))
        classes.append((p,sz,member_types))
    assert len(seen)==16800 and len(classes)==108
    assert Counter(sz for _,sz,_ in classes)==Counter({168:96,56:12})
    dist=Counter()
    for abc in pencils:
        distinct=len(set(types[a] for a in abc))
        dist[distinct]+=1
    assert dist==Counter({3:13104,2:3024,1:672})
    for p,sz,t in classes:
        assert (sz==56)==(len(set(t))==1)
    return masks,curve_reps,classes,dist


def build_rows(masks,classes):
    result=[]
    for p,sz,t in classes:
        row=(str(masks[p[0]]),str(masks[p[1]]),str(masks[p[2]]),
             str(sz),str(168//sz),*(str(i) for i in t))
        assert int(row[0]) ^ int(row[1]) == int(row[2])
        result.append(row)
    return result


def csv_text(rows):
    import io
    buf=io.StringIO(newline='')
    writer=csv.writer(buf,lineterminator='\n')
    writer.writerow(('F_mask','G_mask','F_plus_G_mask','orbit_size','stabilizer_order',
                     'member_type_1','member_type_2','member_type_3'))
    writer.writerows(rows)
    return buf.getvalue()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-csv',action='store_true')
    parser.add_argument('--verify-csv',default='')
    args=parser.parse_args()
    masks,curve_reps,classes,dist=classify()
    csv_out=csv_text(build_rows(masks,classes))
    if args.write_csv:
        with open('pencil_orbits.csv','w',encoding='utf-8',newline='') as f:f.write(csv_out)
    if args.verify_csv:
        with open(args.verify_csv,encoding='utf-8',newline='') as f:actual=f.read()
        assert actual==csv_out
    print('QUINTIC_PENCILS_GROEBNER_PASS',16384,139,1512,16800,108,96,12,
          dist[1],dist[2],dist[3])
    print('CURVE_TYPE_REP_MASKS',curve_reps)
    print('SYMMETRIC_PENCIL_TYPE_ORBITS',dict(sorted(Counter(t[0] for _,sz,t in classes if sz==56).items())))


if __name__=='__main__':main()
