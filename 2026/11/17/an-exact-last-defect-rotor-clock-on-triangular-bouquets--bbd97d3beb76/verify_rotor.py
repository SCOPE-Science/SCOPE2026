"""Reproduce exact first-recurrence counts for rotor walks on triangle bouquets.

Only Python standard library is needed. The chip starts at the common vertex, its
rotor initially points at b_{k-1}, and hub order is a_0,b_0,...,a_{k-1},b_{k-1}.
On each petal the local order is (hub,b_j) at a_j and (a_j,hub) at b_j.
"""
from collections import Counter
from itertools import product
from math import comb
import sys


def neighbors(k):
    out = [[] for _ in range(2*k+1)]
    out[0] = [v for j in range(k) for v in (2*j+1, 2*j+2)]
    for j in range(k):
        a,b = 2*j+1,2*j+2
        out[a] = [0,b]
        out[b] = [a,0]
    return out


def first_entry_by_cycle_detection(k, bits):
    nbr = neighbors(k)
    rot = [2*k-1] + list(bits)
    chip = 0
    seen = {}
    t = 0
    while (chip,tuple(rot)) not in seen:
        seen[(chip,tuple(rot))] = t
        rot[chip] = (rot[chip]+1)%len(nbr[chip])
        chip = nbr[chip][rot[chip]]
        t += 1
    return seen[(chip,tuple(rot))]


def is_unicycle(k, chip, rot, nbr):
    n = 2*k+1
    outgoing = [nbr[v][rot[v]] for v in range(n)]
    # All states must enter the unique cycle through the chip.
    cur = chip
    seen = set()
    while cur not in seen:
        seen.add(cur)
        cur = outgoing[cur]
    if cur != chip:
        return False
    # Every other vertex's rotor path reaches the chip's cycle.
    for v in range(n):
        p=v
        trail=set()
        while p not in seen and p not in trail:
            trail.add(p)
            p=outgoing[p]
        if p not in seen:
            return False
    return True


def first_entry_by_unicycle(k,bits):
    nbr = neighbors(k)
    rot = [2*k-1] + list(bits)
    chip = 0
    for t in range(1+12*k*(2*k+1)):
        if is_unicycle(k,chip,rot,nbr):
            return t
        rot[chip] = (rot[chip]+1)%len(nbr[chip])
        chip=nbr[chip][rot[chip]]
    raise AssertionError('unexpectedly failed to reach recurrence')


def predicted_time(k,bits):
    bad = [j for j in range(k) if bits[2*j]==1 and bits[2*j+1]==0]
    if not bad:
        return 0
    j = bad[-1]
    return 1 + 6*j-2*(len(bad)-1)


def coefficient_histogram(k):
    out=Counter({0:3**k})
    for j in range(k):
        for b in range(j+1):
            out[6*j-2*b+1]+=comb(j,b)*3**(k-b-1)
    return out


def audit(k_max=7):
    grand=0
    for k in range(1,k_max+1):
        hist=Counter()
        for bits in product((0,1), repeat=2*k):
            a=predicted_time(k,bits)
            b=first_entry_by_unicycle(k,bits)
            c=first_entry_by_cycle_detection(k,bits)
            assert a==b==c, (k,bits,a,b,c)
            hist[a]+=1
            grand+=1
        expected=coefficient_histogram(k)
        assert hist==expected, (k,hist,expected)
        assert sum(hist.values())==4**k
        mean_numer=sum(t*c for t,c in hist.items())
        # E tau = (11/2)*k - 21 + 21*(3/4)^k
        assert 2*mean_numer*4**k == (11*k-42)*4**(2*k)+42*3**k*4**k, (k,mean_numer)
        assert max(hist)==6*k-5
        assert hist[6*k-5]==3**(k-1)
        print('k=%d states=%d entry_max=%d maximizers=%d mean=%.9f histogram=%s'%(
            k,4**k,6*k-5,3**(k-1),mean_numer/4**k,sorted(hist.items())))
    print('PASS: %d labelled initial rotor states; independent return-state and rotor-cycle methods agree.'%grand)

if __name__=='__main__':
    audit(int(sys.argv[1]) if len(sys.argv)>1 else 7)
