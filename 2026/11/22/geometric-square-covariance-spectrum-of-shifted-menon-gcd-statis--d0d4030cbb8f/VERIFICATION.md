---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

Execute `python3 check_spectrum.py` using a standard Python 3 interpreter. The checker enumerates the units of each tested prime-power ring, independently computes \(X_a(u)=\gcd(a-u,p^k)\) and centers using \(k+1\), checks all covariance entries against the exact valuation-shell formula, and verifies a complete collection of orthogonal-level difference eigenvectors with integer arithmetic. It checks total multiplicity, trace and the exact total-variation identity using rational arithmetic.

Successful reference execution: `PASS 15 prime-power cases; 315 states, 315 orthogonal-basis vectors, 16861 pairwise covariance entries`. The tested parameter set comprises primes \(2,3,5,7\), positive exponents with \(\varphi(p^k)\le150\), and includes the single-state case \(p=2,k=1\). The largest cases have \((p,k)=(2,6),(7,2),(3,4),(5,3)\).

These calculations do not prove the universal statement. That proof rests on the explicit gcd expansion, the nested projection identity, the level-dimension formula and the elementary atom-mass comparison in RESULT.md. The provenance and mathematical generality of the cited prior results are discussed in that document; no external mathematical audit is asserted.
