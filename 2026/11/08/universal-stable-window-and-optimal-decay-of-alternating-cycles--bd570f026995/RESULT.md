# Universal stable window and optimal decay of alternating cycles in biregular Huygens networks

## Finding

**Theorem.** Let \(G=(A\sqcup B,E)\) be a finite connected simple unweighted bipartite graph with every vertex in \(A\) of degree \(r\geq1\) and every vertex in \(B\) of degree \(s\geq1\). Let \(L\) be its Laplacian and write its eigenvalues as \(0=\lambda_1<\lambda_2\le\cdots\le\lambda_N=\Lambda=r+s\). Consider the synchronous repulsive discrete Huygens map

\[
F_h(\theta)_i=\theta_i+h\sum_{j:\{i,j\}\in E}\sin(\theta_i-\theta_j)\pmod{2\pi},\quad h>0.
\]

For every \(h>2/\Lambda\), the equation \(\Lambda h=2a/\sin a\) has a unique solution \(a\in(0,\pi)\), and the two colour-constant configurations with relative colour phase \(\pi+a\) and \(\pi-a\) form a genuine primitive two-cycle. This branch is unique within the antipodal two-colour ansatz up to common rotation and time shift; no uniqueness among arbitrary network cycles is asserted. Its complete two-step multiplier spectrum is

\[
\mu_j(h)=\left(1-\frac{2a\cot a}{\Lambda}\lambda_j\right)^2,\qquad 1\le j\le N.
\]

The sole neutral rotational multiplier is \(\mu_1=1\). On the quotient by common phase the two-cycle is locally exponentially attracting precisely for \(2/\Lambda<h<\pi/\Lambda\), has **every** return multiplier equal to one at \(h=\pi/\Lambda\), and is a hyperbolic repeller for \(h>\pi/\Lambda\).

On the attracting interval the exact two-step transverse spectral radius is

\[
\rho(h)=\max\left\{\left(1-\frac{2a\cot a}{\Lambda}\lambda_2\right)^2,\ (1-2a\cot a)^2\right\}.
\]

Its unique minimizer is \(h_*=2a_*/(\Lambda\sin a_*)\), where \(a_*\in(0,\pi/2)\) uniquely solves \(2a_*\cot a_*=2\Lambda/(\Lambda+\lambda_2)\), and the minimum equals

\[
\boxed{\rho(h_*)=\left(\frac{\Lambda-\lambda_2}{\Lambda+\lambda_2}\right)^2.}
\]

For a fixed connected graph, both stability edges have sharp asymptotics:

\[
\rho(h)=1-4(\Lambda h-2)+O((\Lambda h-2)^2)\quad(h\downarrow 2/\Lambda),
\]
\[
\rho(h)=1-\frac{\pi\lambda_2}{\Lambda}(\pi-\Lambda h)+O((\pi-\Lambda h)^2)\quad(h\uparrow\pi/\Lambda).
\]

At the upper endpoint, on the **invariant two-colour manifold only**, let the scalar relative angle be \(u=\pi/2+x\) (after subtracting \(\pi\) from the colour difference). In two-step return time \(m\), every sufficiently small nonzero \(x_0\) obeys

\[
x_{m+1}=x_m-\frac{\pi^2}{2}x_m^3+O(x_m^4),\qquad \lim_{m\to\infty}m x_m^2=\pi^{-2}.
\]

## Assumptions and scope

The graph may be irregular across its two classes (stars and all complete bipartite graphs qualify), but degrees are constant within each class. Interaction weights equal one, phases are modulo \(2\pi\), updates are simultaneous, and the common frequency is removed by a co-rotating frame. The spectrum is the positive-semidefinite vertex Laplacian spectrum. Statements about attraction and repulsion are on the \((N-1)\)-dimensional quotient by common phase, not on the full torus where rotation is neutral. The theorem describes one explicit two-colour branch, not all periodic orbits or their global basins.

## Proof

**Invariant subsystem and orbit.** Every class-constant configuration remains so, since \(U'=U+hr\sin(U-V)\) and \(V'=V-hs\sin(U-V)\). Its relative angle \(u=U-V-\pi\) obeys the real lift \(u'=u-\alpha\sin u\), where \(\alpha=(r+s)h\). The symmetric two-cycle \(+a\mapsto-a\mapsto+a\) exists precisely when \(\alpha=2a/\sin a\). Strict positivity of \(\sin a-a\cos a\) on \((0,\pi)\) makes the latter ratio strictly increasing from two to infinity. The lifted full-phase increments at the first point are \(-hr\sin a\) and \(+hs\sin a\); at the second they have opposite signs, proving the **full lift** returns after two steps. Because \(0<a<\pi\), the first update is nontrivial, establishing primitive period two.

**Exact top Laplacian eigenvalue.** Bipartite sign conjugation transforms \(L=D-\mathcal A\) into the nonnegative signless Laplacian \(D+\mathcal A\). The positive vector whose value is \(r\) on \(A\) and \(s\) on \(B\) is an eigenvector of \(D+\mathcal A\) with eigenvalue \(r+s\). The matrix is irreducible by connectivity. Perron–Frobenius therefore proves \(\lambda_N=\Lambda=r+s\), simple. The zero eigenvalue is also simple and \(\lambda_2>0\).

**Return spectrum and stability.** Every edge difference at the two-cycle points equals \(\pi\pm a\) up to sign, so every edge cosine is \(-\cos a\). Direct differentiation gives the same Jacobian at both points, \(DF_h=I-h\cos a L\). The return derivative is \((I-h\cos a L)^2\), giving the complete multiplier spectrum. Write \(q(a)=2a\cot a\). Its derivative is \((\sin(2a)-2a)/\sin^2a<0\), so \(q\) decreases from two to zero on \((0,\pi/2)\), vanishes at \(\pi/2\), and is negative above. As \(0<\lambda_j/\Lambda\le1\) for every nonzero mode, the squared multipliers lie strictly below one for \(0<q<2\), all equal one when \(q=0\), and strictly above one for \(q<0\). Since \(a\mapsto2a/\sin a\) is increasing, this yields the sharp global parameter partition.

**Unique graph-optimal decay.** For \(t=h\cos a=q(a)/\Lambda\in(0,2/\Lambda)\), the function \(\lambda\mapsto(1-t\lambda)^2\) is convex. Its maximum on the set of nonzero graph eigenvalues therefore equals the larger value at the extreme eigenvalues \(\lambda_2\) and \(\Lambda\). Minimize the maximum of these two squared endpoint factors by balancing them with opposite signs: \(1-t_*\lambda_2=-(1-t_*\Lambda)\). This yields \(t_*=2/(\Lambda+\lambda_2)\) and \(\rho_*=[(\Lambda-\lambda_2)/(\Lambda+\lambda_2)]^2\). The permitted interval contains \(t_*\); since \(q(a)\) decreases strictly and \(h(a)\) increases strictly, the optimizer in \(h\) is unique, including for \(N=2\).

**Boundary laws.** As \(a\downarrow0\), Taylor expansion gives \(\alpha=2+a^2/3+O(a^4)\) and \(q=2-2a^2/3+O(a^4)=2-2(\alpha-2)+O((\alpha-2)^2)\). The simple top eigenvalue \(\Lambda\) dominates the transverse spectral radius near this edge, yielding \(\rho=1-4(\alpha-2)+O((\alpha-2)^2)\). As \(a\uparrow\pi/2\), let \(b=\pi/2-a\). Then \(\pi-\alpha=2b+O(b^2)\), \(q=\pi b+O(b^2)\), and the smallest positive eigenvalue \(\lambda_2\) dominates, giving \(\rho=1-(\pi\lambda_2/\Lambda)(\pi-\alpha)+O((\pi-\alpha)^2)\). Consequently the inverse logarithmic two-return relaxation time has asymptotic size \(\Lambda/[\pi\lambda_2(\pi-\Lambda h)]\).

**Parabolic return on the two-colour subsystem.** At \(\alpha=\pi\), write \(u=\pi/2+x\). The first update yields \(u'=-\pi/2+y\), where \(y=x+\pi(1-\cos x)\). The second update gives return displacement \(T(x)=y+\pi(\cos y-1)=x-\pi^2x^3/2+O(x^4)\). For sufficiently small \(x\ne0\), the scalar return preserves its sign and strictly reduces its absolute value. The orbit therefore tends to zero, with \(x_{m+1}^{-2}-x_m^{-2}=\pi^2+o(1)\), and averaging these increments gives \(m x_m^2\to\pi^{-2}\). The vanishing linear contraction in all ambient directions precludes inferring any transverse nonlinear attraction from this scalar argument.

## Verification

The supplied standalone file `check.py` uses Python 3 and NumPy. Executing `python check.py` produced `PASS 92 network, orbit, spectrum, optimum and edge checks`. It constructs stars and complete bipartite graphs, even cycles and hypercubes; checks genuine full-state two-step returns and Jacobian eigenvalues; tests exact spectral minimizers, the critical cubic coefficient, and both endpoint coefficients. These finite checks corroborate but do not prove the universal assertions.

For example, on the star \(K_{1,m}\) with \(m\ge2\), \(\Lambda=m+1\) and \(\lambda_2=1\), giving the exact minimum \(\rho_*=m^2/(m+2)^2\). On the \(d\)-cube with \(d\ge2\), \(\Lambda=2d\) and \(\lambda_2=2\), giving \(\rho_*=(d-1)^2/(d+1)^2\). These graph families do not reduce to the nearest-neighbour cycle case.

## Relationship to prior work

Buescu, D'Aniello and Oliveira (2026, arXiv:2610.10993v1) define this reciprocal discrete Huygens graph model and prove strict Lyapunov descent and exclusion of non-fixed periodic orbits for \(0<h<2/\lambda_{\max}\), with further Morse–Smale results on smaller step intervals. Buescu and Oliveira (2026, arXiv:2610.19953v1) analyze rings on their Lyapunov interval. The present family lies **beyond** that interval. Previous mathematical work has also established local onset of period-two motion on general weighted bipartite graphs and the entire exact branch for even nearest-neighbour cycles, including their optimal contraction. Neither that general local result nor its cycle specialization logically establishes global continuation, the exact graph-independent stability window, the algebraic-connectivity minimax formula and the upper-edge slowdown on **arbitrary connected biregular bipartite graphs**. The graph spectral method and local bifurcation mechanism themselves are not asserted as novel.

## Limitations

The statement does not classify every two-cycle or rule out other attractors, and does not prove any global basin of the displayed branch. Exponential stability means local stability on the common-phase quotient. At the fully neutral endpoint, the inverse-square-root law is proved only within the invariant two-colour subspace; the transverse nonlinear behaviour remains unproved. The graph hypothesis excludes non-biregular graphs and arbitrary weighted edges. Historical priority remains conditional on specialized earlier results not recovered by the searches.

## References

1. J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first publicly posted 2026-10-07, https://arxiv.org/html/2610.10993v1.
2. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, first publicly posted 2026-10-14, https://arxiv.org/abs/2610.19953.
3. J. Buescu, E. D'Aniello and H. M. Oliveira, *A Lyapunov function for a Synchronisation diffeomorphism of three clocks*, arXiv:2502.15371v1, https://arxiv.org/abs/2502.15371.
4. F. M. Atay and O. Karabacak, *Stability of Coupled Map Networks with Delays*, SIAM J. Appl. Dyn. Syst., DOI:10.1137/060652531 (2006), general graph-coupled-map stability context.
