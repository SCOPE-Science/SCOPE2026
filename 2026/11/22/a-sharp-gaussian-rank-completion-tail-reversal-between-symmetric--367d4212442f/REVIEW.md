# Review of the rank-completion tail comparison

## Correctness
**PASS.** The block-inverse matrices multiply exactly to the identity under the stated nonzero Gaussian nullspace coordinates. Conditioning on the independent nullspace coordinates yields the classical product-normal small-ball law and the half-normal square law. The inverse's remaining blocks have exceedance probability of order at most \(R^{-1}\); thus they cannot alter the stated dominant asymptotics. Gaussian numerator integrability and inverse-normal moments give both exact cutoffs. A standalone rational checker passes 2,258 assertions; its tests are supplementary to the analytic proof. The domain is restricted to real, fixed, corank-one, symmetric positive-semidefinite matrices.

## Originality
**PASS, subject to publication-priority risk.** The closest starting source is Sifuentes--Gimbutas--Greengard, arXiv:1401.3068v1, especially its deterministic inverse identity (17), Theorems 3--4 and stabilization section. Those give invertibility and conditioning bounds, not these asymptotic Gaussian tail prefactors or the sharp symmetric-versus-independent moment comparison. The independent-normal product density is classical (Springer--Thompson and subsequent distribution work), but is a scalar result rather than a result on randomized nullspace completion. Chen--Dongarra bounds condition numbers for full Gaussian matrices rather than low-rank completion of a fixed singular matrix. A close synthesis could exist under a different name or in unindexed literature; this was not independently resolved.

## Value
**PASS.** Almost-sure invertibility does not control rare near-singular realizations. The universal contrast between the \(R^{-1/2}\) and \((\log R)/R\) inverse-norm tails is a concrete design tradeoff: preserving symmetry and positive definiteness can worsen extreme inverse amplification. It applies to every positive range spectrum and yields usable exact moment integrability thresholds. The statement deliberately makes no claim about the relative typical condition number.

Self-review: passed. Independent audit: not yet performed.
