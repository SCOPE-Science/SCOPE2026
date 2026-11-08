# A sharp transverse stability boundary for polarized co-evolving opinion leadership

## Finding

The state-dependent opinion--leadership model of Alutto, Zino, Johansson and Fontan admits an exactly invariant two-camp polarization mode. All trajectories initialized in this mode converge exponentially to an explicit partially polarized equilibrium. In the minimal two-agent network the same equilibrium, although attracting within the mode, is locally attracting under **arbitrary small opinion and leadership perturbations** precisely when
\[
\alpha>2\beta\kappa^3.
\]
For \(\alpha<2\beta\kappa^3\) it is instead a hyperbolic saddle with exactly one unstable mode. At equality the linearization has one zero eigenvalue and we make no nonlinear stability assertion. The threshold is independent of the initial opinion magnitude.

## Assumptions and scope

For \(n\ge2\), let \(W\) be a nonnegative row-stochastic matrix and write \(L=I-W\). Opinions \(x_i\) and endogenous leadership weights \(y_i\) follow
\[
\begin{aligned}
\dot x_i&=-(1-y_i)(Lx)_i-y_i(x_i-x_i(0)),\\
\dot y_i&=\alpha(1-y_i)x_i^2-\beta y_i(Lx)_i^2,
\end{aligned}\tag{1}
\]
with common parameters \(\alpha,\beta>0\). The initial opinions are fixed anchors in the right-hand side, not time-varying state variables.

Assume that a sign vector \(s\in\{-1,1\}^n\), taking both signs, satisfies \(Ws=(1-\kappa)s\) for some \(0<\kappa\le2\). Take \(x_i(0)=a s_i\) with \(0<a\le1\) and \(y_i(0)=y_0\) with \(0\le y_0\le1\). For the full stability assertion, specialize to exactly two agents,
\[
W=\begin{pmatrix}1-\kappa/2&\kappa/2\\ \kappa/2&1-\kappa/2\end{pmatrix},
\quad s=(1,-1)^\top.
\]
No conclusion on full-state stability for arbitrary larger networks is claimed.

## Proof

**Exact signed reduction and attraction.** Under the signed ansatz \(x_i=s_i u\) and common \(y_i=y\), we have \((Lx)_i=\kappa s_i u\), so (1) reduces identically to
\[
\begin{aligned}
\dot u&=-[\kappa+(1-\kappa)y]u+ay,\\
\dot y&=(\alpha+\beta\kappa^2)u^2(y_*-y),
\qquad y_*:=\frac{\alpha}{\alpha+\beta\kappa^2}.
\end{aligned}\tag{2}
\]
The coefficient \(A(y)=\kappa+(1-\kappa)y=\kappa(1-y)+y\) is positive on \([0,1]\). At \(u=0\) the first derivative is nonnegative, at \(u=a\) it equals \(-a\kappa(1-y)\le0\), and the leadership derivative points inward at \(y=0,1\). Hence \([0,a]\times[0,1]\) is invariant and \(u(t)>0\) at all finite times from the stipulated initial state. The leadership coordinate is monotone toward \(y_*\). If initially \(y_0=0\), its derivative is positive immediately because \(u(0)=a>0\); for any \(t_0>0\), \(y(t)\ge\delta>0\) for \(t\ge t_0\). If \(y_0>0\), the same bound follows from \(y(t)\ge\min(y_0,y_*)\). Therefore (2) gives \(\dot u\ge -\max(1,\kappa)u+a\delta\) eventually, so \(u(t)\) has a strictly positive lower bound. The exact identity
\[
y(t)-y_*=(y_0-y_*)\exp\!\left[-(\alpha+\beta\kappa^2)\int_0^t u(\tau)^2\,d\tau\right]
\]
then gives exponential decay of \(y-y_*\). The linearly forced first equation gives exponential convergence of \(u\) to
\[
u_*=\frac{a y_*}{\kappa+(1-\kappa)y_*}
=\frac{a\alpha}{\alpha+\beta\kappa^3}.
\]
This proves global attraction **within the precisely specified invariant manifold**, not in the ambient network.

**Exact Jacobian and transverse instability.** For two agents the equilibrium is \((u_*,-u_*,y_*,y_*)\). Set
\[
q:=\frac{\alpha+\beta\kappa^3}{\alpha+\beta\kappa^2},\quad
\eta:=(\alpha+\beta\kappa^2)u_*^2,\quad
d:=\frac{a\kappa}{q}.
\]
Use the linear coordinates \(\delta x=(p+m,-p+m)\) and \(\delta y=(z+h,z-h)\). Direct differentiation of (1) block-diagonalizes its Jacobian into the longitudinal block, acting on \((p,z)\), and transverse block, acting on \((m,h)\):
\[
J_{\parallel}=\begin{pmatrix}-q&d\\0&-\eta\end{pmatrix},\qquad
J_{\perp}=\begin{pmatrix}-y_*&d\\2\alpha(1-y_*)u_*&-\eta\end{pmatrix}.
\]
The longitudinal eigenvalues \(-q,-\eta\) are strictly negative. The transverse trace is \(-y_*-\eta<0\); its determinant simplifies, with no approximation, to
\[
\det J_{\perp}=
\frac{a^2\alpha^2(\alpha-2\beta\kappa^3)}
{(\alpha+\beta\kappa^3)^2}.
\]
A real two-by-two matrix with negative trace and positive determinant has both eigenvalues in the open left half-plane. Negative determinant instead yields exactly one positive and one negative real eigenvalue. This proves the sharp, amplitude-independent stability/saddle classification. At \(\alpha=2\beta\kappa^3\), the transverse determinant vanishes and exactly one zero eigenvalue occurs (the other three eigenvalues are negative), which proves linear degeneracy but not the nonlinear critical classification.

**A concrete instability despite on-mode convergence.** At \(a=\kappa=\alpha=\beta=1\), the fixed point is \((1/2,-1/2,1/2,1/2)\). Longitudinal eigenvalues are \(-1,-1/2\), and the transverse eigenvalues are \((-1\pm\sqrt2)/2\); one is positive, despite all solutions starting with exactly opposite opinions and equal leadership converging to this equilibrium.

## Verification

The self-contained source `verify.py` independently reconstructs both Jacobian blocks symbolically and checks the exact determinant and fixed-point identities, including a temporal resonance example. It additionally compares full and reduced solutions on 120 randomly constructed stochastic networks with an exact sign eigenvector, and checks two scalar trajectories numerically. Run `python verify.py` with SymPy, NumPy and SciPy. The finite computations are checks of formulas, not proofs of the infinite-parametric theorem. The analytic argument above supplies the proof.

## Relationship to prior work

The model, its fixed initial anchors and sufficient convergence results are from Alutto, Zino, Johansson and Fontan (2026). Its general stability results do not state the two-agent sharp all-perturbation threshold \(\alpha=2\beta\kappa^3\), nor this exact signed-mode attraction contrasted with transverse instability. Earlier leader--follower stochastic-network work studies prescribed or otherwise different leader mechanisms. A subsequent adaptive-stubbornness formulation employs a different leadership evolution equation, so its conclusions cannot be transferred without additional argument. Research-index and bibliographic comparisons found no identifiable covering statement; these checks cannot establish absolute uniqueness.

## Limitations

Only the invariant signed-eigenvector initialization is covered for general networks. The transverse stability theorem is for the two-agent matrix stated above; it is a local statement with fixed opinion anchors, not a basin or global-stability classification for arbitrary initial states. The equality case is nonhyperbolic and left open. The influence matrix need not be irreducible for the signed reduction, but the specified two-agent matrix has genuine cross-influence when \(\kappa>0\). The model is deterministic; no stochastic robustness is claimed. Literature not indexed or not accessible in full may contain related formulas.

## References

- Alutto, Zino, Johansson and Fontan, *A Co-evolving Opinion-Leadership Model*, arXiv:2603.24381 (first public March 25, 2026), https://arxiv.org/abs/2603.24381.
- Alutto and collaborators, *On Leadership Emergence in Opinion Dynamics on Social Networks*, arXiv:2606.05825 (2026), https://arxiv.org/abs/2606.05825 (different leadership update law; only accessible excerpt consulted).
- *Leader–follower consensus on activity-driven networks*, Proceedings of the Royal Society A (2020), https://doi.org/10.1098/rspa.2019.0485 (distinct stochastic leader--follower mechanism).
