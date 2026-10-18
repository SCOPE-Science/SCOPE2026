---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For rational cohomology of unmarked genus-zero degree-two stable maps to P^(n-1), Kiem-Moon gives P_n(q)=(1-q^(n-1))(1-q^n)(1-q^(n+1))/((1-q)^2(1-q^2)). The source polynomial uses q=t², hence odd-degree cohomology vanishes. First differences multiply by (1-q) and use coefficients c(j)=floor(j/2)+1 for nonnegative j in 1/[(1-q)(1-q²)]. Up to relevant middle indices, d_k=c(k)-c(k-n+1)-c(k-n)-c(k-n-1); shifts of two numerator factors begin only at degree 2n-1. For n=2m+1, d_(n-1+s)=m-s; for n=2m, d_(n-1+s)=m-1-2floor(s/2). These yield plateaus of width 2 (odd n), 1 (n divisible by 4), 3 (n==2 mod4), exact claimed central positions, and peak floor(3n²/8). Palindromicity (degree 3n-4) supplies decreasing half. n=2 boundary checked, no unsupported higher-degree claim. Independent exact rational-polynomial expansions for n=2..50 verify all peaks, indices and symmetry, but proof is coefficientwise.

## originality

FAIL

FAIL: Kiem--Moon Theorem 1.3(2), expressly crediting Getzler--Pandharipande, gives the closed all-n Poincare polynomial, which determines every Betti number and directly entails the maximum and all plateau positions by one elementary first-difference calculation. The submitted claim does not introduce new geometry or a distinct classification beyond this stronger published all-coefficient theorem. Wording of the exact peak is absent, but claim-vs-prior implication is decisive; failed keyword searches are not treated as novelty proof.

## value

FAIL

FAIL: The peak/plateau is a natural invariant, but all coefficients are already explicitly known and the new claim is routine arithmetic extraction from that complete generating function; no substantive separate geometric, computational or classification gap remains. The mod-four widths are arithmetically neat yet are not a separately motivated unknown non-implied fact under this audit value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
