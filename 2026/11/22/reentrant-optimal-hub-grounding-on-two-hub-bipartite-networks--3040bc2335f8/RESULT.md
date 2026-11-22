# Reentrant optimal hub grounding on two-hub bipartite networks

## Finding

For every integer \(q\ge3\) and budget \(B>0\), consider the unweighted complete bipartite graph \(K_{2,q}\), with two vertices in its smaller part (the *hubs*) and \(q\) vertices in the other part (the *peripherals*). Independently choose nonnegative vertex grounding gains \(g_v\) with \(\sum_v g_v=B\), minimizing
\[
J(g)=\operatorname{tr}\bigl[(L(K_{2,q})+\operatorname{diag}(g))^{-1}\bigr].
\]
The minimizer is unique. Both hubs receive one common gain \(x\ge0\), all \(q\) peripherals receive one common gain \(y>0\), and \(2x+qy=B\).

**Exact support law.** Write \(t=B/q\). Then the optimal hub gain is zero **if and only if**
\[
\boxed{q(q-1)t\ge(t+2)^3.}
\]
For \(3\le q\le5\), the optimal hub gain is positive at every budget. For every integer \(q\ge6\), the equation \((t+2)^3=q(q-1)t\) has exactly two positive solutions \(0<t_-(q)<1<t_+(q)\), and the hub gain is zero precisely for
\[
\boxed{q t_-(q)\le B\le q t_+(q).}
\]
It is strictly positive on both complementary budget intervals. The peripheral gain is always strictly positive. Thus the two hub actuators deactivate and later reactivate as budget grows, although the optimum is unique for every budget. The smallest network exhibiting this behavior is \(K_{2,6}\), with eight vertices.

The two sharp budget thresholds satisfy
\[
\boxed{q t_-(q)\sim 8/q,\qquad q t_+(q)\sim q^2\quad(q\to\infty).}
\]
The minimum value and both optimal gains can be computed without a multidimensional matrix optimization: define
\[
F_q(x,y)=\frac1{q+x}+\frac{q-1}{2+y}+\frac{q+2+x+y}{2x+qy+xy},
\qquad y=\frac{B-2x}{q}.
\]
If the boxed support inequality holds, \(x=0\) and \(y=B/q\). Otherwise \(x\) is the unique solution in \((0,B/2)\) of
\[
\frac{\partial F_q}{\partial x}(x,y)-\frac2q\frac{\partial F_q}{\partial y}(x,y)=0,
\qquad y=\frac{B-2x}{q}.
\]
The global minimum is \(F_q(x,y)\) at this unique pair.

## Assumptions and scope

All graph edges have unit conductance; \(L\) is the unnormalized combinatorial Laplacian. Gains are real, nonnegative, uncapped, and independently adjustable at every vertex. The total gain budget is fixed and positive. Every feasible gain vector has at least one positive entry, so connectedness makes the grounded matrix positive definite. The optimization measures the trace inverse (twice the stationary variance for unit white-noise forcing in continuous-time first-order consensus), not the smallest Laplacian eigenvalue, eigenratio, number of perfect leaders, or edge-conductance design.

## Proof

**1. Strict convexity and unrestricted symmetry reduction.** For any positive definite \(A\) and any nonzero real symmetric diagonal direction \(H\),
\[
\frac{d^2}{ds^2}\operatorname{tr}(A+sH)^{-1}\bigg|_{s=0}
=2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})
=2\|A^{-1/2}HA^{-1}\|_F^2>0.
\]
The feasible simplex is compact; the grounded matrix is positive definite throughout. Thus the minimizer exists and is unique. Independent permutations of the two hubs and the \(q\) peripherals preserve the objective. Uniqueness forces all hub gains to equal \(x\) and all peripheral gains to equal \(y\), without any restriction on asymmetric competitors.

**2. Exact inverse-trace reduction.** The grounded matrix has eigenvalue \(q+x\) once, corresponding to hub difference vectors, and eigenvalue \(2+y\) with multiplicity \(q-1\), corresponding to peripheral zero-sum vectors. On the two-dimensional space of vectors constant within each part, its orthonormal-basis matrix is
\[
\begin{pmatrix}q+x&-\sqrt{2q}\\-\sqrt{2q}&2+y\end{pmatrix},
\]
with determinant \(2x+qy+xy>0\) and trace \(q+2+x+y\). Summing reciprocal eigenvalues proves the displayed formula for \(F_q\).

**3. Peripherals are always active.** Parameterize the feasible interval by \(y\in[0,B/q]\), with \(x=(B-qy)/2\). At the endpoint \(y=0\), setting \(u=B/2>0\), exact differentiation gives
\[
\left.\frac{d}{dy}F_q((B-qy)/2,y)\right|_{y=0}
=-\frac{q\,[q^2u+2q^2+2qu^2+4qu+u^3+2u^2-2u]}{4u(q+u)^2}<0.
\]
The bracket is positive for every \(q\ge3\), \(u>0\), since \((q^2-2)u>0\) and the remaining terms are positive. Hence \(y=0\) cannot minimize.

**4. Exact hub KKT condition.** Parameterize instead by \(x\in[0,B/2]\), with \(y=(B-2x)/q\). At \(x=0\), put \(t=B/q>0\). A second exact differentiation gives
\[
\left.\frac{d}{dx}F_q(x,(B-2x)/q)\right|_{x=0}
=\frac{2\,[q(q-1)t-(t+2)^3]}{q^2t(t+2)^2}.
\]
Because the reduced function is strictly convex, its unique optimum occurs at \(x=0\) if and only if this one-sided derivative is nonnegative. Otherwise its derivative is negative at \(x=0\), positive at \(x=B/2\) by step 3, and has exactly one interior zero. This proves the full finite-budget optimizer classification, including equality boundaries.

**5. Two activation thresholds.** Rearranging the hub condition gives \(q(q-1)\ge (t+2)^3/t\). The function \(\phi(t)=(t+2)^3/t\) decreases strictly on \((0,1)\), increases strictly on \((1,\infty)\), and has minimum \(\phi(1)=27\): indeed \(\phi'(t)=2(t+2)^2(t-1)/t^2\). Since \(q(q-1)<27\) for \(q=3,4,5\) and \(q(q-1)>27\) for all integers \(q\ge6\), exactly the stated support regimes occur. At the two roots the hub gain is zero, not merely tending to zero.

**6. Sharp large-network scales.** For \(q\to\infty\), the smaller root lies below one and must tend to zero. Its defining equation gives \(q(q-1)t_-(q)\to8\), hence \(qt_-(q)\sim8/q\). The larger root exceeds one and tends to infinity. Dividing its equation by \(t_+(q)\) gives \(q(q-1)=t_+(q)^2[1+2/t_+(q)]^3\), hence \(t_+(q)/q\to1\) and \(qt_+(q)\sim q^2\). All limits are along the positive integers.

## Verification

Run `python3 verify_k2q_gain.py` (Python standard library only). It performs direct exact rational inversion of grounded Laplacians, exact rational comparisons of the two marginal derivative formulas, the exact integer onset criterion, root and support tests, independent scalar minimization checks, and asymptotic spot checks. The delivered code passed 4,599 assertions. The finite tests are corroboration, not a proof of the universal statements, which rest on steps 1–6.

## Relationship to prior work

Lin, Fardad and Jovanović (arXiv:1302.0450, first posted 2013-02-03) establish the inverse-trace noisy-consensus objective and its convexity for relaxed leader selection; their full article develops general numerical and combinatorial algorithms, not this all-budget two-hub classification. Zhou and colleagues (arXiv:1511.02012, first posted 2015-11-06) optimize pinning convergence speed through extremal eigenvalues and a different cost restriction, not inverse-trace variance. A later result on heterogeneous-price pinning of complete bipartite networks studies maximization of the smallest grounded-Laplacian eigenvalue; its allocation laws do not imply the inverse-trace threshold here. Previously reported star-network reentrant allocation concerns a tree with one hub, not the cyclic two-hub graph \(K_{2,q}\), and has different support thresholds. The novelty claimed is the exact non-nested hub support, the minimal \(q=6\) boundary, and its two asymptotic scales—not strict convexity or the variance formulation themselves.

## Limitations

The theorem addresses the unit-edge two-hub complete bipartite family only; it does not classify arbitrary \(K_{p,q}\) with \(p>2\), unequal actuator prices, fixed-cardinality leaders, discrete gain caps, or fastest spectral decay. No independent mathematical audit is represented. Related specialist literature may contain equivalent formulations not located during the comparison.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public 2013-02-03), https://arxiv.org/abs/1302.0450 ; IEEE Transactions on Automatic Control 59 (2014), 1789–1802, https://viterbi-web.usc.edu/~mihailo/papers/linfarjovTAC14LeaderSelection.pdf .
2. M.-Y. Zhou, Z. Zhuo, H. Liao, Z.-Q. Fu, and S.-M. Cai, *Enhancing Speed of Pinning Synchronizability: Low-Degree Nodes with High Feedback Gains*, arXiv:1511.02012 (first public 2015-11-06), https://arxiv.org/abs/1511.02012 ; Scientific Reports 5 (2015), 17459, https://www.nature.com/articles/srep17459 .
3. *Exact Heterogeneous-Price Pinning on Complete Bipartite Networks* (public research note, 2026-11-08), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-heterogeneous-price-pinning-on-complete-bipartite-networks--ebfcf6b0163e/RESULT.md .
