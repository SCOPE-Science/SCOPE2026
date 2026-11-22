#!/usr/bin/env python3
"""Exhaustive two-line-union shattering census in AG(2,4), standard library only.

Use GF(4)=GF(2)[w]/(w*w+w+1), encoded 0,1,w,w+1 as 0,1,2,3.
All supports are 16-bit masks, all concepts are 16-bit masks.
"""
from itertools import combinations, product
from collections import defaultdict
import json

MUL=((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))
def mul(x,y):return MUL[x][y]
points=list(product(range(4), repeat=2)); idx={p:i for i,p in enumerate(points)}
lines=[]
for slope in range(4):
    for intercept in range(4):
        lines.append((slope,sum(1<<i for i,(x,y) in enumerate(points)
            if y==mul(slope,x)^intercept)))
for xpos in range(4):
    lines.append((4,sum(1<<i for i,(x,y) in enumerate(points) if x==xpos)))
assert len(lines)==20 and len({a for _,a in lines})==20
assert all(mask.bit_count()==4 for _,mask in lines)
for i,j in combinations(range(16),2):
    assert sum(((m>>i)&1) and ((m>>j)&1) for _,m in lines)==1
classes={key:sorted({A|B for (d,A),(e,B) in combinations(lines,2) if
           key=='all' or ((d==e) if key=='parallel' else (d!=e))})
           for key in ('parallel','nonparallel','all')}
assert [len(classes[k]) for k in ('parallel','nonparallel','all')]==[30,160,190]

def trace_mask(concepts, seq):
    traces=0
    for C in concepts:
        t=sum(1<<j for j,i in enumerate(seq) if (C>>i)&1)
        traces |= 1<<t
    return traces

def shattered(concepts, seq):return trace_mask(concepts,seq)==(1<<(1<<len(seq)))-1

# 5-orbit generators preserve the finite-field affine line relation and parallelism.
def permutation(func):return tuple(idx[func(x,y)] for x,y in points)
gens=[permutation(lambda x,y:(x^1,y)),
      permutation(lambda x,y:(x^2,y)),
      permutation(lambda x,y:(x,y^1)),
      permutation(lambda x,y:(x,y^2)),
      permutation(lambda x,y:(mul(2,x),y)),
      permutation(lambda x,y:(x^y,y)),
      permutation(lambda x,y:(y,x)),
      permutation(lambda x,y:(mul(x,x),mul(y,y)))]

def image_mask(s,g):return sum(1<<g[i] for i in range(16) if (s>>i)&1)
for g in gens:
    line_images={image_mask(m,g) for _,m in lines}
    assert line_images=={m for _,m in lines}
    for d in range(5):
        images={image_mask(m,g) for e,m in lines if e==d}
        assert images in ({m for e,m in lines if e==e2} for e2 in range(5))
    for cls in classes.values(): assert {image_mask(m,g) for m in cls}==set(cls)

rows=[]; polynomials={k:[0]*7 for k in classes}; orbital={}
for size in range(6):
    remain={sum(1<<i for i in s) for s in combinations(range(16),size)}
    table=[]
    while remain:
        seed=min(remain); orbit={seed};queue=[seed]
        for s in queue:
            for g in gens:
                t=image_mask(s,g)
                if t not in orbit:
                    orbit.add(t);queue.append(t)
        assert orbit<=remain
        remain.difference_update(orbit)
        positions=[i for i in range(16) if seed>>i&1]
        trace={name:trace_mask(cons,positions) for name,cons in classes.items()}
        for name,t in trace.items():
            if t==(1<<(1<<size))-1:polynomials[name][size]+=len(orbit)
        c3=sum((m&seed).bit_count()==3 for _,m in lines)
        c4=sum((m&seed).bit_count()==4 for _,m in lines)
        xor4=sum((a^b^c^d)==0 for a,b,c,d in combinations(positions,4))
        row={'k':size,'orbit_size':len(orbit),
             'representative':[list(points[i]) for i in positions],
             'collinear_triples':c3,'full_lines':c4,'xor_zero_quadruples':xor4,
             'traces':{key:hex(val) for key,val in trace.items()},
             'shattered':{key:trace[key]==(1<<(1<<size))-1 for key in classes}}
        table.append(row)
    orbital[size]=sorted(table,key=lambda r:(r['full_lines'],r['xor_zero_quadruples'],r['collinear_triples'],r['orbit_size']))
    assert sum(row['orbit_size'] for row in table)==__import__('math').comb(16,size)
assert [polynomials[k][:6] for k in ('parallel','nonparallel','all')]==[
   [1,16,120,560,1680,0],
   [1,16,120,560,1680,2400],
   [1,16,120,560,1800,3840]
]
assert [len(orbital[k]) for k in range(6)]==[1,1,1,2,4,5]
# Direct all-support tests, not only orbit-class representatives.
for size in range(6):
    for positions in combinations(range(16),size):
        s=sum(1<<i for i in positions)
        xor_dependent=any((a^b^c^d)==0 for a,b,c,d in combinations(positions,4))
        c4=any((m&s).bit_count()==4 for _,m in lines)
        c3=sum((m&s).bit_count()==3 for _,m in lines)
        expected={
         'parallel': size<=4 and not xor_dependent,
         'nonparallel': (size<=4 and not xor_dependent) or (size==5 and c3>=1 and not xor_dependent),
         'all': (size<=4 and not c4) or (size==5 and c3>=1 and not c4)
        }
        for name in classes:
            assert shattered(classes[name],positions)==expected[name],(size,positions,name)
# All six-supports are unshattered; all larger supports fail by heredity.
for positions in combinations(range(16),6):
    for name in ('nonparallel','all'):
        assert not shattered(classes[name],positions)
assert len(classes['parallel'])<32
assert sum(r['orbit_size'] for r in orbital[5] if r['shattered']['nonparallel'])==2400
assert sum(r['orbit_size'] for r in orbital[5] if r['shattered']['all'])==3840
output={'field':'GF(2)[w]/(w^2+w+1)', 'point_order':'lex (x,y) in [0,1,w,w+1]^2',
        'concept_counts':{k:len(v) for k,v in classes.items()},'polynomial_coefficients':polynomials,
        'orbit_tables':{str(k):orbital[k] for k in orbital},
        'generators':'translations by 1,w in x,y; x->w*x; x->x+y; x<->y; Frobenius (x,y)->(x^2,y^2)'}
if __name__=='__main__':
  with open('orbit_certificate.json','w',encoding='utf-8') as f:json.dump(output,f,indent=2,ensure_ascii=True);f.write('\n')
  print('AFFINE_TWO_LINE_SHATTERING_PASS')
  print('support subsets checked:',sum(__import__('math').comb(16,k) for k in range(7)))
  print('orbits by size:',[len(orbital[k]) for k in orbital])
  print('polynomials:',{k:v[:6] for k,v in polynomials.items()})
