---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

All singular points lie on the heavy-coordinate line. Its generic stabilizer has order \(\gcd(a,b)\), so a positive-dimensional singular stratum occurs exactly when that gcd exceeds one; if the gcd is one, only the two endpoints can be singular. Writing \(d=b-a\), the canonical and terminal regions are respectively \(0\le d\le r,1\le a\le r+d\) and their strict versions. Since \(\gcd(a,b)=\gcd(a,d)\), counting coprime lattice points in those triangles gives \(1+\Phi(r)+(2\Phi(r)-1)=3\Phi(r)\) and the terminal formula with \(r-1\). Subtraction gives \(3\varphi(r)\), and the two boundary descriptions follow by the same gcd reduction. The actual verifier blob was inspected and an independent finite regression through \(r=100\) reproduced both census formulas.

## originality

FAIL

At the audited snapshot, a published result for the exact same family already gives the complete canonical and terminal parameter triangles \(0\le d\le r,1\le a\le r+d\) and the strict terminal version. Standard weighted-projective quotient geometry identifies the generic stabilizer on the heavy-coordinate line as \(\mu_{\gcd(a,b)}\), so zero-dimensional singular locus is exactly \(\gcd(a,b)=1\). The assigned formulas then reduce to the elementary count of coprime lattice points in the already-known triangle, using symmetry and the definition of the summatory totient. Under the required implication-level standard, this is a routine arithmetic corollary of stronger published structural data rather than an independent original theorem.

## value

PASS

Counting precisely which canonical and terminal members have isolated singularities is a natural geometric census, and the totient formulas give a useful asymptotic density. The record is rejected only because that census is too direct a consequence of an existing exact parameter classification plus the standard stabilizer criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
