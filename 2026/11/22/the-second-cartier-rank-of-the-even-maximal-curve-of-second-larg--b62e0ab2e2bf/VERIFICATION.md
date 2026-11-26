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

The equation is L(x)=y^(2r+1) with r=q/2 and exponents of L powers of two. At infinity over k(y) the negative valuation of a root is −(2r+1)/r; its denominator forces degree and ramification index r. The affine cover is étale since L′=1. The local parameter y²/x changes under each nonzero kernel translation by a term of order 2r+2, giving different exponent (r−1)(2r+2). Thus dy has divisor (2r(r−1)−2)P∞. The monomials x^i y^j dy with (2r+1)i+rj no greater than that number are indexed by j=2h or 2h+1 and 0≤i<r−1−h; distinct valuations and the genus count prove a basis. For odd intermediate y-degree, write the x-polynomial as E²+xO². A vanishing Cartier image implies E=T O and hence P=L O², impossible for nonzero P of degree <r. For even intermediate y-degree only odd x-degrees survive. The leading term of x^aT has degree a+r/2, so these polynomials cannot cancel the lower plain monomials with which they are grouped. In the even-y case, odd-indexed shifts retain those distinct high leading terms; even-indexed shifts retain only x^(a+1), already in the plain span. At both steps different nonzero branches have distinct output y-degrees, since the even/odd images land in the separate high/low ranges. The x-powers of degree <r are independent over k(y), so the ranks of these separated branches add. For N=r−1−h the paired contributions simplify to floor(N/4)+(N−1)/2 if h is even and 3N/2 otherwise. With r=4K the four-entry blocks give 18u−14, except the final block 1+3+0; summation gives 9K²−5K and subtracting from genus yields the displayed kernel dimension. The endpoint q=8 gives rank 4. Independently I used L+L²=x+x^(2r), so x=x^(2r)+y^(2r+1)+y^(4r+2). Expanding just the exponent of x modulo four gives the direct C² columns by retaining y-exponents 3 mod 4 and taking fourth roots of their square-free y components, then reducing x^r using L(x)=y^(2r+1). Exact sparse binary elimination gave ranks 4,26,124,536,2224 at q=8,16,32,64,128. This bounded calculation checks the count by a different extraction method; the all-q result follows from the parity and injectivity proof. Package replay path check_cartier.py was inspected, not run.

## originality

PASS

The same-family genus and first Cartier rank are prior. The distinct evaluated invariant is the second rank on holomorphic differentials, equivalently its second kernel dimension, not an Ekedahl–Oort classification. The prior Cartier rules supply input to a further rank calculation but not the dimensions of the relevant images and intersections.

## value

PASS

For a distinguished infinite family of maximal curves, the next Cartier step measures image loss not visible to the known a-number. The closed formula is a meaningful exact filtration datum for future torsion and finer invariant computations; it is neither a small numerical example nor a recasting of the first rank. The claim is properly restricted and does not infer the full Ekedahl–Oort type.

The dated certificate retains the supplied scientific assessment, sources and limitations.
