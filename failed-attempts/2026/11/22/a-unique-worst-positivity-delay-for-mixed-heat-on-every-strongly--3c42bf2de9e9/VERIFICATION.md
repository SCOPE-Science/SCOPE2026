---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For the finite unweighted connected noncomplete strongly regular graph, P_0=J/N and aP_a+bP_b=L determine the off-diagonal projector entries. Diagonals are positive by orthogonal projection; edge entries are positive for t>0 since b<=N. For the nonedge, set A=a+eta a^2 and B=b+eta b^2. The sign is the negative of the sign of F=b exp(-At)-a exp(-Bt)-(b-a). Its derivative at zero is ab eta(b-a)>0; the derivative has a single positive zero because the rates differ and aB>bA. Then F decreases to a negative limit, giving exactly one positive, transverse recovery and separately t=0. The root tends to zero as eta grows by T<log[b/(b-a)]/A; as eta decreases to zero, F tends to the ordinarily negative heat expression at any fixed t>0, bounding T below that test time. At an interior maximum F_eta=0, which along with F=0 gives exp(-AT)=b/(a+b) and exp(-BT)=a/(a+b). B/A grows strictly, so the positive stationary point is unique. Solving AT=U, BT=V verifies both closed formulas and their positive denominators. Read the frozen proof, notes, requirements and check_srg_heat.py without executing the uploaded script. An independent 55-digit check solved F=0 and F_eta=0 directly for the Petersen eigenvalues 2 and 5, obtaining eta*=0.2420535986512469 and T*=0.1133584680516284. Neither the numerical check nor the theorem covers general weighted graphs or higher spectra.

## originality

FAIL

Material formula-level coverage, not a priority inference: a distinct same-date result on the identical strongly regular graph class implies the complete mixed positivity classification by exact time rescaling of its fractional heat. A second distinct same-date result already proves the identical dimensionless mixed recovery optimization for arbitrary real 0<p<1 in its proof. Substituting p=1-a/b supplies the optimizer even for primitive graphs; it does not require transferring a statement confined to realizable multipartite graph parameters. The two comparisons jointly leave no distinct horizon or optimizer theorem in the frozen claim. Within-day order is unestablished; this is not a finding of copying or historical precedence.

## value

FAIL

The sharp recovery horizon is a motivated invariant, and the closed dimensional formulas are useful as reference. As a distinct finding, however, the primitive-class horizon is a direct spectral time rescaling of the already stated strongly regular theorem, and the closed optimum is the same normalized scalar maximum already proved in the multipartite comparison, followed by a two-equation change of variables. No additional graph-dependent comparison, behavior or non-mechanical invariant survives. Rewording the closed formula or supplying more computations would not fix this.

The dated certificate retains the supplied scientific assessment, sources and limitations.
