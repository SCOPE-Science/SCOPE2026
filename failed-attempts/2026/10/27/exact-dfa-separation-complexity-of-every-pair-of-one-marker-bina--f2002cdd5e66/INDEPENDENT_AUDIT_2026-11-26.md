# Independent mathematical audit

## correctness

PASS

Let f and g be the zero and one maps and r=n−1−j. The final states are f^(r+d)g(f^i(q)) and f^r g(f^(i+d)(q)). A zero-cycle of length p(d) with marker reset separates; a chain through the earlier marker position with two fixed terminals uses i+3 states; a suffix-counting saturated chain after a reset uses r+2. Conversely, a k below all three terms has L_k|d, i≥k−2 and r≥k−1. If the start's zero-orbit has entered any cycle after i steps, both marker positions coincide as states, and f^r=f^(r+d) everywhere. Otherwise its transient has exactly k−1 states, consuming the whole state space except for a single fixed point. Then both final zero maps are constant. This also excludes a one-state separator. For fixed d, balancing the prefix and suffix budgets yields floor((n−d+4)/2), including the endpoint n−d=1. To require at least k≥3 states the smallest eligible gap is L_(k−1), with n−d≥2k−4; the listed thresholds follow. Inverting the increasing thresholds using log L_m∼m proves the natural-log asymptotic. The frozen checker and verification notes were inspected, not executed. Their recorded exhaustive small-budget checks are finite only; the argument handles all n.

## originality

FAIL

The exact statement is mechanically implied by already published identities and necessary conditions for the full transformation semigroup. Most decisively, Electronic Journal of Combinatorics 24(3) (2017), #P3.35, Proposition 4 gives the same sharp maximal-transient identity and proof in a nonuniform-length pair. Composing it with the explicit unary identity and applying Fact 3 recovers the entire equal-length one-marker classification, not just the logarithmic order or padded examples.

## value

FAIL

The minimum state count is a natural and useful invariant. But every term, including the one-state gain at the sharp prefix boundary, follows by elementary composition of explicit older identities and boundary tests. The optimized length thresholds and asymptotic then follow by balancing the same two inequalities. There is no remaining independent structural contribution in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
