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

The smoothness argument locates the base locus of |4H+12F| at B={X=Y=W=0}; Z³W has a free nonzero constant coefficient and gives a nonvanishing transverse derivative there. Bertini off B and a pencil through Q give the projective smoothing; adjunction and the structure-sheaf exact sequence give K trivial and H¹(O)=H²(O)=0. Independently, the X,Y derivatives of the squarefree binary quartic force X=Y=0 at a singularity; the projective Z,W roots collide only at v=±i,±1,0,∞, with root differences of order two. Centering the two colliding roots gives λz²+μs⁴−q(x,y) as weighted initial form. Its isolated Jacobian colength is 3·3·3=27 in four variables, preserved by the higher weighted terms. Burek’s separate μ=9 for the K3 fibre omits the base variable. The exact ring computation gives (c1,c2,c3) with coefficient pairs (4,12),(6,38),(4,42) in H^j,FH^(j−1); D(c3−c2 D) gives −80H⁴−968FH³, and the intersection values (−10,1) give e(T)=−168. The second check uses six exceptional del Pezzo surfaces of Euler 10 and six Milnor fibres of Euler −26, so e(Q)=−6 and e(Y)−e(T)=6·36=216. A smoothing pencil can be chosen with nonzero perturbation at the six points, which are off B. For a general smooth member the restriction to W=0 is a squarefree constant binary quartic; the four line classes on a smooth K3 fibre have nonsingular matrix J−3I and extend to divisors, independent together with the nonzero base class. Hence the asserted lower bounds 5 and 89 hold, not an exact Hodge pair. Exact coefficient replay: independent_check_3.py. The frozen uploaded checker was inspected rather than executed; frozen audit/attestation/Lean fields record not_performed.

## originality

FAIL

Published exact-family classifications already give smooth anticanonical members in the same scroll and a stronger deformation lower bound. The Euler number is the established rank-four-scroll Chern number. Burek explicitly gives the six threefold weighted initial equations, the six exceptional surfaces, and e(Y)=48. Applying the standard Jacobian-length formula to those very equations and subtracting the two Euler numbers gives the claimed transition and its local contributions. The inspected papers do not print this exact joint statement, but they cover the global inputs and mechanically imply its numerical conclusions. Burek’s printed 9 is not a contrary calculation: it is for the K3 fibres, not the threefold.

## value

FAIL

The specific transition is well motivated, but its narrow exact invariants are mechanically determined by the already published exact scroll family and singularity data. The four-line proof does not improve the published deformation lower bound or establish an exact Hodge pair. No independent surviving quantitative or structural claim beyond those implications was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
