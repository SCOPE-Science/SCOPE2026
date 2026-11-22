# A sharp global feedback threshold and critical relaxation in a two-state adaptive Markov system

## Finding

Consider a two-state adaptive transfer system with one-step mixing. For \(0<c<1/2\), \(k>0\), \(a=kc\in(0,1)\), and learning step \(\delta>0\), define
\[
x_{n+1}=\tfrac12+c\tanh(\theta_n),\qquad
\theta_{n+1}=(1-\delta)\theta_n+\delta k(x_n-\tfrac12).
\]
All solutions from \(x_0\in[0,1]\), \(\theta_0\in\mathbb R\) converge to the unique equilibrium \((1/2,0)\) **if and only if**
\[
0<\delta\le\delta_c:=\frac{2}{1+a}.
\]
At the endpoint, trajectories with \(\theta_0\) and \(-\theta_1\) strictly of the same sign have the universal decay
\[
\lim_{n\to\infty}n\theta_n^2=\frac{3(1+3a)}{4a}.
\]
For each \(\delta_c<\delta<2\), there is a locally attracting primitive two-cycle, with controller amplitude given by the unique positive solution of
\[
(2-\delta)r=\delta a\tanh r.
\]
Its basin contains open subsets of the physical probability--controller state space.

## Assumptions and scope

For each fixed controller \(\theta\), let \(P_\theta\) be the Markov kernel on \(\{0,1\}\) whose two rows equal \((1-p(\theta),p(\theta))\), where \(p(\theta)=1/2+c\tanh\theta\). Thus a distribution with mass \(x\) on state one is mapped to mass \(p(\theta)\), independent of \(x\). Every frozen kernel has a unique invariant distribution and annihilates zero-mass perturbations in one step. The frozen loss is
\[
\ell(\theta,i)=\tfrac12\theta^2-k\theta(i-\tfrac12),\quad i\in\{0,1\}.
\]
Its average derivative is \(G(x,\theta)=\theta-k(x-1/2)\); each frozen loss is uniformly strongly convex, with scalar Hessian one. The reduced stationary gradient is \(\overline G(\theta)=\theta-a\tanh\theta\), which has derivative at least \(1-a>0\). Therefore the adaptive equilibrium is unique. No claim concerns sampled finite-particle noise, arbitrary non-Markovian kernels, or all possible period-two orbits beyond the exhibited symmetry class.

## Proof

**Exact second-order reduction.** From the probability update, for every \(n\ge1\),
\[
\theta_{n+1}=(1-\delta)\theta_n+\delta a\tanh\theta_{n-1}.\tag{1}
\]
For \(0<\delta\le1\), the coefficients \(1-\delta\), \(\delta a\) are nonnegative with sum \(1-\delta(1-a)<1\). Hence the maximal modulus of two consecutive terms contracts at least once every two steps, proving convergence.

For \(\delta>1\), write \(y_n=(-1)^n\theta_n\). Oddness of \(\tanh\) turns (1) into the cooperative recurrence
\[
y_{n+1}=u y_n+b\tanh y_{n-1},\qquad
u=\delta-1>0,\quad b=\delta a>0.\tag{2}
\]
If \(\delta<\delta_c\), then \(u+b=\delta(1+a)-1<1\). The two-step maximum-modulus contraction proves global convergence. If \(\delta=\delta_c\), then \(u+b=1\). The sliding maximum of \(|y_n|\), \(|y_{n-1}|\) is nonincreasing, hence bounded. Let \(L=\limsup |y_n|\). Equation (2) and \(|\tanh t|\le\tanh|t|\) yield \(L\le uL+b\tanh L\). Since \(b>0\) and \(\tanh L<L\) for \(L>0\), necessarily \(L=0\).

**Supercritical attracting flip.** Suppose \(\delta_c<\delta<2\). Then \(0<u<1\), \(u+b>1\). The function \(\tanh r/r\) decreases strictly from one to zero on \((0,\infty)\), so equation \((1-u)r=b\tanh r\) has exactly one positive root \(r\). Recurrence (2) has the positive fixed solution \(y_n=r\), corresponding to a genuine alternating controller orbit, with \(x_n=1/2-c(-1)^n\tanh r\). The Jacobian of the physical map at either orbit point is
\[
J=\begin{pmatrix}0&c\operatorname{sech}^2r\\\delta k&1-\delta\end{pmatrix}.
\]
The negative root of its characteristic polynomial is greater than \(-1\), because the defining equation and strict inequality \(\operatorname{sech}^2 r<\tanh r/r\) imply \(\delta a\operatorname{sech}^2r<2-\delta\). The positive root is less than one, since \(a\operatorname{sech}^2r<1\). Thus both eigenvalues lie strictly inside the unit circle, and the cycle is locally attracting. Alternatively, if \(y_0,y_1>0\), positivity of (2) persists; comparison with its unique positive fixed point bounds the orbit away from zero and infinity. For \(m=\liminf y_n\), \(M=\limsup y_n\), continuity gives \(m\ge u m+b\tanh m\) and \(M\le u M+b\tanh M\). The sign of \(u t+b\tanh t-t\) on either side of \(r\) forces \(m\ge r\ge M\). Hence every orbit of this cone converges to \(r\). The negative cone behaves symmetrically. These cones contain physical initial conditions, for example \(\theta_0>0\), \(x_0=1/2\), for which \(\theta_1=(1-\delta)\theta_0<0\).

If \(\delta\ge2\), the same initial condition yields \(y_0,y_1>0\) and \(u\ge1\), so (2) implies \(y_{n+1}>y_n\); the orbit cannot converge to zero. This proves the global threshold is necessary for all larger steps.

**Exact endpoint rate.** At \(\delta=\delta_c\), put \(u=(1-a)/(1+a)\), \(b=2a/(1+a)\), so \(0<u,b<1\), \(u+b=1\). Assume \(y_0,y_1>0\). Then each \(y_n>0\) and the preceding argument proves \(y_n\to0\). For \(q_n=y_n/y_{n-1}\),
\[
q_{n+1}=u+\frac b{q_n}\frac{\tanh y_{n-1}}{y_{n-1}}.
\]
Eventually \(q_n\) lies in the compact interval \([u,u+b/u]\). It is an asymptotically vanishing perturbation of the map \(q\mapsto u+b/q\). The twofold iterate of that map has derivative \(b^2/(u q+b)^2<1\) uniformly on this interval, and its only positive fixed point is one. The elementary two-step contraction-with-vanishing-errors argument therefore yields \(q_n\to1\). Set \(w_n=y_n+b y_{n-1}\). Equation (2) gives the exact identity
\[
w_n-w_{n+1}=b(y_{n-1}-\tanh y_{n-1}).
\]
Since \(w_n/y_n\to1+b\) and \(t-\tanh t\sim t^3/3\), it follows that
\[
\lim_{n\to\infty}(w_{n+1}^{-2}-w_n^{-2})=\frac{2b}{3(1+b)^3}.
\]
Cesàro summation gives \(n w_n^2\to3(1+b)^3/(2b)\), hence \(n\theta_n^2=n y_n^2\to3(1+b)/(2b)=3(1+3a)/(4a)\). The negative cone follows by odd symmetry. This proves the stated rate without an assumption of monotonicity of individual iterates.

## Verification

The standalone Python file `checker.py` implements the exact physical two-coordinate map, compares it against (1), checks the supercritical root and strict Jacobian stability inequality, and tests convergence and the critical asymptotic for three feedback strengths. It executed successfully with 119,988 recurrence comparisons. Numerical iteration is a consistency check, not a proof of the asymptotic or universal statements.

## Relationship to prior work

Galatolo and Lippi formulate adaptive self-consistent transfer operators, prove small-step local convergence, and discuss loss of stability and observed period-two saturation (arXiv:2611.15649v1, Sections 5 and 8.3.3). The present deliberately elementary two-state model supplies an exact global step frontier, a rigorous attracting flip cycle and a universal endpoint constant. Bento--Oliveira--Silva (arXiv:2211.04853) and Oliveira--Teixeira (arXiv:2502.11016) give broader delayed-difference-equation *attractivity criteria*; the latter may subsume the endpoint convergence component, which is not asserted as an independently new fact. Hong--Ma (2019) likewise gives broad M-matrix global-attractivity criteria. The asserted contribution is the combined exact Markov-control feedback phase transition and quantified endpoint critical law, not the underlying maximum comparison argument.

## Limitations

The plant is a deliberately solvable, rank-one two-state Markov refresh family. The result is deterministic at the probability-law level, not a finite-sample stochastic convergence theorem. The critical constant is proved for explicitly stated alternating-sign sectors, not all initial conditions. Historical work on exact bifurcations in related delayed hyperbolic-tangent recurrences may cover parts of this result; priority requires external specialist review. Independent verification has not been performed.

## References

1. S. Galatolo and V. Lippi, *Autonomous Neural Adaptive Control as a Self-Consistent Transfer Operator*, arXiv:2611.15649v1 (11 November 2026), https://arxiv.org/html/2611.15649v1.
2. A. J. G. Bento, J. J. Oliveira, C. M. Silva, *Existence and stability of a periodic solution of a general difference equation with applications to neural networks with a delay in the leakage terms*, arXiv:2211.04853, https://arxiv.org/abs/2211.04853.
3. J. J. Oliveira and A. S. Teixeira, *Global attractivity criteria for a discrete-time Hopfield neural network model with unbounded delays via singular M-matrices*, arXiv:2502.11016, https://arxiv.org/abs/2502.11016.
4. Y. Hong and W. Ma, *Sufficient and necessary conditions for global attractivity and stability of a class of discrete Hopfield-type neural networks with time delays*, Mathematical Biosciences and Engineering 16 (2019), 4936--4946, https://doi.org/10.3934/mbe.2019249.
