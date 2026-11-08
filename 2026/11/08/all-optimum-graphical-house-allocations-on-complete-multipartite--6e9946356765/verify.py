#!/usr/bin/env python3
"""Exact brute-force checks for multipartite graphical allocations."""
from itertools import combinations
from collections import Counter
from math import factorial

def words(sizes):
    if len(sizes)==1:
        yield (0,)*sizes[0]
        return
    n=sum(sizes)
    for locs in combinations(range(n),sizes[0]):
        mask=set(locs)
        for rest in words(sizes[1:]):
            iterator=iter(rest)
            yield tuple(0 if k in mask else 1+next(iterator) for k in range(n))

def direct_cost(word, values):
    return sum(abs(values[i]-values[j]) for i in range(len(word))
               for j in range(i+1,len(word)) if word[i]!=word[j])

def priorities(sizes):
    return sorted([ (v-2*k-1, i) for i,v in enumerate(sizes) for k in range(v)],reverse=True)

def predicted(sizes):
    d=Counter(w for w,_ in priorities(sizes))
    count=1
    for c in d.values(): count*=factorial(c)
    return count

def optimum_word(word,sizes):
    vals=priorities(sizes)
    return all(word[i] in {part for weight,part in vals if weight==v}
               for i,v in enumerate([w for w,_ in vals])) and all(
         # exact ordered marginal comparison, including ties
         ((sizes[part]-1-2*sum(word[j]==part for j in range(i)))==vals[i][0])
         for i,part in enumerate(word))

def compositions(total,parts):
    if parts==1:yield (total,);return
    for i in range(1,total-parts+2):
        for tail in compositions(total-i,parts-1):yield (i,)+tail

def run():
    instances=profiles=0
    for n in range(3,10):
      for q in range(3,min(n,5)+1):
       for sizes in compositions(n,q):
        # Enumerate one representative for each part-size multiset; labels remain fixed.
        if sizes!=tuple(sorted(sizes)):continue
        ws=list(words(sizes));p=predicted(sizes)
        assert sum(optimum_word(w,sizes) for w in ws)==p,(sizes,'priority count')
        for gaps in [tuple(1 for _ in range(n-1)),tuple(2+(i*i+3*i)%7 for i in range(n-1))]:
            values=[0]
            for d in gaps: values.append(values[-1]+d)
            costs=[direct_cost(w,values) for w in ws]
            mini=min(costs)
            good={w for w,c in zip(ws,costs) if c==mini}
            predicted_good={w for w in ws if optimum_word(w,sizes)}
            assert good==predicted_good,(sizes,gaps,'mismatch',good^predicted_good)
            delta=[values[i+1]-values[i] for i in range(n-1)]
            marg=sorted([v-2*k-1 for v in sizes for k in range(v)],reverse=True)
            expected=sum(delta[r-1]*(r*(n-r)-sum(marg[:r])) for r in range(1,n))
            assert mini==expected,(sizes,'cost formula',mini,expected)
            instances+=1;profiles+=len(ws)
    assert predicted((2,2,2))==36
    assert predicted((1,2,3))==2
    assert predicted((2,2,3))==4
    print('PASS',instances,'exact direct-cost instances;',profiles,'complete group-label assignments tested')

if __name__=='__main__':run()
