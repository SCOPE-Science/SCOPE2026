---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At I, one nontrivial cycle gives one neighbor, with binom(n,s)(n-s-1)! neighbors of fixed-set size s. After multiplication by n the normalization is asymptotic to e by the factorial tail, so each fixed-set size tends to Poisson(1). Conditional on both fixed sets and the first cycle, q eligible arrows satisfy n-|A|-2|B| <= q <= n. For each fixed j and bounded fixed-set sizes, j selected arrows cannot close a cycle; contracting the disjoint directed paths yields the falling-factorial moment (q)_j/(n-|B|-1)_j, uniformly tending to 1. All factorial moments determine the Poisson limit; uniformity follows by applying the same moment argument to any sequence of bounded-size conditioning configurations. Tight fixed-set sizes and the st/n bounded-size intersection estimate yield independence of all three limiting Poisson variables, not finite-size independence. The matrix norms and trace give the exact cosine, first-order expansion gives (2M-S-T)/4, and the derivative of arccos gives (S+T-2M)/(2 sqrt(3)). The variances 3/8 and 1/2 are variances of the limiting laws. Sampling with replacement is handled by the proof. The independent check is analytical; the finite package checker was read, not executed, and is not needed for the limit.

## originality

PASS

The classical adjacency and trace inputs are not novel. The joint independent Poisson law in the uniform incident-edge model and the resulting vertex-angle fluctuation law are distinct from the strongest inspected literature and distinct catalogued results. The exact catalogue match is the assigned finding itself, not an earlier distinct result.

## value

PASS

Uniform pairs of actual one-skeleton edges define a natural local metric statistic. The result identifies both a sharp angular scale and a non-Gaussian discrete limit, supported by a useful joint overlap law; this is more informative than the classical adjacency, a finite angle enumeration, or the concentration angle alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
