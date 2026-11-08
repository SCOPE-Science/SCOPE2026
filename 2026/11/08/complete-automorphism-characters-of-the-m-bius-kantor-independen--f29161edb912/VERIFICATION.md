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

Both bundled programs are standalone and reconstruct the graph and complexes independently. Run `python mk_rank_exact.py` and `python mk_character_certificate.py`, then compare their stdout with `mk_rank_exact_output.txt` and `mk_character_output.txt`. Exact integer-domain boundary ranks give reduced rational Betti ranks 4 and 1 in degrees three and four. The second program checks signed boundary compatibility, all 96 graph automorphisms, every top cohomology sign modulo 101, all 13 conjugacy classes, and class-averaged character norms. All finite assertions are about the single defined graph. No independent audit has been performed.
