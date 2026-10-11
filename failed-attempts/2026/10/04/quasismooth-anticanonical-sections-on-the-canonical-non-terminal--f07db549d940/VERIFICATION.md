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

On the canonical nonterminal boundary \(d=b-a=r\) or \(a=r+d\), the anticanonical degree becomes respectively \(2b\) or \(3a\). The pure heavy monomial handles one heavy axis and the two-heavy stratum, leaving only the other singleton criterion. The three allowable monomial congruences reduce to the displayed divisor conditions, giving the two divisor families and two extra points after removing the common endpoint. The exact verifier checks every boundary pair for \(2\le r\le150\) and confirms the count \(\tau(2r)+\tau(2r-1)+1\).

## originality

FAIL

Resultary already contains the broader published theorem 'A divisibility criterion for quasismooth anticanonical hypersurfaces in two-heavy-weight projective spaces', which gives necessary and sufficient three-way divisibility tests for every \(\mathbb P(1^r,a,b)\) in the full canonical strip. A second published SCOPE theorem gives the exact triangular canonical/terminal region. Restricting those two results to the nonterminal boundary and simplifying the congruences yields the audited divisor list and count. Under the required implication standard, this boundary theorem is a covered special case.

## value

FAIL

The divisor count is a neat corollary, but once the full quasismoothness criterion and the exact canonical boundary are already published, obtaining this list requires only substituting the two equality cases and simplifying divisibility conditions. It is therefore a routine special-case extraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
