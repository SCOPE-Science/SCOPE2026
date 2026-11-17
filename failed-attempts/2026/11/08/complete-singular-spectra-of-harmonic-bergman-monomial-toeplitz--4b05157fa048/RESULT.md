# Complete singular spectra of harmonic Bergman monomial Toeplitz self-commutators

## Finding

On the unweighted complex harmonic Bergman space of the unit disk, let \(T_m=Q M_{z^m}|_{L_h^2}\) for every integer \(m\geq1\), where \(Q\) is the harmonic Bergman orthogonal projection. The selfadjoint self-commutator
\[
D_m=[T_m^*,T_m]=T_m^*T_m-T_mT_m^*
\]
is compact, trace class, and has one-dimensional kernel. Put, for every integer \(j\geq1\),
\[
a_{m,j}=\begin{cases}
\dfrac{j^2(j+1)}{(j+m+1)(m+1)^2},&1\leq j<m,\\[2mm]
\dfrac{m^2}{(j+1)(j+m+1)},&j\geq m.
\end{cases}
\]
The complete spectrum and nonzero singular-value multiset, **including multiplicities**, are
\[
\sigma(D_m)=\{0\}\cup\{a_{m,j},-a_{m,j}:j\geq1\},\qquad
\{s_n(D_m):n\geq1\}=\{a_{m,j},a_{m,j}:j\geq1\}.
\]
The two exact norms are
\[
\boxed{\|D_m\|=\frac{m^2}{(m+1)(2m+1)},\qquad
\|D_m\|_{\mathcal S_1}=\frac{m(5m+1)}{3(m+1)}.}
\]
Moreover \(\operatorname{Tr}D_m=0\), and the singular values in decreasing order satisfy the **sharp indexed asymptotic**
\[
\boxed{\lim_{n\to\infty}n^2s_n(D_m)=4m^2.}
\]
In particular, for every real \(p>0\),
\[
D_m\in\mathcal S_p\quad\Longleftrightarrow\quad p>\tfrac12,
\qquad D_m\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2}.
\]

## Assumptions and scope

The area measure is \(dA(z)=\pi^{-1}dx\,dy\) on \(\mathbb D\). The Hilbert space \(L_h^2(\mathbb D)\) consists of all complex-valued harmonic functions square-integrable for this measure. The bounded Toeplitz operator with bounded symbol \(\phi\) is \(T_\phi=Q M_\phi|_{L_h^2}\). Thus \(T_m=T_{z^m}\) and \(T_m^*=T_{\overline z^{\,m}}\), with no domain ambiguity. The normalization, commutator order, integer restriction \(m\geq1\), and multiplicities are part of the claim. The weak ideal \(\mathcal S_{1/2,\infty}\) is defined here by \(\sup_{n\geq1}n^2s_n(D_m)<\infty\).

## Proof

**Projection and weighted shift.** The harmonic Bergman orthonormal basis indexed by \(j\in\mathbb Z\) is
\[
e_j(z)=\begin{cases}\sqrt{j+1}\,z^j,&j\geq0,\\
\sqrt{1-j}\,\overline z^{-j},&j<0.
\end{cases}
\]
For nonnegative integers \(a,b\), direct angular orthogonality and radial integration give
\[
Q(z^a\overline z^{\,b})=\begin{cases}
\dfrac{a-b+1}{a+1}z^{a-b},&a\geq b,\\[1mm]
\dfrac{b-a+1}{b+1}\overline z^{\,b-a},&a<b.
\end{cases}
\]
Consequently \(T_me_j=w_{m,j}e_{j+m}\), where all \(w_{m,j}>0\) and
\[
w_{m,j}^{2}=\begin{cases}
\dfrac{j+1}{j+m+1},&j\geq0,\\[1mm]
\dfrac{(r+1)(m-r+1)}{(m+1)^2},&j=-r,\ 1\leq r\leq m,\\[1mm]
\dfrac{r-m+1}{r+1},&j=-r,\ r\geq m+1.
\end{cases}\tag{1}
\]
These are bounded weights, as also follows from \(\|T_m\|\leq\|z^m\|_\infty=1\).

**Signed diagonalization.** The adjoint weighted-shift formula gives
\[
D_me_j=(w_{m,j}^2-w_{m,j-m}^2)e_j.\tag{2}
\]
Equation (1) has the reflection property \(w_{m,j}^2=w_{m,-m-j}^2\), so the diagonal coefficient at \(-j\) is the negative of that at \(j\). At \(j=0\), both weights are \(1/(m+1)\), hence the coefficient is zero. For \(1\leq j<m\), substitution of the crossing-origin branch in (1) yields
\[
\frac{j+1}{j+m+1}-\frac{(m-j+1)(j+1)}{(m+1)^2}
=\frac{j^2(j+1)}{(j+m+1)(m+1)^2}.
\]
For \(j\geq m\), both shifted weights use the analytic branch and
\[
\frac{j+1}{j+m+1}-\frac{j-m+1}{j+1}
=\frac{m^2}{(j+1)(j+m+1)}.
\]
Every displayed \(a_{m,j}\) is strictly positive. Hence (2) gives all eigenvalues and eigenvectors, and the kernel is exactly \(\operatorname{span}\{e_0\}\). Since \(a_{m,j}\to0\), the complete spectrum is the stated closure; the signed eigenvalues are paired, including possible accidental repeated numerical values. Moreover, \(\sum_j a_{m,j}<\infty\) by the quadratic tail bound; thus \(D_m\) is trace class and its signed trace cancels absolutely.

**Operator norm.** On the finite branch \(1\leq j<m\), the function \(x\mapsto x^2(x+1)/(x+m+1)\) increases strictly for \(x>0\). On the infinite branch \(j\geq m\), the rational formula decreases strictly. For \(m\geq2\), the junction comparison is
\[
a_{m,m}-a_{m,m-1}=\frac{5m^2-1}{2(m+1)^2(2m+1)}>0.
\]
For \(m=1\) the finite branch is empty. The maximum for all \(m\geq1\) occurs at \(j=m\), and equals the asserted operator norm.

**Trace norm.** Fix \(r\in\{0,\ldots,m-1\}\) and consider the bilateral sequence of weights squared \(w_{m,r+km}^2\) as \(k\in\mathbb Z\). Its limits at both ends are \(1\). The signed coefficients in (2), already proved, imply it decreases up to \(r-m\), then increases to \(1\), with a possible two-point minimum plateau for \(r=0\). Its minimum is
\[
b_{m,r}=\frac{(r+1)(m-r+1)}{(m+1)^2}.
\]
The total variation along this full residue chain therefore equals \(2(1-b_{m,r})\). Summing over all residue chains and using
\[
\sum_{r=0}^{m-1}(r+1)(m-r+1)=\frac{m(m+1)(m+5)}{6}
\]
gives
\[
\|D_m\|_{\mathcal S_1}
=2\sum_{r=0}^{m-1}(1-b_{m,r})
=2m-\frac{m(m+5)}{3(m+1)}
=\frac{m(5m+1)}{3(m+1)}.
\]
The equal tails ensure that all variations converge absolutely; no formal interchange of conditionally convergent sums is used.

**Indexed singular values and endpoint.** The finite branch contributes exactly \(2(m-1)\) singular values counting multiplicities. The remaining values comprise two copies of the strictly decreasing sequence
\[
a_{m,j}=\frac{m^2}{(j+1)(j+m+1)}\sim\frac{m^2}{j^2},\qquad j\to\infty.
\]
Sorting finitely many exceptional positive values changes the tail index by at most a fixed constant depending on \(m\). Since every tail value appears twice, \(s_n(D_m)\sim4m^2/n^2\). Therefore \(\sum_ns_n(D_m)^p<\infty\) exactly when \(2p>1\); the weak endpoint holds, while its strong counterpart diverges harmonically.

## Verification

Run `python3 check_spectrum.py` in the same directory as this document. The independent-formula finite checker uses Python's exact `fractions.Fraction` arithmetic to compare projection-derived weights against (1), test the reflected signed spectrum and monotonicity, and compare the trace-norm expression with an exact positive-tail sum. Its output on the packaged source is `HARMONIC_BERGMAN_MONOMIAL_FINITE_OK 23205`. These 23,205 finite assertions corroborate identities for \(1\leq m\leq30\), but do not prove any universal or infinite-dimensional assertion. The full proof above supplies those steps.

## Relationship to prior work

Tian, Wang and Zhao (2026) prove qualitative noncommutativity for analytic and coanalytic harmonic Bergman Toeplitz operators. The present result quantifies the canonical monomial pair via its **entire** signed spectrum, exact trace and operator norms, and sharp operator-ideal threshold. Dong and Zhou (2014/2016) classify finite-rank commutators of quasihomogeneous Toeplitz operators; their Theorem 4.4 treats finite rank and does not supply the present infinite-rank singular-value list. Dong and Zhou (2012) give earlier quasihomogeneous commutation criteria, also different from these norms. Chbichib and Ghiloufi (2026) analyze singular values of \([M_u,Q]\) on ambient \(L^2\), a different operator from \([QM_{\bar z^m}Q,QM_{z^m}Q]\) acting on the harmonic subspace. Chen, Koo and Lee (2013) study finite ranks of general Toeplitz commutators, not an identified exact trace-norm classification. Prior general projection formulas are used transparently; the claim is the complete quantified consequence for this natural family, not novelty of the projection identity.

## Limitations

The exact formulas concern only the **unweighted** harmonic Bergman space and integer monomial degrees. They do not assert the same spectral behavior for arbitrary analytic symbols, general quasihomogeneous symbols, or weighted spaces. A general formula in older quasihomogeneous literature might imply a portion of this classification after specialization, so independent publication-priority review remains necessary. The full text of Chen, Koo and Lee (2013) was not available for direct inspection; its abstract discusses finite ranks. No independent mathematical audit is claimed.

## References

1. X. Tian, J. Wang and X. Zhao, *Commuting analytic and co-analytic Toeplitz operators on the harmonic Bergman space* (first public September 13, 2026), arXiv:2609.14635, https://arxiv.org/abs/2609.14635 .
2. X.-T. Dong and Z.-H. Zhou, *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*, arXiv:1411.0213v3, especially Section 4, https://arxiv.org/html/1411.0213v3 .
3. X.-T. Dong and Z.-H. Zhou, *Commuting Quasihomogeneous Toeplitz Operators on the Harmonic Bergman Space*, Complex Analysis and Operator Theory **7** (2013), 1267–1285; DOI:10.1007/s11785-012-0223-0.
4. Y. Chen, H. Koo and Y. J. Lee, *Ranks of commutators of Toeplitz operators on the harmonic Bergman space*, Integral Equations and Operator Theory **75** (2013), 31–38; DOI:10.1007/s00020-012-2020-6.
5. K. Chbichib and N. Ghiloufi, *Spectral properties of commutators on harmonic Bergman spaces of the unit disk*, arXiv:2605.24698, https://arxiv.org/abs/2605.24698 .
