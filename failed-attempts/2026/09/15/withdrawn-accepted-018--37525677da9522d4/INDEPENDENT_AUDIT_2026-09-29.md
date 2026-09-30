# Independent Audit — 2026/09/15/018

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `018f90dde5be231a68b088fb080dc34e506b092a`
- Disposition: **FAILED**

## Correctness

**PASS** — The counterexample mechanism is correct, modulo the standard harmless local isotopy used in forming a connected sum diffeomorphism. The -E8 plumbing N is spin with Poincaré-sphere boundary; adding S^2×S^2 gives b+=1 and signature -8. A representative of r×r can be chosen standard near the connect-sum ball without changing its action -id on the hyperbolic summand, so the resulting boundary map is id_P and the positive line is reversed. For φ=id, the equivariant classes forget to the ordinary CF^-(P) local-equivalence class. Since d(P)=±2 is nonzero, ordinary local equivalence is nontrivial, hence neither equivariant class can vanish. This refutes the proposed conjunction.

## Originality

**FAIL** — The construction is a routine interior stabilization: take any suitable negative-definite spin filling with nontrivial boundary Floer correction term, connect-sum S^2×S^2 in the interior, and use a diffeomorphism acting as -id on the new hyperbolic summand while fixing the boundary. The Floer step is only the forgetful map plus the classical d-invariant of the Poincaré sphere. The record itself introduces no new Floer computation or new extension obstruction.

## Scientific value

**FAIL** — The example usefully identifies that the target hypotheses are too weak to force the proposed boundary class, but it does so by an elementary stabilization that leaves the boundary dynamics trivial. This is a diagnostic counterexample rather than a research-level advance in cork or involutive Floer theory.

## Sources

- Corks, involutions, and Heegaard Floer homology (Irving Dai; Matthew Hedden; Abhishek Mallick): https://arxiv.org/abs/2002.02326 — Provides the surrounding equivariant Floer/local-equivalence obstruction framework.
- Absolutely graded Floer homologies and intersection forms for four-manifolds with boundary (Peter Ozsváth; Zoltán Szabó): https://doi.org/10.1016/S0022-4049(03)00114-X — Standard source for correction terms, including the nonzero correction term of the Poincaré homology sphere up to orientation.

## Limitations

- The local smoothing/isotopy needed to form the connected-sum diffeomorphism is standard but is not written carefully in RESULT.md; an invariant ball alone is not by itself the full gluing argument.
- Rejection is based on originality/value, not on the existence of the counterexample.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
