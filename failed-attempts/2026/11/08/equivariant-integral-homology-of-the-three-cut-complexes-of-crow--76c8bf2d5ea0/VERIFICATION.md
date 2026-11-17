---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The Alexander dual Y of the crown ordinary three-cut complex is exactly the two-row (2,2) multiple chessboard complex X on n columns, plus n omitted-diagonal edges {a_i,b_i}. For n>=5, Jojić–Vrećica–Živaljević Theorem 4.4 applies (n>=2+2+2-1), giving a connected pure shellable three-dimensional X and H3(X;Z)=Z^B with B=1+n(n-5)(n-3)(n-2)/4. Relative chain groups add n free H1 generators, so H3(Y)=Z^B, H1(Y)=Z^n and others vanish. The integral universal coefficient theorem and 2n-vertex Alexander duality give H_{2n-6}(K)=Z^B and H_{2n-4}(K)=Z^n; the full (2n-6)-skeleton and lower nonzero group give sharp (2n-7)-connectivity and non-shellability. Explicit fixed-oriented-face trace enumeration for each permutation uses the f,t,u count of 1/2/4 cycles; equivariant Alexander duality twists by sign of entire 2n-vertex action, yielding the formulas. The identity of the submitted character with the prior 2026/10/25 full character was verified algebraically via Q(f)=1-2f+4*C(f,2)-6*C(f,3)+6*C(f,4), T0=Q(f)-2t*(1-f+C(f,2))+t(t-1), T1=1-2t+4*C(t,2)-2u. The actual VERIFY.py and published shellability theorem were inspected; bounded n=5,6,7 computations corroborate but do not prove all n.

## originality

FAIL

A directly accessible 2026-10-25 published RESULT.md proves the same ordinary crown graph three-cut integral homology for ALL n>=5 and gives the same complete rational S_n×C2 characters. The earlier theorem has exactly B=1+n(n-2)(n-3)(n-5)/4, degrees 2n−6 and 2n−4, nonshellability, and parity twists (-1)^n and (-1)^(n+1). Its trace polynomials T0 and T1 are IDENTICAL to the submitted h via binomial identities, not merely agreeing on example n. Its proof uses the same Alexander-dual chessboard plus n relative matched-pair edges and identifies the top relative integral permutation basis. The new sharpened-connectivity observation follows routinely from the full skeleton condition and known nonzero H_{2n−6}; it is not a new substantive theorem. Thus the original all-in-one claim is already covered, and disclaimer/certificate cannot rescue it.

## value

FAIL

The ordinary crown three-cut and natural symmetry characters are mathematically motivated invariants, but the exact infinite-family Betti groups, non-shellability and full S_n×C2 graded rational characters have all been published before. Relabeling the old trace-polynomial parameters and adding the routine sharp-connectivity skeleton deduction does not provide a genuinely new or intrinsically valuable standalone contribution beyond established exact results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
