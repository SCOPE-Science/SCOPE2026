# Even-cycle vertex supports: exact Walsh positivity and parity-sharp deconvolution

## Finding

For every integer \(n\ge1\), uniformly count all permutations \(\pi\in S_n\) according to the set of **labels on even-length cycles**. Let \(T_n\) be XOR convolution by this counting kernel on the Boolean group \(G_n=(\mathbb F_2)^n\). At a Walsh character of weight \(k\), its (unnormalized) multiplier is

\[
\Lambda_{n,k}=\begin{cases}
0,&n\text{ even and }k\text{ odd},\\
k!(n-k)!\binom{\lfloor n/2\rfloor}{\lfloor k/2\rfloor}^{2},&\text{otherwise}.
\end{cases}
\]

Each weight occurs with multiplicity \(\binom nk\). Consequently, the operator is positive semidefinite for all orders. For odd \(n\), it is positive definite with rank \(2^n\), smallest eigenvalue \((n-1)!\), largest eigenvalue \(n!\), and exact Euclidean condition number \(n\). For even \(n=2m\), its rank and nullity both equal \(2^{n-1}\), with zeros exactly on odd-weight characters. The least *positive* eigenvalue is

\[
a_m=\min_{0\le r\le m}(2r)!(2m-2r)!\binom mr^2.
\]

It occurs at the unique \(r=m/2\) when \(m\) is even, and at the two values \(r=(m-1)/2,(m+1)/2\) when \(m\) is odd. The largest positive eigenvalue is \((2m)!\); the nonzero-spectrum condition number and Moore–Penrose inverse operator norm are respectively \((2m)!/a_m\) and \(1/a_m\). As \(m\to\infty\),

\[
\frac{(2m)!}{a_m}\sim\frac{\sqrt{\pi m}}{2}=\sqrt{\frac{\pi n}{8}}.
\]

For even orders, the orthogonal projection onto the range is the Walsh projection retaining even-weight characters; its Euclidean norm is one. There is a sharp contrast: odd-order deconvolution has condition \(n\), whereas even-order deconvolution on the recoverable subspace has asymptotic condition \(\sqrt{\pi n/8}\).

## Assumptions and scope

All cycles are disjoint cycles in the standard permutation decomposition, including fixed points (cycles of odd length one). For a permutation \(\pi\), \(E(\pi)\subseteq[n]\) contains all vertices in cycles of length \(2,4,6,\dots\). Let \(f_n(S)=\#\{\pi\in S_n:E(\pi)=S\}\) and \((T_nh)(x)=\sum_{y\in G_n}f_n(y)h(x-y)\), where binary subtraction equals XOR. Walsh characters are \(\chi_U(S)=(-1)^{|U\cap S|}\), with \(k=|U|\). Positive definite refers to the symmetric matrix associated with unnormalized counting convolution, not a covariance matrix. The normalized probability convolution is \(T_n/n!\), with the same rank and condition number and eigenvalues divided by \(n!\).

## Proof

**Restricted-cycle enumeration.** Let \(A_j\) count permutations on \(j\) prescribed labels having all cycles of even length, and \(B_j\) count permutations having all cycles of odd length. The labelled-cycle exponential formula yields

\[
\sum_{j\ge0}A_j\frac{z^j}{j!}=(1-z^2)^{-1/2},\qquad
\sum_{j\ge0}B_j\frac{z^j}{j!}=(1+z)(1-z^2)^{-1/2}.
\]

Thus \(A_{2j}=((2j-1)!!)^2=(2j)!\binom{2j}{j}/4^j\), \(A_{2j+1}=0\), \(B_{2j}=A_{2j}\), and \(B_{2j+1}=(2j+1)A_{2j}\), with \(A_0=B_0=1\). By independent choices of disjoint cycles on a prescribed subset and its complement,

\[
f_n(S)=A_{|S|}\,B_{n-|S|}.
\]

**Even orders.** Fix \(n=2m\). Let \(Y=G_1G_2\) and \(Z=G_3G_4\), products of four independent real standard normal variables. Their even moments are \(\mathbb E Y^{2j}=\mathbb E Z^{2j}=A_{2j}\), and their odd moments vanish. Splitting \(n\) labelled positions by whether they lie in the selected character gives the exact identity

\[
\Lambda_{2m,k}=\mathbb E\!\left[(Z+Y)^{2m-k}(Z-Y)^k\right].
\]

Indeed, the binomial expansion yields the signed sum \(\sum_{S\subseteq[n]}(-1)^{|U\cap S|}A_{|S|}A_{n-|S|}\), including the correct multiplicity for each placement. The joint exponential generating function for these mixed moments is

\[
\mathbb E\,e^{s(Z+Y)+t(Z-Y)}=
\big((1-(s+t)^2)(1-(s-t)^2)\big)^{-1/2}
=\sum_{\ell\ge0}\binom{2\ell}{\ell}\frac{s^{2\ell}t^{2\ell}}{(1-s^2-t^2)^{2\ell+1}}.
\]

The series holds as a formal power series at the origin (or analytically near zero). There are no odd powers of \(t\). Writing \(k=2r\), the coefficient of \(s^{2(m-r)}t^{2r}\) equals

\[
\sum_{\ell=0}^{\min(r,m-r)}\frac{m!}{\ell!^2(r-\ell)!(m-r-\ell)!}
=\binom mr^2,
\]

where the last step is Vandermonde's identity. Multiplication by \((2r)!(2m-2r)!\) gives the stated even-order formula, including strict positivity for every even \(k\).

**Odd orders.** Let \(n=2m+1\). For even \(|S|\), the formula for \(B\) reads \(f_n(S)=(n-|S|)A_{|S|}A_{n-1-|S|}\). Mark one vertex outside \(S\), then delete that marked vertex from the label set; this gives, for any \(U\subseteq[n]\),

\[
\Lambda_{n,k}=(n-k)\Lambda_{n-1,k}+k\Lambda_{n-1,k-1},
\]

where the first term marks outside \(U\) and the second marks within \(U\) (the deleted vertex is not on an even cycle). If \(k=2r\), only the first term survives, yielding \((n-k)(2r)!(2m-2r)!\binom mr^2=(2r)!(n-2r)!\binom mr^2\). If \(k=2r+1\), only the second term survives, yielding \(k!(n-k)!\binom mr^2\). This proves the full formula.

**Extrema.** The multiplier at weight zero is \(n!\), and every other coefficient has magnitude at most \(n!\) by the triangle inequality. All listed eigenvalues are nonnegative. For odd \(n=2m+1\), the support size \(|E(\pi)|\) is always even, so \(\Lambda_{n,k}=\Lambda_{n,n-k}\). Along even weights the strict successive ratio is

\[
\frac{\Lambda_{2m+1,2r+2}}{\Lambda_{2m+1,2r}}=
\frac{(2r+1)(m-r)}{(2m+1-2r)(r+1)}<1\quad(0\le r<m),
\]

since the denominator exceeds the numerator by \(m+1\). Hence the unique smallest character weights for odd \(n\ge3\) are \(1,n-1\), with value \((n-1)!\). At \(n=1\), both weights have multiplier one, giving the same condition-number formula.

For even \(n=2m\), write \(H_r=\Lambda_{2m,2r}\). Then

\[
\frac{H_{r+1}}{H_r}=\frac{(2r+1)(m-r)}{(2m-2r-1)(r+1)}
\]

is less than, equal to, or greater than one according as \(2r+1\) is less than, equal to, or greater than \(m\). This proves the central minimizing weights including the two equal central minima when \(m\) is odd. The condition-number formula can equivalently be written

\[
\frac{(2m)!}{a_m}=\frac{\binom{2m}{2r_*}}{\binom m{r_*}^{2}},
\quad r_*\in\operatorname*{arg\,min}_{0\le r\le m}H_r.
\]

Finally Stirling's formula and \(r_*/m\to1/2\) give the stated square-root asymptotic.

## Verification

Run the included standalone `verify.py` using standard Python 3. It constructs every permutation directly at orders \(1\le n\le8\), identifies even-length-cycle vertex sets by cycle tracing, computes all Walsh coefficients by an exact butterfly transform, and compares them to the theorem. It separately checks the closed spectrum, extrema, symmetry and adjacent-weight inequalities at orders through 200 using integer arithmetic. The executed test suite reported 47,911 passed exact assertions. Finite tests are cross-checks, not substitutes for the preceding infinite proof.

## Relationship to prior work

The labelled-cycle exponential formula and the restricted even-/odd-cycle counts are classical and are not asserted new. Lugo's *Profiles of Permutations* (2009) explicitly develops the generating functions and statistics for permutations constrained to have only even or only odd cycle lengths. This result instead records, for an **unrestricted** permutation, the exact set of labels that happen to lie on its even cycles, then evaluates its complete signed Walsh spectrum and sharp deconvolution constants. Existing counting and moment formulas are inputs to the proof, not themselves novel contributions.

## Limitations

All claims concern the Boolean XOR convolution of the stated labelled-set statistic. They do not concern convolution on the symmetric group itself, do not establish an analogous formula for arbitrary permitted cycle-length sets, and do not assert priority against unindexed historical equivalent calculations. The bound \(\kappa^+\) for even orders is on the nonzero Fourier spectrum; the full operator has no inverse at those orders.

## References

1. Michael Lugo, *Profiles of permutations*, arXiv:0907.5351 (first publicly posted 2009-07-30), *Electronic Journal of Combinatorics* **16** (2009), R99, DOI: [10.37236/188](https://doi.org/10.37236/188). In particular Sections 1 and 3 on the exponential formula and even/odd cycle restrictions.
2. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009, chapter on labelled permutations and the exponential formula, [open author-hosted edition](https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html).
