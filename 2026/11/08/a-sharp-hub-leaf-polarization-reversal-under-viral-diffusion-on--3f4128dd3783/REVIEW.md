# Scientific review: hub–leaf viral polarization reversal

## Correctness — PASS

The exact conditional eigenspace formula for the star Laplacian separates leaf differences (eigenvalue \(w\)) from hub–leaf contrast (eigenvalue \((m+1)w\)); substituting independent-cascade activation laws gives two expected quadratic forms whose difference factors with one affine sign-changing bracket. Positivity of the threshold and its strict upper bound are proved algebraically, including \(m=1,2\) and \(p=0,1\) boundaries. The standalone `verify.py` checks 180 exact-rational paired comparisons against independent full rational linear-system solves and cascade enumeration. The checks cannot prove the unrestricted assertion; the displayed algebra does.

## Originality — PASS, with limited priority uncertainty

The closest mechanism is Tu–Neumann (2022), arXiv:2202.03573, inspected in accessible full HTML (model, FJ equilibrium, quadratic indices, estimators, optimization and numerical sections). It supplies the general stochastic-cascade/FJ framework and an expectation-estimation method, but no claimed star-specific exact hub-versus-leaf phase transition, and no theorem sign-ordering the polarization seed choices as the transmission probability changes. A distinct deterministic FJ susceptibility-optimization question varies a fixed local anchoring parameter instead of a random cascade. Hunter–Zaman (2018) treat placement of stubborn agents, with a different intervention, and Bhalla–Lechowicz–Musco treat edge rewiring. The full texts of those secondary comparisons were not fully accessible; their titles and available abstracts establish different mechanisms, but unindexed or inaccessible priority remains a risk. Database nonhits are not proof of originality.

## Value — PASS

Expected reach and expected polarization are both natural intervention objectives in the initiating model. The theorem exhibits an exact **ranking reversal** between the two symmetry-distinct seed choices, despite the hub's universal strict advantage in expected reach for nontrivial transmission. The threshold applies to every star size and positive interaction weight, identifies a qualitative population-size boundary at three leaves, and gives a large-star threshold scale. This is a structural, interpretable phase diagram rather than a routine parameter substitution or selected numerical case.

## Limits and residual risks

The result is restricted to one seed, homogeneous independent cascade, zero baseline innate opinions, equal positive shifts, fixed weighted star, and equilibrium (not transient) FJ polarization. The leading primary paper derives general estimators which can in principle be specialized, but the exact seed-order theorem and its sharp sign boundary were not found there. Hidden equivalent results cannot be excluded from the accessible primary and database searches. No independent external audit was conducted.

Self-review: passed. Independent audit: not yet performed.
