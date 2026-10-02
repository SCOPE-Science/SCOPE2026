# Independent audit — SCOPE-20260919-0ad838e02c8a

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For the stated rotationally symmetric Hopf–Langford system, an exact amplitude energy law excludes surrounding Neimark–Sacker invariant circles off \(T=0\); on \(T=0\) the positive periodic orbit lies in a conservative center foliation, contradicting the source's claimed generic torus bifurcation.

## Correctness

**PASS** — Direct polar reduction gives \(\dot r=r(z-a)\), \(\dot\theta=\beta\), and the autonomous \(r,z\) system. At the positive periodic orbit the transverse trace is \(T=(2\gamma+1)\mu-2\gamma\alpha\). With \(w=r^\gamma\), differentiation gives \(E' = T(w')^2\). Therefore a compact invariant circle surrounding the fixed point contradicts an energy maximum/minimum when \(T\ne0\). At \(T=0\), the potential has \(V(b^\gamma)=2\gamma b^2>0\), so nearby regular energy levels are closed and suspend to a continuum of invariant tori. The explicit perturbative family and exact Floquet trace reproduce the stated source-curve mismatch. A fresh independent SymPy reconstruction in this run re-derived the Jacobian trace/determinant, the energy derivative identity, and the special-family formula \(T=(3\nu-2)\varepsilon\); it did not rely on the saved verification log.

## Originality

**FAIL** — FAIL because prior published SCOPE records already contain the same source-specific correction. The 2026-09-18 amplitude-obstruction record proves the exact trace surface, no surrounding torus off it, center foliation on it, and the same first-correction mismatch; the 2026-09-19 energy-obstruction record states the same \(E'=T(w')^2\) mechanism. This record is an alternate derivation, not an original final claim.

The audit separately checked equivalent formulations, broader coverage, exact database/table overlap, and claim-versus-prior implication. Full source-inspection details and residual risks are recorded in the companion JSON.

## Scientific value

**PASS** — PASS: an exact structural obstruction correcting a claimed torus bifurcation in a current preprint is scientifically consequential, with a reusable energy identity and exact Floquet surface. Prior SCOPE coverage defeats originality.

## Disposition

**FAILED.** A validated finding requires correctness, originality, and value all to pass. The original scientific files and reproducibility artifacts are retained with the failed-attempt package.
