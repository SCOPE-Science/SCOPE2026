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

Homogeneity and the extension property reduce complete types to realized finite ordered diagrams with labeled new coordinates. Independently, an internal old gap of separation depth d with k new points is split into k+1 gaps of depths at most d, with at least one equal to d. Its ordinary series for increasing placements is 1/((1-dz)(1-(d+1)z)); each exterior gap contributes (1-(h+1)z)^(-1). There are m_d-m_(d+1) internal gaps of depth d with m_0=n and m_(h+1)=1. Multiplying and labeling by r! gives the claimed EGF and cut independence. The logarithmic differences (j+1)^r-(j-1)^r have degree r-1 with leading coefficient 2r; their evaluation at 1,...,h gives det 2^h times the product of r!, 1<=r<=h. For sharpness take the alternating binomial vector v_j=(-1)^(j-1) binom(h-1,j-1); it kills all degrees below h-1 and not degree h-1. Strictly decreasing integer profiles with large gaps realize both m and m+v at the same n, including h=1. Choosing the nested surviving cut sites yields the binomial fiber formula, with no ambiguity on one or two points and the two distinct three-point gap words (1,0),(0,1). The stated concrete rational model has infinitely many *unmarked* choices in each quotient gap; the finite marked classes themselves are not dense, despite the loose 'densely interspersed' wording. The independent gap computation (python3 /workspace/independent_checks.py 3) checks the explicit sharp witnesses through h=6 and both three-point words through r=4. The frozen program/output were inspected but not executed; its collision loop itself only compares predicted values through r=3. All-arity conclusions use the proof, not the checks. Recovery by h counts assumes n is known.

## originality

PASS

The supported distinct claim is the unrestricted nested-height theorem, with sharp h-count recovery and exact multilevel fibers. A distinct same-day result gives exactly the height-one EGF and fiber, including the three-point ambiguity. This is demonstrable overlap, not evidence of within-day priority; no separate novelty credit is assigned to h=1. The stronger multilevel statement is not obtained from that one-height spectrum without new bookkeeping and an inverse across all levels.

## value

PASS

In a natural hierarchy of homogeneous ordered equivalences, the theorem determines exactly what the numerical counts retain, the sharp worst-case number of counts needed, and how many mutually nonisomorphic ordered base diagrams realize each spectrum at fixed n. The multilevel inverse and exact fibers provide more than an unmarked enumeration or a single low-height coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
