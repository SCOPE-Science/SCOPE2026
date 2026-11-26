---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Fix E in the unique maximal square-zero class. A commuting F has blocks (A,B;0,A), with A^2=0 and AB+BA=0. For r=rank A and h=m-2r, use the decomposition of the m-space into the image I of A, a complement of I in ker A, and a space J mapped isomorphically to I. Anticommutation leaves free blocks B_II,B_IH,B_IJ,B_HH,B_HJ, with B_JJ=-B_II and the other blocks zero, also in characteristic two. Solving Av=0 and Au=-Bv shows nullity F=m+nullity B_HH, so precisely q^((m-r)^2+r^2) Phi_h choices of B have maximal rank. The image/kernel flag and quotient isomorphism count for A is q^(2r(m-r)) Phi_m/(Phi_r Phi_h); the full class has size q^(2m^2) Phi_(2m)/Phi_m. These give the stated normalized law, including r=0 and h=0. For the asymptotics put a_r=Phi_infty/Phi_r. The tail product gives 0<=1-a_r=O_q(q^-r) and the prefactor after extracting Phi_infty differs from 1 by O_q(q^-m). Summing over r<=floor(m/2) gives the stated constant and remainder. Normalizing the summable deviations of a_r from 1 gives the stated total-variation bound and hence the rescaled limit. Frozen checker and output were inspected, not rerun; they cover nine small prime-field cases, not the all-field or limit claims.

## originality

FAIL

The October 13 Resultary record gives exactly the labeled-pair count for the same scope, all finite fields and each product rank. Switching to probability and simplifying Gaussian factors do not change the result. The extra fixed-field statement and its error follow from summing geometrically decaying defects in those same exact weights; the predecessor need not state the limit verbatim.

## value

FAIL

Product rank in this natural ensemble is a meaningful invariant, but the exact invariant is already known in labeled-count form. The new presentation and routine summable-weight limit do not establish an independently substantive remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
