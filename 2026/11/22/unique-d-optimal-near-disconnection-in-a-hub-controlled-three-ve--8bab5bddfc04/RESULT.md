# Unique D-optimal near-disconnection in a hub-controlled three-vertex diffusion network

## Finding

Consider the continuous-time, scalar-hub-controlled system \(\dot z=-(\mu I+L)z+e_0 a(t)\) on the three-vertex star, with \(\mu>0\), positive edge conductances \(u,v\), and fixed conductance budget \(u+v=S>0\). Set \(\tau=\mu/S\). Its infinite-horizon controllability Gramian is \(G=\int_0^\infty e^{-(\mu I+L)t}e_0e_0^{\mathsf T}e^{-(\mu I+L)t}\,dt\). Maximizing \(\det G\) among all admissible conductances has **exactly two labelled optimal designs**, related by interchanging the leaves: 

\[
\{u_*,v_*\}=\left\{\frac S2\bigl(1+\sqrt{1-4x_*(\tau)}\bigr),\ \frac S2\bigl(1-\sqrt{1-4x_*(\tau)}\bigr)\right\},
\]
where \(x_*(\tau)\) is the **unique positive root** of
\[
(108\tau^2+120\tau+9)x^2+12\tau(\tau+1)(4\tau^2+8\tau-1)x-8\tau^2(\tau+1)(\tau+2)=0.
\]
In every case \(0<x_*(\tau)<1/6\), so the optimal conductances are unequal. The optimal normalized product \(x_*(\tau)=u_*v_*/S^2\) increases strictly with the damping ratio, tending from zero to \(1/6\). More precisely, with \(c=2(1+\sqrt5)/3\),
\[
x_*(\tau)=c\tau+O(\tau^2)\ (\tau\downarrow0),\qquad
x_*(\tau)=\frac16-\frac{1}{48\tau^2}+O(\tau^{-3})\ (\tau\to\infty).
\]
Thus the **weak optimal spoke** has conductance \(\min(u_*,v_*)=c\mu+O(\mu^2/S)\) as \(\mu\downarrow0\). The maximal Gramian determinant obeys the sharp asymptotic
\[
\max\det G\ \sim\ \frac{5\sqrt5-11}{1152\,\mu^2 S}\qquad(\mu/S\downarrow0).
\]
For any *fixed* unequal, positive conductances, however, \(\det G\) grows only on the order of \(\mu^{-1}\) as \(\mu\downarrow0\). The optimum therefore uses an asymptotically vanishing—but still positive—edge to exploit slow-mode controllability while preserving full rank.

## Assumptions and scope

The vertex set is \(\{0,1,2\}\), with vertex \(0\) the hub and no edge between leaves. The **combinatorial weighted Laplacian** is
\[
L=\begin{pmatrix}u+v&-u&-v\\-u&u&0\\-v&0&v\end{pmatrix}.
\]
The input acts only at the hub and has no cost-weight scaling; the stable dynamics matrix is \(-A\), where \(A=\mu I+L\). The full three-dimensional state and both positive spokes are included, with a fixed *sum* of unpriced conductances \(S>0\). The infinite-horizon Gramian is the unique positive-semidefinite solution of \(AG+GA=e_0e_0^{\mathsf T}\). Its determinant is the squared reachable-ellipsoid volume up to a dimension-dependent constant; it is not the smallest eigenvalue or trace of the inverse. For equal spokes the hub-only input is not controllable, so the determinant is zero.

## Proof

**Exact Gramian determinant.** Write \(p=uv\), \(S=u+v\). The three eigenvalues of \(A\) are \(\alpha_0=\mu\) and \(\alpha_\pm=\mu+S\pm\sqrt{S^2-3p}\), which are positive and distinct for \(u,v>0\). The Kalman matrix \(K=[e_0,Ae_0,A^2e_0]\) has \(\det K=uv(v-u)\), up to its sign convention. If \(A=U\operatorname{diag}(\alpha_i)U^{\mathsf T}\) and \(c_i=(U^{\mathsf T}e_0)_i\), then in modal coordinates \(G_{ij}=c_ic_j/(\alpha_i+\alpha_j)\). The Cauchy determinant identity and the Vandermonde factor from \(K\) cancel the spectral differences and give the exact formula
\[
\det G=\frac{(\det K)^2}{\prod_{i,j}(\alpha_i+\alpha_j)}
=\frac{p^2(S^2-4p)}{32\mu(\mu+S)^2(4\mu^2+4\mu S+3p)^2(\mu^2+2\mu S+3p)}.\tag{1}
\]
The formula extends continuously through \(u=v\), where both sides vanish. The denominator is strictly positive for all admissible parameters.

**Global and unique optimum.** The feasible product is \(0<p\le S^2/4\), and both boundary values \(p=0\) (the closure) and \(p=S^2/4\) give zero determinant. Put \(x=p/S^2\) and \(\tau=\mu/S\). The variable-dependent factor in (1) is
\[
F_\tau(x)=\frac{x^2(1-4x)}{(4\tau^2+4\tau+3x)^2(\tau^2+2\tau+3x)},\qquad 0<x<\frac14.
\]
Its logarithmic derivative is
\[
 g_\tau(x)=\frac2x-\frac4{1-4x}-\frac6{4\tau^2+4\tau+3x}-\frac3{\tau^2+2\tau+3x}
=-\frac{Q_\tau(x)}{x(1-4x)(4\tau^2+4\tau+3x)(\tau^2+2\tau+3x)},
\]
where \(Q_\tau(x)\) is the quadratic stated in the finding. Its quadratic coefficient is positive and its constant coefficient is strictly negative, hence its two real roots have opposite signs. Consequently the unique positive root \(x_*(\tau)\) is the unique stationary point; \(F_\tau\) increases before it and decreases afterward. Moreover,
\[
Q_\tau(1/6)=(12\tau^2+16\tau+3)/12>0,
\]
so \(x_*(\tau)<1/6\). The map \(\{u,v\}\mapsto p=uv\) is one-to-one on unordered positive pairs of given sum. Therefore the unordered conductance pair is the sole optimum, and its two labelled permutations are the only maximizers. No zero-weight or equal-weight limiting design maximizes the strictly positive objective.

**Strict monotonicity and limits.** For fixed \(0<x<1/4\), differentiating the logarithmic derivative in damping gives
\[
\partial_\tau g_\tau(x)=\frac{6(8\tau+4)}{(4\tau^2+4\tau+3x)^2}+\frac{3(2\tau+2)}{(\tau^2+2\tau+3x)^2}>0.
\]
Since for every \(\tau\) the function \(g_\tau\) is positive below its single zero and negative above it, increasing \(\tau\) strictly moves that zero rightward. The quadratic equation, after setting \(x=c\tau+O(\tau^2)\) and comparing the first nonzero powers, yields \(9c^2-12c-16=0\), whose positive root is \(c=2(1+\sqrt5)/3\). Comparing the leading and next terms as \(\tau\to\infty\) yields \(x=1/6-1/(48\tau^2)+O(\tau^{-3})\). Each expansion follows from a simple nonzero derivative of the respective rescaled polynomial at its limiting positive root; thus they describe the unique global optimum rather than just a formal candidate. Since \(uv=S^2x\) and the weaker root of \(z(S-z)=p\) is \(z=(S-\sqrt{S^2-4p})/2\), the weak-spoke expansion follows.

Substituting \(p\sim c\mu S\) into (1) yields
\[
\det G\sim\frac{c^2}{32(4+3c)^2(2+3c)}\frac1{\mu^2 S}
=\frac{5\sqrt5-11}{1152}\frac1{\mu^2 S}.
\]
For fixed \(p\in(0,S^2/4)\), equation (1) instead gives \(\det G\sim (S^2-4p)/(864\mu S^2p)\), showing the strict contrast in scaling. This establishes every stated asymptotic and boundary.

## Verification

Run `python verify.py` with Python and SymPy. The script solves the Lyapunov equation symbolically, checks the determinant in (1), the Kalman minor, the quadratic stationary equation and root signs, both asymptotic constants, and six numerical roots for distinct damping ratios. Its exact algebraic assertions returned `EXACT_CONTROL_GRAMIAN_OK`. The proof for **all** positive parameters is the spectral-Cauchy and quadratic sign argument above, not the finite numerical tests; the symbolic identities are checked with exact algebra.

## Relationship to prior work

Pasqualetti, Zampieri and Bullo (2013), arXiv:1308.1201, analyze quantitative network controllability, energy lower bounds, and actuator selection. Their complete openly accessible HTML paper, including model, theorem sections, and appendices, does not state the exact three-vertex fixed-edge-budget D-optimal classification given here. Cortesi, Summers and Lygeros (2014), arXiv:1403.6351, establish submodularity of Gramian-based objectives when **selecting actuators** for a fixed system; this is not optimization of two continuous conductances with an actuator fixed at the hub. A closely related public graph-star record derives **sensor-location rankings** for given conductances and a finite observation horizon, not the optimization of the conductance ratio for an infinite-horizon controlled, damped system. Becker et al. (arXiv:1902.04195, 2019) consider edge-weight design for a given admissible polytope, but target bounds on the smallest Gramian eigenvalue and on inverse-Gramian trace rather than this analytic log-volume optimum. These broader frameworks motivate but do not imply the displayed quadratic optimum; overlap under different aliases remains a publication-priority risk.

## Limitations

The result concerns just three vertices, a single hub input, positive undirected conductances, fixed total edge budget, positive scalar leakage, and the infinite-horizon **determinant** metric. It does not assert an optimal allocation for arbitrary stars, finite-time Gramians, other actuator locations, nonlinear dynamics, finite energy input constraints, or minimax controllability. At \(\mu=0\) the Gramian integral diverges, so the singular limit is an asymptotic statement and not a feasible unshifted optimization problem. The strict weak-edge behavior is a consequence of this volume objective; a vanishing edge may be undesirable under robustness or mixing criteria. Possible unindexed equivalent work remains to be reviewed; independent validation has not occurred.

## References

- F. Pasqualetti, S. Zampieri and F. Bullo, *Controllability Metrics, Limitations and Algorithms for Complex Networks*, arXiv:1308.1201, first submitted 2013-08-06. https://arxiv.org/html/1308.1201v3 .
- F. L. Cortesi, T. H. Summers and J. Lygeros, *Submodularity of Energy Related Controllability Metrics*, arXiv:1403.6351, first submitted 2014-03-25. https://arxiv.org/html/1403.6351v1 .
- C. O. Becker, S. Pequito, G. J. Pappas and V. M. Preciado, *Network Design for Controllability Metrics*, arXiv:1902.04195, first submitted 2019-02-12. https://arxiv.org/abs/1902.04195 .
- *A complete D-optimal single-sensor classification on weighted diffusion stars*, public mathematical research record, 2026-10-13. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-complete-d-optimal-single-sensor-classification-on-weighted-di--860ca1cdc9c7 .
