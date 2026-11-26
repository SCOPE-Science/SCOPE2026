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

An anchored cycle using all five-bit edges defines exactly one incoming-to-outgoing matching per four-bit vertex and conversely a single 32-cycle in the successor permutation defines exactly one de Bruijn rotation class. No reversal/complement quotient is taken in this count. Independent bit-prefix enumeration rooted at 00000 and enforcing all four wrap windows recovers 2,048 words; XOR/popcount over all 31 nonzero rotations independently computes the signed periodic correlations. All 47 bins match exactly, including endpoints 192:12 and 1952:4, missing multiples, the three plus one four-element extremal orbits, and moments 2813/4 and 1336631/16. Symmetry pairs opposite shifts; each correlation is divisible by four, and the balanced antipodal shift has an even number of unequal pairs and is divisible by eight, giving energy divisibility by 32. Balance at each lag below five comes from uniform five-windows. Parseval with unnormalized forward transform gives fourth-power sum divided by 32 less 1024. Replay: python3 /workspace/branches/independent_replay.py 5; output /workspace/branches/independent_replay.out. Frozen scripts were inspected, not executed.

## originality

FAIL

A distinct same-date Resultary record provides a per-cycle table of the full periodic signature and orbit labels for exactly these 2,048 rotation classes, in the same autocorrelation normalization. Taking squared norms and tallying already supplied rows mechanically yields the energy histogram, moments, extremal classes/orbits and 1024/E distribution; the histogram need not be printed there. This is coverage, not a determination of relative priority. The checked journal papers give weaker aggregates or extreme single-lag values rather than that full coverage.

## value

FAIL

Periodic energy is a natural aggregate and the finite histogram would be independently useful if exact cycle-level data were unknown. Here all the asserted quantitative and symmetry results are direct projections of the richer existing table. A re-enumeration and normalization check validate the numbers but do not add an independently needed classification or identify a distinct surviving result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
