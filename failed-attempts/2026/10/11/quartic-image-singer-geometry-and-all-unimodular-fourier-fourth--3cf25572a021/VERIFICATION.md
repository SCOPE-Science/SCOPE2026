---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Independent enumeration of all 91 unordered pairs (a,b) in F_13 gives 76 distinct two-sum fibers, 61 singleton and 15 double fibers; accounting for ordered pairs yields fourth-moment numerator 445. The fourth-power image {0,1,3,9} is a (13,4,1) difference set and all unordered sums are distinct, so f(t)=zeta_13^(A t)u_{t^4} saturates each fiber triangle bound. Independent SymPy Smith normal form of the 15x13 integer pair-relation matrix is diagonal (1 repeated eight times,13), rational rank9, showing exactly 13 connected components of dimension4. The normalization of the competing record uses p^-1 and reports 445/169, equivalent to numerator 445 for the originally defined normalized fourth-moment. This verifies the entire finite classification, not extrapolation.

## originality

FAIL

A DISTINCT published Resultary record, “Sidon quartic-power images and the complete phase-only fourth-moment equality groups”, was retrieved and its entire RESULT.md read. It proves for prime fields that p=5 and p=13 are exactly the Sidon fourth-power cases and at p=13 the identical phase-only fourth-moment maximum 445/169 (p^-1 Fourier convention) with every equality phase f(t)=zeta_13^(A t)u_{t^4} and 13 disjoint real four-tori. The submitted p=13-only theorem is a strict special case of this stronger existing statement; its different normalization does not confer originality. Finite-field paraboloid results by González-Riquelme–Oliveira e Silva are background, not the decisive covering source.

## value

FAIL

Despite correctness and genuine finite combinatorial structure, the whole p=13 conclusion, including equality-phase components and the exact extremal energy, is already established in the stronger p in {5,13} classification. No additional independently motivated mathematical fact or stronger bound remains to justify a separate contribution; alternate determinant certificates are not a new theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
