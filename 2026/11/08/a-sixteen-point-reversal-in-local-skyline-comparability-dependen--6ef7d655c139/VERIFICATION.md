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

# Reproduction and limits

Run `python3 pareto_overlap_verifier.py` with Python 3. The checker exhausts independent coordinate-rank configurations with the first coordinate fixed by label exchangeability; it independently compares exact mixed moments with finite rational sums, checks planar harmonic expressions and their cutoff, and tests the disjoint sign for bounded parameters. The recorded run passed 957 exact assertions. Its exhaustive searches concern only the stated finite parameter sets. The proof in `RESULT.md` supplies the infinite-parameter statements by algebra and integral inequalities. No external or independent audit is claimed.
