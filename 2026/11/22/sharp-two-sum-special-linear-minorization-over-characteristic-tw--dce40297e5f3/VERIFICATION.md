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

In characteristic two V=A+U, and det(I+U⁻¹A)=1+tr(U⁻¹A)+det A, giving the trace constraint with the stated sign. Over the residue field a rank-one target reduces by determinant-one changes to diag(1,0); the condition W₁₁=0 leaves q choices of W₂₂ and q−1 choices of the first off-diagonal entry, the second then fixed. For a primitive invertible target C=WA has fixed determinant and nonzero trace δ; its separable polynomial x²+δx+δ splits precisely when the absolute trace of δ⁻¹ is zero, by the Artin–Schreier equation. The split and irreducible conjugacy classes have centralizers of orders (q−1)² and q²−1, giving q(q+1) and q(q−1) solutions. At every non-scalar WA the restricted trace differential is nonzero: the trace pairing on M₂ is nondegenerate and the orthogonal complement to trace-zero matrices is the scalar line, including in characteristic two. Successive square-zero layers each give q² joint lifts, or q³ lifts of the determinant-one constraint alone. For A=π^sB the annihilator of π^s is (π^(k−s)), so the shorter-ring equation and the q^(3s) preimage factor are exact. Rank-one B gives the stated exact count. For invertible leading B the residue trace-zero matrices have diagonal entries equal to some a with a²=det B+bc; every (b,c) gives exactly one a, only b=c=0 being scalar. Counting only the q²−1 smooth residue points gives a bound larger than the minimum by a factor (q+1)q^(s−1). Zero is also strict. Rank-one targets and the nonsplit invertible targets yield exactly the stated equality locus; the latter use q/2 nonzero determinants, since absolute trace one excludes zero and inversion permutes nonzero values. Normalizing by |SL₂(R)|² and q^(4k) verifies the length-independent minorization. The proof also covers k=1 and q=2, where the split invertible stratum is empty.

## originality

PASS

The finite-field fiber problem is prior, and the same style of sharp depth-independent minorization is known in the odd-residue-characteristic analogue. Credit is restricted to the nonreduced characteristic-two chain-ring minimum and equality locus, including their exact lift density, not the field case or the appearance of the same functional constant in a different regime. The closest distinct indexed result is over odd prime-power rings, which does not cover any of the stated nonreduced rings.

## value

PASS

The least fiber is the sharp uniform additive mixing guarantee for two determinant-one summands. Its normalized constant persisting at arbitrary nilpotence length, with all equality targets determined by reduction, is a useful quantitative refinement of mere additive coverage. The minimum and complete equality classification require controlling both primitive and divisible targets rather than just recounting over the residue field.

The dated certificate retains the supplied scientific assessment, sources and limitations.
