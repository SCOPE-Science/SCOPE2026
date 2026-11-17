---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Maximum ones in any circular window can be achieved starting at a 1-run boundary, so comparing prefixes P_U(n),P_C(n) of the two candidate rotations suffices. With a>=c the difference P_C-P_U increases up to n=a+b if b>d, then decreases; its positive maximum is min(c,b-d). If b<=d it is everywhere <=0. Thus a cycle has a periodically prefix-normal rotation iff (a-c)(b-d)<=0; equality cases and unique infinite word follow because the prefix-one counts determine a word. Necklace identification (a,b,c,d)~(c,d,a,b) gives the two rational generating series z^4/[(1-z)^2(1-z²)^2] and z^6/[(1-z)^2(1-z²)^2]. Direct independent circular windows checked all 625 quadruples 1<=a,b,c,d<=5. Infinite proof is case/series argument, not the finite test.

## originality

PASS

The older cyclic-cut theorem checks only linear (nonwrapping) factors, and the separate 2026-11-02 weight-three theorem classifies exactly three ones using circular factors. They do not imply this four-run family with arbitrary two one-runs or its defect formula; standard linear prefix normal forms likewise may not be rotations. OEIS A006918 has the numeric coefficient sequence but not this run-order interpretation. Same-day self-result is not independent prior.

## value

PASS

The four-run family is the first nontrivial general run-structure boundary: a sharp signed gap obstruction and exact defect let one decide canonical rotation directly and enumerate successful/failed necklaces for all lengths. The meaningful structure is not the already-indexed integer sequence alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
