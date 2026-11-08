---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and scope

The source `verify.py` uses only the standard Python library. From the stated ray coordinates it constructs all ordered-pair rays and all three-index conditions
\[
(2n+2)(h_{p,q}-h_{q,p})=(2n)(h_{p,r}+h_{r,p}-h_{q,r}-h_{r,q}).
\]
It checks their ranks by exact rational elimination and verifies that all global characters and constants solve the equations. It checks the ranks and vertex counts of upper and lower facets, together with the least positive integer divisible by both \(2\) and \(2n-1\).

Run `python3 verify.py` in the same directory as the source. The completed check printed:

```text
n=3: rays=12; upper-facet relation rank=8; Picard rank=1; canonical Cartier index=10; PASS
n=4: rays=20; upper-facet relation rank=15; Picard rank=1; canonical Cartier index=14; PASS
n=5: rays=30; upper-facet relation rank=24; Picard rank=1; canonical Cartier index=18; PASS
n=6: rays=42; upper-facet relation rank=35; Picard rank=1; canonical Cartier index=22; PASS
EXACT_CHECKS_PASS
```

The computations are finite confirmations only. The all-dimensions proof uses the displayed three-index identities and the four-point argument for at least four indices; the torsion calculation uses an unrestricted integral lattice-saturation proof. The source articles were read for the original fan and the already-known abstract class group and Gorenstein index. The precise global Picard embedding is the assertion requiring independent mathematical validation.
