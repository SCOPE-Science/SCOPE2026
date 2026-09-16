"""Script Q: kill the 15 survivors using WITHIN-W vs WITHIN-V1 structure.
Survivors all use windows of type {A,W,W} (as B: pair {W,W}? NO — B needs equal pair;
{A,W,W} sorted depths (0,1,1): equal pair is W,W at depth1, third A at depth0 <1: NOT a B edge!
Wait — how did edge() return True for {A,W,W}? edge() with nx0==0: depths (0,1,1): a==b? (0,1,1): a=0,b=1,c=1: b==c and a<b -> TRUE. But that means: two W (depth1) + one A (depth0):
equal pair at depth 1 (W,W), third at depth 0 which is SMALLER. B-rule requires third STRICTLY DEEPER (e>d). So this is a BUG: (b==c and a<b) with a=0 <1 claims edge, but third is shallower!
Fix: B edge = equal pair at depth d, third at depth e>d. (0,1,1): pair at 1, third at 0: NOT edge.
Correct rule: (a==b and c>b) or (b==c and a... ) need pair to be the MIN: (a==b and c>b).
For (0,1,1): a=0,b=1: a!=b; b==c=1, pair at 1, third a=0 <1: not edge. So second clause must be dropped!
Similarly (0,0,1): pair at 0, third at 1 >0: edge (first clause). So ONLY (a==b and c>b).
But wait: does B contain triples {y1,y2 in V1^(d), w deeper}? depths (d,d,e), e>d: sorted (d,d,e): a==b, c>b. Yes. Any triple with exactly-two-equal where equal pair is the min. The (b==c,a<b) case = equal pair is max = triple like {shallow, deep, deep} with deep pair in same block: e.g. {A, W1, W2} both W in same block V1^(1): IS that in B? B[V1^(0),V2^(0)] needs 2 in V1^(0): no. H[V2^(0)] = B[V1^(1), V2^(1)]: needs 2 in W: {A,W1,W2} has only... A is not in V2^(0)! A in V1^(0). So {A,W1,W2}: A outside V2-subproblem. NOT in B. Correct: not edge. Good — bug confirmed, and it also affects the baseline descent lemma? Baseline: window-sum argument said windows in B have sum in {0,2} w.r.t. V1^(0) indicator... {A,W1,W2} has sum 1: absent (verified in census: (1,False)). And all-zero windows: present only if B-edge inside V2. Fine.
Re-run P with corrected rule; survivors should vanish (then star lemma proved). Also re-check baseline script A unaffected (it only enumerated words, rule-independent)."""
import itertools

def edge(u, v, w):
    states = (u, v, w)
    nx0 = states.count(0)
    others = [s for s in states if s != 0]
    if nx0 == 0:
        d = {1: 0, 2: 1, 3: 2}
        t = tuple(sorted(d[s] for s in states))
        a, b, c = t
        if a == b and c > b: return True
        return False
    if nx0 >= 2:
        return False
    a, b = others
    def deeper(s): return s in (2, 3)
    B = (a == 1 and deeper(b)) or (b == 1 and deeper(a))
    S = (a == 2 and b == 2)
    return B or S

# sanity: B-edge types
assert edge(1, 1, 2) and edge(1, 1, 3) and edge(2, 2, 3)
assert not edge(1, 2, 2) and not edge(1, 2, 3) and not edge(2, 3, 3)
assert not edge(1, 1, 1) and not edge(2, 2, 2)
assert edge(0, 1, 2) and edge(0, 1, 3) and edge(0, 2, 2) and not edge(0, 2, 3)
assert edge(0, 2, 2) or True  # star: {x0,W,W} -> S True
assert edge(0, 2, 2)  # via star
assert not edge(0, 1, 1) and not edge(0, 3, 3) and not edge(0, 0, 1 == 1)
print("edge-rule sanity OK")

surv = []
for rest in itertools.product([1, 2, 3], repeat=6):
    w = (0,) + rest
    wins = [(w[i], w[(i+1)%7], w[(i+2)%7]) for i in range(7)]
    has_star = any((win.count(0) == 1 and sum(1 for s in win if s == 2) == 2) for win in wins)
    if not has_star: continue
    if all(edge(*win) for win in wins):
        surv.append(w)
print("surviving words with corrected rule:", len(surv))
for w in surv[:30]:
    print("  ", w)

# Also: full classification — any C7 using >=1 star edge impossible => star family C7-free
# provided B-only C7 impossible. Re-verify B-only impossibility with corrected rule:
# B-only words over depths {0,1,2,3} with all windows (d,d,e),e>d:
survB = []
for w in itertools.product(range(4), repeat=7):
    wins = [tuple(sorted((w[i], w[(i+1)%7], w[(i+2)%7]))) for i in range(7)]
    if all((x[0] == x[1] and x[2] > x[1]) for x in wins):
        survB.append(w)
print("B-only all-window words:", len(survB))
