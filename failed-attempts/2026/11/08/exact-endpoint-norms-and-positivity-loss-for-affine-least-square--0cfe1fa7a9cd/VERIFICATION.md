---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Covariance E[Y_iY_j]=delta_ij/(d+2) gives K_d(x,y)=1+(d+2)x·y and unit row mass. Rotational invariance and convexity make row absolute mass maximal precisely on |x|=1; negative part is the spherical cap Y·u<-1/(d+2). The one-coordinate beta density gives C_d=(d+2)c_d∫_{1/(d+2)}^1(t-1/(d+2))(1-t²)^((d-1)/2)dt; integration by substitution yields the stated incomplete beta expression. A Gaussian sphere/ball-coordinate representation plus bounded second moment gives the dimension limit. Independent exact polynomial integrals at d=1,3,5 yielded C_1=1/3, C_3=64/125 and C_5=11097/16807 and independently reproduced the earlier ball-box formula specialized to k=0. Correctness is not an originality finding.

## originality

FAIL

Decisive prior full coverage: published 2 November 2026 Sharp affine-projection norms on ball–box products proves the exact L-infinity operator norm, exact nonnegative-input defect, unique product-boundary norming locations, sign extremizers, and high-dimensional limit for B_2^d×[-1,1]^k for EVERY d>=1 and k>=0. Setting k=0 gives precisely the submitted uniform solid ball, and its H_{d,1}(-1/(d+2))=(C_d)/(d+2) makes the earlier norm formula 1+2C_d. Thus all claimed parts are a direct, nontrivial but already established special case; differing incomplete-beta presentation is not novelty.

## value

FAIL

The solid-ball affine projection norm and sharp positivity-loss problem are mathematically motivated, but this exact claim with all extremizers and limits is already contained in a stronger complete ball–box theorem. Its k=0 evaluation is a mechanical specialization, not an unknown independently useful exact fact. The correct original package does not have a surviving separate value-bearing result suitable for acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
