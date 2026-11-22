# Full Euclidean chord spectrum and Gaussian overlap law of wheel spanning-tree polytopes

## Finding

Let \(W_m=K_1\vee C_m\) be the labelled wheel with \(m\ge3\) rim vertices, \(m\) spokes and \(m\) rim edges, and let \(P_m\subset\mathbb R^{2m}\) be the convex hull of the standard edge-indicator vectors of its spanning trees. For two independent, uniformly selected spanning trees \(T,U\), put \(X_m=|T\cap U|\) and \(Q_m=\|\mathbf1_T-\mathbf1_U\|^2=2(m-X_m)\).

**Theorem (complete ordered chord spectrum).** The polynomial \(F_m(q)=\sum_{T,U}q^{|T\cap U|}\) is, for every \(m\ge3\),

\[
\boxed{F_m(q)=\operatorname{tr}(M(q)^m)-4\operatorname{tr}(A(q)^m)+4q^m,}
\]

where all matrix entries are polynomials and

\[
M(q)=\begin{pmatrix}
2+2q&2q&2q&q^2\\
2&1+q&1&q\\
2&1&1+q&q\\
1&1&1&q
\end{pmatrix},\qquad
A(q)=\begin{pmatrix}1+q&q\\1&q\end{pmatrix}.
\]

Thus \([q^k]F_m(q)\) counts ordered polytope-vertex pairs at squared Euclidean distance \(2(m-k)\), including the diagonal when \(k=m\). A complete unordered distinct-vertex distance histogram is obtained by halving each coefficient for \(k<m\).

**Theorem (Gaussian chord fluctuations).** Define

\[
\mu=\frac{7-2\sqrt5}{5},\qquad
\sigma^2=\frac{22\sqrt5-30}{125}>0.
\]

As \(m\to\infty\),

\[
\frac{X_m-\mu m}{\sqrt{\sigma^2m}}\ \Longrightarrow\ N(0,1).
\]

Equivalently, \((Q_m-2(1-\mu)m)/(2\sqrt{\sigma^2m})\) converges to a standard normal distribution (up to sign, which does not change the limit). In particular, \(\mathbb E Q_m/m\to 2(1-\mu)\) and \(\operatorname{Var}(Q_m)/m\to4\sigma^2\). The exactly known endpoint \([q^0]F_m(q)=2^{m+1}-4\) is a consistency check, not claimed as a new complementary-tree count.

## Assumptions and scope

Each rim edge \(r_i\) joins vertex \(i\) to \(i+1\) modulo \(m\); each spoke \(s_i\) joins rim vertex \(i\) to the hub. Every tree has \(m\) edges and its edge-indicator is a distinct vertex of the graphic-matroid base polytope. The metric is the unweighted Euclidean metric of the \(2m\) edge coordinates; there is no graph shortest-path or minimum-weight tree metric. The pair enumeration is **ordered**, with replacement, and the Gaussian statement concerns independent vertex-uniform sampling.

## Proof

**1. Cyclic finite-state encoding of a tree.** The chosen rim edges of a spanning tree cannot contain the full rim cycle. They form paths, including singleton paths, and each path must have exactly one spoke: zero leaves it disconnected from the hub, two create a cycle through the hub. Conversely, this property yields a spanning tree. Scan successive rim vertices cyclically. A bit \(c\) records whether the current rim component has already received a spoke before the present vertex. At a vertex select a spoke bit \(s\) and the outgoing rim-edge bit \(r\). All allowed transitions are exactly

\[
\begin{array}{c|ccc}
c& (s,r,c_{\rm next})\\ \hline
0&(0,1,0)&(1,0,0)&(1,1,1)\\
1&(0,0,0)&(0,1,1)&
\end{array}
\]

(the unused table entry is ignored). When \(r=0\), the component ends and its spoke count must equal one, so the new state is zero. When \(r=1\), the component continues. Every valid tree has at least one missing rim edge and therefore exactly one cyclic state path. The only additional cyclic state paths are the two constant-state paths representing **all rim edges and no spokes**, an invalid wheel spanning tree. Call this extra edge set \(R\).

**2. Exact pair-weight transfer and subtraction.** For two state paths, write the state pair in order \((0,0),(0,1),(1,0),(1,1)\). Give each simultaneous local choice weight \(q^{ss'+rr'}\), so that multiplying over all \(m\) vertices yields \(q^{|T\cap U|}\). Summing the five allowed single-path transitions in each coordinate gives exactly the displayed \(4\)-by-\(4\) matrix \(M(q)\). Likewise, weighting a single path by \(q^r\) yields \(A(q)\). Consequently, \(\operatorname{tr}M(q)^m\) counts every valid ordered pair once, each pair with one invalid factor twice, and the pair \((R,R)\) four times. If \(S(q)=\sum_{T\text{ tree}}q^{|T\cap R|}\), then

\[
\operatorname{tr}A(q)^m=S(q)+2q^m,
\qquad
\operatorname{tr}M(q)^m=F_m(q)+4S(q)+4q^m.
\]

Eliminating \(S(q)\) proves the formula \(F_m=\operatorname{tr}M^m-4\operatorname{tr}A^m+4q^m\), including the two subtle spurious cyclic histories. Finally, \(\|\mathbf1_T-\mathbf1_U\|^2=2m-2|T\cap U|\), proving the Euclidean histogram interpretation.

**3. Spectral analysis for all large wheels.** Direct determinant expansion gives

\[
\det(\lambda I-M(q))=(\lambda-q)
\bigl[\lambda^3-4(q+1)\lambda^2+4(q^2+1)\lambda-q^3\bigr].
\]

At \(q=1\), \(M(1)\) has strictly positive entries, so its Perron eigenvalue is simple and strictly dominates every other eigenvalue in modulus. The Perron eigenvalue is \(\Lambda=(7+3\sqrt5)/2\). The spectral radius of \(A(1)\) is \((3+\sqrt5)/2<\Lambda\), and the correction \(4q^m\) is also exponentially subordinate near \(q=1\). Analytic matrix perturbation therefore gives, uniformly for complex \(t\) in a fixed sufficiently small neighborhood of zero,

\[
\mathbb E e^{tX_m}=\frac{F_m(e^t)}{F_m(1)}
=\left(\frac{\lambda(e^t)}{\Lambda}\right)^m\bigl(1+O(\theta^m)\bigr),\quad0<\theta<1,
\]

where \(\lambda(q)\) is the analytic continuation of the positive Perron root. The constant implicit in the error is uniform near zero. The nondegenerate second derivative of \(\log\lambda(e^t)\) yields the central limit theorem by the characteristic-function method, expanding at \(t=iu/\sqrt m\).

**4. Exact constants.** Implicit differentiation of the cubic factor \(p(\lambda,q)=0\) at \((\lambda,q)=(\Lambda,1)\) gives

\[
\frac{\lambda'(1)}{\Lambda}=\frac{7-2\sqrt5}{5},
\qquad
\frac{\lambda'(1)}{\Lambda}+\frac{\lambda''(1)}{\Lambda}
-\left(\frac{\lambda'(1)}{\Lambda}\right)^2
=\frac{22\sqrt5-30}{125}>0.
\]

These are precisely the first two cumulants per rim vertex for \(X_m\). The positive variance establishes a nondegenerate Gaussian limit, and the exact moment asymptotics follow by differentiating the uniform analytic expression near zero.

## Verification

The accompanying standalone `check_wheel_chords.py` contains an independent union-find spanning-tree enumerator, a separate exact integer polynomial matrix-power evaluator, and finite asymptotic-moment checks. Run `python3 check_wheel_chords.py`. For every \(3\le m\le8\), it enumerates all \(m\)-edge subsets of the wheel, retains precisely the spanning trees, computes all \(5{,}688{,}628\) ordered tree pairs, and compares each coefficient of the complete enumerated polynomial with the matrix identity. The end coefficients, the total wheel tree counts, and moment ratios at \(m=20,40,80\) are also tested. The success marker is `WHEEL_TREE_CHORD_PASS`. The infinite-size result is proved by the transfer and spectral arguments above, not inferred from these finite tests.

## Relationship to prior work

The wheel spanning-tree count \(L_{2m}-2\) is classical (Benjamin and Yerger). A previously published exact wheel basis-exchange diameter and complementary-pair census already establishes \([q^0]F_m=2^{m+1}-4\); the current theorem does not claim those endpoints as original. Existing wheel spanning-tree vertex-covariance formulas determine first and second overlap moments but do not specify the complete pair-distance histogram. Published wheel Fourier results classify vanishing Walsh coefficients and sharp nonzero multipliers without supplying the full distribution of pairwise Euclidean tree-incidence distances. In contrast, the present polynomial describes **all** \(m+1\) overlap coefficients simultaneously and gives a wheel-specific nondegenerate Gaussian limit with exact mean and variance.

Bóna and Wagner's study of the intersection of independent spanning trees (2025) covers complete graphs, Erdős–Rényi graphs, and complete multipartite families, with Poisson limits in its dense regimes. Its inspected text does not treat the fixed-degree wheel family and does not establish the transfer polynomial or Gaussian constants here. Pineda-Villavicencio and Schröter (2020) establish general geometric and combinatorial properties of matroid polytopes, but no vertex-pair Euclidean histogram of the wheel family. This is a new calculation relative to the inspected statements, not an assertion that all unindexed equivalent formulas are absent.

## Limitations

The theorem is limited to unweighted labelled wheels and uniform vertex pairs; it does not give the full two-tree overlap law for arbitrary matroid base polytopes or weighted random trees. The integer transfer identity is exact for each \(m\), but only the asymptotic Gaussian limit (not a local limit theorem or a Berry–Esseen bound) is asserted. The closed-form endpoint coefficients and wheel spanning-tree total are acknowledged as prior knowledge. Relevant published literature has been inspected, but historical priority remains provisional pending broader independent checking.

## References

- G. Pineda-Villavicencio and B. Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227v1 (first public 2020-10-20), MSC2020 52B11 (05C60), https://arxiv.org/abs/2010.10227.
- A. T. Benjamin and C. R. Yerger, *Combinatorial Interpretations of Spanning Tree Identities*, Bulletin of the Institute of Combinatorics and Its Applications 47 (2006), 37–42; author-hosted PDF: https://math.hmc.edu/benjamin/wp-content/uploads/sites/5/2019/06/Combinatorial-Interpretations-of-Spanning-Tree-Identities.pdf.
- M. Bóna and S. Wagner, *On the intersection of pairs of trees*, arXiv:2501.18570v1 (2025-01-30), https://arxiv.org/abs/2501.18570.
- *Wheel spanning-tree exchange centers and complementary-tree census*, published mathematical research record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-wheel-spanning-tree-exchange-centers-and-complementary-tree-cens--6102930841e3.
- *Quadratic vertex-covariance anisotropy of wheel spanning-tree polytopes*, published mathematical research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-quadratic-vertex-covariance-anisotropy-of-wheel-spanning-tree-po--20c51f1ae988.
- *Period-three Fourier singularity and fourfold divisibility for wheel spanning-tree kernels*, published mathematical research record (2026-11-16), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-period-three-fourier-singularity-and-fourfold-divisibility-for-w--8adb2e48710a.
