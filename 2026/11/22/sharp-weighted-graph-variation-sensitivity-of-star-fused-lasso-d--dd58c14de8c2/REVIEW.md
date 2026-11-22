# Scientific review — sharp weighted graph-variation sensitivity of star fused-lasso denoising

## Correctness — PASS

The objective is strictly convex for every strictly positive fidelity mass. Each fusion pattern yields the explicitly derived affine Jacobian, whose edge-difference matrix has columns of weighted \(\ell_1\) norm \(1\) for unfused inputs and \((m_i/M_S)(\sum_{j\notin S}w_j)/w_i\) for fused inputs. The singleton-fusion inequality controls every larger fused set. A finite piecewise-affine decomposition proves the global two-input upper bound. Strictly complementary KKT constructions realize every fusion region and actual finite input pairs attain every candidate column factor. Exact rational enumerations and numerical scalar-root denoising checks independently test these mechanisms. The proof, not the finite tests, covers all dimensions and positive real parameters.

## Originality — PASS, qualified

The four-page ICASSP 2011 graph-TV paper by Couprie et al. details proximal algorithms but not the data-pair modulus. Vaiter et al. (arXiv:1404.5557, initial 2014-04-22, Section 4.2) supply a general local sensitivity/Jacobian theorem for partly smooth penalties, including analysis regularizers; their global weighted graph-TV Lipschitz modulus and star-specific maximal face computation are not stated. Madrid Padilla et al. (arXiv:1608.03384, initial 2016-08-11, Introduction and Sections 2–3.2) study graph fused-lasso statistical rates and tree/path TV embeddings, not sharp two-input variation sensitivity. A path-specific convex edge-proximal contraction criterion does not determine what happens at a branching hub; available nonlinear graph-heat results address different (often one-input and/or heat) operators. Semantic searches under graph TV resolvent, fused lasso, weighted star, prox sensitivity, and active-face equivalents found no identical or dominating sharp formula. This is evidence supporting originality, not a proof of historical priority; unpublished or unindexed formulations remain a residual risk.

## Mathematical value — PASS

This exact natural perturbation invariant quantifies the distinction between single-input graph-TV reduction and stability of two denoised signals, and identifies a sharp branching obstruction: four leaves force expansion with equal observation masses under *every* positive measurement-edge reweighting. It also gives the exact hub-mass stabilizing threshold, finite attaining witnesses, and a penalty-strength independence that is lost discontinuously at zero regularization. These are structural stability criteria for a widely studied nonlinear regularization map, rather than isolated table entries or numerical constants.

## Scope and risks

The calculation assumes a finite star, positive fidelity masses and positive anisotropic penalty coefficients, fixed weights across compared inputs, and a weighted quadratic loss. It does not prove a similar formula on arbitrary trees or with zero coefficients or other fidelities. A broader literature or independent expert check could locate historical equivalent statements; this assessment certifies neither priority nor independent validation.

Self-review: passed. Independent audit: not yet performed.
