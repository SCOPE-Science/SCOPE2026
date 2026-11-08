# Review of one-spin stability on antiferromagnetic wheels

## Correctness

**PASS.** A single-spin flip changes the energy by exactly \(2J\sigma_v(a-\sum_{u\sim v}\sigma_u)\), which yields necessary and sufficient local inequalities. Fixing hub orientation reduces allowed rim configurations to cyclic maximal independent sets, bounded-run words, or independent sets with a hub-magnetization cutoff. Their counts give all field rows, including the marginal equalities at \(a=1,2,3,n\). The critical-field upper bound uses the four-state no-triple-repeat automaton; its spectral radius is the golden ratio, and the Lucas lower bound matches it. The attached `checker.py` independently confirmed 90 finite spin enumeration comparisons and 105 cyclic-run coefficient comparisons for rim sizes 5 through 14. The proof, not enumeration, supplies all-size validity.

## Originality

**PASS, subject to historical priority risk.** The low-field Perrin count of cyclic maximal independent sets is already known, and is expressly *not* claimed new. Bisdorff–Marichal (arXiv:math/0701647), §3, gives those exact forbidden-word constraints and the Perrin recurrence. Waclaw–Burda (arXiv:0801.1224) develop a general disordered-coupling local-minimum framework, not the uniform antiferromagnetic wheel with field-dependent hub stability. De Smedt–Godrèche–Luck (arXiv:cond-mat/0202465) analyze constrained one-dimensional spin dynamics, and Baek–Ha–Jeong (arXiv:1112.5927) study random-network dynamical final states. A prior wheel study concerning three-state Potts *ground states* does not imply this two-state *local-minimum count*. The original statement is the **combined exact wheel field diagram and critical entropy spike/drop**, not its known cyclic-sequence ingredient. Search and full-text inspection did not identify direct coverage. This is not a claim of exhaustive priority certification.

## Mathematical value

**PASS.** One-spin minima are an established energy-landscape observable and can be dynamically trapping at nondegenerate fields. The exact all-size finite-wheel calculation identifies a nonmonotone, field-induced change in state-space complexity: positive Perrin entropy, higher golden-ratio entropy precisely at the marginal field, then zero entropy, together with parity-dependent polynomial counts and hub-polarity reversal. The coupling between the high-degree hub and a locally frustrated cycle supplies the structural mechanism, which cannot be read off from the known Perrin count alone.

## Scope and independent status

At marginal fields, weak minima need not be absorbing for zero-temperature dynamics that allows neutral-energy flips. No claim is made about dynamics, equilibrium Gibbs measures, attraction-basin weights, or finite-temperature barriers. The source comparison is limited to the checked literature and published record searches.

Self-review: passed. Independent audit: not yet performed.
