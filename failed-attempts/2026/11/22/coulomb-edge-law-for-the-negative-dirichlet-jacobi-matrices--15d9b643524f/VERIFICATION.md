---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

RESULT.md lines 23–60: the hoppings converge to 1, giving a compact perturbation of the free half-line operator with essential spectrum [−2,2]. Outside that interval the recurrence starting at site zero gives simplicity, and alternating signs give exact reflection. Deleting interblock bonds costs at most two per cut for strict threshold counts. The exact constant-hopping cosine count with rounding error at most one and a 2Δ norm bound apply on each block. Below ε^(−1/3) a dimension bound suffices; the dyadic blocks up to η/ε have O_s(√m+1) counts apiece by comparison to the free block at threshold 2−C_s/m. The terminal tail beyond (s+η)/ε has norm below 2+ε. On the remaining scaled compact interval the uniform expansion 2a_n=2+sε/x+O_{s,η}(εδ+ε²) and the two shifted thresholds give upper and lower Riemann sums, with continuous positive-part square root even at the turning point. The omitted small-x integral is O_s(√η); substituting x=s sin²u gives the normalized integral s/2. Strict monotone count inversion gives the coefficient s²/4 in the j-law; a jump at an equality threshold changes the count by only one because of simplicity. The frozen checker was read, not run; its finite truncations test consistency, not the limit. No claim about the top eigenvalue or parameter uniformity is proved or needed.

## originality

FAIL

Verified stronger coverage, not a literature-access failure: distinct Resultary record b8745f13efaa proves the general discrete Coulomb comparison formula in proof §4 and the matching kinetic/potential squeeze in §5. The exact frozen count follows by direct substitution of free kinetic coefficient 1 and tail strength s, for every fixed s>0. The hypotheses of the general comparison, unlike those of that record's particular Bergman-Toeplitz application, do not restrict s. A classical explicit Pollaczek comparator independently gives the same squeeze. No priority or order is inferred from the shared date of the two records.

## value

FAIL

The operator and edge invariant are natural, and the frozen proof is a usable elementary exposition. But as an asserted exact new result, the coefficient is a direct evaluation of an already available general Coulomb formula at κ=1,g=s. The inverse eigenvalue and symmetry statements are routine consequences, and neither the motivating top-eigenvalue problem nor a refined error or uniform law is addressed. The specialization alone supplies no independent mathematical gain warranting acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
