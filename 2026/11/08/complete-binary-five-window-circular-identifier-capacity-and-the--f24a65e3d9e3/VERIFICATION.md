---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the exact capacity profile

The complete certificate comprises `witnesses.json`, `verify.py` and `verify_independent.py`. Run both independent standard-library Python checks from their directory:

```text
python3 verify.py
python3 verify_independent.py
```

The direct checker confirms every listed cyclic word of length \(5\le k\le32\) contains exactly \(k\) different five-windows, that different words in the same family have disjoint window sets, and that each claimed family reaches the upper bound except \(k=7\). It independently enumerates all \(128\) binary words of length seven into \(20\) necklace classes, identifies precisely \(12\) valid necklaces, checks the proposed three-group cover, and verifies every within-group pair intersects. Result: `DIRECT_CERTIFICATE_OK`.

The second checker constructs the directed five-bit de Bruijn graph, independently enumerates all its length-seven simple cycles, finds exactly \(12\), checks no four are vertex-disjoint and at least one triple is, then recomputes the entire constructive witness table as vertex sets. Result: `INDEPENDENT_DIGRAPH_OK`. Both results were observed with the included files.

The infinite tail \(k>32\) is proved by the 32-window counting argument, not by finite simulation. Exact limits: binary alphabet, cyclic index-sensitive five-windows, noiseless observation, no reversal identification. No independent scientific audit was performed.
