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

# Reproducible exact verification

Run `python3 VERIFY.py` in the directory containing `CERTIFICATE.json`. These two files are complete and require only Python's standard library. `VERIFY_OUTPUT.txt` contains the recorded output of a successful replay.

The verification reconstructs every graph edge, all ten perfect matchings by recursion, and independently scans the complete set of six-edge candidate matchings. It processes exactly 988 fault sets of cardinality zero through three, checking each nerve as the common-edge intersection complex of surviving perfect matchings. It replays all 2,632 certificate free-face pairs with direct exhaustive searches of proper cofaces in the current complex. Every residue is confirmed to be either empty (no perfect matching) or a connected one-dimensional graph. The first Betti rank is obtained from exact graph counts, and the Euler characteristic of each ORIGINAL perfect-matching complex is independently evaluated by generating its original graph-edge faces.

The exact table asserted in RESULT.md is encoded as assertions, including the two exceptional alternating outer-rim triples. The proof uses no random sampling, finite field substitution, unverifiable logs or conditional computational timeout. It makes no claims for faults of size four or above. An independent human mathematical audit is not recorded.
