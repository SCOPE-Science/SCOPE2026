# Independent mathematical audit

## correctness

PASS

Recording the number of b's after each successive a gives a weakly decreasing A-tuple between B and 0, with sum C. The successive differences recover the intervening b-gaps, including leading and trailing ones, so this is a weight-preserving bijection. If the last of the first r matched a's has index j and the next matched a has index k>j, the needed intervening and final b's exist exactly when lambda_j>lambda_k>=1. Monotonicity lets one set j=r, or equivalently says there must be two distinct occupied gaps after successive a's with indices at least r. Thus for m positive rows, avoidance is automatic for m<r and otherwise holds exactly when rows r through m have a common value v, with m=r included. At m=0 the weight is 1. For 0<m<r, removing one cell per positive row leaves an m-by-(B-1) rectangle. For m>=r, removal of v cells from each positive row leaves an (r-1)-by-(B-v) rectangle, giving weight factor z^{mv}. These decompositions are bijective, including empty ranges when A=0 and vanishing Gaussian terms when B=0. At z=1 both hockey-stick sums yield the stated total. Every area C in [0,AB] is attained by full rows followed by at most one partial row and then zeros; for B=0 only C=0 occurs. Area AB-1 is uniquely a one-cell deletion from the rectangle, giving a^{A-1}ba b^{B-1}; it contains the pattern exactly under the stated composition bounds, while area AB gives a^A b^B, which avoids. Equation (3) is correct under the cited definition of Parikh-class probability, uniform conditional sampling within the class (Fazekas–Huang–Mercaş, Section 5); that convention is implicit in the wording and should not be read as a claim for arbitrary sampling laws. For instance the class (3,3,7) has aabbab and abaabb, of which only the first contains aabab. Independently used an exact weighted greedy-prefix automaton (appending a b adds the current number of a's to C) to compare all coefficients over 600 cases with 0<=A,B<=9 and 2<=r<=7, including the example and one-hole boundary. These finite checks support, not replace, the bijective proof.

## originality

PASS

The distinct supported result is the structural tail-gap constraint and evaluated full ab-pair-refined Gaussian polynomial for this four-run family. The word/partition bijection, basic count-to-uniform-probability ratio and generic greedy automata are prior or standard; the unweighted totals and one-hole boundary are useful consequences, not claimed here as independent new machinery. The closest exact same-day record uses a nonequivalent pattern. No stronger inspected theorem provides this evaluated refinement by substitution.

## value

PASS

Binary Parikh data and scattered-pattern containment are a preexisting exact conditional-counting problem. Across an entire four-run family the theorem turns avoidance into one simple constraint on tail gaps and yields coefficients for all compositions and pair counts, including nonmonotone containment at the top boundary. This gives exact test cases for generic estimates and structural insight beyond unfiltered class enumeration or one short example. No complexity result for binary-encoded parameters, extension to other pattern families, or arbitrary-distribution probability formula is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
