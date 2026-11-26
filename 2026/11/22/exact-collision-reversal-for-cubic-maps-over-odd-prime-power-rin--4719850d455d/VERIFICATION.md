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

Count zeros of LQ with L=x-y and Q=x^2+xy+y^2+c. For p>=5, completing the square gives #Q=p-chi_p(-3) since the constant is nonzero and the quadratic character sum follows by factoring a difference of two squares. The conic is smooth and meets the diagonal at I=1+chi_p(-c/3) points with Jacobian determinant 6a nonzero. Exactly one vanishing factor gives p^(k-1) lifts per point. At each crossing, Hensel via x at fixed u=x-y gives a bijection with u,v in the maximal ideal modulo p^k. Count u=0 separately; each valuation 1<=r<k contributes (p-1)p^(k-1), including the empty range for k=1. The smooth-only count is 2p-chi_p(-3)-2I, yielding the displayed formula and strictly opposite signs at k=1 and k>=2. At 3, the difference quotient on each source disk reduces to c, so injectivity modulo 3^k on that disk and equal cardinality give bijectivity onto its target disk. The reduction (1+c)x assigns either disjoint target disks or the same disk; squaring the fiber sizes yields 3^k or 3^(k+1). Independent replay: python3 /workspace/independent_checks.py 2 checks 240 direct ordered-pair counts across six odd primes, multiple exponents, all unit residues, and negative and positive lifts, up to modulus 125. These finite tests corroborate but do not replace the proof.

## originality

PASS

The supported distinct contribution is the explicit all-depth ordered collision law for the unit-perturbed cubic and its Legendre-class reversal, not the general lifting method, the use of character sums, or a new permutation criterion. There is close existing work on the same observable for a quartic, and distinct Dickson fiber theorems. None of the compared exact statements gives this parameter regime. This is a best-of-knowledge decision.

## value

PASS

The second moment is the exact independent-input coincidence statistic for a basic cubic family. It detects a change in the ordering of collision probabilities missed by reduction modulo p, and distinguishes bounded from linearly growing normalized counts over every depth. The explicit class reversal and uniform law, not just application of Hensel lifting or a finite check, justify the claim's value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
