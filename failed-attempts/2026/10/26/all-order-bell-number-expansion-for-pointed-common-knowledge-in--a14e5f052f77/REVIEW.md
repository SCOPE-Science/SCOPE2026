# Independent mathematical audit

## correctness

PASS

The class of world 1 in the least equivalence relation containing the union is precisely its reachability component. For a fixed s-set containing 1, each partition respects its cut, the s-side restrictions must jointly connect, and the complement restrictions are arbitrary; independent marking then contributes p^s. This gives both the exact probability and the connected-count recurrence, also at n=1. For the tail, the displayed ratio of U_{s+1} to U_s is uniformly bounded below 1 for 2≤s<n/2: below n^{2/3} it is o(1), up to n/4 its limiting upper bound is 3p/4, and in the remaining range it is at most p+o(1). Above half-size one can also bound the actual tail directly by p^{n/2}, since the unmarked size probabilities sum to one. Thus for fixed positive K the first omitted bound U_{K+1} has the stated scale, and successive fixed-size terms have relative scale W(n)^r/n^{r-1}. The first-order replacement of the leading Bell ratio does not have the required two-term accuracy: at the saddle ρ=W(n), the coefficient ratio for exp(e^z−1) gives B_{n-1}/B_n=(ρ/n)(1+1/(2n)+o(1/n)). In the same-radius integrals the extra e^{iθ} factor gives the correction κ₃/(2κ₂²)−1/(2κ₂), with κ₂=n(1+ρ), κ₃=n(1+3ρ+ρ²), by Gaussian integration. The resulting relative O(1/n) change with nonzero leading constant exceeds the claimed relative remainder. Checked the frozen restricted-growth and union–find code by inspection; it compares the finite rooted histogram and p=1/2 probabilities, not the asymptotic. No uploaded code was run.

## originality

FAIL

The marked probability is not stated verbatim in the strongest matching distinct Resultary record. But that record already supplies the exact rooted component count and uniform cut estimates strong enough for the entire fixed-order remainder. Multiplying by p^s and splitting the prior bounds at a sufficiently large fixed size gives the frozen claims without a new estimate. This establishes mathematical coverage, not priority inferred from the matching date keys.

## value

FAIL

The pointed marked probability is a natural observable and keeping exact Bell ratios is appropriate. In this record, however, its exact coefficients and all fixed-order error bounds follow by elementary marking and summation from the matched record's recurrence and cut bounds. No independently useful unresolved estimate, regime, or structural result remains beyond that implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
