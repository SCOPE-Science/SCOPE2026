---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

In \(A=(\bigoplus_{n\ge1}M_n(\mathbb C))_{\ell_\infty}\), the element \(a=(J_n)\) has spectrum exactly \(\overline{\mathbb D}\): outside the disk the geometric resolvents are uniformly bounded, while for \(0<|\lambda|<1\) their norms grow at least as \(|\lambda|^{-n}\) and on \(|\lambda|=1\) at least as \(\sqrt n\). Von Neumann's inequality gives the polynomial-norm upper bound and finite-support comparison with the unilateral shift gives equality. Liu–Shen's published realization of arbitrary countable \(\ell_\infty\)-sums of finite-dimensional unital Banach algebras transports these identities to a Calkin algebra. The first \(r\) coordinates are killed by the \(r\)-th power, so each finite detector is nilpotent.

## originality

FAIL

The completed claim is a direct specialization/application of prior general coverage rather than a new nonstandard theorem. Liu–Shen already realize every countable \(\ell_\infty\)-sum of finite-dimensional unital Banach algebras as a Calkin algebra. Choosing the classical matrix algebras \(M_n\) and the standard nilpotent Jordan compressions \(J_n\), then applying the textbook coordinatewise invertibility criterion and unilateral-shift functional calculus, yields the submitted Calkin example without a new structural lemma. The absence of the exact words 'Jordan' or 'spectrum' from the realization paper does not defeat this implication-level coverage.

## value

PASS

As a counterexample/boundary illustration, the construction is mathematically well motivated: it shows sharply that jointly faithful norming finite detectors need not recover any fixed-stage spectral geometry. That conceptual boundary is useful even though the example is not original enough for acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
