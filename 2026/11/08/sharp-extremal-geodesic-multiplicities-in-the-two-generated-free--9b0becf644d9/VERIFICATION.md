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

# Verification record

Execute `python3 verification/check.py` with the current working directory at the artifact root. This uses only the Python standard library. The program regenerates the count of all signed input words of lengths zero through eight, independently reduces free-group words to produce their prefix-visited Munn trees and endpoints, and checks exact multiplicities for all ordered pairs in eleven cases, including four-leaf star and branching shapes. It further counts the shortest words in each tested \(\mathcal R\)-, \(\mathcal L\)- and \(\mathcal D\)-class and compares the proposed formulas. It then generates all unlabeled abstract finite trees with up to ten edges by iterative leaf addition and canonical rooted-tree encodings. It filters those of maximum degree four, computes all endpoint multiplicities, and verifies the claimed extremal formula for each edge size. Its output is preserved verbatim in `verification/output.txt`.

Expected final lines: `VERIFY_OK trees=11 endpoint_pairs=171 enumerated_words=87381` and `EXTREMAL_VERIFY_OK m=0..10`. These calculations only check a finite range and do not certify all \(m\); the mathematical proof supplies all-size quantifiers, embeddings, optimization, and limiting exponent. No independent audit has been performed.
