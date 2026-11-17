"""Independent labelled-state verification of threshold-two CCA on triangle bouquets.
Run with Python 3.10+; no third-party dependencies.
"""
from itertools import product
from collections import Counter


def update(x, k):
    out = list(x)
    for v in range(2*k+1):
        if v == 0:
            near = range(1,2*k+1)
        else:
            w = v+1 if v % 2 else v-1
            near = (0,w)
        succ = (x[v]+1) % 3
        if sum(x[w] == succ for w in near) >= 2:
            out[v] = succ
    return tuple(out)


def predicted_rotation(x, k):
    h=x[0]
    pairs={ (a,b):0 for a in range(3) for b in range(a,3)}
    for j in range(k):
        a,b=(x[1+2*j]-h)%3,(x[2+2*j]-h)%3
        pairs[tuple(sorted((a,b)))]+=1
    A,B,C,D,E,F=(pairs[p] for p in ((0,0),(0,1),(0,2),(1,1),(1,2),(2,2)))
    return (B+2*D+E>=2 and E+2*F>=2 and A+C>=1 and B+D>=1)


def bad_count(k):
    if k==1: return 9
    return 3*6**k+2*k*6**(k-1)+2*k*4**(k-1)-(3+2*k)*3**k-2*k


def main():
    for k in range(1,6):
        period=Counter(); entries=Counter()
        for x in product(range(3),repeat=2*k+1):
            traj=[x]
            for _ in range(6):traj.append(update(traj[-1],k))
            assert traj[6]==traj[3], (k,x,traj)
            eventual=3 if traj[4]!=traj[3] else 1
            assert (eventual==3)==predicted_rotation(x,k),(k,x)
            t=min(i for i in range(4) if traj[i+eventual]==traj[i])
            period[eventual]+=1;entries[t]+=1
        expected=3*(9**k-bad_count(k))
        assert period[3]==expected,(k,period,expected)
        print(f'k={k}, labelled={3**(2*k+1)}, rotating={period[3]}, fixed_basin={period[1]}, entry_times={dict(sorted(entries.items()))}')
    print('PASS: exact labelled trajectories and closed basin law')

if __name__=='__main__':main()
