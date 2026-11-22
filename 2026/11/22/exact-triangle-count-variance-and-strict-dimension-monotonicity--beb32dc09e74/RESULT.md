# Exact triangle-count variance and strict dimension monotonicity in spherical hemisphere graphs

## Finding

Let \(n\geq3\) and \(d\geq1\) be integers. Sample \(X_1,\ldots,X_n\) independently and uniformly from the sphere \(S^{d-1}\subset\mathbb R^d\), and join \(i\) to \(j\) when \(\langle X_i,X_j\rangle>0\). Let \(T_{n,d}\) count the unordered vertex triples inducing complete triangles. For independent uniform \(X,Y\), put \(R_d=|\langle X,Y\rangle|\), and define
\[
 u_d=\frac{\mathbb E\arcsin R_d}{4\pi},\qquad
 h_d=\frac{\mathbb E(\arcsin R_d)^2}{8\pi^2},\qquad
 p_d=\frac18+u_d,\qquad
 c_d=\frac1{64}+\frac{u_d}{4}+h_d-u_d^2.
\]
Then the following are exact for all such \(n,d\):
\[
 \mathbb ET_{n,d}=\binom n3p_d,\qquad
 \operatorname{Var}(T_{n,d})=\binom n3p_d(1-p_d)+2\binom n2\binom{n-2}2c_d.
\]
For each fixed \(n\ge3\), both \(\mathbb ET_{n,d}\) and \(\operatorname{Var}(T_{n,d})\) are **strictly decreasing** as the ambient integer dimension \(d\) increases. In particular, all finite-dimensional triangle-count variances strictly exceed the independent-edge \(G(n,1/2)\) benchmark
\[
 V_{n,\infty}=\frac7{64}\binom n3+\frac1{32}\binom n2\binom{n-2}2.
\]
The first three dimensions have explicit constants:
\[
 (p_1,c_1)=(\tfrac14,\tfrac1{16}),\quad
 (p_2,c_2)=(\tfrac3{16},\tfrac{29}{768}),\quad
 (p_3,c_3)=(\tfrac14-\tfrac1{4\pi},\tfrac{\pi^2-5}{16\pi^2}).
\]
Moreover, for every fixed \(n\ge3\), as \(d\to\infty\) through positive integers,
\[
 \operatorname{Var}(T_{n,d})-V_{n,\infty}
 =\frac{\frac34\binom n3+\frac12\binom n2\binom{n-2}2}{2\pi\sqrt{2\pi d}}+O_n(d^{-1}).
\]
Thus the excess variance has a **strict positive leading constant** and vanishes at the \(d^{-1/2}\) rate.

## Assumptions and scope

The graph has a deterministic number \(n\) of i.i.d. sphere-uniform vertices, independent across vertices; edges are deterministic halfspace tests with threshold exactly zero, not independently resampled edges. The dimension can be any positive integer. The sphere \(S^0\) comprises the two equally likely points \(\{-1,+1\}\). All graph triangle counts are over unordered triples, and all covariance and variance statements concern that fixed graph distribution. The asymptotic error constant can depend on fixed \(n\); no uniformity in a growing number of vertices is asserted.

For \(d\ge2\), \(R_d\) has density
\[
 f_{R_d}(r)=\frac{2\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-r^2)^{(d-3)/2},\quad0<r<1,
\]
and \(R_1=1\) almost surely. These formulas give fully explicit convergent one-dimensional integrals for the two constants in any dimension.

## Proof

**1. Conditional wedge.** Fix distinct sampled vertices \(X_1=x\), \(X_2=y\), with \(c=\langle x,y\rangle\). A new uniform spherical vertex \(Z\) has both dot products positive exactly when its projection onto the two-dimensional span of \(x,y\) lies in a wedge of angle \(\pi-\arccos c\). Rotational invariance therefore gives the exact probability
\[
 a(c)=\Pr(\langle Z,x\rangle>0,\langle Z,y\rangle>0\mid x,y)
 =\frac14+\frac{\arcsin c}{2\pi}.
\]
For dimension one the same identity holds at the only possible inputs \(c=\pm1\): the two conditional probabilities are respectively \(1/2\) and \(0\).

**2. Single triangle and two triangles sharing an edge.** Let \(C=\langle X_1,X_2\rangle\) and \(I_{ijk}\) indicate that triple \(i,j,k\) forms a triangle. By the wedge formula,
\[
 \mathbb EI_{123}=\mathbb E[\mathbf1_{\{C>0\}}a(C)]
 =\frac18+\frac{\mathbb E\arcsin|C|}{4\pi}=p_d.
\]
Here symmetry of \(C\) was used. Given \(X_1,X_2\), the indicators \(I_{123},I_{124}\) are conditionally independent, hence
\[
 \mathbb E[I_{123}I_{124}]
 =\mathbb E[\mathbf1_{\{C>0\}}a(C)^2]
 =\frac1{32}+\frac{u_d}{2}+h_d.
\]
Their covariance is therefore \(c_d=1/64+u_d/4+h_d-u_d^2\).

**3. Independence for smaller overlaps and counting pairs.** Disjoint triples involve independent samples. For triples with just one common vertex \(X_i\), condition on that vertex. Each triangle event uses disjoint remaining samples, and its conditional probability is \(p_d\), independent of the chosen \(X_i\) by rotation invariance, so these triangle events are independent unconditionally. Only a common edge creates a covariance contribution. There are \(\binom n3\) diagonal indicators and \(\binom n2\binom{n-2}2\) unordered pairs of distinct triangles sharing an edge. The factor two in the covariance expansion gives the exact displayed variance.

**4. Strict decrease with dimension.** Couple all dimensions using one infinite sequence \(G_1,G_2,\ldots\) of independent standard Gaussian variables:
\[
 R_d\ \overset{\mathrm{law}}=\ \frac{|G_1|}{\sqrt{G_1^2+\cdots+G_d^2}}.
\]
This coupling is strictly decreasing at every dimension increment almost surely. Since \(\arcsin\) and its square are strictly increasing on \((0,1)\), both \(u_d\) and \(h_d\) strictly decrease. Also \(0<u_d\le1/8\), so \(u\mapsto u/4-u^2\) is nondecreasing over the full range. Therefore \(p_d\) and \(c_d\) decrease strictly, while \(p\mapsto p(1-p)\) is strictly increasing on \([1/8,1/4]\). The exact variance formula now proves the strict dimension comparison for every \(n\ge3\). The limiting values \(u_d,h_d\to0\) follow from the coupling and bounded convergence; they give the strict excess over \(V_{n,\infty}\).

**5. Exact low dimensions.** For \(d=1\), \(R_d=1\), giving \(u_1=1/8\), \(h_1=1/32\). For \(d=2\), write the random angle as \(\Theta\sim\mathrm{Uniform}[0,\pi]\); then \(\arcsin|\cos\Theta|=|\pi/2-\Theta|\), whose first and second moments are \(\pi/4\) and \(\pi^2/12\). This yields \(p_2=3/16\) and \(c_2=29/768\). For \(d=3\), \(R_3\) is uniform on \([0,1]\), so \(\mathbb E\arcsin R_3=\pi/2-1\) and \(\mathbb E(\arcsin R_3)^2=\pi^2/4-2\), giving the stated \(p_3,c_3\).

**6. Sharp high-dimensional coefficient.** The beta/gamma integral gives
\[
 \mathbb ER_d=\frac{\Gamma(d/2)}{\sqrt\pi\Gamma((d+1)/2)}
 =\sqrt{\frac2{\pi d}}+O(d^{-3/2}),\qquad
 \mathbb ER_d^2=\frac1d.
\]
The bounds \(\arcsin r=r+O(r^3)\) and \((\arcsin r)^2=r^2+O(r^4)\), uniformly for \(0\le r\le1\), together with beta moments \(\mathbb ER_d^3=O(d^{-3/2})\) and \(\mathbb ER_d^4=O(d^{-2})\), yield
\[
 u_d=\frac1{2\pi\sqrt{2\pi d}}+O(d^{-3/2}),\qquad
 h_d=\frac1{8\pi^2d}+O(d^{-2}).
\]
Subtract the limiting variance, expand \(p_d(1-p_d)=7/64+(3/4)u_d-u_d^2\) and \(c_d=1/64+(1/4)u_d+h_d-u_d^2\), then collect the leading \(d^{-1/2}\) term. This proves the final asymptotic, with error \(O_n(d^{-1})\).

## Verification

The included standalone \(\texttt{check_variance.py}\) uses only the Python standard library. It exhaustively enumerates all sign assignments for \(d=1\), \(3\le n\le10\), verifying the exact expectation and variance as rational numbers; independently checks the exact angular integration constants for \(d=2\); compares numerical integral evaluations with the exact \(d=2,3\) formulas; and tests dimension monotonicity and the leading asymptotic at a finite selection of dimensions. Running \(\texttt{python3 check_variance.py}\) produces 60 passing deterministic assertions. Those finite checks do not prove the universal statements; steps 1–6 above are the proof.

## Relationship to prior work

The spherical geometric-graph model and triangle count are standard: Bubeck, Ding, Eldan and Rácz (arXiv:1411.5713, especially Sections 1–3 and the sparse-triangle second-moment estimate in Section 4) prove detection results and bounds for triangle expectations/variances, and emphasize signed-triangle statistics. Their sparse second-moment argument invokes the same overlap decomposition but supplies inequalities, not this exact all-dimension covariance, strict dimension order, or sharp positive variance excess. Bok, Li and Yu (arXiv:2603.24545, Sections 4 and Appendix B) study signed-triangle test variance for planted geometry and do not establish the present uncentered triangle-count classification. Deka, Luo and Wu (arXiv:2510.09196v1, first public 2025-10-10) study rare complete graphs and atypical edge counts, motivating a finite-dimensional exact invariant beyond those large-deviation conclusions. Hunter, Milojević and Sudakov (arXiv:2607.22480v1) analyze geometry distinguishability and a joint graph-probability approximation, not strict finite-d variance monotonicity. The conclusions here are particular to deterministic hemisphere-threshold edges, rather than affine-randomized links or Euclidean triangle-acuteness events.

## Limitations

The results apply only at edge density \(1/2\) (hemisphere threshold zero) and assume i.i.d. isotropic spherical samples. No claim is made for nonzero thresholds, sparse regimes, growing \(n\) at the same time as \(d\), higher cumulants, or optimal statistical testing. The exact formulas are integrals, not elementary closed forms in every dimension. The published-paper search does not certify absolute historical priority; in particular, equivalent formulas may occur under different terminology. Independent mathematical validation has not been carried out.

## References

- P. Deka, F. Luo, B. Wu, *Rare event probabilities in random geometric graphs*, arXiv:2510.09196v1 (first public 2025-10-10), https://arxiv.org/abs/2510.09196.
- S. Bubeck, J. Ding, R. Eldan, M. Z. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713, https://arxiv.org/abs/1411.5713.
- J. Bok, S. Li, S. H. Yu, *Detection of local geometry in random graphs: information-theoretic and computational limits*, arXiv:2603.24545v1, https://arxiv.org/html/2603.24545.
- Z. Hunter, A. Milojević, B. Sudakov, *Distinguishability threshold for random geometric graphs*, arXiv:2607.22480v1, https://arxiv.org/abs/2607.22480.
