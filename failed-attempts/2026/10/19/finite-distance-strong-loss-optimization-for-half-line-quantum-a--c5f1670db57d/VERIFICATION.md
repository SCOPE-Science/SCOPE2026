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

The exact half-line normalization and all claims check analytically. After dropping the scalar energy and rescaling time by Ω/2, the boundary resolvent entry is −w^s/(1−iηw), where z=−w−w⁻¹ and |w|<1 for Im z>0; this follows from the free decaying solution and the first-row boundary equation. Laplace–Plancherel gives η/π times its real-energy squared integral. The boundary limit is justified by |1−iηw|≥1 and a uniform integrable squared tail from |w|≤1/(|z|−1). On the band put w=e^{ik}; off the band put w=±q on the two tails. The energy Jacobians give exactly F+G_s in RESULT.md. Reciprocal subtraction gives the positive claimed integrand; successive distances multiply it by q². Differentiation gives P_s′(1)>0 and strict increase on (0,1]; at both ends P_s tends to zero for s≥2, so maxima exist strictly above 1. The η-uniform bound G_s≤1/[2πs(s−1)] and strict isolated maximum of F localize all maxima. F″(1)=−2/(3π) and compact-local G_s″=O(s⁻²) give eventual strict concavity. The beta moment at η=1 gives P_s′(1)=1/(2πs³)+O(s⁻⁴); the stationary equation and quadratic expansion give respectively 3/(4s³) and 3/(16πs⁶) with the claimed errors. At s=1 the substitution t=ηq instead gives the exceptional strong-loss limit 1. The supporting script was inspected, not run; its finite-chain comparison is not an exact tail certificate, and no such certificate is needed for the analytical proof. No uniqueness for small s is inferred.

## originality

FAIL

A distinct indexed record gives the same optimizer existence, strict strong-loss location, eventual uniqueness, and leading coefficient, for the identical model and normalization. Its proof also makes the gain coefficient an immediate Taylor consequence. The reciprocal identity and strict distance law are not asserted there but are direct subtraction and positive-weight comparison of the earlier published Eq. (15); they do not supply a substantive standalone remainder. This is a present coverage assessment, not an assertion that the November-labelled record predates this October-labelled record or that there was any dependence.

## value

PASS

As a mathematical question, determining whether a distant-source matching prescription remains globally optimal at every finite distance is structurally motivated; an exact strong-loss direction and uniform localization give more than a small numerical improvement. The independent uncovered remainder, considered alone, would not justify repair: the gain and reciprocal defect are short consequences of the checked coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
