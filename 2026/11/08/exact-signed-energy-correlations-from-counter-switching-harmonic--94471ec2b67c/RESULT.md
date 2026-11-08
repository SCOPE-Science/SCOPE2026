# Exact signed energy correlations from counter-switching harmonic confinement

## Finding

Let two noninteracting Brownian particles experience a shared stationary, two-state Markov environment, but allow their harmonic spring constants to respond differently in the two states. Their ordinary positional covariance is zero, whereas their connected four-point correlation, equivalently the covariance of their squared positions, has a **complete signed classification**: it is strictly positive when their two stiffness changes have the same sign, strictly negative when the changes have opposite signs, and vanishes precisely when at least one particle has state-independent stiffness. This holds for arbitrary positive transition rates, positive stiffnesses, and independent positive thermal diffusivities.

More precisely, write the four doubled stiffnesses as \(a,b,c,d>0\), with \((a,b)\) for particle 1 and \((c,d)\) for particle 2, and let the shared environment switch \(0\to1\) at rate \(p>0\) and \(1\to0\) at rate \(q>0\). With diffusion constants \(D_1,D_2>0\), define

\[
\begin{aligned}
K_1&=ab+aq+bp,\\
K_2&=cd+cq+dp,\\
K_{12}&=(a+c)(b+d)+(a+c)q+(b+d)p,\\
N&=ab+ad+ap+2aq+bc+2bp+bq+cd+cp+2cq+2dp+dq+2(p+q)^2.
\end{aligned}
\]

Then the exact joint fourth cumulant is

\[
\boxed{\kappa(X_1,X_1,X_2,X_2)=
\frac{4D_1D_2pq(a-b)(c-d)N}{(p+q)^2K_1K_2K_{12}}.}
\]

All factors except \((a-b)(c-d)\) are strictly positive. In particular the sign, including its exact zero boundary, does not depend on the transition-rate ratio or on either diffusion constant. The positions obey \(\operatorname{Cov}(X_1,X_2)=0\) identically despite the generally nonzero joint fourth cumulant.

## Assumptions and scope

Fix four stiffness coefficients \(\mu_{1,0},\mu_{1,1},\mu_{2,0},\mu_{2,1}>0\) and \(D_1,D_2,p,q>0\). Let \(S_t\in\{0,1\}\) be a stationary, irreducible, continuous-time Markov chain with rates \(p\) from 0 to 1 and \(q\) from 1 to 0. Let \(W_1,W_2\) be independent standard two-sided Brownian motions independent of the environment. The unique stationary solutions are

\[
dX_i(t)=-\mu_{i,S_t}X_i(t)\,dt+\sqrt{2D_i}\,dW_i(t),\qquad i=1,2.
\]

Set \(a=2\mu_{1,0}\), \(b=2\mu_{1,1}\), \(c=2\mu_{2,0}\), and \(d=2\mu_{2,1}\). The random variables \(X_i\) in the theorem denote their positions at the same arbitrary stationary time. The theorem concerns zero-mean, independent-noise particles without direct pairwise forces. It makes no general statement for a multi-state environmental chain, cross-correlated Brownian noises, or state-dependent diffusion constants.

## Proof

**Stationarity and conditional Gaussian reduction.** Since every \(\mu_{i,s}\) is positive, the stationary convolution

\[
X_i(t)=\sqrt{2D_i}\int_{-\infty}^{t}
\exp\left[-\int_u^t\mu_{i,S_v}\,dv\right]dW_i(u)
\]

exists in \(L^2\), is the unique stationary solution, and has finite moments of every order. Conditioned on the complete environmental history, the two positions are independent centered Gaussians with strictly positive random variances \(V_i(t)\) solving

\[
\dot V_1=2D_1-\lambda_{1,S_t}V_1,\qquad
\dot V_2=2D_2-\lambda_{2,S_t}V_2,
\]

where \(\lambda_{1,0}=a\), \(\lambda_{1,1}=b\), \(\lambda_{2,0}=c\), and \(\lambda_{2,1}=d\). Hence

\[
\operatorname{Cov}(X_1,X_2)=0,
\quad
\kappa(X_1,X_1,X_2,X_2)=\operatorname{Cov}(V_1,V_2).
\]

The last identity follows from the definition of a fourth cumulant, conditional Gaussian independence, and the vanishing position covariance.

**Exact stationary moment equations.** Let \(\pi=(q,p)^\mathsf{T}/(p+q)\), and define the column vectors of unnormalized state-conditional moments

\[
U_s=\mathbb E[V_1\mathbf1_{\{S=s\}}],\quad
T_s=\mathbb E[V_2\mathbf1_{\{S=s\}}],\quad
Z_s=\mathbb E[V_1V_2\mathbf1_{\{S=s\}}].
\]

The joint generator of \((S,V_1,V_2)\), applied successively to \(V_1\), \(V_2\), and \(V_1V_2\) in each state, gives

\[
\begin{aligned}
\begin{pmatrix}a+p&-q\\-p&b+q\end{pmatrix}U&=2D_1\pi,\\
\begin{pmatrix}c+p&-q\\-p&d+q\end{pmatrix}T&=2D_2\pi,\\
\begin{pmatrix}a+c+p&-q\\-p&b+d+q\end{pmatrix}Z&=2D_1T+2D_2U.
\end{aligned}
\]

Each matrix is invertible because its determinant is respectively \(K_1\), \(K_2\), and \(K_{12}\), all strictly positive. In particular,

\[
\operatorname{Cov}(V_1,V_2)
=(Z_0+Z_1)-(U_0+U_1)(T_0+T_1).
\]

**Factoring the sign.** Put \(k=p+q\). By the two-by-two inverse formula,

\[
\begin{aligned}
U&=\frac{2D_1}{kK_1}\binom{q(b+k)}{p(a+k)},\\
T&=\frac{2D_2}{kK_2}\binom{q(d+k)}{p(c+k)}.
\end{aligned}
\]

After substituting these two expressions into the third equation, clearing the common denominator \(k^2K_1K_2K_{12}\) in \(\operatorname{Cov}(V_1,V_2)/(4D_1D_2)\), the numerator becomes

\[
\begin{aligned}
R={}&k\big[q(b+d+k)((d+k)K_1+(b+k)K_2)\\
&\hspace{18mm}+p(a+c+k)((c+k)K_1+(a+k)K_2)\big]\\
&-(qb+pa+k^2)(qd+pc+k^2)K_{12}.
\end{aligned}
\]

Direct expansion establishes the exact **polynomial identity** \(R=pq(a-b)(c-d)N\). This is not a numerical extrapolation: the standalone standard-library `algebra_certificate.py` represents both polynomials as integer-coefficient monomial dictionaries and checks their 51 coefficients exactly. Thus the displayed rational formula follows for every parameter tuple in the domain. The positive-term expression for \(N\) proves \(N>0\). Consequently the covariance has sign \(\operatorname{sgn}((a-b)(c-d))\), and it vanishes if and only if \(a=b\) or \(c=d\). This also proves the claimed classification for the fourth cumulant.

As a concrete counter-switching instance, \((a,b,c,d,p,q,D_1,D_2)=(1,4,5,2,2,3,1,1)\) gives the exact negative covariance \(-192/3625\). With \((c,d)=(2,5)\) and the remaining parameters unchanged it instead equals \(328/4875>0\).

## Verification

The attached `algebra_certificate.py` checks the universal numerator polynomial identity coefficientwise using exact integer arithmetic (51 monomials on each side). The attached `verify.py` independently implements the three moment equations with exact rational two-by-two elimination and separately evaluates the factorized formula. Running `python verify.py` requires only the Python standard library. It checks **1,536** tuples of strictly positive rational parameters, including degenerate equal-stiffness boundaries, both strict signs, multiple transition asymmetries, and non-unit diffusion strengths; every equality and sign assertion passes. The infinite-parameter theorem is justified by the preceding symbolic matrix identity and strict positivity, not by this finite enumeration.

## Relationship to prior work

Biroli, Kulkarni, Majumdar and Schehr (arXiv:2312.02570, first posted 2023-12-05) establish a joint distribution and positive squared-position correlation for **identical** noninteracting particles sharing the same two-state harmonic trap (their Eqs. 12–14). The present heterogeneous sign result extends the natural physical question to particles responding in opposite directions to the same environmental switch, a case not covered by their common-variance representation.

Huang, Jansen, Mandjes, Spreij and De Turck (arXiv:1412.7952, first posted 2014-12-26) already define the broader multi-component Markov-modulated Ornstein–Uhlenbeck model with a common finite-state environment. Their Section 6.1 proves conditional Gaussianity, and Section 6.4 gives a general stationary **mixed-moment recursion**. Thus the present model and the ability in principle to calculate its fourth moments are known. The additional mathematical statement assessed here is the **explicit rate-uniform sign factorization and exact zero-boundary classification** for heterogeneous two-state confinement, not a new model, a new conditional-independence lemma, or a general-purpose moment recursion. The 2014 recursion is a substantial antecedent and a limitation on claims of novelty.

## Limitations

This proves a stationary equal-time signed fourth cumulant for a two-state environment with fixed diffusion strengths and independent thermal noises. It does not imply a sign law for the ordinary positional correlation beyond the asserted zero, for conditional mutual information, for arbitrary multi-state modulation, or for higher connected cumulants. The explicit covariance is a new derived specialization of an established general moment-recursion framework; the mathematical record may contain a previously unindexed equivalent sign factorization, and independent scientific validation is not claimed.

## References

1. M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570, first posted 2023-12-05, https://arxiv.org/abs/2312.02570 . See Eq. 2 and Eqs. 12–14.
2. G. Huang, H. M. Jansen, M. Mandjes, P. Spreij, K. De Turck, *Markov-modulated Ornstein–Uhlenbeck processes*, arXiv:1412.7952, first posted 2014-12-26, https://arxiv.org/abs/1412.7952 . See Sections 6.1–6.4, especially the mixed-moment recursion.
