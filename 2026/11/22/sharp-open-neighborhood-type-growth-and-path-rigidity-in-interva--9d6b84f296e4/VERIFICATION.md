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

For generic marked endpoints each nonempty interval-query trace is recoverable from its minimum included right endpoint and maximum included left endpoint. There are at most B=1+binom(m+1,2) query traces, minus one per strict containment pair. A probe just past the earliest right endpoint or just before the latest left endpoint reproduces that mark's open trace; if these marks coincide, their m−1 containments more than compensate for the missing second probe. Thus equality for m≥3 excludes containment, requires all B contiguous blocks, and makes every interior marked trace noncontiguous. Each interior singleton block forces its two neighbors to be disjoint; a noncontiguous marked trace then requires both consecutive overlaps. Conversely a proper ordered path representation has a private segment in each marked interval, so probes give all contiguous blocks and the interior marks give every extra pattern. Thus every ordered path as an ordered graph extends, with an appropriate representation. The statement does not guarantee extension of arbitrary fixed coordinates: an ordered path may be represented with containment. The endpoint marks both give the middle singleton at m=3, so realizing eight traces requires nine vertices; their singleton traces differ for m≥4, and omitting the already realized block probes attains the one-vertex-per-trace lower bound. The m=1,2 witnesses and the 8-to-13 shattering boundary check directly.

## originality

PASS

The exact numerical maximum and resulting VC dimension are covered by the distinct same-day indexed record 4. The supported distinctive claim of this stronger theorem is the necessity of the ordered-path structure at equality together with exact minimum host order, including the exceptional nine-vertex minimum for three marks. No equivalent classification or order theorem was demonstrated in the bounded checks. This does not assign priority to either same-day record.

## value

PASS

The equality classification determines which marked induced graphs can generate the maximum. The exact order threshold explains where an optimal realization can assign one vertex per trace, and why the smallest shattered support forces an extra vertex. Neither structural piece is obtained by evaluating the trace polynomial alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
