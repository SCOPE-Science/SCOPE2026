# Scientific review: cyclic one-step image counts of Rule 110

## Correctness: PASS

The proof builds the exact four-state pair-overlap graph and then its \(75\)-state reachable Boolean-relation automaton. The transfer counts each indexed cyclic output once when its relation product has a nonzero diagonal. All recurrence values for \(n=11,\ldots,85\) vanish exactly, and Cayley–Hamilton makes these \(75\) checks a proof for every later length, not an inference from a finite prefix. The initial coefficients and polynomial factorization are checked. Separate direct evolution enumeration through length \(18\) agrees. The dominant pole and coefficient are established by explicit algebra and root bounds; no unproved infinite claim rests on enumeration alone.

## Originality: PASS (with historical-priority risk)

Jen (1989) derives preimages of particular output strings; Mora–Martínez–McIntosh (2004) builds Rule 110 ancestor procedures; Juárez Martínez et al. (2007) focuses on glider phase languages. These frameworks are relevant but the inspected statements do not supply the explicit all-length rational count of *distinct indexed cyclic outputs*. A finite public Garden-of-Eden census already gives \(102\) excluded configurations at length \(8\) and \(37542\) at length \(16\), which is correctly treated as prior finite data. Nearby published work on temporal trace complexity and other elementary rules does not imply this formula. Earlier general algorithms may make the count computable, and an unidentified exact historical sequence is an acknowledged residual priority risk.

## Value: PASS

Distinct one-step outputs measure exact finite-volume loss of reachability in Rule 110, a standard universal nonlinear cellular automaton. The theorem provides every finite ring size and a sharp spatial image growth rate, complementing preimage methods and the known isolated finite censuses. It is a meaningful complete invariant, not an arbitrary small-sample table or a restatement of individual-predecessor formulae.

## Scientific limits

The result does not address multiple updates, full spatiotemporal entropy, or all cellular automata. No external independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
