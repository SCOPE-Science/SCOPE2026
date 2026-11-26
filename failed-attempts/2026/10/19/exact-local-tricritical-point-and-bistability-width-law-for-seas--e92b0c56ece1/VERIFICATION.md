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

Expanding s first and then sK(s)=c(s+2ms²+(3/2)m²s³+O(s⁴)) reproduces the three coefficients of G−q. At z_c the quadratic coefficient B(m) has its only zero where (4m−1)z_c=1, with B′=b₁>0 and cubic −D_*<0. Dividing by q gives an analytic h with h_z=2/z_*>0 and h_qq=−2D_*<0. The fixed-parameter positive branch at tricriticality follows by rescaling q by √(z−z_*); the two equations h=h_q=0 give the unique nearby fold, whose q and z−z_c have leading coefficients b₁/(2D_*) and −z_*b₁²/(8D_*). Strict local concavity and h(0)<0 give exactly two small positive roots between the fold and z_c; q h_q and G′>0 give the stated iteration stability. A separate 70-digit derivative calculation on the map reproduced 1.4200496086697041779168, 1.470159219746206226674, 1.057345229126056404612, and 1.7114559380248466630345 for the lifespan, degree, square-root amplitude and width coefficient. The stated b=sK(s) is the full lifespan-biased requirement including the sampled step: K counts the other required steps, not necessarily only the future steps after the encounter.

## originality

FAIL

A distinct indexed Resultary finding explicitly supplies the same exact tricritical point and onset coefficient and a stronger global fixed-point diagram that includes the local bistability and stability conclusions. Although it does not print the width constant W_*, it gives the same analytic fold equations and all the leading Taylor data that determine W_* mechanically. The frozen and distinct catalogue paths carry different dates; this assesses existing mathematical coverage, not first discovery or chronology of derivation.

## value

PASS

Locating and resolving the narrow bistable region in the natural lifespan parameter gives a useful benchmark for numerical phase diagrams of this map, and the onset coefficient quantifies small viable fractions. These are useful mathematical conclusions of the model; that utility does not supply a new contribution over the matched coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
