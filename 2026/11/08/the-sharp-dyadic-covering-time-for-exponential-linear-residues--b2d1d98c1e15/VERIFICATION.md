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

The standalone `verify.py` checks all pairs \(a\bmod 2^k\), odd \(b\bmod2^k\) for \(1\le k\le8\), verifies coverage by \(2^k+k-1\), the complete odd-base first-period permutation, and a sharp even-base witness for each \(b\). Additional tests exercise \(9\le k\le16\). The exact output observed was:

```text
VERIFY_OK all_moduli=2^1..2^8 all_b_odd all_a_mod_2^k triple_checks= 43690 sharp_witness_b_classes= 255 larger_sample_classes= 32 odd_base_permutation=PASS even_base_sharp_cutoff=PASS
```

The unrestricted result follows from the proof in `RESULT.md`, not from the finite check. No independent audit was performed.
