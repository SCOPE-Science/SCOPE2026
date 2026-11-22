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

Use Python 3 (standard library only). In the directory containing the accompanying files, run:

```sh
python3 verify_local.py
python3 verify_global.py
```

The actual recorded outputs are supplied as `local_output.txt` and `global_output.txt`. The local program computes the signed difference by directly forming the deletion and original triple histograms and exhaustively enumerates all \(k^5\) neighborhoods for \(1\le k\le5\), grouped by exact support. The global program independently forms complete post-deletion histograms of explicit de Bruijn-based witness words; it tests every deletion position for \(q=2,3,4,5\).

Both programs finished successfully; expected full-support counts are `1, 8, 90, 192, 120` and expected witness capacities are `14, 121, 608, 2069`. Exhaustive finite checks support the five-neighborhood census but alone cannot prove a theorem for arbitrary alphabet size. The general-support relabeling argument and universal-factor construction in `RESULT.md` supply that proof. The exact minimum saturation length is not independently established.
