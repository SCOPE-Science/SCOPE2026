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

For either G-leading directive, the unprimed denominators start q_0=1, q_1=a_1 and stay odd because each later partial quotient is 2. The modified endpoints Q_N=q'_N are not the parity selectors: Q_1 is even. Thus Theorem 54 takes the G-leading, both-unprimed-denominators-odd, a_{N+2}>1 branch, including N=0, and gives R_v(n+1)=n+3Q_{N+1}+Q_N for Q_N≤n<Q_{N+1}. Its Q recurrence has roots 1±√2 with a nonzero dominant coefficient for either a_1. Writing m=n+1 turns the block into Q_N+1≤m≤Q_{N+1}. The mesh m/Q_N has spacing 1/Q_N and endpoints tending to 1 and α=1+√2, so its cluster set is [1,α]. On it the ratio is 1+(3Q_{N+1}/Q_N+1−1/Q_N)/(m/Q_N). Compactness excludes all other limits, and rounded, clipped integer arguments attain each x in the limiting interval. The decreasing map 1+(3α+1)/x gives endpoints 3+√2 and 5+3√2. The excluded initial length m=1 does not affect the limit set. The record, certificate, and verifier were inspected. The verifier was not run, and its parity assertion on line 26 is tautological; the branch was instead checked directly from the primary theorem.

## originality

FAIL

The inspected primary paper does not explicitly state this cluster interval. It does, however, already determine the exact recurrence function and the endpoint scale for both languages. The claimed interval is a mechanical corollary of those results: the scale ratio converges, the rescaled integer mesh fills a compact interval, and the normalized formula is the reciprocal image of that mesh. The finding does not add a separate return-word theorem, an extension to other languages, or any second-order result.

## value

FAIL

The invariant and the extremal pair are natural, and reporting the full cluster set is more informative than reporting only the limsup. But the exact full interval is mechanically recoverable from the published all-length recurrence theorem via the limiting integer mesh. There is no independent residual invariant, example separating the two languages, or structural result. The calculation is useful exposition of the published theorem, not a distinct exact contribution under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
