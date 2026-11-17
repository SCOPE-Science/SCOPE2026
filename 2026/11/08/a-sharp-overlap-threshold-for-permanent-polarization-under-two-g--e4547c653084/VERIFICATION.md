---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The two hyperedges are the entire vertex set; each is odd and neither contains the other. If both inactive, shared vertices force global consensus. The first effective clock event chooses uniformly among active groups. After one group becomes monochrome, only the other can act; after it acts, the two private blocks have fixed opposing opinions. Every subsequent shared-block flip is dominated by its private block exactly when 2s<a and 2s<b, yielding a closed alternating class; otherwise consensus occurs within four effective updates. Fair-initial averaging correctly includes the sole-active clock correction. An independently written state enumerator (not the supplied verify.py) checked every labelled configuration in six structures including (3,3,1),(5,5,s=1,2,3),(3,5,1),(5,7,2), and reproduced probabilities 1/4,5/16,1/8,0,9/32,5/32.

## originality

PASS

The 3-uniform loose hyperstar/two-triplet case is explicitly known and not new. The all-odd-group-size, all-overlap conditional first-event law and averaged binomial-tail boundary were not implied by inspected 3-body, mean-field, adaptive or lattice-block works. Identical title in Resultary is the assigned finding. Best-of-knowledge with residual sparse-hypergraph priority risk.

## value

PASS

A complete class/absorption classification for a natural minimal overlapping-group model, with exact conditional and fair-initialization probabilities and sharp structural overlap boundary. It isolates permanent polarization despite connectivity and distinguishes active updates from time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
