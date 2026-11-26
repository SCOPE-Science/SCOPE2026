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

The divisor-totient expansion separates the nested block-averaging spaces. On the constants the scalar is p^(k-1)(p+k(p-1)); on the j-th difference space it is (k-j+1)p^(k-1)(p-1), positive also at k=1. The telescoped inverse in the H_j basis has coefficients obtained by adjacent reciprocal differences divided by the block sizes. The coefficient denominators are exactly the displayed LCM list, with m=k-j. Because differences with each exact valuation 0,...,k-1 occur, the coefficients are recovered by subtracting successive actual entries, including the diagonal; cancellations in individual entries cannot reduce the LCM. Clearing the inverse is equivalent to annihilating the cokernel. Modulo p the matrix factors as block sum, then J_p-I_p, then injective block replication. J_p^2=0 modulo p gives invertibility of the middle map and rank p. This is an all-depth proof. Separately, python3 /workspace/branches/check_circulant.py solves the first inverse column directly over Q, uses circulant shifts to read the exponent, and cross-checks Smith forms and modular ranks through selected orders up to 27. It confirmed 32, 480, 252, and 1536 for the listed composite orders, and 8748 at (p,k)=(3,3) and 245760 at (2,6). No general full Smith form is established.

## originality

PASS

Credit the spectral framework and the overlapping shallow-depth Smith computations. The supported distinct claim is the explicit integral exponent uniformly in prime-power depth, with the uniform modular rank; no inspected stronger result evaluated it at all depths. This is a bounded best-of-knowledge judgment, not a priority claim for depth one or the odd-prime depth-two subcase.

## value

PASS

The largest integral invariant factor of this natural valuation-based cyclic convolution is the least multiplier for solving every integer right-hand side over the lattice. An explicit formula with only k+1 denominators allows exact torsion calculations without forming the p^k by p^k matrix. The first-prime loss of information in the ordinary spectrum is genuine, and the modular rank gives the exact number of p-divisible factors. The value is the uniform arithmetic invariant, not a new general Smith theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
