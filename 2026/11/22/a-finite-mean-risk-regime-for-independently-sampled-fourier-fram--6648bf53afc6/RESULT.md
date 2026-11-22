# A finite-mean-risk regime for independently sampled Fourier frames

## Finding

Let \(N\ge3\) and \(m\ge N\) be integers. Draw \(Z_1,\ldots,Z_m\) independently and uniformly from the complex unit circle. Form the unnormalized consecutive-frequency sampling matrix
\[
A_{m,N}=(Z_j^k)_{1\le j\le m,\ 0\le k<N},\qquad
\Lambda_{m,N}=\lambda_{\min}(A_{m,N}^*A_{m,N}),\qquad
R_{m,N}=\operatorname{tr}((A_{m,N}^*A_{m,N})^{-1}).
\]
The inverse exists almost surely. The following opposing, all-dimension sampling regimes hold:

**(A) Collision-forced divergence.** For \(N\le m\le2N-1\),
\[
\mathbb E[\Lambda_{m,N}^{-1}]=\mathbb E[R_{m,N}]=\infty.
\]
More precisely, for fixed \(m,N\), there is \(c_{m,N}>0\) such that
\[
\Pr\{\Lambda_{m,N}\le s\}\ge c_{m,N}s^{(m-1)/(2N-2)}
\]
for all sufficiently small positive \(s\).

**(B) Independent-block regularization.** Whenever \(k\ge1\) is an integer and \(m\ge kN\), there is \(C_{N,k}<\infty\), independent of \(m\), such that
\[
\Pr\{\Lambda_{m,N}\le s\}\le C_{N,k}s^{k/2}
\bigl(1+\log(1/s)\bigr)^{k(N-2)},\qquad 0<s< s_{N,k},
\]
and hence
\[
\mathbb E[\Lambda_{m,N}^{-p}]<\infty\quad\text{for every }0<p<k/2.
\]
In particular, for every \(N\ge3\) and \(m\ge3N\),
\[
\boxed{\mathbb E[R_{m,N}]<\infty.}
\]
For the first nontrivial centered three-frequency model \(N=3\), the average inverse-Gram noise risk is thus infinite for \(m=3,4,5\) but finite for every \(m\ge9\). The interval \(6\le m\le8\) is **not** classified here. The sufficient threshold \(3N\) is not asserted to be optimal.

## Assumptions and scope

The angles are independent Haar-uniform on \([0,2\pi)\); the matrix is complex, unnormalized, and uses consecutive frequencies \(0,\ldots,N-1\). Translating the frequency band by an integer only multiplies rows by unimodular factors and does not alter the Gram spectrum. This includes the centered odd-frequency band used in the motivating study after a harmless frequency translation. All finite-moment constants depend on fixed \(N,k,p\), never on \(m\ge kN\). The assertions concern fixed finite dimensional matrices, not limits in which \(N\) grows. Whenever the additive observation noise has independent centered complex coordinates with common variance \(\nu>0\), the conditional least-squares coefficient error has mean squared norm \(\nu R_{m,N}\). Thus the expectation in (B) gives finite unconditional noise risk; no signal prior is required for full-column-rank least squares.

## Proof

**1. Almost-sure rank.** Any \(N\) rows with distinct nodes form a square Vandermonde matrix of determinant \(\prod_{i<j}(Z_j-Z_i)\). Independence and continuity make the first \(N\) nodes distinct almost surely, so the full matrix has column rank \(N\).

**2. Divergence via a multiple-zero test polynomial.** Fix the first sample \(Z_1\). For \(0<\delta<1\), consider the event \(E_\delta\) where every other angle differs from that of \(Z_1\) by at most \(\delta\) in circular angular distance. Its probability is exactly \((\delta/\pi)^{m-1}\). Put
\[
P_\delta(z)=\frac{(z-Z_1)^{N-1}}{\sqrt{\binom{2N-2}{N-1}}}.
\]
Its coefficient vector has squared Euclidean norm one, by the binomial-square identity and \(|Z_1|=1\). On \(E_\delta\), every \(|Z_j-Z_1|\le\delta\), hence the Rayleigh principle gives
\[
\Lambda_{m,N}\le\sum_{j=1}^m|P_\delta(Z_j)|^2
\le\frac{m\delta^{2N-2}}{\binom{2N-2}{N-1}}.
\]
For sufficiently small \(s\), take \(\delta=(s\binom{2N-2}{N-1}/m)^{1/(2N-2)}\). This proves the displayed small-eigenvalue lower bound. Finally, for \(\Lambda>0\), the layer-cake identity gives
\[
\mathbb E[\Lambda^{-1}]
\ge\int_{1/s_0}^{\infty}\Pr\{\Lambda<1/t\}\,dt;
\]
this diverges when \((m-1)/(2N-2)\le1\), precisely \(m\le2N-1\). Since \(R\ge\Lambda^{-1}\), its expectation also diverges.

**3. Square-block inverse-tail lemma.** Let \(V\) be an \(N\times N\) Vandermonde matrix from \(N\) independent uniform nodes, and set \(L=\lambda_{\min}(V^*V)\). The coefficient vector of the \(i\)-th Lagrange polynomial is the \(i\)-th column of \(V^{-1}\). Its numerator coefficient squared norm is at most
\[
B_N^2=\sum_{r=0}^{N-1}\binom{N-1}{r}^2=\binom{2N-2}{N-1}.
\]
Writing \(Q_i=\prod_{j\ne i}|Z_i-Z_j|^{-1}\), it follows deterministically that
\[
L^{-1/2}=\|V^{-1}\|_{\mathrm{op}}
\le\|V^{-1}\|_{\mathrm F}\le B_N\sqrt N\max_i Q_i.
\]
Conditional on \(Z_i\), the \(N-1\) variables \(U_j=|Z_i-Z_j|/2\) are independent with
\[
\Pr\{U_j\le u\}=\frac2\pi\arcsin u\le u,
\qquad0\le u\le1.
\]
Thus \(-\log U_j\) is stochastically no larger than a standard exponential variable. The sum of \(N-1\) independent standard exponentials has exact gamma tail
\[
\Pr\{G_{N-1}\ge t\}=e^{-t}\sum_{r=0}^{N-2}\frac{t^r}{r!},\qquad t\ge0.
\]
Since \(Q_i=2^{-(N-1)}\prod_{j\ne i}U_j^{-1}\), conditioning and the union bound show, with \(H_N(s)=2^{N-1}/(B_N\sqrt{Ns})\), that whenever \(H_N(s)\ge1\),
\[
\Pr\{L\le s\}
\le\frac{N}{H_N(s)}\sum_{r=0}^{N-2}
\frac{(\log H_N(s))^r}{r!}.
\tag{1}
\]
Consequently \(\Pr\{L\le s\}\le C_N\sqrt{s}(1+\log(1/s))^{N-2}\) for small \(s\). This is a genuine finite-dimensional, square-block estimate; it is not a claim of independence between the Lagrange columns.

**4. Multiple independent square blocks.** If \(m\ge kN\), partition the first \(kN\) sample rows into \(k\) disjoint blocks \(V_1,\ldots,V_k\) of \(N\) rows. The positive Gram decomposition gives
\[
A_{m,N}^*A_{m,N}\succeq\sum_{b=1}^{k}V_b^*V_b,
\qquad\Lambda_{m,N}\ge\sum_{b=1}^k L_b,
\]
where \(L_b=\lambda_{\min}(V_b^*V_b)\) are independent. Therefore
\[
\Pr\{\Lambda_{m,N}\le s\}
\le\prod_{b=1}^k\Pr\{L_b\le s\},
\]
which together with (1) proves (B)'s explicit power-logarithm bound. Its layer-cake integral for \(\Lambda^{-p}\) converges whenever \(p<k/2\). Taking \(k=3\) and \(p=1\), and using \(R_{m,N}\le N\Lambda_{m,N}^{-1}\), gives finite expected noise amplification for every \(m\ge3N\). This completes the theorem. \(\square\)

## Verification

The standalone `CHECK.py` evaluates the Vandermonde, Lagrange inverse, binomial normalization, positive Gram-block sum, and eigenvalue bounds for deterministic random configurations and checks the exact gamma-tail and angular-chord formulas. Its computations are supplementary: the infinitely quantified results follow from the binomial identity, Haar angular law, independent-block Gram positivity and layer-cake integrals. Run `python CHECK.py` with NumPy installed in the extracted package directory.

## Relationship to prior work

Xu and Shen (arXiv:2609.29286v1, September 24, 2026) study exactly independent uniform circle nodes in Fourier–Vandermonde regression. Their Theorem 6 asserts divergence of the expected inverse least singular value across sample counts, citing a minimum-pair-separation argument. The conclusion of (B) gives a contrary finite expectation for the overdetermined regime \(m\ge3N\); a collision between two *rows* need not destroy full *column* rank after sufficient oversampling. This comparison is a mathematical conflict of statements, not a claim that all other results of the paper are incorrect.

An earlier published square-matrix result, *Critical inverse moments and logarithmic tails of random Fourier interpolation* (2026), obtains sharp fractional-moment and logarithmic-tail laws for \(m=N\). The present proof rederives only the square tail estimate needed as a lemma and then treats a distinct, oversampled \(m\ge3N\) regime by independence of multiple subframes. Another published result, *Sharp small-singular tails and inverse-moment thresholds for a circular Fourier sketch* (2026), determines the complete two-frequency case, whereas the present theorem addresses every \(N\ge3\). Deterministic clustered-Vandermonde bounds by Kunis and Nagel address singular-value geometry, not unconditional inverse-moment integrability of an oversampled random design. The earlier Bass–Gröchenig paper studies random trigonometric sampling condition-number distributions; its full text could not be accessed for a theorem-level comparison. No worldwide novelty certification is claimed.

## Limitations

The sufficient finite-risk bound \(m\ge3N\) is not proved optimal, and the intermediate interval \(2N\le m<3N\) remains unresolved by this argument. The result does not claim precise small-eigenvalue leading constants, uniform-in-\(N\) estimates, arbitrary frequency sets, or correlated nodes. The square-block bound is a relatively direct application of Lagrange interpolation and the addition of independent positive Gram matrices, although the resulting opposing risk regimes address a substantive open comparison in the motivating model. Earlier stronger sampling estimates could imply the same sufficient condition. The full Bass–Gröchenig article remained inaccessible through the available channels, so priority over an equivalent older result remains a specific risk. No independent mathematical audit has been conducted.

## References

1. H. Xu and Y. Shen, *Non-asymptotic Analysis of Expected Reconstruction Risk for Trigonometric Polynomial Models*, arXiv:2609.29286v1, first public September 24, 2026. https://arxiv.org/abs/2609.29286
2. *Critical inverse moments and logarithmic tails of random Fourier interpolation*, published November 8, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-critical-inverse-moments-and-logarithmic-tails-of-random-fourier--323dcae74731/RESULT.md
3. *Sharp small-singular tails and inverse-moment thresholds for a circular Fourier sketch*, published November 2, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-small-singular-tails-and-inverse-moment-thresholds-for-a-c--5fb2ea549d24/RESULT.md
4. S. Kunis and D. Nagel, *On the smallest singular value of multivariate Vandermonde matrices with clustered nodes*, arXiv:1907.07119v1 (July 16, 2019). https://arxiv.org/abs/1907.07119
5. R. F. Bass and K. Gröchenig, *Random Sampling of Multivariate Trigonometric Polynomials*, SIAM J. Math. Anal. 36 (2004/05), 773–795. https://doi.org/10.1137/S0036141003432316
