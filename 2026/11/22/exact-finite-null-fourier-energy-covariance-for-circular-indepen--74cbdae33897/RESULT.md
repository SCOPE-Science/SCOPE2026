# Exact finite-null Fourier-energy covariance for circular independence

## Finding

For independent uniform circular coordinates, the finite-sample covariance of any two squared empirical characteristic-function factorization discrepancies has exactly four values, classified solely by which absolute Fourier frequencies coincide and by their relative signs. This yields an exact variance formula for rectangular-frequency independence statistics and a frequency-budget crossover that is invisible to fixed-frequency asymptotics.

Let \(n\ge 2\), let \((X_i,Y_i)_{i=1}^n\) be independent observations with independent uniform coordinates on \([0,2\pi)\), and let \(p,q,r,s\in\mathbb Z\setminus\{0\}\). Define

\[
D_{p,q}=\frac1n\sum_{i=1}^n e^{\mathrm i(pX_i+qY_i)}-\left(\frac1n\sum_{i=1}^n e^{\mathrm ipX_i}\right)\left(\frac1n\sum_{i=1}^n e^{\mathrm iqY_i}\right),\qquad Z_{p,q}=\frac{n^2}{n-1}|D_{p,q}|^2.
\]

Then \(\mathbb EZ_{p,q}=1\), and the **complete exact finite-null covariance law** is

\[
\operatorname{Cov}(Z_{p,q},Z_{r,s})=
\begin{cases}
0,&|p|\ne |r|\ \text{and}\ |q|\ne |s|,\\[2pt]
\displaystyle\frac{1}{n(n-1)},&\text{exactly one absolute-frequency coordinate coincides},\\[5pt]
\displaystyle\frac{n+3}{n^2(n-1)},&|p|=|r|,\ |q|=|s|,\ pqrs<0,\\[5pt]
\displaystyle\frac{n(n-1)^2+3}{n^2(n-1)},&|p|=|r|,\ |q|=|s|,\ pqrs>0.
\end{cases}
\]

The last case includes identical modes and their simultaneous sign reversal. Thus modes with no shared absolute frequency are exactly uncorrelated, whereas modes sharing just one absolute frequency have strictly positive covariance, although this dependence tends to zero for fixed modes as the sample size grows.

For positive integers \(P,Q\), the natural symmetric rectangular harmonic statistic

\[
S_{P,Q}=\sum_{p=1}^{P}\sum_{q=1}^{Q}\left(Z_{p,q}+Z_{p,-q}\right)
\]

has exact expectation \(2PQ\) and variance

\[
\boxed{\operatorname{Var}(S_{P,Q})=\frac{2PQ}{n^2(n-1)}\left[n(n-1)^2+n+6+2n(P+Q-2)\right].}
\]

In particular, the exact ratio of variance to mean grows substantially above its fixed-frequency limit of one when \(P+Q\) is of order \(n^2\). This statement concerns null second moments, not an asserted distributional approximation or a level guarantee.

## Assumptions and scope

All observations are iid, with both circular coordinates **uniform and mutually independent**. These are stronger assumptions than a generic null hypothesis of independence for arbitrary circular marginals. Frequencies are nonzero integers and may be arbitrarily large; no restriction linking \(P,Q\) to \(n\) is imposed. The phase convention uses radians; multiplying both angular coordinates by an integer merely indexes their Haar characters. The statistics are empirically centered using the product of sample marginal characteristic functions, not the known population characteristic functions.

The calculation is invariant under separate rotations of the two coordinate samples, since such rotations multiply \(D_{p,q}\) by a unit complex phase. For \(n=2\), the two signed modes with the same absolute-frequency pair have identical squared energies; the displayed covariance formulas remain valid, including their equality at that boundary.

## Proof

**1. Matrix representation and normalization.** Let \(H=I_n-\mathbf1\mathbf1^\top/n\), so \(H^\top=H\) and \(H^2=H\). Write \(a_i=e^{\mathrm ipX_i}\), \(b_j=e^{\mathrm iqY_j}\). Direct expansion gives

\[
D_{p,q}=\frac1n\sum_{i,j=1}^n H_{ij}a_i b_j.
\]

Haar character orthogonality implies \(\mathbb E(a_i\overline a_k)=\delta_{ik}\) and likewise for \(b\), because \(p,q\ne0\). Consequently

\[
\mathbb E|D_{p,q}|^2=\frac1{n^2}\sum_{i,j}H_{ij}^2=\frac{\operatorname{tr}(H)}{n^2}=\frac{n-1}{n^2},
\]

establishing \(\mathbb EZ_{p,q}=1\).

**2. Fourth-order character orthogonality.** For nonzero \(p,r\) and indices \(i,k,a,c\in\{1,\ldots,n\}\), independent uniform angles give the *exact* identity

\[
\begin{aligned}
&\mathbb E\big[e^{\mathrm ip(X_i-X_k)}e^{\mathrm ir(X_a-X_c)}\big]\\
&\quad=\delta_{ik}\delta_{ac}
+\mathbf1_{p=r}\left(\delta_{ic}\delta_{ak}-\delta_{i=k=a=c}\right)
+\mathbf1_{p=-r}\left(\delta_{ia}\delta_{kc}-\delta_{i=k=a=c}\right).
\end{aligned}
\]

Here \(\delta_{i=k=a=c}\) denotes the indicator that all four sample indices agree. For the two potential crossed pairings, the all-equal case has been subtracted once to avoid duplicate counting. Character orthogonality shows that no other arithmetic frequency resonance can arise from a product with just two positive and two negative character occurrences. The same identity applies independently to the \(Y\) coordinates at frequencies \(q,s\).

**3. Contract the two fourth-moment tensors.** Expanding \(\mathbb E(|D_{p,q}|^2|D_{r,s}|^2)\) using the matrix representation, subtracting \(\{(n-1)/n^2\}^2\), and inserting the two orthogonality identities yields three kinds of terms. If neither absolute frequency matches, only the baseline pairing survives and the covariance vanishes. One matched coordinate contributes

\[
\frac{1}{n^4}\sum_{i\ne k}(H^2)_{ik}^{2}=
\frac{1}{n^4}\sum_{i\ne k}H_{ik}^2=\frac{n-1}{n^5}.
\]

If both coordinates match, there are two one-coordinate contributions, plus one double-crossing contraction. When the relative signs agree, the latter is \(T_{\parallel}/n^4\), and when they disagree, it is \(T_{\times}/n^4\), with

\[
\begin{aligned}
T_{\parallel}&=\sum_{i\ne k}\sum_{j\ne l}H_{ij}^{2}H_{kl}^{2}=\frac{(n-1)(n^3-2n^2-n+3)}{n^2},\\
T_{\times}&=\sum_{i\ne k}\sum_{j\ne l}H_{ij}H_{kj}H_{kl}H_{il}=-\frac{(n-1)(n-3)}{n^2}.
\end{aligned}
\]

For completeness, these contractions follow by writing \(H_{ij}=\delta_{ij}-1/n\), using each row-square sum \(\sum_jH_{ij}^2=(n-1)/n\), \(\sum_{ij}H_{ij}^2=n-1\), \(\operatorname{tr}(H^4)=n-1\), and subtracting terms with equal row or column indices. These are explicit finite sums, valid also for \(n=2,3\).

Therefore the four cases for **unnormalized** squared energies are zero, \((n-1)/n^5\), \((n-1)(n+3)/n^6\), and \((n-1)\{n(n-1)^2+3\}/n^6\), respectively. Multiplication by \(n^4/(n-1)^2\) proves the displayed normalized covariance law.

**4. Rectangular-grid variance.** There are \(2PQ\) signed energies in \(S_{P,Q}\). Each has variance \(v=\{n(n-1)^2+3\}/\{n^2(n-1)\}\). There are \(PQ\) unordered opposite-sign pairs with both absolute frequencies equal; their covariance is \(w=(n+3)/\{n^2(n-1)\}\). Finally, there are exactly \(2PQ(P+Q-2)\) unordered pairs sharing precisely one absolute-frequency coordinate; each has covariance \(u=1/\{n(n-1)\}\). All other pairs contribute zero. Consequently

\[
\operatorname{Var}(S_{P,Q})=(2PQ)v+2(PQ)w+4PQ(P+Q-2)u,
\]

which simplifies to the claimed formula. This proves the finite-sample theorem for every admissible parameter, without asymptotic passage.

## Verification

The standalone `verify.py` computes Haar moments by **independent Laurent-polynomial constant-term extraction** from \(n^2D_{p,q}\); it does not implement the projection-matrix contractions used in the proof. Running `python verify.py` reproduces 33 exact rational comparisons for eleven frequency configurations at each of \(n=2,3,4\), including opposite-frequency signs and unrelated nonconsecutive frequencies. Another twelve exact-rational assertions verify the rectangular combinatorial variance identity for several grid sizes. All 45 assertions passed. The checker is a finite cross-check, not a substitute for the general proof.

## Relationship to prior work

García-Portugués, Lafaye de Micheaux, Meintanis and Verdebout (2021), Section 3, Equations (8)–(11), introduce the empirical-characteristic-function factorization discrepancy and its weighted circular-independence test. Their Appendix B calculates an **asymptotic covariance matrix of the linear real/imaginary discrepancies**, whereas the present result calculates an **exact finite-sample covariance matrix of their squared magnitudes**, under the explicitly stronger uniform-null assumption, and derives an exact growing-grid variance law. Nothing about the definition of the statistic, the characteristic-function method, or asymptotic Gaussian covariance is claimed as new.

Pfister, Bühlmann, Schölkopf and Peters (2016) provide a broad kernel-independence framework encompassing characteristic-function methods, with general asymptotic moment expansions for related V-statistics (Propositions 3.10–3.11). Those statements do not directly give an exact finite-\(n\) frequency-pair classification or the \(P+Q\) correction for this particular rectangular signed-frequency statistic. The present claim is not a general improvement of kernel-based null calibration; it is a specialized exact calculation.

## Limitations

The exact null formula requires independent **uniform** circular marginals; it does not extend verbatim to arbitrary independent angular distributions, nor does it establish rejection thresholds, finite-sample test level, test power or a high-dimensional limit distribution. The \(P+Q\) crossover describes second moments and does not by itself establish a central limit theorem when the harmonic grid grows. Literature comparison was focused on the defining source, a broad kernel-treatment source, and searches for equivalent finite-harmonic covariance formulas; independently confirming global historical priority is outstanding. Published covariance formulas for other kernels or after marginal transforms might conceivably yield an indirect alternative derivation.

## References

1. E. García-Portugués, P. Lafaye de Micheaux, S. G. Meintanis and T. Verdebout, *Nonparametric tests of independence for circular data based on trigonometric moments*, arXiv:2104.14620v1 (first public 2021-04-29), Section 3 and Supplementary Appendix B. https://arxiv.org/html/2104.14620v1
2. N. Pfister, P. Bühlmann, B. Schölkopf and J. Peters, *Kernel-based Tests for Joint Independence*, arXiv:1603.00285 (first public 2016-03-01), Sections 2–3, Propositions 3.10–3.11, Appendix D.5. https://arxiv.org/pdf/1603.00285
