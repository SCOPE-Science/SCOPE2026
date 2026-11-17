# Exact Markov sign dynamics with a hidden directed covariance mode in a paired tent map

## Finding

For the symmetric paired tent map at equal leakage parameters \(a=b=1/2\), the stationary left/right sign observation is **exactly** a symmetric two-state Markov chain, not merely an asymptotic metastable approximation. At the same time, the full coordinate \(X_n\) reveals a strictly directed pair-correlation asymmetry hidden from that coarse chain.

Let \(X_0\) have the stationary absolutely continuous probability described below, \(X_n=T^n(X_0)\), and \(S_n=\operatorname{sgn}(X_n)\). For each integer \(n\geq0\),

\[
\mathbb E[S_0S_n]=3^{-n},\qquad
\mathbb E[X_0X_n]=\tfrac14\,3^{-n},
\]

and

\[
\mathbb E[X_0S_n]=\frac{1}{3^{n+1}}+\frac{(-1)^n}{12\cdot9^n},
\qquad
\mathbb E[S_0X_n]=\begin{cases}5/12,&n=0,\\(3/4)3^{-n},&n\geq1.\end{cases}
\]

In particular, for every \(n\geq1\), the strictly positive directed covariance defect is

\[
\boxed{\mathbb E[S_0X_n]-\mathbb E[X_0S_n]
=\frac5{12}\,3^{-n}-\frac1{12}(-1/9)^n>0.}
\]

Thus a reversible two-state sign observation can coexist with unequal forward/reverse sign–coordinate correlations. The component \((-1/9)^n\) is an exact hidden decay mode that disappears from both marginal autocovariance sequences. The corresponding sign-sum central limit variance is \(2\); the asymptotic variance rate of coordinate sums is \(1/2\).

## Assumptions and scope

The deterministic piecewise affine map \(T:[-1,1]\to[-1,1]\) is

\[
T(x)=\begin{cases}
3x+2,&-1\leq x\leq-1/2,\\
-3x-1,&-1/2<x<0,\\
0,&x=0,\\
-3x+1,&0<x\leq1/2,\\
3x-2,&1/2<x\leq1.
\end{cases}
\]

This is the \(a=b=1/2\) specialization of the standard paired tent family [1]. Both turning-point images cycle: \(T(-1/2)=1/2\) and \(T(1/2)=-1/2\), explaining the natural finite partition. Define the four open cells, in increasing order, by

\[
I_1=(-1,-1/2),\quad I_2=(-1/2,0),\quad I_3=(0,1/2),\quad I_4=(1/2,1).
\]

The stationary initial law \(\mu\) has density

\[
h(x)=\begin{cases}1/3,&1/2<|x|<1,\\2/3,&0<|x|<1/2.\end{cases}
\]

Values on finitely many boundaries are immaterial for \(\mu\)-almost-sure statistics; the map is not claimed to be invertible or random. Both \(X_n\) and \(S_n\) have mean zero.

## Proof

**1. Four-cell Markov structure and stationary law.** Every restriction of \(T\) to a cell is an affine bijection onto a union of whole target cells. The successive target sets for sources \(I_1,I_2,I_3,I_4\) are respectively \(\{1,2,3\}\), \(\{1,2,3\}\), \(\{2,3,4\}\), \(\{2,3,4\}\). Because each cell has length \(1/2\) and the absolute slope is \(3\), the stationary cell itinerary has stochastic matrix

\[
P=\frac13\begin{pmatrix}1&1&1&0\\1&1&1&0\\0&1&1&1\\0&1&1&1\end{pmatrix},
\qquad
\pi=(1/6,1/3,1/3,1/6).
\]

The density above is constant within each cell; substituting it in the Perron–Frobenius formula gives exactly \(\mathcal Lh=h\), and its cell masses are \(\pi\). All entries of \(P^2\) are positive. The Markov expansion therefore has a mixing stationary absolutely continuous law; the piecewise affine expanding Markov map has this unique absolutely continuous invariant probability by the standard primitive Markov/Lasota–Yorke argument. Conditional density within a cell, even after any positive-probability finite itinerary history, is uniform, since all admissible branch images cover whole target cells affinely. This proves the actual deterministic cell itinerary is the stationary Markov chain \(P\), not just a matrix approximation.

**2. Exact sign Markovization.** The first two source rows of \(P\) both assign probability \(2/3\) to the left half and \(1/3\) to the right half. The last two rows both assign probability \(1/3\) to the left and \(2/3\) to the right. This strong lumpability yields the exact sign-transition matrix, ordered left then right,

\[
Q=\begin{pmatrix}2/3&1/3\\1/3&2/3\end{pmatrix},
\qquad \mathbb P(S_0=s_0,\ldots,S_n=s_n)=\frac12\prod_{j=1}^nQ_{s_{j-1},s_j}.
\]

The sign chain is stationary, symmetric and reversible. Its nontrivial eigenvalue is \(1/3\), giving \(\mathbb E[S_0S_n]=3^{-n}\) and the standard finite-state Markov-chain central limit theorem with variance \(1+2\sum_{n\geq1}3^{-n}=2\).

**3. Affine-density transfer and exact cross-statistics.** To retain the position within each cell rather than merely its label, consider densities \(g|_{I_j}(x)=A_j+B_jx\), an eight-dimensional invariant space for \(\mathcal L\). Use the affine branches \(T|_{I_j}(x)=s_jx+d_j\) with

\[
(s_1,s_2,s_3,s_4)=(3,-3,-3,3),\qquad
(d_1,d_2,d_3,d_4)=(2,-1,1,-2).
\]

Let \(J_1=\{1,2\}\), \(J_2=J_3=\{1,2,3,4\}\), \(J_4=\{3,4\}\) be the incoming sources. Then, directly by inverse-branch substitution, the coefficient update is

\[
A'_i=\frac13\sum_{j\in J_i}\left(A_j-\frac{d_j}{s_j}B_j\right),
\qquad B'_i=\frac13\sum_{j\in J_i}\frac{B_j}{s_j}.
\]

This defines an explicit rational eight-by-eight matrix \(L\), whose characteristic polynomial is

\[
\det(\lambda I-L)=\frac{\lambda^4(\lambda-1)(3\lambda-1)(9\lambda-1)(9\lambda+1)}{243}.
\]

For observable \(f\in\{x,\operatorname{sgn}x\}\) and initial observable multiplier \(g\in\{x,\operatorname{sgn}x\}\), take the piecewise affine initial density \(gh\), apply \((I-zL)^{-1}\), and integrate against \(f\) on the four cells. Elementary polynomial antiderivatives give the **four exact** generating functions (all expressions mean their Taylor expansions about \(z=0\)):

\[
\begin{aligned}
\sum_{n\ge0}z^n\mathbb E[X_0X_n]&=\frac3{4(3-z)},\\
\sum_{n\ge0}z^n\mathbb E[S_0S_n]&=\frac3{3-z},\\
\sum_{n\ge0}z^n\mathbb E[S_0X_n]&=\frac{4z+15}{12(3-z)},\\
\sum_{n\ge0}z^n\mathbb E[X_0S_n]&=\frac{z+45}{4(3-z)(9+z)}.
\end{aligned}
\]

Partial fractions give the displayed all-lag formulas. For \(n\ge1\), positivity of the directed defect is immediate: \(5\cdot3^{-n}>|(-1/9)^n|\). In particular \(\mathbb E[S_0X_1]-\mathbb E[X_0S_1]=4/27\). While the sign process itself is reversible, the pair \((X,S)\) has a detectable directional covariance asymmetry. No claim of a new general time-reversal theorem is made.

**4. Finite-window variances.** Stationarity, zero means and the two marginal autocorrelation formulas yield, for each integer \(N\ge1\),

\[
\operatorname{Var}\!\left(\sum_{j=0}^{N-1}S_j\right)
=2N-\frac32(1-3^{-N}),\quad
\operatorname{Var}\!\left(\sum_{j=0}^{N-1}X_j\right)
=\frac N2-\frac38(1-3^{-N}).
\]

These are finite identities, not inferences from finite enumeration. Dividing by \(N\) proves the variance rates \(2\) and \(1/2\), respectively. Only the sign-sum Gaussian limit is asserted; it follows from its exact finite-state Markov representation.

## Verification

The independent symbolic calculation `verify_paired.py` reconstructs the four source images, the stochastic transition matrix, the stationary density, and the complete eight-dimensional affine-density transfer operator using rational arithmetic. It checks the four rational generating functions as algebraic identities, the spectrum, all four correlations at lags \(0\) through \(15\), sign lumpability, strict direction at each tested lag, and exact finite-window variances for \(1\le N\le10\). Run `python verify_paired.py` with SymPy. The hand proof above, rather than those finite checks alone, establishes all-lag identities.

## Relationship to prior work

González-Tokman and Peters [1, §8] define precisely this two-parameter paired-tent family and establish asymptotic metastable averaging of invariant densities as leakage tends to zero. Their inspected §8 does not calculate the finite-leakage sign-word law or directed mixed correlations. Horan [2, §4.6] introduced the underlying family and finite transfer ideas, and his later dissertation [3, Chapter 5] works out a sequence of Markov parameters strictly below \(1/2\). The first Markov parameter \(q=(\sqrt3-1)/2\) is distinct from the present critical two-cycle value \(1/2\); published analysis of its sign observable finds it is *not* one-step Markov [4]. The present value therefore gives a contrasting, exactly lumpable coarse observation and the independent exact mixed-statistic mode, without asserting novelty of the map, Markov partitions, primitive-chain CLTs or transfer operators themselves.

The stronger 2026 diffusion study [5, §7] applies general small-leakage diffusion/CLT results to random paired tent maps. Those do not provide the present finite-parameter rational covariance functions or exact first-order sign-word law. Searching for mathematical equivalents and stronger results did not identify a published expression of this specific joint exact statistic, but absence of a match is not a proof of publication priority.

## Limitations

All identities require the **fixed deterministic** choice \(a=b=1/2\) and initial distribution \(\mu\). They do not describe other leakage values, driven/random switching, arbitrary initial measures, higher-order joint coordinate laws, or the global classification of stationary measures (atomic periodic measures also exist). At the chosen parameter the finite Markov reduction is especially simple; the resulting formulas are model-specific. A pre-existing treatment of this exact critical parameter or a universal formula implying these directional cross-correlations would supersede the novelty assessment. Independent verification is not claimed.

## References

1. C. González-Tokman and J. Peters, *Averaging for random metastable systems*, arXiv:2406.09672, first publicly posted 2024-06-14, §8. https://arxiv.org/abs/2406.09672
2. J. Horan, *Asymptotics for the second-largest Lyapunov exponent for some Perron–Frobenius operator cocycles*, arXiv:1910.12112, first posted 2019-10-26. https://arxiv.org/abs/1910.12112
3. J. Horan, *Spectral gap and asymptotics for a family of cocycles of Perron–Frobenius operators*, Ph.D. thesis, University of Victoria, 2020, Chapter 5. https://dspace.library.uvic.ca/bitstreams/8562f6eb-cc75-497a-8f7f-299b114ec884/download
4. *Exact oscillatory sign memory and a finite-leakage diffusion coefficient for a paired tent map*, 2026, result at \(q=(\sqrt3-1)/2\). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-oscillatory-sign-memory-and-a-finite-leakage-diffusion-coe--2072573574e5
5. *Jumping for Diffusion in Random Metastable Systems*, *Annales Henri Poincaré* (2026), §7, doi:10.1007/s00023-026-01738-4. https://doi.org/10.1007/s00023-026-01738-4
