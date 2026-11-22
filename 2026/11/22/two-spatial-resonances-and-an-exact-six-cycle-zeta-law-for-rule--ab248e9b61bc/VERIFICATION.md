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

# Reproducibility checks

Run `python3 verify_transfer.py` in the package directory. It rebuilds all temporal-column constraint graphs from the local Rule 22 truth table, runs an exact Tarjan decomposition, determines all cyclic-block characteristic polynomials using integer closed-walk counts and Newton identities, and verifies the determinant ratio \(D_6(z)/D_2(z)=(1-z^8)^3(1-z^{10})^2(1-4z^{10})\) as a coefficient identity. The \(p=1\) and \(p=3\) transfer determinants agree exactly. All graph vertices are covered; this is a complete finite certificate supporting an all-length trace theorem.

Run `python3 verify_direct.py`. Independently implemented bitwise Rule 22 enumerates all \(2^n\) states for each \(3\le n\le20\) and checks exact first, second, third and sixth returns. It verifies the predicted number of primitive period-six configurations at every tested size, including nonzero cases at eight, ten, sixteen and twenty. These bounded tests alone would not prove a universal result; the transfer correspondence and complete exact graph block calculation establish the unbounded claim.

Both scripts require only Python 3's standard library. No network access, random sampling, external reference files or nonstandard arithmetic packages are required. Independent audit has not been performed.
