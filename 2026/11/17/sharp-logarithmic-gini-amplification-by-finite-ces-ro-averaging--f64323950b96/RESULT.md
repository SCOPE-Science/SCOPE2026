# Sharp logarithmic Gini amplification by finite Cesàro averaging

## Finding

For each integer \(n\ge2\), define the real prefix Cesàro matrix by
\[
(C_nx)_i=\frac1i\sum_{j=1}^{i}x_j,\qquad 1\le i\le n,
\]
and define the complete-graph Gini variation seminorm
\[
G_n(x)=\sum_{1\le i<j\le n}|x_i-x_j|.
\]
Writing \(H_n=\sum_{i=1}^{n}1/i\), the sharp quotient operator seminorm is
\[
\boxed{\ \sup_{G_n(x)>0}\frac{G_n(C_nx)}{G_n(x)}
=\frac{(n+1)H_n-2n}{n-1}.\ }
\]
The constant is attained for every \(n\) by the first-coordinate indicator \(e_1=(1,0,\ldots,0)\), and therefore also gives the exact two-input Lipschitz constant of this linear operator. The sequence of constants is strictly increasing, is at most one exactly for \(2\le n\le5\), and obeys
\[
\frac{(n+1)H_n-2n}{n-1}
=\log n+\gamma-2+O\!\left(\frac{\log n}{n}\right).
\]
Thus finite prefix averaging has logarithmically growing sharp amplification in complete-graph variation, despite having sharp contraction factor \(1-1/n\) in finite adjacent-edge path variation.

## Assumptions and scope

Everything is over real vectors of exactly \(n\ge2\) coordinates, with uniform prefix averages and equal weights on all \(\binom n2\) unordered coordinate pairs. Constants form the kernel of \(G_n\), and \(C_n\mathbf1=\mathbf1\), so the quotient seminorm and two-input quotient are well defined. The theorem makes no assertion about iterated Cesàro powers, weighted coordinate-pair variation or infinite-sequence Gini geometry.

## Proof

**1. Reduction to binary cuts.** For any real \(x\), sort its distinct levels. There exist nested nonempty proper upper-level sets \(S_a\), positive increments \(\delta_a\), and \(c\in\mathbb R\) such that
\[
x=c\mathbf1+\sum_a\delta_a\mathbf1_{S_a},\qquad
G_n(x)=\sum_a\delta_a|S_a|(n-|S_a|).
\]
Because \(C_n\mathbf1=\mathbf1\), the triangle inequality gives
\[
\frac{G_n(C_nx)}{G_n(x)}\le
\max_{\varnothing\ne S\subsetneq[n]}
\frac{G_n(C_n\mathbf1_S)}{|S|(n-|S|)}.
\]
Every binary cut is itself admissible, so equality holds in this reduction. Replacing a cut by its complement does not change the quotient: \(C_n\mathbf1_{S^c}=\mathbf1-C_n\mathbf1_S\). Hence it is sufficient to take \(k=|S|\le n/2\).

**2. Exact column norms and monotonicity.** Define \(g_j=G_n(C_ne_j)\). The column \(C_ne_j\) is zero before index \(j\) and has entry \(1/i\) at each \(i\ge j\). Summing its pairwise absolute differences yields
\[
g_j=(n+2j-1)(H_n-H_{j-1})-2(n-j+1).
\]
In particular \(g_1=(n+1)H_n-2n\), and
\[
g_{j+1}-g_j=2\sum_{i=j}^n\frac1i-\frac{n+1}{j}\le0.
\]
For completeness, set \(D_j(n)=n+1-2j\sum_{i=j}^n1/i\). Its consecutive difference is \(1-2j/(n+1)\), so its minimum over integers \(n\ge j\) occurs at \(n=2j-1\) or the adjacent integer. At \(n=2j-1\) the \(j\) summands are each at most \(1/j\), giving \(D_j(2j-1)\ge0\). This proves the displayed monotonicity for every \(j\). Thus, for any cut of size \(k\),
\[
G_n(C_n\mathbf1_S)\le\sum_{j\in S}g_j\le\sum_{j=1}^k g_j.
\]
Directly summing the harmonic formula gives
\[
\frac1k\sum_{j=1}^kg_j
=(n+k)(H_n-H_k)-n+\frac{3k-1}{2}.
\]

**3. Uniform harmonic inequality.** Put
\[
F(n,k)=\frac{n-k}{n-1}\big((n+1)H_n-2n\big)
-\left[(n+k)(H_n-H_k)-n+\frac{3k-1}{2}\right].
\]
For \(n\ge9\) and \(2\le k\le\lfloor n/2\rfloor\), we prove \(F(n,k)>0\). Its exact first difference in \(n\), for every \(n\ge2k\), is
\[
F(n+1,k)-F(n,k)=H_k-1-
\frac{2(k-1)}{n-1}\left(1-\frac{H_n}{n}\right)>0.
\]
Indeed \(H_k-1\ge(k-1)/k\), while \(H_n\ge1\) gives
\[
\frac{2(k-1)}{n-1}\left(1-\frac{H_n}{n}\right)
<\frac{2(k-1)}n\le\frac{k-1}{k}.
\]
For \(k=2,3,4\), direct rational evaluation gives \(F(9,k)>0\). For each \(5\le k\le21\), the exact rational quantities \(F(2k,k)\) are strictly positive; the complete seventeen-case certificate is checked in the standalone `check_gini_cesaro.py`. To cover all remaining \(k\ge22\) without any finite extrapolation, rewrite the initial value as
\[
\frac{F(2k,k)}k
=\frac{2k+1}{2k-1}H_k
-\frac{4(k-1)}{2k-1}(H_{2k}-H_k)
-\frac{4k}{2k-1}+\frac{k+1}{2k}.
\]
The elementary integral inequalities \(H_k\ge\log(k+1)>\log23>3\) and \(H_{2k}-H_k\le\log2<7/10\), together with \(4(k-1)/(2k-1)<2\) and \(4k/(2k-1)\le88/43\), imply
\[
\frac{F(2k,k)}k>3-\frac75-\frac{88}{43}+\frac12
=\frac{23}{430}>0.
\]
The positive first differences now prove \(F(n,k)>0\) for every claimed pair. When \(k=1\), the decreasing-column property already gives the desired bound. Combining these cases with the cut reduction proves the sharp upper bound for every \(n\ge9\).

**4. The small dimensions.** For each \(2\le n\le8\), every nonempty proper cut is enumerated with exact fractions in `check_gini_cesaro.py`. The resulting maxima, in order, are \(1/2\), \(2/3\), \(29/36\), \(37/40\), \(103/100\), \(118/105\), and \(2369/1960\), exactly the harmonic formula. There are 494 checked cuts in total. This finite certificate is exhaustive in precisely these seven dimensions; all larger dimensions are handled by Step 3.

**5. Sharpness and consequences.** Since \(C_ne_1=(1,1/2,\dots,1/n)\),
\[
G_n(C_ne_1)=\sum_{i<j}\left(\frac1i-\frac1j\right)
=(n+1)H_n-2n,
\qquad G_n(e_1)=n-1.
\]
This attains the upper bound. The constant is strictly increasing in \(n\), because after clearing positive denominators its successive difference has numerator
\[
\frac{(n-1)(n+2)}{n+1}-2(H_n-1)
\ge\frac{n-1}{n+1}>0,
\]
where \(H_n-1\le(n-1)/2\). The exact fifth- and sixth-dimensional values \(37/40<1<103/100\) give the nonexpansivity threshold. Finally, \(H_n=\log n+\gamma+O(1/n)\) yields the stated asymptotic.

## Verification

Run `python3 check_gini_cesaro.py` with ordinary Python 3. The dependency-free script uses `fractions.Fraction` throughout all claimed finite certificates, checks all 494 small-dimensional cuts, all seventeen harmonic base cases, the three special anchors, and independently checks the explicit column identities and difference identities on finite test grids. Additional signed-vector tests are diagnostics, not substitutes for the all-dimensional arguments above. The proof requires no unprovided source code, data file or third-party library.

## Relationship to prior work

Akhmedov and Başar (2008), Theorem 3.1, compute a norm-one result for the infinite Cesàro operator in the \(bv_p\) sequence norm based on consecutive differences. The present seminorm instead sums differences between **all** coordinate pairs, and the sharp norm grows like \(\log n\); the former statement cannot imply the latter. Lacruz–León-Saavedra–Petrovic–Zabeti (first posted March 19, 2014), particularly Section 5, study extended eigenoperators of the discrete Cesàro operator on \(\ell^p\); those spectral results likewise do not give the finite Gini quotient norm. For comparison, the finite path-variation norm of one application of \(C_n\) is \(1-1/n\): applying the cut reduction to contiguous step functions, each step at position \(r\) is mapped to the monotone profile \(1\) on the first \(r\) entries and \(r/i\) subsequently, whose variation is \(1-r/n\). Hence the path norm is attained at \(r=1\). This strict finite-dimensional contraction does not imply the current complete-graph formula. Searches for the pairwise-difference, Gini, complete-graph variation, and Hardy/Cesàro formulations did not identify an equivalent statement; this absence is not proof of global historical priority.

## Limitations

The exact formula applies to the real finite prefix Cesàro matrix and unweighted complete-graph Gini variation, not to arbitrary weighted Gini norms, signed stochastic kernels, generalized Cesàro matrices or all iterates. The relevant older published text on \(bv_p\) was readable, but visual PDF-page retrieval was rate-limited; this is a source-access limitation, not evidence of coverage or absence. Bibliographic priority remains qualified pending wider independent review.

## References

1. A. M. Akhmedov and F. Başar, *The Fine Spectra of the Cesàro Operator \(C_1\) over the Sequence Space \(bv_p\)*, Mathematical Journal of Okayama University **50** (2008), 135–147, Theorem 3.1; publisher open text: https://ousar.lib.okayama-u.ac.jp/files/public/3/33130/20160528030811158559/fulltext.pdf . Day-precision first-online posting is not verified for this older journal source.
2. M. Lacruz, F. León-Saavedra, J. Petrovic and O. Zabeti, *Extended eigenvalues for Cesàro operators*, arXiv:1403.4844, initial public version March 19, 2014, particularly Section 5: https://arxiv.org/abs/1403.4844 .
