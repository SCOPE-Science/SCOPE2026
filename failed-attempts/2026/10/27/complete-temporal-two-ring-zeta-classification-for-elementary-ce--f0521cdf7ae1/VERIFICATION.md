---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For k=1,2, a based length-n closed walk in the 2k-bit overlap graph has a periodic bit string x obtained by taking the first bit at each successive step. Shifts force the vertex at step i to be (x_i,…,x_{i+2k-1}) modulo n, also when n is shorter than the window. The edge tests then impose exactly the kth-iterate fixed-point constraints, and a labeled cyclic configuration gives the inverse walk. Thus trace counts configurations, not rotation classes. The formal log-determinant identity gives integer denominators of degrees at most 4 and 16 and the quotient D/E. On the second-iterate fixed set, the dynamics is an involution, so the difference counts exact-period-two configurations and half of it counts temporal two-orbits. Independently enumerated labeled configurations under direct cyclic updates for every rule and n=1,…,16, with no use of the uploaded graph or verifier code. The formal coefficient recurrence applied to these direct counts determines all denominator coefficients given the degree bounds. All rule entries, class memberships, 51 ordered pairs, 40 second denominators, and 25 coprime ratio classes matched. The first-witness histogram is (64,48,6,17,2,12) for 1–6, with 107 identical denominator pairs, which implies absence at every length; 12 first witnesses at six prove optimality. Replay: python3 /workspace/branches/independent-checks/check_eca.py with the frozen package directory. The uploaded generator imports the verifier's computations; these are not two independent implementations. The direct reproduction is distinct. No conclusion is drawn about higher temporal periods or infinite spatial lattices.

## originality

FAIL

Distinct indexed record SCOPE-20261117-78b8bdccc729 gives the same all-rule sharp witness statement, absence count and ordered zeta census, and supplies the per-rule denominator polynomials and first witnesses. I cross-multiplied the polynomials from its actual 256-row table and independently obtained exactly 25 quotient classes. That quotient count is not claimed verbatim in the inspected prose but is a mechanical regrouping of the exact indexed data. This is demonstrated equivalent coverage, not a conclusion about priority, independence or derivation between the two records.

## value

FAIL

The natural all-rule invariant and sharp finite detection bound are worthwhile in isolation. In this record, however, they reproduce an equivalent indexed classification. Reducing and regrouping the already-tabulated pair data gives the 25 count mechanically, with no distinct structural consequence demonstrated. Independent reproduction validates the mathematics but is not a new result of the stated kind.

The dated certificate retains the supplied scientific assessment, sources and limitations.
