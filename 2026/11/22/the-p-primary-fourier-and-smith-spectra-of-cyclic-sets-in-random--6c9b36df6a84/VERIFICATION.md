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

A fixed cyclic set of r>0 vertices carries an independent permutation and a directed forest rooted at that set. The reduced complete-graph Laplacian nI−J on the n−r nonroot vertices has determinant r n^(n−r−1), with the empty determinant at r=n giving one. Thus the convolution coefficient is c_r=r! r n^(n−r−1) for r<n, with c_n=n!. The weight-k multiplier is the scalar product of these coefficients with the coefficients of (1−z)^k(1+z)^(n−k). For r=n−1−m≥1, one has v_p(c_r)=b+ma−v_p(m!)+v_p(r), since v_p(n−i)=v_p(i) for 1≤i<n. Legendre's bound v_p(m!)≤(m−1)/2 gives v_p(c_r)≥b+a for m≥1, and ≥b+2a for m≥2 (m=2 directly). For 0<k<n the sole leading term modulo p^(b+a) is c_(n−1)(−1)^k(n−2k), with v_p(n−2k)=v_p(k)<a. At k=n the two terminal terms sum to (n−1)! n(n−2); the r=n−2 Krawtchouk coefficient is −binom(n,2), supplying a further p^a in that term, and all earlier terms are already divisible by p^(b+2a). This proves the boundary valuation b+a, including n=3. The trivial shell counts n^n. The Walsh matrix is invertible over Z_(p) because its square is 2^n I, so diagonalization yields the local Smith factors, exact rank after normalization, and determinant assertion. Every kernel coefficient is divisible by p^b, which also directly proves that the normalization is integral. Independent leaf-pruning and signed summation over all maps gave the shell multipliers (27,−7,−1,−3) at n=3 and (3125,−13,−39,−169,−163,−165) at n=5; recursive polynomial coefficient checks agreed at n=9,25,27,49,81,121,169 as well. These are corroboration, not the proof for all p,a.

## originality

PASS

The exact weighted cyclic-set distribution is classical. The closest same-object signed spectral record gives a negative-sign regime but no p-adic valuation classification. The distinct supported contribution is the prime-power valuation in every shell, with a separate endpoint cancellation, and its explicit local Smith consequences, not the enumeration, Walsh transform, or generic Smith theory alone.

## value

PASS

This is a complete exact obstruction to local deconvolution for a natural counting kernel, not a finite valuation table. It distinguishes recovery power by character weight throughout an infinite family and accounts separately for the two endpoints, including cancellation at full parity. It also decides nonvanishing of the entire spectrum in the stated regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
