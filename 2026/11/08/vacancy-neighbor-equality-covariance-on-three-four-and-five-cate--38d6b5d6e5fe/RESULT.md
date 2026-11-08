# Vacancy–neighbor equality covariance on three-, four-, and five-category cycles

## Finding
Let \(n\ge0\) be an integer and \(r\in\{3,4,5\}\). Select \(X=(X_1,\ldots,X_r)\) uniformly among the nonnegative integer vectors with \(\sum_iX_i=n\). Index coordinates cyclically, and define the vacancy count \(Z=\sum_i\mathbf1\{X_i=0\}\) and the neighboring-equality count \(E=\sum_i\mathbf1\{X_i=X_{i+1}\}\), with \(X_{r+1}=X_1\).

The covariance is exactly

\[
\operatorname{Cov}(Z,E)=
\begin{cases}
0,&r=3,\ n\text{ even},\\
-\dfrac{6(n-1)}{(n+1)(n+2)^2},&r=3,\ n\text{ odd},\\
\dfrac{24n}{(n+1)(n+2)(n+3)^2},&r=4,\ n\text{ even},\\
0,&r=4,\ n\text{ odd},\\
\dfrac{10n}{(n+1)(n+3)(n+4)},&r=5,\ n\text{ even},\\
\dfrac{10(n-1)(n+6)}{(n+2)(n+3)(n+4)^2},&r=5,\ n\text{ odd}.
\end{cases}
\]

Thus, for \(n\ge2\), three categories have strictly *negative* covariance exactly at odd totals and zero covariance at even totals; four categories have strictly *positive* covariance exactly at even totals and zero covariance at odd totals; five categories have strictly *positive* covariance at every total. This is a complete all-total sign classification for the first three nontrivial cyclic category counts. The vanishing statements concern covariance, not independence.

## Assumptions and scope
The sample space consists of \(\binom{n+r-1}{r-1}\) equally likely weak compositions, not of multinomial vectors obtained from independent equiprobable draws. Equivalently it is the symmetric Dirichlet–multinomial model with all Dirichlet parameters equal to one. The cycle has labeled positions, and its \(r\) undirected neighboring pairs are counted once each. At \(n=0\) and \(n=1\), the covariance is zero for all three values of \(r\). No sign assertion for \(r\ge6\) is part of this result.

## Proof
Write \(B_r(n)=\binom{n+r-1}{r-1}\) for \(r\ge1\), and \(B_0(n)=\mathbf1\{n=0\}\). Put
\[
H_r(n)=\sum_{j=0}^{\lfloor n/2\rfloor}B_{r-2}(n-2j),\qquad r\ge2.
\]
In particular \(H_2(n)=\mathbf1\{n\text{ even}\}\). Fixing two prescribed coordinates to be equal to \(j\ge0\) leaves \(r-2\) weak-composition coordinates summing to \(n-2j\); hence \(H_r(n)\) counts the vectors for which a prescribed adjacent pair is equal.

By cyclic symmetry and the fact that each coordinate lies on exactly two cycle edges,
\[
\begin{aligned}
\mathbb EZ&=\frac{rB_{r-1}(n)}{B_r(n)},\\
\mathbb EE&=\frac{rH_r(n)}{B_r(n)},\\
\mathbb E[ZE]&=\frac{r\bigl(2B_{r-2}(n)+(r-2)H_{r-1}(n)\bigr)}{B_r(n)}.
\end{aligned}
\]
Indeed, when a vacancy index belongs to the marked edge, equality forces both edge values to be zero, with \(B_{r-2}(n)\) choices. When it is distinct from both endpoints, deleting the zero coordinate leaves a marked equal pair among \(r-1\) remaining coordinates, with \(H_{r-1}(n)\) choices. Consequently, for *every* \(r\ge3\),
\[
\operatorname{Cov}(Z,E)=\frac{r}{B_r(n)^2}\bigl[B_r(n)\{2B_{r-2}(n)+(r-2)H_{r-1}(n)\}-rB_{r-1}(n)H_r(n)\bigr].\tag{1}
\]
This identity also handles the degenerate totals \(n=0,1\).

The required equal-pair counts are elementary. For \(n=2\ell\) and \(n=2\ell+1\), respectively,
\[
\begin{array}{c|cc}
&n=2\ell&n=2\ell+1\\\hline
H_2(n)&1&0\\
H_3(n)&\ell+1&\ell+1\\
H_4(n)&(\ell+1)^2&(\ell+1)(\ell+2)\\
H_5(n)&\dfrac{(\ell+1)(\ell+2)(4\ell+3)}6&\dfrac{(\ell+1)(\ell+2)(4\ell+9)}6
\end{array}
\]
The last two rows follow from summing, respectively, \(n-2j+1\) and \(\binom{n-2j+2}{2}\) over \(0\le j\le\lfloor n/2\rfloor\). Substitution into (1) and cancellation of common binomial factors gives exactly the six displayed rational expressions. Their numerator factors establish the strict sign statements for every \(n\ge2\), with no asymptotic argument or numerical extrapolation.

## Verification
The standalone `verify.py` recomputes (1) using exact integer binomial coefficients and `Fraction` arithmetic; compares all six closed expressions for \(0\le n\le500\); independently enumerates every weak composition for \(r\in\{3,4,5\}\) and \(0\le n\le12\); additionally enumerates \(r=6,7,8\) at totals up to six as crosschecks of (1); and verifies the strict signs over the tested range. All 3060 assertions passed. The proof above, rather than these finite checks, establishes the formulas for unbounded totals.

## Relationship to prior work
Bender and Canfield (2005) analyze locally restricted *positive* compositions with varying part counts and joint asymptotics of local statistics. Their (2010) follow-up treats periodic adjacent inequalities and may allow zero parts, but the studied conditions intentionally exclude unrestricted zero-part compositions of unbounded length. The present object has a *fixed*, labeled cyclic number of categories and a uniform weak-composition law, and the conclusion is an exact, all-total finite-category covariance phase classification. The classical Dirichlet–multinomial law identifies the equivalent Pólya-sampling interpretation but does not itself imply the displayed equality-vacancy formulas without additional computation. Related occupancy-frequency covariance laws and fixed-content binary run-transition laws concern other statistics and neither implies this neighbor-equality classification. These comparisons limit the priority claim to the exact three-/four-/five-category phase boundary, not to stars-and-bars or generic generating-function methods.

## Limitations
The result does not classify all larger cycle lengths, higher-order dependence, or non-unit Dirichlet parameters. The algebraic formulas can be reconstructed from elementary stars-and-bars probabilities; consequently, an unlocated older exact finite-category multivariate treatment could contain the statement implicitly. No independent priority or correctness audit has been performed.

## References
1. E. A. Bender and E. R. Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics 12 (2005), R57, first published November 7, 2005, https://doi.org/10.37236/1954 .
2. E. A. Bender and E. R. Canfield, *Locally Restricted Compositions III. Adjacent-Part Periodic Inequalities*, Electronic Journal of Combinatorics 17 (2010), R145, published October 29, 2010, https://doi.org/10.37236/417 .
3. J. E. Mosimann, *On the compound multinomial distribution, the multivariate beta distribution, and correlations among proportions*, Biometrika 49 (1962), 65–82, https://doi.org/10.1093/biomet/49.1-2.65 . Historical background only; the date is not asserted as an exact first-online publication day.
