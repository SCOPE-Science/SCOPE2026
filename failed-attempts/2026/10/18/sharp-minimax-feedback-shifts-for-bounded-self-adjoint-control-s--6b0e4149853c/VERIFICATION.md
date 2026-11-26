---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The quadratic change of variables gives the indicated positive definite Hessian (there is a harmless typesetting slip at the control quadratic term of the proof). Every mode has scalar curvature f_delta(a)=(1+alpha a²)/(a+delta)². Its derivative has sign alpha delta a−1, so the extreme modes can be realized by the two spectral endpoints and the clipped interior minimum, in a three-dimensional diagonal witness. With theta=arctan(sqrt(alpha)a) and phi=arctan(sqrt(alpha)delta), the condition number of the robust envelope is the ratio of max to min of sin² on a translated interval of length Delta. Moving an interval on one side of pi/2 toward the peak strictly lowers that ratio by strict cotangent monotonicity; on a straddling interval the smaller endpoint sine strictly increases toward the unique centered placement and then decreases. The centered placement is feasible for every specified interval including mu=0. This proves the unique optimum, its sec² value, and that the interior witness mode lies strictly between the endpoints. Endpoint modes alone have condition number one. The mu=0 and unit-parameter special cases follow by the half-angle identity and direct evaluation of the matched shift. The frozen finite checks were inspected, not rerun, and are not needed for these universal statements.

## originality

FAIL

A distinct indexed record, 4e27f751ca0b, establishes the same optimizer for every fixed matrix with its actual extremal eigenvalues, the same sharp envelope, and exactly the same equality witnesses. It mathematically covers the frozen robust theorem, as the direct-sum reduction below shows. This is a finding of demonstrated coverage in the inspected corpus, not a determination of historical priority or of which record derives from the other. The catalogue paths bear different dates, with the covering record labelled later; no provenance inference is made from those labels.

## value

FAIL

The exact design rule and sharp witness are useful mathematical information, but the proposed robust formulation adds no independently useful unknown exact fact once the indexed fixed-matrix theorem and its sharpness are available. The uniform bound and unique gain follow by endpoint augmentation plus that same witness; the benchmark examples are evaluations of the covered law, not new boundaries. No surviving distinct valuable remainder was identified to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
