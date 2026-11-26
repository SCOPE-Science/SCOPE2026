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

For a six-cycle with divisisors d_i=5^{e_i}, put D=prod d_i. The product of the matrices [[0,d_i],[1,1]] has determinant D and has D as an eigenvalue, so its trace is D+1. Expanding the trace as cyclic binary walks gives 1 plus the weighted nonempty independent-set sum: each isolated zero contributes the divisor for the transition into it. This independently recovers the frozen determinant equation. Modulo five, the proper nonempty undivided set must induce one edge and one isolated vertex (independent-set counts by size: {1}, {2,3}, {4,5,7}, {7,8,9}, {12}). No divisions would give 1=17; all six divisions give a normalized sum at most 17/125. The twelve surviving supports each attain equality at the minimum three positive exponents, and increasing any one makes the normalized sum strictly decrease. Replay `python3 /workspace/reproductions/2.py` for the twelve transfer-matrix support checks and exact primitive fixed lines, yielding rotation representatives (1,1,2,3,1,4) and (2,9,11,4,3,7). Each entry of a periodic orbit is prime to five, so only multipliers coprime to five work. After removing the common factor of two to its highest power, the nonzero parity pair has period three; in a three-cycle the largest entry must be the undivided sum of the other two, forcing (5^u-1)(5^v-1)=4 with u,v>=1, impossible. This establishes all positive six-periodic points and excludes shorter positive periods, not longer periods or convergence. The frozen checker was inspected, not run. Its raw signed permutation count (20) is distinct from the count of surviving monomials (18).

## originality

FAIL

The earlier 2026-10-25 UTC Resultary record gives both families, exhaustiveness for every positive fixed point of the six-step map, and minimality. The central transfer trace and the frozen cyclic determinant impose the same weighted identity. The frozen presentation does not leave a materially different classification.

## value

FAIL

Exhaustiveness at the shortest period is a natural question and would be useful if unknown, but the earlier record already proves it with effectively the same weighted identity. No new cycle, bound, or broader theorem remains; the six-by-six encoding does not itself constitute a substantive new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
