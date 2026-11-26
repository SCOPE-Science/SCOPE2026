---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The complete gradient Gram spectrum and both extremal switches check analytically. Frobenius unit trace-free symmetric matrices have global Dirichlet norm squared 4/(d+2). In the normalized Z,C,S sector the longitude-zero diagonal is (1,1−2/d,1+2/d), with only Z–C off diagonal, sqrt((d−2)/d); rotation then gives the longitude harmonics of orders 2 and 4. The mixed pair has zero-longitude values 1±(d−2)/(2d), and transverse trace-free quadratics contribute the mass eigenvalue. Integration gives the stated blocks and multiplicities. With t=cos L, the competing odd planar branch meets an extremal radial branch only at t²=d(d−2)/8; for d=4 the solutions are excluded endpoints, and only d=3 gives interior ties. The radial determinant divided by the mass squared is (d+2)L²/(3d)+O(L⁴), giving the reported condition-number constants. Analyticity proves strict positivity on both the lune and its complement. The independent cubature reproduced 24 full Gram spectra including both switch apertures; the all-parameter proof does not depend on sampling. Square radius has the beta law as in RESULT.md; the radial notation in one verifier comment does not affect its moments.

## originality

PASS

The strongest inspected overlaps are the same quadratic/lune problem with a scalar norm, the same quadratic-gradient problem on antipodal caps, and the general vector Slepian framework. None gives or mechanically yields the six lune branches and the dimension-three-only pair of switches. This is a bounded best-of-knowledge decision.

## value

PASS

For gradient observations of global quadratics, the extremal eigenvalues quantify sharp norm recovery, and the full spectrum specifies all observable symmetry sectors. The dimension-three-only pair of switches and the sharp narrow-lune conditioning law distinguish genuinely different observation behavior from scalar concentration and from caps. These conclusions are useful independently of a higher-degree extension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
