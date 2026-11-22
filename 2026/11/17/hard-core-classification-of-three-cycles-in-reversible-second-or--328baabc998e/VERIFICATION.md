---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For n>=3 the third-iterate fixed state corresponds bijectively to three successive temporal rows. Rule54 update forces parity of each column equal to the OR of neighboring row bits. Either parity zero everywhere yields uniform-zero history, or parity one everywhere requires columns 001,010,100,111, and defect columns cannot occupy spatial sites distance two. Converse reconstructs exact R^3 fixed states. Three independent one-hot colors give polynomial H_n(w)=1+s_n(w) for odd n, 1+s_(n/2)(w)^2 for even n, s0=2,s1=1,s_m=s_(m-1)+3w*s_(m-2). This yields (H_n(1)-2)/3 primitive temporal three-orbits and entropy log((1+sqrt13)/2). Independent brute-force rings n3..8 yielded 11,50,62,101,338,962 fixed states; analytical bijection proves all n.

## originality

PASS

Best-of-knowledge comparison of actual statement/implications, including relevant primary material and related published records; residual priority limitations stated.

## value

PASS

Motivated complete period-three structural classification of canonical reversible second-order Rule54, yielding an exact weighted distribution, all-ring orbit census and entropy rather than a small-state numerical list. A precise reusable invariant beyond generic transfer-matrix computability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
