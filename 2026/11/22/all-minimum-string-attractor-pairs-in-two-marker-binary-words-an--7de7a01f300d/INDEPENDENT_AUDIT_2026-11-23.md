# Independent mathematical audit

## correctness

PASS

The headline means minimum cardinality two, not a collection of two attractors; the formulas and quantified pair description make the intended claim clear. Any two-position attractor must select exactly one marker and one zero, and 0^M forces the zero into a longest run. Any zero in such a run suffices for every pure-zero length, and either marker suffices for every factor containing both markers. With the first marker selected, uncovered one-marker factors are exactly the second occurrence rectangle [0,b]×[0,c] minus [0,a]×[0,b]. The left excess exists iff b>a and is governed by the unique occurrence of 0^(a+1)1; the right excess exists iff c>b and is governed by the unique occurrence of 10^(b+1). All larger excess intervals contain the corresponding diagnostic interval. Both excesses make the intersection consist of the forbidden marker; otherwise intersect the proper interval(s) with the union of longest runs. This gives exactly the printed cases and integer lengths, including a=c>b and b=a=c; reversal gives the second family without overlap. If b is largest, the first-marker family is nonempty. If an outer gap is largest, say a, the first-marker family works when c≤b, and the reversed family works when c>b (since a≥c). Thus minimum size is always attained. Equality in the upper bound 2(a+b+c) already forces every zero to be in a longest run, so all three lengths agree, which conversely suffices. For the mean, off ties the discrete cases are a+c+2, max(a,c), and b+1 as b moves from largest to intermediate to smallest. Positive compositions yield a uniform simplex Riemann sum; tie planes carry O(n) lattice triples out of Θ(n²), and K/n is uniformly bounded. Uniform-simplex inclusion-exclusion gives Pr(max>u)=Σ_{j=1}^3(−1)^(j+1) binom(3,j)(1−ju)_+² and hence E[max]=11/18; E[min]=1/9 from the surviving simplex above u in each coordinate. Symmetry of the ranks of the middle gap gives (1−11/18+11/18+1/9)/3=10/27 and verifies the distributional formula. Read VERIFICATION.md, verify_pairs.py, verify_intervals.py and both saved outputs without executing them. The supplied full-search count compares 1000 triples; the 512-case interval check tests sufficiency of each proposed pair by literal coverage. Neither is the unbounded proof.

## originality

PASS

The symmetric-slice cardinality two and some explicit pairs are already present in the same-day symmetric five-run record. The supported distinct contribution is the complete minimum pair family for arbitrary positive outer and middle gaps, its resonance and limiting multiplicity distribution/mean. The best related classifications retrieved concern different run patterns or truncated factors; no priority is inferred from absence or same-day ordering.

## value

PASS

Two isolated markers are a natural next regime after single-block binary words, and an optimum value of two alone does not say where either position may be placed. The exact occurrence obstructions, equal-gap resonance, and nondegenerate limiting law explain both the finite ties and the linear typical scale. The closed count is useful for this standard attractor invariant rather than just a finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
