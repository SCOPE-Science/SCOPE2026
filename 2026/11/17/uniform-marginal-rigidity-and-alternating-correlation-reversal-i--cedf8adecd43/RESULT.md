# Uniform-marginal rigidity and alternating correlation reversal in a periodic threshold neuron

## Finding

The McCulloch–Pitts scalar recurrence with alternating gains admits exactly two *genuinely period-two* gain choices in the natural interval \([1,2]^2\) for which normalized Lebesgue measure on \((-1,1)\) is preserved at **each** of its two phases. These choices are \((\beta_0,\beta_1)=(2,1)\) and \((1,2)\). Despite identical uniform one-time marginals, their phase-resolved temporal correlations have opposite signs.

For the ordering \((2,1)\), let \(U\) be uniform on \((-1,1)\), set \(X_0=U\), and iterate
\[
X_{n+1}=\beta_n X_n-\operatorname{sgn}(X_n),\qquad
\beta_{2j}=2,\quad \beta_{2j+1}=1.
\]
Write \(C_{\mathrm e}(k)=\mathbb E[X_{2j}X_{2j+k}]\) and \(C_{\mathrm o}(k)=\mathbb E[X_{2j+1}X_{2j+1+k}]\), where the values are independent of \(j\ge0\). Then \(C_{\mathrm e}(0)=C_{\mathrm o}(0)=1/3\), and, for every integer \(m\ge0\),
\[
\begin{aligned}
C_{\mathrm e}(2m+1)&=\frac{1}{3\,2^{m+1}}, &
C_{\mathrm o}(2m+1)&=-\frac{1}{6\,2^m},\\
C_{\mathrm e}(2m+2)&=-\frac{1}{6\,2^{m+1}}, &
C_{\mathrm o}(2m+2)&=\frac{1}{3\,2^{m+1}}.
\end{aligned}
\]
In particular, the covariance at lag two is negative in the even phase and positive in the odd phase, although every sample has mean zero and variance \(1/3\).

For the naturally paired output
\[
S_m=\sum_{j=0}^{m-1}(X_{2j+1}+X_{2j+2}),\qquad m\ge1,
\]
there is also the exact finite-window variance and Gaussian limit
\[
\boxed{\operatorname{Var}(S_m)=m-\frac43+\frac{4}{3\,2^m},
\qquad \frac{S_m}{\sqrt m}\ \Longrightarrow\ N(0,1).}
\]
The ordering \((1,2)\) exchanges the phase roles of the same invariant two-phase uniform measure.

## Assumptions and scope

Define \(F_b(x)=bx-\operatorname{sgn}(x)\) for \(x\in(-1,1)\setminus\{0\}\) and \(b\in[1,2]\). Assign any value in \([-1,1]\) at the threshold \(x=0\); every statement concerning Lebesgue-almost-everywhere trajectories is independent of this assignment. The two gains \(\beta_0,\beta_1\) are assumed distinct. We say the pair is **uniform at both phases** when the skew-product transformation
\[
(x,i)\longmapsto(F_{\beta_i}(x),1-i),\quad i\in\{0,1\},
\]
preserves \(\lambda\otimes\frac12(\delta_0+\delta_1)\), with \(\lambda\) normalized Lebesgue measure on \((-1,1)\). Equivalently, both individual branch maps preserve \(\lambda\). The covariance formulas refer to the ordering \((2,1)\), with initial \(U\sim\lambda\); they are not statements about every initial probability law or all coefficients.

## Proof

**Step 1: rigidity of uniform phase marginals.** For \(1<b<2\), the map \(F_b\) has positive-slope branches mapping \((-1,0)\) onto \((1-b,1)\) and \((0,1)\) onto \((-1,b-1)\). Its push-forward of \(\lambda\) has the almost-everywhere density
\[
h_b(y)=\frac{\mathbf 1_{(1-b,1)}(y)+\mathbf 1_{(-1,b-1)}(y)}{2b},\qquad -1<y<1.
\]
The overlap interval \((1-b,b-1)\) has positive length, and the nonoverlap region also has positive length. Thus \(h_b\) takes two distinct values, not the constant \(1/2\). At \(b=1\) the branch images partition the interval and at \(b=2\) they each cover it, giving density \(1/2\) in both cases. Consequently \(F_b\) preserves \(\lambda\) exactly for \(b\in\{1,2\}\), proving the claimed unique distinct pairs.

**Step 2: exact dyadic reduction.** Denote \(A=F_2\) and \(B=F_1\). Outside the null set of threshold preimages,
\[
B^2=\operatorname{id},\qquad A\circ B=A,\qquad A=\operatorname{id}+B.
\]
The phase-two maps are \(B\circ A\) and \(A\circ B=A\); conjugation by the measure-preserving involution \(B\) identifies \(B\circ A\) with \(A\). The map \(A\) is the signed binary doubling map. Thus both phase-two dynamics are measure-theoretically conjugate to a one-sided fair Bernoulli shift (up to a null set), giving a natural exact model for phase-dependent dependence without any independence assumption on successive voltages.

**Step 3: all lag covariances.** The transfer operator for \(A\) acting on normalized Lebesgue measure has two inverse branches \(y\mapsto(y-1)/2\) and \(y\mapsto(y+1)/2\), each weighted by \(1/2\). Applied to the observable \(x\), it yields
\[
(P_A x)(y)=\frac y2,\qquad P_A^m x=2^{-m}x.
\]
Therefore, for \(m\ge0\),
\[
\begin{aligned}
\mathbb E[U A^m(U)]&=\frac{1}{3\,2^m},\\
\mathbb E[U B(A^m(U))]&=\mathbb E[U A^m(U)]-\mathbb E[U\operatorname{sgn}(A^m(U))]
=-\frac{1}{6\,2^m},
\end{aligned}
\]
since \(\int_{-1}^1 |y|\,d\lambda(y)=1/2\). From \(A\circ B=A\),
\[
X_{2j+1}=A^{j+1}(U),\qquad X_{2j+2}=B(A^{j+1}(U)).
\]
These identities, plus invariance of \(\lambda\) under \(A\) and \(B\), give the announced two phase-dependent covariance sequences for every lag. The even-start formula also applies at \(j=0\), directly by \(X_0=U\).

**Step 4: finite-window fluctuations.** The identity \(A(x)=x+B(x)\) gives \(X_{2j+1}+X_{2j+2}=X_{2j+3}\). With \(W=A(U)\sim\lambda\),
\[
S_m=\sum_{j=1}^m A^j(W).
\]
The exact covariance \(\operatorname{Cov}(A^j(W),A^{j+k}(W))=1/(3\,2^k)\) gives
\[
\operatorname{Var}(S_m)=\frac m3+\frac23\sum_{k=1}^{m-1}\frac{m-k}{2^k}
=m-\frac43+\frac4{3\,2^m}.
\]
Represent \(W=\sum_{i\ge1}\varepsilon_i2^{-i}\) with independent fair \(\varepsilon_i\in\{-1,1\}\). Binary shifting gives \(A^j(W)=\sum_{k\ge1}\varepsilon_{j+k}2^{-k}\), and summing the geometric coefficients establishes the deterministic bound
\[
\left|S_m-\sum_{i=2}^{m+1}\varepsilon_i\right|\le2
\]
for every non-dyadic binary expansion. The classical independent-sign central limit theorem and this bounded error prove \(S_m/\sqrt m\Rightarrow N(0,1)\). No finite computation is used as proof of this limit.

## Verification

The included `verify.py` performs exact rational arithmetic, splitting initial intervals at each branch boundary. It integrates every resulting piecewise-affine coordinate product exactly against normalized Lebesgue measure. Checks include every covariance formula at lags \(0\) through \(12\) in **each** phase and all block-sum variances for \(1\le m\le8\); these calculations passed. The transfer identity, binary recoding, all-lag statements, and Gaussian limit are proved symbolically above rather than extrapolated from those finite checks. Reproduce with `python3 verify.py` from the extracted package directory.

## Relationship to prior work

Bula and Radin's *Chaotic single neuron model with periodic coefficients with period two* (first publicly available 2023-12-13) introduces the exact alternating-threshold recurrence and characterizes deterministic attracting intervals and chaotic behavior for selected gains. The present theorem instead classifies the exceptional uniform-marginal endpoint pairs and computes phase-conditioned correlations and finite-window fluctuations. Their *Eventually periodic solutions of single neuron model* (2020) treats eventual periodicity for periodic internal decay, not the stated statistical laws. The binary-doubling shift and its transfer-operator techniques are classical; the claim is **not** that those ingredients themselves are novel. The asserted addition is their exact phase-resolved assembly and uniform-gain rigidity for this nonautonomous threshold neuron.

## Limitations

The gain classification is restricted to \([1,2]\) and to uniform conditional marginals at **both** time parities. The Gaussian limit concerns the specified paired sum, not every observable or arbitrary transient initial state. Dyadic and threshold-preimage exceptional sets have zero Lebesgue measure, and no assertion is made about their pointwise orbit itineraries. The two-phase uniform measure need not be the only invariant probability measure. Existing literature on Markov partitions, doubling-map observables, or earlier periodic neuron-map studies may imply parts of the formulas by other methods; in particular, the full text of Bula and Radin's 2015 periodic-orbit paper was not available for comparison. Independent mathematical review has not been performed.

## References

1. I. Bula and M. A. Radin, *Chaotic single neuron model with periodic coefficients with period two*, Nonlinear Analysis: Modelling and Control **29** (2024), 111–123, published online 2023-12-13. https://doi.org/10.15388/namc.2024.29.33766. Full text: https://www.journals.vu.lt/nonlinear-analysis/article/download/33766/32339/86114.
2. I. Bula and M. A. Radin, *Eventually periodic solutions of single neuron model*, Nonlinear Analysis: Modelling and Control **25** (2020), 903–918. https://doi.org/10.15388/namc.2020.25.20555. Full text: https://www.journals.vu.lt/nonlinear-analysis/article/download/20555/20005/37053.
3. I. Bula and M. A. Radin, *Periodic orbits of a neuron model with periodic internal decay rate*, Applied Mathematics and Computation (2015), https://doi.org/10.1016/j.amc.2015.05.097. Full-text comparison remains incomplete.
