---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For any 3-node mask, repeated time coordinate yields a 2x2 Gram principal minor with minimum 3b²/s and repeated modulation yields (a-b)²/s; both fall strictly below (a²-2ab+4b²)/s for 0<b<a. Thus all optimizers are the six bijective time-frequency permutation graphs. Direct Gram characteristic factorization on a representative gives eigenvalues lower=(a²-2ab+4b²)/s and upper=(a²+ab+b²)/s twice; modulation shifts and conjugation cover all six. Optimize r=b/a to get (3-sqrt3)/2, attained by Poisson self-Fourier periodized Gaussian at λ=3. Independently enumerated all 84 masks for three positive symmetric windows, finding exactly six optimizers and the predicted least eigenvalue. All-parameter proof is interlacing, explicit characteristic identity and calculus, not numerical enumeration.

## originality

PASS

Earlier finite Gaussian full-spark/basis theorem proves all N=3 triples are bases but does not optimize smallest singular value or identify six universal best masks, nor give a sharp over-Gaussian-width constant. Full-spark is existence, not the posed minimax geometry.

## value

PASS

The sharp lower-eigenvalue design and exact optimum count address a natural minimal three-sample stability question on a complete nine-atom finite Gabor orbit, with a width-independent Gaussian optimum and sharp worst-width constant. These are actionable finite-frame stability quantities, not merely a restatement of full spark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
