# Odd-Poisson rung counts and Dirichlet gaps in weakly coupled ladder spanning trees

## Finding

**Theorem (critical weak-rung point process).** Let \(L_n=P_n\square K_2\), \(n\ge1\), have both rail-edge conductances equal to \(1\) and all \(n\) rung conductances equal to \(c_n=t/n^2\), for a fixed \(t>0\). Sample a spanning tree \(T_n\) with probability proportional to the product of its edge conductances. Let \(I_n\subseteq\{1,\ldots,n\}\) be its rung columns, \(K_n=|I_n|\), and
\[
\Xi_n=\sum_{i\in I_n}\delta_{(i-1/2)/n}.
\]
Then \(\Xi_n\) converges weakly as a finite point process on \([0,1]\) to the determinantal process with continuous kernel
\[
\boxed{\quad
\mathcal K_t(x,y)=1+2\sum_{m=1}^{\infty}
\frac{2t}{2t+\pi^2m^2}\cos(m\pi x)\cos(m\pi y),
\qquad 0\le x,y\le1.
\quad}
\]
The operator has the Neumann cosine basis as eigenfunctions, with eigenvalues \(1\) and \(\frac{2t}{2t+\pi^2m^2}\), \(m\ge1\).

The total number \(K_n\) converges in **total variation** to \(K_t\) with
\[
\boxed{\quad
\Pr(K_t=k)=\frac{(\sqrt{2t})^{2k-1}}
{(2k-1)!\sinh\sqrt{2t}},\qquad k=1,2,\ldots .\quad}
\]
Equivalently, \(2K_t-1\) has a \(\operatorname{Poisson}(\sqrt{2t})\) distribution conditioned to be odd. Its probability generating function and mean are
\[
\mathbb E[u^{K_t}]=\frac{\sqrt u\sinh(\sqrt{2tu})}{\sinh\sqrt{2t}},
\qquad \mathbb E K_t=\frac{1+\sqrt{2t}\coth\sqrt{2t}}2.
\]

For every fixed \(k\ge1\), conditional on \(K_n=k\), the ordered limiting rung positions \(0<X_1<\cdots<X_k<1\) have joint density
\[
\boxed{\quad f_k(x_1,\ldots,x_k)
=(2k-1)!\prod_{j=1}^{k-1}(x_{j+1}-x_j).\quad}
\]
Equivalently, their \(k+1\) consecutive boundary-inclusive spacings converge jointly to
\[
\boxed{\quad(X_1,X_2-X_1,\ldots,X_k-X_{k-1},1-X_k)
\sim\operatorname{Dirichlet}(1,\underbrace{2,\ldots,2}_{k-1},1).\quad}
\]
For \(k=1\), the one rung is uniform on \([0,1]\). Additionally, between every consecutive pair of rungs, the tree omits exactly one rail edge. Conditioned on the limiting rung locations, those \(k-1\) omitted edges independently choose a fair rail and a position uniform on the corresponding inter-rung interval. Thus the theorem gives a complete limiting spatial description of both retained rungs and mandatory rail cuts.

**Sharp scale.** The same model with arbitrary \(c_n>0\) satisfies \(K_n\to1\) in probability if \(n^2c_n\to0\), and \(K_n\to\infty\) in probability if \(n^2c_n\to\infty\). Hence \(n^{-2}\) is the unique order yielding a nontrivial finite, nonconstant rung-count limit.

## Assumptions and scope

The ladder has two distinct vertices in each column, with a rung joining them; each rail joins consecutive columns. A spanning tree contains all \(2n\) vertices and exactly \(2n-1\) edges. The graph is connected for every \(c_n>0\), even when \(c_n\to0\). The spanning-tree probability is \(c_n^{K_n}/Z_n(c_n)\), since rail conductances equal one. The boundary-inclusive spacing vector has dimension \(k+1\), whose Dirichlet parameter sum is \(2k\). The determinantal kernel acts on Lebesgue measure on \([0,1]\); the point-process convergence is for counting measures on this compact interval. All limits fix \(t>0\) unless explicitly stated under Sharp scale.

## Proof

**1. Exact finite spanning-tree structure.** Let the selected rung columns be \(1\le i_1<\cdots<i_k\le n\). At least one rung must be present to connect the rails. Every interval from \(i_j\) to \(i_{j+1}\) forms a rail-and-two-rung cycle if all its horizontal edges remain. Thus, for every \(j<k\), at least one horizontal edge must be deleted within that interval. The tree has precisely \(k-1\) missing horizontal edges, as it has \(2n-1\) present edges among the \(2(n-1)+k\) rail/rung candidates under the specified rung set. Therefore exactly one rail edge is deleted between each consecutive pair of selected rungs and none outside. Conversely, making exactly those deletions produces a connected acyclic graph. There are \(2(i_{j+1}-i_j)\) choices for the missing edge in gap \(j\). Consequently
\[
\boxed{\quad \#\{T_n:I_n=\{i_1,\ldots,i_k\}\}
=2^{k-1}\prod_{j=1}^{k-1}(i_{j+1}-i_j).\quad}
\]
For fixed rung columns, the choices of missing edges in different gaps are independent and uniform, even under the conductance-weighted tree law.

**2. Exact finite rung-count coefficients.** Denote by \(a_{n,k}\) the number of unweighted trees having exactly \(k\) rungs. The previous formula and a weak-composition generating function give
\[
\sum_{n\ge1}\sum_{k\ge1}a_{n,k}u^kz^{n-1}
=\frac{u}{(1-z)^2}\sum_{j\ge0}\left(\frac{2uz}{(1-z)^2}\right)^j
=\frac{u}{1-2(1+u)z+z^2},
\]
so, for \(1\le k\le n\),
\[
\boxed{\quad a_{n,k}=2^{k-1}\binom{n+k-1}{2k-1},\qquad
Z_n(c)=\sum_{k=1}^na_{n,k}c^k.\quad}
\]
This coefficient identity is a finite counting input, not itself asserted to be the principal new contribution.

**3. Critical rung-count limit and total variation.** For every fixed \(k\ge1\),
\[
n a_{n,k}(t/n^2)^k\longrightarrow
\frac{2^{k-1}t^k}{(2k-1)!}.
\]
For \(k\le n\), \(n+k-1\le2n\) and hence
\[
n a_{n,k}(t/n^2)^k\le
\frac{2^{3k-2}t^k}{(2k-1)!}.
\]
The upper bound is summable over \(k\) (declare terms zero for \(k>n\)). Dominated convergence gives
\[
 nZ_n(t/n^2)\longrightarrow
\sum_{k\ge1}\frac{2^{k-1}t^k}{(2k-1)!}
=\sqrt{\frac t2}\sinh\sqrt{2t}.
\]
After normalization, the limiting count mass is the boxed formula. Since these masses sum to one, discrete Scheffé convergence gives convergence of \(K_n\) in total variation. Summing the odd Poisson series proves the stated interpretation, generating function and mean.

**4. Conditional spatial and rail-cut limits.** At fixed \(k\), the conditional probability of ordered rung columns is proportional to \(\prod_{j<k}(i_{j+1}-i_j)\), by step 1. Standard Riemann sums on the ordered \(k\)-simplex show that the rescaled positions converge to a density proportional to \(\prod_{j<k}(x_{j+1}-x_j)\). The normalization is \((2k-1)!\), by the Dirichlet integral for parameters \((1,2,\ldots,2,1)\); these parameters also identify the spacing distribution. The conditional missing-edge choices are exactly independent and uniform over \(2(i_{j+1}-i_j)\) possibilities. As the gap lengths diverge on the event of distinct limiting points, each edge's rail label tends to a fair coin and its scaled position tends to a uniform point within its gap. Thus the joint conditional marked limit holds. Tightness of the total rung count from step 3 promotes convergence for every fixed \(k\) to convergence of the complete finite marked configuration.

**5. Determinantal continuum kernel.** The weighted spanning-tree transfer-current theorem gives the finite rung determinantal kernel
\[
K_n^{\rm rung}=2c_n\bigl(L(P_n)+2c_nI\bigr)^{-1}.
\]
Here \(L(P_n)\) is the combinatorial path Laplacian. Its orthonormal eigenvectors are the constant vector and discrete Neumann cosines; eigenvalues are \(4\sin^2(m\pi/(2n))\) for \(m=0,\ldots,n-1\). Hence the rung kernel eigenvalues are
\[
q_{n,m}=\frac{2c_n}{2c_n+4\sin^2(m\pi/(2n))},\quad m=0,\ldots,n-1.
\]
At \(c_n=t/n^2\), \(q_{n,0}=1\), while for each fixed \(m\ge1\),
\[
 q_{n,m}\longrightarrow\frac{2t}{2t+\pi^2m^2}.
\]
Moreover, \(\sin(m\pi/(2n))\ge m/n\), so \(q_{n,m}\le2t/(2t+4m^2)\). Embed the discrete column functions as step functions on \([0,1]\). The eigenvectors converge in \(L^2\) to the continuous normalized Neumann cosine functions; the uniform summable spectral bound gives trace-norm convergence of the embedded kernels to the displayed \(\mathcal K_t\). Continuity of determinantal correlation measures under trace-norm convergence yields the determinantal point-process limit, consistent with step 4. Equivalently, independently selected Bernoulli variables with probabilities \(q_{n,m}\) represent the finite determinantal point count; their summable parameter convergence directly proves total-variation convergence of the count. The Euler sine product \(\sinh x/x=\prod_{m\ge1}(1+x^2/(\pi^2m^2))\) gives the same odd-Poisson generating function from the limiting eigenvalues.

**6. Sharpness of the scale.** For arbitrary \(c_n>0\), the same finite eigenvalue formula holds. If \(n^2c_n\to0\), the bound \(\sum_{m\ge1}q_{n,m}\le (n^2c_n)\sum_{m\ge1}(2m^2)^{-1}\to0\) forces \(K_n\to1\). If \(n^2c_n\to\infty\), every fixed number of the eigenvalues \(q_{n,1},q_{n,2},\ldots\) tends to one. Consequently \(K_n\to\infty\) in probability. This completes the proof.

## Verification

`verify_critical_ladder.py` is a Python 3 standard-library-only executable. It checks the exact rung-configuration formula by independently enumerating all spanning trees through seven rungs, compares every finite rung-inclusion probability with exact rational transfer-current determinants through five rungs at four conductances, and tests the spectral count identity and bounded numerical convergence to odd-conditioned Poisson and Dirichlet marginals. Execute `python3 verify_critical_ladder.py` in the same directory. In the reference execution it returned `VERIFY_OK: 627 exact assertions / bounded numerical checks`. The all-size limit results are supplied by steps 1–6, not by finite enumeration.

## Relationship to prior work

Burton and Pemantle's transfer-current theorem is the general source of the finite determinantal edge law. Häggström's 1994 doctoral work treated uniform spanning trees on infinite ladder-like graphs, and Lyons and Peres' 2016 book discusses finite ladder spanning trees, providing a directly relevant archival foundation for the model. Lyons and Steif study stationary determinantal processes; this older theory predates the present weak-coupling scaling. Klenke (2017) develops random spanning trees of infinite weighted ladders, renewal/gap descriptions, and finite-volume counting. A published finite-volume weighted-ladder result gives the exact boundary-corrected rung kernel and the fixed-weight bulk/endpoint limits. These provide foundational finite formulas, but the theorem above concerns the **critical \(n^{-2}\) scaling**, its full continuum spatial process, odd-conditioned Poisson count, boundary-sensitive Dirichlet spacings, and independently marked rail cuts.

A different published result for weakly coupled *wheel* spanning trees produces an **even-conditioned** Poisson root count and cyclic Dirichlet component lengths; it does not imply the present open-ladder odd-count and two boundary-parameter-one spacings, because the underlying graph and its cut/spoke constraints differ. The finite coefficient and transfer-current formulas are credited as ingredients, not newly discovered general identities. The genuine new statement being assessed is the combined critical continuum law and sharp crossover.

## Limitations

The model has two open rails, uniform rail conductances and homogeneous rung conductance. The explicit limiting law uses a fixed finite critical parameter \(t>0\). The scale dichotomy addresses only whether the total rung count remains one or diverges, not fluctuation laws for supercritical counts. The result does not establish analogous marked limits for prisms, wider strips, unequal rails, or arbitrary site-dependent rung strengths. Historical priority remains subject to inaccessible and unindexed equivalent continuum-limit literature; a general result from which the exact specialized limit follows would limit the originality claim. Independent mathematical validation has not been performed.

## References

- Häggström, O., *Aspects of Spatial Random Processes*, doctoral thesis, University of Gothenburg/Chalmers (1994), fourth paper on uniform spanning trees of a class of infinite graphs. https://research.chalmers.se/en/publication/1290
- Lyons, R. and Peres, Y., *Probability on Trees and Networks*, Cambridge University Press, hardback 2016; the public author page identifies a dated November 2016 hardback version (its revision date is not asserted to be its first public appearance). https://rdlyons.pages.iu.edu/prbtree/
- Burton, R. and Pemantle, R., *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings Via Transfer-Impedances*, Annals of Probability **21** (1993), 1329–1371. https://doi.org/10.1214/aop/1176989121
- Lyons, R. and Steif, J., *Stationary Determinantal Processes: Phase Multiplicity, Bernoullicity, Entropy, and Domination*, arXiv:math/0204324, first posted 26 April 2002. https://arxiv.org/abs/math/0204324
- Klenke, A., *The Random Spanning Tree on Ladder-like Graphs*, arXiv:1704.00182, first posted 1 April 2017. https://arxiv.org/abs/1704.00182
- Gantert, N. and Klenke, A., *Biased Random Walk on Spanning Trees of the Ladder Graph*, arXiv:2210.07859 (2022), Journal of Statistical Physics **190** (2023), 83. https://arxiv.org/abs/2210.07859
- *Exact finite-volume rung kernel and boundary–bulk split for weighted ladder spanning trees*, published mathematical record, 4 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-finite-volume-rung-kernel-and-boundary-bulk-split-for-weig--647fc3f7ee8c
- *Exact spoke–cut compositions in weighted wheel spanning trees and their critical spatial limit*, published mathematical record, 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-spoke-cut-compositions-in-weighted-wheel-spanning-trees-an--c4b024089d31
