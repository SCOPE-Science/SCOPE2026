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

Run `python3 check.py` in a directory containing the complete extracted package. Python 3 and its standard library are the only dependencies. The program generates all unlabeled trees through nine vertices by canonical leaf-extension, checks their degree sequences and matching polynomials, and verifies that exactly two size-nine pairs collide on both invariants. For the four corresponding 17-generator two-step nilpotent Lie algebras it reconstructs every Chevalley–Eilenberg differential from the graph edges, checks \(d^2=0\) through degree three, and computes exact rational ranks through the fourth coboundary. Full-matrix modular ranks over a prime field give an independent numerical crosscheck. `CERTIFICATE.txt` contains the output from execution of the packaged script.

The exact rational rank computation is a mathematical certificate for the stated finite claims when combined with the complete enumeration algorithm and its proof in `RESULT.md`. A modular check alone could not establish a characteristic-zero rank, and no finite check supplies an infinite-family conclusion. No external independent audit has been performed.
