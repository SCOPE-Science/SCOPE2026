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

# Reproducible exact verification

The certificate and verifier describe both fully bidirected graph models explicitly, using ascending lexicographic ordered-pair arc labels. Run `python3 verify.py morse_certificate.json` from the folder containing the two files. The standard-library verifier enumerates all legal arc subsets twice by different methods, checks every augmented Hasse incidence for two distinct acyclic matchings per graph, computes every signed integral gradient-path contribution and compares all resulting critical masks and Morse boundary entries to the certificate.

The checker then diagonalizes each integral Morse boundary using only unimodular integer operations and verifies that the entire uneliminated block is zero. This is the integral torsion check; ranks over two finite prime fields alone would not suffice. Independent unreduced simplicial boundary ranks over primes two and three provide a separate computation.

Expected counts: 6497 faces, including empty, and 29160 Hasse incidences in each graph; Wagner has 3194 matched pairs and critical ranks 15, 52, 32, 10; the cube has 3193 pairs and critical ranks 8, 51, 40, 12. The resulting reduced integral homology is torsion-free with Wagner ranks 4, 41, 32, 10 and cube ranks 6, 45, 36, 12 in degrees three through six. The recorded output is in `verification_output.txt`.

The verification establishes the exact finite statement and no assertion of a complete homotopy type, general infinite-family classification, uniqueness in the literature, or independent human validation.
