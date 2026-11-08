# A rational cross-tree covariance kernel for correlated uniform-attachment degree profiles

## Finding

Consider two correlated uniform-attachment trees grown on the same arrival labels. For every fixed degree cutoff \(K\), their centered outdegree-count vectors obey a joint Gaussian limit. The entire **cross-tree** limiting covariance matrix is specified by the following rational bivariate generating function:

\[
\boxed{\displaystyle
\mathcal C_\alpha(z,w)=
\sum_{k,l\geq0}c_{kl}(\alpha)z^k w^l
=\frac{\alpha(1+\alpha)(1-z)^2(1-w)^2}
{(3-z-w)(2-z)(2-w)
[3-\alpha-(1-\alpha)(z+w)-\alpha zw]}.}
\]

Specifically, if \(N_{n,k}^{(r)}\) is the number of vertices with exactly \(k\) children in tree \(r\in\{1,2\}\), then for every fixed integer \(K\geq0\),

\[
\left(\frac{N_{n,k}^{(r)}-n2^{-k-1}}{\sqrt n}:
 0\leq k\leq K,\ r=1,2\right)
\ \xrightarrow{d}\ (V_k^{(r)}:0\leq k\leq K,r=1,2),
\]

where the right side is centered Gaussian, \(\operatorname{Cov}(V_k^{(1)},V_l^{(2)})=c_{kl}(\alpha)\), and \(\operatorname{Cov}(V_k^{(r)},V_l^{(r)})=c_{kl}(1)\). Moreover,

\[
\lim_{n\to\infty}\frac1n
\operatorname{Cov}(N_{n,k}^{(1)},N_{n,l}^{(2)})=c_{kl}(\alpha).
\]

The first non-leaf entry is an explicit strictly increasing function of the attachment-correlation parameter:

\[
\boxed{\displaystyle
c_{11}(\alpha)=\frac{\alpha(1+\alpha)
(5\alpha^2-18\alpha+297)}{432(3-\alpha)^3},\qquad 0\leq\alpha\leq1.}
\]

For every \(\alpha>0\), \(c_{01}(\alpha)=-\alpha(1+\alpha)(15-\alpha)/[72(3-\alpha)^2]<0\). In particular, the limiting variance of the difference of the outdegree-one counts is \(2[71/432-c_{11}(\alpha)]\), strictly decreasing from \(71/216\) to zero as \(\alpha\) increases from zero to one.

## Assumptions and scope

Start at \(n=1\) with one vertex labeled \(1\) in each tree. For each integer \(n\geq1\), add vertex \(n+1\) to both trees. Independently across steps, with probability \(\alpha\in[0,1]\) choose one label uniformly from \(\{1,\ldots,n\}\) and use it as the parent in **both** trees; with probability \(1-\alpha\), choose the two parent labels independently, each uniformly on this set. Each new vertex contributes exactly one edge to each tree. Outdegree means the number of children in the root-oriented tree; it is not the undirected degree of the root. The joint central limit theorem is finite-dimensional in the fixed degree cutoff; no infinite-dimensional topology is claimed.

Define the same-label joint degree counts and degree-generating polynomials by

\[
A_{n,k,l}=\#\{v:\deg^+_{T_n^{(1)}}(v)=k,
\deg^+_{T_n^{(2)}}(v)=l\},
\quad Z_n(z,w)=\sum_{k,l\geq0}A_{n,k,l}z^kw^l,
\]

\[
F_n^{(r)}(z)=\sum_{k\geq0}N_{n,k}^{(r)}z^k,
\qquad P(z)=\frac1{2-z}.
\]

Every generating-function assertion is a formal power-series identity around \(z=w=0\), and therefore defines each fixed coefficient without additional analytic convergence assumptions.

## Proof

**1. The paired-degree law of large numbers.** Conditional on the current labeled trees, the joint polynomial has the exact one-step drift

\[
\begin{aligned}
\mathbb E[Z_{n+1}(z,w)-Z_n(z,w)\mid\mathcal F_n]
={}&1+\frac{\alpha(zw-1)+(1-\alpha)(z+w-2)}nZ_n(z,w)\\
&+\frac{(1-\alpha)(z-1)(w-1)}{n^2}Z_n(z,w).
\end{aligned}
\]

The last term corrects the event in which both independent parent choices hit the same vertex. For each fixed \((k,l)\), normalize the coefficient \(A_{n,k,l}\) by \(n\). The resulting stochastic-approximation drift has diagonal contraction \(3-\alpha\geq2\), depends otherwise only on the coefficients \((k-1,l)\), \((k,l-1)\), and \((k-1,l-1)\), and has a uniformly bounded martingale increment divided by \(n+1\). The collision correction is \(O(n^{-2})\) after normalization. The scalar contraction lemma (variation of constants, bounded martingale differences, and square-summable step sizes), inductively over \(k+l\), gives the almost-sure limits \(A_{n,k,l}/n\to q_{kl}(\alpha)\), with

\[
(3-\alpha)q_{kl}=\mathbf1_{k=l=0}
+(1-\alpha)(q_{k-1,l}+q_{k,l-1})
+\alpha q_{k-1,l-1},
\]

where negative indices have zero coefficients. Summing as formal series yields

\[
Q_\alpha(z,w)=\sum q_{kl}(\alpha)z^kw^l
=\frac1{3-\alpha-(1-\alpha)(z+w)-\alpha zw}.
\]

Each single tree has the well-known limiting degree series \(P(z)=1/(2-z)\): this also follows directly from the next drift identity. Notice that \(Q_\alpha(z,1)=P(z)\), as required by the marginal models.

**2. Exact marginal drift and innovation cross-covariance.** For either tree,

\[
\mathbb E[F_{n+1}^{(r)}(z)-F_n^{(r)}(z)\mid\mathcal F_n]
=1+\frac{z-1}{n}F_n^{(r)}(z).
\]

Set \(G_n^{(r)}(z)=F_n^{(r)}(z)-nP(z)\), and let \(\xi_{n+1}^{(r)}(z)\) be the centered one-step increment. Since \((2-z)P(z)=1\),

\[
G_{n+1}^{(r)}(z)=\left(1+\frac{z-1}{n}\right)G_n^{(r)}(z)
+\xi_{n+1}^{(r)}(z).
\]

The common-label branch and independent-label branch have identical conditional marginal means. Consequently the **exact** conditional cross-innovation covariance is

\[
\mathbb E[\xi_{n+1}^{(1)}(z)\xi_{n+1}^{(2)}(w)\mid\mathcal F_n]
=\alpha(z-1)(w-1)
\left[\frac{Z_n(z,w)}n
-\frac{F_n^{(1)}(z)F_n^{(2)}(w)}{n^2}\right].
\]

Taking coefficientwise limits using step 1 and bounded degree proportions gives the deterministic cross-noise generating function

\[
S_\alpha(z,w)=\alpha(1-z)(1-w)
\bigl[Q_\alpha(z,w)-P(z)P(w)\bigr].
\]

The within-tree noise limit is the same formula with \(\alpha=1\), since both chosen degree arguments then belong to the same tree.

**3. Joint central limit theorem and the covariance kernel.** For each fixed cutoff, the coefficients of \(G_n^{(r)}\) form a finite linear stochastic recursion with drift matrix \(B=-I+J\), where \(J\) has ones immediately below the diagonal and zeros elsewhere. All martingale innovations are bounded. Its fundamental-matrix multiplier from an innovation at time \(\lfloor nt\rfloor\) to time \(n\) converges, for \(0<t\leq1\), to \(t^{-B}=t\exp(-J\log t)\). The deterministic mean recursion for \(G_n\) also gives \(\mathbb E G_{n,k}^{(r)}=o(\sqrt n)\) for each fixed \(k\), justifying centering by \(n2^{-k-1}\). The bounded innovations satisfy the triangular-array Lindeberg condition, while their conditional quadratic variations converge by step 1; the contribution from \(t\leq\varepsilon\) vanishes uniformly as \(\varepsilon\downarrow0\), because \(t\exp(-J\log t)\) is bounded and square-integrable near zero. The martingale central limit theorem and Cramér–Wold therefore give the stated finite-dimensional joint Gaussian limit.

For the cross block, the covariance integral in generating notation is

\[
\mathcal C_\alpha(z,w)
=\int_0^1t^{2-z-w} S_\alpha(z,w)\,dt
=\frac{S_\alpha(z,w)}{3-z-w}.
\]

This identity is coefficientwise: the integral of any finite coefficient contains only terms \(t^2(\log t)^m\), which are integrable. The same recursion for second moments and bounded conditional variances proves \(n^{-1}\operatorname{Cov}(N_{n,k}^{(1)},N_{n,l}^{(2)})\to c_{kl}(\alpha)\), rather than merely asserting moment convergence from weak convergence. Since

\[
(2-z)(2-w)-[3-\alpha-(1-\alpha)(z+w)-\alpha zw]
=(1+\alpha)(1-z)(1-w),
\]

substitution and cancellation yield the boxed rational kernel.

**4. Non-leaf coefficients and strictness.** Coefficient extraction at \((k,l)=(0,0),(0,1),(1,1)\) gives

\[
\begin{aligned}
c_{00}(\alpha)&=\frac{\alpha(1+\alpha)}{12(3-\alpha)},\\
c_{01}(\alpha)=c_{10}(\alpha)&=-\frac{\alpha(1+\alpha)(15-\alpha)}{72(3-\alpha)^2},\\
c_{11}(\alpha)&=\frac{\alpha(1+\alpha)(5\alpha^2-18\alpha+297)}{432(3-\alpha)^3}.
\end{aligned}
\]

The derivative of the last expression is

\[
\frac{891+2268\alpha+162\alpha^2+60\alpha^3-5\alpha^4}
{432(3-\alpha)^4}>0 \quad (0\leq\alpha\leq1).
\]

At \(\alpha=1\), both trees are identical and \(c_{11}(1)=71/432\); at \(\alpha=0\), they are independent and the cross kernel vanishes. The joint Gaussian difference and its strictly decreasing variance follow immediately.

## Verification

The standalone file `verify.py` reproduces finite exact checks with only the Python standard library. It checks the four-factor generating-function identity coefficientwise through bidegree seven, for six rational values of \(\alpha\), all displayed low-degree coefficients and determinant identities, and the exact conditional cross-innovation identity by enumerating paired parent choices. On the prepared file, 649 exact rational assertions passed. Independently, simulations at \(n=1000\) with 15,000 paired trees per tested parameter agreed with the predicted cross covariances at sampling precision. These checks do not certify an infinite-dimensional limit; the proof supplies the limiting argument.

## Relationship to prior work

Bäumler, Rácz, Ross, and Sridhar (2026) introduced this sprinkled-correlation model and proved detection and estimation theorems. Their Appendix A calculates Gaussian leaf-count statistics and explicitly identifies an analytically tractable **higher-degree** covariance representation as a remaining problem. The present statement gives an explicit bivariate rational generating function for every fixed pair of outdegrees, including the first non-leaf degree, and a joint Gaussian limit. Their leaf-count result is recovered as the coefficient \(c_{00}(\alpha)\), not re-presented as new.

Janson (2005) derived the marginal outdegree covariance series for a single recursive tree. Setting \(\alpha=1\) in the new formula exactly reproduces his equation (1.1) and the benchmark \(c_{11}(1)=71/432\). That single-tree result does not determine cross-tree dependence for intermediate \(\alpha\). Rácz and Sridhar (2022) study an initial-common-growth/change-point coupling, which is distinct from the independently sprinkled alignment used here. Priority against unidentified broader multitype-urn formulations is not claimed as settled.

## Limitations

The limit is for each fixed finite collection of degree indices, not for an unspecified topology on all degree counts. It does not give perfect correlation detection from a fixed number of Gaussian degree-profile observations, nor a consistent single-pair estimator based only on a fixed number of degree counts. The covariance series is a Gaussian second-order description, not a full distributional identity at finite \(n\). The statement assumes uniform one-parent attachments and time-independent \(\alpha\). Independent mathematical audit and definitive historical-priority assessment have not been performed.

## References

1. J. Bäumler, M. Z. Rácz, N. Ross, and A. Sridhar, *Correlated uniform attachment trees*, arXiv:2606.02472, first posted 2026-06-01, https://arxiv.org/html/2606.02472.
2. S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms 26 (2005), 69–83, DOI:10.1002/rsa.20046; author preprint https://www2.math.uu.se/~svantejs/papers/sj155.pdf.
3. M. Z. Rácz and A. Sridhar, *Correlated randomly growing graphs*, Annals of Applied Probability 32 (2022), 1058–1111; preprint arXiv:2004.13537, https://arxiv.org/abs/2004.13537.
