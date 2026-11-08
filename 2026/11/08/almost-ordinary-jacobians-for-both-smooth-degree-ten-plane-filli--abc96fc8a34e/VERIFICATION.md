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

All three scripts are self-contained Python-standard-library programs and use only exact finite-field arithmetic.

Run `python3 verify_smoothness.py`. It constructs the three homogeneous gradient generators for \(F_k\), substitutes each of \(X=1\), \(Y=1\), and \(Z=1\), and runs a Buchberger reduction over \(\mathbb F_7\); each of six tests explicitly reaches the constant polynomial \(1\). This proves geometric nonsingularity, not merely smoothness at rational points.

Run `python3 verify_cartier.py`. It expands the homogeneous polynomial \(F_k^6\) in \(\mathbb F_7[X,Y,Z]\), extracts the classical degree-seven-adjoint Hasse--Witt matrix, verifies its \(36\)-determinant is zero and a specified \(35\)-minor is nonzero, and repeats for the square. This proves exact Cartier rank \(35\), stable rank \(35\), \(a=1\) and \(p\)-rank \(35\) for both smooth parameters. The modulo-seven coefficient twist is trivial, so ordinary matrix squaring is correct.

Run `python3 verify_points.py`. It enumerates all normalized points of \(\mathbb P^2(\mathbb F_{49})\) using each of two different irreducible quadratic presentations. It returns \(95+8=103\) for \(k=1\), and \(99+8=107\) for \(k=3\), confirming the extension counts without a statistical estimate.

The three program outputs must be verified against the actual locally extracted files. These finite checks prove finite identities and exhaustive field calculations only. They do not prove any uniform-in-characteristic statement or establish historical priority. Independent audit has not been performed.
