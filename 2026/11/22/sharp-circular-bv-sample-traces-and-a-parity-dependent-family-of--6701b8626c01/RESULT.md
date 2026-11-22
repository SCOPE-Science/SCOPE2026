# Sharp circular BV sample traces and a parity-dependent family of optimal node designs

## Finding
Let \(N\ge2\) distinct measurement sites \(x_1,\ldots,x_N\) occur in cyclic order on the unit circle \(\mathbb T=\mathbb R/\mathbb Z\), with positive cyclic gaps \(g_1,\ldots,g_N\) summing to one. For real periodic \(f\in W^{1,1}(\mathbb T)\), put \(\bar f=\int_{\mathbb T}f\) and define the sharp trace constant
\[
C(X)=\sup_{f\not\equiv\mathrm{constant}}\frac{\bigl(\sum_{j=1}^{N}|f(x_j)-\bar f|^2\bigr)^{1/2}}{\int_{\mathbb T}|f'(x)|\,dx}.
\]
For \(k=0,\ldots,N-1\), let \(L_{i,k}=\sum_{j=0}^{k}g_{i+j}\), with cyclic subscripts. Then the exact finite-cut law is
\[
C(X)^2=\frac14\max_{0\le k<N}\max_{1\le i\le N}\bigl[k(1-L_{i,k})^2+(N-k)L_{i,k}^2\bigr]. \tag{1}
\]
Over all placements of the \(N\) sites,
\[
\min_X C(X)^2=\frac{\lfloor N^2/4\rfloor+1}{4N}. \tag{2}
\]
When \(N\) is odd or \(N\equiv0\pmod4\), the minimizers are precisely equally spaced sites, up to rotation. When \(N\equiv2\pmod4\), **all** minimizers have alternating gaps
\[
g_{2j-1}=\frac{1+\varepsilon}{N},\qquad g_{2j}=\frac{1-\varepsilon}{N},\qquad |\varepsilon|\le\sqrt2-1. \tag{3}
\]
For example, every even-length alternating design with six sites satisfying (3) attains \(C(X)^2=5/12\). The contrast threshold in (3) is independent of \(N\).

## Assumptions and scope
The circle has arclength one; the measurements are distinct and equally weighted in the *un-normalized* Euclidean norm; centering is by the **continuous arclength mean**, not by the sample mean. Functions are real, absolutely continuous and periodic, with the standard \(L^1\) derivative seminorm. Constants are factored out. All cyclic gaps are strictly positive. The result gives a supremum; discontinuous two-jump step functions are limits of admissible smooth functions, not asserted to lie in \(W^{1,1}\).

## Proof
**1. Two-jump reduction.** Every periodic \(f\in W^{1,1}(\mathbb T)\) has a signed derivative measure \(\mu=f'\,dx\) of total mass zero. Unless \(f\) is constant, its positive and negative parts each have mass \(V/2\), where \(V=\int|f'|\). Write \(\mu=(V/2)(P-Q)\) with probability measures \(P,Q\). The mean-zero primitive of \(\delta_s-\delta_t\) is the centered indicator of one of the two directed arcs between \(s,t\), up to sign. By linearity and the triangle inequality, the sample-vector norm divided by \(V\) is at most half the maximum centered sample-vector norm of an arc indicator. Conversely, approximate both endpoint atoms by smooth narrow derivative bumps of opposite sign, producing periodic \(W^{1,1}\) functions with variation exactly \(V\) and arbitrarily close sample vectors. Hence the two-jump upper bound is the sharp supremum.

**2. Exact finite cut.** If an arc has length \(\ell\) and contains exactly \(k\) sample sites, the squared Euclidean norm of its centered indicator vector is
\[
F_k(\ell)=k(1-\ell)^2+(N-k)\ell^2.
\]
For a fixed contiguous run of \(k\) sites, admissible arc lengths range between the internal gap sum and the sum of the \(k+1\) surrounding gaps. Since \(F_k\) is convex in \(\ell\), the largest value is approached at one of these two endpoints. The short-arc endpoint for \(k\) is the long-arc endpoint of the complementary \(N-k\) sites and gives the same squared norm. The long endpoint has length \(L_{i,k}\), proving (1), including empty arcs \(k=0\); arcs containing all sites are covered by their empty complements.

**3. Universal optimum.** For each fixed \(k\), the cyclic mean of \(L_{i,k}\) over \(i\) is \((k+1)/N\). Some \(L_{i,k}\) is at least this mean. As \(F_k\) is strictly increasing on \([k/N,1]\),
\[
4C(X)^2\ge F_k((k+1)/N)=\frac{k(N-k)+1}{N}.
\]
Maximizing over integer \(k\) gives the lower bound (2). Equally spaced sites attain equality for every cut in (1), proving sharpness.

**4. Rigidity and alternating exception.** If equality holds, each \(k\) maximizing \(k(N-k)\) must have all \(L_{i,k}=(k+1)/N\); otherwise a long cut exceeds the average and strict monotonicity raises the constant. This means \(g_i=g_{i+k+1}\) for all \(i\). For odd \(N\), the two maximizing values \(k=(N-1)/2,(N+1)/2\) yield consecutive shift periods, forcing all gaps equal. For \(N=2m\), only \(k=m\) maximizes. If \(m\) is even, \(\gcd(2m,m+1)=1\), so the gaps are equal. If \(m\) is odd, that gcd is two, so gaps alternate and can be parametrized by (3) with \(|\varepsilon|<1\).

For alternating gaps set \(e=|\varepsilon|\). A run of \(k+1\) gaps has maximum length \((k+1+\delta_k)/N\), where \(\delta_k=e\) for even \(k\) and \(\delta_k=0\) for odd \(k\). Substitution into (1) yields exactly
\[
4NC(X)^2=\max_{0\le k<N}\{k(N-k)+1+2\delta_k+\delta_k^2\}.
\]
Here \(m\) is odd; the central odd index \(k=m\) gives \(m^2+1\). The nearest even indices (one of them is \(0\) when \(N=2\)) give \(m^2+2e+e^2\); every other index has no larger value. Thus (2) holds exactly when \(e^2+2e\le1\), equivalently \(e\le\sqrt2-1\). This completes the necessary and sufficient classification.

## Verification
`CHECK.py` uses exact rational arithmetic to recompute (1) and (2) for all uniform designs with \(2\le N\le38\), 3,276 enumerated small nonuniform designs, and rational alternating perturbations for \(N\equiv2\pmod4\). It also checks the cyclic-period gcd split. The generated checker reports 3,369 successful exact rational comparisons. These finite tests corroborate the proof and are not substituted for the universal quantified argument.

## Relationship to prior work
The BV measure representation and scalar Koksma–Hlawka setting in Aistleitner–Dick provide a conceptual starting point, but their scalar quadrature discrepancy does not imply the Euclidean vector trace problem or its optimizer classification. Cianchi–Ferone–Nitsch–Trombetti optimize mean-value BV **boundary trace** constants over Euclidean domains, not discrete arclength sample sites on a periodic one-dimensional manifold. Cianchi–Maz'ya treat Sobolev embeddings and continuous boundary trace norms in arbitrary Euclidean domains; Lahti–Shanmugalingam establish existence and \(L^1\) bounds for BV traces on metric domains. Neither of these addresses the exact finite-cut objective (1) or the nonunique alternating optimal designs (3). A separate published research-index comparison identified work on \(H^1\) circular evaluation with a *measure augmented by atoms*, on periodic spline projection, and on discrete cycle derivative embeddings. Those have different derivative norms, centering, and target operators, and do not imply (1)–(3).

## Limitations
The minimization is for real periodic \(W^{1,1}\) functions and unnormalized \(\ell^2\) measurement errors only. No theorem is claimed for complex-valued functions, other derivative exponents, weighted measurement norms, noisy samples, or arbitrary compact graphs. Priority risk remains from unindexed circle-specific Poincaré sampling literature; literature-index absence is not a proof of novelty. The checker verifies rational test families, not all continuous node placements. The sharp constant is a supremum approached by steep two-jump profiles.

## References
- A. Cianchi, V. Ferone, C. Nitsch, C. Trombetti, *Balls minimize trace constants in BV*, arXiv:1301.5770 (first public 2013-01-24), https://arxiv.org/abs/1301.5770.
- C. Aistleitner and J. Dick, *Functions of bounded variation, signed measures, and a general Koksma–Hlawka inequality*, arXiv:1406.0230 (first public 2014-06-02), https://arxiv.org/html/1406.0230v2.
- A. Cianchi and V. Maz'ya, *Sobolev inequalities in arbitrary domains*, arXiv:1501.01257 (first public 2015-01-04), https://arxiv.org/html/1501.01257v1.
- P. Lahti and N. Shanmugalingam, *Trace theorems for functions of bounded variation in metric spaces*, arXiv:1507.07006 (first public 2015-07-24), https://arxiv.org/abs/1507.07006.
