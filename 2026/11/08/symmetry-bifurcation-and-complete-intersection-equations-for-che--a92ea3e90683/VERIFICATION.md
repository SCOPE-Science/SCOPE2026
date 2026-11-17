---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

C PASS. For integers u≥3 and even n≥4, the recurrence has strong divisibility gcd(U_i,U_j)=U_gcd(i,j), a primitive minimal triple, gcd(a,b)=u, and identity (u²−1)b=a+u c. At n=4 and 6|n the Apéry normal-form reductions provide distinct residues and a rectangular Apéry set, yielding two binomial toric relations, symmetric Frobenius formulas and Hilbert series. For other even n≥8 (3∤n), the only possible gcd gluing is (a,b) and forces c=x(a/u)+y(b/u); gcd(A,B)=1 then A|d−y with 1≤d−y≤d<A, impossible. The Herzog three-generator criterion applies; finite Apéry checks are supplementary, not proof.

## originality

PASS

O PASS (best of knowledge). Inspected primary and published theorem statements and compared their precise objects, parameter domains and implications; none of the checked wider source theorems directly implies this full final claim. Source-level checks and narrower known deductions are credited; residual priority risk preserved.

## value

PASS

V PASS. All-index symmetry phase classification and explicit complete-intersection presentations for a natural Lucas/Chebyshev recurrence family answer a genuine semigroup-structural question; isolated n=4 and divisibility-by-six branches are not textbook substitutions or finite slices. The exact Apéry rectangles determine Hilbert and Frobenius invariants useful for semigroup algebra computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
