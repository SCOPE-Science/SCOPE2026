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

On friendship graph with m>=3 triangles, unit hopping, off-diagonal dephasing g>0, peripheral population-loss rate 2 and initial peripheral in another triangle, dissipative Hilbert–Schmidt quadratic form makes the Lindblad generator strictly stable: zero real dissipation would force diagonal operator zero at trap and constant over connected edges, hence zero. Permutations of nondistinguished triangles and within-pair swaps leave 18 real Hermitian orbit coordinates. Each generator entry is affine in m; evaluating orbit bases at m=3,4 exactly reconstructs all m. Independently formed the exact symbolic 18x18 matrix and integrated trace rational N/D; SymPy confirms all coefficients of N,D and of (g+1)N-m^2 D/4 and N-m g D/4 are nonnegative in g,m-2, proving T>=m^2/[4(g+1)] and T>=mg/4. Exact scaling g=z sqrt(m) gives F(z)=2(z^2+1)(z^2+2)/(z(3z^2+4)). Coercive bounds exclude optimizing z->0 or infinity; unique positive root of 3z^6+3z^4-6z^2-8 gives z*=1.226929487... and F(z*)=1.681019855... . Independent full (2m+1)^2 complex Liouvillian solves at m=3..6, g=0.5,1,3 agree with reduced mean in 12 tests. No extrapolation replaces the exact symbolic identity.

## originality

PASS

After comparing exact statements, hypotheses, data orders and implications, no inspected stronger source subsumes the surviving precise claim; known prerequisite results and any overlapping subclaims are expressly credited. This is best-of-knowledge, not a claim of proof of historical priority.

## value

PASS

Sharp transport-rate and optimal-noise asymptotics for a natural hub-of-triangles network with a peripheral trap, adding peripheral pair bonds absent from star models. Exact 18-orbit reduction and global optimizer convergence explain a nontrivial m^(3/2) bottleneck and quantitatively distinct minimizer/constants. Potentially useful as a benchmark for dephasing-assisted trapping; not an experimental or multiparticle claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
