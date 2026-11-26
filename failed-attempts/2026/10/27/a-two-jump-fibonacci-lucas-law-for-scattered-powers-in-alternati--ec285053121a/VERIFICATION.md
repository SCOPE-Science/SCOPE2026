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

Match each letter at its earliest possible position. The first letter uses pair 1, and the next uses the same pair exactly for 01. Thus q copies of a nonempty root cost 1+q d+(q−1)e pairs, with d the internal weak-descent count and e its closing weak-descent indicator. Writing x=z^q and h=z^(q−1), the trace with internal weights T=(x,1;x,x) and closing weights E=(h,1;h,h) is tr((I−yT)^−1 E)=[2h+y(x+h−2xh)]/[1−2xy+y²(x²−x)]. Multiplication by zy counts first appearances, and division by 1−z counts all admissible hosts. At y=1, the two numerator parts over 1−3x+x² give the even Lucas and Fibonacci sequences starting at m=1; cumulative sums give F_(2m+3)−2 at k=qm and 2F_(2m+2)−2 at k=qm+r, r≥1. The m=0 values are zero and singleton roots first enter at k=q. Distinct roots give distinct powers, so embeddings are not overcounted.

## originality

FAIL

A distinct indexed record gives the entire binary square first-appearance spectrum, including length, and the arbitrary-target greedy period cost. For a given root let t be its exact square threshold. Then t=2d+1+e; t is even iff e=1, and the q-power threshold is exactly q floor(t/2)+(t mod 2). Hence all claimed q≥2 spectra are determined by reindexing the square spectrum; the Lucas/Fibonacci labels are coefficient identifications in that same rational function. This is demonstrable equivalent coverage in the inspected corpus, not a determination of who established it first or an assertion that a later-dated catalogue entry was publicly available before the frozen record.

## value

FAIL

The exact root spectrum is a natural invariant, but no distinct scientific gain over the verified square-spectrum comparison survives in the frozen theorem: its extra exponent parameter relabels the same first-appearance events, and the two jumps and Fibonacci–Lucas forms follow by splitting the existing binary rational function. A presentation of the reindexing can be useful exposition, but it does not establish a nonmechanical new counting result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
