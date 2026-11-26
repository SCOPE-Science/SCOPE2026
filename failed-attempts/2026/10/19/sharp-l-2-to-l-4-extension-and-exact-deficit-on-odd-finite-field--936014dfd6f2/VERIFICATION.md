---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a nonzero pair-sum (x,y), both coordinates are nonzero, and the representing parameters are the roots of Z²−xZ+x/y; the only exceptional fiber is (0,0), exactly the ordered antipodal pairs. Character orthogonality gives q²Q/n⁴ for the output fourth power, while the input fourth power is M²/n². Counting diagonal and distinct pairs with their ordered multiplicities gives Q=2M²−Σ(A_t²+|B_t|²/2)+|B|². Expanding the centered sums using ΣA_t=M and ΣB_t=B gives the stated identity with k=n/2, including k=1. The last term is nonnegative by |B|≤Σ2|f(t)f(−t)|≤M. If the deficit is zero for nonzero f, the equal A_t and |B|=M force each pair to have equal moduli and all coefficients to have the same positive modulus; equal B_t gives the common product. The converse and attainment by a constant function follow directly. The proof works for every odd prime power; the frozen checker was inspected but not run and only supplies finite diagnostics.

## originality

FAIL

A distinct earlier Resultary record explicitly states the identical sharp constant and equality class on the same domain with the same normalization, and proves the identical weighted fourth-moment identity. The three-term deficit is not displayed there but is a direct algebraic regrouping of that identity: there is no additional mathematical inequality or stability theorem in the frozen remainder.

## value

FAIL

The exact rate and extremizer classification for this natural curve would have mathematical value if not already available. The only new display splits the known deficit by the elementary variance identity; the frozen finding does not go further to a stability estimate in distance to the extremizer family or another independently useful result. Repackaging alone is not a valuable surviving claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
