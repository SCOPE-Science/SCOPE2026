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

# Reproducibility and verification

The finite domain is precisely the \(3^{10}\) assignments to the ten labelled vertices of each of \(GP(5,1)\) and \(GP(5,2)\). The rule has three deterministic cases: excited goes refractory, refractory goes rest, and a resting site excites only with two or three excited neighbors. The zero vector is a fixed state.

Run `python3 verification/check_python.py` with NumPy; run `g++ -std=c++17 -O2 verification/check_independent.cpp -o check_independent` then `./check_independent` with a C++17 compiler; and run `python3 verification/check_geometry.py` using only Python's standard library. Each program exhausts every assignment independently and checks complete extinction by update four, the time histogram, and the terminal excitation-support coefficients. `verification/results.txt` records a successful full execution of all three programs. The latter program constructs the Petersen graph from disjoint two-subsets and the prism from two five-cycles, independently of the two GP edge enumerators. These verifiers prove a finite, fully covered assertion; they do not prove the absence of an earlier equivalent result or extend the claim to other graphs.

The noncomputational four-cycle obstruction follows by taking any second-generation excited vertex, its two first-generation neighbors, and the shared initial excited neighbor forced whenever at most three sites were excited initially. The four are distinct and form a four-cycle. This lemma needs no computation; the sharpness and exact population counts use the complete finite enumeration.
