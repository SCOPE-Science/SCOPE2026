---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Conservation gives a single particle current J. Writing z_i=Pr(hole at i)/w_i gives p z_(i+1)-q z_i=J/(w_i w_(i+1)). Iterating around the cycle and normalizing gives J=(p^n-q^n)/Z*, with Z*=sum_(i,j) w_i p^j q^(n-1-j)/(w_(i+j) w_(i+j+1))>0. Independent symbolic replay (python /workspace/branches/replay_trap.py) gives 8abcd Z*=P and 2(p^4-q^4)=epsilon(1+epsilon^2), and also reproduces the three-site formula. An independent generator-cofactor check agrees. Subtracting denominators at opposite biases gives even-current sign -sgn(Delta) at every nonzero interior bias; expansion gives the stated quadratic coefficient. All rates of the balanced-opposite-sums witness (1,2,4,3) are distinct, so it has no reflection. The three-site and single-particle boundaries are odd and the proof makes no general multi-particle claim. The packaged verifier was inspected, not executed.

## originality

FAIL

Two distinct published Resultary records explicitly cover the exact four-site one-vacancy result. One gives the same non-reflection witness and parity sign; the other supplies the same rational per-bond current, iff locus and quadratic coefficient, with three-site results. This is established statement-level coverage, not inferred priority or a claim about who derived it first. The primary QTM paper establishes the setting and different symmetry criteria, not this fixed-sector classification in the passages read.

## value

PASS

The mathematical result is useful in substance: it identifies a minimal nondegenerate ring with rectification, classifies an accidental all-bias cancellation not forced by spatial reflection, and shows that one quadratic coefficient diagnoses exact parity in this sector. This value does not repair the direct originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
