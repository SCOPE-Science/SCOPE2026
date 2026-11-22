# Review of the first-excited wavelet observation theorem

## Correctness

**PASS.** The source wavelet normalization and Jacobi reproducing kernel are explicitly identified; the hyperbolic Jacobian, total wavelet energy, cumulative mass, two-lobe geometry and global bathtub comparison are derived in `RESULT.md`. The mask maximizer is unique even among nonradial fractional masks because threshold level circles have zero measure. The annular birth coefficients, distinct one-sided curvatures and parameter asymptotics follow from nondegenerate Taylor expansions and limiting root equations. Numerical checks (104 finite assertions) corroborate independently evaluated quadratures and boundary expansions but are not used as a substitute for the proof.

## Originality

**PASS, best-knowledge, with residual historical risk.** The exact first-excited wavelet kernel and the superlevel variational principle are previously known mathematical ingredients, **not** original contributions. The inspected primary paper [1] gives the Jacobi response but does not formulate the complete finite-area topological transition or its critical-area and non-\(C^2\) coefficients. The sharp Faber--Krahn theorem [2] treats an analytic (zeroth-order) wavelet and optimizes over both signals and sets; it does not settle the fixed first-excited response. The hyperbolic density and coherent-state literature [3,4] addresses sampling and operator geometry rather than the present area-budget frontier. The finite literature comparison is not a proof of priority; generic rearrangement principles might make this result accessible from published ingredients and specialized earlier accounts may exist.

## Mathematical value

**PASS.** The first Laguerre wavelet is the minimal higher-order case with a nodal pseudohyperbolic circle, so it is the natural first test of whether contiguous sensing remains optimal. The theorem answers that natural fixed-signal observation problem for every positive order parameter and every finite hyperbolic area, with **unique optimal shape, exact captured fraction, one precise topology transition, one-sided energy curvature, and an explicit nucleation rate**. This distinguishes the fixed excited wavelet from the analytic disk case; it is not a claim about the harder unrestricted higher-order Faber--Krahn problem. The complete sharp constants are useful for choosing observation masks and testing general concentration bounds.

## Prior work and limits

The closest paper is Abreu--Speckbacher, *Donoho--Logan large sieve principles for the wavelet transform*, arXiv:2210.13056 (2022), especially its equations (20), (24)--(25). Ramos--Tilli, *A Faber--Krahn inequality for wavelet transforms*, arXiv:2205.07998, covers analytic windows with a different quantification. The result is for one fixed signal/window and not all inputs. Independent checking and a definitive historical-priority study have not been performed.

Self-review: passed. Independent audit: not yet performed.
