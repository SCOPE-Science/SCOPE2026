# Reentrant hub grounding in A-optimal noisy star consensus

## Finding
For every integer \(m\ge2\) and every real budget \(B>0\), let \(L\) be the unit-conductance combinatorial Laplacian of the star \(K_{1,m}\), indexed by hub \(0\) and leaves \(1,\ldots,m\). Allocate arbitrary nonnegative individual diagonal grounding gains \(g_i\) satisfying \(\sum_{i=0}^m g_i=B\). The unique global minimizer of
\[
\mathcal J(g)=\operatorname{tr}\left[(L+\operatorname{diag}(g))^{-1}\right]
\]
has equal positive leaf gains \(q_*=(B-p_*)/m>0\), where \(p_*=g_0\) is the hub gain. Define
\[
H_m(B)=B^3+4mB^2-m(m^3-m^2-5m)B+2m^3.
\]
The hub is ungrounded **if and only if** \(H_m(B)\le0\). For \(m=2,3\), the hub is grounded at every positive budget. For every \(m\ge4\), the cubic \(H_m\) has exactly two distinct positive roots \(B_-(m)<B_+(m)\), and the unique optimizer has
\[
\boxed{p_*>0\text{ for }0<B<B_-(m)\text{ and }B>B_+(m),\qquad p_*=0\text{ for }B_-(m)\le B\le B_+(m).}
\]
Thus the smallest star with hub withdrawal followed by reactivation is the five-vertex star \(K_{1,4}\); its exact thresholds are \(B_-(4)=2\sqrt{33}-10\) and \(B_+(4)=4\). The thresholds have asymptotic scales
\[
\boxed{B_-(m)\sim 2/m,\qquad B_+(m)\sim m^2\quad(m\to\infty).}
\]
The unique optimal hub gain outside the zero region is the unique interior stationary point of the explicit strictly convex function
\[
\Phi_{m,B}(p)=\frac{m-1}{1+(B-p)/m}+\frac{m+p+1+(B-p)/m}{(m+p)(1+(B-p)/m)-m},\qquad 0\le p\le B.
\]
Inside the zero region, the exact optimal value is
\[
\mathcal J_* = \frac{m(m-1)}{m+B}+\frac{m+1}{B}+\frac1m.
\]

## Assumptions and scope
The star has \(m+1\) vertices and fixed, identical unit edge conductances. All diagonal grounding gains, including the hub gain, may independently equal zero; the *total* gain budget is strictly positive and must be fully spent. Because the graph is connected, \(L+\operatorname{diag}(g)\) is positive definite for every feasible gain vector. The objective is the unnormalized inverse trace, corresponding to twice the total stationary mean-square deviation of the linear system \(\dot x=-(L+\operatorname{diag}(g))x+w\) with spatially independent unit-intensity white disturbances. It is not the smallest-eigenvalue decay-rate objective, and it does not permit changing edge weights or feedback prices. Results concern global optimization over **all individual** gains, not merely leaf-symmetric candidates.

## Proof
**1. Existence, strict convexity, and forced leaf symmetry.** For any feasible vector, the pinned Laplacian is positive definite since \(z^{\mathsf T}(L+\operatorname{diag}(g))z=\sum_{i=1}^m(z_0-z_i)^2+\sum_i g_i z_i^2\) vanishes only at \(z=0\). The simplex is compact, so a minimizer exists. Along any nonconstant affine perturbation \(A(s)=A+sD\) with \(D\ne0\),
\[
\frac{d^2}{ds^2}\operatorname{tr}(A(s)^{-1})=2\operatorname{tr}\big(A(s)^{-1}D A(s)^{-1}D A(s)^{-1}\big)>0,
\]
by writing the trace as the trace of a nonzero positive-semidefinite square conjugated by \(A(s)^{-1/2}\). The diagonal mapping from gains to matrices is injective. Thus the minimizer is unique. Every permutation of leaves preserves the graph, budget and objective, so uniqueness forces equal leaf gains. Write \(p=g_0\), \(q=(B-p)/m\).

**2. Reduction to one variable.** On the \(m-1\)-dimensional leaf-difference space, the matrix has eigenvalue \(t=1+q\). On the span of the hub and the normalized all-leaf vector, it is the arrowhead quotient \(\begin{pmatrix}u&-\sqrt m\\-\sqrt m&t\end{pmatrix}\), with \(u=m+p\). Its determinant is \(D=ut-m>0\). Therefore its inverse trace is exactly
\[
\Phi_{m,B}(p)=\frac{m-1}{t}+\frac{u+t}{D}.
\]
It is strictly convex for \(0\le p\le B\), since the corresponding individual gain vector varies nontrivially with \(p\).

**3. Boundary derivatives decide support.** Differentiation, using \(u'=1\), \(t'=-1/m\) and \(D'=t-u/m\), gives
\[
\Phi'_{m,B}(p)=\frac{m-1}{m t^2}+\frac{(1-1/m)D-(u+t)(t-u/m)}{D^2}.
\]
Clearing strictly positive denominators at both endpoints yields the exact identities
\[
\Phi'_{m,B}(0)=-\frac{H_m(B)}{Bm^2(B+m)^2},\qquad
\Phi'_{m,B}(B)=\frac{B+2}{B}>0.
\]
A strictly convex differentiable function on \([0,B]\) with strictly positive right-end derivative has a unique minimizer strictly below \(B\). It is exactly \(p=0\) when its left-end derivative is nonnegative; otherwise there is exactly one root of its derivative in \((0,B)\). This establishes the all-budget optimizer and shows that every leaf has strictly positive gain.

**4. Exactly two phase boundaries from five vertices onward.** For \(m=2\), \(H_2(B)=B^3+8B^2+12B+16>0\). For \(m=3\), \(H_3(B)=B^3+12B^2-9B+54>0\), as the quadratic \(12B^2-9B+54\) is strictly positive. For \(m=4\),
\[
H_4(B)=(B-4)(B^2+20B-32),
\]
which has exactly the claimed positive zeros and is negative between them. For every \(m\ge5\), \(H_m(0)=2m^3>0\), \(H_m(m)=-m^3(m-4)(m+3)<0\) and \(H_m(B)\to+\infty\) as \(B\to+\infty\). Its ordered coefficient signs are \(+,+,-,+\), giving at most two positive zeros by Descartes' rule; the two sign changes ensure there are exactly two distinct positive roots. The sign of \(H_m\) is consequently negative precisely between them, and zero at the boundaries. For large \(m\), substituting \(B=s/m\) into \(m^{-3}H_m(B)\) gives the limit \(2-s\) for fixed \(s>0\). Substituting \(B=s m^2\) into \(m^{-6}H_m(B)\) gives \(s^3-s\). Bracketing the two unique positive roots with these limiting signs proves \(mB_-(m)\to2\) and \(B_+(m)/m^2\to1\).

**5. Objective on the hub-free interval.** Substitute \(p=0\), \(q=B/m\) into the formula from step 2 and simplify to obtain \(m(m-1)/(m+B)+(m+1)/B+1/m\), proving the stated exact minimum. Every equality and boundary case follows from the unique minimizer already established.

## Verification
Run `python3 verify_star_gain.py` from the same directory; it requires only the Python standard library. The program independently builds and inverts pinned star matrices using exact rational Gauss–Jordan elimination, compares their traces and diagonal-square gradients to the arrowhead formulas, checks the symbolic boundary-derivative identities on rational inputs, and tests the root and active-set classification over a broad collection of \(m\) and \(B\). It prints `VERIFY_OK: 15472 exact-rational and numerical assertions`. The algebra and convexity arguments above, not the finite computations, establish the universal statement.

## Relationship to prior work
Lin, Fardad and Jovanović (2013) formulate noisy leader selection through the same inverse-trace objective and a convex relaxation of Boolean leader choices, but their general matrix optimization does not derive the exact reentrant star hub-budget classification. Fitch and Leonard (2014) analyze fixed-size sets of finite-strength or ideal leaders and joint-centrality formulas; their path/cycle cases and one-/two-leader results do not optimize all independent gains under a summed continuous budget. Li, Duan and Chen (2007) analyze synchronization costs and star pinning but not this stationary-noise inverse-trace criterion. Lin, Fardad and Jovanović (2010) study optimized *edge* feedback gains and mean-centered consensus, rather than these diagonal ground gains. Related exact results on star spectral-gap allocations and discrete perfect-leader placement address distinct performance indices or decision variables. Inverse-trace convexity is prior mathematics; the new statement is the explicit all-budget triple regime and its sharp leaf-count and budget thresholds.

## Limitations
The law is star-specific, assumes unit fixed spoke conductances, unit per-node feedback prices and independent isotropic white forcing, and optimizes trace inverse rather than maximum decay rate or spectral condition number. It gives an implicit scalar stationary-point characterization when the hub is active, not radicals for that optimizer. No real-world noise or robustness experiment is claimed. Older inaccessible or unindexed specialized optimal-gain studies might contain equivalent statements; a database search cannot certify publication priority. The analytical proof is a mathematical argument, not independent validation.

## References
- F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first submitted 2013-02-03. https://arxiv.org/abs/1302.0450
- K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first submitted 2014-07-07. https://arxiv.org/abs/1407.1569
- R. Li, Z. Duan and G. Chen, *Cost and Effects of Pinning Control for Network Synchronization*, arXiv:0710.2716, first submitted 2007-10-15. https://arxiv.org/abs/0710.2716
- F. Lin, M. Fardad and M. R. Jovanović, *On the Optimal Localized Feedback Design for Multi-Vehicle Systems*, 2010, https://ecs.syr.edu/faculty/fardad/Papers/LinFarJov10b.pdf
- S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first submitted 2014-12-20. https://arxiv.org/abs/1412.6595
