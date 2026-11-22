#!/usr/bin/env python3
"""Exact finite integral Morse certificate for two local Kneser complexes.
No dependencies beyond Python's standard library; all faces rebuilt from definition.
"""
import itertools, collections

T=list(itertools.combinations(range(7),3))
assert len(T)==35
neighbors=[]
for i,t in enumerate(T):
 mask=sum(1<<j for j,s in enumerate(T) if i!=j and set(t).intersection(s))
 neighbors.append(mask)

def faces_for(forbidden):
 allowed=((1<<35)-1)
 for i in forbidden:allowed &= ~(1<<i)
 faces=set()
 def visit(face,candidates):
  while candidates:
   b=candidates&-candidates;candidates ^=b
   i=b.bit_length()-1
   newface=face|b;faces.add(newface)
   visit(newface,candidates & neighbors[i])
 visit(0,allowed)
 return faces

def certificate(name,forbidden,trial,expected_total,expected_critical):
 faces=faces_for(forbidden)
 assert len(faces)==expected_total,(name,len(faces))
 active=faces.copy();mate={}
 order=[i for i in range(35) if i not in forbidden]
 if trial==2:
  order=[17,25,21,34,3,30,1,5,11,8,15,18,28,31,16,13,14,29,19,2,23,7,20,9,10,22,26,24,32,27,12,33,6,4]
  assert sorted(order)==[i for i in range(35) if i not in forbidden]
 for v in order:
  b=1<<v
  lower=[s for s in active if not s&b and s|b in active]
  for s in lower:
   q=s|b
   assert s not in mate and q not in mate
   mate[s]=q;mate[q]=s
  active.difference_update(lower)
  active.difference_update(s|b for s in lower)
 counts=dict(sorted(collections.Counter(s.bit_count()-1 for s in active).items()))
 assert counts==expected_critical,(name,counts)
 assert len(mate)+len(active)==len(faces)
 # Exhaustive directed Hasse graph acyclicity check: paired incidence
 # points upward, every other codimension-one incidence points downward.
 state={};count=0
 for root in faces:
  if root in state:continue
  state[root]=1; stack=[(root,None)];count+=1
  while stack:
   x,it=stack[-1]
   if it is None:
    m=mate.get(x)
    out=[];sub=x
    while sub:
     b=sub&-sub;sub^=b
     y=x^b
     if y and y!=m:out.append(y)
    if m is not None and m.bit_count()>x.bit_count():out.append(m)
    stack[-1]=(x,iter(out));it=stack[-1][1]
   try:y=next(it)
   except StopIteration:state[x]=2;stack.pop();continue
   sy=state.get(y,0)
   if sy==1:raise AssertionError((name,'directed Hasse cycle',x,y))
   if sy==0:state[y]=1;count+=1;stack.append((y,None))
 assert count==len(faces)
 print(f'{name}: {len(faces)} nonempty faces; {len(mate)//2} Morse pairs; critical dimensions {counts}; directed Hasse graph acyclic; PASS')

# Fix a named triple: the lexicographically first (0,1,2).
center=0
forbidden_link={center}|{i for i in range(35) if i!=center and set(T[i]).isdisjoint(T[center])}
assert len(forbidden_link)==5
certificate('link',forbidden_link,0,277713,{0:1,5:6,8:4})
certificate('deletion',{center},2,1000971,{0:1,6:23,9:3})
print('Integral Morse boundaries vanish: no consecutive critical dimensions; all verified.')
