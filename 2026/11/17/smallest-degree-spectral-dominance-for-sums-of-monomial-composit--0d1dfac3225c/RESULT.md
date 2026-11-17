# Smallest-degree spectral dominance for sums of monomial compositions on logarithmic Hardy scales

## Finding
For a finite, nonzero linear combination of monomial composition operators on a logarithmically weighted analytic Hilbert space, the **smallest input monomial degree alone** determines the asymptotic sequence of singular values once the coefficient weights decay faster than every fixed negative power of \(\log n\) in the specified scale. This gives a sharp compactness/Schatten trichotomy and a universal logarithmic residue at its Schatten boundary.

Precisely, for \(c>0\), \(\gamma>0\), finite \(D\subseteq\{2,3,\ldots\}\), and complex coefficients \(a_d\ne0\), let \(d_0=\min D\), \(T=\sum_{d\in D} a_d C_{z^d}\). Then \(T\) is compact exactly when \(\gamma>1\). For \(\gamma>1\),
\[
s_n(T)\sim |a_{d_0}|\exp\left(-\frac c2\{[\log(d_0n+1)]^\gamma-[\log(n+1)]^\gamma\}\right).
\]
At \(1<\gamma<2\), it lies in no \(\mathcal S_p\) with finite \(p>0\); at \(\gamma>2\), it lies in all such ideals. At \(\gamma=2\), the exact threshold is \(p_*=1/(c\log d_0)\): membership holds precisely for \(p>p_*\), and
\[
\lim_{N\to\infty}\frac1{\log N}\sum_{n=1}^N s_n(T)^{p_*}
=|a_{d_0}|^{p_*}d_0^{-1/2}.
\]
In particular, every standard Dixmier trace of the positive critical power has this same value when defined by its generalized logarithmic mean.

## Assumptions and scope
The Hilbert space \(H_{c,\gamma}\) consists of holomorphic \(f(z)=\sum_{n\ge0} b_nz^n\) on the unit disk with
\[
\|f\|^2=\sum_{n\ge0}\beta_n|b_n|^2,\qquad
\beta_n=\exp[-c(\log(n+1))^\gamma].
\]
Its monomial orthonormal basis is \(e_n=z^n/\sqrt{\beta_n}\). As \(\beta_n^{1/n}\to1\), these functions are analytic in the disk. The maps \(C_{z^d}:f\mapsto f(z^d)\) are bounded contractions since the weights are nonincreasing. The singular values \(s_n\) are ordered decreasingly from \(n=1\). The coefficients \(a_d\) may have arbitrary complex phases. All limits keep \(c,\gamma,D,a_d\) fixed.

## Proof
**1. Exact monomial singular data.** For each fixed integer \(d\ge2\),
\[
C_{z^d}e_n=r_d(n)e_{dn},\qquad r_d(n)=\sqrt{\beta_{dn}/\beta_n}
=\exp[-\tfrac c2 F_d(n)],\quad F_d(x)=(\log(dx+1))^\gamma-(\log(x+1))^\gamma.
\]
The output basis vectors are mutually orthogonal for distinct \(n\), hence the nonzero singular values are precisely the decreasing rearrangement of \(r_d(0),r_d(1),\ldots\). For \(\gamma>1\), calculus yields
\[
F_d'(x)=\frac{\gamma(\gamma-1)\log d}{x}(\log x)^{\gamma-2}(1+o(1))>0,
\quad F_d(x)=\gamma(\log d)(\log x)^{\gamma-1}(1+O(1/\log x)).
\]
Consequently the \(r_d(n)\) are eventually decreasing, and \(s_n(C_{z^d})\sim r_d(n)\). Moreover, \(r_d(n)\to0\) exactly when \(\gamma>1\). When \(\gamma=1\), its limit is \(d^{-c/2}\); for \(0<\gamma<1\), its limit is \(1\).

**2. No cancellation can restore noncompactness below the first transition.** For \(n\ge1\), the output degrees \(dn\), \(d\in D\), are distinct, so
\[
\|Te_n\|^2=\sum_{d\in D}|a_d|^2r_d(n)^2
\longrightarrow
\begin{cases}\sum_{d\in D}|a_d|^2,&0<\gamma<1,\\
\sum_{d\in D}|a_d|^2d^{-c},&\gamma=1.
\end{cases}
\]
The orthonormal sequence \((e_n)\) is weakly null. Both limits are strictly positive, so \(T\) cannot be compact when \(\gamma\le1\). When \(\gamma>1\), every \(C_{z^d}\) is compact by step 1 and so is their finite sum.

**3. Singular-value dominance despite overlapping output ranges.** Suppose \(\gamma>1\), write \(A=a_{d_0}C_{z^{d_0}}\) and \(B=T-A\). If \(B=0\), the claim follows from step 1. Otherwise choose \(\theta\) satisfying
\[
\left(\frac{\log d_0}{\min_{d\in D\setminus\{d_0\}}\log d}\right)^{1/(\gamma-1)}<\theta<1.
\]
Using the fixed-sum singular-value inequality, the result in step 1 gives
\[
s_{\lfloor n^\theta\rfloor}(B)
\le\sum_{d\in D\setminus\{d_0\}}
|a_d|\,s_{\lfloor n^\theta/J\rfloor}(C_{z^d})
=o(s_n(A)),
\]
where \(J=|D|-1\). Indeed, the logarithm of each ratio is asymptotic to a strictly negative constant times \((\log n)^{\gamma-1}\), because \(\theta^{\gamma-1}\log d>\log d_0\). The finitely many integer-index shifts do not alter this conclusion.

For \(k_n=\lfloor n^\theta\rfloor\), the expansion of \(F_{d_0}\) and its derivative show that \(s_{n\pm k_n}(A)/s_n(A)\to1\). The two Ky Fan inequalities, applied to \(T=A+B\) and \(A=T-B\), give
\[
s_{n+k_n-1}(A)-s_{k_n}(B)\le s_n(T)
\le s_{n-k_n+1}(A)+s_{k_n}(B).
\]
Dividing by \(s_n(A)\) and passing to the limit proves \(s_n(T)\sim s_n(A)\sim |a_{d_0}|r_{d_0}(n)\). This argument handles all overlapping output degrees and all coefficient phases; it is not an orthogonality assertion about distinct columns.

**4. Sharp ideal boundaries and residue.** Set \(a=\log d_0>0\). The expansion from step 1 gives
\[
\log s_n(T)=-\tfrac{c\gamma a}{2}(\log n)^{\gamma-1}(1+o(1)).
\]
For \(1<\gamma<2\), this decay is slower than any fixed negative power of \(n\), so \(\sum_n s_n(T)^p=\infty\) for every finite \(p>0\). For \(\gamma>2\), it is faster than all powers, so every such sum converges. If \(\gamma=2\), the sharper expansion is
\[
s_n(T)\sim |a_{d_0}|e^{-ca^2/2}n^{-ca}.
\]
Therefore \(\sum_n s_n(T)^p<\infty\) exactly when \(pca>1\). At \(p_*=1/(ca)\),
\[
n\,s_n(T)^{p_*}\longrightarrow |a_{d_0}|^{p_*}\exp(-a/2)=|a_{d_0}|^{p_*}d_0^{-1/2}.
\]
The elementary logarithmic summation lemma for sequences \(u_n\sim K/n\) gives the claimed \(\log N\)-normalized limit. This establishes the measurable weak trace in the standard logarithmic-mean sense.

## Verification
The proof is analytical. The independent numerical routines in `CHECK.py` verify exact finite orthogonality/weight identities for several parameter sets, compare dense finite matrices against their column-squared norms, and test the explicitly predicted critical tail limit. These are diagnostics, not the proof of any infinite-dimensional statement.

## Relationship to prior work
Cruz-Zamorano, Dellepiane and Seco (2026) study equality of compact and Schatten symbol classes between weighted Hardy spaces and obtain abstract criteria for special weights; their introduction, operator definitions, weight characterization, principal theorems, and final questions do not give the singular values of finite sums of monomial composition operators on the logarithmic scales here. Their Hilbert--Schmidt identity supplies motivation but does not evaluate the non-orthogonal finite sum. Kriete and Moorhouse (2006) study compactness of finite linear combinations on classical Hardy/Bergman spaces, which are not these logarithmic coefficient spaces. Li, Wang and Zhao (2026) study compactness on Bergman--Orlicz spaces, not these exact singular-value asymptotics. Classical Ky Fan inequalities and elementary monomial data are used as inputs rather than claimed as new.

## Limitations
The logarithmic coefficient weight is specified exactly; the theorem does not give a general characterization for arbitrary weights or all composition symbols, nor a full singular-value asymptotic for noncompact \(\gamma\le1\). The compact-case proof assumes a fixed finite number of distinct monomial degrees, with nonzero lowest coefficient; infinitely many degrees or degree-dependent coefficients can invalidate spectral dominance. The critical residue is a limit of singular-value logarithmic sums, not an operator trace-class assertion. Literature comparisons establish no absolute publication priority; older equivalent operator-ideal statements may exist.

## References
- F. J. Cruz-Zamorano, E. Dellepiane, D. Seco, *Compact and Hilbert-Schmidt composition operators on weighted Hardy spaces*, arXiv:2610.40148v1 (publicly posted 2026-10-29), especially Sections 1, 2, 4--6.
- T. Kriete, J. Moorhouse, *Linear relations in the Calkin algebra for composition operators*, arXiv:math/0608466 (2006).
- Y. Li, Z. Wang, L. Zhao, *Compact linear combination of composition operators on Bergman-Orlicz spaces*, arXiv:2609.28111 (2026).
- G. Lechner, D. Li, H. Queffélec, L. Rodríguez-Piazza, *Approximation numbers of weighted composition operators*, J. Funct. Anal. 274 (2018), 1928--1958.
