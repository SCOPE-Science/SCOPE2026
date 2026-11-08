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

# Reproduction of exact finite-state checks

Run `python3 verify.py` in the same directory. It uses only the Python standard library.

The verifier constructs the sixteen-state reverse maps directly from the local Boolean polynomial, computes the four eight-element image sets, and checks each of the eight restricted bijections. It independently verifies the specified root-loop permutations and their orders; an exhaustive permutation-closure search constructs all \(40320\) distinct permutations of eight indices. It checks the two coprime lifted-cycle lengths \(6\) and \(35\).

For each length \(2\le N\le13\), the program enumerates all \(2^N\) input words, forms an output histogram by applying the *forward* rule, and compares every target's direct fiber size to the fixed-point count from the reverse-map permutation extension. This supplies exactly \(\sum_{N=2}^{13}2^N=16380\) independent target comparisons. It also verifies that seven-predecessor targets are absent throughout and checks the nine integer rencontres counts.

Expected output:

`VERIFY_OK group_order=40320 lifted_cycle_lengths=6,35 cyclic_targets=16380 limit_numerators=14833,14832,7420,2464,630,112,28,0,1`

The verified finite enumerations establish the quoted exact graph and group certificates; the all-size conclusion uses the mathematical proof of strong connectivity, coprime cycle lengths and Perron–Frobenius convergence. The calculation neither proves an optimal spectral gap nor constitutes an independent external audit.
