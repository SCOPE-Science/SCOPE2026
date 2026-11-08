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

Run `python3 verify_clebsch_dominance.py` from the directory holding the embedded program, using only Python 3 standard-library modules. The accompanying `verification_clebsch_dominance.txt` records the exact expected output.

**Actual executed checks:** independent forbidden-closed-neighborhood and complement-domination criteria on every one of \(2^{16}=65{,}536\) masks; strongly regular graph parameters \((16,5,0,2)\); complete face vector and \(-130\) Euler characteristic; independently enumerated independence number \(5\) and minimum vertex cover \(11\); deterministic 26,799-pair discrete-Morse matching with one critical zero-cell and 131 critical nine-cells; all 401,088 nonempty-face Hasse covers; complete acyclicity proof by topological sorting 53,730 faces; and two SHA-256 certificate fingerprints.

**Claim-to-evidence:** the critical-cell distribution plus a full finite acyclicity check satisfies the hypotheses of Forman's discrete Morse equivalence. Because the resulting CW complex has only one zero-cell and nine-dimensional cells, its attaching maps are all constant; this proves the integral wedge rather than just mod-prime homology. Independent Euler and vertex-cover computations cross-check, but do not replace, the matching certificate.

**Boundaries:** the checker exhausts a single explicitly defined sixteen-vertex graph, not an infinite family. It is reproducible ordinary source code, not an independently commissioned certification. Neither the graph's automorphism homology character nor a publication-priority theorem is claimed or tested.
