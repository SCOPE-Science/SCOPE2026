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

For the stated monic coefficient prefixes, P_0=1 and all other cases reduce by the coefficient shift to the two- or three-term remainder. Adjacent Stern values are coprime by reducing both recurrences to a smaller neighboring pair; positivity and the same recurrences give s(k)=1 exactly at powers of two. The ratio s(k+1)/s(k) is below 1 at odd k>1, is 1 at k=1, and at even k=2r equals 1+s(r+1)/s(r), giving the binary-length bound. By Eneström–Kakeya in descending-coefficient convention, roots of P_n for 1≤n≤2^h−1 have modulus at most h. For offset two a common root is the reduced rational −s(n+3)/s(n+2), hence an integer by monicity. Its denominator forces n+2=2^h and its numerator is h+1, outside the root bound. For offset three at n=2r the remainder factors as (X+1)(s(r+1)X+s(r+2)); the two roots are real but the exact even decomposition P_2r=(1+X+X^2)P_(r−1)(X^2)+s(r+1) is positive on the real axis (r>=1). At n=2r+1 the quadratic has coefficients u+v,v,v+w for adjacent positive Stern values u,v,w, is primitive by gcd(u,v)=1 and irreducible by its negative discriminant. Its leading coefficient is larger than one; by Gauss's lemma it cannot divide a monic integer polynomial. This excludes all common complex roots, hence also zero resultants, with no finite-range assumption. Independently ran 160 rational gcds against the short remainders, n=0..79 at both offsets, in /workspace/frozen_review_arithmetic.py (SymPy). Read the frozen verification note and script without executing it; the latter instead uses finite modular witnesses with degree preserved by monicity. Neither regression extends the domain of the proof or asserts nonvanishing over all finite fields.

## originality

PASS

The result concerns the monic coefficient-prefix family over Q[X] simultaneously at offsets two and three, not the positive integers obtained by evaluating a dyadic subfamily of Stern (0,1)-polynomials. The coefficient family and its adjacent resultant, root bound, and even-degree positivity are antecedents, not contributions here. The available evidence does not cover the universal two- and three-offset exclusion of common roots. The assertion of distinct content is based on the actual difference of objects and remainders; it is not a claim of historical priority.

## value

PASS

The offsets are the first cases in which the coefficient-prefix resultant no longer reduces to a nonzero constant remainder; this is a natural test of pairwise coprimality beyond adjacency. The theorem proves that no exceptional index occurs in either family, with genuinely different mechanisms for a linear remainder and for each parity of the quadratic remainder. It supplies a usable exact common-factor exclusion, not a proposed pattern from finite data or a claim for larger gaps.

The dated certificate retains the supplied scientific assessment, sources and limitations.
