---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The unique block form F(v,z)=(Av,Bv+(wedge² A)z), with A²=A and BA+(wedge² A)B=B, is correct for any finite field, including characteristic 2. Splitting V=im A ⊕ ker A gives B(im A)⊆ker wedge²A and B(ker A)⊆im wedge²A. The B fiber has dimension r(C(n,2)-C(r,2))+(n-r)C(r,2). Central shear conjugation removes B, proving one automorphism orbit for each r; counting image subspaces and complements yields the exact N_{n,r}. The cubic E_n(x) and exact Taylor identity prove the fixed-q two-neighbor tail and growth constant, not merely asymptotic guesses. Independent SymPy exponent/discriminant checks and direct matrix enumeration for (n,q)=(2,2),(2,3),(3,2) corroborated all three histograms and all claimed finite boundaries. The all-n proof was reconstructed from the actual assigned RESULT.md, not inferred from VERIFY_OK. No substantive correctness flaw found.

## originality

FAIL

An October 13, 2026 full published theorem on identical free two-step Lie algebras already gives the entire finite-field rank polynomial and one automorphism orbit per rank. The assigned count is coefficientwise identical after an elementary exponent identity. The remaining fixed-q mode/tail/growth statements follow by one-variable cubic optimization and Gaussian bounds from that earlier exact polynomial; these are straightforward corollaries, not distinct unknown mathematical facts.

## value

FAIL

The object and invariant—Lie retractions and induced image ranks—are inherently natural and valuable. However the submitted claim repeats the previously published complete count, allowed ranks and orbit classification, while the two-neighbor probability/growth constants follow by routine derivative/Taylor/maximum-term estimates applied to that already-known closed polynomial. No distinct non-implied structural lemma, motivated open cutoff, or independent exact invariant remains; the bounded verifier only reproduces already-known small cases. This is a duplicate/corollary rejection, not a judgment that finite-field enumeration lacks value generally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
