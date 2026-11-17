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

# Verification of the stated theorem

The proof is a symbolic functional-analytic argument. The following proof-critical statements were checked against the definitions (and are proved in RESULT.md): (i) surjectivity of \(S\) gives exponentially controlled preimages, hence \(K(T)=E\oplus\{0\}\); (ii) a quasinilpotent restriction has zero analytic core, forcing the semi-regular summand to contain \(E\oplus\{0\}\); (iii) any additional vector with nonzero lower coordinate would create a kernel vector outside the upper-coordinate range, violating semi-regularity; (iv) a complementary closed invariant subspace is a bounded graph and invariance is equivalent to \(SV=-J\); (v) the quotient-based shift satisfies \(S\) onto and \(SJ=0\); (vi) the equation \(SV=-J\) would split the quotient; (vii) direct powers equal \(S^n\oplus0\) for \(n\ge2\).

The existence of an uncomplemented subspace of complex \(\ell^p\), \(1<p<\infty\), \(p\ne2\), follows from the established Lindenstrauss–Tzafriri theorem and non-Hilbertianity of \(\ell^p\). Uniform convexity of quotients and \(\ell^2\)-sums are standard Banach-space facts. No computer enumeration, experimental certificate, or independent validation is asserted.

Scope limits: the exact equivalence concerns a surjective upper-left corner and zero lower row; the counterexample is existential and its choice of uncomplemented subspace is not given by a coefficient list. Publication priority remains subject to older related literature, especially arXiv:2610.23229. The independent audit has not been performed.
