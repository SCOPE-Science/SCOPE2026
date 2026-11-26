# Independent mathematical audit

## correctness

PASS

Cai et al., Proposition 9, and its Type-A definition supply the exact distinct-read criterion; distance one has only one read in common. The alternating disagreement interval is uniquely the span of the mismatches, and even length is equivalent to weight preservation. Cutting where consecutive letters are equal gives disjoint maximal alternating blocks; each block contributes precisely its number of opposite-symbol endpoint pairs. The matrix entries give the correct length, Hamming weight and product of zero/one counts for the two endpoints, and equal touching symbols identify exactly the permitted joins. Its zero constant term ensures the formal inverse, with the empty word accounted for separately. Counting placements and outside bits gives both edge formulas without double-counting, and no edges skipping a weight layer. With block minority/majority counts a_i,b_i, the degree is at most both rs and ∑a_i(a_i+1)≤r(r+1); alternating all minority bits in one block and padding by majority bits attains the bound, also when r=0 or s=r. Handshaking and the binomial ratio's supported factors (k−j)(n−k−j)/[(n−2j)(n−2j−1)]≤1/2 give the claimed limit by dominated convergence. Direct enumeration of distinct deletion-output sets, compared with a separately expanded transfer series, confirmed joint histograms, both edge strata and layer maxima through n=8, including constant words and n=1. This PASS covers the mathematical Finding; there is an inaccurate descriptive clause about prior spectra in line 73, addressed under originality.

## originality

PASS

Credit the joint weight and even-interval degree enumeration, exact edge stratification and layer-specific maximum and mean, not adjacency or the unrestricted degree-spectrum method. RESULT.md line 73 incorrectly calls the prior full-graph spectrum the marginal ∑_k P_{n,k,d}. That marginal instead counts within-layer degrees across all words. For n=3, 010 has full degree 3 and within-layer degree 2, and the same-layer maximum anywhere is 2, so the histograms differ. This error in the comparison does not alter the Finding or its proof; it is the distinction between the observables that establishes the gap.

## value

PASS

Fixed composition is a natural source constraint for deletion-reconstruction problems. The layer graph is the relevant local ambiguity object for such codes, so the full histogram, sharp maximum versus typical-scale mean, and distinction between preserved-weight and cross-weight edges give usable quantitative information not provided by the unconditioned graph. These results solve an exact motivated enumeration problem without claiming an optimal code size or downstream coding theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
