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

Kitano--Nakae prove \(\Delta_K\doteq P_T(\Delta_{\hat K})^2\). In the UFD \(\mathbb Z[t,t^{-1}]\), a reciprocal Laurent polynomial is a Fox--Milnor norm exactly when every self-reciprocal irreducible orbit has even multiplicity; multiplication by the reciprocal square \((\Delta_{\hat K})^2\) changes those multiplicities only by even amounts. Thus \(\Delta_K\) is a norm exactly when \(P_T\) is. For a repeated numerator polynomial \(Q\), \(Q^n\) is a norm for even \(n\), while if \(Q\) has any odd self-reciprocal irreducible multiplicity then the same obstruction remains for odd \(n\). The polynomial \(2t^2-3t+2\) is self-reciprocal and irreducible because its discriminant is \(-7\), so the advertised odd-copy obstruction is correct.

## originality

FAIL

The exact multiple-tangle source already supplies the factorization \(\Delta_K=P_T(\Delta_{\hat K})^2\), while Fox--Milnor supplies the classical norm obstruction. The asserted independence from the partial knot and the odd/even repetition rule are then immediate unique-factorization consequences of multiplying by a reciprocal square. Under the required implication-level standard, the fact that Kitano--Nakae do not print the sliceness corollary verbatim does not make this a new result.

## value

FAIL

Applying a classical factor-parity obstruction to a published product formula is mathematically useful bookkeeping, but the odd/even law and partial-knot independence require no new structural lemma once those ingredients are known. Under the shared value bar this is a routine source-specific corollary rather than a substantive new boundary or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
