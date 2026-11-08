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

The complete finite-graph proof is given in `RESULT.md`, with the standalone Python 3 verifier `verify_heawood.py`. Execute `python3 verify_heawood.py` from the directory containing that script. It needs only the Python standard library.

The script reconstructs the seven Fano lines as three-point sets closed under binary XOR, builds the 14-site incidence adjacency matrix, and checks that every vertex has degree three. For each of all 3003 six-site subsets, it constructs the seven-by-seven detection matrix consisting of the all-ones row and six point or line indicator rows. Fraction-free integer elimination determines exact rank, producing successes by point count \((7,84,420,868,420,84,7)\), 1890 successes and 1113 failures.

As an algorithmically independent check, for every one of the same 3003 subsets it computes the 14-dimensional adjacency Krylov span from basis vectors at the chosen sites, using the first four matrix powers. Rank is checked modulo 1000003, and all 3003 results agree with the exact-rational criterion. The characteristic relation \((A^2-9I)(A^2-2I)=0\) shows that these four powers are sufficient to span each Krylov space. This modular corroboration is not used alone to prove a rational non-rank.

The symmetry checker constructs 168 invertible Fano coordinate changes, composes them with point–line polarity to obtain 336 adjacency-preserving permutations, and partitions every six-site set into 24 orbits. Exactly 14 orbits are successful. Counts and orbit totals are checked against the explicit generating polynomial.

The analytic argument is valid for all positive site-specific loss strengths; the finite verifier uses only graph and rational-incidence data. No proof of a uniform decay-time bound, robustness to Hamiltonian disorder, or independent scientific audit is asserted.
