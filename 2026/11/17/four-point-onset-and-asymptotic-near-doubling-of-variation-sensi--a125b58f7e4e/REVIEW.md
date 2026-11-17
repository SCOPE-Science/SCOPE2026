# Self-review

## Correctness
PASS. Each possible strict active-curvature face of convex least-squares projection is realizable, with orthogonal linear derivative. Translation invariance reduces the adjacent-BV operator norm to single-jump probes. Exhaustive exact-rational enumeration covers all faces for sizes two through ten; finite input pairs are verified by primal feasibility and positive KKT multipliers. An explicit face with free endpoints and affine interior gives the two analytic asymptotic lower-bound formulas. No finite enumeration is claimed to prove the unrestricted large-dimension behavior.

## Originality
PASS, with historical-priority risk. The closest published convex-sequence result concerns coordinate maximum-norm sensitivity; the previously available complete-pair Gini values are also different. Meyer (2008) supplies facewise cone projection structure, Chatterjee–Guntuboyina–Sen (2013) study squared-error risk, and Mazumder and colleagues (2015) study algorithms and Lipschitz constraints on functions. None of the inspected propositions supplies these BV coefficients or the near-doubling lower bound. The technique of face enumeration itself is not claimed as new; nonindexed historic work remains a risk.

## Value
PASS. Adjacent variation quantifies perturbations in the localized jumps that shape-restricted signal fitting is intended to control. It is meaningful that Euclidean projection amplifies such differences from four samples onward and that a realizable family makes amplification arbitrarily close to two. The exactly classified sizes through ten show a real eight-to-nine-sample plateau. These conclusions are not merely restatements of known sup-norm or Gini bounds.

## Limits and provenance
The exact coefficients beyond ten and a matching asymptotic upper bound are unproved. Claims concern equal-weight equally spaced real sequences only. The proof is reproducible from `RESULT.md` and `verify_convex_bv.py`.

Self-review: passed. Independent audit: not yet performed.
