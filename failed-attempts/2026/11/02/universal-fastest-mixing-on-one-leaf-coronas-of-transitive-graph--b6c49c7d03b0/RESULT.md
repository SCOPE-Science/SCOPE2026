# Universal fastest mixing on one-leaf coronas of transitive graphs

## Finding

Let \(H\) be any finite connected simple graph on \(n\ge2\) vertices, regular of degree \(d\ge1\), and both vertex- and edge-transitive. Attach one distinct pendant vertex to every vertex of \(H\) to form its one-leaf corona \(G=H\circ K_1\). Let \(\alpha>0\) denote the smallest nonzero eigenvalue of the unweighted Laplacian \(L_H\), and define
\[
 c=\frac{\alpha}{2d},\qquad s=\sqrt{\frac{\alpha}{d}},\qquad D=2+(1-c)s.
\]
Among **all** real symmetric, nonnegative, row-stochastic matrices \(P\) supported on the edges and diagonal of \(G\), the minimum second-largest eigenvalue modulus is
\[
 \boxed{\mu_*(G)=\frac{2-2c+s}{D}},\qquad
 \boxed{1-\mu_*(G)=\frac{c(2-s)}{D}}.
\]
A global optimizer gives transition probability
\[
 \boxed{a_* = \frac{c+(1-c)s}{D}}
\]
to each core-to-own-leaf edge and
\[
 \boxed{b_* = \frac{2-c}{dD}}
\]
to every core edge. It gives **zero holding probability at every core vertex** and positive holding probability \(1-a_*\) at each leaf. This optimizer is unique among matrices constant on the two edge orbits; uniqueness among all unsymmetrized matrices is **not** claimed.

The optimum depends on the base graph only through its normalized algebraic connectivity \(\alpha/d\), not its largest Laplacian eigenvalue. Along any graph family with \(\alpha/d\to0\),
\[
 a_*\sim\tfrac12\sqrt{\alpha/d},\qquad
 1-\mu_*\sim\frac{\alpha}{2d},\qquad
 db_*\to1.
\]
For \(H=K_n\) the optimum tends to \(a_*=2/5\), \(\mu_*=4/5\) as \(n\to\infty\). For every balanced complete bipartite base \(H=K_{m,m}\), \(m\ge2\), these values hold **exactly** (with \(db_*=3/5\)) because \(\alpha/d=1\). For hypercubes \(H=Q_d\), the optimal leaf weight is asymptotic to \(1/\sqrt{2d}\) and the spectral gap to \(1/d\). For \(H=K_2\), the corona is the four-vertex path and \(\mu_*=1/\sqrt2\).

## Assumptions and scope

The graph \(H\) is finite, connected, undirected, loop-free, nonempty, and simple, with \(n\ge2\). It is both vertex-transitive and edge-transitive; the edge-transitivity is needed for the one-core-edge orbit. The corona contains \(2n\) vertices, exactly one pendant edge incident to each leaf, and all original core edges. Holding probabilities are allowed; no off-diagonal transition is allowed outside graph edges. The matrix is symmetric and stochastic, hence has uniform stationary measure. The objective is
\[
 \mu(P)=\left\|P-\frac{\mathbf1\mathbf1^{\mathsf T}}{2n}\right\|_2,
\]
where \(\|\cdot\|_2\) is the spectral operator norm. Every feasible matrix, including asymmetric edge allocations across automorphism orbits, participates in the global comparison. The trivial eigenvalue \(1\) is excluded from \(\mu\).

The positive Laplacian spectrum satisfies \(0<\alpha\le\beta\le2d\), so \(0<c\le1\) and \(0<s\le\sqrt2\). Formulae also cover the base \(K_2\).

## Proof

**1. Unrestricted-to-orbit reduction.** The finite automorphism group of \(H\) permutes core vertices and their paired leaves, transitively on the set of pendant edges and separately on all core edges. Averaging an arbitrary feasible \(P\) over this group preserves nonnegativity, symmetry, row sums and edge support. Because the spectral norm is convex and unitarily invariant, averaging cannot increase \(\mu(P)\). Thus some unrestricted global optimizer belongs to the two-parameter family with pendant probability \(a\) and core-edge probability \(b\), where
\[
 a\ge0,\quad b\ge0,\quad a+db\le1.
\]
The corresponding matrix, in core-then-leaf vertex order, is
\[
 P(a,b)=\begin{pmatrix}I-aI-bL_H&aI\\aI&(1-a)I\end{pmatrix}.
\]

**2. Exact spectral envelopes.** For each eigenvalue \(\lambda\) of \(L_H\), the two-dimensional block is
\[
 \begin{pmatrix}1-a-b\lambda&a\\a&1-a\end{pmatrix},
\]
with eigenvalues
\[
 u_\pm(\lambda)=1-a-\frac{b\lambda}{2}\pm\sqrt{a^2+\left(\frac{b\lambda}{2}\right)^2}.
\]
For \(\lambda=0\) these give \(1\) and \(1-2a\). For \(\lambda>0\), \(u_+\) is nonincreasing and \(u_-\) nonincreasing in \(\lambda\). Because \(b\beta\le2db\le2(1-a)\), their sum at \(\beta\) is nonnegative, giving \(u_+(\beta)\ge |u_-(\beta)|\) if \(u_-\) is negative (otherwise the inequality is immediate). When \(u_-(\lambda)\) is positive it is directly bounded by \(u_+(\lambda)\); when negative its magnitude is bounded by \(|u_-(\beta)|\). Therefore every nontrivial spectral modulus is bounded by \(u_+(\alpha)\) except possibly \(|1-2a|\), and
\[
 \mu(P(a,b))=\max\{u_+(\alpha),\ |1-2a|\}.
\]
This proves that the upper spectral endpoint \(\beta\) does not enter the minimax objective. The boundary cases \(a=0\) and \(a=1\) have \(\mu=1\), so an optimum with \(\mu<1\) has \(0<a<1\).

**3. The core row is saturated.** For each fixed \(0<a<1\), \(u_+(\alpha)\) is strictly decreasing in \(b\): its derivative is
\[
 -\frac\alpha2+\frac{b\alpha^2}{4\sqrt{a^2+(b\alpha/2)^2}}<0.
\]
It follows that for every admissible \((a,b)\), \(\mu(P(a,b))\ge u_+(\alpha)\ge F(a)\), where the rightmost function uses \(b=(1-a)/d\):
\[
 F(a)=(1-c)(1-a)+\sqrt{a^2+c^2(1-a)^2}.
\]
The second derivative is
\[
 F''(a)=\frac{c^2}{[a^2+c^2(1-a)^2]^{3/2}}>0.
\]
Moreover, \(F'(0)=-1\), \(F'(1)=c>0\), so \(F\) has a unique interior minimizer.

**4. Closed-form minimizer and attainment.** Set \(t=a/(1-a)\). The stationarity equation becomes
\[
 \frac{t-c^2}{\sqrt{t^2+c^2}}=1-c.
\]
Its unique positive root satisfying the unsquared sign constraint is
\[
 t_* = \frac{c+(1-c)\sqrt{2c}}{2-c}.
\]
Consequently \(a_*=t_*/(1+t_*)\) and \(b_*=(1-a_*)/d\), yielding the stated formulas. To evaluate \(F(a_*)\), note the identity
\[
 [c+(1-c)s]^2+c^2(2-c)^2=[s+c(1-c)]^2
\]
under \(s^2=2c\); all factors on the right are nonnegative. This gives \(F(a_*)=(2-2c+s)/D\).

Finally \(a_*\le1/2\), since \((1-c)s\le2(1-c)\). Therefore
\[
 |1-2a_*|=1-2a_*\le1-a_*\le u_+(\alpha)=F(a_*),
\]
so the lower bound from Step 3 is attained by \(P(a_*,b_*)\). The strict convexity of \(F\) and strict decrease in \(b\) at \(a_*\) show uniqueness of this orbit-invariant optimizer. Averaging in Step 1 establishes global optimality without making any unrestricted uniqueness claim.

**5. Asymptotic consequences.** Subtracting the two fractions yields the exact gap identity \(1-\mu_*=c(2-s)/D\). As \(c\downarrow0\), \(s=\sqrt{2c}\), \(D=2+O(\sqrt c)\), and the stated square-root and gap limits follow. For \(H=K_n\), \(\alpha=n\) and \(d=n-1\), hence \(c\to1/2\), \(s\to1\), giving \(a_*\to2/5\) and \(\mu_*\to4/5\). For \(K_2\), \(c=1\) gives \(a_*=b_*=1/2\), \(\mu_*=1/\sqrt2\).

## Verification

Run `python verify.py` with the packages specified in `requirements.txt`. The executed verifier produced `PASS 1768 symbolic/numeric grouped assertions`. It separately constructs the full transition matrix and compares its eigenvalues with the closed formulas for cycles, complete graphs, hypercubes, balanced complete bipartite graphs, the Petersen graph and Johnson graphs. It also runs one-dimensional numerical optimizations, checks feasible off-optimum orbit allocations, checks asymmetric feasible samples, and verifies exact symbolic stationarity identities. These finite computations test implementation and special cases; they do **not** prove the infinite-family theorem. Its unrestricted optimality is provided by Step 1 of the proof.

## Relationship to prior work

Boyd, Diaconis and Xiao's 2004 paper established the global convex SLEM formulation and treated path special cases. Boyd, Diaconis, Parrilo and Xiao (arXiv:0709.0955, first submitted September 6, 2007) established automorphism averaging, orbit reductions and particular graph formulas. Their inspected work covers neither this leaf-corona construction nor the normalized-algebraic-connectivity-only minimax law.

A pre-existing calculation for the sunlet \(C_m\circ K_1\) is a **special case** of the formula above, not a novelty claim here. The contribution is the uniform theorem for **every connected vertex- and edge-transitive base**, including complete graphs, hypercubes and Johnson graphs, and the proof that the largest Laplacian eigenvalue is immaterial. The 2020 clique-lifted-graph literature concerns a different operation (replacement by clique fibers); an accessible abstract does not settle the possible full-text overlap. The relationship is one of general convex tools and specialized graph formulas, not a claim that the underlying FMMC framework is new.

## Limitations

Only symmetric stochastic chains with uniform stationary distribution are optimized, and base graphs must be connected and both vertex- and edge-transitive. The theorem does not cover arbitrary irregular bases or arbitrary nonreversible chains. It does not prove uniqueness among unrestricted non-orbit-constant optimizers. Numerical verification is finite and cannot certify all graph orders. While checked literature and search records did not show broader coverage, inaccessible or unindexed specialized work may contain equivalent statements; originality is therefore qualified, not guaranteed. No independent mathematical audit has been performed.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689, DOI: https://doi.org/10.1137/S0036144503423264, first verified electronic publication October 29, 2004. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (September 6, 2007), later SIAM J. Optimization 20 (2009), 792–819, DOI: https://doi.org/10.1137/070689413. Author-hosted full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Trans. Signal and Information Processing over Networks 6 (2020), 88–104, DOI: https://doi.org/10.1109/TSIPN.2020.2964211; full text was not available for a complete comparison.
