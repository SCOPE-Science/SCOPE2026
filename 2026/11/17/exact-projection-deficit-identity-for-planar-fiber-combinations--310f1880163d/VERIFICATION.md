---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
    ]
  }
}
---

# Independent mathematical audit

## correctness

PASS

For x in P1 intersect P2 the classical fiber sum is theta I1(x)+(1-theta)I2(x), an interval of length theta*l1(x)+(1-theta)*l2(x); outside the intersection it is empty. Fubini integrates this to area(Ftheta). Subtracting Cavalieri area(Ki)=integral_{Pi} li yields exactly theta*integral_{P1\P2}l1+(1-theta)*integral_{P2\P1}l2. With theta strictly in (0,1), full-dimensional planar bodies have strictly positive fiber lengths in the interior of projection intervals. Distinct compact projection intervals have a positive-length interval in at least one difference, so deficit>0; equal intervals make it zero. Boundary theta=0/1 is correctly excluded. Exact independent checks give (overlap, output, weighted, deficit)=(2,4,6,2) for the nested rectangles and (3/2,5,20/3,5/3) for overlapping unequal projections. Both have origin interior. Finite checks corroborate, and the general proof is the integral argument, not extrapolation.

## originality

PASS

Qualified best-of-knowledge originality as an explicit correction and strict projection-deficit/equality observation for the unrestricted published Hoehner–Xing statement, not originality of the Fubini identity itself. The publisher full-text theorem and shadow property were inspected directly, and independent arithmetic confirms the contradiction; three Resultary semantic comparisons and targeted searches identified no indexed prior correction. Original McMullen 1999 full text and possible errata were not inspected; those are material residual priority risks but do not by themselves prove coverage.

## value

PASS

The motivation is substantive even though the integral proof is elementary: the printed unrestricted p=1 fiber Brunn–Minkowski lower bound is a prominent theorem invoked to motivate broader p inequalities. A two-rectangle counterexample shows a real hypothesis failure, not a numerical rounding anomaly; the full planar formula quantifies the failure and characterizes exactly when the weighted-area identity has equality. This correction can prevent false applications and clarifies the necessary common-projection boundary. It does not purport to refute McMullen under unknown original hypotheses or establish p>1 claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
