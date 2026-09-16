# Characterize i=3 contributions: |W|=4, comp-1 in {1,2,3}. For Delta, when is G[W] disconnected with W spanning >=2 colors?
# Mono W impossible at (3,3,3,3)? sizes 3: |W|=4 non-mono always. So ALL beta_{3,4}(Delta) comes from mixed W.
# For Gamma: 116. Total C(12,4)=495. So ~23% of 4-sets disconnected.
# Structural: G[W] disconnected mixed means some color-split with no cross edges between parts. Cross nonedges in Gamma: 12 cross + 12 mono = 24 missing of 66.
# For a general Delta with partition sizes n_j: MISSING edges include all mono (sum C(nj,2)) + some cross. FEWER total missing than Gamma? join has 18 missing <24 yet lower strand. So strand is about missing-edge LAYOUT: Gamma's missing edges are concentrated to disconnect many W.
# Upper-bound idea: comp(G[W])-1 = sum over components... For each W, comp-1 <= (number of missing cross pairs + mono pairs within W)/max(1,...)? Each extra component C needs >= |C|*(|W|-|C|) missing pairs? For bipartition-ish: if G[W] has components C1..Ct, missing pairs >= sum_{p<q}|Cp||Cq| =: M(W). And comp-1 = t-1 <= M(W) with equality iff t=2 and... t-1 vs M: M >= C(t,2) >= t-1. So beta_{i,i+1} <= sum_W M(W) = (total missing pairs)*C(n-2,i-1). Same weak bound as before (m*C(n-2,i-1), m=24: i=3 -> 24*C(10,2)=1080 vs 116). Factor ~9 slack. The slack: each disconnected W counted once per missing pair but has MANY missing pairs (e.g., W with pieces 2+2: M=4, counted 1). To tighten need to divide by typical M. M depends on W profile; balanced constraints force M large? For Gamma most disconnected W have M=4+? If avg M ~ 9, bound ~120. Hmm plausible but proving "avg M >= m*C(n-2,i-1)/Gamma_beta" for all Delta = essentially the whole problem. BLOCKED on analytic side.
# Let's at least quantify for Gamma: distribution of M over disconnected W.
import itertools, sys
sys.path.insert(0,'output/artifacts')
from flipsearch import stacked_chain
facets,colors,n=stacked_chain(4,2)
nbr=[0]*n
for F in facets:
    for a,b in itertools.combinations(sorted(F),2):
        nbr[a]|=(1<<b); nbr[b]|=(1<<a)
from collections import Counter
h=Counter(); tot=Counter()
for mask in range(1,1<<n):
    W=[v for v in range(n) if (mask>>v)&1]
    s=len(W)
    if s not in (2,3,4,5): continue
    rem=mask; comp=0
    while rem:
        comp+=1
        u=(rem&(-rem)).bit_length()-1
        stack=(1<<u); seen=0
        while stack:
            w=(stack&(-stack)).bit_length()-1
            stack^=(1<<w)
            if (seen>>w)&1: continue
            seen|=(1<<w)
            stack|=(nbr[w]&mask&~seen)
        rem&=~seen
    if comp>1:
        # missing pairs within W
        M=sum(1 for a,b in itertools.combinations(W,2) if not (nbr[a]>>b)&1)
        h[(s,comp-1,M)]+=1
    tot[s]+=1
for k in sorted(h): print(k,h[k])
