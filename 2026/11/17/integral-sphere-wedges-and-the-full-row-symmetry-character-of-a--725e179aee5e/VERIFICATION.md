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

# Finite reproducibility and scope
Run `python3 verify_chessboard.py` and `python3 verify_symmetry.py` using Python 3.10+ standard library in the same directory. Exact outputs are included. The former enumerates all 19,979 augmented faces, checks every 95,683 Hasse cover in a directed acyclicity test, constructs exact signed integral Morse chain maps, checks \(\partial^2=0\), and cancels 30 and 300 unit pivots. No inference from a partial sample is used. The latter builds signed-orbit invariant chain complexes for a row transposition and a row three-cycle, confirms squared boundaries vanish, and computes ranks at two primes coprime to six. The scientific proof explains the homotopy cancellation and the rational trace extraction; raw logs alone are not accepted as a proof. An independent mathematical audit has not been performed.
