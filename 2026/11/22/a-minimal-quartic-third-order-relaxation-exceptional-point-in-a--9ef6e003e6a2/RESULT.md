# A minimal quartic third-order relaxation exceptional point in a harmonically trapped active Brownian particle

## Finding

At equality of the trap and angular relaxation rates, the fourth moment of one Cartesian position coordinate of a harmonically trapped active Brownian particle is the lowest positional moment displaying a quadratic-in-time relaxation term. The finite nine-dimensional polynomial–Fourier sector used for this moment has a single size-three Jordan block at eigenvalue \(-4\kappa\). The conditional expectation of \(X_t^4\) contains the term
\[
\frac{v^4}{2\kappa^2}t^2e^{-4\kappa t}\cos(2\Theta_0).
\]
Here *contains* identifies the coefficient of one term in an exact finite exponential-polynomial expansion as a function of the initial state; it does not mean the coefficient remains nonzero at every initial angle. The coefficient multiplying \(\cos(2\Theta_0)\) is independent of the translational diffusivity.

## Assumptions and scope

For \(\kappa,v,D_r>0\) and \(D\ge0\), let independent standard Brownian motions \(W,B\) drive
\[
dX_t=(-\kappa X_t+v\cos\Theta_t)dt+\sqrt{2D}\,dW_t,\qquad
d\Theta_t=\sqrt{2D_r}\,dB_t\pmod{2\pi}.
\]
The initial state \((X_0,\Theta_0)\) may be arbitrary and deterministic. Take \(D_r=\kappa\). Define \(s=D/\kappa\) and monic scaled probabilists' Hermite polynomials \(H_j(x)=s^{j/2}\operatorname{He}_j(x/\sqrt{s})\) for \(D>0\), extended at \(s=0\) as \(H_j(x)=x^j\). They satisfy \(H'_j=jH_{j-1}\), \((D\partial_x^2-\kappa x\partial_x)H_j=-j\kappa H_j\), and \(H_4=x^4-6sx^2+3s^2\). The Jordan statement concerns the backward generator on a finite polynomial–Fourier space, not a spectral theorem on its full function-space domain.

## Proof

**1. Invariant sectors.** Write \(h_{j,m}=H_j(x)\cos(m\theta)\) for \(j,m\ge0\). The backward generator is
\[
\mathcal L=(-\kappa x+v\cos\theta)\partial_x+D\partial_x^2+D_r\partial_\theta^2.
\]
For \(j\ge1\) the derivative identity and the cosine multiplication rule give
\[
\mathcal L h_{j,m}=-(j\kappa+m^2D_r)h_{j,m}+
\begin{cases}
jv h_{j-1,1},&m=0,\\
\frac{jv}{2}(h_{j-1,m-1}+h_{j-1,m+1}),&m\ge1.
\end{cases}
\]
There is no off-diagonal term for \(j=0\). For the single initial observable \(H_N=h_{N,0}\) this formula gives the invariant coordinate sector spanned by \(h_{j,m}\) with \(0\le j\le N\), \(0\le m\le N-j\), and \(m\equiv N-j\pmod2\). For a general positional polynomial, evolve each term of its Hermite expansion in its own sector and add. In order of descending \(j\) the generator is triangular with diagonal \(-j\kappa-m^2D_r\). Applying the polynomial moment equations to this closed system gives its exact backward semigroup. The expectations are finite by the explicit stable linear filter with bounded propulsion and Gaussian noise.

**2. Quartic resonance.** The ordered coordinate list for \(H_4\), with each pair denoting \((j,m)\), is
\[
(4,0),(3,1),(2,0),(2,2),(1,1),(1,3),(0,0),(0,2),(0,4).
\]
At \(D_r=\kappa\), exactly \((4,0),(3,1),(0,2)\) share eigenvalue \(-4\kappa\), giving algebraic multiplicity three. To prove defectiveness of order three, one needs a nonzero cubic resolvent pole; the three repeated diagonal entries alone are not enough.

**3. Cubic pole and its leading coefficient.** Write \(R(z)=(zI-\mathcal L)^{-1}\) in this sector. The entry from \((4,0)\) to \((0,2)\) is a sum over four-edge paths, by triangular inversion. All start with the edge \((4,0)\to(3,1)\), of coefficient \(4v\). The remaining three edges have intermediate pairs \(((2,0),(1,1))\), \(((2,2),(1,1))\), or \(((2,2),(1,3))\). For each path the other three vertices are resonant. The products of its four edge coefficients are \(6v^4,3v^4,3v^4\), respectively. The two nonresonant denominators, evaluated at \(z=-4\kappa\), have products \(4\kappa^2,-4\kappa^2,12\kappa^2\), respectively. Thus
\[
\lim_{z\to-4\kappa}(z+4\kappa)^3R(z)_{(0,2),(4,0)}
=\frac{3v^4}{2\kappa^2}-\frac{3v^4}{4\kappa^2}+\frac{v^4}{4\kappa^2}
=\frac{v^4}{\kappa^2}.
\]
This is nonzero, so a Jordan block of size at least three occurs. The algebraic multiplicity is exactly three, which also rules out additional blocks at this eigenvalue. The inverse Laplace transform of \((z+4\kappa)^{-3}\) is \(\tfrac12t^2e^{-4\kappa t}\). Hence the conditional expectation of \(H_4(X_t)\) has the asserted coefficient. No stationary initialization is needed.

**4. Minimality and the raw quartic.** In the sectors of \(H_1,H_2,H_3\), the diagonal values of \(-\mathcal L/\kappa\) are, respectively, \((1,1)\), \((2,2,0,4)\), and \((3,3,1,5,1,9)\) in descending degree and then increasing angular order. Each eigenvalue has algebraic multiplicity at most two in each sector, and the constant sector is trivial. Thus the conditional relaxation of every positional polynomial of degree at most three, being a sum of these evolutions, has no \(t^2e^{\lambda t}\) term. Since \(x^4-H_4(x)\) has degree two, the term in the conditional expectation of the raw fourth moment is the same as for \(H_4\). This proves sharp minimality at the specified resonance.

## Verification

The supplied `verify_ep.py` builds the exact moment generator and tests the algebraic and geometric multiplicities, the pole coefficient, the path sum, lower degrees and two non-unit rational parameter choices. It requires Python and SymPy. The path identity and finite sector argument above establish the result for all the stated parameters; the rational tests are supplementary.

## Relationship to prior work

Caraglio and Franosch [1] give the triangular forward-mode representation and exact propagator for the planar problem. Projection onto one Cartesian coordinate gives the process considered here. Their time-integral recursion can in principle recover the resonant fourth moment; neither triangularity nor the passive diagonal rates alone establish the Jordan order. The question here is specifically whether the paths with three coincident rates cancel, and whether a positional moment of smaller degree can carry such a term. Shee, Dhar and Chaudhuri [2] give an exact Laplace moment recursion and compute the transient **radial** fourth moment, not this single Cartesian fourth moment with its pure second angular harmonic. Pattanayak and coauthors [3] compute time-dependent displacement moments of a harmonically trapped swimmer with torque; their radial fourth moment concerns a different observable. Nakul and Gopalakrishnan [4] study stationary harmonic active Brownian laws. No novelty is claimed for the generator, moment method, or general triangular evolution; the contribution is the explicit noncancellation and minimal observable degree at this resonance.

## Limitations

Only this harmonically trapped process, \(D_r=\kappa\), and positional polynomial observables are considered. The finite Jordan block does not classify the full generator domain or all parameter ratios. The coefficient can vanish after averaging over the initial angle, and no finite-window detectability result is proved. The comparison is best-of-knowledge; a prior specialization of an exact moment or propagator formula could affect priority.

## References

1. M. Caraglio and T. Franosch, *Analytic Solution of an Active Brownian Particle in a Harmonic Well*, arXiv:2210.04205 (2022), https://arxiv.org/abs/2210.04205.
2. A. Shee, A. Dhar and D. Chaudhuri, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234 (2020), https://arxiv.org/abs/2005.14234.
3. A. Pattanayak, A. Shee, A. Chaudhuri and D. Chaudhuri, *Exact dynamics and dimensional effects in torque-driven trapped active Brownian particles*, arXiv:2603.26967v2 (2026), https://arxiv.org/abs/2603.26967v2.
4. E. Nakul and M. Gopalakrishnan, *Stationary states of an active Brownian particle in a harmonic trap*, arXiv:2209.09184 (2022), https://arxiv.org/abs/2209.09184.
