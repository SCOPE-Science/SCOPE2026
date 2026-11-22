# Sharp negative third-level Walsh correlation for symmetric monotone functions

## Finding

For every integer \(n\geq3\), the exact minimum of the third Walsh-level correlation \(W_3[f,g]\) over all **permutation-invariant, coordinatewise nondecreasing functions** \(f,g:\{0,1\}^n\to[0,1]\) is

\[
\min W_3[f,g]=-\binom n3\frac{P_{n-1}Q_{n-1}}{2^{2n}(n-1)^2(n-2)^2},
\]
where for \(m\geq2\),
\[
F_m(k)=\binom mk\big((m-2k)^2-m\big),\quad
P_m=\max_{0\leq k\leq m}F_m(k),\quad
Q_m=\max_{0\leq k\leq m}(-F_m(k)).
\]
The extremal indices and hence the value are explicit. Put
\[
r_m=1+\sqrt{3m+1},\qquad
k_m=\max\!\left\{0,\left\lceil\frac{m-r_m}{2}\right\rceil\right\}.
\]
Then
\[
P_m=F_m(k_m),\qquad
Q_m=(m-\varepsilon_m)\binom m{\lfloor m/2\rfloor},
\qquad
\varepsilon_m=\begin{cases}0,&m\text{ even},\\1,&m\text{ odd}.
\end{cases}
\]
The positive-maximizer indices of \(F_m\) form \(\{k_m,m-k_m\}\), augmented by \(\{k_m+1,m-k_m-1\}\) if \(m-2k_m=r_m\). The negative-minimizer indices are exactly \(\{\lfloor m/2\rfloor,\lceil m/2\rceil\}\). Repeated elements in these sets are understood only once.

Write \(T_t(x)=\mathbf 1_{\{|x|\geq t\}}\), where \(|x|\) is Hamming weight. **Every equality pair**, up to exchange of \(f,g\), consists of \(f\) in the convex hull of those \(T_{k+1}\) with positive-maximizer indices \(k\), and \(g\) in the convex hull of those \(T_{k+1}\) with negative-minimizer indices \(k\). In particular, both functions have values zero at the zero vector and one at the all-one vector.

The optimal negative correlation has the dimension-free limit
\[
\boxed{\displaystyle\min W_3[f,g]=-\frac{e^{-3/2}}{6\pi}+O(n^{-1/2})}\,.
\]
The off-central extremal thresholds lie at Hamming weights \(n/2\pm\sqrt{3n}/2+O(1)\); the opposite extremizer is an ordinary central threshold. (All numerical constants use the normalized Walsh transform below.)

## Assumptions and scope

The cube is uniformly distributed. For \(S\subseteq\{1,\ldots,n\}\), the Walsh character is \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) and the Fourier coefficient is \(\widehat f(S)=2^{-n}\sum_x f(x)\chi_S(x)\). Set \(W_3[f,g]=\sum_{|S|=3}\widehat f(S)\widehat g(S)\). Functions are real, permutation-invariant, coordinatewise nondecreasing, bounded between zero and one, and the result concerns every integer \(n\geq3\). There are no assertions for nonsymmetric or unbounded inputs.

## Proof

**1. Threshold simplex.** For a permutation-invariant nondecreasing \(f\), let \(v_j\) be its value at every vector of weight \(j\). Then \(0\leq v_0\leq\cdots\leq v_n\leq1\), and
\[
f=v_0+\sum_{t=1}^n (v_t-v_{t-1})T_t,
\qquad v_t-v_{t-1}\geq0,
\quad \sum_t(v_t-v_{t-1})\leq1.
\]
The constant has zero nonempty Fourier coefficients. Symmetry makes the level-three coefficient common to all triples. Thus the possible scalar coefficients form the convex hull of zero and the \(n\) threshold coefficients.

**2. Exact threshold coefficient.** Condition on the remaining \(n-3\) bits. Condition on the three distinguished bits and apply Pascal's identity twice to the resulting alternating binomial sums. Hence for each triple \(S\)
\[
\widehat T_t(S)=2^{-n}\left[-\binom{n-3}{t-1}+2\binom{n-3}{t-2}-\binom{n-3}{t-3}\right]
=-\frac{F_{n-1}(t-1)}{2^n(n-1)(n-2)}.
\]
Out-of-range binomial coefficients are zero. Both positive and negative scalar coefficients occur, because \(F_m(0)=m(m-1)>0\) and \(F_m(\lfloor m/2\rfloor)<0\) for \(m\geq2\). Thus their entire admissible interval has endpoints \(-P_m/[2^nm(m-1)]\) and \(+Q_m/[2^nm(m-1)]\).

**3. Discrete peak locations.** Symmetry gives \(F_m(k)=F_m(m-k)\). Write \(j=m-2k\). For \(0\leq k<m/2\), elementary use of \(\binom m{k+1}=\binom mk(m-k)/(k+1)\) gives the exact difference
\[
F_m(k+1)-F_m(k)=\frac{\binom mk}{k+1}(j-1)(j^2-2j-3m).
\]
For \(j\geq2\), this changes sign once, at \(j=1+\sqrt{3m+1}\); on the middle parity boundary \(j=1\) the values are equal. It follows that the left-hand **positive** maximum occurs at \(k_m\), and also at \(k_m+1\) exactly in the stated tie case. The reflected indices give all positive maximizers. Conversely, wherever \(F_m(k)<0\), both \(\binom mk\) and the positive factor \(m-(m-2k)^2\) are maximized at the central index or pair, proving the stated formula for \(Q_m\) and all its indices.

**4. Sharp cross-correlation and equality.** If \(c_f\) and \(c_g\) are the common level-three coefficients, then \(W_3[f,g]=\binom n3 c_fc_g\). Over the product of the same interval containing both signs, the minimum is the product of its opposite endpoints. This proves the sharp formula. Equality requires a full unit mass of threshold increments on the indices attaining the appropriate endpoint (since both endpoints are nonzero), which gives precisely the convex hulls above. Each permitted pair realizes the bound.

**5. Limit.** For \(j=m-2k=O(\sqrt m)\), Stirling's formula yields uniformly in the relevant parity lattice
\[
2^{-m}\binom m{(m-j)/2}=\sqrt{\frac2{\pi m}}e^{-j^2/(2m)}\big(1+O(m^{-1/2})\big).
\]
The positive peak satisfies \(j=\sqrt{3m}+O(1)\), so \(P_m/2^m=2m\sqrt{2/(\pi m)}e^{-3/2}(1+O(m^{-1/2}))\). At the central negative peak, \(j\in\{0,1\}\), giving \(Q_m/2^m=m\sqrt{2/(\pi m)}(1+O(m^{-1/2}))\). Substitute these two estimates and \(n=m+1\) into the finite sharp formula to obtain \(-e^{-3/2}/(6\pi)+O(n^{-1/2})\).

## Verification

The standalone `check_level3.py` uses exact integer/rational arithmetic and only the Python standard library. Run `python3 check_level3.py`. It checks the discrete peak and equality-index classification for every dimension \(3\leq n\leq120\), checks all 7,257 threshold-coefficient identities, checks each dimension's exhaustive threshold-pair optimum, and independently computes every Walsh sum for dimensions \(3\leq n\leq8\). These are supplementary finite checks, **not** a substitute for the all-dimension proof.

## Relationship to prior work

Chang, Li, Wang and Wang [1] proved a general lower bound for the third-level cross correlation of increasing functions in terms of their first-level correlation and variances, and examined its optimal coefficient in their sharpness discussion. Their question concerns a ratio involving those statistics, whereas the present theorem exactly optimizes the **absolute** third-level cross correlation in the bounded permutation-invariant class, including all equality cases and a Gaussian limit. Neither assertion implies the other's sharp extremal constant. Bernasconi [2] gave Krawtchouk formulas for Fourier coefficients of symmetric threshold functions, which supplies a classical representation ingredient; the discrete optimization of two opposite extremal coefficients and their full equality class is not given in the inspected threshold discussion. Chang [3] proves distinct spectral and covariance inequalities, not this fixed-level sharp bound.

## Limitations

This exact result applies only to the specified symmetric monotone \([0,1]\)-valued class. The unrestricted monotone case, other levels, and the optimal ratio constant in [1] are not settled. The argument is an analytical proof with finite reproducibility checks; no independent audit has been performed. The originality assessment is relative to the inspected literature, and older unindexed or otherwise uninspected equivalent statements remain possible.

## References

[1] F. Chang, Z. Li, G. Wang, M. Wang, *Fourier level inequalities on the discrete cube via complex hypercontractivity and Riesz transforms*, arXiv:2611.08289v1 (first public November 5, 2026), https://arxiv.org/abs/2611.08289.

[2] A. Bernasconi, *Harmonic analysis and Boolean function complexity*, Calcolo **35** (1998), 149–186, doi:10.1007/S100920050014; open text https://www.academia.edu/21101025/Harmonic_analysis_and_Boolean_function_complexity.

[3] F. Chang, *A spectral correlation inequality for increasing Boolean functions*, arXiv:2606.08958 (2026), https://arxiv.org/abs/2606.08958.
