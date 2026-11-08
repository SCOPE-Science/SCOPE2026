"""Exact finite checks for unit-chore restricted-assignment Prop1 thresholds.
Run with Python 3.10+: python verify.py
"""
from itertools import combinations, product
from functools import lru_cache


def eligible_subsets(m):
    return [c for k in range(2,m+1) for c in combinations(range(m),k)]


def transition(state, candidates, recipient, denominator=12):
    k=len(candidates)
    assert denominator % k == 0 and recipient in candidates
    return tuple(state[i] - (denominator//k if i in candidates else 0)
                 + (denominator if i == recipient else 0) for i in range(len(state)))


def verify_three_agent_invariant():
    D=6
    states=[p for p in product(range(-5,6),repeat=3) if sum(p)==0]
    assert len(states)==91
    checked=0
    for s in states:
        for C in eligible_subsets(3):
            r=min(C,key=lambda i:(s[i],i))
            t=transition(s,C,r,D)
            if max(abs(x) for x in s) <= 5:
                assert max(abs(x) for x in t) <=5,(s,C,t)
                checked+=1
    valid=[p for p in states if max(abs(x) for x in p)<=5]
    assert len(valid)==91
    return len(valid),checked


def verify_four_job_greedy():
    m=4;D=12;sets=eligible_subsets(m)
    count=0
    for horizon in range(5):
        for seq in product(sets,repeat=horizon):
            d=[0]*m;loads=[0]*m;shares=[0]*m
            for C in seq:
                chosen=min(C,key=lambda i:(d[i],i))
                for i in C:shares[i]+=D//len(C)
                loads[chosen]+=1
                d=list(transition(tuple(d),C,chosen,D))
                assert all(d[i]==D*loads[i]-shares[i] for i in range(m))
                assert all(loads[i]==0 or D*(loads[i]-1)<=shares[i] for i in range(m)),(seq,d)
            count+=1
    assert count == sum(11**h for h in range(5))
    return count


def verify_game():
    D=12;m=4; sets=eligible_subsets(m)
    @lru_cache(None)
    def can_survive(sorted_state,horizon):
        if horizon==0:return True
        for C in sets:
            if not any(max(next_state:=transition(sorted_state,C,j,D)) <=D
                       and can_survive(tuple(sorted(next_state)),horizon-1)
                       for j in C):
                return False
        return True
    assert can_survive((0,0,0,0),4)
    assert not can_survive((0,0,0,0),5)
    return can_survive.cache_info()


def verify_adversary():
    # Adversary: 1 all four; 2 and 3 exclude first recipient;
    # if recipients 2 and 3 differ, 4 uses those two;
    # 5 uses recipient 1 and recipient 4.
    D=12;m=4
    traces=0;first_fail=[0]*6
    for a in range(4):
        d=transition((0,)*m,(0,1,2,3),a,D)
        E=tuple(i for i in range(m) if i!=a)
        for b in E:
            t2=transition(d,E,b,D)
            if max(t2)>D:
                first_fail[2]+=1;continue
            for c in E:
                t3=transition(t2,E,c,D)
                if max(t3)>D:
                    first_fail[3]+=1;traces+=1;continue
                assert c!=b
                for x in (b,c):
                    t4=transition(t3,(b,c),x,D)
                    assert max(t4)<=D
                    for y in (a,x):
                        t5=transition(t4,(a,x),y,D)
                        assert max(t5)>D,(a,b,c,x,y,t5)
                        first_fail[5]+=1;traces+=1
    assert traces==108  # 12 three-step failures and 96 five-step failures
    return traces,first_fail

if __name__=='__main__':
    print('three invariant',verify_three_agent_invariant())
    print('four greedy prefixes',verify_four_job_greedy())
    print('minimax',verify_game())
    print('adversary',verify_adversary())
