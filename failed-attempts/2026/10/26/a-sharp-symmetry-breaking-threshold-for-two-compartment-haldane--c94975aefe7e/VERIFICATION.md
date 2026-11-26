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

FAIL

The frozen Finding asserts two strict global maxima above threshold. They are distinct and tied by reflection, so neither is a strict global maximum. For example, b=2, N=6 gives 3−4/√5 and 3+4/√5 at the same value 25/64. They are both global maximizers and each is a strict local maximum. The proof also incorrectly says the threshold cubic is negative at 2√3 for all b≥0; it equals −8b there and vanishes at b=0. The underlying classification with these corrections checks out: with u=x(N−x), the denominator is positive, the derivative numerator G decreases from a positive value, and its right-endpoint sign is the sign of 12N+8b−N³. At equality J′=0 and J″<0, so reflection yields a negative quartic. With M=N²/4, differentiation of G(N,u*)=0 yields (N²−4u*)′=4(d/dN)G(N,M)/G_u at the threshold, giving 3(L_b²−4)/(2L_b). Expanding the explicit root gives the asserted large-N terms. The supplementary independent replay `python3 /workspace/independent_checks.py 3` checks the rational reduction, onset, high-load coefficient and exact example. It also finds 14,392 in-range derivative trials rather than the 14,400 candidates printed as tests by the frozen checker. The finite checks do not certify the theorem.

## originality

FAIL

A distinct indexed finding supplies the same constrained allocation theorem, explicit maximizing branches and onset under equivalent coordinates, with a derivative proof that also yields the local types. This is established mathematical coverage in the current catalogue, not evidence that the other record was publicly first: its listed date is later than the frozen record's. The remaining distinctions are the regular b=0 limiting case and extra high-load Taylor terms of the same explicit solution, not a separately substantive, uncovered classification. The negative verdict concerns distinct content as reviewed, not an allegation about authorship or historical priority.

## value

PASS

As mathematics, the full fixed-total classification addresses a natural nonconcave optimization: inhibition changes the optimizer from equal loading to two interior unequal allocations, with a sharp onset and a useful high-load interpretation for a static model. The value of that full classification is separate from its lack of distinctness here. Extra terms of the same optimizer or the regular zero-parameter boundary do not support a separate repair on their own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
