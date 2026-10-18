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

For real n-point increasing cone and 1<p<∞, uniqueness/coercivity hold. Fitted maximal constant blocks satisfy scalar ∑sgn(a_i−m)|a_i−m|^(p−1)=0, are monotone and translation equivariant; their direct-sum maps have Lipschitz <=|B|^(1/p) for p<2. When p>2, balancing residual powers and t↦t^((p−2)/(p−1)) subadditivity force normalized derivative weights <=1/2; Hölder gives repeated-block constant <= (|B|/2)^(1/p). The finite-selection/segment lemma pastes block regimes. At strictly complementary full-pooling data, a residual-zero coordinate below p=2 gives mean shift h+o(h), while ±1 extreme residuals above p=2 give derivative weights 1/2,1/2; these attain sharp supremal constants locally. Hilbert projection and n<=2 have norm 1. Sources RESULT.md/verify_isotonic.py actually read; numerical tests are not universal proof.

## originality

FAIL

FAIL for originality. The complete published Resultary RESULT.md for every finite partial order, not just chains, states the IDENTICAL sharp real unweighted ℓp projection Lipschitz constants as a function of maximal weak component size N: 1 at p=2 or N<=2, N^(1/p) at 1<p<2, and (N/2)^(1/p) at p>2, and proves both bounds. The assigned chain cone is the path/DAG special case with N=n. This is direct stronger prior statement-to-claim implication, not similarity of a title, parameter, or algorithm. The separately read diagonal-line projection result proves the shared scalar-block component and is explicitly distinguished from a full-chain proof. No independent unclaimed chain invariant survives.

## value

FAIL

Though an exact sharp stability invariant of isotonic regression would ordinarily be mathematically useful, the all-partial-orders theorem already supplies this precise chain constant and its sharpness throughout the domain. The additional presentation is a known special-case computation, not a distinct structural insight or unknown exact fact; no viable uncaptured valuable remainder was found.

The dated certificate retains the supplied scientific assessment, sources and limitations.
