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

Left translation factors a unitary from the Fourier blocks and leaves aI+b pi(g)* for g=x⁻¹y. Across the regular representation each root of unity occurs n/m times, from n/m cycles of length m. These blocks are normal, hence their singular values are the moduli of their eigenvalues; dividing the sum by √n√(|a|²+|b|²) gives (1). With lambda=2|ab|/(|a|²+|b|²), the normalized mean of √(1+lambda cos(phi+2πj/m)) is concave in lambda with derivative zero at 0. It strictly decreases for lambda>0 if any cosine is nonzero; when all cosines vanish (only an orthogonal phase at m=2), the constant mean 1 is strictly larger than the balanced cancelling value 1/√2. For phase zero this exception cannot occur. At lambda=1 the positive cosine-modulus sum is periodic and satisfies S''=−S<0 between its zeros of individual summands, so all minima are at a cancelling summand. All such locations have the same sum by cyclic permutation. The phase relation b/a∈−mu_m and the signed constant follow from 2∑_{j=1}^{m−1}sin(πj/m)=2cot(π/(2m)). For phase zero, pairing j and m−j gives 1+2∑_{j=1}^{floor((m−1)/2)}cos(πj/m); finite cosine summation yields cot for even m and csc for odd m. With x=π/(2m), x cot x decreases as x increases while x csc x increases; the monotonicities are strict. Lagrange and Cauchy give the smallest possible nonidentity order p. In even-order groups order two gives 1/√2 and strictly beats all other orders (odd m have D_m>2√2/π); in odd-order groups the largest realized order minimizes D_m. The order-21 example is the nontrivial semidirect product C₇ ⋊ C₃, not a direct product. The control character in the typesetting of the semidirect-product symbol is a presentation defect; independently checked the intended example using the action by multiplication by 2 modulo 7, with 14 elements of order 3 and six of order 7.

## originality

PASS

Credit the trace formula as a direct consequence of the earlier two-spike rank proof's full regular spectral multiplicities. Also credit the equal-positive root mean and parity/order dependency, including the two-point indicator specialization, to overlapping known or same-day comparisons; do not infer precedence from a shared date. What remains distinct is the complete optimization over nonzero coefficients in this trace/ℓ² ratio: unique balancing in both classes, all optimal complex phases, exact normalized sharp minima, and the signed-versus-positive comparison for arbitrary finite groups. No stronger inspected claim supplies that coefficient optimization.

## value

PASS

The complete coefficient minimum and its equality classification are useful exact sparsity benchmarks for the normalized Fourier-algebra/trace objective, including the first genuinely variable support size. Positive and arbitrary complex coefficients have different arithmetic minimizers in the nontrivial odd-order cases where the least prime and largest actual order differ. The classification explains that contrast through a sharp equality condition on coefficient balance and cancellation, rather than merely recomputing an indicator norm or a rank count. It also covers coincidence of the optimizing orders, without falsely asserting strict separation for all odd-order groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
