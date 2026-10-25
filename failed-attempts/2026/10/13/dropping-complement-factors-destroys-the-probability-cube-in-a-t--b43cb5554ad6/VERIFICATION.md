---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

From printed Eqs. (6)–(7), dx/dt=x(π_gs−[xπ_gs+(1−x)π_gw])=x(1−x)(π_gs−π_gw) identically. Eq. (19) deletes (1−x). Its government bracket at (x,y,z)=(1,0,1) is B_g−C_g+C_weak, because yz=0 and 1−z=0. The published Table 3 gives 3−5/2+3/2=2, so dx/dt=2>0 at x=1, while original replicator velocity is zero. By local continuity, any differentiable solution of the reduced drift starting there has x(t)=1+2t+o(t)>1 for small t>0. This is a rigorous counterexample to forward invariance of [0,1]^3. The x-identity and boundary substitution were separately reconstructed symbolically in SymPy; finite evaluation supports but does not replace the exact argument. The argument is deterministic only and does not infer SDE behavior from an ambiguous stochastic notation.

## originality

FAIL

The exact source-specific value 2 was not found in a prior record, but the mathematical content is an immediate instantiation of the already published 2026-10-04 Resultary correction of omitted complement factors: it gives the same x(1−x) versus xB upper-face tangency obstruction and a positive boundary drift of 3.8 in another three-population model. Benaïm–Hofbauer–Sandholm already establish general replicator simplex invariance. Here the only new calculation is plugging Su–Long Table 3 parameters into the already-known template. The result is a useful correction notice but not an original mathematical proposition after stronger/alias/implication comparison.

## value

PASS

Although the mathematical mechanism is already known, the source-specific violation is materially important to the 2026 applied paper: x is explicitly a strategy probability and the paper draws boundary stability and trajectory conclusions from Eqs. (19)–(24). A concrete admissible baseline witness proving immediate departure from the state space is relevant to anyone validating or repairing that model. This is more than a cosmetic notation slip; it falsifies the asserted probability interpretation without claiming all stochastic or interior results fail. Mathematical usefulness does not overcome the separate failure of originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
