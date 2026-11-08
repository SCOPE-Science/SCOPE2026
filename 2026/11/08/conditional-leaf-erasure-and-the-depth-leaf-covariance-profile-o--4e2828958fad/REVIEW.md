# Self-review

## Correctness: PASS

Independently selected uniform parents remain independent under a product restriction that excludes a prescribed set of terminal labels from later parent choices. After erasing those leaves, the surviving parent variables have precisely the uniform recursive-tree law, not merely matching moments. This proves the full conditional law for every permissible finite size and conditioning set. The standard independent-Bernoulli depth generating function and the telescoping fixed-leaf probabilities yield the indexed and summed covariance formulas. A separate leaf-count moment recurrence supplies the correlation asymptotic. The included standard-library verifier recomputes 17,014 exact finite checks through size eight, including full reduced-tree distribution comparisons; the infinite assertions rest on the analytic proof.

## Originality: PASS, subject to historical priority limitations

The closest primary sources are Janson (global degree-count asymptotics), Panholzer–Prodinger (unconditional birth-label depth distribution), and Saunders (size-conditioned deletion algorithms). Their inspected passages do not imply uniformity of the *entire tree after conditioning selected earlier labels to be terminal* or the resulting entire set-indexed joint generating functions. Previously published covariance identities for total path length against one leaf indicator give only first moments of a sum, and therefore do not imply the specified full conditional distribution. Some older works could contain an implicit equivalent: the 1991 Mahmoud–Smythe paper was not available in full text. Searches are evidence of comparison, not proof of uniqueness.

## Value: PASS

The conditional deletion statement is a structural and distribution-level invariance law for natural survival events in a canonical random-tree growth process. It simultaneously determines the depth under every finite collection of terminal constraints, not one artificially selected moment; its exact covariance profile distinguishes individual birth labels and quantifies the negative dependence between depth and leaf abundance. This makes it useful for studying observed surviving tips in recursive genealogies and for mixed-moment calculations. The covariance is a derived consequence, not an inflated second theorem.

## Limits

The distinction between terminal-label conditioning and random deletion is essential, as is the uniform-parent assumption. The inaccessible older source creates a bounded historical-priority risk but no identified mathematical implication covering the claim. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
