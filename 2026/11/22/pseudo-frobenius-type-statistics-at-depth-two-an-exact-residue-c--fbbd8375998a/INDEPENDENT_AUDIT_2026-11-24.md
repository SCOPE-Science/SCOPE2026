# Independent mathematical audit

## correctness

PASS

For m<F<2m all positive sums exceed F, so the r−1 optional positions are iid fair bits under the stated uniform law. For a gap in [m+1,F] or (r,m), addition of any positive member crosses F. For 1≤j≤r, addition of m first forces j∈B; the remaining below-conductor additions give exactly b∈B and j+b≤r ⇒ j+b∈B. This yields t=m−1−|B|+H, including r=1 and m=r+1. For a fixed j, the implications are monotonicity along step-j chains in [1,r−1]. The multiples chain is all ones, and the chain terminating at r−j is all zeros. They coincide exactly when j divides r; otherwise independent unforced paths of L vertices each allow L+1 words, giving the product with no extra bit count. For j>r/2 the fixed two bits and r−j−1 implications use disjoint coordinates, giving the exact geometric tail that sums to 1−(3/4)^(r−1−floor(r/2)). For the smaller j the path graph admits a disjoint matching of size at least (r−1−j)/3, so the sum of the probabilities is O(r(3/4)^(r/6)). Thus E H=1+O(r(3/4)^(r/6)), and Markov makes H/√r negligible; the centered reflected binomial CLT and Slutsky prove the Gaussian law. All dependence on admissible m is a deterministic translation. Separately, review_checks/semigroup.py enumerated 12,285 semigroups using maximal Apéry representatives under the semigroup-difference order. The maximum test is exact since w+s is in Apéry precisely when w−m+s fails membership. It reproduced the PF sets, residue counts and rational means for r=1,…,12 at three admissible m values per r. It also recovered irreducibles {6,7,8,9} and {6,7,9,10}, and PF sets {10,11} and {3,8,11}, with genus seven in both examples. Finite enumeration does not prove the uniform asymptotics.

## originality

PASS

The exact cardinality and binomial genus component are already known in the same window and are not distinct. The residue-chain product and quantitative control of the type-specific discrepancy, enabling the uniform type CLT, remain distinct in the inspected comparisons. Neither same-day embedding-dimension result supplies a type law.

## value

PASS

Cohen–Macaulay type is a natural invariant not recoverable from the enumerated genus and embedding dimension. The formula explicitly resolves the average defect from the binomial component at all admissible parameters and controls it sharply enough for uniform fluctuations. The separation example makes that additional information concrete and the limiting correction is not a renaming of genus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
