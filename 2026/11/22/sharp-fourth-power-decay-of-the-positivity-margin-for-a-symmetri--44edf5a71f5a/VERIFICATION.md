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

Reconstructed the actual bound. For p1=1/2 write A=p3-1/2 and D=p2 sum_i x_i^2(x_i^2-1)^2, so F=A^2+9D-1/16. Rounding each coordinate to 0 or its sign at magnitude 2/3 gives |x_i^3-sigma(x_i)| <= 3 x_i^2|x_i^2-1| (the ratio is at most 6/5 below the cutoff and 57/20 above, with the zero cases immediate). Cauchy–Schwarz and the distance of a half-integer to the nearest integer yield |A|+3 sqrt(D)>=1/2, hence F>=1/16. Homogeneity rescales this to F>=16 p1^8; p1=0 is covered directly. On the p2=1 sphere, if s^2=p1^2>=1/(8n) this gives 1/(256n^4); otherwise ||x^3-4s^2 x||_2>=1/n-4s^2>=1/(2n) by the power mean and the reverse triangle inequality, which more than compensates the negative term. Independently expanded both parity witnesses by the binomial theorem: p1=1/2, q=p2=n+1/(4n) for even n and n-3/(4n) for odd n, and the two numerators agree exactly. For even n>=2 the unnormalized F is less than 13 and q>=n. For odd n>=3 it is at most 159/16 (the last two positive terms are dominated by the negative n^(-2) term) and q/n>=11/12, giving n^4 F/q^4 <= (159/16)(12/11)^4<16. Normalization divides by q^4. The exact replay is python3 /workspace/review_evidence/algebra.py (SymPy; octic block).

## originality

PASS

The polynomial, positive definiteness, and base rounding estimate are already due to Debus–Schabert. The distinct supported claim is the all-dimension matching order n^(-4) for the spherical minimum. The closest primary statement uses balanced sign vectors and proves only nonuniform positivity with a weaker even-dimensional O(n^(-2)) upper bound. The strongest matching catalog entry is the frozen record itself. No distinct coverage was established in the inspected sources.

## value

PASS

This is the particular octic at the center of a dimension-uniform SOS obstruction, so its spherical margin is an independently motivated invariant. The result pins down the rate of loss of positivity in every dimension rather than just its eventual loss; it exhibits a near-balanced mechanism missed by the exactly balanced witnesses and rules out faster-order decay for all real directions. It does not claim new SOS certificates or their degree bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
