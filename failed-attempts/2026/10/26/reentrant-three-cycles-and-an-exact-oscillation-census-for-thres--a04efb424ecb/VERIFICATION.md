---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Saturation at two commutes with adding whole color classes, so simultaneous moves depend exactly on the 26×26 nonempty capped pairs. Following each occupied initial shore-color class lifts the quotient to the labelled dynamics: its members never split, and equality of all those colors is equivalent to equality of the entire labelled assignment. Independent bounded reproduction at /workspace/branches/a94a865e-ba3e-4d7e-951a-09501c3ce91b/independent_census.py (run with python3) exhausts the 676 pairs and 2808 admissible tags. Tag entry is at most three; the pair-level LCM distribution is 613, 15 and 48 for periods 1, 3 and 4 respectively, ruling out a mixed period 12. The simultaneous return of all tags then gives F^15=F^3. The reproduced periodic-minus-fixed signature polynomial for k=3 is E(x)^3E(y)^3+E(x)^3((1+y)^3−1)+E(y)^3((1+x)^3−1), and for k=4 it is 6E(x)^2E(y)^2, with E(z)=exp(z)−1−z. Weighting capped counts 0,1,2 by 1,z,E(z) and extracting labelled coefficients gives the claimed primitive-point counts and size cutoffs. The independent literal vertex check of ((1,2),(0,0,2,2)) enters at update three. The fixed-point formula follows by checking each occupied color's opposite successor count, and a union bound shows that both shores have all colors repeated with proportion tending to one, giving the recurrent proportion claim. The frozen verifier and recorded output were inspected, not executed; their quotient totals agree with the fresh certificate.

## originality

FAIL

The mathematical classification is substantially covered by two distinct indexed findings with the same threshold-two CCA on labelled complete bipartite graphs. b3abd8d3ada1 states the full all-size period set, sharp transient, identity, and exact reentrant three-cycle cutoffs. fd4efc95a2d1 gives the identical time-zero primitive three- and four-period counts when both shores have size at least two; the one-vertex cases are covered by the first record for period three and have no four-cycles. This is established statement-level overlap, not a conclusion about who obtained or disclosed the mathematics first. The indexed paths have later directory dates, which are not a basis for assigning priority or independent provenance.

## value

PASS

As mathematics, the sharp size-independent transient and nonmonotone disappearance and reappearance of three-cycles are meaningful structural facts for threshold dynamics, and the labelled counts quantify them exactly. This assessment of the content does not resolve the originality failure. No distinct valuable remainder of the frozen claim was established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
