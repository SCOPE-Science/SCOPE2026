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

Formal Euler-product extraction via U_m gives b_m(m^r-1)=[q]H_(r-1). Integral binomial Newton bases yield coefficients α_s(i), with α_s(s)=m^s and α_(i+1)(i)=-(i)(m-1)m^i/2, and α_3(1)=m(m-1)(m-2)/6. The weighted induction m^(k+j-1)|a_(k,j) eliminates j>=2 modulo m^(k+1). Under gcd(m,6)=1, m|α_3(1) and the remaining a_(k,1) recursion gives m^(r-1)((m+1)/2)^(r-2) modulo m^r, a unit for every m>=5 coprime to 6 and all r>=2. Independent recurrence checks of m=5,7,25,35 for bounded depths corroborated; m=3 failure at r=4 correctly excluded.

## originality

PASS

Rødseth–Sellers gives prior m^(r-1) divisibility and the integral operator method, but this leaves the next base-m digit indeterminate. Żmija 2024 extends divisibility bounds to other bases and 2017 gives higher-power algorithms; no inspected theorem states the uniform closed leading unit for arbitrary r. Related published m-ary four depth-three branch gcds are for differently shifted indices and do not imply this exact all-ones unit. Search incompleteness remains.

## value

PASS

Sharpens a classical all-power m-ary divisibility statement on the natural base-m all-ones index tower into an explicit nonzero first m-adic digit for every admissible m and depth. Valuation exactness matters in arithmetic partition theory and is not automatic from older divisibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
