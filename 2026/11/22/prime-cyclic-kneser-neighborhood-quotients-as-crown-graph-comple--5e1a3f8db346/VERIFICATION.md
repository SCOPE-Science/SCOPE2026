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

# Verification and limits

The prime-uniform proof is purely mathematical and does not depend on finite enumeration. It checks the exact combinatorial face criterion, the equivariant poset equivalence, the barycentric lens-complement retraction, the two-vertex crown voltage graph, free translation, the degree bounds, the group-(co)homology spectral sequences and the top Euler-rank calculation. The exact date-qualified literature comparison is in `REVIEW.md` and `AUDIT.json`.

Execute `python3 verify_kneser.py` with the standard Python library. This constructs ranks and signed boundary incidence matrices of the cyclic rank-selected Boolean quotients. For prime five the quotient graph has cell counts (4,6) and 3 cycles. For prime seven the cell counts are (16,140,300,180), Euler characteristic -4; ranks over F_2 are (15,125,175) and over F_7 (15,124,175). Corresponding homology dimensions are (1,0,0,5) and (1,1,1,5). Each quotient boundary composition was checked to be zero. These finite computations are evidence for the low-dimensional sample only and do not replace the general proof or certify absence of unexpected integral torsion at all primes.

Only odd primes at least seven are covered. The geometric relation is a homotopy equivalence, not a homeomorphism between the finite orbit quotient and the open lens complement. The exact first-public source date is taken from the earliest explicitly dated archival reference consulted (2002-08-09) rather than inferred from the 1978 journal year. No independent external audit has been performed.
