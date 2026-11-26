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

Neutral antisymmetric modes split off as a zero direct summand; in the bright block the independently computed quartic is (x²-k)(x²+gamma²-t²)-2x(x+t). A multiple nonreal root would make it a squared real quadratic, contradicting the absent cubic and nonzero linear coefficients. A multiple root at zero is excluded by P'(0)=-2t, and elimination at a positive root would force t<0. Negative repeated roots -u give the stated T_k,G_k. T_k' has just the two stated critical points, with 0<y_k<k and strict decrease between them, so the coupling interval is nonempty and contains exactly three crossings. Their gains are distinct since two negative double roots contradict the zero cubic coefficient; gamma>0, u²!=k and t!=4u³ give transverse double roots. To justify alternation, including the step not explicit in the frozen proof, P(sqrt(k))=-2k-2t sqrt(k)<0 and both tails are positive: there are always at least two real roots, so the phases must alternate 4,2,4,2 starting at the simple Hermitian spectrum. At gamma=t the simple bright zero can coincide only semisimply with dark modes (direct sum). At t=4y_k^(3/2) the quartic factors as (x+sqrt(y_k))³(x-3sqrt(y_k)); G_k(sqrt(y_k))>0, and the indicated rank-three minor is nonzero there and at every positive-gain collision. Each such multiple root therefore has one Jordan block of the claimed size.

## originality

PASS

Reentrant PT symmetry, three gain thresholds on other graphs, and EP3 constructions are known. The distinct supported claim is the exact all-size fixed-link gain sweep and nonzero-energy EP3 for a balanced triangle with identical neutral pendant leaves at its hub.

## value

PASS

A single closing link changes the spectral behavior of a previously unlinked balanced star. The exact open interval guarantees a second real window despite prior symmetry breaking, and the nonzero-energy Jordan block gives a sharply tunable and analytically checkable higher-order degeneracy. The bright reduction exhibits how spectator modes can affect the active spectrum without changing the dark zero eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
