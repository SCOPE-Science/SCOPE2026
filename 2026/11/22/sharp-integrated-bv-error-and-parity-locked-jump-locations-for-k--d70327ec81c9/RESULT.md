# Sharp integrated BV error and parity-locked jump locations for Kantorovich approximation

## Finding

Define the classical Bernstein–Kantorovich operator, for every integer \(n\ge0\), by
\[
(K_nf)(x)=(n+1)\sum_{k=0}^{n}\binom nk x^k(1-x)^{n-k}\int_{k/(n+1)}^{(k+1)/(n+1)}f(t)\,dt,\qquad 0\le x\le1.
\]
Its exact norm from real distributional \(BV(0,1)\), modulo constants and equipped with total variation, to \(L^1(0,1)\), for the error operator \(K_n-I\), is
\[
C_{2m}=\frac{\binom{2m}{m}}{2\cdot4^m},\qquad
C_{2m+1}=2\binom{2m+1}{m}
\left(\frac{m+1}{2m+3}\right)^{m+1}
\left(\frac{m+2}{2m+3}\right)^{m+2},\quad m\ge0.
\]
For even degree the unique norming jump location is \(1/2\). For odd degree \(n=2m+1\), the only two norming locations are \((m+1)/(2m+3)\) and \((m+2)/(2m+3)\); a nontrivial combination of both jumps is **not** norming. More generally, on every open averaging cell \((j/(n+1),(j+1)/(n+1))\), the single-jump error has exactly one strict local maximum at \((j+1)/(n+2)\), with strict local minima at the internal cell boundaries. Finally,
\[
\lim_{n\to\infty}\sqrt{n}\,C_n=\frac1{\sqrt{2\pi}}.
\]
The formulas include \(n=0\), when the operator is ordinary averaging and \(C_0=1/2\).

## Assumptions and scope

The input is a real equivalence class \(f\in BV(0,1)\), with distributional derivative measure \(Df\), and \(|Df|(0,1)>0\). We measure error using Lebesgue \(L^1(0,1)\) and variation using \(|Df|(0,1)\). Boundary point representatives and point values at jumps have no effect on the operator or this norm. The domain is \([0,1]\); cells are unweighted, equal length and nonperiodic. Define the unit right-jump function \(H_s(t)=\mathbf1_{(s,1)}(t)\) for \(0<s<1\).

## Proof

**1. Reduction to jumps.** Every real \(BV(0,1)\) equivalence class admits, almost everywhere, the representation
\[
f(t)=c+\int_{(0,1)}H_s(t)\,d\mu(s),\qquad \mu=Df.
\]
The operator preserves constants and is bounded on \(L^1\), so Bochner/Fubini integration and the triangle inequality imply
\[
\|K_nf-f\|_1\le\int_{(0,1)}\|K_nH_s-H_s\|_1\,d|\mu|(s)
\le \big(\sup_{0<s<1}E_n(s)\big)|Df|(0,1),
\]
where \(E_n(s)=\|K_nH_s-H_s\|_1\). Each jump has unit variation; consequently the supremum over all BV inputs is exactly the supremum of \(E_n\).

**2. One-jump error and derivative.** Write \(p_{n,k}(x)=\binom nkx^k(1-x)^{n-k}\). On the open cell \(j/(n+1)<s<(j+1)/(n+1)\), let \(u=(n+1)s-j\in(0,1)\). Directly from the cell averages,
\[
q_s(x):=(K_nH_s)(x)=\sum_{k=j+1}^np_{n,k}(x)+(1-u)p_{n,j}(x).
\]
Because \(\int_0^1p_{n,k}(x)\,dx=1/(n+1)\), the operator preserves the Lebesgue integral. Also \(0<q_s(x)<1\) for interior \(x,s\). Therefore
\[
E_n(s)=\int_0^s q_s(x)\,dx+\int_s^1(1-q_s(x))\,dx
=2\int_0^s q_s(x)\,dx.
\]
Differentiate with respect to the jump location within its cell, and use the exact beta-binomial tail identity
\[
(n+1)\int_0^sp_{n,j}(x)\,dx
=\sum_{k=j+1}^np_{n,k}(s)+s\,p_{n,j}(s).
\]
It follows that
\[
E_n'(s)=2p_{n,j}(s)\bigl[j+1-(n+2)s\bigr].
\]
Thus the unique interior maximum on cell \(j\) is at \(s_j=(j+1)/(n+2)\). Since \(E_n\) is continuous and the derivative is strictly negative at the right end of each preceding cell and strictly positive at the left end of the next, each internal cell boundary is a strict local minimum. The endpoint limits \(E_n(0)=E_n(1)=0\) cannot maximize.

**3. Exact cell-peak values.** Let \(N=n+1\), \(t=j+1\), \(s=s_j=t/(N+1)\), and \(Z\sim\operatorname{Bin}(N,s)\). The beta-binomial identity above gives
\[
\frac{N}{2}E_n(s_j)
=\mathbb E(Z-t)_+ + s\Pr(Z\ge t).
\]
The elementary binomial tail-moment identity
\[
\mathbb E(Z-t)_+=(Ns-t)\Pr(Z\ge t+1)+(N-t)s\Pr(Z=t)
\]
uses \(Ns=t-s\) and reduces the preceding expression to \((N-t+1)s\Pr(Z=t)\). Simplifying the binomial coefficient and \(s=t/(N+1)\) yields
\[
E_n(s_j)=2\binom nj
\left(\frac{j+1}{n+2}\right)^{j+1}
\left(\frac{n+1-j}{n+2}\right)^{n-j+1}.
\]
Every cell peak is an exact rational number.

**4. Global parity and all norming locations.** Put \(a_k=(k+1)^{k+1}/k!\), for nonnegative integers \(k\). Apart from the same positive factor for all \(j\), the peak above is \(a_ja_{n-j}\). Its ratio sequence satisfies
\[
\frac{a_{k+1}}{a_k}=\left(1+\frac1{k+1}\right)^{k+2}.
\]
This is strictly decreasing in \(k\): for \(t>0\), differentiating \((t+1)\log(1+1/t)\) gives \(\log(1+1/t)-1/t<0\). Consequently
\[
\frac{E_n(s_{j+1})}{E_n(s_j)}
=\frac{a_{j+1}/a_j}{a_{n-j}/a_{n-j-1}}
\]
is greater than one precisely when \(2j<n-1\), equal to one precisely when \(2j=n-1\), and smaller afterward. Reflection gives the same conclusion. There is exactly one central global peak for even \(n\), and exactly two symmetric central peaks for odd \(n\). Substituting their indices into the formula in step 3 proves the two displayed exact constants.

**5. Complete equality classification.** By strictness of the peak comparisons and of cell-wise maximization, equality in step 1 forces the derivative measure \(Df\) to be supported only on the global maximizing jump locations. For even \(n\), it must therefore be a nonzero single atom at the midpoint. For odd \(n\), let the two possible locations be \(a<b\). The error profiles \(K_nH_a-H_a\) and \(K_nH_b-H_b\) are strictly positive left of their jump and strictly negative right of it. If the two jump coefficients have the same sign, the two signed error profiles have opposite signs on \((a,b)\); if they have opposite signs, the signed profiles have opposite signs on \((0,a)\). Both regions have positive measure and both profiles are nonzero there. Hence the \(L^1\) triangle inequality is strict whenever both coefficients are nonzero. Exactly one nonzero jump is necessary and sufficient.

**6. Asymptotics.** The peak formula can be written \(E_n(s_j)=2s_j(1-s_j)\Pr(\operatorname{Bin}(n,s_j)=j)\). For the globally maximizing indices, \(j=n/2+O(1)\) and \(s_j=1/2+O(1/n)\). Stirling's formula (equivalently the elementary central-binomial local approximation) gives \(\Pr(\operatorname{Bin}(n,s_j)=j)\sim\sqrt{2/(\pi n)}\). Thus \(\sqrt n\,C_n\to1/\sqrt{2\pi}\).

## Verification

The standalone `check_kantorovich.py` uses exact rational arithmetic to compare the beta-binomial formula with every cell peak through degree 28, verify the reflection and parity maxima, test strict nearby decay, and verify the integral-preservation and derivative identities at rational jumps. Optional NumPy/SciPy checks test random signed multijump data by numerical quadrature. The finite checks are corroboration, **not** proofs of the universal BV quantifiers or of historical novelty. Run `python3 check_kantorovich.py` from this package directory; optional numerical checks are skipped gracefully if NumPy/SciPy are unavailable.

## Relationship to prior work

Kivinukk and Metsmägi (2011) prove variation-diminution and rates of convergence in the **variation seminorm** for Kantorovich polynomials, principally for smooth or absolutely continuous inputs. That is not an integrated \(BV\)-to-\(L^1\) sharp error norm or a complete discontinuous-extremizer classification. Finta (2014) gives \(L^p\) approximation theorems for a \(q\)-Kantorovich family, with the classical operator as a specialization, but does not state these exact finite-degree coefficients in its available main-result text. Berdysheva and collaborators (2022/2024) obtain pointwise and global \(L^1\)-type bounds for a general integral-operator framework, including Kantorovich operators; their displayed global results have unspecified comparison constants and do not imply the parity-resolved exact constants here. Gonska, Heilmann and Raşa (2011) study higher-order Kantorovich modifications and moment estimates; their full publisher text could not be inspected, so overlapping unpublished or inaccessible historical results remain a residual risk.

Related exact sharp integrated \(BV\) approximation norms have been established separately for the *point-sampled Bernstein operator* and the *Bernstein–Durrmeyer integral operator*. Their kernels and optimal jump sets differ. In particular, the parity-locked displacement of the two optimal Kantorovich jumps, and its cell-wise local-extremum structure, are not formal substitutions into the other operator formulas. The present norm has the same first-order asymptotic as classical Bernstein error, while its first-order coefficient is smaller by \(\sqrt2\) than the Durrmeyer error coefficient under the respective canonical normalizations.

## Limitations

This result concerns only the classical real, unweighted, one-dimensional Bernstein–Kantorovich operator on a uniform noncyclic cell partition. It does not cover generalized \(q\)-Kantorovich rules, weighted cells, multivariate smoothing, other output norms or exact history of priority. The proof is mathematical, and finite numerical tests cannot independently certify infinite-dimensional statements. The literature comparison does not exclude unindexed or inaccessible equivalent results; an independent external audit has not been performed.

## References

1. H. Gonska, M. Heilmann and I. Raşa, “Kantorovich Operators of Order k,” *Numerical Functional Analysis and Optimization* 32 (2011), 717–738, first published online 23 May 2011. https://doi.org/10.1080/01630563.2011.580877
2. A. Kivinukk and T. Metsmägi, “Approximation in variation by the Kantorovich operators,” *Proceedings of the Estonian Academy of Sciences* 60 (2011), 201–209. Open full text: https://kirj.ee/public/proceedings_pdf/2011/issue_4/proc-2011-4-201-209.pdf
3. Z. Finta, “\(L^p\)-Approximation by \(q\)-Kantorovich Operators,” *Journal of Operators* (2014), 958656, first published 15 May 2014. https://doi.org/10.1155/2014/958656
4. E. E. Berdysheva, N. Dyn, E. Farkhi and A. Mokhov, “Metric approximation of set-valued functions of bounded variation by integral operators,” first public arXiv preprint 1 December 2022; *Constructive Approximation* (published online 13 March 2024). https://arxiv.org/abs/2212.00439
