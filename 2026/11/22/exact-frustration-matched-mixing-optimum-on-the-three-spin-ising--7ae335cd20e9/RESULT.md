# Exact frustration-matched mixing optimum on the three-spin Ising cycle

## Finding
For every ferromagnetic reference coupling \(K>0\), inverse temperature \(\beta>0\), and defect ratio \(h\geq0\), consider the zero-field Ising triangle with exchanges \((J_{12},J_{23},J_{13})=(K,K,-hK)\). Under continuous-time single-site heat-bath Glauber dynamics with **each vertex updated at rate one**, the complete Markov spectral gap \(g_\beta(h)\) is strictly increasing on \(0\leq h\leq1\) and strictly decreasing on \(h\geq1\), with the unique optimum
\[
\boxed{\max_{h\geq0}g_\beta(h)=g_\beta(1)=1-\tfrac12\tanh(2\beta K).}
\]
The dependence has a genuine cusp at the optimum. For each **fixed** \(h\ne1\), \(g_\beta(h)\to0\) as \(\beta K\to\infty\), but \(g_\beta(1)\to1/2\). The transition occurs within the sharp \(1/(\beta K)\)-scale window: for every fixed real \(u\), taking \(h=1+u/(\beta K)\) gives
\[
\boxed{\lim_{\beta K\to\infty}g_\beta\!\left(1+\frac{u}{\beta K}\right)=\frac{1}{1+e^{2|u|}}.}
\]
For fixed \(u<0\), the parameter \(h\) is positive for sufficiently large \(\beta K\). These statements concern the finite-state Markov spectral gap, not merely the magnetization mode.

## Assumptions and scope
A configuration is \(\sigma=(\sigma_1,\sigma_2,\sigma_3)\in\{-1,+1\}^3\); its Gibbs probability is proportional to \(\exp\{\beta K(\sigma_1\sigma_2+\sigma_2\sigma_3-h\sigma_1\sigma_3)\}\). Independently at rate one, each site resamples its spin from the exact Gibbs conditional distribution given the other two sites. The generator \(L\) acting on observables is
\[
(Lf)(\sigma)=\sum_{i=1}^3\frac{f(\sigma^{(i)})-f(\sigma)}{1+\exp(2\beta\sigma_i\sum_{j\ne i}J_{ij}\sigma_j)},
\]
where \(\sigma^{(i)}\) flips site \(i\). The spectral gap is the least strictly positive eigenvalue of \(-L\) in the finite-state reversible chain. Write \(t=\beta K\), and define
\[
\begin{aligned}
x&=\tanh(t(1+h)),&y&=\tanh(t(1-h)),\\
a&=(x+y)/2,&b&=(x-y)/2,\\
c&=\tfrac12\tanh(2t),&R&=\sqrt{b^2+8ac}.
\end{aligned}
\]
For finite \(t>0\) and \(h\geq0\), \(a>0\), \(c>0\), \(0\leq b<1\), and \(a,c<1\).

## Proof
**1. Complete invariant-block decomposition.** The heat-bath identities give
\[
\begin{aligned}
L\sigma_1&=-\sigma_1+a\sigma_2-b\sigma_3,\\
L\sigma_2&=c\sigma_1-\sigma_2+c\sigma_3,\\
L\sigma_3&=-b\sigma_1+a\sigma_2-\sigma_3.
\end{aligned}
\]
The odd-observable sector is spanned by \(\sigma_1,\sigma_2,\sigma_3,\sigma_1\sigma_2\sigma_3\). Its degree-one subspace is invariant, and the three-spin monomial has diagonal generator coefficient \(-3\) modulo the degree-one subspace, because
\[
L(\sigma_1\sigma_2\sigma_3)=-3\sigma_1\sigma_2\sigma_3+(a+c)(\sigma_1+\sigma_3)-2b\sigma_2.
\]
Exchange of sites \(1\) and \(3\) separates the degree-one operator into one antisymmetric eigenmode with eigenvalue \(-1+b\) and a symmetric two-dimensional block with eigenvalues \(-1-b/2\pm R/2\). Thus the odd-sector decay rates are \(1-b\), \(1+(b-R)/2\), \(1+(b+R)/2\), and \(3\).

For the even sector, set \(Q_{ij}=\sigma_i\sigma_j\). Direct substitution yields
\[
\begin{aligned}
LQ_{12}&=(a+c)-2Q_{12}-bQ_{23}+cQ_{13},\\
LQ_{23}&=(a+c)-2Q_{23}-bQ_{12}+cQ_{13},\\
LQ_{13}&=-2b-2Q_{13}+a(Q_{12}+Q_{23}).
\end{aligned}
\]
Together with \(L1=0\), this gives the even-sector decay rates \(0\), \(2-b\), \(2+(b-R)/2\), and \(2+(b+R)/2\). Every nonconstant even-sector decay rate exceeds a corresponding odd-sector decay rate by one, while the additional three-spin rate is \(3\). Since the chain is irreducible for finite \(\beta\), the **full** gap is
\[
\boxed{g_\beta(h)=\min\!\left\{1-b,\;1+\frac{b-R}{2}\right\}.}
\]
In particular, the exact characteristic polynomial of \(-L\), with indeterminate \(z\), is
\[
z(z-3)(z-1+b)(z-2+b)
\big((z-1)^2-b(z-1)-2ac\big)
\big((z-2)^2-b(z-2)-2ac\big).
\]
No large-system limit or numerical diagonalization is needed for this identity.

**2. Exact optimum.** For fixed \(t>0\), \(a(h)\) decreases strictly for \(h>0\), while \(b(h)\) increases strictly for \(h\geq0\). At \(h=1\), \(a=b=c\). Hence for \(h<1\), \(a>c>b\), whereas for \(h>1\), \(0<a<c<b<1\). Define \(\rho=(-b+R)/2\), the positive solution to \(\rho^2+b\rho=2ac\). The inequalities \(ac>b^2\) for \(h<1\) and \(ac<b^2\) for \(h>1\) imply respectively \(\rho>b\) and \(\rho<b\). Therefore
\[
g_\beta(h)=\begin{cases}
1-\rho(h),&0\leq h\leq1,\\
1-b(h),&h\geq1.
\end{cases}
\]
Differentiating \(\rho^2+b\rho=2ac\),
\[
\rho'(h)=\frac{2c a'(h)-b'(h)\rho(h)}{2\rho(h)+b(h)}<0
\]
for \(0\leq h\leq1\). For \(h>1\), \(b'(h)>0\). This proves strict monotonicity on either side and the unique maximum \(1-c\). The one-sided derivatives at \(h=1\) have opposite nonzero signs, establishing the cusp.

**3. Singular low-temperature boundary layer.** If \(h\ne1\) is fixed, then \((a,b,c)\to(1,0,1/2)\) when \(h<1\), and \((a,b,c)\to(0,1,1/2)\) when \(h>1\); the exact gap formula tends to zero. At \(h=1\), \(g=1-c\to1/2\). For \(h=1+u/t\) with fixed \(u\), the limit of \((a,b,c)\) is
\[
\left(\frac{1-\tanh u}{2},\frac{1+\tanh u}{2},\frac12\right).
\]
For \(u<0\), substitution yields \(\rho=(1-\tanh u)/2\); for \(u\geq0\), the other branch gives \(1-b=(1-\tanh u)/2\). Thus the limit on both sides is \((1-|\tanh u|)/2=1/(1+e^{2|u|})\), including \(u=0\).

## Verification
The accompanying standalone Python 3 program `verify.py` enumerates all eight spin configurations. For 64 pairs of rational bond Boltzmann factors, it computes every transition rate exactly using rational arithmetic and checks all 64 monomial-generator identities per parameter pair, totaling **4096 exact equalities**. It verifies the odd/even invariant-block identities used in the symbolic proof without making claims about untested real parameters. Run `python3 verify.py` from the directory containing this file; no external packages are required. The analytic proof above, rather than the finite test grid, establishes the universal quantifiers.

## Relationship to prior work
Nacu's ferromagnetic-cycle theorem proves monotonic slowing when **all** cycle exchanges are nonnegative; his exact linear-spin reduction is a relevant structural precursor, but its sign and Perron arguments do not prove the present *opposite-sign*, nonmonotone defect law. Pini and Rettori analyze antiferromagnetic nearest-neighbor chains with driving fields and a competing-next-neighbor model, rather than the full reversible Markov gap under a single negative triangular bond. Ismail and Salem study a six-spin triangular-lattice cluster with competing interactions; the accessible abstract does not establish the three-spin defect optimum, but the full paper was not available for a conclusive content comparison. The complete eight-state block calculation and the boundary-layer scaling here are not supplied by those stated results.

## Limitations
The result is for three spins, zero external field, two equal positive bonds, one negative bond, and rate-one heat-bath updates. It does not assert the identical optimum for larger rings, non-heat-bath rates, or unequal positive bonds. It is a finite Markov relaxation phenomenon, not a thermodynamic phase transition. The historical-priority assessment is based on located sources and does not certify novelty against unindexed literature; one relevant six-spin paper could not be inspected in full.

## References
- S. Nacu, *Glauber Dynamics on the Cycle Is Monotone*, arXiv:math/0305056v1, first public 2003-05-03. https://arxiv.org/abs/math/0305056
- M. G. Pini and A. Rettori, *Effect of antiferromagnetic exchange interactions on the Glauber dynamics of one-dimensional Ising models*, arXiv:0707.1953v1, first public 2007-07-13. https://arxiv.org/abs/0707.1953
- G. Ismail and A. Salem, *Dynamics of Ising spins with antiferromagnetic bonds on a triangular lattice*, first online 2003-04-16, doi:10.1002/pssb.200301657. https://doi.org/10.1002/pssb.200301657
