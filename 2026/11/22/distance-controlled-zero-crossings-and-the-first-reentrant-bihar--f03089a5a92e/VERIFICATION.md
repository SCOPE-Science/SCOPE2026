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

For the unnormalized cube, the Walsh eigenvalues of L are 2k. At distance r the entry times 2^d has coefficient c_{d,r,k} on x^(k^2), x=exp(-4t). Double counting gives c_{d,r,k}=binom(d,k)K_r(k)/binom(d,r), with K_r of degree r and leading term (-2)^r y^r/r!. Each reversal in the nonzero samples of K_r forces a real root between successive sampled indices, so Descartes bounds all positive x roots with multiplicity by r. At t=0 Laplacian powers of degree below r cannot connect the two vertices. For even r=2q the (2q)! shortest walks give leading coefficient (-1)^q (2q)!/q!; for odd r=2q+1 the r+1 adjacency term is excluded by parity, leaving leading coefficient (-1)^q 2d(2q+1)!/q!. Thus x=1 accounts for exactly ceil(r/2) roots. The constant coefficient gives a positive limit as t tends to infinity, yielding the claimed positivity at distance one and exactly one simple crossing at distances two and three. On Q4, independent exact arithmetic confirms the two P4 brackets (0.25,0.26), (0.93,0.94) and the P2 and P3 brackets (0.85,0.86), (0.50,0.51). The bound establishes uniqueness and simplicity in each bracket; reversing their order under x=exp(-4t) gives the stated times and the first dimension with two crossings. Before the first antipodal crossing distance two is negative; between antipodal crossings the antipodal class is negative. After the final crossing all classes are positive, with only the antipodal zero at that endpoint. Each row sums to one and the absolute row sum adds twice the negative mass; shell sizes 6, 4, 1 divided by 16 give the displayed norm, and symmetry gives the same column norm.

## originality

PASS

The distinct supported additions are the all-dimension distance-only count for the squared Laplacian and the first double crossing with exact Q4 classification. Walsh/Krawtchouk identities, Descartes, negative-mass norms and general eventual positivity are not novelty claims. Fixed-size, exponent-dependent and different-graph comparators have substantial method or special-case overlap but do not supply the supported claim.

## value

PASS

Counting entry zeros with multiplicity governs how often a signed diffusion entry can reverse sign, and the bound depends only on distance, not the number of spectral levels. The first double crossing is a sharp natural witness rather than a sampled fluctuation: all lower dimensions are proved incapable of it and the exact Q4 thresholds settle entrywise recovery and both endpoint norms. It distinguishes reentry of individual entries from eventual positivity of the full operator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
