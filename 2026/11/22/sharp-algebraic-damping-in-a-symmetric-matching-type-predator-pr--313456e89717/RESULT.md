# Sharp algebraic damping in a symmetric matching-type predator–prey system

## Finding
For the four-population, equal-within-species-competition, matching-type predator–prey flow described below, suppose its all-positive coexistence state is \((u,u,v,v)\), with \(u,v>0\). Define the type contrasts \(X=n_0-n_1\), \(Y=h_0-h_1\) and the elliptic contrast amplitude
\[
R(t)^2=X(t)^2+\frac{pu}{\rho v}Y(t)^2.
\]
Every strictly positive initial condition **other than** the exactly type-symmetric subspace \(X(0)=Y(0)=0\) obeys the sharp, initial-condition-independent asymptotic law
\[
\boxed{\lim_{t\to\infty}tR(t)^2=\frac{1}{2uD},\qquad
D=c|W_1|^2+\frac{p\gamma}{\rho}|W_2|^2>0,}
\]
where \(W\) is the explicitly computable two-dimensional complex vector defined below. Thus the type imbalance has an inverse-square-root rather than exponential decay envelope. On the exactly symmetric invariant subspace, relaxation of the two population totals is exponential.

For the admissible normalization \(u=v=c=\gamma=p=\rho=1\), \(b-d=3\), and \(\beta-\delta=1\), the law is particularly simple:
\[
\boxed{\lim_{t\to\infty}t\bigl[(n_0-n_1)^2+(h_0-h_1)^2\bigr]=\frac{260}{9}.}
\]

## Assumptions and scope
All rates \(c,\gamma,p,\rho\) are strictly positive. The net prey and predator growth rates are \(a=b-d\) and \(g=\beta-\delta\), with \(a>0\), and the deterministic continuous-time dynamics for \(i\in\{0,1\}\) are
\[
\dot n_i=n_i\bigl(a-c(n_0+n_1)-ph_i\bigr),\qquad
\dot h_i=h_i\bigl(g-\gamma(h_0+h_1)+\rho n_i\bigr).
\]
Assume the unique fully interior equilibrium exists, equivalently
\[
u:=\frac{2\gamma a-pg}{4c\gamma+p\rho}>0,
\qquad v:=\frac{\rho a+2cg}{4c\gamma+p\rho}>0.
\]
Equivalently \(a=2cu+pv\) and \(g=2\gamma v-\rho u\). Every initial abundance is strictly positive and independent of any stochastic population scaling. Time is the deterministic ecological time of these equations.

Define
\[
\omega=\sqrt{p\rho uv},\qquad
J=\begin{pmatrix}-2cu&-pu\\ \rho v&-2\gamma v\end{pmatrix},\qquad
F=\frac{\omega}{4u}\begin{pmatrix}-1\\\rho/p\end{pmatrix},\qquad
W=(2i\omega I-J)^{-1}F.
\]
The inverse exists because \(J\) is Hurwitz. This formula defines \(D\) without a choice of eigenvectors or phase convention.

## Proof
**1. Global convergence and exact dissipation.** Put \(A=n_0+n_1-2u\), \(B=h_0+h_1-2v\), \(X=n_0-n_1\), \(Y=h_0-h_1\). Direct expansion gives the exact four-equation system
\[
\begin{aligned}
\dot A&=-2cuA-puB-cA^2-\tfrac p2AB-\tfrac p2XY,\\
\dot B&=\rho vA-2\gamma vB-\gamma B^2+\tfrac\rho2 AB+\tfrac\rho2 XY,\\
\dot X&=-puY-cAX-\tfrac p2(AY+BX),\\
\dot Y&=\rho vX-\gamma BY+\tfrac\rho2(AY+BX).
\end{aligned}
\]
The nonnegative relative-entropy functional
\[
V=\sum_{i=0}^1\bigl[n_i-u-u\log(n_i/u)\bigr]
+\frac p\rho\sum_{i=0}^1\bigl[h_i-v-v\log(h_i/v)\bigr]
\]
has the **exact** derivative
\[
\dot V=-cA^2-\frac{p\gamma}{\rho}B^2.
\]
Its sublevel sets are compact inside the strictly positive orthant, so positive solutions are global and bounded away from zero and infinity. On \(A=B=0\), invariance requires \(XY=0\); whenever \((X,Y)\ne(0,0)\) with \(XY=0\), the equations for \(\dot X,\dot Y\) instantly leave that condition. Hence the largest invariant subset of \(\dot V=0\) is the equilibrium. LaSalle's principle yields convergence of all positive solutions to \((u,u,v,v)\). This convergence also appears in Proposition 2.4 of the originating paper and is not claimed as new.

**2. Stable and oscillatory directions.** The linearization splits into the Hurwitz block \(J\) acting on \((A,B)\), with trace \(-2cu-2\gamma v<0\) and determinant \(uv(4c\gamma+p\rho)>0\), and the semisimple center block
\[
\begin{pmatrix}0&-pu\\\rho v&0\end{pmatrix}
\]
acting on \((X,Y)\), with eigenvalues \(\pm i\omega\). The plane \(X=Y=0\) is invariant and is precisely the local strong-stable manifold; it is tangent to the entire stable spectral subspace. Every other positive orbit, once close to equilibrium, tracks a nonzero center-manifold orbit with exponentially small error.

**3. Forced second harmonic.** Introduce polar center coordinates \(X=R\cos\theta\), \(Y=\frac{\omega}{pu}R\sin\theta\). Along a smooth local center manifold, \(\dot R=O(R^3)\) and \(\dot\theta=\omega+O(R^2)\). The quadratic stable-coordinate invariance equation is
\[
\frac{d}{dt}\begin{pmatrix}A\\B\end{pmatrix}
=J\begin{pmatrix}A\\B\end{pmatrix}
+R^2F\sin(2\theta)+O(R^3).
\]
Its unique bounded periodic quadratic solution is
\[
\begin{pmatrix}A\\B\end{pmatrix}
=R^2\operatorname{Im}\bigl(W e^{2i\theta}\bigr)+O(R^3),
\quad W=(2i\omega I-J)^{-1}F.
\]
In particular, \(D>0\) because \(F\ne0\), the inverse is nonsingular, and both dissipation weights are positive.

**4. Sharp radial rate.** The entropy has the center-manifold expansion \(V=R^2/(4u)+O(R^4)\); there is no cubic correction by simultaneous type interchange symmetry. Let
\[
G(\theta)=c\bigl[\operatorname{Im}(W_1e^{2i\theta})\bigr]^2
+\frac{p\gamma}{\rho}\bigl[\operatorname{Im}(W_2e^{2i\theta})\bigr]^2.
\]
Then \(\dot V=-R^4G(\theta)+O(R^5)\), whence
\[
\frac{d}{dt}\frac1V=16u^2 G(\theta)+O(R).
\]
Since \(\dot\theta\to\omega>0\), the time-average of \(G(\theta(t))\) is its angular average \(D/2\). Because \(R\to0\), Cesàro averaging yields \((tV)^{-1}\to 8u^2D\), and thus \(tR^2\to1/(2uD)\). Exponential tracking transfers the same limit to every orbit outside the strong-stable plane.

**5. Exact normalization.** When all six positive coefficients and both equilibrium abundances equal one, \(J=\bigl(\begin{smallmatrix}-2&-1\\1&-2\end{smallmatrix}\bigr)\), \(\omega=1\), and
\[
W_1=-\frac{19}{260}+\frac{11i}{130},\qquad
W_2=\frac{17}{260}-\frac{3i}{130},\qquad D=\frac9{520}.
\]
Therefore \(1/(2uD)=260/9\), as asserted.

## Verification
The standalone `verify.py` uses exact symbolic algebra to independently check the relative-entropy derivative and the rational transfer coefficient. It also integrates three strictly positive examples for a long but **finite** ecological time (12,000 units), comparing the finite-time products with the predicted limits. Running `python verify.py` requires SymPy, NumPy, and SciPy. The asymptotic theorem relies on the analytic center-manifold, invariance and averaging arguments above; no finite integration is treated as an infinite-time proof.

## Relationship to prior work
Costa, Czuppon and Forien (2026), §2.2 and Appendix A.2, establish the four-type deterministic model, positive coexistence and its global attraction; their later discussion highlights the degeneracy of dissipation in the symmetric model. They do not give the type-contrast \(t^{-1/2}\) rate or its explicit universal coefficient. Costa, Hauzy, Loeuille and Méléard (2014/2015), §3, give global Lotka–Volterra stability criteria involving positive-definite prey competition, unlike the rank-one within-species competition here. General critical-Hopf ringdown mathematics does not determine the model-specific second-harmonic transfer constant \(D\). No stochastic post-accumulation convergence claim is made.

## Limitations
This is a theorem for the deterministic, symmetric, four-population ODE with strictly positive coexistence and strictly positive initial abundances. It does not give a uniform error bound over all initial data, a stochastic finite-population relaxation theorem, a mixing-time bound in the mutation-scaling limit, or the logarithmic phase correction. Exact type symmetry has exponential rather than algebraic relaxation. The calculation has not received an independent scientific audit; a targeted literature comparison is not an exhaustive priority guarantee.

## References
1. M. Costa, P. Czuppon, R. Forien, *Eco-evolutionary cycles in a matching type predator-prey interaction*, arXiv:2609.04834v1 (first public preprint 2026-09-04), https://arxiv.org/abs/2609.04834 . Relevant: §2.2, Proposition 2.4, Appendix A.2, §4.3, §6.
2. M. Costa, C. Hauzy, N. Loeuille, S. Méléard, *Stochastic eco-evolutionary model of a prey-predator community*, arXiv:1407.3069v1 (2014), https://arxiv.org/abs/1407.3069 . Relevant: §3, Assumption C.1 and stability hypotheses.
3. J. Carr, *Applications of Centre Manifold Theory*, Springer (1981), for standard smooth center-manifold and stable-foliation results.
