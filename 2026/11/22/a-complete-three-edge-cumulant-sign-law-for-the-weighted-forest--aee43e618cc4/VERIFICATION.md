---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

A cycle must traverse two entire arms: an internal vertex has degree two, so a cycle entering a path cannot leave it before a terminal. Thus complete arms prior to the forest conditioning are independent with probabilities p_i, and the conditioning is that at most one completes. Write D=1+sum_i R_i. The forest partition function is product_e(1+t_e)*product_i(1-p_i)*D; differentiating its log in distinct log-activities gives the joint third cumulant. Independent derivation of the first two cases: for e in arm i, the log-activity derivative of R_i is R_i*d_e; for distinct e,f in arm i the mixed derivative is R_i*(1+p_i)*d_e*d_f. For three different arms only log D contributes, giving 2*pi_i*pi_j*pi_l*d_e*d_f*d_g. For a 2+1 split, differentiate R_j*d_g/D twice on arm i, giving pi_i*pi_j*(2*pi_i-1-p_i)*d_e*d_f*d_g. In the remaining case keep other arms fixed; (1-p_i)*D=(1+S_i)*(1-r_i). Only log(1-r_i) contributes to the three-distinct-edge mixed derivative within arm i. Each derivative of r_i at a distinct edge multiplies it by (1-b_e), so the remaining scalar derivative is (r*d/dr)^3 log(1-r)=-r*(1+r)/(1-r)^3. All denominators are strictly positive, pi_i<p_i follows from the presence of another positive-weight path, and 0<r_i<p_i<1. These facts prove strict signs and the stated positive-triple census for every finite allowed activity vector. No use of tree-only measures or repeated-edge cumulants.

## originality

PASS

Best-of-knowledge pass for the complete all-activity third connected edge-occupancy sign law and its case formulas on theta graphs. Neither the forest ensemble nor pairwise anticorrelation is new here.

## value

PASS

A distinct-edge third cumulant measures how one edge's activity changes the correlation of two others. On this natural family the direction depends only on whether three paths are occupied, even with unrestricted heterogeneous activities. This isolates a sharp third-arm onset for positive nonlinear response and counts exactly how many triples exhibit it, beyond a second-order result and beyond a single symmetric example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
