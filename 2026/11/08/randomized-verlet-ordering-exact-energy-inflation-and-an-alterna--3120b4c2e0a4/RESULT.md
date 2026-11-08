# Randomized Verlet ordering: exact energy inflation and an alternating stability boundary

## Finding

For the unit harmonic oscillator \(\dot q=p\), \(\dot p=-q\), let \(0<h<2\). Independently at each step select with equal probabilities the position-Verlet step \(A_h=D_{h/2}K_hD_{h/2}\) or the velocity-Verlet step \(B_h=K_{h/2}D_hK_{h/2}\), where \(D_s(q,p)=(q+sp,p)\) and \(K_s(q,p)=(q,p-sq)\). If \(X_n=(q_n,p_n)^\mathsf T\) and \(H(X)=\|X\|_2^2/2\), then, for every deterministic initial state and every integer \(n\ge0\),

\[
\mathbb E H(X_n)=\left(1+\frac{h^6}{32}\right)^n H(X_0).
\]

Thus independent, balanced random choice of two individually bounded symplectic Verlet integrators causes exact exponential growth of expected physical energy for each nonzero initial state. The physical-time onset is sharp: whenever \(h\downarrow0\) and \(n(h)h^6\to\tau\in[0,\infty)\), the mean-energy ratio converges to \(e^{\tau/32}\). In particular, an order-one change requires physical horizon \(T=nh\) of order \(h^{-5}\).

The instability persists in the mean-square operator for *every* nondegenerate independent mixing probability \(0<p<1\), while either unmixed Verlet map has bounded powers for \(0<h<2\). An exactly alternating schedule, using \(A_hB_h\) repeatedly instead of independent random choice, has bounded powers precisely for \(0<h<\sqrt5-1\); at \(h=\sqrt5-1\) it has a nontrivial Jordan block and linearly growing trajectories, and for \(\sqrt5-1<h<2\) it has an exponentially growing direction. These assertions concern the linear unit-frequency oscillator, the indicated fixed stepsize and the Euclidean physical energy; no almost-sure growth exponent or nonlinear-oscillator assertion is made.

## Assumptions and scope

Set \(X=(q,p)^\mathsf T\in\mathbb R^2\) and physical Hamiltonian \(H(X)=(q^2+p^2)/2\). For \(s\in\mathbb R\), the drift and kick matrices are

\[
D_s=\begin{pmatrix}1&s\\0&1\end{pmatrix},\qquad K_s=\begin{pmatrix}1&0\\-s&1\end{pmatrix}.
\]

The two palindromic second-order maps are

\[
A_h=\begin{pmatrix}d&hc\\-h&d\end{pmatrix},\quad
B_h=\begin{pmatrix}d&h\\-hc&d\end{pmatrix},\quad
d=1-\frac{h^2}{2},\quad c=1-\frac{h^2}{4}.
\]

Both are real symplectic, with determinant one and trace \(2-h^2\). For the randomized scheme, choose the maps independently at each step, \(\Pr(M_j=A_h)=p\), \(\Pr(M_j=B_h)=1-p\), and put \(X_n=M_n\cdots M_1X_0\). The exact scalar energy law uses \(p=1/2\). We state mean-square operator instability for \(0<p<1\), not a uniform pointwise lower bound for every initial state. A separate deterministic experiment repeats the two-step product \(A_hB_h\), whose reversed order \(B_hA_h\) has identical trace and determinant.

## Proof

**Step 1: stability of each constituent.** Direct multiplication gives \(\det A_h=\det B_h=1\) and \(\operatorname{tr} A_h=\operatorname{tr} B_h=2-h^2\). For \(0<h<2\), these traces lie strictly between \(-2\) and \(2\), so each fixed matrix has distinct conjugate unit-modulus eigenvalues and is diagonalizable over \(\mathbb C\). Its integer powers are therefore bounded. This does not assert energy conservation in the original Euclidean norm.

**Step 2: the exact balanced random energy law.** Since the choice of \(M_{n+1}\) is independent of \(X_n\),

\[
\mathbb E[\|X_{n+1}\|_2^2\mid X_n]
=X_n^\mathsf T\frac{A_h^\mathsf TA_h+B_h^\mathsf TB_h}{2}X_n.
\]

The two matrices have opposite off-diagonal Gram entries \(\mp d h^3/4\) and opposite diagonal deviations. Explicitly,

\[
\frac{A_h^\mathsf TA_h+B_h^\mathsf TB_h}{2}
=\left[d^2+\frac{h^2}{2}(1+c^2)\right]I_2
=\left(1+\frac{h^6}{32}\right)I_2.
\]

The conditional identity holds for every value of \(X_n\). Taking expectations and iterating proves the formula for every integer \(n\ge0\), including \(n=0\). For \(n(h)h^6\to\tau\), the logarithmic energy ratio is \(n(h)\log(1+h^6/32)\to\tau/32\), proving the physical-time assertion. Note that \(T_h=n(h)h\), hence \(n(h)h^6=T_hh^5\).

**Step 3: every genuinely mixed independent law has a growing second-moment mode.** On the three-dimensional real space of symmetric \(2\times2\) matrices define the positive linear map

\[
\mathcal T_p(S)=pA_hSA_h^\mathsf T+(1-p)B_hSB_h^\mathsf T.
\]

Writing \(S=\begin{psmallmatrix}x&y\\y&z\end{psmallmatrix}\) gives the matrix \(T_p=pT(A_h)+(1-p)T(B_h)\), where, for any \(M=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\),

\[
T(M)=\begin{pmatrix}
a^2&2ab&b^2\\ac&ad+bc&bd\\c^2&2cd&d^2
\end{pmatrix}.
\]

Expanding this explicit determinant and factoring yields the exact identity

\[
\det(I_3-T_p)=-\frac{h^8p(1-p)(8-h^2)^2}{128}<0,
\qquad 0<h<2,\quad0<p<1.
\]

The real cubic polynomial \(\det(\lambda I_3-T_p)\) is negative at \(\lambda=1\) and positive for sufficiently large positive \(\lambda\), so \(T_p\) has a real eigenvalue strictly above one. Therefore its spectral radius is greater than one. Because \(\mathcal T_p\) preserves the cone of positive-semidefinite matrices, finite-dimensional Perron theory gives a nonzero positive-semidefinite eigenmatrix for its spectral radius. If the expected squared norms from both coordinate-vector initializations were bounded for all \(n\), then \(\operatorname{tr}\mathcal T_p^n(I_2)\) would be bounded, contradicting the growing trace of the positive-semidefinite eigenmatrix (which is bounded above by a multiple of \(I_2\)). Thus no nondegenerate independent mixing law is uniformly mean-square stable. This step does **not** imply that each realization, or each deterministic initial vector, grows exponentially almost surely.

**Step 4: an exact alternating-schedule phase transition.** The two-step propagator \(P_h=A_hB_h\) has \(\det P_h=1\) and

\[
\operatorname{tr}P_h=2-4h^2+h^4-\frac{h^6}{16}.
\]

The sign factors are

\[
\operatorname{tr}P_h-2=-\frac{h^2(h^2-8)^2}{16}<0,
\]

\[
\operatorname{tr}P_h+2=-\frac{(h^2-4)(h^2-2h-4)(h^2+2h-4)}{16}.
\]

On \(0<h<2\), the second expression is positive exactly for \(h<\sqrt5-1\), vanishes at \(h=\sqrt5-1\), and is negative above that threshold. In the first interval \(|\operatorname{tr}P_h|<2\), so all powers are bounded. At equality \(\operatorname{tr}P_h=-2\), \(\det P_h=1\), but \(P_h\ne-I_2\) because its upper-right entry \(h(1-h^2/2)(2-h^2/4)\) is nonzero there; the nontrivial Jordan block gives linearly growing trajectories. Above the threshold, \(\operatorname{tr}P_h<-2\), so \(P_h\) has one real eigenvalue of modulus greater than one and a corresponding exponentially growing direction. This proves the sharp alternating boundary.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to check both factor identities, both symplectic determinants, the balanced Gram identity, the three-dimensional second-moment determinant at an independent grid of rational steps and mixing probabilities, and the complete finite-path mean-energy identity by exhaustive enumeration for small step counts. It also checks the trace sign change on either side of \(\sqrt5-1\) by exact rational test points. Run `python3 verify.py` after extracting the package.

The proof above is analytic for all parameter values in the stated scope. Finite rational checks are supplemental and do not replace it.

## Relationship to prior work

Casas, Sanz-Serna and Shaw (arXiv:2210.07048, first public 13 October 2022) formulate the two Verlet orders and analyze deterministic splitting stability, with a principal theorem for rotation/kick Strang methods. Their studied semitrace and fixed-method stability regions do not state the stochastic ordered-pair law here, the exact mean-energy factor or the mixed-versus-alternating comparison.

Batcho and Schlick (J. Chem. Phys. 115, 4019–4029, 2001) compare fixed position- and velocity-Verlet fast inner cycles in two-component harmonic impulse integration, deriving resonant trace conditions and outer-step stability distinctions. They do not randomly or alternately select the two single-step maps on one unit oscillator; their matrix products involve a separate slow-force impulse and a fixed inner scheme.

Ni and Hu (arXiv:2407.18726, first public 26 July 2024) give explicit modified Hamiltonians for the two fixed Verlet orders on the harmonic oscillator, with different position and momentum coefficients, and relate their fixed-order trajectories. Those facts do not determine the energy distribution of independent order selection nor the exact stability boundary of repeated mixed products.

Lie, Stahn and Sullivan (arXiv:2103.16506, first public 30 March 2021) analyze additive random perturbations of one-step solvers for deterministic operator equations. Their stated update is an underlying deterministic map plus an additive perturbation, whereas this finding concerns random choice between two nonlinear-in-stepsize symplectic maps and uses physical energy over an unbounded horizon.

Closely related published research on randomized Lie ordering gives fixed-final-time error laws for first-order \(e^{hA}e^{hB}\) and \(e^{hB}e^{hA}\), not the present second-order Verlet fixed-step energy law. Published work on variable-step Verlet treats a fixed map order with random steps, not a fixed step with random order. Those nearby results motivated explicit comparison but do not logically imply the numerical constants or alternating boundary established here. Publication precedence for an equivalent old mixed-Verlet calculation remains unconfirmed.

## Limitations

The result is for one exact, linear unit-frequency oscillator with no forcing, damping, rounding or numerical noise, with the two indicated second-order maps. Mean-square instability does not imply divergence of typical trajectories; a positive Lyapunov exponent is not proved. The alternating analysis concerns a predetermined period-two pattern, not Markov-dependent or adaptively chosen orders. Finite exact checks do not establish originality. An older derivation of these identities in the geometric-integrator literature may exist.

## References

- P. F. Batcho and T. Schlick, *Special stability advantages of position-Verlet over velocity-Verlet in multiple-time step integration*, J. Chem. Phys. 115, 4019–4029 (2001), https://doi.org/10.1063/1.1389855.
- F. Casas, J. M. Sanz-Serna and L. Shaw, *A New Optimality Property of Strang's Splitting*, arXiv:2210.07048 (first submitted 2022-10-13), https://arxiv.org/abs/2210.07048.
- L. Ni and Z. Hu, *On the relation between the velocity- and position-Verlet integrators*, arXiv:2407.18726 (first submitted 2024-07-26), https://arxiv.org/abs/2407.18726.
- H. C. Lie, M. Stahn and T. J. Sullivan, *Randomised one-step time integration methods for deterministic operator differential equations*, arXiv:2103.16506 (first submitted 2021-03-30), https://arxiv.org/abs/2103.16506.
