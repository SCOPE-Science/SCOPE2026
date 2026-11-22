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

# Reproducibility
Run `python verify.py` with Python 3. The program uses only the standard library and makes no web requests. It checks 393,216 products exhaustively for \(n=2\) and \(k=2\), all 2,989 prescribed level/matching profiles for \(1\le n\le7\), \(1\le k\le5\), and 7,920 deterministic random examples over small truncated polynomial chain rings, plus 1,830 checks over \(\mathbb Z/2^k\mathbb Z\) using direct enumeration of image modules. The image-generator count uses additive dimensions of the image and its radical multiple and is separate from the theoretical Hall-cover proof.

Expected concluding line: `VERIFY_OK`. The program does not enumerate all triples in arbitrary size, does not certify absence of undiscovered prior work, and is not a substitute for the universal proof. The correctness argument for arbitrary finite commutative chain rings is in `RESULT.md`.
