"""S3: gluing admissibility + Rosales identities check (stdlib only)."""
import sys
sys.path.insert(0, "output/artifacts")
from math import gcd
from sglue import semigroup_stats, in_sg_sieve


def member_of(gens_small, c, x):
    """x in <gens_small + [c..]> ? exact for the 'truncated' semigroups we use."""
    if x < 0:
        return False
    if x >= c:
        # need care: our semigroups are <base>_c i.e. all >= c included
        return True
    # sieve to x
    is_sg = in_sg_sieve(gens_small, x)
    # must also consider that semigroup contains [c..]; but x<c so only base gens matter... plus combinations landing < c
    return bool(is_sg[x])


def rosales_predict(sA, sB, k1, k2):
    cC = k1 * sA["c"] + k2 * sB["c"] + (k1 - 1) * (k2 - 1)
    gC = k1 * sA["g"] + k2 * sB["g"] + (k1 - 1) * (k2 - 1) // 2
    dC = k1 * sA["delta"] + k2 * sB["delta"] + (k1 - 1) * (k2 - 1) // 2
    mC = min(k1 * sA["m"], k2 * sB["m"])
    eC = sA["e"] + sB["e"]
    return dict(c=cC, g=gC, delta=dC, m=mC, e=eC)


def e_glue_formula(sA, sB, k1, k2):
    """Closed E-gluing formula from base data only (no enumeration of C).
    esC = #{a in GA : k1*a < cC} + #{b in GB : k2*b < cC}
    jC  = #{a in GA : cC<=k1*a<=cC+mC-1} + #{b : cC<=k2*b<=cC+mC-1}
    dqC = mC - jC ; qC=ceil(cC/mC); nuC=qC*mC-cC
    E(C)= esC*deltaC - qC*dqC + nuC  (deltaC,qC... via Rosales/locked def)."""
    P = rosales_predict(sA, sB, k1, k2)
    cC, mC = P["c"], P["m"]
    esC = sum(1 for a in sA["gens"] if k1 * a < cC) + sum(1 for b in sB["gens"] if k2 * b < cC)
    jC = sum(1 for a in sA["gens"] if cC <= k1 * a <= cC + mC - 1) + \
        sum(1 for b in sB["gens"] if cC <= k2 * b <= cC + mC - 1)
    dqC = mC - jC
    qC = -(-cC // mC)
    nuC = qC * mC - cC
    E = esC * P["delta"] - qC * dqC + nuC
    return dict(E=E, esC=esC, jC=jC, dqC=dqC, qC=qC, nuC=nuC, **P)
