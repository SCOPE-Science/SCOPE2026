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

PASS

Colour exchange makes the fixed m=floor(N/2) choice exact for W_n. A disconnected colour implies that its complement is connected, so k-1 cross-component edges are necessary and sufficient when the disconnected colour has k components. A specified cut of a edges is empty with probability at most 2^(-a)(1+1/N)^a ≤ e·2^(-a). Two isolates use a=2n-3; a component of size two uses a=2(n-2); cuts of sizes 3 through floor(n/2) contribute at most e·2^n·2^(-3(n-3)). Thus the non-singleton exceptional probability is O(n²4^(-n)), and the expectation differs from the isolate expectation by at most O(n³4^(-n)). In the normalized central product log, the first three power sums give -1+(2-2)/n+(5-14/3)/n²+O(n^(-3)), and the higher powers sum to O(n^(-3)). For the half-integer shifts, the symmetric average of the two factors cancels odd terms; the quadratic term is δ²(A²-B)/2 with A=4/n+O(n^(-2)) and B=O(n^(-3)). This gives 2ε_n/n², so the parity-resolved coefficients are correct. Independent log-product replay gives scaled coefficients 0.3367039875 and 2.3566886531 at n=300 and 302, tracking 1/3 and 7/3 respectively; only the proof establishes the bounds on the graph events.

## originality

FAIL

The November 2 indexed rare-event theorem covers the same probability model and states the exact falling-factorial main term for both P(W_n=1) and E W_n, each with an exponentially smaller residual than the entire remainder scale of the frozen expansion, plus the identical O(n²4^(-n)) tail. The parity coefficient is an explicit evaluation of that exact main term, not additional probabilistic information. The catalogue date is later than October 18; verified mathematical coverage does not establish earlier priority.

## value

FAIL

The balanced model and the distinction between one and several wild edges are well motivated. Once the same-model theorem with the exact main term and smaller residual is accounted for, the surviving computation is a Taylor expansion of a known finite product. It supplies no distinct bound or new mechanism and does not warrant a separate validated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
