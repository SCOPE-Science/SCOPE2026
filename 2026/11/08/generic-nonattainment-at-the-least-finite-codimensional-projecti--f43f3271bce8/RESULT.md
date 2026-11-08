# Generic nonattainment at the least finite-codimensional projection constant

## Finding

Let \(K\) be a nonempty compact metrizable space without isolated points, let \(m\ge2\), and let \(\mu_1,\ldots,\mu_m\) be pairwise mutually singular Borel probability measures on \(K\). In the real or complex Banach space \(C(K)\), set
\[
Y(\boldsymbol\mu)=\left\{f\in C(K):\int_K f\,d\mu_j=0\ \text{for all }1\le j\le m\right\}.
\]
Then \(Y(\boldsymbol\mu)\) has codimension \(m\), and its relative projection constant is exactly
\[
\lambda(Y(\boldsymbol\mu),C(K))=2.
\]
**Attainment classification:** A projection onto \(Y(\boldsymbol\mu)\) has norm \(2\) if and only if the closed topological supports \(\operatorname{supp}\mu_1,\ldots,\operatorname{supp}\mu_m\) are pairwise disjoint. In particular, measure-theoretic mutual singularity alone does not guarantee attainment.

Endow \(\mathcal P(K)^m\), the space of probability-measure \(m\)-tuples, with its product weak topology. Pairwise singular tuples form a dense \(G_\delta\) subset. Within that subset, tuples with an attained minimum form a **dense meagre** subset, whereas a dense \(G_\delta\) set of tuples consists of pairwise singular, nonatomic, full-topological-support measures and gives an **unattained** minimum. Thus, among tuples at the least possible projection constant, both alternatives are dense, but nonattainment is Baire generic.

There is also an explicit sharp **order-of-growth** law for near-minimal projections. For \(K=[0,1]\), \(\mu_1\) Lebesgue probability measure, and \(\mu_2=\delta_0\), write every projection onto \(Y(\boldsymbol\mu)\) as
\[
(Pf)(x)=f(x)-\left(\int_0^1f(s)\,ds\right)g_1(x)-f(0)g_2(x).
\]
For \(0<\varepsilon<1\), if \(\|P\|\le2+\varepsilon\) and \(g_1\) is Lipschitz with constant \(L\), then
\[
L\ge\frac{(1+\varepsilon)^2}{2\varepsilon}.
\]
Conversely, for each integer \(t\ge2\), there are explicit piecewise-linear coefficient functions \(g_1,g_2\) with
\[
\|P_t\|=2+\frac{2}{2t-1},\qquad
\operatorname{Lip}(g_1)=\operatorname{Lip}(g_2)=t+\frac{t}{2t-1}.
\]
Hence the necessary \(1/\varepsilon\) Lipschitz blow-up is optimal in order. The leading constant in this rate is **not** asserted optimal.

## Assumptions and scope

All measures are positive regular Borel probabilities. Their pairwise mutual singularity is measure-theoretic; topological supports are the smallest closed full-measure sets and may overlap even for singular measures. A projection means a bounded linear idempotent with image the designated closed subspace. Define \(\lambda(Y,X)\) as the infimum of operator norms among projections \(X\to Y\). The Baire-category assertion concerns the product weak topology of \(\mathcal P(K)^m\), not a topology on the Grassmannian of finite-codimensional subspaces. The Lipschitz statement concerns the distinguished biorthogonal coefficient function \(g_1\), with real or complex values; in the explicit upper construction the coefficient functions are real.

## Proof

**1. Projection coordinates and their exact norms.** Pairwise singular probabilities are linearly independent: there exist disjoint Borel sets \(A_j\) with \(\mu_j(A_j)=1\). Hence the common kernel has codimension \(m\). Any projection \(P:C(K)\to Y\) has a unique representation
\[
Pf=f-\sum_{j=1}^{m}\left(\int_K f\,d\mu_j\right)g_j,
\qquad \int_Kg_j\,d\mu_i=\delta_{ij},
\]
where each \(g_j\in C(K)\). To see this, the difference \(I-P\) has finite rank and annihilates \(Y\); the quotient coordinates \(f\mapsto (\int f\,d\mu_j)_j\) identify its coefficients, and idempotence supplies the biorthogonality identities.

Put \(Sf=\sum_j(\int f\,d\mu_j)g_j\). Mutual singularity gives \(\|\sum_j c_j\mu_j\|=\sum_j|c_j|\). Testing \(S^*\) on point masses, and using \(\|S\|=\sup_{x\in K}\|S^*\delta_x\|\), therefore gives
\[
\|S\|=\max_{x\in K}\sum_{j=1}^{m}|g_j(x)|.
\]
Since \(K\) has no isolated points, \(C(K)\) has the Daugavet property, so the finite-rank Daugavet identity gives
\[
\boxed{\ \|P\|=1+\max_{x\in K}\sum_j|g_j(x)|\ }.
\]
This is an exact coordinate norm formula for every admissible projection, not merely for minimizers.

**2. Infimum equals two.** A bounded norm-one projection from the measure space \(M(K)=C(K)^*\) onto \(W=\operatorname{span}\{\mu_j\}\) is obtained by \(Q\nu=\sum_j\nu(A_j)\mu_j\). Indeed, \(Q\mu_i=\mu_i\) and \(\|Q\nu\|=\sum_j|\nu(A_j)|\le\|\nu\|\). The 2026 Daugavet duality of Kania and Lewicki, Theorem 3.1, therefore yields \(\lambda(Y,C(K))=1+\lambda(W,M(K))=2\). There is also a direct continuous approximation: choose disjoint compact sets \(F_j\subset A_j\) with \(\mu_j(F_j)>1-\eta\), then pairwise disjoint open neighborhoods \(U_j\supset F_j\) with \(\mu_i(U_j)<\eta\) for \(i\ne j\), and continuous \(0\le\varphi_j\le1\) supported in \(U_j\), equal to \(1\) on \(F_j\). For the matrix \(M_{ij}=\int\varphi_j\,d\mu_i\), one has \(\|I-M\|_{\infty\to\infty}\le m\eta\). If \(m\eta<1\), set \(g_j=\sum_i (M^{-1})_{ij}\varphi_i\). Then \(\int g_j\,d\mu_i=\delta_{ij}\), and disjointness of the \(\varphi_i\)-supports gives \(\max_x\sum_j|g_j(x)|\le(1-m\eta)^{-1}\). The exact norm formula supplies projections with norms tending to \(2\).

**3. Attainment is exactly topological separation.** If \(\|P\|=2\), the coordinate norm formula gives \(\sum_j|g_j(x)|\le1\) for every \(x\). But \(\int g_i\,d\mu_i=1\) with \(\mu_i\) a probability. Consequently \(g_i=1\) \(\mu_i\)-almost everywhere, hence by continuity on the whole \(\operatorname{supp}\mu_i\). On that support every other \(g_j\) must be zero. Were two supports to intersect, the values \(g_i=g_j=1\) at the intersection would contradict the pointwise bound. Conversely, if these finitely many closed supports are disjoint, normality gives continuous \(0\le g_j\le1\) with \(g_j=1\) on \(\operatorname{supp}\mu_j\) and mutually disjoint supports. They satisfy all biorthogonality conditions and \(\sum_j|g_j|\le1\), so the corresponding projection has norm \(2\).

**4. Genericity and two dense strata.** Write \(\mathcal P(K)\) for probabilities with weak topology; it is compact metrizable. For two probabilities, mutual singularity is equivalent to \(\|\mu-\nu\|=2\). The total-variation norm is lower semicontinuous for weak convergence, since it is the supremum over continuous test functions of their absolute integrals. Thus singular pairs form
\[
\bigcap_{r=1}^{\infty}\{(\mu,\nu):\|\mu-\nu\|>2-1/r\},
\]
a \(G_\delta\). It is dense: finitely supported approximating measures can be chosen with all their atoms distinct across finitely many components, because \(K\) has no isolated points. Intersecting over finitely many pairs proves the singular-tuples assertion. Full support is also dense \(G_\delta\): for a countable base \((U_s)\), require \(\mu(U_s)>0\) for each \(s\); each condition is open, and a small admixture of any fixed full-support probability makes it hold densely. Nonatomic measures form a further dense \(G_\delta\) on perfect compact metric spaces (the classical generic-measure theorem of Lenz and Stollmann); alternatively, density follows from approximating atoms by diffuse measures on small perfect subsets. The intersection of these conditions is dense \(G_\delta\) in \(\mathcal P(K)^m\). Every tuple there has intersecting full supports, so by step 3 its minimum is unattained. On the other hand, the finite measures with pairwise disjoint supports are dense and attain the minimum. Because the nonattainment set contains a dense \(G_\delta\), the attaining set is meagre, also relative to the dense \(G_\delta\) space of mutually singular tuples.

**5. Exact-order Lipschitz cost.** For \(\mu_1=dx\) and \(\mu_2=\delta_0\), biorthogonality gives \(g_1(0)=0\), \(\int_0^1g_1=1\), \(g_2(0)=1\), \(\int_0^1g_2=0\). If \(\|P\|\le2+\varepsilon\), step 1 yields \(|g_1(x)|\le1+\varepsilon\). If \(g_1\) is \(L\)-Lipschitz, then \(\operatorname{Re} g_1(x)\le\min\{Lx,1+\varepsilon\}\). For \(0<\varepsilon<1\), integrating and using \(\int\operatorname{Re}g_1=1\) first forces \(L>1+\varepsilon\), and then gives
\[
1\le(1+\varepsilon)-\frac{(1+\varepsilon)^2}{2L},
\]
which rearranges to the asserted lower bound.

For the converse let \(t\ge2\) be an integer, put \(a_t(x)=\min\{tx,1\}\), \(b_t(x)=\max\{1-tx,0\}\), and define
\[
 c_t=\left(1-\frac1{2t}\right)^{-1},\qquad
 g_1=c_ta_t,\qquad
 g_2=b_t-\frac1{2t}g_1.
\]
Direct integration gives \(\int g_1=1\), \(\int g_2=0\), \(g_1(0)=0\), \(g_2(0)=1\). On each side of \(x=1/t\), \(|g_1|+|g_2|\) is a convex piecewise-linear function and its maximum is among its endpoint values. It equals
\[
 c_t\left(1+\frac1{2t}\right)=\frac{2t+1}{2t-1}.
\]
The two Lipschitz constants both equal \(c_tt=t+t/(2t-1)\). Substitution into the exact projection norm completes the construction. In particular, \((\|P_t\|-2)\operatorname{Lip}(g_1)\to1\), whereas every family with defect \(\varepsilon\downarrow0\) has product at least asymptotically \(1/2\). The order \(\varepsilon^{-1}\) cannot be improved, but these estimates do not establish an optimal leading coefficient.

## Verification

The proof is analytical and applies to infinitely many measures and operators as quantified. Exact rational diagnostics for the explicit two-function construction are provided in `CHECK.py` (run with Python 3). That file checks the two integrals, all biorthogonality endpoints, the exact norm formula and both Lipschitz constants for 1,000 integer parameters, giving 11,000 finite assertions. Those diagnostics do not prove the Baire assertion, the general compact-space claim, or the sharp-order result for every real tolerance; those are established in the preceding proof.

## Relationship to prior work

Kania and Lewicki (arXiv:2604.10771v1, 12 April 2026) prove the Daugavet projection-duality formula \(\lambda(Y,X)=1+\lambda(Y^\perp,X^*)\) and classify hyperplane attainment. Their codimension-two constructions attain nonattainment for constants strictly above \(2\); they do not state the pairwise-singular probability-measure support criterion, the dense/meagre dichotomy, or the Lipschitz cost. Their hyperplane criterion already characterizes codimension-one endpoint nonattainment by norm attainment of the defining functional; it does not classify the present higher-codimensional positive-measure setting. The numerical lower value \(2\) and the duality identity are **prior input, not new claims**. Lenz and Stollmann (Duke Math. J. 131 (2006), Theorem 2.2) establish general \(G_\delta\) properties for mutually singular, diffuse, and full-support measures; our use of those facts is credited and not presented as a new theorem in measure theory. A previous analysis of codimension-two projection constants \(2+t/(1+t+t^2)\) for \(0<t\le1\) concerns strictly larger constants, not the minimal-constant stratum or its topology/regularity.

## Limitations

The classification assumes **positive, pairwise singular probability measures** and a perfect compact metrizable \(K\). It does not classify general signed annihilators or arbitrary finite-codimensional subspaces, nor compute the optimal leading coefficient in the Lipschitz cost. The genericity is a statement about measure-tuples, not about all subspaces of fixed codimension. The near-minimal Lipschitz estimate is specific to Lebesgue measure and evaluation at the endpoint. While explicit implication comparisons did not identify a covering result, a broader characterization of weak-star-continuous norm-one projections onto finite-dimensional measure spans could subsume the support criterion; the publication-priority status therefore remains qualified pending independent literature review.

## References

1. T. Kania and G. Lewicki, *Finite-codimensional subspaces of Daugavet spaces: projection constants and minimal projections*, arXiv:2604.10771v1 (first public 2026-04-12), Theorems 3.1 and 5.2 and Sections 4–6. https://arxiv.org/html/2604.10771v1
2. D. Lenz and P. Stollmann, *Generic sets in spaces of measures and generic singular continuous spectrum for Delone Hamiltonians*, Duke Math. J. 131 (2006), 203–217, especially Theorem 2.2. https://www.tu-chemnitz.de/mathematik/analysis/preprints/LenzS-06.pdf
3. V. M. Kadets, R. V. Shvidkoy, G. G. Sirotkin, and D. Werner, *Banach spaces with the Daugavet property*, Trans. Amer. Math. Soc. 352 (2000), 855–873 (finite-rank Daugavet identity as used in Reference 1).
