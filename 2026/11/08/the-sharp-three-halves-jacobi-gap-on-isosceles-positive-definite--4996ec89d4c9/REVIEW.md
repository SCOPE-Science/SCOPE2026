# Scientific review: a sharp Jacobi preconditioning approximation gap

## Correctness — PASS

The theorem is limited to real unit-diagonal positive-definite matrices with two equal positive correlations. The averaging reduction from all diagonal scalings to the symmetric one-parameter scaling is valid in the Loewner order, and the resulting eigenvalue formulas yield the true global optimal condition number. The parameter domain splits at the two explicit crossings; three analytic positivity certificates prove the strict \(3/2\) upper bound. The near-singular family proves the constant is sharp. The symbolic checker reproduces the polynomial identities and 6,829 checks. The random checks are auxiliary and are not mistaken for a proof.

## Originality — PASS with identified precedence risks

Classical equal-modulus conditions and the complete pointwise \(3\times3\) optimal diagonal-scaling problem are already solved, especially in Kolotilina (2006); no novelty is claimed for either. The specifically assessed statement is the **uniform sharp loss factor** of unmodified Jacobi scaling over the entire two-parameter positive-correlation isosceles family, including strictness and an asymptotic extremizing family. The inspected classical full text, the relevant parts of Kolotilina's author-hosted full text, and the 2020/2022 papers did not state that factor or the corresponding global optimization over all parameter pairs. Strong residual risk remains from specialist approximation-bound literature or uninspected sections of the earlier complete pointwise classifications. This remains a same-authority mathematical literature assessment, not an independent precedence certification.

## Value — PASS

Dimension-dependent approximation guarantees for simple diagonal preconditioning are a central numerical-linear-algebra concern. The sharp \(3/2\) factor improves substantially on the classical general \(n\)-factor guarantee for a natural matrix family and is attained in the limit near a concrete ill-conditioned boundary. This is an exact performance benchmark rather than a trivial renaming of the known pointwise scaling solution. It makes no runtime or higher-dimensional claim.

## Closest literature and limitations

- Kolotilina (2006), *Solution of the Problem of Optimal Diagonal Scaling for Quasireal Hermitian Positive-Definite 3×3 Matrices* (DOI:10.1007/s10958-005-0488-1), completely settles each individual \(3\times3\) scaling problem and Jacobi-optimality conditions. The new claim does not compete with that result.
- Golub and Varah (1974), *On a Characterization of the Best \(\ell_2\)-Scaling of a Matrix*, characterize spectral optimizer geometry, not a sharp two-parameter family approximation ratio.
- Jambulapati et al. (2020), arXiv:2008.01722, and Qu et al. (2022), arXiv:2209.00809, develop diagonal preconditioning approximation and algorithms without the particular sharp family-wise constant in their inspected results.

The proof applies only to the stated positive-correlation isosceles family. Mathematical novelty could be altered by specialist precedent. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
