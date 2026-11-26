# Independent mathematical audit

## correctness

PASS

With t coins all excesses 0,…,2t over t(pk+1) are attainable, so passage to multiples of p gives the stated represented intervals J_t. They are empty up to t_p−1, nonempty thereafter, with both endpoints strictly increasing. Thus the interval before J_{t_p} has exactly kt_p missing integers and, between J_t and J_{t+1}, the number of missing integers is the positive part of k−2q−floor(3r/p), with t=pq+r. Within each quotient block this is nonincreasing, with unchanged value at wraparound because p≥3. At q=0 the j=0 residue class is excluded precisely by t≥t_p; all classes occur at q≥1. For 1≤ℓ<k the odd deficit k−ℓ picks the middle class only; the even deficit ≥2 picks the outer pair, including the valid last class at q=0 when k−ℓ=2. This gives the histogram and the unique length kt_p. Counting the two deficit parities and then weighting by ℓ gives the stated block count and genus. This covers p=3 and k=2 without appeal to the finite diagnostic; the worked example (7,8) has 24 blocks and genus 116.

## originality

FAIL

The histogram is not printed as such in the earlier sources, but it is mechanically implied by a prior exact interval decomposition and its explicit per-interval multiple count, valid on the whole frozen domain. No distinct remainder was found. This is stronger coverage evidence than the scalar genus or Frobenius formulas, which alone would not determine a run histogram.

## value

FAIL

The histogram is a natural and useful refinement of genus in principle. In this submission the exact histogram and apparent transition at p=4 follow by elementary residue counting and merging the initial projected intervals from an existing complete gap description. No independently useful exact fact beyond that mechanical extraction survives the value requirement for a narrow invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
