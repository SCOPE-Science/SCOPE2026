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

# Verification

Run `python3 verify.py` using Python 3.8+ standard library. The checker enumerates all \(1072\) primes less than \(19000\) congruent to one modulo three, compares two independently derived length-four color spectra for every prime, and confirms the exact list of \(39\) exceptional primes. Extra cube-set consistency tests are performed for seven boundary primes. The output explicitly verifies that \(547\) misses just \((0,2,2,0)\) for \(g=2\), while \(571\) is complete.

For the remaining infinite range, independently inspect the proof's orthogonality expansion, character-sum bound with distinct roots, support weights \(24+64+48=136\), excluded-start contribution at most \(4\cdot27=108\), and positivity of \(p-136\sqrt p-108\) for \(p\ge19000\). No finite calculation certifies this asymptotic estimate. No external independent audit was performed.
