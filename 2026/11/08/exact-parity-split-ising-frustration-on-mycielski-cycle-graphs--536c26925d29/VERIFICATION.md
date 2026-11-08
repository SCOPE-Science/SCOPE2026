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

The hand proof in `RESULT.md` minimizes each shadow spin exactly, then proves the sharp cyclic-word inequality and enumerates all equality cases for every integer \(n\ge4\).

Run `g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`. The executable enumerates all \(2^{2n+1}\) physical-spin configurations for each \(4\le n\le11\), testing energies, multiplicities, and the full ground-state magnetization profile. All eight cases passed.

Run `python3 verify_transfer.py`. It separately uses a four-state max-plus count recursion after exact local elimination, for each \(4\le n\le201\); all 198 cases passed. Neither finite test is a certificate of the general theorem on its own. The energy convention, graph edges, and the unique minimizing choice for each shadow spin are specified in the proof. Independent scientific audit has not been performed.
