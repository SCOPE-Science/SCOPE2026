# Walsh spectral soft thresholding has sharp Boolean-cube variation amplification of order \(2^{d/2}\)

## Finding
Fix an integer \(d\ge1\) and put \(N=2^d\). Let \(Q_d\) be the unit-edge Boolean cube, with real vertex signals and edge total variation \(V_d(f)=\sum_{i=1}^d\sum_{x:x_i=0}|f(x)-f(x\oplus e_i)|\). Let \(T_{d,\lambda}\), for \(\lambda>0\), preserve the constant Walsh coefficient and apply scalar soft thresholding to every other orthonormal Walsh coefficient. Its **sharp two-input** variation modulus
\[
L_d=\sup_{V_d(f-g)>0}\frac{V_d(T_{d,\lambda}f-T_{d,\lambda}g)}{V_d(f-g)}
\]
is independent of \(\lambda\), attained by two distinct inputs, and has the **exact finite spectral-cut formula**
\[
L_d=\max_{A\subseteq \mathbb F_2^d\setminus\{0\}}\;\max_{\varnothing\ne B\subsetneq\mathbb F_2^d}
\frac{V_d(P_A\mathbf 1_B)}{|\partial B|},
\qquad
(P_Af)(x)=\frac1N\sum_{s\in A}\sum_{y\in\mathbb F_2^d}(-1)^{s\cdot(x+y)}f(y).
\]
Here \(|\partial B|=V_d(\mathbf1_B)\), and the inner product in the exponent is over \(\mathbb F_2\). For every \(d\ge1\),
\[
\boxed{\max\left\{1,\;2-\frac4N,\;\frac{N-2}{2\sqrt{6N}}\right\}\le L_d\le\sqrt N.}
\]
In particular \(L_d=\Theta(2^{d/2})\). Exhaustive exact finite enumeration gives \(L_1=L_2=1\) and \(L_3=3/2\); hence strict two-input variation expansivity begins at dimension three and persists at all greater dimensions.

## Assumptions and scope
Vertices are the finite abelian group \(\mathbb F_2^d\) and two vertices are adjacent if they differ in exactly one coordinate. Every undirected edge is counted once and has unit weight. Inputs are arbitrary real vectors; no positivity, sparsity or stochastic distribution is assumed. The Walsh characters are \(\chi_s(x)=(-1)^{s\cdot x}\), with orthonormal basis \(N^{-1/2}\chi_s\) under the ordinary Euclidean inner product. For scalar threshold \(\lambda>0\), the transform coefficient \(c_s\) is replaced by \(\operatorname{sgn}(c_s)(|c_s|-\lambda)_+\) for \(s\ne0\), while \(c_0\) is unchanged. The variation seminorm ignores constants, and \(L_d\) is the supremum over pairs with positive denominator.

## Proof
**1. All spectral masks and their sharp global maximum.** In an open coefficient chamber of soft thresholding, the derivative of \(T_{d,\lambda}\) is the orthogonal Fourier–Walsh projection \(P_A\), where \(A\) consists of the nonconstant coefficients above threshold in absolute value. The preserved constant projection may be added without changing any variation. Every subset \(A\) is realizable: take orthonormal Walsh coefficients equal to \(2\lambda\) on \(A\), zero on the others, and choose any constant coefficient. On a sufficiently small neighborhood, the difference of the outputs for two input points equals \(P_A\) of their difference, up to an irrelevant constant. Along a line segment, the coordinatewise piecewise-affine soft threshold has finitely many slopes; integration yields
\[
V_d(T_{d,\lambda}f-T_{d,\lambda}g)\le\left(\max_A\|P_A\|_{V_d\to V_d}\right)V_d(f-g).
\]
Conversely, local realization of every mask produces an exactly attaining two-input pair for any norm-attaining direction of \(P_A\). Thus \(L_d=\max_A\|P_A\|_{V_d\to V_d}\), independently of the positive threshold.

**2. Cut extremizers.** On every finite graph, each real signal has the layer-cake representation \(h=\min_x h(x)+\int_{\min h}^{\max h}\mathbf1_{\{h>t\}}\,dt\), while discrete coarea gives \(V_d(h)=\int|\partial\{h>t\}|\,dt\). Since \(P_A\) kills constants, the triangle inequality and coarea give
\[
V_d(P_Ah)\le\bigg(\max_{\varnothing\ne B\subsetneq\mathbb F_2^d}\frac{V_d(P_A\mathbf1_B)}{|\partial B|}\bigg)V_d(h).
\]
Equality in the operator norm follows by using the maximizing indicator. Finite maximization and the local chamber argument prove the exact spectral-cut formula and attainment.

**3. Universal upper bound.** Let \(D_i f(x)=f(x)-f(x\oplus e_i)\). Fourier–Walsh projections commute with \(D_i\), and an orthogonal projection on \(\mathbb R^N\) has \(\ell^1\)-operator norm at most \(\sqrt N\), by \(\|Pv\|_1\le\sqrt N\|Pv\|_2\le\sqrt N\|v\|_2\le\sqrt N\|v\|_1\). Therefore
\[
V_d(P_Ah)=\frac12\sum_{i=1}^d\|P_A D_ih\|_1\le\sqrt N\,V_d(h).
\]

**4. Explicit deterministic lower bounds.** Taking all nonconstant characters gives \(P_A=I-P_{\{0\}}\) and hence \(L_d\ge1\). For \(d\ge2\), omit additionally the parity character \(\chi_{(1,\ldots,1)}\), so \(P_A=I-P_{\{0\}}-P_{\{(1,\ldots,1)\}}\). For a singleton indicator \(h=\mathbf1_{\{0\}}\), each of the \(d\) edges at zero contributes \(1-2/N\) to \(V_d(P_Ah)\), while the remaining \(d(N/2-1)\) edges each contribute \(2/N\). Consequently
\[
\frac{V_d(P_Ah)}{V_d(h)}=2-\frac4N.
\]
For every \(d\ge3\) this exceeds one, proving the onset assertion once the two-dimensional finite case is checked.

**5. A square-root lower bound for all dimensions.** Independently include every nonconstant character in \(A\) with probability \(1/2\). Write its membership as \(\eta_s=(1+\varepsilon_s)/2\) with independent Rademacher signs. For each coordinate \(i\) and each \(x\notin\{0,e_i\}\), orthogonality of characters on the affine frequency halfspace \(\{s:s_i=1\}\) cancels the deterministic mean, giving
\[
D_i(P_A\mathbf1_{\{0\}})(x)=\frac1N\sum_{s:s_i=1}\varepsilon_s\chi_s(x).
\]
The sum contains exactly \(m=N/2\) independent symmetric signs. It has second moment \(m\) and fourth moment \(3m^2-2m\le3m^2\). Hölder interpolation implies \(\mathbb E|\sum_{j=1}^m\varepsilon_j|\ge (\mathbb E Y^2)^{3/2}/(\mathbb E Y^4)^{1/2}\ge\sqrt{m/3}\). Summing over the \(N-2\) eligible vertices and dividing by two for oriented-edge double counting yields
\[
\mathbb E_A V_d(P_A\mathbf1_{\{0\}})\ge\frac{d(N-2)}{2\sqrt{6N}}.
\]
Since \(V_d(\mathbf1_{\{0\}})=d\), at least one concrete deterministic spectral mask meets the asserted lower bound. Combining Steps 3 and 5 proves \(L_d=\Theta(\sqrt N)=\Theta(2^{d/2})\).

**6. The exact small dimensions.** The supplied exact-integer/rational checker enumerates every one of the \(2^{N-1}\) spectral masks and every one of the \(2^N-2\) nontrivial indicator cuts for each \(d=1,2,3\), computing every numerator from the Walsh projection formula in Step 2 and verifying the maximum values \(1,1,3/2\). This is a complete finite proof of those three exact values, not sampling of possible masks or cuts. Step 4 proves strictly greater-than-one gain at every \(d\ge3\).

## Verification
Run the self-contained Python 3 script `verify.py` from this directory. It uses only the standard library, enumerates every mask and nontrivial cut for dimensions one through three, and verifies that two real inputs in the same strict threshold chamber exactly attain the resulting norm. Separate integer-only computations produce single-vertex sharp witnesses for selected masks through dimension nine. Those latter witnesses corroborate the square-root-growth construction; they are not a proof for unbounded dimension, which is supplied by Steps 3–5. The exact enumeration establishes the stated small-dimension values, while the proof is independent of numerical extrapolation.

## Relationship to prior work
Chen, Sandryhaila, Moura and Kovačević (arXiv:1411.7414, first posted November 26, 2014) analyze graph signal recovery and graph spectral variation objectives; their inspected paper explicitly adopts a quadratic graph-variation objective, not the current two-input edge-\(\ell^1\) norm of nonlinear Walsh coefficient shrinkage. Cheraghchi and Indyk (arXiv:1504.07648, first posted April 28, 2015) give the Walsh–Hadamard normalization and sparse recovery framework, not graph-total-variation operator norms. Closely related Walsh projection results on the Hamming cube compute Lipschitz-\(\ell^\infty\) or Lipschitz-free projection norms by coordinate-shadow kernels; these use the **maximum** edge difference (or its dual), whereas the present problem uses the **sum** of edge differences and reduces to all graph cuts. Other basis-dependent soft-threshold variation estimates on finite paths, including DCT-II and Haar, do not imply the Boolean-cube graph-variation mask/cut formula or its exponential dependence on cube dimension. The coarea and norm inequalities are standard ingredients; the new object-specific identification and the dimension-growth statement are the claimed contribution.

## Limitations
The leading asymptotic constant in \(L_d/2^{d/2}\) is not determined. The exponential lower bound is existential in the spectral-mask selection and does not identify all maximizing masks. The theorem concerns unweighted Boolean-cube **edge** total variation, standard real Walsh coefficients and identical positive soft thresholds on all nonconstant coefficients. Unequal edge weights, complex data, non-Walsh bases, nonlinear adaptive thresholds and other graph families remain outside scope. Literature searching cannot exclude every unindexed equivalent or stronger historical result. No independent mathematical audit is claimed.

## References
1. S. Chen, A. Sandryhaila, J. M. F. Moura, J. Kovačević, *Signal Recovery on Graphs: Variation Minimization*, arXiv:1411.7414v1, first public November 26, 2014, https://arxiv.org/abs/1411.7414.
2. M. Cheraghchi, P. Indyk, *Nearly Optimal Deterministic Algorithm for Sparse Walsh-Hadamard Transform*, arXiv:1504.07648v1, first public April 28, 2015, https://arxiv.org/abs/1504.07648.
3. *Coordinate-shadow norm formula for Walsh projections on Hamming Lipschitz-free spaces*, publicly accessible research text, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-coordinate-shadow-norm-formula-for-walsh-projections-on-hamming--6d24f15eba8d (mathematically different Lipschitz-free norm).
4. M. T. Lacey and Y. Do, *Weighted bounds for variational Walsh-Fourier series*, arXiv:1112.1744 (Fourier-sum index variation rather than spatial graph total variation).
