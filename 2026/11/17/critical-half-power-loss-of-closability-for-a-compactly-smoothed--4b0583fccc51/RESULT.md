# Critical half-power loss of closability for a compactly smoothed graph

## Finding

On complex \(H=\ell^2(\mathbb N)\), let \(D\) be the maximal diagonal operator \((Dx)_j=jx_j\), let \(e_1\) be the first coordinate vector, and define, on \(\mathcal D(D)\),
\[
Tx=Dx+\Bigl(\sum_{j\geq1}x_j\Bigr)e_1,\qquad (Rx)_j=j^{-1}x_j.
\]
Then \(T\) is a densely defined closed bijection onto \(H\) with compact bounded inverse, and \(R\) is a positive injective compact contraction. Yet the compositions \(S_\alpha=R^\alpha T\), all initially defined on \(\mathcal D(D)\), have the following *complete* graph-closure phase diagram. Write \(D_\alpha=\operatorname{diag}(j^{1-\alpha})\) with maximal domain.

For \(0\leq\alpha<1/2\), the graph closure is the graph of the closed bijection
\[
\overline{S_\alpha}=\bigl(I+e_1\otimes v_\alpha\bigr)D_\alpha,\qquad
v_\alpha=(j^{\alpha-1})_{j\geq1}\in H,
\]
where \((e_1\otimes v)z=\langle z,v\rangle e_1\) (inner product linear in the first argument). For every \(\alpha\geq1/2\), instead,
\[
\overline{\operatorname{graph} S_\alpha}
=\{(x,D_\alpha x+c e_1):x\in\mathcal D(D_\alpha),\ c\in\mathbb C\}.
\]
In particular \(S_\alpha\) is closable **exactly** below the half-power, and at and above the threshold its closed relation has one-dimensional multivalued part \(\mathbb C e_1\), with no larger defect.

The associated nonnegative form \(q_\alpha[x]=\|S_\alpha x\|^2\) on \(\mathcal D(D)\) is closable exactly in the same subcritical range. Its canonical largest closable part is \(q_\alpha\) itself below the threshold, whereas for \(\alpha\geq1/2\) it is
\[
q_{\alpha,\mathrm{reg}}[x]=\sum_{j\geq2}j^{2(1-\alpha)}|x_j|^2,
\]
with singular remainder \(\bigl|x_1+\sum_jx_j\bigr|^2\). Thus compact post-smoothing produces a sharp change in both the operator closure and the canonical form decomposition.

There is also an exact finite-section cost for generating unit trace from a small \(D_\alpha\)-graph vector:
\[
\begin{split}
c_{\alpha,N}^2&=\inf_{\substack{x\in\operatorname{span}\{e_1,\ldots,e_N\}\\\sum_{j=1}^Nx_j=1}}(\|x\|^2+\|D_\alpha x\|^2)\\
&=\left(\sum_{j=1}^{N}\frac1{1+j^{2(1-\alpha)}}\right)^{-1}.
\end{split}
\]
Consequently, \(c_{\alpha,N}\to c_{\alpha,\infty}>0\) if \(0\leq\alpha<1/2\), while
\[
c_{\alpha,N}\sim
\begin{cases}
(\log N)^{-1/2},&\alpha=1/2,\\
\sqrt{2\alpha-1}\,N^{1/2-\alpha},&1/2<\alpha<1,\\
\sqrt{2/N},&\alpha=1,\\
N^{-1/2},&\alpha>1.
\end{cases}
\]
The logarithmic endpoint is therefore visible quantitatively as well as in closability.

## Assumptions and scope

The index set is \(\mathbb N=\{1,2,\ldots\}\); the scalar field is \(\mathbb C\); \(\alpha\) is any real number in \([0,\infty)\), and the finite-section parameter \(N\) is a positive integer. A graph closure is taken in the Hilbert product \(H\oplus H\) and may be a multivalued linear relation. The maximal diagonal domain means \(\mathcal D(D_\alpha)=\{x\in H:(j^{1-\alpha}x_j)_j\in H\}\). The series \(\sum_jx_j\) on \(\mathcal D(D)\) is absolutely convergent by Cauchy–Schwarz applied to \((jx_j)_j\) and \((j^{-1})_j\). No statement is made about arbitrary pairs of noncommuting operators or arbitrary damping sequences.

## Proof

**1. Original closed bijection.** Put \(u=(j^{-1})_j\in H\) and \(E=e_1\otimes u\). Since \(\langle e_1,u\rangle=1\), \(E^2=E\), so \(I+E\) is boundedly invertible with inverse \(I-E/2\). The identity \(T=(I+E)D\) on \(\mathcal D(D)\) proves closedness and bijectivity. The inverse \(D^{-1}(I-E/2)\) is compact, as \(D^{-1}=\operatorname{diag}(j^{-1})\) is compact. The same diagonal calculation proves the assertions about \(R\).

**2. Subcritical closure.** On \(\mathcal D(D)\), \(S_\alpha x=D_\alpha x+e_1\sum_jx_j\). If \(\alpha<1/2\), \(v_\alpha=(j^{\alpha-1})_j\) lies in \(H\), and \(\sum_jx_j=\langle D_\alpha x,v_\alpha\rangle\). Let \(E_\alpha=e_1\otimes v_\alpha\). Again \(E_\alpha^2=E_\alpha\), hence \(I+E_\alpha\) and its inverse \(I-E_\alpha/2\) are bounded. The product \((I+E_\alpha)D_\alpha\) is closed. Finitely supported vectors are a core for every maximal diagonal operator, and \(\mathcal D(D)\) contains these and is contained in \(\mathcal D(D_\alpha)\). Thus the graph closure of the restriction is precisely the stated closed operator.

**3. Supercritical relation.** For \(\alpha\geq1/2\), the relation \(\mathcal G_\alpha=\operatorname{graph}(D_\alpha)+\bigl(\{0\}\times\mathbb C e_1\bigr)\) is closed, because it is the sum of a closed subspace and a finite-dimensional subspace, and it contains the graph of \(S_\alpha\). Conversely, for a finite index set \(F\), minimizing \(\|h\|^2+\|D_\alpha h\|^2\) subject to \(\operatorname{supp}h\subseteq F\) and \(\sum_jh_j=1\) gives the reciprocal of \(\sum_{j\in F}(1+j^{2(1-\alpha)})^{-1}\). Every tail of this latter series diverges when \(\alpha\geq1/2\). Accordingly, for any finite starting index and any prescribed scalar \(b\), a finitely supported tail vector \(h\) can have \(\sum_jh_j=b\) and arbitrarily small \(D_\alpha\)-graph norm. Given \(x\in\mathcal D(D_\alpha)\) and \(c\in\mathbb C\), truncate \(x\) at index \(m\), and add such a tail vector with sum \(c-\sum_{j=1}^m x_j\) and graph norm below \(1/m\). This sequence lies in \(\mathcal D(D)\), tends to \(x\) in the graph norm of \(D_\alpha\), and its \(S_\alpha\)-images tend to \(D_\alpha x+c e_1\). Therefore \(\overline{\operatorname{graph} S_\alpha}=\mathcal G_\alpha\). The multivalued part is precisely \(\mathbb C e_1\). Independently, the adjoint test \((S_\alpha^*z)_j=j^{1-\alpha}z_j+z_1\) shows for \(\alpha\geq1/2\) that \(\mathcal D(S_\alpha^*)=\mathcal D(D_\alpha)\cap e_1^\perp\): if \(z_1\ne0\), its would-be adjoint coordinates force \(|z_j|\) to behave like \(|z_1|j^{\alpha-1}\), which is not square-summable. This separately confirms the one-dimensional defect.

**4. Form decomposition.** The graph projection characterisation of the largest closable part of a nonnegative form represented by \(S_\alpha\) projects the image onto the orthogonal complement of the multivalued part of its closure. Below the threshold that part is zero, so the entire form is closable. At and above it the complement is \(e_1^\perp\), and the projection of \(S_\alpha x\) equals \(\sum_{j\geq2}j^{1-\alpha}x_j e_j\), yielding the displayed maximal regular part. Its orthogonal residual is \((x_1+\sum_jx_j)e_1\). The latter scalar functional is nonclosable and its one-dimensional-range form is singular, as directly witnessed by the same tail vectors of Step 3.

**5. Exact finite-section cost.** The squared graph norm on the first \(N\) coordinates is \(\sum_{j=1}^N(1+j^{2(1-\alpha)})|x_j|^2\). Weighted Cauchy–Schwarz gives the lower bound \((\sum_{j=1}^N(1+j^{2(1-\alpha)})^{-1})^{-1}\); equality is attained uniquely at \(x_j=(1+j^{2(1-\alpha)})^{-1}/\sum_{k=1}^N(1+k^{2(1-\alpha)})^{-1}\). Standard harmonic-sum asymptotics give all five displayed regimes, including the exact \(\alpha=1\) identity. This also provides an independent route to the sharp transition: the trace functional has positive graph-norm capacity precisely below \(1/2\).

## Verification

The five proof steps are independent of finite numerical experiments. The included \`proof_check.py\` executes exact-rational capacity and stationarity checks at three integral exponents, an exact-rational inverse formula on three finite sections, and supplementary positive-real evaluations around the critical exponent. These finite tests cannot establish the unbounded-domain statements, which follow from the core, graph-closure, adjoint and divergence arguments above. To reproduce: run \`python proof_check.py\` in an ordinary Python 3 environment. No third-party packages are required.

## Relationship to prior work

Hassi and de Snoo (2026), Sections 3–5, prove abstract implications for products of linear relations and construct a nonnegative \(T\) and positive contraction \(R\) with \(R^{1/2}T\) closable but \(RT\) singular. Their example is an existential range-theoretic construction, not the explicit compact-inverse, one-channel graph-closure classification and finite-section capacity law here. The earlier Hassi–de Snoo paper (2025), particularly Section 3, gives general regular/singular decompositions of semibounded forms via representing maps; those abstract projection formulas are used rather than claimed as new. Simon (1978) established the overarching canonical decomposition of nonnegative forms. The claim here is the exact model-specific threshold, graph relation and logarithmic endpoint profile, not a new general decomposition theorem. Classical work on bounded rank-one perturbations of diagonal normal operators concerns invariant subspaces rather than loss of closability under an unbounded graph coupling.

## Limitations

The result concerns one explicit rank-one coupling on a separable Hilbert space and polynomial compact damping. It is not a classification of arbitrary closed operators or compact multipliers. The source papers contain more general abstract existence results, and priority for an independently formulated but unindexed equivalent explicit example remains possible. The finite-section calculations do not certify any statement about infinite graphs; the latter is proved analytically. Independent mathematical audit has not been performed.

## References

1. S. Hassi and H. de Snoo, *Non-standard behaviour of semibounded forms and their representations*, arXiv:2611.08225v1 (first public version 5 November 2026), https://arxiv.org/html/2611.08225v1.
2. S. Hassi and H. S. V. de Snoo, *Representing maps for semibounded forms and their Lebesgue-type decompositions*, Journal of the London Mathematical Society (2025), https://doi.org/10.1112/jlms.70368.
3. B. Simon, *A canonical decomposition for quadratic forms with applications to monotone convergence theorems*, Journal of Functional Analysis **28** (1978), 377–385, https://doi.org/10.1016/0022-1236(78)90094-0.
4. E. A. Gallardo-Gutiérrez and F. J. González-Doña, *Finite rank perturbations of normal operators: Spectral subspaces and Borel series*, Journal de Mathématiques Pures et Appliquées (2022), https://doi.org/10.1016/j.matpur.2022.04.002.
