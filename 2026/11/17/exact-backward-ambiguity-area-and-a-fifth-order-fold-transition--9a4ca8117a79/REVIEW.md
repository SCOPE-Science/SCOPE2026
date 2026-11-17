# Self-review: exact backward-ambiguity area in a plankton map

## Correctness

PASS. For every \(0<u<1\), the biological predecessor interval is \([1-\sqrt{1-u},1]\), and the exact second-output fiber \(h_u\) has a strictly negative second derivative with inward-pointing first derivatives at both endpoints. Hence at most two antecedents occur, with exactly two for \(v_0(u)<v<v_*(u)\). The critical curve \(y_c(t)=2(1-t)(A+\gamma t)/A\) has an explicitly parameterized admissible arc; integrating its target-space height over the prey target reproduces the piecewise rational area formula and its fifth-order contact. The symbolic checker `check.py` verifies the identities, the derivative jump, the exact target fraction, and two algebraic sources of one image. The infinite statements follow from concavity and one-variable integration, not numerical sampling.

## Originality

PASS within the inspected literature. The full accessible original paper, Shoyimardonov (arXiv:2505.09968v1), establishes the map and forward invariant-domain, convergence, and fixed-point bifurcation results, but does not address area or exact inverse fibers. Vidiella, Lázaro, Alsedà and Sardanyés (DOI:10.5772/intechopen.89572) do describe two-preimage regions for a *different* nonlinear predator–prey map: its predator population vanishes after one step on the entire prey-free edge, whereas the present predator population there evolves by \(y\mapsto Ay\), \(A>0\). General noninvertible planar-map fold work by England, Krauskopf and Osinga (DOI:10.1142/S0218127405012466) supplies background but no identified implication for the formulas here. Searches for equivalent inverse-image counts, stronger parameter classifications, exact image-area tables, and implications in published mathematical research records found no covering claim. The complete 2005 article was not available for full-text comparison. Absolute historical priority cannot be certified by searches.

## Mathematical value

PASS. The exact two-cover target area measures loss of backward identifiability in a biologically motivated map, including a biologically forward-invariant subregime. The fold's attachment to a different source boundary creates a mathematically sharp \(C^4\)-but-not-\(C^5\) area transition, and its critical multiple-preimage fraction is exactly \(2/17\). Neither quantity is implied by equilibrium stability alone. The result is a complete natural one-step classification for this model, not an arbitrary numerical slice.

## Limits

Only strictly positive prey targets and one-step antecedents in the specified triangle are classified; this does not count unconstrained real predecessors, multistep trees, or source-space probabilities. Biological forward convergence statements concern strict-interior initial conditions. The status is not independent validation.

Self-review: passed. Independent audit: not yet performed.
