# Review of quadratic leaf–cycle regression

## Correctness

PASS. The rooted-forest determinant gives the exact number of extensions of each labeled cycle. Deleting a fixed non-cycle leaf gives the conditional mean without approximation, including the zero- and one-nonroot boundary cases. The exact finite difference of that mean proves the strict covariance sign. The half-normal limit follows from product weights and a Gaussian majorant; the telescoping difference and moment domination yield the quadratic conditional regression and normalized covariance constant. The included standalone verifier passed 2,738 exact checks, including exhaustive connected-graph enumeration through seven vertices. Finite tests support but do not replace the infinite proof.

## Originality

PASS with historical-priority risk. Kolchin's 1999 enumeration and forest-counting framework is broader combinatorial machinery, but the inspected relevant section does not state a leaf-versus-cycle conditional regression or covariance law. Janson's 2003 cycle point-process results concern sparse random graphs near criticality, while Ben-Naim and Krapivsky's 2004 paper treats a growing random multigraph and component sizes. Neither inspected study identifies the all-size strict leaf regression and quadratic conditional-mean limit. Search did not locate a matching exact table or earlier statement, but a stronger older bivariate generating function might encode the same result implicitly; absence from search is not a proof of novelty. The classical cycle enumeration and half-normal limit are not claimed as new.

## Value

PASS. A natural geometric question about the tree attachments of a unique graph cycle receives a complete finite-size sign classification and a precise non-Gaussian second-order regression. The cancellation of the expected linear response explains why a cycle containing order \(\sqrt n\) vertices changes the expected number of leaves only by order one, even though the total leaf count is order \(n\). The explicit covariance constant provides a quantitative dependence benchmark for random connected graphs of cycle rank one, not a routine numerical increment.

## Scope and residual risks

Only simple labeled connected unicyclic graphs are covered. No variance or joint limit of the unconditioned leaf count is asserted. The analysis uses established Cayley-forest enumeration; future historical specialist review should check older joint degree/length enumeration sources. Mathematical verification here is not independently audited.

Self-review: passed. Independent audit: not yet performed.
