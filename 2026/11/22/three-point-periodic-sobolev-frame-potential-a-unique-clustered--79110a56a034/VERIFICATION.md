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

The mean-zero periodic kernel K=B2/2 has derivative jump −1 at the origin and solves −K''=δ0−1, yielding the claimed evaluation Gram matrix. For gaps a+b+c=1 the potential is 1/48+2∑K(a)^2. Any boundary point contributes at least K(0)^2=1/144 to the unordered sum, above the candidate's 1/864. At an interior stationary point three distinct gaps would be all the roots of the cubic w'(t)−m, where w=K²; their sum would be 3/2, not 1. With gaps (t,t,1−2t), the stationarity difference is (3t−1)²(6t−1)/6, leaving only the equilateral and clustered candidates, with unordered sums 1/432 and 1/864. All permutations of the clustered gaps describe the same class up to rotation/reflection. At that class, the antisymmetric vector has eigenvalue 1/9 and the symmetric block is (1/72)[[4,√2],[√2,6]], hence (5±√3)/72. Multiplying the two potentials by 144 gives 10/3 and 11/3. The rational grid in VERIFY.py is corroborative; the calculation just given exhausts real candidates.

## originality

PASS

The inspected same-setting records minimize the largest Gram eigenvalue, not the sum of squared eigenvalues, and produce different nodes. General unrestricted frame-potential results do not imply the sharp value on this particular curve of evaluation vectors. No matching finite table or broader implication was found in the comparisons below; this is an evidence-bounded judgment, not a claim to historical priority.

## value

PASS

This is the first three-site case in which competing pair separations are constrained by the geometry of a circle. It gives a sharp and unique clustered design where uniform spacing fails for the standard Gram-squared criterion, with a factor-of-two reduction in unordered off-diagonal energy. The exact comparison is useful as a benchmark for site-constrained frame design and for distinguishing different design criteria, not as a general Sobolev sampling prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
