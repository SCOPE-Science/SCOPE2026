---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Set q=h+1, c=hm-1, u=floor(c/q); for residue r, admissible two-coin base costs from x-y congruent r mod m have least candidates A=r(m+1), B=(m-r)c, each repeated at +qm. Other congruence branches start after these first-two candidates by m(m+1)>qm or mc>qm, so the second threshold is min(max(A,B),min(A,B)+qm). Comparing c-qu against 0 determines the four pieces, maximizing w_r minus m yields g1=(m+1)u+(h-1)m-1+[q|m], and summing (w_r-r)/m gives the claimed genus. I independently implemented a three-denomination representation-count DP for every 3<=m<=24 and 2<=h<m (253 parameter pairs), checked all second thresholds, g1 and n1 exactly; no exception. All-unrestricted quantifiers rest on the symbolic branch inequalities, not the finite check.

## originality

PASS

No inspected earlier result supplies these explicit residuewise second thresholds and closed two-parameter formulas; general p-Apéry concepts and numerical-semigroup algorithms are credited.

## value

PASS

The full p=1 thresholds and generalized genus are natural next-level Frobenius invariants of a motivated two-parameter family. The sharp divisibility-triggered +1 jump is a structural effect invisible to the classical p=0 formulas, not a tiny unmotivated parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
