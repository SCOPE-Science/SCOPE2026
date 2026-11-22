# Irreversible edge fusion on weighted cycles: a four-vertex rigidity theorem and a triangle exception

## Finding

Let \(n\ge3\), let \(m_i>0\) be vertex fidelity masses and \(a_i>0\) be edge penalties on the cyclic edge from vertex \(i\) to \(i+1\), where indices are interpreted modulo \(n\). For arbitrary real data \(y=(y_i)\), let \(u(\lambda)\) uniquely minimize
\[
 F_\lambda(u)=\frac12\sum_{i=0}^{n-1}m_i(u_i-y_i)^2+\lambda\sum_{i=0}^{n-1}a_i|u_{i+1}-u_i|,\qquad \lambda\ge0.
\]
Say the penalty profile has **universal irreversible edge fusion** if for every \(y\), every cyclic edge \(i\), and every \(0\le\lambda_0\le\lambda_1\), the equality \(u_i(\lambda_0)=u_{i+1}(\lambda_0)\) implies \(u_i(\lambda_1)=u_{i+1}(\lambda_1)\).

**Theorem.** If \(n\ge4\), universal irreversible edge fusion holds if and only if \(a_0=\cdots=a_{n-1}\). The criterion is independent of the positive fidelity masses. If \(n=3\), it holds if and only if, for each \(i\in\{0,1,2\}\),
\[
 \left|m_{i+1}a_{i-1}-m_i a_{i+1}\right|\le(m_i+m_{i+1})a_i.
\]
Consequently the nonconstant triangle weights \((a_0,a_1,a_2)=(1,2,2)\) with unit masses permit irreversible edge fusion for every data vector, whereas every nonconstant positive edge profile on a cycle with at least four vertices admits data for which a fitted edge fuses and later separates.

## Assumptions and scope

The vertex and edge weights are fixed and strictly positive; the graph is the simple undirected cycle with \(n\ge3\) vertices; fidelity is strictly convex, quadratic and diagonal; all edge penalties are multiplied by the same nonnegative scalar \(\lambda\). Fusion is equality of adjacent fitted coordinates, not equality of data coordinates. The statement requires persistence for **all** data and every regularization level, rather than persistence for a particular signal. Neither a ring with a duplicated parallel edge nor a path with special endpoint penalties is being identified with this cycle.

## Proof

**1. Flux optimality.** Strict convexity gives a unique fit. For \(\lambda>0\) it is characterized by fluxes \(q_i\in[-a_i,a_i]\), where \(q_i=a_i\operatorname{sign}(u_{i+1}-u_i)\) whenever the edge difference is nonzero, and
\[
 m_i(u_i-y_i)+\lambda(q_{i-1}-q_i)=0\quad\text{for every }i.
\]
This follows by taking the subgradient of every absolute edge difference. Conversely, these equations and sign conditions imply global optimality; strict convexity implies uniqueness.

**2. Persistence formula for a proper fused block.** Between consecutive changes in the finitely piecewise-affine solution path, let \(B=\{r,r+1,\ldots,s\}\) be a maximal proper contiguous block of equal fitted values \(c\), with both external edge differences nonzero. Call their fixed signed fluxes \(q_L=q_{r-1}\) and \(q_R=q_s\); these are constant on the interval because their edge signs are fixed. Let \(M_B=\sum_{j=r}^s m_j\), \(\bar y_B=M_B^{-1}\sum_{j=r}^s m_jy_j\), and \(\theta_e=M_B^{-1}\sum_{j=r}^{e}m_j\) for an internal edge \(e\in\{r,\ldots,s-1\}\). Summing the optimality equations gives \(c=\bar y_B+\lambda(q_R-q_L)/M_B\), and summing up to the internal edge gives
\[
 q_e(\lambda)=(1-\theta_e)q_L+\theta_e q_R+\frac1\lambda\sum_{j=r}^{e}m_j(\bar y_B-y_j).
\]
In particular, if the block exists at \(\lambda_0>0\), then at later levels with unchanged exterior signs,
\[
 q_e(\lambda)=\frac{\lambda_0}{\lambda}q_e(\lambda_0)+\left(1-\frac{\lambda_0}{\lambda}\right)\big((1-\theta_e)q_L+\theta_e q_R\big).
\]
Thus every internal flux stays feasible whenever both its initial flux and its limiting exterior-flux average lie in \([-a_e,a_e]\).

**3. Sufficiency.** When \(n\ge4\) and all \(a_i=a\), each exterior flux is of absolute value \(a\), and their convex average is in \([-a,a]\). Hence no proper fused block can become infeasible merely because regularization increases. When \(n=3\), the only nontrivial proper fused blocks have two vertices. Their two exterior edges both attach to the same remaining vertex and necessarily carry opposite signs; for the fused edge \(i\), their convex average has absolute value
\[
 A_i=\frac{|m_{i+1}a_{i-1}-m_i a_{i+1}|}{m_i+m_{i+1}},
\]
which is at most \(a_i\) exactly under the three stated inequalities. A fully fused solution remains fully fused at later \(\lambda\): preserve its constant fitted value (the mass-weighted global mean) and rescale every feasible flux by \(\lambda_0/\lambda\). At \(\lambda=0\), any initially equal data remain equal for sufficiently small positive \(\lambda\) by the same subgradient continuation for their maximal equal-data blocks; the preceding inequalities control their internal fluxes, while all initially nonzero edge differences retain their signs locally. A finite polyhedral solution path has only finitely many affine regimes on a bounded interval; a first breaking event would contradict the flux continuation argument. Consequently all fused edges persist for every \(\lambda\ge\lambda_0\).

**4. Necessity via a controllable two-site block.** For an internal edge \(i\), put
\[
 A=\frac{m_{i+1}q_L+m_iq_R}{m_i+m_{i+1}}.
\]
Choose prescribed exterior signs such that \(A>a_i\), and at \(\lambda_0=1\) prescribe a fitted vector with \(u_i=u_{i+1}=c\), all other neighboring differences nonzero and widely separated, along with internal flux \(q_i(1)=-a_i\). Put the other fluxes at the signed edge limits; choose the original data by the exact stationarity inversion
\[
 y_j=u_j+\frac{q_{j-1}-q_j}{m_j}.
\]
Then this vector is the unique minimizer at \(\lambda=1\). As long as the exterior gaps stay open, the hypothesized fused pair would require
\[
 q_i(\lambda)=A-\frac{A+a_i}{\lambda}.
\]
It is feasible for \(1\le\lambda\le\lambda_*=(A+a_i)/(A-a_i)\), but exceeds \(a_i\) at every slightly larger level. The two-site fused branch actually exists for an interval with positive length after \(\lambda=1\) by the flux formula and the initial exterior sign separation. Choose all other fitted coordinates with large, pairwise-separated magnitudes; since the KKT equations imply
\[
 |u_j(\lambda)-y_j|\le\lambda\frac{a_{j-1}+a_j}{m_j},
\]
these exterior signs remain unchanged through \(\lambda_*+\delta\) for some \(\delta>0\). Therefore fusion cannot persist: the selected edge separates. For a positive \(A\) of opposite sign, reverse all fitted values and fluxes.

For \(n\ge4\), every nonconstant cyclic profile has an edge \(i\) with minimal \(a_i\) adjacent to a strictly larger neighboring penalty (choose an endpoint of a plateau of minima). Prescribe both external fluxes positive: \(q_L=a_{i-1}\) and \(q_R=a_{i+1}\). A fitted pair between a much lower left neighbor and a much higher right neighbor realizes both signs (this requires four distinct vertices). Then
\[
 A=\frac{m_{i+1}a_{i-1}+m_i a_{i+1}}{m_i+m_{i+1}}>a_i.
\]
For \(n=3\), the third vertex lies on both exterior edges, so their signs are forced to be opposite. One obtains either sign of
\[
 A=\frac{m_{i+1}a_{i-1}-m_i a_{i+1}}{m_i+m_{i+1}}.
\]
If the triangle inequality in the theorem fails, choose the third coordinate on the appropriate side and reverse the global sign if needed to make \(A>a_i\). The same construction forces unfusion. This proves both converses.

**5. Explicit certificates.** For \(n=4\), choose \(m=(1,1,1,1)\), \(a=(1,2,3,4)\), \(y=(5,-3,105,-107)\). On \(1\le\lambda\le2\), the unique fit is
\[
 u(\lambda)=(1-\lambda,1-\lambda,105-5\lambda,-107+7\lambda)
\]
with admissible flux \(q=(3-4/\lambda,2,-3,4)\). For \(2<\lambda\le3\), it is
\[
 u(\lambda)=(5-3\lambda,-3+\lambda,105-5\lambda,-107+7\lambda)
\]
with flux \(q=(1,2,-3,4)\). The first two vertices are fused at \(\lambda=3/2\) but separated at \(\lambda=5/2\). For \(n=3\), choose \(m=(1,1,1)\), \(a=(1,1,4)\), \(y=(5,0,-105)\). On \(1\le\lambda\le5\), the fit is
\[
 u(\lambda)=((5-5\lambda)/2,(5-5\lambda)/2,-105+5\lambda)
\]
with \(q=(3/2-5/(2\lambda),-1,4)\). On \(5<\lambda\le7\), it is
\[
 u(\lambda)=(5-3\lambda,-2\lambda,-105+5\lambda)
\]
with \(q=(1,-1,4)\). Thus the first edge is fused at \(\lambda=3\) but separated at \(\lambda=6\). All displayed branches satisfy the exact KKT equations and sign restrictions.

## Verification

The accompanying standalone `check_cycle.py` uses exact rational arithmetic to check the KKT equations and subgradient feasibility for eight regularization levels in each explicit witness, as well as the predicted fusion/unfusion. It checks a nonconstant stable triangle and 1,700 seeded finite weighted-cycle examples of the minimum-edge obstruction. The finite checks are not an exhaustive verification of the universal quantifiers: those follow from the flux-continuation and minimizer-construction proofs above. Execute `python check_cycle.py` with a standard Python 3 installation; no third-party package is required.

## Relationship to prior work

Hoefling's *A path algorithm for the Fused Lasso Signal Approximator* (arXiv:0910.0526, publicly submitted 3 October 2009) develops graph fused-lasso solution paths, including possible splitting and maximum-flow tests for general graphs. Tibshirani and Taylor's *The solution path of the generalized lasso* (2011) develops a general dual path and a boundary lemma, giving a prior route to sufficiency in familiar equal-penalty settings. Bento, Furmaniak and Ray's *On the Complexity of the Weighted Fused Lasso* (arXiv:1801.04987) addresses weighted paths and unfusion phenomena. These sources supply general methodology or special cases; the contribution isolated here is the complete **necessary-and-sufficient, all-data cycle-penalty classification**, especially the rigid four-vertex onset, mass-independence beyond the triangle, and the nonconstant admissible triangle regime. The known equal-penalty sufficiency and the existence of graph unfusion are not represented as novel. No claim is made about graphs with branches or chords.

## Limitations

The classification is for fixed finite simple cycles and a single common TV-regularization strength. The fidelity must be positive diagonal quadratic, and no additional absolute-value sparsity penalty, boundary condition, or nonconvex loss is included. The theorem is a universal-for-all-data statement; some particular signals may fuse monotonically even when the profile fails the criterion. The analytic proof establishes event structure and existence of counterexamples without giving a graph-independent bound on their splitting times. Historical-priority uncertainty remains because indexing and source access cannot exclude all equivalent older statements. The source-date field records an archival founding paper's first public date, not a publication date for the present theorem.

## References

1. H. Hoefling, *A path algorithm for the Fused Lasso Signal Approximator*, arXiv:0910.0526, first posted 3 October 2009, https://arxiv.org/abs/0910.0526.
2. R. J. Tibshirani and J. Taylor, *The solution path of the generalized lasso*, Annals of Statistics **39** (2011), 1335–1371, https://www.stat.cmu.edu/~ryantibs/papers/genlasso-aos.pdf.
3. J. Bento, A. Furmaniak and S. Ray, *On the Complexity of the Weighted Fused Lasso*, arXiv:1801.04987, https://arxiv.org/abs/1801.04987.
