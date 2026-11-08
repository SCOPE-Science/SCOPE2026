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
# Complete finite checks

Run `python3 verify_heawood_dominance.py` using Python 3.10 or later. No third-party dependencies are needed. The program generates the seven lines of the Fano plane, all incidence edges and both equivalent descriptions of the dominance complex. The first test matches all 8,851 faces using point-first order; the second runs the line-first order independently. For each, the entire directed Hasse graph of 52,304 face-covering relations is explicitly built and topologically sorted, checking acyclicity rather than assuming it. The 168 invertible ternary-bit linear maps and the 168 point–line duality compositions are enumerated, tested for graph-automorphism status, and individually tested for signed reduced Lefschetz trace. All 336 traces equal one. The saved file `verification_output.txt` is reproduced exactly and ends with `ALL_CHECKS_PASS`.

The theorem's integral conclusion uses Forman's exact acyclic-matching theorem; no field computation, timeout, experiment on a proper subset, or outside certificate is substituted for proof. The rank-one degree-six homology action follows from the signed Lefschetz calculation. The checker proves nothing about larger planes, publication priority, or external audit.
