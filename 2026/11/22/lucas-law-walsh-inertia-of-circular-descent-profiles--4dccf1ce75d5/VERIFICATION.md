---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Each character is an eigenfunction of counting XOR convolution with eigenvalue n! times its mean under the uniform descent law; the characters are a full basis even when eigenvalues coincide. For a proper frequency an unmarked edge cuts the cycle into a path; different marked runs involve disjoint blocks of positions. Independent continuous labels yield a uniform rank permutation and prove independence of the within-block rank permutations, including for consecutive runs separated by just one unmarked edge. A run of length r therefore gives A_{r+1}(−1)/(r+1)! in the expectation. The Eulerian series specializes to 1+tanh z. The odd coefficients alternate and are all nonzero: in f'=1−f² for f=tanh z, the contributing products at each positive even order all have the same sign, opposite to the sign of the next odd coefficient. The constant and all even positive degrees are as stated. For the full frequency, rotate the maximal element to the final position; the wrap contributes one descent and the n rotations are distinct, so that multiplier is −n A_{n−1}(−1). This checks the normalization, all signs and both parity cases. The supported proper masks are uniquely covered by matching within each even run (an end vertex forces the next edge). The full mask at even n is the only collision, of the two perfect matchings. The two-state edge indicator matrix gives the ordinary matching enumerator as its trace-power, with roots of x²−x−t; at t=1 the trace is L_n and at t=−1 it is 2 cos(nπ/3). Subtract the excess full-cover term at even n, with its correct sign (−1)^{n/2} at t=−1; sum and difference then give the two nonzero inertia counts, and the complementary dimension gives nullity. L_n~φ^n, yielding the stated fraction. Independent exact enumeration agreed on all 504 multipliers at n=3,…,8; the separate checker and logs are `independent_circular_descent_check.py`, `check_3_5.txt`, and `check_6_8.txt` in `/workspace/branches/3a015977-3acf-41ae-8106-385f368efda7/`. This is a finite cross-check, not the basis for the all-n assertion.

## originality

PASS

The positional linear Walsh result already gives the proper-mask formulas by rotation to an unmarked edge. The full-mask multiplier is the classical circular Eulerian identity at −1. The supported distinct claim is the resulting cyclic spectral assembly, especially the single double-cover correction and exact all-n positive, negative and zero multiplicities. The strongest inspected prior sources do not supply that inertia. No priority certification is inferred from identical or same-day catalog hits.

## value

PASS

The cyclic Fourier-diagonal operator is natural and is not specified by the distribution of total cyclic descents. Its exact support and inertia determine recoverable and lost directions and quantify the sign imbalance, including a specific even-cycle correction and an arithmetic periodicity absent from the path rank count. This is a complete usable spectral classification of the stated invariant, not a small-order curiosity or only a reformulation of an Eulerian identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
