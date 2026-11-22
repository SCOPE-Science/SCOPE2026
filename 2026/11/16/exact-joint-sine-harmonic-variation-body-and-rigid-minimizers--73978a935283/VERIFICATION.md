---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Periodic integration by parts gives X=int cos(nt)dnu and Y=int cos(2nt)dnu=2int u^2 dnu for the zero-mass signed derivative nu=df. Equal Jordan masses m<=1/2 and adding common mass reduce the image to X=(a-b)/2, Y=r-s where a,b are probability first moments on [-1,1] and r in [a^2,1],s in [b^2,1]. For fixed X, min |b|=max(0,2|X|-1), so the exact upper cap is 1-b^2, and reflection gives lower cap; convexity fills every vertical section and integration gives 10/3. The homogeneous gauge has branches |Y| for |Y|>=2|X| and 4|X|^2/(4|X|-|Y|) otherwise. Equality r=1 and s=b^2 forces the asserted +/- endpoint and point masses, with lifts to 2 or 3 step-function jumps; no unique original-circle location is implied for n>1. This is an analytic all-n argument; CHECK.py contains only rational consistency points.

## originality

PASS

No inspected stronger or equivalent statement gives the full two-harmonic BV moment body, inverse gauge, and rigid Jordan pushforward classification. Classical signed-moment theory supplies the method, and Sluchak gives one-harmonic variation inequalities, not this joint sharp image. Best-of-knowledge priority only.

## value

PASS

Doubling harmonics is structurally natural through cos(2t)=2cos^2(t)-1. The independent one-mode variation constraints give a square with substantial unattainable corners; the exact sharp feasible region, inverse interpolation norm and boundary extremizers answer a motivated joint moment interpolation problem and are not a mere normalization or finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
