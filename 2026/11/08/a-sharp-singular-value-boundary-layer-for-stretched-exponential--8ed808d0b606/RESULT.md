# A sharp singular-value boundary layer for stretched-exponential Aluthge iterates

## Finding

Let \(c>0\), \(\alpha>0\), \(0<t<1\), and let \(W\) be the compact unilateral weighted shift with weights \(\exp[-c(j+1)^\alpha]\), indexed by \(j\geq0\). For its generalized Aluthge iterates \(W_n=\Delta_t^n(W)\), put \(M_n=\|W_n\|\). For every \(0<p<\infty\), define the normalized singular-value mass
\[
B_{p,n}=\frac{\|W_n\|_{\mathcal S_p}^{p}}{M_n^{p}}.
\]
Then, as \(n\to\infty\),
\[
\boxed{B_{p,n}\sim
\begin{cases}
1,&\alpha>1,\\[3pt]
(1-e^{-pc})^{-1},&\alpha=1\quad\text{(in fact equality at every }n\text{)},\\[3pt]
\dfrac{t^{1-\alpha}}{pc\alpha}\,n^{1-\alpha},&0<\alpha<1.
\end{cases}}
\]
(The notation \(u_n\sim v_n\) means \(u_n/v_n\to1\).) For every \(n\ge0\), with \(X_n\sim\operatorname{Bin}(n,t)\), the complete ordered singular-value list is exactly
\[
\boxed{\ s_{j+1}(W_n)=\exp[-c\,\mathbb E(j+1+X_n)^\alpha],\quad j=0,1,2,\dots.\ }
\]
In particular, \(-\log M_n\sim c(tn)^\alpha\). In the stretched regime \(0<\alpha<1\), for each fixed \(u\ge0\),
\[
\boxed{\frac{s_{\lfloor u n^{1-\alpha}\rfloor+1}(W_n)}{M_n}
\longrightarrow \exp[-c\alpha t^{\alpha-1}u],}
\]
locally uniformly in \(u\in[0,\infty)\). In the compressed regime \(\alpha>1\), every fixed nonleading singular value is negligible compared with \(M_n\): \(s_{j+1}(W_n)/M_n\to0\) for every fixed \(j\ge1\). At \(\alpha=1\), the relative singular values are exactly \(e^{-cj}\) for all \(n\).

Equivalently, the proportion of the Schatten \(p\)-mass borne by the largest singular value tends to \(1\) for \(\alpha>1\), equals \(1-e^{-pc}\) for \(\alpha=1\), and is asymptotic to \(pc\alpha t^{\alpha-1}n^{\alpha-1}\) for \(0<\alpha<1\). Thus there is a sharp boundary at the ordinary exponential weight \(\alpha=1\), separating asymptotic rank-one concentration from a boundary layer of diverging effective singular-value count.

## Assumptions and scope

Work on complex \(\ell^2(\mathbb N_0)\), with orthonormal basis \((e_j)_{j\ge0}\) and \(We_j=\exp[-c(j+1)^\alpha]e_{j+1}\). All parameters \(c,\alpha\) are fixed positive reals, \(t\) is fixed strictly between zero and one, and \(p\) is any fixed positive real. For \(0<p<1\), \(\|\cdot\|_{\mathcal S_p}\) denotes the standard Schatten quasi-norm. The integer \(n\) tends to infinity with these parameters fixed. The operator is compact and belongs to every \(\mathcal S_p\) because its weights decrease superpolynomially. No claim is made about uniformity as \(p,t,c,\alpha\) vary or as \(t\) approaches the endpoints.

The transform is defined from the polar decomposition \(T=U|T|\) by \(\Delta_t(T)=|T|^tU|T|^{1-t}\). The expression for Aluthge iterated weights as binomially weighted geometric means is a known formula, appearing explicitly as equation (9) in Stanković's 2026 paper [3]. Its derivation below is for clarity, not a novelty claim.

## Proof

**1. Exact singular values.** Since all weights are strictly positive, the polar partial isometry is the unilateral isometric shift, while \(|W|\) is diagonal. A single generalized Aluthge step replaces the positive weight \(w_j\) by \(w_j^{1-t}w_{j+1}^t\). Iteration, Pascal's identity and the binomial theorem yield
\[
\log w_j^{(n)}=\sum_{k=0}^{n}\binom nk t^k(1-t)^{n-k}\log w_{j+k}
=-c\,\mathbb E(j+1+X_n)^\alpha.
\]
The function \(j\mapsto\mathbb E(j+1+X_n)^\alpha\) is strictly increasing. Hence the positive weights \(w_j^{(n)}\) already appear in decreasing order and form precisely the nonzero singular values of \(W_n\). Write \(F_n(j)=\mathbb E(j+1+X_n)^\alpha\) and \(D_n(j)=F_n(j)-F_n(0)\). The exact Schatten identity becomes
\[
B_{p,n}=\sum_{j=0}^{\infty}e^{-pc D_n(j)}.
\]
All these sums converge since \(D_n(j)\) tends to infinity at least like a positive multiple of \(j^\alpha\) for fixed \(n\).

**2. Logarithmic operator-norm decay.** The binomial law of large numbers gives \(X_n/n\to t\) in probability. The functions \(((1+X_n)/n)^\alpha\) are uniformly bounded for \(n\ge1\), so bounded convergence in probability gives \(F_n(0)/n^\alpha\to t^\alpha\). Thus \(-\log M_n=cF_n(0)\sim c(tn)^\alpha\).

**3. Compressed exponent \(\alpha>1\).** For every \(j\ge1\), the integral identity
\[
D_n(j)=\int_0^j\alpha\,\mathbb E(1+X_n+s)^{\alpha-1}\,ds
\]
shows that \(D_n(j)\ge\alpha j\), since \(1+X_n+s\ge1\). For each fixed \(j\ge1\), the same law of large numbers implies
\[
\frac{D_n(j)}{n^{\alpha-1}}\longrightarrow\alpha j t^{\alpha-1}>0.
\]
Consequently, \(e^{-pcD_n(j)}\to0\) for each \(j\ge1\), and it is bounded by the summable sequence \(e^{-pc\alpha j}\). Dominated convergence for the series gives \(B_{p,n}\to1\). The fixed-rank normalized singular-value limit follows from the same estimate.

**4. Critical exponent \(\alpha=1\).** In this case \(F_n(j)=j+1+nt\), so \(D_n(j)=j\) identically. Summing the geometric series yields \(B_{p,n}=(1-e^{-pc})^{-1}\) and \(s_{j+1}(W_n)/M_n=e^{-cj}\) for every \(n\).

**5. Stretched exponent \(0<\alpha<1\): local profile.** Define \(a_n=n^{1-\alpha}\). The binomial Chernoff bound implies that \(X_n\) lies between \(tn/2\) and \(3tn/2\) except on an event of probability \(O(e^{-\kappa n})\), for a constant \(\kappa>0\). For each fixed \(A>0\) and \(0\le s\le Aa_n\), the rescaled integrand equals \(((1+X_n+s)/n)^{\alpha-1}\). On the central event it is uniformly bounded and uniformly continuous in \(X_n/n\) and \(s/n\), and \(s/n\le A n^{-\alpha}\to0\). The binomial law of large numbers and bounded convergence in probability therefore yield uniform convergence of its expectations to \(t^{\alpha-1}\) on the central event. On the exceptional event, its expectation is at most \(n^{1-\alpha}O(e^{-\kappa n})\), since \((1+X_n+s)^{\alpha-1}\le1\). Consequently
\[
\sup_{0\le s\le Aa_n}\left|
 n^{1-\alpha}\mathbb E(1+X_n+s)^{\alpha-1}-t^{\alpha-1}
\right|\longrightarrow0.
\]
Integrating the derivative in Step 3 shows, uniformly for \(0\le u\le A\),
\[
D_n(\lfloor ua_n\rfloor)\longrightarrow\alpha t^{\alpha-1}u.
\]
Exponentiation proves the stated locally uniform normalized singular-value profile.

**6. Summable uniform tails and the sharp mass coefficient.** We establish the tail estimate needed to pass from the local profile to the full Schatten sum. As \(\alpha-1<0\) and \(X_n\le n\), for \(0\le j\le n\),
\[
D_n(j)=\mathbb E\!\int_0^j\alpha(1+X_n+s)^{\alpha-1}ds
\ge\alpha j(2n+1)^{\alpha-1}.
\]
Hence, for any \(A>0\), the part of the sum over \(Aa_n<j\le n\), divided by \(a_n\), is bounded for large \(n\) by \(C e^{-c_0A}\), with positive constants \(C,c_0\) depending only on the fixed parameters. To control \(j>n\), concavity shows that \((x+j)^\alpha-x^\alpha\) decreases in \(x\). Since \(X_n+1\le n+1\),
\[
D_n(j)\ge(n+j+1)^\alpha-(n+1)^\alpha.
\]
For \(n<j<2n\), the right side exceeds \(\kappa_1 n^\alpha\). For \(j\ge2n\) and \(n\ge2\), one has \(n+1\le3j/4\), and the right side exceeds \(\kappa_2j^\alpha\), where \(\kappa_1,\kappa_2>0\) depend on \(\alpha\). Elementary comparison with \(\int_{2n}^\infty e^{-pc\kappa_2x^\alpha}dx\) therefore gives
\[
\frac1{a_n}\sum_{j>n}e^{-pcD_n(j)}\longrightarrow0.
\]
The local convergence of Step 5, viewed as a Riemann sum on \([0,A]\), together with these tail bounds and then \(A\to\infty\), proves
\[
\lim_{n\to\infty}\frac{B_{p,n}}{n^{1-\alpha}}
=\int_0^\infty e^{-pc\alpha t^{\alpha-1}u}du
=\frac{t^{1-\alpha}}{pc\alpha}.
\]
All three regimes and their normalized mass proportions follow.

## Verification

The accompanying standalone `check.py` computes binomial probabilities, compares the binomial expectation formula against direct repeated transforms on finite initial weight segments, tests the exact critical case, and compares finite Schatten masses with their predicted asymptotic regimes. It passed **582 finite diagnostic assertions** using standard Python. These checks do not certify the infinite-dimensional claims; Steps 1–6 above supply the proof. For reproduction, execute `python check.py` with Python 3 and its standard library. The relative tolerance used in the noncritical finite-rate tests is deliberately coarse because the theorem claims asymptotics rather than a finite-step error estimate.

## Relationship to prior work

Pal and Chandok [1] prove generalized-Aluthge-related weighted Schatten numerical-radius inequalities, not the normalized singular-value mass or the boundary-layer trichotomy above. Bala [2] studies norm convergence of compact-operator Aluthge iterates. Stanković [3], made publicly available on November 5, 2026, proves that every unilateral weighted shift in a Schatten class has Aluthge iterates whose Schatten quasi-norm tends to zero, and records the exact binomial geometric-mean formula (Proposition 5.8, equation (9)). The present finding **does not claim** either that binomial formula or unnormalized convergence as new. Instead it identifies the three sharp and mutually different normalized asymptotic regimes, the complete limiting stretched-regime profile and its constant. Dykema and Schultz [4] study binomially weighted ergodic averaging and a finite-von-Neumann-algebra Aluthge setting, without this compact unilateral-shift Schatten mass classification.

## Limitations

The result assumes a strictly positive stretched-exponential weight profile and a fixed interior transform parameter. It is not a classification of arbitrary compact shifts, nonsmooth weight profiles, or operators with multiplicity. The result does not provide a uniform error bound in all parameters. The value of the theorem depends on the precise normalized singular-value distribution; it should not be confused with the pre-existing qualitative conclusion that all unnormalized singular values vanish. Further literature may contain a broader regularly varying or binomial-smoothing theorem implying this specialized trichotomy. Independent review has not been performed.

## References

1. K. Pal and S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336, first posted 2026-10-08. https://arxiv.org/abs/2610.11336
2. N. Bala, *The iterated Aluthge Transforms of compact operators*, arXiv:2602.07916, first posted 2026-02-08. https://arxiv.org/abs/2602.07916
3. H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728, first posted 2026-11-05; especially Proposition 5.8 and its equation (9). https://arxiv.org/html/2611.07728v1
4. K. Dykema and H. Schultz, *Brown measure and iterates of the Aluthge transform for some operators arising from measurable actions*, arXiv:math/0512197, first posted 2005-12-09. https://arxiv.org/html/math/0512197v4
