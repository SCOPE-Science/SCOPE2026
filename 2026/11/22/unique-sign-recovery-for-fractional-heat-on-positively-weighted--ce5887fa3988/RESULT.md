# Unique sign recovery for fractional heat on positively weighted stars

## Finding

Consider a star on vertices \(\{0,1,\ldots,m\}\), with hub \(0\), \(m\ge2\) leaves, and arbitrary positive spoke conductances \(w_1,\ldots,w_m\). Let \(L\) be its symmetric combinatorial Laplacian, and define \(K_\alpha(t)=\exp(-tL^\alpha)\) by symmetric spectral calculus for \(\alpha>0\) and \(t\ge0\).

**Complete fractional-order sign classification.**

* If \(0<\alpha\le1\), every entry of \(K_\alpha(t)\) is strictly positive for every \(t>0\).
* If \(\alpha>1\), every diagonal entry and every hub–leaf entry is strictly positive for every \(t>0\). For **each** distinct leaf pair \(i\ne j\) there is exactly one finite number \(T_{ij}(\alpha,w)>0\) such that
  \[
  K_\alpha(t)_{ij}<0\quad(0<t<T_{ij}),\qquad
  K_\alpha(T_{ij})_{ij}=0,\qquad
  K_\alpha(t)_{ij}>0\quad(t>T_{ij}).
  \]
  This positive zero is simple.

Thus \(T_*(\alpha,w)=\max_{1\le i<j\le m}T_{ij}(\alpha,w)\) is the **sharp entrywise nonnegativity and maximum-norm contractivity horizon**:
\[
K_\alpha(t)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad
\|K_\alpha(t)\|_{\ell^\infty\to\ell^\infty}=1
\quad\Longleftrightarrow\quad t=0\text{ or }t\ge T_*\qquad(\alpha>1).
\]
At \(t=T_*\) at least one leaf-pair entry is zero; all entries are strictly positive for \(t>T_*\). For \(0<\alpha\le1\), entrywise positivity and maximum-norm contractivity hold at all positive times.

**Structural strengthening.** The entire \(\alpha>1\) conclusion continues to hold with \(L^\alpha\) replaced by \(\phi(L)\), for any strictly increasing, strictly convex real function \(\phi\) on the spectral interval \([0,\lambda_{\max}(L)]\) satisfying \(\phi(0)=0\). The recovery times then depend on \(\phi\). Strict convexity and increasingness are essential assumptions of this strengthening; no conclusion is claimed for arbitrary spectral multipliers.

## Assumptions and scope

Write \(W=\sum_{i=1}^m w_i\). In hub-first order,
\[
L=\begin{pmatrix}W&-w^{\mathsf T}\\-w&\operatorname{diag}(w)\end{pmatrix},
\qquad w=(w_1,\ldots,w_m)^{\mathsf T}.
\]
All weights are finite and strictly positive; ties are allowed. No normalization by vertex degrees or masses is used. Because \(L\mathbf1=0\), each \(K_\alpha(t)\) is symmetric and has row sums one, even when its entries are temporarily negative.

An explicit finite spectral equation determines each recovery time. Let \(d_1<\cdots<d_r\) be the distinct weights, with multiplicities \(s_a\), and put \(W=\sum_a s_a d_a\). The **radial** eigenvalues \(\theta_0=0,\theta_1,\ldots,\theta_r\) are the roots of
\[
\theta-W-\sum_{a=1}^r\frac{s_a d_a^2}{\theta-d_a}=0,
\]
with exactly one root in each \((d_a,d_{a+1})\) and one in \((d_r,\infty)\), in addition to \(\theta_0=0\). For a radial root \(\theta\), set
\[
c(\theta)=\left[1+\sum_{a=1}^r s_a\left(\frac{d_a}{d_a-\theta}\right)^2\right]^{-1},
\qquad q_a(\theta)=\frac{d_a}{d_a-\theta}.
\]
If leaves \(i,j\) belong to weight classes \(a,b\), respectively, then for \(i\ne j\)
\[
K_\alpha(t)_{ij}=
\sum_{k=0}^{r}c(\theta_k)q_a(\theta_k)q_b(\theta_k)
 e^{-t\theta_k^\alpha}
-\mathbf1_{a=b}\frac{e^{-td_a^\alpha}}{s_a}.
\]
The unique positive zero of this explicitly specified exponential polynomial is \(T_{ij}\). With a general spectral multiplier \(\phi\), replace each exponent \(\lambda^\alpha\) by \(\phi(\lambda)\). The additional eigenvalues \(d_a\), each of multiplicity \(s_a-1\), are accounted for in the last term.

## Proof

**1. Radial spectrum and projector signs.** Split the leaf coordinates into classes of equal conductance. For each class \(a\), its coordinate-sum-zero subspace is an eigenspace of eigenvalue \(d_a\), and its orthogonal radial complement is the \((r+1)\)-dimensional arrowhead space containing the hub and the class-constant vectors. The eigenvalue equation for a radial vector \(v\) gives
\[
v_i=q_a(\theta)v_0,\qquad
\theta-W-\sum_a\frac{s_a d_a^2}{\theta-d_a}=0.
\]
The derivative of the secular function is \(1+\sum_a s_ad_a^2/(\theta-d_a)^2>0\) away from poles; its one-sided limits at successive poles imply the stated interlacing. Normalizing the radial eigenvector gives \(v_0^2=c(\theta)\) and yields the spectral coefficients displayed above.

For two leaves in **different** weight classes \(a<b\), the radial spectral coefficient has the sign of \((d_a-\theta)(d_b-\theta)\): it is positive below \(d_a\), negative between \(d_a\) and \(d_b\), and positive above \(d_b\). At tied-weight eigenvalues the cross-class coefficient is zero. For two different leaves in the **same** class \(a\), every radial coefficient is positive and the single additional coefficient at eigenvalue \(d_a\) equals \(-1/s_a\). Hence, after collecting equal eigenvalues, every leaf-pair coefficient sequence, in increasing eigenvalue order, has precisely the sign-block pattern
\[
+\,\cdots\,+,\quad-\,\cdots\,-,\quad+\,\cdots\,+.
\]
There are nonempty positive blocks on both sides of the negative block, including the constant-mode coefficient \(1/(m+1)\).

For a hub–leaf pair, all nonzero coefficients come from radial eigenvectors and are \(c(\theta)q_a(\theta)\): their signs are a nonempty positive block followed by a nonempty negative block. Because the coefficients sum to zero and \(e^{-t\phi(\theta)}\) strictly decreases with \(\theta\) for \(t>0\), the hub–leaf entry of \(e^{-t\phi(L)}\) is strictly positive. Every diagonal is a sum of nonnegative spectral terms and is strictly positive.

**2. Strict negative initial slope for convex spectral multipliers.** For leaves \(i\ne j\), let \(\sigma=\sum_k a_k\delta_{\lambda_k}\) be their signed spectral measure, with distinct eigenvalues combined. The spectral identities \(I_{ij}=0\) and \(L_{ij}=0\) imply
\[
\int 1\,d\sigma=0,\qquad\int\lambda\,d\sigma=0.
\]
By Step 1, positive measure coefficients occur strictly outside the interval containing the negative ones. For a strictly convex \(\phi\), choose the secant affine line through the first and last negative support positions; if there is only one negative position, choose a supporting tangent line there. Then \(\phi\) minus that line is nonpositive at all negative support positions and strictly positive at the positive support positions, so
\[
\phi(L)_{ij}=\int\phi(\lambda)\,d\sigma(\lambda)>0.
\]
For a nondifferentiable convex function with a single negative spectral position, a supporting affine line suffices; strict convexity makes the inequality strict at all other positions. Consequently
\[
\left.\frac{d}{dt}e^{-t\phi(L)}_{ij}\right|_{t=0}=-\phi(L)_{ij}<0.
\]
This applies to \(\phi(\lambda)=\lambda^\alpha\) for every \(\alpha>1\).

**3. Exactly one recovery, not merely eventual positivity.** The generalized Descartes rule for exponential polynomials says that, for strictly increasing real exponents \(\rho_k\), the number of real zeros counted with multiplicity of \(\sum_k a_ke^{-t\rho_k}\) is at most the number of sign changes in the coefficient sequence. One proof sets \(x=e^{-t}>0\) and applies the generalized polynomial Descartes rule to \(\sum_k a_kx^{\rho_k}\), established by repeated differentiation and Rolle's theorem. In Step 1 the leaf-pair sequence has two sign changes, so its exponential polynomial has at most two real zeros counting multiplicity. One is the simple zero at \(t=0\) from Step 2. Since the constant eigenmode contributes \(1/(m+1)\) while all other terms decay as \(t\to\infty\), the leaf-pair entry tends to \(1/(m+1)>0\). It starts negative and ends positive, so it has a second real zero in \((0,\infty)\), uniquely; this zero must be simple. The same proof applies to all strictly increasing strictly convex \(\phi\) with \(\phi(0)=0\).

**4. The positive fractional-order regime.** For \(\alpha=1\), \(-L\) is an irreducible Metzler generator and \(e^{-tL}\) is strictly positive for \(t>0\). For \(0<\alpha<1\), the finite-dimensional Bernstein representation
\[
L^\alpha=c_\alpha\int_0^\infty(I-e^{-sL})s^{-1-\alpha}\,ds,
\qquad c_\alpha>0,
\]
implies that all off-diagonal entries of \(L^\alpha\) are strictly negative, because \(e^{-sL}\) is strictly positive for all \(s>0\). Thus \(-L^\alpha\) is a Metzler generator with strictly positive off-diagonals; its exponential is strictly positive for \(t>0\).

**5. The maximum-norm equivalence.** Every \(K_\alpha(t)\) has row sums one. Therefore
\[
\|K_\alpha(t)\|_{\ell^\infty\to\ell^\infty}
=1+2\max_i\sum_{j:K_\alpha(t)_{ij}<0}|K_\alpha(t)_{ij}|.
\]
The sign classification proves that the right-hand side equals one precisely at the times stated in the finding. No claim about other graph classes follows.

## Verification

The spectral recipe above is directly evaluable after finding the radial secular roots. For an easily checked special case of \(m\) equal positive conductances \(w\), the off-diagonal leaf-to-leaf expression becomes
\[
\frac1{m+1}-\frac1m e^{-tw^\alpha}
+\frac1{m(m+1)}e^{-t((m+1)w)^\alpha},
\]
which agrees with the unweighted complete-bipartite special case after time scaling. This special case is not claimed as a new result.

The accompanying `verify_star.py` uses NumPy and SciPy to check the combinatorial \(L^2\) leaf–leaf identity, spectral reconstruction, positivity and root signs on 216 explicit or seeded parameter configurations and orders, with 1,608 pair-level trials. Run `python verify_star.py` after installing NumPy and SciPy. These finite checks supplement but do not replace the analytic proof for arbitrary weights, leaf counts, orders and times.

## Relationship to prior work

Gregorio and Mugnolo (2017, first arXiv release) examine positivity failure and eventual Markovian behavior of discrete graph bi-Laplacians; their Section 2 gives a three-vertex unweighted path kernel and the general noncomplete-graph obstruction, but not an all-weight star leaf-pair single-zero theorem. Benzi and Simunec (2020) develop fractional graph-diffusion matrix functions for the subunit-order regime, where preservation of positivity by fractional \(M\)-matrix powers is established. A published complete-multipartite fractional-heat classification includes the **equal-conductance star** as a special case; the classification here is for arbitrary independent positive weights and a convex spectral-function class, with a different sign-regularity argument.

An earlier result on positively weighted star backward-Euler biharmonic *resolvents* is not an implication comparison for this statement: a Laplace-averaged inverse can have a single threshold without every time-domain matrix entry having exactly one sign crossing. This result concerns the full continuous-time exponential and all weighted-star leaf pairs. The algebraic spectral proof may have an earlier equivalent formulation under rank-one arrowhead-matrix sign variation; no priority claim is made beyond the comparisons documented in REVIEW.md.

## Limitations

The theorem does not identify which leaf pair realizes the final threshold \(T_*\) for every collection of unequal weights, and it does not give a closed elementary formula for those roots beyond the finite spectral equations. No general-tree, directed-graph, normalized-Laplacian, or nonconvex spectral-filter classification is claimed. Finite numerical checks are not an exhaustive proof. Historical novelty requires independent literature review.

## References

1. F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370, first publicly submitted 2017-12-20, especially Section 2. https://arxiv.org/abs/1712.07370
2. M. Benzi and I. Simunec, *Rational Krylov methods for fractional diffusion problems on graphs*, arXiv:2012.08389, first submitted 2020-12-15, especially Sections 2–3. https://arxiv.org/abs/2012.08389
3. *A sharp positivity transition for fractional graph heat on complete multipartite networks*, public mathematical record, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1
