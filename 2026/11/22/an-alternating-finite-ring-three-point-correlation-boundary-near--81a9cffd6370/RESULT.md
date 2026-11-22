# An alternating finite-ring three-point correlation boundary near fugacity two

## Finding

Consider a homogeneous hard-core lattice gas on the simple cycle \(C_{3m+1}\), with integer \(m\ge2\) and strictly positive common fugacity \(\lambda\). Let \(X_j\) be the indicator that site \(j\) is occupied, with vertices indexed modulo \(3m+1\). The three marked sites are \(0,m,2m\), whose successive circular gaps are \(m,m,m+1\). Their connected third moment is
\[
K_m(\lambda)=\mathbb E[(X_0-\mathbb EX_0)(X_m-\mathbb EX_m)(X_{2m}-\mathbb EX_{2m})].
\]

For every \(m\ge2\), this third moment is strictly positive at all sufficiently small positive fugacities, strictly negative at all sufficiently large fugacities, and therefore has at least one positive-fugacity sign crossing. At the same fixed fugacity \(\lambda=2\), its sign alternates **exactly** with ring size:
\[
\operatorname{sgn}K_m(2)=(-1)^{m+1}.
\]
For all sufficiently large \(m\), there is exactly one crossing in a fixed neighborhood of \(\lambda=2\). Denote its fugacity by \(\lambda_m\). It obeys the quantitative parity-split finite-size law
\[
\lambda_m=2-\frac32(-1)^m2^{-m}+O(m4^{-m}).
\]
In particular this local crossing lies below \(2\) for large even \(m\) and above \(2\) for large odd \(m\). The theorem does **not** assert that the complete positive-fugacity root set has cardinality one for every finite \(m\).

## Assumptions and scope

The allowed configurations are all independent vertex sets of \(C_{3m+1}\), each weighted by \(\lambda^{|S|}\); expectations refer to the normalized finite-volume Gibbs law. There is no limit on particle count apart from nearest-neighbor exclusion. The three indicators concern distinct sites for every \(m\ge2\). Equivalently, the model is a monomer–dimer matching gas on a cycle with the three observables recording occupation of specified edges. The statement is about equal fugacities, the indicated nearly equally spaced triple, and finite-volume cumulants. The symbol \(O(m4^{-m})\) means a bound by a universal constant times \(m4^{-m}\) for all sufficiently large integers \(m\).

## Proof

Set \(t\in(0,1)\) by \(\lambda=t/(1-t)^2\). Introduce the symmetric transfer matrix and occupied-state projector
\[
T=\begin{pmatrix}1&\sqrt\lambda\\\sqrt\lambda&0\end{pmatrix},\qquad P=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
The eigenvalues of \(T\) are \(\alpha=(1-t)^{-1}\) and \(\beta=-t(1-t)^{-1}\). Direct spectral projection gives
\[
Z_n=\operatorname{tr}T^n=\alpha^n(1+(-t)^n),\qquad
\langle1|T^d|1\rangle=\frac{\alpha^d(t+(-t)^d)}{1+t}.
\]
For three prescribed marked sites whose cyclic gap lengths are \(a,b,c\), the joint occupancy probability equals \(\langle1|T^a|1\rangle\langle1|T^b|1\rangle\langle1|T^c|1\rangle/Z_{a+b+c}\). The corresponding one- and two-point functions follow from the same identity with one or two projectors. Thus, writing \(q=1+(-t)^{3m+1}\), \(r=(-t)^m\), and \(f_d=(t+(-t)^d)/(1+t)\),
\[
\begin{aligned}
p_1&=f_{3m+1}/q,\\
p_{2,m}&=f_mf_{2m+1}/q,\\
p_{2,m+1}&=f_{m+1}f_{2m}/q,\\
p_3&=f_m^2f_{m+1}/q,\\
K_m&=p_3-p_1(2p_{2,m}+p_{2,m+1})+2p_1^3.
\end{aligned}
\]
Expanding and collecting these four explicit rational functions yields the exact factorization
\[
(1+t)^3q^3 K_m=-r^2t(r-1)(t-1)H_m(t),
\]
where
\[
H_m(t)=r^4t^3-2r^4t^2-r^3t+2r^2t^2-2r^2t+rt^2+2t-1.
\]
Because \(r<1\), \(t<1\), and the denominator is positive, the sign of \(K_m\) is the opposite of the sign of \(H_m\). As \(t\downarrow0\), \(H_m(t)\to-1\), proving positive low-fugacity cumulants. At \(t=1\), \(H_m(1)=0\), and explicit differentiation (including the derivative of \(r=(-t)^m\)) gives
\[
H'_m(1)=\begin{cases}4-6m,&m\text{ even},\\2-2m,&m\text{ odd} .\end{cases}
\]
This is strictly negative for every \(m\ge2\). Hence \(H_m(t)>0\) sufficiently close to \(1\) from below, giving a strictly negative high-fugacity cumulant. Continuity proves at least one sign crossing.

At \(t=1/2\), let \(a=2^{-m}\) and \(\varepsilon=(-1)^m\). Direct substitution gives
\[
H_m(1/2)=\frac{\varepsilon a}{4}-\frac{a^2}{2}-\frac{\varepsilon a^3}{2}-\frac{3a^4}{8}.
\]
If \(m\) is even, then \(a\le1/4\) and the right side is strictly positive. If \(m\) is odd, then \(a\le1/8\) and it is strictly negative. Since \(t=1/2\) corresponds to \(\lambda=2\), the stated exact alternating sign follows.

Finally, on the fixed interval \([2/5,3/5]\), the functions \(H_m(t)\) converge uniformly together with their first derivatives to \(2t-1\). Hence for all sufficiently large \(m\) there is exactly one simple zero \(t_m\) in this interval. Expanding the explicit polynomial around \(t=1/2\),
\[
H_m(1/2)=\frac{(-1)^m2^{-m}}4+O(4^{-m}),\qquad
H'_m(1/2)=2+O(m2^{-m}),
\]
so the intermediate-value theorem and Taylor's formula, uniformly on the resulting \(O(2^{-m})\) neighborhood, yield
\[
t_m=\frac12-\frac{(-1)^m2^{-m}}8+O(m4^{-m}).
\]
The derivative of \(t/(1-t)^2\) at \(t=1/2\) equals \(12\); substitution proves the asserted formula for \(\lambda_m\). These steps are analytic statements for all eligible integers, not extrapolations from finite enumeration.

## Verification

The standalone standard-library program `verify_cyclic_cumulant.py` independently enumerates allowed occupied subsets, computes exact-rational one-, two- and three-site moments, and compares them against the transfer-matrix formula and the fully factored expression at five rational parameter values for each of four cycle sizes. It separately checks more transfer identities and the sign at \(\lambda=2\) through \(m=12\). Run `python3 verify_cyclic_cumulant.py` from the same directory. The program reports `CYCLIC_THIRD_CUMULANT_EXACT_OK 64 checks`. These finite tests supplement, but do not replace, the all-size analytic proof above.

## Relationship to prior work

Scott and Sokal [1], Section 3.2 (especially their Examples 3.2 and 3.3), give the classical path and cycle independent-set partition polynomials and the transfer-matrix framework; these identities are used here as known ingredients. Their statements do not classify the sign of the third connected occupation moment for the specified three positions, nor its alternating finite-size crossing displacement. Tokar and Dreyssé [2] solve a different one-dimensional lattice-gas cluster-size problem in the canonical, infinite-system setting. Tanaka, Morita and Hiroike [3] analyze direct and total two-point correlations for longer-range one-dimensional interactions at fixed density; the accessible abstract does not settle the finite-ring three-site comparison. Prior pair-observable results on cyclic monomer–dimer models do not determine a third cumulant, which involves an independent three-site joint probability and cancellation of lower moments.

## Limitations

No global uniqueness assertion is made about all positive roots of \(K_m\) at arbitrary finite \(m\). The analysis is restricted to nearest-neighbor exclusion, equal activities, and the particular triple with gaps \(m,m,m+1\); it does not establish a thermodynamic phase transition. The finite-volume cumulant itself decays rapidly as the marked sites separate. Earlier unindexed derivations of the same special three-point formula are a residual historical-priority risk. No independent external validation has been performed.

## References

[1] A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, arXiv:cond-mat/0309352, first public version 2003-09-15, https://arxiv.org/abs/cond-mat/0309352 .

[2] V. I. Tokar and H. Dreyssé, *Analytical solution of 1D lattice gas model with infinite number of multiatom interactions*, arXiv:cond-mat/0210582, first public version 2002-10-25, https://arxiv.org/abs/cond-mat/0210582 .

[3] K. Tanaka, T. Morita and K. Hiroike, *Correlation Functions of a One-Dimensional Lattice Gas with Interactions Up to Third-Nearest Neighbors*, Progress of Theoretical Physics Supplement 87 (1986), 214–228, https://doi.org/10.1143/PTPS.87.214 .
