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

# Reproducibility and boundaries

The embedded `verification/theta_two_particle_check.py` is a standalone Python program using only the standard library. Running `python verification/theta_two_particle_check.py` prints the recorded output saved as `verification/run_output.txt`. Actual checks encompass exact enumeration of vertices, edges and squares of the unordered two-particle Abrams complex, the square boundary identity, uniqueness of free edges, integral cycle-basis reduction, cellular automorphisms, and full trace comparisons. Every arm permutation and both choices of pole swap were checked for \(m=2,3,4,5\). For \(m=6,7\) identity, reversal and cyclic shift were checked. The \(m=2\) case is a boundary consistency test only; the stated group-automorphism theorem starts at \(m\ge3\).

There are \(2m^2\) oriented edges and \(m(m-1)\) squares, with one uniquely paired free edge per square. The surviving graph has cycle rank \(\binom m2\). The program checks all \(\binom m2\) basis cycles and their signed images for every sampled automorphism, including the pole-swap sign. Formal correctness for infinitely many \(m\) depends on the direct cubical collapse and chain identities in RESULT.md, rather than the tested finite range. The graph braid stable-equivalence theorem of Prue–Scrimshaw is the external topological input.

No independent audit, equivariant homotopy classification, or verification for higher particle counts is asserted.
