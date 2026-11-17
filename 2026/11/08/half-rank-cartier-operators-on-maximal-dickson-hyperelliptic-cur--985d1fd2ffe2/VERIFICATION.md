---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The cover Y_n:w²=t^(2n)+1 is smooth since p∤n; the tame involution t->t^-1,w->w/t^n has quotient X_n with invariant differentials eta_i=omega_i-omega_(n-i). For each i=1..n-1, hyperelliptic Cartier coefficients of (t^(2n)+1)^((p-1)/2) are nonzero binomial terms iff the least residue r_i=pi mod 2n lies in 1..n-1, in which case i maps to one distinct output. Under p²=-1 mod2n, theta(i)=min(r_i,2n-r_i) is a fixed-point-free involution on 1..n-1 switching active and inactive indices; i and n-i have equal activity, hence exactly (n-1)/4 active invariant pairs. This also forces n=1 mod4. Iterating transitions multiplies i by p²=-1, outside active index range, giving C²=0, and rank g/2 implies imC=kerC. Smoothness, genus g=(n-1)/2 and a=g-rank are consistent. Independent modular calculations of Cartier rank and square zero for 6 admissible (p,n) pairs confirm, but infinite proof is the residue involution.

## originality

PASS

The prior Tafazolian-Top 2019 quotient construction and maximality criterion are same family and fully credited; Borges-Reis 2026 proves small automorphism group, also credited. Maximality over F_(p^4) implies Cartier nilpotence, not its first rank. The newly evaluated g/2 Cartier rank and g/2 a-number are not provided by these prior statements. Resultary same-day rational Jacobian group theorem for exactly same curves over finite fields concerns prime-to-p rational torsion and is logically orthogonal to geometric p-rank/a-number. A 2025 closely relevant paper on Chebyshev maximal curves only had abstract available, creating residual priority risk. Borges-Reis full arXiv unavailable and Oxford vpn_disconnected: no claim of document-wide noncoverage.

## value

PASS

The Jacobian a-number measures local p-torsion and is not determined by supersingular Newton slopes, maximum point count, or rational Jacobian group abstract structure. Uniform half-rank computation for a natural maximal low-automorphism curve family, with explicit genus-six cases in infinitely many characteristics, is a motivated exact geometric invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
