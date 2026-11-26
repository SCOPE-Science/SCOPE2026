# Independent mathematical audit

## correctness

PASS

For an unselected rim vertex its signature is its set of selected cyclic neighbors. For n≥7, a repeated nonempty signature can only be a singleton at the two neighbors of the same landmark, colliding exactly when both adjoining gaps have length at least two. Empty signatures lie at internal gap vertices: there is at most one gap of length at least three and its length is at most four. Ordinary resolution additionally excludes a four-gap. Without it there must be at least three rim landmarks for n≥7, so the hub is distinguishable even when not selected. For indexed cyclic gap lists the orbit-safe argument is that each list has n choices of starting vertex and each labelled subset of size k has k marked lifts. RESULT.md:69's n/k wording is this aggregate quotient, not a literal count per individual list. The transfer trace gives −log D and the one-exception term z²AC/D; the optional hub gives 1+z. The rim length bound n≤floor(5k/2)+2 and positivity of the coefficient at floor(2n/5) establish the minimum. Explicit coefficient extraction gives b_n/n in residue order: 1/s+s+(s+3) binom(s,2)+binom(s+1,4); 1+s+binom(s,2); 1; s+s(s+1)+binom(s+1,3); s. These simplify to the claimed polynomials, including boundary values. The denominator has a unique simple minimum-modulus root by positivity and its consecutive x and x² terms. After the n multiplier the logarithmic term is O(ρ^(−n)), whereas the exceptional term is Θ(nρ^(−n)); the limit is the ratio of pole numerators, 1+ρ. Independently testing all wheel subsets by distance-mask coverage with both hub choices for n=7,…,14 matched both full polynomials (python /workspace/reproductions/wheel.py). This is bounded corroboration; the proof covers all n≥7.

## originality

PASS

The gap feasibility, minimum nonlocal dimension, and the complete ordinary wheel enumeration are prior coverage. The distinct mathematical content is the nonlocal all-size polynomial and five nonlocal basis formulas, the exact difference, and the limiting ordinary/nonlocal separation. No strengthened prior statement implying those enumerative claims was found in the comparisons below.

## value

PASS

Counting all feasible landmark sets and all minimum sets answers two distinct natural questions left by the dimension. Residue-dependent growth and a positive limiting fraction of sets that fail ordinary resolution quantify the difference between standard graph-distance requirements. These conclusions go beyond minimum cardinalities and concern every labelled wheel in scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
