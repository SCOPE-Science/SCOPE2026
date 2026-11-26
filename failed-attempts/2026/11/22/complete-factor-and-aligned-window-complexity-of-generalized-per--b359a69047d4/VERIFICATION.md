---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The valuation recursion is u_(2j)=0, u_(2j+1)=u_j+1 mod q. For n≥4 a factor contains a 1, which occurs only at odd indices, so the two starting phases are disjoint and yield injective encodings of half-length factor sets. The small counts q, 2q−1, 3q−1 are correct: at length three the only potential overlap is 000, which cannot occur at odd starts because it would require adjacent q−1 letters. The resulting deficit recurrences determine c(n); the step from m to m+1 cannot straddle the integral break 3·2^(h−1) without meeting it at an endpoint, and the affine branch extends consistently to the next dyadic endpoint. For odd n a factor recurs at its start modulo a sufficiently high power of two, so CRT supplies a start divisible by n. For even lengths the window is exactly a morphism image of the shorter aligned window; injectivity proves W_q(2n)=W_q(n). Strict increase of P_q yields the parity criterion, and dyadic substitution gives both counts. This is an all-parameter proof, independently corroborated below.

## originality

FAIL

Verified mathematical coverage, not a correctness defect or an access-based rejection. Sell's 2018 simple-Toeplitz complexity theorem already specializes to the entire closed factor formula for all q≥2. A distinct same-day prime-base Resultary result explicitly treats p=2 as covered by its proof and gives the identical free-part window count for all phases, including phase zero. Its intended novel range is p≥3; neither its date nor its citation record establishes priority for W_q. The exact window coverage is demonstrable nonetheless, and a distinct originality claim for the frozen combined theorem is not established. Neither the short proof nor the displayed corollaries leave a new mathematical claim within the frozen scope.

## value

FAIL

The factor/window contrast is instructive, but as a distinct result the frozen theorem leaves no independent mathematical gain: the explicit factor formula is a parameter substitution into Sell's closed formulas, the window claim restricts the verified all-phase result, and the strict parity and dyadic oscillation corollaries follow by substitution. A clean short exposition of these covered facts is useful pedagogically, but the frozen package does not add a new invariant, bound, or scope that would justify it as a distinct research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
