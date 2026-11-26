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

The nontame part of the odd-prime cyclic unit group has order p^(m−1); its e-th powers form 1+p^min(m,s+1) R. On the prime-to-p factor the image has order r. Raising v to p−1 removes the tame factor and is invertible on principal units, so condition (P) is exact. For v in the image, each of h residue roots has p^d lifts. The affine iteration multiplies b by S_e(u). For u≡1 mod p the integer odd-prime lifting identity gives valuation min(s,m), also directly true for u=1. Otherwise u−1 is a unit and (u−1)S_e(u)=v−1 gives valuation ν_m(v−1). Multiplication by a coefficient of valuation j has image p^jR and kernel size p^j, including j=m. Summing these disjoint root classes proves the stated target formula. For each of the (r−1)p^(m−1−d) nonprincipal multipliers all p^m translations occur; for each of the p^(m−1−d) principal multipliers exactly p^(m−a) occur. This proves the image size and depth stability for m>s. It also gives the identity, field and tame-exponent cases, and the final p-element image followed by collapse along the indicated (p−1)p^s chain, not an ordering claim for arbitrary larger integers e. Translation order p^m and an embedded unit of order p−1 force the sharp group exponent. The frozen checker and log were inspected, not executed. A separate affine doubling count (`python3 /workspace/independent_checks.py 4`) passed 1,017,468 target comparisons on the frozen grid: 280 rows, 215 distinct (p,m,e) triples because the input lists repeat some exponents. These finite checks do not establish the universal quantifiers.

## originality

PASS

Best of current knowledge, the distinct result is the complete prescribed-target two-contribution count at arbitrary odd-prime cyclic-ring depth and every positive exponent. The closest same-family word-map source treats Engel words, not powers. Known affine group structure, order and character data provide ingredients, not the evaluated translation multiplicities for all multiplier-root classes. No claim of novelty for the geometric sum identity, cyclic roots, the field boundary alone, or the elementary exponent calculation.

## value

PASS

The holomorph is a standard affine group and exact unary word fibers are natural invariants. The uniform count in one multiplier stratum and the two nested-ideal contributions in the other identify a sharp root concentration and exact attainable fraction across depths, not just a known group exponent, a single census, or reuse of a cyclic-unit formula. The image-density and terminal-chain statements clarify the distribution's behavior; no broad extension to all chain rings or even primes is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
