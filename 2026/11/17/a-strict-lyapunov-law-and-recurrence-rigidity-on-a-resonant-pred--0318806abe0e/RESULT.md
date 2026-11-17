# A strict Lyapunov law and recurrence rigidity on a resonant predator–prey equilibrium segment

## Finding
For the two-dimensional polynomial predator–prey map of Lee, Chan, Im, Chan and Cheang (Type 2), a two-parameter resonance supports a complete segment of strictly positive fixed points. On this resonance there is a **strict monomial Lyapunov function** throughout every positive orbit: no strictly positive nonconstant periodic orbit of any period, or nonfixed recurrent point, is possible. Moreover, every forward-positive trajectory either approaches the coordinate axes in the sense that its smaller population tends to zero, or converges to one point of the positive equilibrium segment. A nonempty, exactly characterized part of this segment attracts an open set of positive trajectories even when the prey growth parameter exceeds its scalar flip threshold.

## Assumptions and scope
Let \(m>1\) and \(d>0\), and define
\[
S=m-1,\qquad k=\frac{d+1}{m-1},\qquad a=\frac{d(m-1)}{d+1},\qquad b=\frac{m(d+1)}{m-1}.
\]
In particular \(a,b,k>0\), \(ak=d\), and \(b=mk\). Study the polynomial map \(F:(x,y)\mapsto (x',y')\) given by
\[
 x'=mx(1-x)-axy,\qquad y'=-dy(1-y)+bxy.
\]
It is the Type-2 discrete homomorphic Lotka–Volterra map with the positive parameters \((\mu_0,\mu_1,\nu_0,\nu_1)=(m,a,d,b)\). All recurrence and convergence claims concern **strictly positive forward orbits** \((x_n,y_n)\), for which both coordinates are positive at every finite iterate. The map is not asserted to preserve the whole positive quadrant.

Set \(H=mx+ay\), \(e=H-S\), and \(V(x,y)=x^k y\). The positive equilibrium set is exactly
\[
E^+=\{(x,y):x>0,\ y>0,\ mx+ay=S\}.
\]
For every globally positive forward orbit, \(V_n=V(x_n,y_n)\) decreases to a limit \(V_\infty\ge0\). Precisely one of the following holds:

1. \(V_\infty=0\), in which case \(\min\{x_n,y_n\}\to0\);
2. \(V_\infty>0\), in which case \((x_n,y_n)\to(x_\infty,y_\infty)\in E^+\).

Every positive periodic orbit is fixed, and every positive recurrent point is fixed. Along \(E^+\), the two eigenvalues of \(DF\) are \(1\) and
\[
\lambda(y)=2-m+(a+d)y.
\]
The sharp **normally contracting** portion \(|\lambda|<1\) is exactly
\[
\max\!\left\{0,\frac{m-3}{a+d}\right\}<y<\frac{m-1}{a+d},\qquad x=\frac{S-ay}{m}.
\]
Every point of this nonempty subsegment has a positive open neighborhood whose trajectories remain positive and converge to some equilibrium in \(E^+\). An interior transverse multiplier \(-1\) occurs when \(m>3\) at \(y=(m-3)/(a+d)\), but even there no positive nonconstant period-two orbit exists.

## Proof
**Exact rank-one reduction.** The chosen parameters give \(bx+dy=kH\). Hence
\[
x'=x(m-H)=x(1-e),\qquad y'=y(-d+kH)=y(1+ke).
\]
A positive step requires \(-1/k<e<1\). The weighted total satisfies the exact transverse identity
\[
 e'=e(1-mx+dy).
\]
All strictly positive fixed points satisfy \(e=0\), since \(x'=x\) forces \(e=0\). Conversely, the entire positive segment \(e=0\) is fixed; its endpoints on the coordinate axes are fixed as well.

**Strict Lyapunov inequality.** For every positive step,
\[
\frac{V(x',y')}{V(x,y)}=(1-e)^k(1+ke)\le1.
\]
Indeed, weighted AM–GM applied with weights \(k/(k+1)\) and \(1/(k+1)\) gives
\[
 (1-e)^{k/(k+1)}(1+ke)^{1/(k+1)}
 \le\frac{k(1-e)+(1+ke)}{k+1}=1.
\]
Equality holds exactly at \(e=0\). This proves strict decrease for every nonfixed positive step. A nonconstant periodic positive orbit would force its Lyapunov value to decrease and return to the original value, which is impossible. Likewise, positive forward recurrence of a nonfixed point is incompatible with the strict first-step decrease and continuity of \(V\).

**Global positive-orbit dichotomy.** If all iterates stay strictly positive, positivity of both multipliers forces \(d/k<H_n<m\). Thus \(0<x_n<1\) and \(0<y_n<m/a\), so the orbit is bounded. The nonincreasing values \(V_n\) converge. If \(V_\infty=0\), boundedness and \(V_n=x_n^k y_n\to0\) imply \(\min\{x_n,y_n\}\to0\). If \(V_\infty>0\), then \(y_n\ge V_\infty\) and \(x_n\ge(aV_\infty/m)^{1/k}\). Therefore the orbit lies in a compact subset of the positive quadrant.

Since the loss factor \((1-e)^k(1+ke)\) is continuous and strictly less than one for \(e\ne0\), the convergence \(V_n\to V_\infty>0\) on this compact set forces \(e_n\to0\). Hence every accumulation point lies in \(E^+\). The exact map form gives \((x_{n+1},y_{n+1})-(x_n,y_n)=e_n(-x_n,ky_n)\to(0,0)\). The level set \(V=V_\infty\) intersects \(E^+\) in at most two points: after eliminating \(y=(S-mx)/a\), the function \(x^k(S-mx)/a\) is strictly increasing up to its unique maximum and strictly decreasing thereafter. A bounded sequence with vanishing successive increments cannot have a finite disconnected set of distinct accumulation points (every transition would produce further accumulation points). Its accumulation set here is therefore one point, proving convergence to a positive equilibrium.

**Sharp normal interval and local attraction.** At \(q=(x,y)\in E^+\), direct differentiation gives
\[
DF(q)=\begin{pmatrix}1-mx&-ax\\by&1+dy\end{pmatrix}.
\]
Its eigenvalues are \(1\) (tangent to \(E^+\)) and \(1-mx+dy=2-m+(a+d)y\) (transverse). Solving \(-1<\lambda(y)<1\) on the open equilibrium segment yields exactly the stated bounds, a nonempty interval for every \(m>1,d>0\). For a fixed point in that interval, choose a sufficiently small positive neighborhood where \(|1-mx+dy|\le\rho<1\). The identity for \(e'\) implies geometric contraction of \(|e_n|\) as long as the orbit remains there, while the increments of \(x_n,y_n\) are bounded by a constant times \(|e_n|\). Choosing the initial point close enough makes their sum smaller than the neighborhood margin, proving forward invariance of a smaller open neighborhood, positivity, and convergence to \(E^+\). The interval is sharp as a strict linear normal-contraction condition; no claim is made about nonlinear dynamics at its endpoints.

## Verification
The supplied `checker.py` verifies parameter identities, the exact transverse recurrence, the monomial ratio and the Jacobian factorization symbolically. For the rational instance \((m,d,a,b,k)=(2,1,1/2,4,2)\), it also verifies the strictly contracting point \((x,y)=(2/5,2/5)\), with transverse multiplier \(3/5\), and the one-step capture \((3/5,1/5)\mapsto(21/50,8/25)\) onto the equilibrium line. In this instance the strict Lyapunov inequality is certified by
\[
1-(1-e)^2(1+2e)=e^2(3-2e)>0
\]
for \(-1/2<e<1\) and \(e\ne0\). Exact checks supplement, but do not replace, the general analytic proof.

## Relationship to prior work
The map is Equation (20), Type 2, in Lee, Chan, Im, Chan and Cheang (arXiv:2301.11669, initial public posting 2023-01-27), whose analysis emphasizes equilibrium multipliers and numerical bifurcations. The present theorem addresses the resonant parameter intersection \(a=d(m-1)/(d+1)\), \(b=m(d+1)/(m-1)\), and establishes a strict global Lyapunov law, exclusion of every positive nonconstant periodic orbit, and a positive-orbit convergence dichotomy. Kon's 2023 paper examines perturbations of a fixed-point segment in a **different Ricker competition model**, and Baigent et al. study convergence for a planar exponential Ricker map. Neither accessible statement directly covers the polynomial Type-2 resonance; see the review for detailed access limitations.

## Limitations
The conclusion is conditional on forward positivity; a general initial condition in the positive quadrant can leave it. The boundary alternative describes the smaller population, not a complete classification of coordinate-wise boundary orbits. Individual equilibria on the segment are not asymptotically stable as isolated points because of the tangential eigenvalue \(1\). The theorem does not characterize the nonlinear behavior exactly at the normal-neutral endpoints or claim that the Lyapunov function is conserved. A related 2023 paper on invariant-curve persistence was available only in abstract form, so equivalent uninspected results remain a publication-priority risk.

## References
1. Wei Shan Lee, Hou Fai Chan, Ka Ian Im, Kuan Ieong Chan, and U Hin Cheang, *Predator Extinction arose from Chaos of the Prey: the Chaotic Behavior of a Homomorphic Two-Dimensional Logistic Map in the Form of Lotka-Volterra Equations*, arXiv:2301.11669 (first submitted 2023-01-27), https://arxiv.org/abs/2301.11669 .
2. Ryusuke Kon, *Invariant curves in a discrete-time two-species system*, Journal of Difference Equations and Applications 30 (2024), 1711–1726; published online 2023-11-09, https://doi.org/10.1080/10236198.2023.2279632 .
3. Stephen Baigent, Zhanyuan Hou, Saber Elaydi, E. C. Balreira, and Rafael Luís, *A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds*, Journal of Difference Equations and Applications 29 (2023), 575–591, https://doi.org/10.1080/10236198.2023.2222855 .
4. Jiying Ma and Mingxia Duan, *Codimension-two bifurcations of a two-dimensional discrete time Lotka-Volterra predator-prey model*, Discrete and Continuous Dynamical Systems B 29 (2024), 1217–1242, https://doi.org/10.3934/dcdsb.2023131 .
