#!/usr/bin/env python3
"""Exact modular half-domain root census using logarithmic derivatives."""
from math import isqrt
import csv
import sys

def primes_through(n):
    return [p for p in range(3, n + 1, 2) if all(p % d for d in range(3,isqrt(p)+1,2))]

def root_data(p, a, inverses):
    # Only need 1<=a<= (p-1)//2; 2a<p.
    aa = (a*a) % p
    prod = 1
    log_derivative = 0
    val = 1
    drv = 0
    for k in range(1,a):
        factor = (aa - k*k) % p
        assert factor
        prod = prod*factor % p
        log_derivative = (log_derivative + 2*a*inverses[factor]) % p
        val = (val+prod) % p
        drv = (drv + prod*log_derivative) % p
    # Values for all subsequent k vanish; derivatives are nonzero possibly
    # until the second congruent zero k=p-a.
    derivterm = (2*a*prod) % p
    for k in range(a,p-a):
        if k>a:
            derivterm = (derivterm * ((aa-k*k) % p)) % p
        drv = (drv + derivterm) % p
    return val,drv

def run():
    total_odd = total_roots = low_roots = total_multiple = 0
    table = []
    for p in primes_through(971):
        inv = [0]*p
        inv[1]=1
        for j in range(2,p):
            inv[j] = (- (p//j)*inv[p%j])%p
        roots = []
        repeated = []
        for a in range(1,(p+1)//2):
            val, drv = root_data(p,a,inv)
            if val == 0:
                roots += [a,p-a]
                if drv==0:
                    repeated += [a,p-a]
        table.append((p, len(roots), ";".join(map(str, sorted(roots)))))
        total_odd += 1
        total_roots += len(roots)
        total_multiple += len(repeated)
        if p < 971:
            low_roots += len(roots)
            assert not repeated,(p,repeated)
        else:
            assert sorted(roots)==[194,777]
            assert sorted(repeated)==[194,777]
            print('AT_971_ROOTS',sorted(roots),'MULTIPLE',sorted(repeated))
    assert(total_odd,total_roots,low_roots,total_multiple)==(163,144,142,2)
    print('PRIMES',total_odd,'ALL_ROOTS',total_roots,'SMALLER_ROOTS',low_roots,'MULTIPLE',total_multiple)
    print('INDEPENDENT_LOG_DERIVATIVE_CHECK_OK')
    if len(sys.argv) > 1 and sys.argv[1] == '--table':
        with open(sys.argv[2], 'w', encoding='utf-8', newline='') as out:
            writer = csv.writer(out, lineterminator='\n')
            writer.writerow(('prime','root_count','root_half_indices'))
            writer.writerows(table)

if __name__=='__main__':run()
