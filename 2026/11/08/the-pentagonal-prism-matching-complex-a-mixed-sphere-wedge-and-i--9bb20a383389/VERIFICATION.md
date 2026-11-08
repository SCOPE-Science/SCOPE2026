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

# Reproducible verification

Run `python3 verify_prism_matching.py` with standard Python 3.9 or newer. No external packages, network calls or additional data files are required. The program prints a distinctive final verification marker, plus the face and incidence counts, critical-cell vector, zero integral differential, mod-two ranks, symmetry representation and ordinary-versus-perfect face comparison. `verification_output.txt` is the output recorded from a real execution of the included script.

The program checks the complete fifteen-edge power set independently of the incremental face generator. It constructs two full discrete Morse matchings, reverses exactly their paired Hasse incidences and topologically sorts the resulting entire directed incidence graph. It computes exact signed integer boundaries by gradient elimination and by the stabilized chain flow; it checks that integral flow representatives are cycles. For each generating automorphism, it calculates the induced integral chain action with orientation signs, projects onto the critical homology basis, crosschecks the character using the second Morse matching and checks signed simplicial Lefschetz traces.

The resulting Morse CW complex has one zero-cell, two two-cells and two three-cells, with a zero integral degree matrix. The homotopy deduction uses the fact that the two-skeleton is a wedge of two two-spheres and that attaching maps of three-cells to it are determined by their degree vectors. The independent mod-two boundary ranks are supplemental, not the basis of the integral claim. The calculation proves no general result for arbitrary circular-ladder length and does not establish equivariant wedge splitting.
