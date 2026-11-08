# Heterogeneous tumbling sharpens the exponential binding length of a jammed two-swimmer pair

## Finding

Two independently tumbling swimmers that attract through a linear potential and cannot cross have an exactly exponential stationary separation distribution away from their collision atom. At a fixed sum of individual tumbling rates, the exponential decay exponent is uniquely maximized when the rates are equal; it decreases strictly as the rates become more unequal. In the rare-flipper limit a sharp new threshold occurs at propulsion speed twice the attractive-force scale: the decay exponent stays positive below the threshold and collapses to zero at and above it, with distinct square-root and linear critical scalings.

More precisely, for all \(v>g>0\) and \(\gamma_1,\gamma_2>0\), define \(s=\gamma_1+\gamma_2\), \(p=\gamma_1\gamma_2\). The unique positive decay exponent \(\lambda\) solves
\[
\sqrt{\gamma_1^2+v^2\lambda^2}+\sqrt{\gamma_2^2+v^2\lambda^2}=s+2g\lambda.
\]
Equivalently it is the unique positive root of
\[
4g^2(v^2-g^2)\lambda^3+4gs(v^2-2g^2)\lambda^2+
\bigl[s^2(v^2-4g^2)-4g^2p\bigr]\lambda-4gsp=0.
\]
Fix \(s>0\). Then \(\lambda\) is strictly increasing with \(p\in(0,s^2/4]\), is bounded by \(sg/(v^2-g^2)\), and attains that bound exactly at equal tumbling rates. When \(\gamma_1\downarrow0\), \(\gamma_2=s-\gamma_1\),
\[
\lambda\longrightarrow
\begin{cases}
\dfrac{s(2g-v)}{2g(v-g)},&g<v<2g,\\
0,&v\ge2g.
\end{cases}
\]
Writing \(p=\gamma_1\gamma_2\downarrow0\), the sharp vanishing rates are
\[
\lambda\sim\frac{\sqrt{p}}{\sqrt{2}g}\quad(v=2g),\qquad
\lambda\sim\frac{4gp}{s(v^2-4g^2)}\quad(v>2g).
\]

## Assumptions and scope

Let \(X_1(t)\le X_2(t)\) denote positions on the infinite real line. Each particle has propulsion speed \(v>0\), and its heading \(\sigma_i(t)\in\{-1,+1\}\) flips independently at constant rate \(\gamma_i>0\). The attractive potential is \(g|X_2-X_1|\), with force magnitude \(g>0\) on each particle. There is no translational diffusion. At positive separation \(Y=X_2-X_1\), the velocity is \(\dot Y=v(\sigma_2-\sigma_1)-2g\). At contact \(Y=0\), negative separation velocities are reflected by a minimal continuous regulator, which implements noncrossing, sticky jamming. Assume \(v>g\), so the heading pair \((-1,+1)\) can separate. Conclusions concern the unique stationary joint law of \(Y\) and the heading pair, not the absolute center of mass.

## Proof

Order heading pairs as \((+,+),(+,-),(-,+),(-,-)\). Set \(Q\) to the four-state generator which flips the first or second sign at rates \(\gamma_1\) and \(\gamma_2\), respectively, and
\[
W=\operatorname{diag}(-2g,-2g-2v,-2g+2v,-2g).
\]
In stationarity the autonomous four-state phase chain has uniform marginals and mean separation drift \(-2g<0\). A stationary two-sided realization gives the reflected path as the finite almost-sure supremum of integrated past phase velocities; strict negative mean drift proves this supremum is finite and the stationary workload unique by coupling of reflected trajectories.

For an exponential interior density \(h e^{-\lambda y}\), stationarity requires \((Q^\top+\lambda W)h=0\). The top eigenvalue of this symmetric tilted matrix is
\[
\psi(\lambda)=-s-2g\lambda+
\sqrt{\gamma_1^2+v^2\lambda^2}+
\sqrt{\gamma_2^2+v^2\lambda^2}.
\]
It satisfies \(\psi(0)=0\), \(\psi'(0)=-2g<0\), strict convexity for positive arguments, and \(\psi(\lambda)\to+\infty\) as \(\lambda\to\infty\), because \(v>g\). Thus exactly one positive solution \(\lambda_*\) exists, and Perron--Frobenius yields its strictly positive eigenvector \(h\). A direct symbolic determinant identity is
\[
\det(Q^\top+zW)=-4z P_{s,p}(z),
\]
where \(P_{s,p}\) is the displayed cubic. Its coefficient signs have exactly one change when read from the leading coefficient to the negative constant, throughout \(v>g\), by splitting at \(v=\sqrt2 g\) and \(v=2g\). Descartes' rule confirms that the cubic has exactly one positive zero.

To construct the boundary atom, let \(O\) denote the single positive-velocity phase \((-1,+1)\) and \(U\) the other three phases. The subgenerator \(Q_{UU}\) is transient, so \((-Q_{UU}^\top)^{-1}\) has nonnegative entries. Define the unnormalized contact vector \(m\) by \(m_O=0\) and
\[
m_U=(-Q_{UU}^\top)^{-1}(-W_U h_U),
\]
which is strictly positive. The eigenvector equation, together with \(\sum_j W_{jj}h_j=0\), implies \(Q^\top m=Wh\), including in the outward phase. Consequently
\[
\pi(dy,j)=C h_j e^{-\lambda_* y}\mathbf1_{y>0}\,dy+C m_j\delta_0(dy),\qquad
C=\left(\frac{\sum_jh_j}{\lambda_*}+\sum_jm_j\right)^{-1}
\]
satisfies both the interior and reflection-boundary stationary generator identities. Existence and uniqueness above identify it as the invariant law. The separation marginal is therefore a single positive exponential plus a positive atom, with finite stationary mean for every positive pair of rates.

For fixed \(s\), the function \(x\mapsto\sqrt{x^2+v^2 z^2}\) is strictly convex when \(z>0\). Hence unequal pairs with larger \(|\gamma_1-\gamma_2|\) make \(\psi(z)\) strictly larger. Each convex curve crosses zero at its unique positive root, so that root is strictly smaller for the more unequal pair. In particular the balanced solution is \(\lambda_*=sg/(v^2-g^2)\), as follows by setting both rates to \(s/2\).

For \(\gamma_1\downarrow0\) and \(\gamma_2=s-\gamma_1\), continuity of \(\psi\) gives limiting root \(s(2g-v)/(2g(v-g))\) when \(g<v<2g\). When \(v\ge2g\), the only nonnegative limiting root is zero. At \(v=2g\), the leading balance in the cubic is \(8g^3s\lambda^2-4gsp=0\), giving \(\lambda\sim\sqrt{p}/(\sqrt2 g)\). When \(v>2g\), the leading balance is \(s^2(v^2-4g^2)\lambda-4gsp=0\), proving the stated linear asymptotic. This completes all quantified assertions.

## Verification

The independent `verify.py` uses exact symbolic determinant and equal-rate factorization identities, tests 55 parameter cases against Perron eigenvalues and boundary balance, and compares three stationary means and contact weights with event-time simulations. It uses Python, SymPy and NumPy and requires no network. Run `python3 verify.py` alongside this file. Numerical tests are supporting evidence; the arguments above prove the global statements.

## Relationship to prior work

Touzo and Le Doussal (2023, arXiv:2308.06118) study attractive active rank diffusion and its many-particle phase diagram, with the homogeneous two-particle literature as background. Le Doussal, Majumdar and Schehr (2021, arXiv:2105.11838) solve the original identical-tumbling, attractive, crossing-particle bound state. Hahn (2025, arXiv:2501.11379), the closest comparison, explicitly determines jammed, attractive pair steady states with a common flip rate; its instantaneous model compresses the two equal-rate headings into three phases. The present independent unequal rates require four phases and the strict balancing/rare-flipper conclusions are not stated in those inspected works. Hahn, Guillin and Michel (2023, arXiv:2306.00831) treat general jamming on a finite torus, rather than the attractive infinite-line model. The process can also be represented as a standard two-source Markov-modulated fluid queue, so general queueing matrix theory may imply formulas underlying this derivation; no novelty is asserted for that framework, the spectral method, or the equal-rate exponential.

## Limitations

The theorem assumes a hard contact constraint, no translational thermal diffusion, symmetric individual heading flips and a linear attractive potential. It does not cover different propulsion speeds, finite tumbling durations, or higher particle numbers. The singular zero-rate endpoint is a limit of strictly positive rates; no invariant law is asserted for an exactly frozen particle at that endpoint. Existing fluid-queue techniques may imply parts of the polynomial and stationary measure, and unindexed or inaccessible prior work may contain the balancing or critical-limit classification. No independent external scientific audit has been performed.

## References

- L. Touzo and P. Le Doussal, *Non-equilibrium phase transitions in active rank diffusions*, first public 2023-08-11, https://arxiv.org/abs/2308.06118 .
- P. Le Doussal, S. N. Majumdar and G. Schehr, *Stationary nonequilibrium bound state of a pair of run and tumble particles*, 2021, https://arxiv.org/abs/2105.11838 .
- L. Hahn, *Steady state and mixing of two run-and-tumble particles interacting through jamming and attractive forces*, 2025, https://arxiv.org/abs/2501.11379 .
- L. Hahn, A. Guillin and M. Michel, *Jamming pair of general run-and-tumble particles: Exact results, symmetries and steady-state universality classes*, 2023, https://arxiv.org/abs/2306.00831 .
- W. R. W. Scheinhardt, *Markov-modulated and feedback fluid queues*, thesis (1998), https://research.utwente.nl/en/publications/markov-modulated-and-feedback-fluid-queues/ .
