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
# Verification scope

Run `python3 verify_q4_character.py` with Python 3.10 or later. The program needs only the standard library and reconstructs the graph, independence faces and full symmetry group. It checks \(742\) faces, all \(2816\) Hasse covers, \(367\) matched pairs, \(384\) signed simplicial traces, and Fourier multiplicities on all \(16\) translation characters. The program certifies an acyclic complete matching via a full topological sort; a list of critical counts alone would not be enough.

The delivered file `verification_output.txt` is the actual standard output of the checker. The checker was run again after the files were read back from the delivered JSONL row and its output matched the embedded record byte-for-byte. The proof's use of discrete Morse theory and semisimple characteristic-zero representation theory is mathematical reasoning in addition to the finite certificate. No claims beyond the sixteen-vertex graph are inferred from enumeration.

No independent audit or external mathematical certification has been performed.
