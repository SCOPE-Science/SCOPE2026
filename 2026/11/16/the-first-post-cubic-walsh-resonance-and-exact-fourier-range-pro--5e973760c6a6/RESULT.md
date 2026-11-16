# The first post-cubic Walsh resonance and exact Fourier range projection for length-ten Motzkin paths

## Finding

Write each classical Motzkin excursion as a length-\(n\) word in horizontal, up, and down steps. At every position use the Boolean two-coordinate encoding \(H=(0,0)\), \(U=(1,0)\), and \(D=(0,1)\). At length ten, the indicator of the resulting \(2188\)-point support in \(G=\mathbb F_2^{20}\) has exactly \(67312\) vanishing Walsh coefficients, or equivalently the associated convolution has rank

\[
\operatorname{rank}T_{10}=1048576-67312=981264.
\]

The 302-level signed multiplier distribution is completely specified by `spectrum.csv`. Exactly 48 zeros have frequency Hamming weight four, and no zero has weight below four. An explicit weight-four zero changes signs on the up steps at positions \(2,6,8\) and the down step at position \(5\). The smallest nonzero multiplier magnitude is \(2\).

Let \(R=\operatorname{ran}T_{10}\). Among **all** real or complex linear projections onto \(R\), without a translation-invariance restriction, the exact smallest endpoint norms are

\[
\Lambda_1(R)=\Lambda_\infty(R)=\frac{1630103}{32768}.
\]

This is the first singular length **after three**: all corresponding convolutions at lengths \(4,5,6,7,8,9\) are invertible. Lengths \(2\) and \(3\) are singular. The first-return assertion does not claim that oddness of the Motzkin count is new.

## Assumptions and scope

A Motzkin excursion of length \(n\) is a word in \(\{H,U,D\}^n\) whose cumulative height, with increments \(0,+1,-1\), is always nonnegative and ends at zero. Associate to each word \(p\) a binary incidence vector \(x(p)\in\mathbb F_2^{2n}\), with coordinates \((u_i,d_i)\) at each position \(i\in\{1,\ldots,n\}\), given by the three encodings above. These vectors are distinct for distinct words.

The finite group \(G_n=\mathbb F_2^{2n}\) carries counting measure. Write \(F_n\) for the indicator of the Motzkin incidence support and define unnormalized convolution

\[
(T_nf)(x)=\sum_{p\in\mathcal M_n} f(x+x(p)).
\]

Its Walsh multiplier at \(k=(k_i^U,k_i^D)_{i=1}^n\) is

\[
W_n(k)=\sum_{p\in\mathcal M_n}(-1)^{\sum_{i=1}^n(k_i^Uu_i(p)+k_i^Dd_i(p))}.
\]

The normalization is \(\widehat f(k)=\sum_{x\in G_n}f(x)(-1)^{\langle k,x\rangle}\), with inversion factor \(|G_n|^{-1}\). All exact numerical spectral and projection claims in this result concern \(n=10\), except the stated invertibility checks for lengths at most nine.

## Proof

**Small-length boundary.** Directly from the standard first-return decomposition, \(M_0=1\) and \(M_{n+1}=M_n+\sum_{j=0}^{n-1}M_jM_{n-1-j}\), where \(M_n=|\mathcal M_n|\). The values for lengths \(1\) through \(10\) are respectively \(1,2,4,9,21,51,127,323,835,2188\). Every Walsh multiplier is congruent to \(M_n\) modulo two, because every character value is \(\pm1\). Thus the odd values at lengths four through nine give invertibility; length one is also invertible. The explicit paths at length two give \(W_2(k)=1+(-1)^{k_1^U+k_2^D}\), hence zeros occur. At length three, the four paths \(HHH,HUD,UHD,UDH\) give a zero when the sign of the up step at position one alone is negative: \(1+1-1-1=0\). This settles the asserted small-length boundary.

**Finite exact certificate.** For each \(k\in\mathbb F_2^{20}\), put \(\epsilon_i^U=(-1)^{k_i^U}\) and \(\epsilon_i^D=(-1)^{k_i^D}\). Start with \(a_{0,0}=1\) and all other entries zero, and apply the recurrence, with negative heights excluded,

\[
a_{i+1,h}=a_{i,h}+\epsilon_i^U a_{i,h-1}+\epsilon_i^D a_{i,h+1}
\]

for the ten positions. Then \(a_{10,0}=W_{10}(k)\), because each legal step contributes its individual sign and exactly the nonnegative excursions return to height zero. The executable `verify_motzkin10.cpp` evaluates this recurrence independently at **every** one of the \(2^{20}=1048576\) frequencies. A second implementation recursively enumerates all \(2188\) legal incidences, forms their \(2^{20}\)-entry indicator, and computes its Walsh transform using integer add/subtract butterflies. The two arrays agree at every frequency. The resulting signed multiplier histogram in `spectrum.csv` has 302 distinct values and exactly 67312 zeros, hence rank 981264 by character diagonalization.

The exact weight-class census in `zeros_by_weight.csv` has zero counts at weights zero to three, 48 at weight four, and no others below four. The lexicographically first minimal-weight zero frequency is the 20-bit integer mask \(17924=2^2+2^9+2^{10}+2^{14}\), hence up signs at positions \(2,6,8\) and the down sign at position \(5\). Precisely \(1094\) of the \(2188\) paths contribute each of the signs \(+1\) and \(-1\) there. The smallest nonzero absolute multiplier is 2. The computed Parseval identity is

\[
\sum_{k\in G}|W_{10}(k)|^2=1048576\cdot2188=2294284288.
\]

**Projection norm and unrestricted optimality.** Let \(E=\{k:W_{10}(k)\neq0\}\). The unique translation-invariant projection onto \(R\) is the Fourier-support projection \(P_E\), convolution by \(K(x)=2^{-20}H(x)\), where

\[
H(x)=\sum_{k\in E}(-1)^{\langle k,x\rangle}.
\]

The second complete integer Walsh transform of \(\mathbf1_E\) has \(542\) signed levels, all recorded in `projection_kernel.csv`, and gives

\[
\sum_{x\in G}|H(x)|=52163296,\qquad
\sum_{x\in G}H(x)^2=1048576\cdot981264=1028929880064.
\]

The convolution norm of \(P_E\) on \(\ell^1(G)\) and \(\ell^\infty(G)\) is \(2^{-20}\sum_x|H(x)|=1630103/32768\). To prove minimality among all projections, average any real or complex projection \(Q\) onto \(R\) over conjugation by the group translations. Since \(R\) is translation invariant, the average still projects onto \(R\); the operator norm cannot increase. The averaged operator commutes with translations, hence equals \(P_E\). Therefore no alternative projection has a smaller endpoint norm. This last argument is analytic and independent of the numerical certificate.

## Verification

From a clean directory containing `verify_motzkin10.cpp`, `spectrum.csv`, `projection_kernel.csv`, and `zeros_by_weight.csv`, compile and replay:

```sh
g++ -std=c++17 -O3 verify_motzkin10.cpp -o verify_motzkin10
./verify_motzkin10 --verify
```

The program uses only standard C++17 integer arithmetic. It checks the full transform against the independent height-dynamic recurrence, equality of the three certificates to regenerated values, injectivity of the incidence encoding, the rank, minimum zero-character degree, minimum nonzero gap, both Parseval equalities, and the projection-kernel absolute sum. `--emit` regenerates the three CSV certificates. No Monte Carlo steps or unproved large-dimension extrapolations are used.

## Relationship to prior work

Oste and Van der Jeugt (2015) develop Motzkin and Jacobi–Rogers generating polynomials, recurrence relations, and tridiagonal-matrix interpretations, mainly assigning weights by step height. These methods motivate the transfer approach but do not evaluate the full time-coordinate Walsh spectrum or the exact range-projection constant reported here. Krattenthaler and Müller (first posted 2016) investigate scalar Motzkin numbers modulo powers of two; this explains why even Motzkin counts are a natural potential singularity boundary, but parity alone does not determine the number of Fourier zeros, their minimal frequency weight, or the sharp range-projection norm. The present results also have the equivalent description as all \(\pm1\) specializations of a time-indexed up/down incidence enumerator.

## Limitations

The exact spectral census concerns length ten, and the small-length argument covers only lengths one through nine. No formula for the Fourier nullity in arbitrary length or all possible frequencies is claimed. Although the calculation uses two independent exact algorithms, independent external mathematical validation has not been performed; historical-priority searches are bounded. The terminal result does not claim that the classical Motzkin numbers, their scalar parity, general transfer recurrences, or translation averaging are new.

## References

1. R. Oste and J. Van der Jeugt, *Motzkin Paths, Motzkin Polynomials and Recurrence Relations*, Electronic Journal of Combinatorics 22(2), P2.8 (published 2015-04-21), https://doi.org/10.37236/4781, open-access full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i2p8/pdf/.
2. C. Krattenthaler and T. W. Müller, *Motzkin Numbers and Related Sequences Modulo Powers of 2*, first arXiv posting 2016-08-19, https://arxiv.org/abs/1608.05657.
