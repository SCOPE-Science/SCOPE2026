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

A word is specified by its first symbol and its +/-1 differences in Z/3. The endpoints of a candidate triple are distinct exactly when its two signs have a common value e, in which case the triple contains all three symbols. The swap leaves its two internal adjacencies proper; an existing outside neighbor clashes with the new endpoint exactly when its original outside sign was e, since 3e=0. Thus the swap starts at exactly a maximal two-run, including runs at either boundary. Distinct swaps change distinct two-element sets of positions, so counting legal indices counts distinct outputs. Given a composition of m into run lengths, there are six words, and each part of size two contributes one to degree. This proves the series, filling all degrees with ones and twos, and shows the top coefficients by placing the unique leftover one when m is odd. The derivatives at u=1 give E[D]=(m+1)/8 and E[D(D-1)]=(m-2)(m+3)/64 in the specified ranges, hence the variance and the edge count by handshaking. Interior indicators of -++- or +--+ have mean 1/8; joint probabilities at lags 1,2,3 are respectively 0,1/32,1/64, so the positive long-run variance is 7/64. The bounded 3-dependent CLT and at most two boundary contributions yield the normalized limit. At u=0 the reciprocal cubic has one root in (1,2); its two stationary values are negative and the complex roots have modulus lambda^(-1/2). The simple positive dominant pole is not canceled, proving the frozen fraction rate. The attached checker was inspected, not executed.

## originality

PASS

The exact maximal-run distribution is already known, including the two-sign rather than just the success-run version. Credit is specifically for the graph-theoretic characterization of all admissible distance-two swaps as maximal two-runs of ternary differences, and hence for the degree law as a graph invariant. The graph conversion is not provided by the exact run theorem or by the adjacent- and star-swap results. No independent originality is credited to the run enumerator, frozen sequence, or routine deductions from them as binary/composition results.

## value

PASS

The useful content is the local characterization of every one-move output in this natural proper-coloring graph. It directly decides isolation, possible degree, and the set of valid initial swap positions without generating or testing neighbor words, and identifies which classical exact distribution governs that graph. The run counts by themselves, including the database sequence, are not a separate mathematical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
