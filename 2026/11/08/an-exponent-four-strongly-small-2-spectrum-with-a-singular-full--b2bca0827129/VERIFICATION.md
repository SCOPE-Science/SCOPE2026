---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Checked the actual RESULT.md and finite CHECK.py in frozen tree. The reversible (16,6,2) difference set on (Z/4)^2 gives a real even Fourier sign with every normalized coefficient ±1/4 (independently enumerated all 16 characters). Tensoring gives s_j(-z)=s_j(z), s_j(0)=1 and q_j=4^j. The local density f_j=1+a b_j(w)cos(pi t/2)+i a q_j 1_{w=0}sin(pi t/2) has Fourier support {0}∪{(s_j(z),z)} with coefficients a s_j(z)/q_j, and each nonzero local set is disjoint from its negative. For 0<a≤1/2, the strictly positive p_j=1+a b_j cos has independent bounded g_j with Haar means 0 versus rho means a²/2; dyadic Chebyshev–Borel–Cantelli yields mutually singular infinite product rho and Haar. Because sum_j ||f_j−p_j||_1=a/6, L¹(rho) product perturbations converge to complex singular mass-one mu with exact Fourier support and variation norm ≤exp(a/6). Parseval gives ∥mu*mu∥₂²=∏(1+a⁴/16^j). If gamma has finite block support, E∩(gamma−E) is finite, since every outside block must vanish; character twists and total-variation L¹ approximation then prove |alpha|*|beta| absolutely continuous for every alpha,beta∈M_E. Finite computations corroborate the seed and do not replace the infinite proof.

## originality

PASS

The relevant existing theorem of Ohrysko gives the general finite-intersection/product-perturbation mechanism and explicit examples in exponent-six products and odd-prime-exponent products, but no exponent-four construction in the publicly readable statement. A coordinate change cannot map their cyclic torsion exponents to (Z/4)^N. The nonstandard new ingredient is the order-16 reversible even flat sign that permits antipodal cancellation in pure exponent four. This is a best-of-knowledge PASS subject to significant full-text/access priority risk; the primary full paper could not be inspected, so no whole-paper absence claim is made.

## value

PASS

The existence of a strongly small-2 non-Riesz set on a pure 2-primary compact group is a natural algebraic boundary for the earlier explicit exponent-six and odd-prime counterexamples. The proof supplies a reusable explicit Fourier-flat finite seed, exact singular full-support witness and quantitative L² convolution norm; it is not a mere renaming of a previously treated torsion group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
