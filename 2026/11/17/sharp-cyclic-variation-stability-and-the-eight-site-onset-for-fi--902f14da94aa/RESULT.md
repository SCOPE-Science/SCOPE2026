# Sharp cyclic variation stability and the eight-site onset for five-point trimmed means

## Finding

For an integer \(n\ge5\) and \(x\in\mathbb R^n\), with indices read modulo \(n\), let \(x_{i,[1]}\le\cdots\le x_{i,[5]}\) be the five order statistics of \(x_{i-2},x_{i-1},x_i,x_{i+1},x_{i+2}\). Define the symmetric five-point one-on-each-side trimmed mean
\[
(T_nx)_i=\frac{x_{i,[2]}+x_{i,[3]}+x_{i,[4]}}{3},
\qquad V_n(h)=\sum_{i\in\mathbb Z/n\mathbb Z}|h_{i+1}-h_i|.
\]
Its sharp two-input quotient-seminorm coefficient is
\[
\Lambda_n=\sup_{V_n(a-b)>0}\frac{V_n(T_na-T_nb)}{V_n(a-b)}=
\begin{cases}
0,&n=5,\\
1,&n=6,7,\\
4/3,&n=8,9,\\
5/3,&n\ge10.
\end{cases}
\]
In particular, this filter is nonexpansive in **perturbation variation** exactly through seven sites, first strictly expansive at eight, and attains its universal sharp bound from ten sites onward. This is a two-input statement, not a one-input variation-diminishing assertion.

## Assumptions and scope

The data are real; the five inputs of each window are distinct *positions*, because \(n\ge5\). All sites have equal weight, windows wrap cyclically, and trimming removes exactly one sample at each extreme. Ties are allowed: the sum of the three middle *values* is single-valued and continuous. Variation is a seminorm on the quotient by constants. The supremum is over all pairs with nonzero input-difference variation.

## Proof

**Rank-chamber reduction.** If every coordinate of an input \(x\) is distinct, all order-statistic selections are locally fixed. On this chamber the map \(T_n\) is linear, with a matrix \(S_x\) whose row at \(i\) has entries \(1/3\) in exactly the three positions selected by the middle order statistics and zero elsewhere. Its rows sum to one. The map is continuous and piecewise linear on finitely many polyhedral rank chambers. Every segment of input space is partitionable into finitely many segments on which a rank-choice matrix applies (limits handle ties). Therefore the global two-input seminorm coefficient is precisely the largest operator quotient-seminorm of the matrices \(S_x\). Every such linear modulus can be approached and attained as a quotient for distinct finite pairs \(x+\epsilon h,x\) by choosing \(\epsilon>0\) small enough to remain in that chamber.

**Binary-cut reduction.** For any real vector \(h\), its layer-cake representation modulo constants writes \(h\) as an integral of its superlevel-set indicators. Every \(S_x\) preserves constants. The triangle inequality and the discrete coarea identity imply
\[
\|S_x\|_{V_n}=\max_{\varnothing\ne A\subsetneq\mathbb Z/n\mathbb Z}\frac{V_n(S_x\mathbf1_A)}{V_n(\mathbf1_A)}.
\]
Complementing \(A\) does not change this quotient, so enumeration may fix the indicator at site zero to be zero.

**A uniform \(5/3\) upper bound.** Two adjacent centered five-point windows have four shared sites. Sort their four common values. The two *middle* of these common four values occur among the middle three of either five-point window, irrespective of the value of its fifth, unshared sample. Consequently their selected middle triples have at least two sites in common, and the difference between the fractions of an arbitrary binary indicator supported on the two triples is at most \(1/3\).

More explicitly, for a rank-chamber selection \(S_x\), each linear output edge difference
\[
(S_xh)_{i+1}-(S_xh)_i
\]
is a linear functional of the six sites in the union of the adjacent windows and vanishes on constants. Its expression in the five consecutive input edge differences has five coefficients of absolute value at most \(1/3\): each coefficient is the response to a unit step inserted at the corresponding input edge, and the shared-middle-two observation bounds the response. Every cyclic input edge occurs in five such six-site windows (for \(n\ge6\)). Summing the absolute values first over output edges and then over input edges therefore gives
\[
V_n(S_xh)\le\frac53V_n(h)\qquad(n\ge6).
\]
For \(n=5\), every window is the entire cycle, so all outputs coincide and \(V_5(T_5x)=0\).

**All cases below ten sites.** For \(5\le n\le9\), a finite exact enumeration runs through all \(n!\) strict coordinate rankings and all \(2^{n-1}-1\) nontrivial binary cuts after complement identification. Each row of the selection matrix is computed by sorting five integer ranks. Each numerator and denominator is an integer; comparisons use exact cross multiplication. The maximum of \(3V_n(S_x\mathbf1_A)/V_n(\mathbf1_A)\) is respectively \(0,3,3,4,4\) for \(n=5,6,7,8,9\). Thus the first three levels in the displayed formula follow without floating-point inference. Complete executable C++17 source and test counts appear in the accompanying `check_trimmed_mean.cpp`; no sampling is used in this finite classification.

**Sharpness from ten sites.** Work with zero-based indices and define the binary cut \(h\) by \(h_i=1\) for indices \(2,3,4,5,6\) and \(h_i=0\) otherwise. Its cyclic variation is exactly \(2\). For dimensions \(10\) through \(14\), choose the following five distinct-integer rank vectors \(x\):

| \(n\) | Rank vector \(x\) |
|---|---|
| \(10\) | `6,8,5,3,9,2,1,4,7,0` |
| \(11\) | `4,1,5,0,3,10,6,8,9,7,2` |
| \(12\) | `1,3,10,0,2,4,9,5,8,6,11,7` |
| \(13\) | `9,10,2,7,11,12,3,4,6,8,1,5,0` |
| \(14\) | `4,9,5,10,2,3,6,7,0,13,8,1,12,11` |

For each such vector, let \(Y_i\) count how many of the three selected middle samples have \(h=1\). Direct integer sorting of the five windows gives \(V_n(Y)=10\) in every row of the table. Hence \(V_n(S_xh)/V_n(h)=(10/3)/2=5/3\). This is a genuine two-input ratio, not merely a derivative: \(T_n(x+\tfrac14h)-T_n(x)=\tfrac1{12}Y\) because coordinate ranks cannot change under a quarter-unit perturbation.

For any \(n>14\), begin with the displayed fourteen-site configuration and insert \(n-14\) additional zero-*indicator* positions between old indices \(10\) and \(11\), assigning these new positions any distinct integer data values outside \(\{0,\ldots,13\}\). The five-one indicator arc remains unchanged. The output indicator counts at the five sensitive output edges on either side of each of its two boundaries remain as in the fourteen-site configuration: all windows intersecting the inserted positions contain only zero indicators, and the original windows close enough to the two boundaries are unchanged. Thus the original total variation \(V_n(Y)=10\) persists and sharpness holds for every \(n\ge14\). This completes the classification.

## Verification

Compile and run the included independent-of-numerical-libraries exact checker:

```
g++ -O3 -std=c++17 check_trimmed_mean.cpp -o check_trimmed_mean
./check_trimmed_mean
```

It exhausts \(1{,}800\), \(22{,}320\), \(317{,}520\), \(5{,}120{,}640\), and \(92{,}534{,}400\) rank-and-cut combinations at \(n=5,6,7,8,9\); verifies the six-element adjacent-middle overlap principle; and checks the explicit and padded witnesses through eighty sites. The finite exhaustiveness is justified by the rank-chamber and binary-cut reductions. The all-dimensional upper bound and the padding argument are mathematical proofs, not claims extrapolated from finite tests.

## Relationship to prior work

Moving trimmed means are classical members of the order-statistic-filter family, developed by Bovik, Huang and Munson in 1982–1983. Veldhuizen's accessible 1998 chapter explicitly identifies trimmed means and the piecewise rank-chamber structure. These foundations do not, by themselves, give the complete-pair cyclic variation modulus. Earlier separate results for cyclic running *medians* address a different operator (the central rank alone) and cannot imply the smaller trimmed-mean coefficients or their first-amplification threshold. The present contribution is an exact stability classification for the average of the middle three ranks, not a claim of inventing trimming or order statistics.

## Limitations

The proof does not classify general asymmetric rank weights, other window sizes, nonperiodic boundary conventions, repeated iterations, or statistical noise risk. Historical novelty remains subject to unavailable full texts of some original order-statistic-filter papers, despite targeted searches. The exact coefficients are only for the stated deterministic two-input seminorm.

## References

- A. C. Bovik, T. S. Huang, and D. C. Munson, *Nonlinear filtering using linear combinations of order statistics*, ICASSP 1982, pp. 2067–2070, DOI: 10.1109/ICASSP.1982.1171857. Conference proceedings dated May 3–5, 1982.
- A. C. Bovik, T. S. Huang, and D. C. Munson, *A Generalization of Median Filtering Using Linear Combinations of Order Statistics*, IEEE Trans. Acoust. Speech Signal Process. 31 (1983), 1342–1350, DOI: 10.1109/TASSP.1983.1164247.
- H. G. Longbotham and A. C. Bovik, *Theory of Order Statistic Filters and Their Relationship to Linear FIR Filters*, IEEE Trans. Acoust. Speech Signal Process. 37 (1989), 275–287, DOI: 10.1109/29.21690.
- T. Veldhuizen, *Order statistic filters*, in an online literature review (1998), https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/VELDHUIZEN/node13.html.
