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

The exact incidence matrix uses the fifteen two-subsets and twenty three-subsets of a fixed six-element set; entry \(B_{a,t}\) is one exactly when \(a\subset t\). The provided independent verifiers build the matrix anew, rather than loading a certificate or other run's output.

- `verify_integral.py` needs Python 3 with standard library only. It checks all 225 entries of the Gram identity, exact degrees, zero Laplacian row sums, two independent reduced-Laplacian determinants by fraction-free elimination, and the complete prime-local Smith valuations over prime powers of \(2\), \(3\), and \(5\). Both vertex deletion choices give the same data; all 34 pivots have valuations at most two, within the modulus \(p^9\).
- `verify_sympy.py` needs SymPy. It independently checks the exact 15-by-15 Gram characteristic polynomial, the 35-by-35 Laplacian characteristic polynomial and the full integer Smith forms after deleting vertices of opposite types.

The verified group has 24 unit Smith entries and ten nontrivial invariant factors: \(2,2,10,10,30,30,180,180,180,180\). Its order agrees with the spanning-tree count. These finite exact calculations prove this specified 35-vertex case, not a general family theorem, and do not establish historical uniqueness or independent validation.
