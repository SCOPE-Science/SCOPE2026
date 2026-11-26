---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For S_1 the special first-branch value at zero is N-1; in the other branch the fraction is k+k/(N-1) for 0<=k<=N-2 and floors to k=N-1-z. For S_{N-1}, the ceiling branch has the same expression with 1<=k<=N-1 and gives k after subtracting one; the last state maps to zero. Thus the two branch maps are reversal and cyclic increment, including wraparound. Each swaps parity. Restricting the second iterate to even states z=2j gives j -> -j for C_1 and j -> -j-1 for C_{N-1}, modulo N/2. Both maps are involutions. Because N/2 is even, the first has exactly two fixed points j=0,N/4 and the second has none. Every cycle alternates parity, so each such fixed point gives exactly one primitive two-cycle, and all remaining states are in primitive four-cycles. The two partners at the first endpoint are N-1 and N/2-1, giving the stated pairs. The counts are (N-4)/4 and N/4 for four-cycles, respectively. The order is the lcm of primitive periods; at m=2 the first endpoint is exactly order two and the second remains order four. A d-cycle contributes d fixed points at exponents divisible by d, giving the zeta factor (1-t^d)^(-1) and thus both formulas. Independent replay: python3 /workspace/independent_checks.py 4 recomputed exact rational floors and ceilings and enumerated least return times for 16,376 endpoint/state pairs, at both controls for m=2..12, including the identities of the two-cycles. This is bounded corroboration; the orbit argument proves all m>=2.

## originality

PASS

Choi et al. define the identical map and prove bijectivity and a discrete Lyapunov law; their conclusion identifies period classification as unfinished. The exact endpoint primitive spectra and orders are not supplied by those results. The zeta factors are standard consequences of the census, not a separate claim of novelty. This is a bounded judgment on the inspected sources.

## value

PASS

Period dependence is expressly open as a systematic question in the paper introducing the map. The two extreme admissible controls are natural boundary cases. Their all-precision classification shows the sharply different two-cycle counts and the collapse from the unhybridized shift's N-step order to four at the right endpoint. Together with the paper's different Lyapunov diagnostic this illustrates why that diagnostic alone does not determine finite orbit length. The contribution is the exact mathematical boundary census, not an assertion about interior controls, postprocessing, or applied security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
