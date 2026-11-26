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

The two sides of the braid identity have coordinates (f²(z),gf(y),g²(x)) and (f²(z),fg(y),g²(x)); commuting with the solution is equivalent to commuting with f and g separately. The latter centralizer A contains f and g, so H=<f,g> is itself elementary abelian of dimension at most two if A=(C_p)^r. A map between transitive H-sets is an equivariant bijection exactly when their stabilizers agree, and each possible representative image then determines the map. Thus each orbit type K with multiplicity m_K contributes (H/K) wr S_(m_K). For nonfixed types a transposition of copies fails to commute with a translation on just one copy, so no type repeats. Fixed points may occur singly or, for p=2, in one pair contributing rank one. At rank two H there are p+1 distinct line stabilizers and one trivial stabilizer, contributing ranks one and two at costs p and p². H of smaller dimension adds no candidate above rank one for odd p or rank two for p=2. The faithful-action lower bound pr follows since the intersection of A-orbit stabilizers is zero and p^d>=pd. For odd p, exceeding p+1 forces the free orbit and leaves precisely r-2 line types, giving the stronger bound. Counting the types yields both impossibility cutoffs; distinct projective-form translations, the optional free block and the fixed pair attain all permitted ranks, including the cyclic single-form case. Independent bounded checks enumerated 54 block profiles at p=2,3,5,7 and calculated centralizer orders by extending possible representative images along orbits; these are corroboration, not the all-rank proof. Replay: `python3 /workspace/branches/review_checks.py 5`.

## originality

PASS

The recognized classical ingredients are the commuting-permutation ansatz, equivariant centralizer decomposition and unrestricted faithful degree pr. The distinct claim is the sharp realization minimum and impossibility cutoff for full elementary-abelian automorphism groups in precisely this two-generator permutation family. Neither general centralizer/Yang–Baxter realizability nor the inspected involutive classification gives these cutoffs or minima. No independent equivalent was established in the bounded comparison.

## value

PASS

This is a natural minimum realization problem suggested by work on full Yang–Baxter automorphism groups. It identifies a genuine obstruction not seen in faithful permutation degree: after the supply of line stabilizers is exhausted, odd primes require one costly free orbit and then no further rank is possible. At two, the free block has no excess cost and the fixed-pair exception extends the rank cutoff. The exact feasible ranges and optimal constructions are usable together.

The dated certificate retains the supplied scientific assessment, sources and limitations.
