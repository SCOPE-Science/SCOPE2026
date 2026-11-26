---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The angular expansion of f0+bar(z)f1 exhausts the full space: one scalar sector at -1 and two dimensions per nonnegative mode. With x=n+1, the truncated beta law normalized by q^x is the law of qS for S~Beta(x,1). For the standardized degree-one polynomial, this gives compressed first moment −sqrt(x(x+2))(1−q) and compressed second moment q²+x(x+2)(1−q)² after division by q^x. In multiplying the two matrices the cross-terms linear in their diagonal differences cancel, leaving the signed (r−q) factor claimed. Each positive branch has two singular values, and coincident branch values add multiplicities; no simplicity across different modes is required. All these blocks are invertible for distinct cutoffs, so the scalar sector gives the complete kernel. Exponential decay proves fixed-cutoff Schatten membership. The exact formula on the u=epsilon(n+1) grid converges uniformly on interior compacta, with envelope ab|a−b|(u+epsilon)^3 exp(−(a+b)u); this controls both tails of power sums and maxima. The limiting maximum is at u=3/(a+b), and the rate optimization reduces to maximizing w(1−w²), with w=|a−b|/(a+b). Strong convergence of the compressions follows by dominated convergence on each vector and uniform contractivity. Independent 40-digit quadrature of the moments gave signed block entries .122213505, .0270662057 and .008350872055 at (n,q,r)=(0,.3,.7),(5,.42,.91),(19,.7,.93), matching the formula to within 3e−42 at working precision. For rates (1,3) and epsilon=.001, independently summed finite-mode ratios to the analytic limits were .999990920, .999999250 and .999999033 for powers 1/4, 1 and 2; the norm ratio was .999999694. These are corroboration only; the supplied checker was inspected, not executed.

## originality

PASS

The general block representation is established prior work, and the finite-cutoff formula is an explicit low-degree evaluation of it, not a new diagonalization theorem. The surviving main contribution is the moving two-cutoff spectral profile with sharp norm and all-Schatten constants; no covering result was identified in inspected material. In particular, compactness for each pair does not decide whether the pairwise commutator retains order-one norm when both cutoffs move.

## value

PASS

The full bianalytic space is the first radial Bergman setting with genuine matrix-valued fibers. Two increasing concentration regions provide a natural test of whether compressions becoming identities retain noncommutativity. The result locates the escaping order-one modes, quantifies their combined mass at all powers, and determines the sharp rate ratio rather than merely exhibiting two operators that fail to commute.

The dated certificate retains the supplied scientific assessment, sources and limitations.
