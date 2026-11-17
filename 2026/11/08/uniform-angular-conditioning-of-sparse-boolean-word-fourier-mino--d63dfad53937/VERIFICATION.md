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

The entry identity (1+a)^|A cap B| = sum_{C subset A cap B} a^|C| with a=omega-1 gives F=Z D Z^T on the downward-closed Boolean support poset; unitriangular Z proves invertibility for m>=2 and produces the exact Möbius inverse indexed by A union B. F-J differs only on pairs with intersection: at most n b_(n,r)^2 such pairs and each error <=2, giving O_r(n^(r-1/2)) Frobenius error independent of m. F^-1 differs from its origin rank-one component by union-size >=1 entries, with squared Frobenius remainder O_r(|a|^(-2r)n^(2r-1)); the dominant entry is a^-r(n^r/r!+O_r(n^(r-1))) uniformly because |a|<=2. Multiplying yields the sharp uniformly relative n^-1/2 law; rank-one gap estimates yield extremal vector claims. Independently built F, Z D Z^T and explicit inverse, checked both products for (n,r,m)=(7,1,3),(8,1,13),(7,2,5),(9,2,31), with max residual below 10^-9. Exact asymptotic needs fixed r; finite cases are not its proof.

## originality

PASS

General meet-matrix factorization/inversion and the m=2 Boolean-ball specialization are already known, and the published fixed-alphabet *full* Hamming-ball theorem has a different row/column index set when m>=3. The submitted angle-dependent sharp asymptotic is uniformly valid for arbitrary m_n, unlike fixed-q full Hamming balls. Fresh searches and a full-text neighboring theorem comparison did not identify a matching two-parameter statement.

## value

PASS

This is a sharp reconstruction-stability law for a natural polynomial-size subset of the multivariate Fourier matrix, explaining the combined n^(2r) dimension amplification and angular blowup [2 sin(pi/m)]^-r with no relation required between n and m. The extremal singular-vector localization identifies which coordinates cause instability. A growing modulus changes the actual numerical difficulty; this is not merely applying fixed-q conditioning with a renamed parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
