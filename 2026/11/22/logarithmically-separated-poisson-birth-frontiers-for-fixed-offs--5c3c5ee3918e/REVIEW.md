# Scientific review: fixed-offspring Poisson birth frontiers

## Correctness — PASS

The stated limit is derived from the exact multivariate child-count generating function for independently chosen parents, not from simulations. A uniform marked rare-event estimate follows by factoring the probability that all marked vertices receive no children and interpreting the remaining finite polynomial coefficients as collision-free weighted draws. Factorial moments prove joint Poisson convergence on compact positive birth-age scales. An exact one-vertex bound controls points approaching the origin. The first-arrival and earliest-at-most-\(K\) corollaries then follow from zero-count probabilities and scale separation. `verify.py` reproduces the finite generating-function law by exhaustive parent-choice enumeration through eight vertices and tests the exact marginal identities; the infinite claims are proved analytically.

## Originality — PASS, with documented historical risk

Kuba–Panholzer (2006 online) obtain exact laws for a *single specified label*, and Janson (2004) and Holmgren–Janson (2014) describe the numbers of each degree over the **whole tree**. The previously published first-leaf theorem is the \(r=0\) case. These do not directly cover the independent **joint** point-process law for \(r\geq1\), the logarithmic separation of first-appearance birth labels, or the earliest-\(\leq K\) selection law. Full-text inspection was possible for Kuba–Panholzer and Holmgren–Janson. Not all older recursive-tree papers and published leaf-process material were accessible in full, so priority is subject to that limitation; a negative search is not proof of uniqueness.

## Value — PASS

The theorem resolves a natural age-ordered extreme in recursive trees: the earliest vertex of each fixed direct-child degree. The coexistence of linear global degree-class populations with sharply separated earliest-birth scales is not visible from standard global degree CLTs. The full multi-class Poisson result identifies the successive early arrivals and establishes asymptotic independence at different scales. The counterintuitive consequence that the oldest vertex among those having at most \(K\) children typically has **exactly** \(K\) children is a direct structural use.

## Closest literature and scope limits

Janson, doi:10.1002/rsa.20046; Kuba–Panholzer, doi:10.1016/j.jcta.2006.08.003; Holmgren–Janson, arXiv:1406.6883; Addario-Berry–Eslava, arXiv:1507.05981; and the previously published oldest-leaf process were compared by mathematical object, normalizations, and implications. The proof is restricted to a fixed finite family of child-degree classes. Neither growing degrees, finite-size independence, nor a quantitative Poisson approximation rate is claimed. Independent verification has not occurred.

Self-review: passed. Independent audit: not yet performed.
