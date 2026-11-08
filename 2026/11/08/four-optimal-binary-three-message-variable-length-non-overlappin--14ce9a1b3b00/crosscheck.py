"""Independent exhaustive composition-of-lengths search (no structural cutoffs).
For each triple totaling at most 16, enumerate its binary strings and reject
forbidden factors and matching proper/improper prefix-suffix overlaps.
"""
from itertools import product, combinations
from collections import Counter


def seqs(k):
    return [''.join(t) for t in product('01',repeat=k)]

def overlaps(a,b):
    # Include self-overlaps and full-word factor collisions.
    if a in b or b in a: return True
    return any(a.startswith(b[-i:]) or b.startswith(a[-i:])
               for i in range(1,min(len(a),len(b))+1))

def self_border(s):
    return any(s[:i]==s[-i:] for i in range(1,len(s)))

W={k:[s for s in seqs(k) if not self_border(s)] for k in range(2,13)}
# Each word has length >=2; sum <=16 forces largest <=12. The search
# enumerates all sorted length triples and ALL orientations (not just 0...1).
out=Counter(); codebooks=[]
for a in range(2,13):
  for b in range(a,13):
    for c in range(b,13):
      if a+b+c>16:continue
      for x in W[a]:
        for y in W[b]:
          if a==b and x>=y:continue
          if overlaps(x,y):continue
          for z in W[c]:
            if b==c and y>=z:continue
            if not overlaps(x,z) and not overlaps(y,z):
              out[(a,b,c)]+=1
              codebooks.append(tuple(sorted((x,y,z))))
assert out=={(5,5,6):4},out
assert len(set(codebooks))==4,codebooks
print('PASS complete_unrestricted_length_profiles',dict(out),
      'unique_codes',len(set(codebooks)))
