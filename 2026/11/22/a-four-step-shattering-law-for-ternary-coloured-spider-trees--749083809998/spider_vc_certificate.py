"""Finite, exactly reproducible certificate for ternary-colouring shattering of three-arm spiders.

No third-party packages.  Run: python3 spider_vc_certificate.py
A vertex query tests equality to one of three named colours; 0 encodes no query.
"""
from itertools import product
from functools import lru_cache

PALETTE = 7  # three-bit mask

def neighbour(mask):
    """Colours allowed at a predecessor adjacent to a vertex allowed 'mask'."""
    assert 1 <= mask <= 7
    return 7 if mask.bit_count() >= 2 else 7 ^ mask

def extend(signature, mark):
    """Add one vertex towards the hub. mark=0,1,2,3 (0: unqueried)."""
    out = set()
    for mask in signature:
        base = neighbour(mask)
        if mark == 0:
            out.add(base)
        else:
            singleton = 1 << (mark - 1)
            out.update((base & singleton, base & (7 ^ singleton)))
    if 0 in out:
        return None  # some binary trace is impossible on this arm
    return tuple(sorted(out))

def next_dp(dp):
    result = {}
    for state, score in dp.items():
        for mark in range(4):
            dest = extend(state, mark)
            if dest is not None:
                result[dest] = max(result.get(dest, -1000000), score + bool(mark))
    return result

def all_dp(up_to):
    arr = [{(7,): 0}]
    for _ in range(up_to):
        arr.append(next_dp(arr[-1]))
    return arr

@lru_cache(maxsize=None)
def hub_admissible(sig1, sig2, sig3, mark):
    for m1, m2, m3 in product(sig1, sig2, sig3):
        common = neighbour(m1) & neighbour(m2) & neighbour(m3)
        if not common:
            return False
        if mark:
            bit = 1 << (mark - 1)
            if not common & bit or not common & (7 ^ bit):
                return False
    return True

def vc(a, b, c, dp):
    ans = -1
    for s1, w1 in dp[a].items():
        for s2, w2 in dp[b].items():
            for s3, w3 in dp[c].items():
                for mark in range(4):
                    if hub_admissible(s1, s2, s3, mark):
                        ans = max(ans, w1 + w2 + w3 + bool(mark))
    return ans

def spider_edges(a, b, c):
    edges = []
    arms = []
    nxt = 1
    for L in (a, b, c):
        arm = tuple(range(nxt, nxt + L))
        arms.append(arm)
        for i, v in enumerate(arm):
            edges.append((0 if i == 0 else arm[i - 1], v))
        nxt += L
    return edges, arms

def colour_query_masks(a,b,c):
    edges,_ = spider_edges(a,b,c)
    n=1+a+b+c
    good=[cols for cols in product(range(1,4),repeat=n) if all(cols[u]!=cols[v] for u,v in edges)]
    all_mask=(1<<len(good))-1
    masks={(v,t):sum(1<<i for i,col in enumerate(good) if col[v]==t) for v in range(n) for t in range(1,4)}
    return all_mask,masks

def brute_trace(marks, all_mask, query_masks):
    leaves=[all_mask]
    for v,c in enumerate(marks):
        if c==0:continue
        q=query_masks[v,c]
        next_leaves=[]
        for m in leaves:
            p=m&q; neg=m&(all_mask^q)
            if not p or not neg:return False
            next_leaves.extend((p,neg))
        leaves=next_leaves
    return True

def signature_trace(a,b,c,marks):
    _, arms = spider_edges(a,b,c)
    signatures = []
    for arm in arms:
        state = (7,)
        for v in reversed(arm):
            state = extend(state,marks[v])
            if state is None:
                return False
        signatures.append(state)
    return hub_admissible(*signatures,marks[0])

def run_checks():
    dp = all_dp(15)
    assert len(dp[3]) == 19
    state_list = sorted(dp[4]); states = set(state_list)
    assert len(states) == 20
    for j in range(4,16):
        assert set(dp[j]) == states, ('nonclosed',j)
    assert all(dp[8][s] == dp[4][s]+3 for s in states)
    for j in range(4,12):
        assert all(dp[j+4][s] == dp[j][s]+3 for s in states)
    print('STATE_CERTIFICATE_PASS: 20 states stable from length 4; four-step shift exactly +3')
    print('id|masks|D4|D8|transition for marks 0,1,2,3 (X means infeasible)')
    ids={s:i for i,s in enumerate(state_list)}
    for i, s in enumerate(state_list):
        trans = [ids[t] if (t:=extend(s,j)) is not None else 'X' for j in range(4)]
        print(i,','.join(str(x) for x in s),dp[4][s],dp[8][s],*trans,sep='|')
    cases=[];support_count=0
    for a in range(1,5):
        for b in range(a,5):
            for c in range(b,5):
                if a+b+c>6:continue
                cases.append((a,b,c))
                all_mask,query_masks=colour_query_masks(a,b,c)
                best=-1
                for marks in product(range(4),repeat=1+a+b+c):
                    x=signature_trace(a,b,c,marks)
                    y=brute_trace(marks,all_mask,query_masks)
                    assert x==y,(a,b,c,marks,x,y)
                    support_count+=1
                    if x:
                        best=max(best,sum(bool(t) for t in marks))
                assert best==vc(a,b,c,dp),(a,b,c,best,vc(a,b,c,dp))
    print('DIRECT_COLOURING_ENUMERATION_PASS:',len(cases),'spider graphs;',support_count,'marked-query sets')
    print('CASES',cases)
    for m in range(1,13):
        expected = 1+(9*m+3)//4
        assert vc(m,m,m,dp)==expected,(m,vc(m,m,m,dp),expected)
    print('BALANCED_VALUES_PASS: 1..12:',[vc(m,m,m,dp) for m in range(1,13)])
    for a,b,c in [(1,2,3),(2,3,5),(4,5,6),(7,7,7),(1,8,10),(6,9,12)]:
        for i in range(3):
            v=(a,b,c); plus=list(v); plus[i]+=4
            if v[i]>=4 and max(plus)<=15:
                assert vc(*plus,dp)==vc(*v,dp)+3,(v,plus)
    print('SPIDER_PERIOD_COMPARISONS_PASS')
    print('ALL_CHECKS_PASS')

if __name__ == '__main__':
    run_checks()
