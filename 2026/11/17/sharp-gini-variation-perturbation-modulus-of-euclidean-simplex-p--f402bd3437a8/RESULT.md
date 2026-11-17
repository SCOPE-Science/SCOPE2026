# Sharp Gini-variation perturbation modulus of Euclidean simplex projection

## Finding

For \(n\ge2\), \(r>0\), define the positive-mass simplex
\[
\Delta_{n,r}=\{z\in\mathbb R^n: z_i\ge0,\ \sum_{i=1}^nz_i=r\}
\]
and its ordinary Euclidean nearest-point map \(P_r\). Equip real vectors modulo constants with the **complete-graph Gini-variation seminorm**
\[
G_n(z)=\sum_{1\le i<j\le n}|z_i-z_j|.
\]
Then the optimal two-input modulus is exactly
\[
\boxed{L_n:=\sup_{G_n(x-y)>0}\frac{G_n(P_rx-P_ry)}{G_n(x-y)}
=\max_{2\le k\le n}\frac{(k-1)(2n-k)}{k(n-1)}.}
\]
It is independent of \(r>0\), and every maximum is attained. The maximizing integers \(k\in\{2,\ldots,n\}\) are precisely those satisfying \(k(k-1)\le2n\le k(k+1)\). The constant is \(1\) in dimensions two and three, strictly greater than \(1\) in every dimension \(n\ge4\), and obeys
\[
\lim_{n\to\infty}L_n=2,\qquad
\lim_{n\to\infty}\sqrt n(2-L_n)=2\sqrt2.
\]
Nonetheless \(G_n(P_rx)\le G_n(x)\) holds for every individual input. The sharp two-input modulus measures a different, genuinely larger notion of perturbation stability.

## Assumptions and scope

The inputs and outputs are real vectors, projection is uniquely defined by squared Euclidean distance, and the variation sums unit-weight differences over **every** unordered coordinate pair (the unweighted complete graph). A vector has zero Gini variation precisely when it is constant. Since \(P_r(x+c\mathbf1)=P_r(x)\), the two-input quotient is well-defined on the quotient modulo constants. Every integer \(n\ge2\) and every real simplex mass \(r>0\) is included; no restriction is imposed on input signs or magnitudes.

## Proof

**1. Every support yields an affine cell.** The simplex KKT conditions give \((P_rx)_i=(x_i-\tau)_+\), where \(\sum_i(x_i-\tau)_+=r\). For a fixed, nonempty active support \(S\subseteq\{1,\ldots,n\}\) of cardinality \(k\), the threshold is \(\tau=(\sum_{j\in S}x_j-r)/k\). The affine linear part is
\[
(J_Sh)_i=\begin{cases}h_i-k^{-1}\sum_{j\in S}h_j,&i\in S,\\0,&i\notin S.\end{cases}
\]
The choice \(x_i=r/k\) for \(i\in S\) and \(x_i=-r\) for \(i\notin S\) has threshold zero with strict support inequalities; hence every support occurs on an open cell. The map is continuous piecewise affine with finitely many cells. Integrating its affine slopes along each segment, and using small perturbations within every open cell for the reverse inequality, gives
\[
L_n=\max_{\varnothing\ne S\subseteq[n]}\|J_S\|_{G_n\to G_n}.
\]
Every \(J_S\) annihilates constants; the possible nondifferentiability on cell boundaries causes no difficulty.

**2. Cut indicators determine the operator norm.** For any real vector \(h\), sort its coordinates increasingly and write \(h\), modulo a constant, as a nonnegative linear combination of indicators \(\mathbf1_T\) of successive upper-level sets. The exact layer-cake identity is
\[
G_n(h)=\sum_{\text{successive levels }T}\alpha_T|T|(n-|T|),\qquad\alpha_T\ge0.
\]
Since \(J_S\mathbf1=0\), the triangle inequality and the reverse test with each individual cut give the exact formula
\[
\|J_S\|_{G_n\to G_n}
=\max_{\varnothing\ne T\subsetneq[n]}
\frac{G_n(J_S\mathbf1_T)}{|T|(n-|T|)}.
\]
This reduction is valid for all real inputs, not just binary ones.

**3. Optimize the active support and cut.** Put \(a=|S\cap T|\), \(b=|S\setminus T|\), \(c=n-k\), and \(u=|T\setminus S|\), so \(a+b=k\), \(0\le u\le c\). If \(a=0\) or \(b=0\), then \(J_S\mathbf1_T=0\). Otherwise its coordinate values are \(b/k\) on the \(a\) active selected positions, \(-a/k\) on the remaining \(b\) active positions, and zero outside \(S\). Therefore
\[
G_n(J_S\mathbf1_T)=ab\left(1+\frac{2c}{k}\right),\qquad
G_n(\mathbf1_T)=(a+u)(b+c-u).
\]
The denominator is concave as a function of \(u\in[0,c]\) and hence is at least its smaller endpoint value,
\[
\min\{a(b+c),\ b(a+c)\}.
\]
By swapping \(a,b\), suppose \(a\le b\). The cut ratio is at most
\[
\left(1+\frac{2c}{k}\right)\frac{b}{b+c}.
\]
For fixed \(k,c\), this is maximized by \(a=1\), \(b=k-1\) (if \(c=0\), it is constantly one). Choosing \(T\) to consist of one active coordinate attains the bound exactly. Thus, for every \(2\le k\le n\),
\[
\max_{|S|=k}\|J_S\|_{G_n\to G_n}
=\frac{(k-1)(2n-k)}{k(n-1)}.
\]
The singleton-support case has zero Jacobian. Maximizing over \(k\) proves the sharp formula.

**4. Finite-order structure and attained pairs.** The numerator of the preceding expression after multiplication by \(n-1\) equals \(2n+1-k-2n/k\). Consecutive support sizes differ by
\[
(n-1)(L_{n,k+1}-L_{n,k})=-1+\frac{2n}{k(k+1)}.
\]
Consequently all maximizing support sizes satisfy \(k(k-1)\le2n\le k(k+1)\), with adjacent ties exactly at \(2n=k(k+1)\). For any such \(k\), choose \(S=\{1,\ldots,k\}\), \(x_i=r/k\) in \(S\), and \(x_i=-r\) outside. Choose \(0<\varepsilon<r/k\) and put \(y=x+\varepsilon e_1\). Both projections have the same strict support, and
\[
P_ry-P_rx=\varepsilon J_Se_1,\qquad y-x=\varepsilon e_1.
\]
The ratio equals the displayed maximum, proving actual attainment by finite nonzero differences. Direct inspection of \(n=2,3\) gives one; already \(n=4,k=3\) gives \(10/9>1\), and the sharp formula is increasing with \(n\) for each fixed \(k\ge2\) once \(n\ge k\). Finally an optimal \(k\) differs from \(\sqrt{2n}\) by at most one, so \(k+2n/k=2\sqrt{2n}+O(n^{-1/2})\), yielding both limits.

**5. Single-input contractivity.** For each fixed input \(x\), the scalar function \(t\mapsto(t-\tau(x))_+\) is one-Lipschitz. Applying it to every coordinate shows \(|(P_rx)_i-(P_rx)_j|\le|x_i-x_j|\) for each pair and hence \(G_n(P_rx)\le G_n(x)\). The single-input statement does not imply the two-input estimate with constant one.

## Verification

Run `python3 checker.py` using Python 3.10 or later; only the Python standard library is needed. The independent exact-rational program enumerates 346,476 active-support/cut comparisons in dimensions two through nine, verifies 88 actual sharp-attainment pairs in dimensions two through 89, and checks 28,574 nontrivial rational two-input inequalities in dimensions two through eight. It computes the simplex projection independently by sorting and thresholding. These finite diagnostics do not replace the all-dimensional analytical proof given above.

## Relationship to prior work

The KKT threshold formula for Euclidean simplex projection and its algorithms are classical: Duchi et al. [1] and Condat [2] treat computation. Martins and Astudillo [3] derive the active-set Jacobian and observe its complete-graph Laplacian form; their results do not compute the norm under pairwise-coordinate-difference variation. An earlier mathematical record [4] computes the sharp two-input variation modulus of the same simplex map when variation uses **cyclic adjacent pairs** rather than all coordinate pairs. That result has a norm of order \(n\), while the present complete-graph norm tends to two, and the interval-cut calculation in [4] does not contain the complete-graph coarea calculation or the support-size transition found here. These differing function seminorms are not ordered by a sharp implication. Published \(\ell_p\)-stability estimates for simplex or cross-polytope projection use coordinate norms rather than the Gini-variation quotient and do not determine its sharp constant. The comparison concerns mathematical implications, not merely titles. An equivalent older result under Gini mean difference, pairwise dispersion, or nonlinear projection terminology remains a priority risk.

## Limitations

The theorem is for finite dimensions, standard positive-mass simplices, real Euclidean projection and unit-weight complete-graph variation. It is not an optimal constant for weighted pairwise variation, arbitrary graphs, or non-Euclidean metric projections. No claim of exhaustive historical priority or independent mathematical validation is made.

## References

[1] J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, *Efficient Projections onto the \(\ell_1\)-Ball for Learning in High Dimensions*, ICML 2008, DOI https://doi.org/10.1145/1390156.1390191, publicly published 2008-07-05.

[2] L. Condat, *Fast Projection onto the Simplex and the \(\ell_1\) Ball*, HAL-01056171v1 (2014), open-access preprint https://optimization-online.org/wp-content/uploads/2014/08/4498.pdf.

[3] A. Martins and R. Astudillo, *From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification*, arXiv:1602.02068v1 (publicly posted 2016-02-05), ICML 2016, PDF https://proceedings.mlr.press/v48/martins16.pdf, especially Proposition 1 and Eq. (12).

[4] *Sharp cyclic-variation amplification of Euclidean simplex projection*, 2026 mathematical record, identifier 95284892279a, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-cyclic-variation-amplification-of-euclidean-simplex-projec--95284892279a.
