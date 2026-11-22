"""Reproducible exact-arithmetic checks for finite-switch extremal adoption."""
from fractions import Fraction as Q
from random import Random


def action(x, levels, cuts):
    for k, theta in enumerate(cuts):
        if x < theta:
            return levels[k]
    return levels[-1]


def trace_extreme(levels, cuts, alpha, weight, seed, target, start, max_steps=200):
    rest = [i for i in range(len(cuts)) if i not in seed]
    x = {i: Q(start) for i in rest}
    tr = []
    for t in range(max_steps+1):
        tr.append(tuple(action(x[i],levels,cuts[i]) for i in rest))
        if t == max_steps: break
        y = {}
        for i in rest:
            v = sum((weight[i][j]*target for j in seed),Q(0))
            v += sum((weight[i][j]*action(x[j],levels,cuts[j]) for j in rest),Q(0))
            y[i] = alpha[i]*x[i] +(1-alpha[i])*v
        x = y
    return rest,tr


def fast_extreme(levels, cuts, alpha, weight, seed, target, start, max_time=10000):
    rest = [i for i in range(len(cuts)) if i not in seed]
    x = {i: Q(start) for i in rest}
    t=0; changes=0; events=[(0,tuple(action(x[i],levels,cuts[i]) for i in rest))]
    while True:
        a = {i:action(x[i],levels,cuts[i]) for i in rest}
        v = {i:sum((weight[i][j]*target for j in seed),Q(0))+
              sum((weight[i][j]*a[j] for j in rest),Q(0)) for i in rest}
        next_times=[]
        for i in rest:
            k=levels.index(a[i]); threshold=None; strict=False
            if start == -1 and k < len(levels)-1:
                threshold=cuts[i][k]
                if v[i]<=threshold: continue
            elif start == 1 and k>0:
                threshold=cuts[i][k-1]
                strict=True
                if v[i]>=threshold:continue
            else:continue
            # Find first t with a threshold crossing (strict if descending).
            z=alpha[i]; j=1
            while t+j<=max_time:
                nx=v[i]+(x[i]-v[i])*z**j
                if (nx<threshold if strict else nx>=threshold): break
                j*=2
            if t+j>max_time:raise RuntimeError('Event wait > test limit')
            left=max(0,j//2);right=j
            while left+1<right:
                mid=(left+right)//2
                nx=v[i]+(x[i]-v[i])*z**mid
                if (nx<threshold if strict else nx>=threshold):right=mid
                else:left=mid
            next_times.append(right)
        if not next_times:return {'end_time':t,'profile':events[-1][1],'events':events,'changes':changes}
        dt=min(next_times)
        x={i:v[i]+(x[i]-v[i])*alpha[i]**dt for i in rest}
        t+=dt
        new=tuple(action(x[i],levels,cuts[i]) for i in rest)
        if new == events[-1][1]:raise AssertionError('no action change')
        changes+=sum(abs(levels.index(new[z])-levels.index(events[-1][1][z])) for z in range(len(rest)))
        events.append((t,new))
        assert changes<=len(rest)*(len(levels)-1)


def example():
    z=Q(0); one=Q(1)
    levels=(Q(-1),z,Q(9,10),one)
    cuts=((Q(-1,2),Q(1,4),Q(19,20)),)*2 + ((Q(-4,5),Q(3,10),Q(19,20)),(Q(-3,10),Q(4,5),Q(19,20)))
    w=((z,one,z,z),(one,z,z,z),(Q(2,5),z,z,Q(3,5)),(Q(2,5),z,Q(3,5),z))
    alpha=(Q(1,2),)*4
    low=fast_extreme(levels,cuts,alpha,w,(0,1),z,-1)
    high=fast_extreme(levels,cuts,alpha,w,(0,1),z,+1)
    assert low['events']==[(0,(Q(-1),Q(-1))),(1,(z,Q(-1))),(3,(z,z))], low
    assert high['events']==[(0,(one,one)),(1,(Q(9,10),Q(9,10))),(2,(Q(9,10),z)),(4,(z,z))],high
    assert low['changes']==2 and high['changes']==4
    assert low['end_time']==3 and high['end_time']==4
    assert Q(2,5) <= Q(7,10)  # Source scalar cascade fails for each outsider
    lo=trace_extreme(levels,cuts,alpha,w,(0,1),z,-1,20)[1]
    hi=trace_extreme(levels,cuts,alpha,w,(0,1),z,+1,20)[1]
    assert lo[2]==(z,Q(-1)) and lo[3]==(z,z)
    assert hi[3]==(Q(9,10),z) and hi[4]==(z,z)
    for t in range(21):
        for j in (0,1):
            assert levels.index(lo[t][j])<=levels.index(hi[t][j])
    print('four-action exact certificate: low 3, high 4, uniform takeover T=4; scalar cascade stays at seed')


def stress():
    rng=Random(271828)
    valid=0
    for trial in range(130):
        levelset = [Q(-1),Q(0),Q(9,10),Q(1)] if trial%2 else [Q(-1),Q(0),Q(1)]
        levels=tuple(levelset);n=4;alpha=[Q(rng.choice((1,2,3)),rng.choice((4,5))) for _ in range(n)]
        # ensure 0<alpha<1
        cuts=[]
        for i in range(n):
            row=[]
            for k in range(len(levels)-1):
                left,right=levels[k],levels[k+1]
                row.append(left + (right-left)*Q(rng.randint(1,9),10))
            cuts.append(tuple(row))
        w=[[Q(0) for j in range(n)] for i in range(n)]
        w[0][1]=w[1][0]=Q(1)
        for i in (2,3):
            p=Q(rng.randint(1,9),10)
            w[i][0]=p
            w[i][5-i]=1-p
        for side in (-1,1):
            fr=fast_extreme(levels,cuts,alpha,w,(0,1),Q(0),side,max_time=5000)
            rest,tr=trace_extreme(levels,cuts,alpha,w,(0,1),Q(0),side,200)
            for tm,pr in fr['events']:
                if tm<=200:assert tr[tm]==pr,(trial,side,tm,pr,tr[tm])
            for t in range(200):
                # reconstruct event-stage profile
                pr=fr['events'][0][1]
                for et,ep in fr['events']:
                    if et>t:break
                    pr=ep
                assert pr==tr[t],(trial,side,t,pr,tr[t])
            valid+=1
    print('exact event skips vs stepwise rational iteration:',valid,'trajectories × 200 times, PASS')
if __name__=='__main__':
    example();stress()
