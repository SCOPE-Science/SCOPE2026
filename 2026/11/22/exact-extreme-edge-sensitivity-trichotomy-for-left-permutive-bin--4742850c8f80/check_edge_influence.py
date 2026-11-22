"""Standalone exhaustive check for the extreme light-cone influence trichotomy.

The proof, not these finite comparisons, establishes all-time claims.
Run: python check_edge_influence.py
"""

def local_rule(h, a, b, c):
    return a ^ ((h >> (2*b + c)) & 1)


def rule_number(h):
    return sum(local_rule(h,a,b,c) << (4*a+2*b+c)
               for a in (0,1) for b in (0,1) for c in (0,1))


def output(h, initial, t):
    values = initial[:]
    for _ in range(t):
        values = [local_rule(h, values[j], values[j+1], values[j+2])
                  for j in range(len(values)-2)]
    return values[0]


def observed_count(h,t):
    # Among the 2^(2t) possible values of all *other* initial coordinates,
    # count assignments for which changing the rightmost input changes output.
    count = 0
    for mask in range(1 << (2*t)):
        initial = [(mask >> j) & 1 for j in range(2*t)]
        count += output(h,initial+[0],t) != output(h,initial+[1],t)
    return count


def expected_count(h,t):
    d0=((h>>0)&1)^((h>>1)&1)
    d1=((h>>2)&1)^((h>>3)&1)
    if d0==d1==0:return 0
    if d0==d1==1:return 1<<(2*t)
    return 1<<t


def boundary_word(h, initial, t):
    # At each stage the cell immediately LEFT of the (unperturbed)
    # rightmost causal boundary is the penultimate shrinking-array cell.
    values = initial[:]
    bits = []
    for s in range(t):
        bits.append(values[-2])
        values = [local_rule(h, values[j], values[j+1], values[j+2])
                  for j in range(len(values)-2)]
    return sum(v << s for s,v in enumerate(bits))


def verify_boundary_factorization(h, t):
    d0=((h>>0)&1)^((h>>1)&1)
    d1=((h>>2)&1)^((h>>3)&1)
    counts=[0]*(1<<t)
    for mask in range(1<<(2*t+1)):
        x=[(mask>>j)&1 for j in range(2*t+1)]
        z=boundary_word(h,x,t)
        counts[z]+=1
        predicted=all((d1 if ((z>>s)&1) else d0) for s in range(t))
        y=output(h,x,t)
        x2=x[:]
        x2[-1]^=1
        actual=(y!=output(h,x2,t))
        assert bool(predicted)==actual,(h,t,mask,predicted,actual)
    assert counts==[1<<(t+1)]*(1<<t), (h,t,counts)


def main():
    counts = {}
    tested=0
    for h in range(16):
        rn=rule_number(h)
        d0=((h>>0)&1)^((h>>1)&1)
        d1=((h>>2)&1)^((h>>3)&1)
        case=('zero' if (d0,d1)==(0,0) else
              'one' if (d0,d1)==(1,1) else 'exponential')
        counts[case]=counts.get(case,0)+1
        for t in range(1,7):
            if t<=5:
                verify_boundary_factorization(h,t)
            got=observed_count(h,t)
            want=expected_count(h,t)
            assert got==want, (h,rn,t,got,want)
            tested+=1
    assert counts=={'zero':4,'one':4,'exponential':8}, counts
    assert rule_number(0b1110)==30, rule_number(0b1110)
    print('PASS:', tested, 'complete small-time ECA comparisons, 16 rules, t=1..6')
    print('PASS: 80 complete boundary-independence and path-factorization comparisons, t=1..5')
    print('Rule-class census:', counts)
    print('Rule 30: rightmost influence = 2^(-t), leftmost = 1')

if __name__=='__main__':main()
