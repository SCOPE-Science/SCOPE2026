# The first interior-node obstruction for spectral quadrature on a tensor Veronese ball

## Finding
Let \(d\ge1\) be an integer, and let \(e_d^{\square}(n)\) be the smallest deterministic worst-case integration error on the class defined below when at most \(n\) function evaluations may be made in \([0,1]^d\). These evaluations may be adaptive and the final estimate nonlinear. Let \(\tau_{n,d}\) be the nuclear-norm spectral tail of the integration matrix (defined below), the standard lower bound for \(n\) evaluations. Then
\[
e_d^{\square}(n)=\tau_{n,d}\quad(n=0,1,2),\qquad
e_d^{\square}(n)>\tau_{n,d}\quad(3\le n\le d+1,\ d\ge2).
\]
In particular, **three evaluations are the first count at which restricting the sites to the physical cube necessarily loses the spectral optimum**, even with signed weights, adaptation, or nonlinear postprocessing.

The underlying first-excitation spectral compression \(H_{d,r}\) also admits a sharp positive-atomic representation classification: for each \(1\le r\le d\), a finite positive combination of physical-cube evaluation matrices equals \(H_{d,r}\) if and only if \(r\le3\). For \(r=1,2,3\), exactly \(2r\) atoms are necessary and sufficient, at explicitly specified symmetric physical-cube nodes. For \(r\ge4\), no number of positive physical-cube atoms can represent this compression.

## Assumptions and scope
Write \(\theta(x)=(x-1/2)/2\), \(z(x)=(\cos\theta(x),\sin\theta(x))^{\mathsf T}\), and \(v_d(x)=\bigotimes_{j=1}^{d}z(x_j)\). For a real symmetric matrix \(M\) of size \(2^d\) with operator norm at most one, put \(f_M(x)=v_d(x)^{\mathsf T}Mv_d(x)\), with \(x\in\mathbb R^d\). The input class is exactly \(\{f_M:\ M=M^{\mathsf T},\ \|M\|_{\mathrm{op}}\le1\}\), with its induced quotient norm on functions. Its real linear span has dimension \(3^d\). The integral is \(I_d(f)=\int_{[0,1]^d}f(x)\,dx\).

Let \(K_d(x)=v_d(x)v_d(x)^{\mathsf T}\). The integration matrix is
\[
G_d=\int_{[0,1]^d}K_d(x)\,dx
=\operatorname{diag}(q,p)^{\otimes d},\quad
q=\tfrac12+\sin(\tfrac12),\quad p=\tfrac12-\sin(\tfrac12).
\]
Thus its \(2^d\) positive eigenvalues are \(q^{d-k}p^k\) with multiplicities \(\binom dk\). Arrange them nonincreasingly as \(\lambda_j\), and set \(\tau_{n,d}=\sum_{j>n}\lambda_j\), interpreted as zero for \(n\ge2^d\).

Denote by \(e_\emptyset\) the tensor basis vector with all factors \((1,0)\), and by \(e_j\) the vector with only the \(j\)-th factor equal to \((0,1)\). For \(1\le r\le d\), define the positive rank-\(r+1\) *first-excitation compression*
\[
H_{d,r}=q^d e_\emptyset e_\emptyset^{\mathsf T}+q^{d-1}p\sum_{j=1}^r e_je_j^{\mathsf T}.
\]
The word `positive` in the representation classification refers to strictly positive quadrature coefficients. No positivity restriction is imposed on arbitrary competing algorithms in the worst-case error statement.

## Proof
**1. Nuclear-norm formulation and the equality case.** For fixed evaluation sites, the optimal linear recovery error on this operator-norm matrix ball is \(\inf_{a_i\in\mathbb R}\|G_d-\sum_i a_iK_d(x_i)\|_*\). This follows by duality between operator and nuclear norm and Hahn–Banach distance to the span of the observations. It also gives the lower bound for adaptive, nonlinear algorithms: run one on the zero input; its selected sites are then fixed, while the two inputs \(\pm f_M\) with \(\operatorname{tr}(MK_d(x_i))=0\) give identical observations. Their worst-case separation is exactly the dual-norm distance. Consequently
\[
e_d^\square(n)=\inf_{x_i\in[0,1]^d,\ a_i\in\mathbb R}
\bigl\|G_d-\sum_{i=1}^na_iK_d(x_i)\bigr\|_*.
\]
If \(Q\) is any symmetric matrix of rank at most \(n\), let \(W=\operatorname{ran}Q\), \(P\) be the orthogonal projector onto \(W^\perp\), and \(E=G_d-Q\). Then
\[
\|G_d-Q\|_*\ge\operatorname{tr}(PE)=\operatorname{tr}(PG_d)\ge\tau_{n,d}.
\]
Equality with \(n\le d+1\) forces \(\operatorname{rank}Q=n\), \(E\succeq0\) supported entirely on \(W^\perp\), and \(W\) to be a maximizing \(n\)-plane for the eigenvalue sum. Indeed, the equality condition in \(\|E\|_*\ge\operatorname{tr}(PE)\) forces each positive eigenvector of \(E\) into \(W^\perp\) and excludes negative eigenvalues; rank loss would discard another positive eigenvalue. Thus \(W\) reduces \(G_d\) and \(Q=G_d|_W\). When \(n=r+1\le d+1\), this means
\[
W=\operatorname{span}\{e_\emptyset\}\oplus U,
\quad U\subseteq\operatorname{span}\{e_1,\ldots,e_d\},\quad\dim U=r.
\]

**2. Why the first shell needs twice as many sites.** Suppose a rank-\(r+1\) equality matrix \(Q=G_d|_W\) were a sum of at most \(r+1\) physical-cube evaluation matrices. Its \(r+1\) strictly positive eigenvalues force exactly \(r+1\) linearly independent evaluation vectors and all their coefficients to be positive: Sylvester inertia applied to \(V\operatorname{diag}(a_i)V^{\mathsf T}\) bounds its positive inertia by the number of positive \(a_i\).

Each evaluation vector must belong to \(W\), since a positive sum of outer products has range equal to the span of its summand vectors. For cube sites \(|\theta(x_j)|\le1/4\), all \(\cos\theta(x_j)>0\). If two different coordinates have nonzero sine factors, the product vector has a nonzero double-excitation coordinate, which is impossible in \(W\). Hence each noncentral evaluation vector has the form \(\cos t\,e_\emptyset+\sin t\,e_j\) for a single \(j\). The active coordinate vectors must span \(r\) distinct axes, because \(\dim U=r\). On every such axis the target matrix has zero \((e_\emptyset,e_j)\) cross entry and a strictly positive \((e_j,e_j)\) entry. With positive weights and positive \(\cos t\), there must be **at least one positive and one negative** nonzero \(\sin t\) on each active axis. Therefore at least \(2r\) evaluation nodes are necessary. For \(r\ge2\), \(r+1<2r\); equality is impossible.

This exclusion is strict at the infimum, not only for attained formulas. If \(Q_k=\sum_{i=1}^{r+1}a_{ki}K_d(x_{ki})\) approached nuclear error \(\tau_{r+1,d}\), the error bound would keep \(Q_k\) bounded. A subsequence would converge to the rank-\(r+1\) positive equality matrix just characterized. For sufficiently large \(k\), each \(Q_k\) has \(r+1\) positive eigenvalues, so its \(r+1\) coefficients are all positive. Since \(\operatorname{tr}K_d(x)=1\), their sum \(\operatorname{tr}Q_k\) is bounded. Compactness of the cube and of bounded nonnegative coefficients yields a positive \((r+1)\)-atom representation of the limiting equality matrix, contradicting the preceding counting argument. Thus the difference from \(\tau_{r+1,d}\) is a strictly positive (dimension-dependent) number.

**3. The sharp positive-atomic threshold.** For the specified diagonal \(H_{d,r}\), every positive atom must be supported on its range and therefore can vary along at most one of the first \(r\) coordinate axes. For a node on axis \(j\), its vacuum-to-excitation diagonal contribution ratio is \(\cot^2 t\ge\cot^2(1/4)\). Summing the contributions gives the necessary inequality
\[
q^d\ge r q^{d-1}p\cot^2(1/4),
\quad\text{equivalently}\quad
r\le\frac{q}{p\cot^2(1/4)}.
\]
The strict inequalities \(3<q/(p\cot^2(1/4))<4\) follow from the elementary alternating Taylor bounds for \(\sin(1/2)\), \(\sin(1/4)\), and \(\cos(1/4)\); the rational bounds \(47\le q/p<50\) and \(15<\cot^2(1/4)<31/2\) already suffice.

Conversely, if \(r\le3\), set \(t_r=\arctan\sqrt{rp/q}\), so \(0<t_r<1/4\). For each \(j=1,\ldots,r\), take the two physical-cube nodes with all coordinates \(1/2\) except \(x_j=1/2\pm2t_r\), and give each weight
\[
a_r=\frac{q^{d-1}p}{2\sin^2 t_r}>0.
\]
The opposite cross terms cancel, the \(j\)-th excitation diagonal has total mass \(2a_r\sin^2t_r=q^{d-1}p\), and the vacuum diagonal has mass \(2r a_r\cos^2t_r=q^d\). This gives exactly \(H_{d,r}\), with \(2r\) nodes. The sign-cancellation argument proves that fewer positive nodes are impossible.

**4. The zero-, one-, and two-evaluation cases.** At \(n=0\), zero is optimal and the error is \(\operatorname{tr}G_d=1\). At \(n=1\), the central node with weight \(q^d\) represents \(H_{d,0}=q^d e_\emptyset e_\emptyset^{\mathsf T}\), attaining error \(1-q^d\). At \(n=2\), the \(r=1\) construction represents \(H_{d,1}\) and attains error \(1-q^d-q^{d-1}p=1-q^{d-1}\). This proves all assertions.

## Verification
A standard-library Python script `checks/verify.py` establishes rational Taylor enclosures for the strict threshold \(3<q/(p\cot^2(1/4))<4\), then numerically checks the explicit positive atomic construction for \(1\le d\le7\) and \(1\le r\le\min(d,3)\), as well as further spectral-tail identities. Invocation: `python3 checks/verify.py`. The observed output is in `checks/verification-output.txt` (`VERIFY_OK 213`). The universal claims rely on the analytic proof above, not on the finite script.

## Relationship to prior work
Sengelen Sevim's 2026 work on integration of infinitely differentiable functions obtains a dimension-dependent spectral lower bound for deterministic integration on the cube. Earlier work by Hinrichs, Krieg, Novak, and Vybíral supplies Hilbert-space cubature lower-bound techniques. The present theorem concerns a specifically defined operator-norm tensor trigonometric subball and distinguishes *attainment* of a spectral lower bound by physical-cube point evaluations from the lower bound itself. Its positive-atomic representation criterion and the exact third-evaluation obstruction are not implied by a spectral tail formula alone. No historical priority or independence beyond the documented comparisons is claimed.

## Limitations
The strict gap for \(3\le n\le d+1\) is proved without an explicit numerical size. The representability threshold applies only to the indicated leading spectral compression, not to arbitrary positive matrices or to exact integration after including all spectral shells. The result is deterministic and worst-case on this finite-dimensional class; it makes no claim about Monte Carlo error or the entire ambient smooth-function unit ball. Full text of one closely related 2026 article was inaccessible for independent priority checking; an unindexed equivalent result may exist. No external mathematical audit has been performed.

## References
1. E. Sengelen Sevim, *The curse of dimensionality for integration of infinitely differentiable functions*, Journal of Complexity 97 (2026), article 102074, DOI: https://doi.org/10.1016/j.jco.2026.102074 (public online report 14 August 2026).
2. A. Hinrichs, D. Krieg, E. Novak and J. Vybíral, *Lower bounds for the error of quadrature formulas for Hilbert spaces*, Journal of Complexity 65 (2021), article 101544, arXiv:2004.00274, https://doi.org/10.1016/j.jco.2020.101544.
3. E. Novak, *Intractability results for positive quadrature formulas and extremal problems for trigonometric polynomials*, Journal of Complexity 15 (1999), 299–316, https://doi.org/10.1006/jcom.1999.0507.
