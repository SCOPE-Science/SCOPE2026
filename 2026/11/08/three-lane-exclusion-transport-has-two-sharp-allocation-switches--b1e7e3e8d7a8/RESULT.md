# Three-lane exclusion transport has two sharp allocation switches and a local-optimum coexistence window

## Finding

Consider the three-lane exclusion process specified below, with uncoupled rightward bias \(A>0\), arbitrary signed interlane coupling \(\gamma\in\mathbb R\), and stationary densities \((p_1,p_2,p_3)\) constrained by \(p_1+p_2+p_3=1\). The total *signed* stationary rightward current is \(J_\gamma=\sum_{i=1}^3j_i\). Its exact optimum over all such density allocations is

\[
C(\gamma)=\max_{p_i\ge0,\ \sum p_i=1}J_\gamma(p)=
\begin{cases}
0,&\gamma\le-2A,\\[2pt]
(2A+\gamma)/4,&-2A\le\gamma\le-6A/7,\\[2pt]
2(3A+2\gamma)/9,&\gamma\ge-6A/7.
\end{cases}
\]

All maximizing allocations are classified, including the switching values:

- \(\gamma<-2A\): exactly the three fully concentrated corners, permutations of \((1,0,0)\).
- \(\gamma=-2A\): the entire boundary of the density simplex, i.e. every triple with at least one zero coordinate.
- \(-2A<\gamma<-6A/7\): exactly the three balanced two-lane allocations, permutations of \((1/2,1/2,0)\).
- \(\gamma=-6A/7\): those three balanced two-lane allocations **and** the uniform three-lane allocation \((1/3,1/3,1/3)\), and no others. The optimal current is \(2A/7>0\).
- \(\gamma>-6A/7\): only the uniform three-lane allocation.

The local-optimum structure is sharper. The uniform interior allocation is a strict local maximum exactly for \(\gamma>-A\); the balanced two-lane boundary allocations are strict local maxima for \(-2A<\gamma<-4A/5\). These branches coexist as distinct strict local optima throughout

\[
-A<\gamma<-4A/5,
\]

and exchange global optimality at \(\gamma=-6A/7\). The uniform interior state loses local maximality at \(-A\), while the balanced face state loses it at \(-4A/5\). The maximal-current curve has derivative jumps at both \(-2A\) and \(-6A/7\).

This is a **choice of allocation across separately conserved stationary sectors**. It is not a claim of dynamical symmetry breaking or spontaneous interlane particle transfer in a fixed realization.

## Assumptions and scope

Take three parallel periodic exclusion rings, each with \(L\ge3\) sites and binary occupations \(\eta_k^i\in\{0,1\}\). Particles hop only to a vacant nearest-neighbour site of the *same* ring; no interlane hopping occurs. For bond \((k,k+1)\) on lane \(i\), define the signed forward-minus-backward rate

\[
d_i(k)=A+\frac\gamma2\sum_{j\ne i}(\eta_k^j+\eta_{k+1}^j).
\]

For example, choose actual **strictly positive** right and left rates

\[
r_i^+(k)=b+\max\{d_i(k),0\},\qquad
r_i^-(k)=b+\max\{-d_i(k),0\},\quad b>0.
\]

Thus all real \(\gamma\) values are physically valid rates, including those where the effective drift is locally reversed. Since each lane conserves its particle number \(N_i\), optimization is performed over externally selected sectors, with \(N_1+N_2+N_3=L\), in the limit \(L\to\infty\) along sectors with densities \(N_i/L\to p_i\).

The stationary canonical measure is uniform within each fixed particle-count sector. Its thermodynamic limit is the product Bernoulli measure with prescribed lane densities. The one-bond limiting currents, consistent with Popkov (2026), are

\[
j_i=p_i(1-p_i)\left(A+\gamma\sum_{j\ne i}p_j\right).
\]

The finite-ring signed current for fixed sector counts is exactly \(L/(L-1)\) times the displayed thermodynamic current evaluated at \(p_i=N_i/L\); this does not imply the same *continuum set of optimal allocations* at every finite \(L\), since finite densities are discrete.

The primary MSC2020 classification is 82C22 (interacting particle systems).

## Proof

**1. Invariant distribution and microscopic current.** For a configuration with occupation pair \((\eta_k^i,\eta_{k+1}^i)=(1,0)\), its incoming-minus-outgoing mass under a uniform sector law, from the two orientations of that bond, is \(-d_i(k)\). For \((0,1)\) it is \(+d_i(k)\). Consequently total incoming-minus-outgoing mass is

\[
\sum_{i,k}(\eta_{k+1}^i-\eta_k^i)
\left[A+\frac\gamma2\sum_{j\ne i}(\eta_k^j+\eta_{k+1}^j)\right]=0.
\]

The constant contributions telescope in \(k\). For each unordered pair of lanes \(i,j\), the two coupling contributions combine to \(\gamma\sum_k(\eta_{k+1}^i\eta_{k+1}^j-\eta_k^i\eta_k^j)=0\). Positivity of all hopping rates makes each nontrivial fixed-count sector irreducible, so the uniform canonical law is stationary and unique in that sector. Under that law, different lanes are independent; for each lane, \(\Pr(\eta_k^i=1,\eta_{k+1}^i=0)=N_i(L-N_i)/[L(L-1)]\). Taking the mean of \(d_i(k)\) in the independent other lanes gives the claimed exact current and its limit.

**2. Symmetric-polynomial reduction.** Under \(\sum_i p_i=1\), set \(e_2=p_1p_2+p_2p_3+p_3p_1\) and \(e_3=p_1p_2p_3\). Direct expansion gives

\[
J_\gamma=(2A+\gamma)e_2+3\gamma e_3.
\]

The three relevant candidates have currents

\[
J_{\mathrm{uniform}}=\frac{2(3A+2\gamma)}9,\quad
J_{\mathrm{face}}=\frac{2A+\gamma}4,\quad
J_{\mathrm{corner}}=0.
\]

**3. Global sharpness and equality.** On the density simplex \(e_2\le1/3\) and \(e_3\le1/27\), with simultaneous equality only at the uniform allocation. Schur's cubic inequality gives

\[
4e_2-9e_3\le1.
\]

Its equality cases on the closed simplex are exactly the uniform allocation and permutations of \((1/2,1/2,0)\). To see the sharp boundary directly, fix \(z=p_3\) and write \(p_1p_2=t\le(1-z)^2/4\). Then \(4e_2-9e_3=4z(1-z)+(4-9z)t\). If \(z\le4/9\), its maximum over \(t\) occurs at \(t=(1-z)^2/4\), leaving a deficit \(z(3z-1)^2/4\). If \(z\ge4/9\), the maximum is at \(t=0\), giving \(4z(1-z)\le1\). This also proves the equality cases.

At \(\gamma=-6A/7\), the current equals \((2A/7)(4e_2-9e_3)\). At \(\gamma=0\), the current is \(2Ae_2\); at \(\gamma=-2A\), it is \(-6Ae_3\). For \(-6A/7<\gamma<0\), interpolate affinely between the first two parameter values: the uniform state uniquely saturates both endpoint upper bounds. For \(-2A<\gamma<-6A/7\), interpolate between \(-2A\) and \(-6A/7\): only balanced faces simultaneously saturate both endpoint bounds. For \(\gamma>0\), both \(e_2,e_3\) are simultaneously maximized only at uniform density. For \(\gamma<-2A\), both coefficients in the symmetric-polynomial representation are negative, hence the corners alone maximize the current. The endpoint equality cases follow directly. This proves the full piecewise maximum and every optimizer.

**4. All local maximizers and the two local-stability thresholds.** Write \(J_\gamma=\sum_{i=1}^3f(p_i)\), where \(f(t)=t(1-t)[A+\gamma(1-t)]\). At the uniform state, the tangent Hessian is \(-2(A+\gamma)\) times the identity on the tangent plane. It is strictly negative for \(\gamma>-A\), strictly positive for \(\gamma<-A\); at equality the nonzero cubic term changes sign along feasible directions. Thus the uniform state is a strict local maximum exactly in the claimed region.

At a balanced face \((1/2,1/2,0)\), the tangential second derivative is negative when \(2A+\gamma>0\); the inward first variation equals \(f'(0)-f'(1/2)=A+5\gamma/4\). The face is a strict local maximum if and only if \(-2A<\gamma<-4A/5\). At the upper endpoint the inward first variation vanishes but the curve \(((1-z)/2,(1-z)/2,z)\), \(z>0\) small, increases current by \((3A/10)z^2(1-2z)>0\), so it is not a local maximum there. At \(\gamma=-2A\) every face point is globally maximal but not strict; below it only the three corners are locally maximal.

There are no other interior local maxima. Indeed, the stationarity equations \(f'(p_i)=f'(p_j)\) and the quadratic form of \(f'\) permit at most two distinct interior values. If they are not all equal, relabel to \((x,x,1-2x)\) with \(x\ne1/3\), at which stationarity implies \(2A+\gamma(1+3x)=0\). The second variations along \((1,1,-2)\) and \((1,-1,0)\) are opposite, nonzero quantities proportional to \(-6\gamma(3x-1)\) and \(+6\gamma(3x-1)\), so this point is a saddle. No unbalanced face point is maximal because the restriction to a face is \((2A+\gamma)t(1-t)\). Corners are strict local maximizers precisely below \(-2A\). This completes the local classification.

**5. Why three lanes are the first distinct case.** For only two lanes with the same symmetric rate difference and fixed combined density \(p_1+p_2=1\), the current reduces to \((2A+\gamma)p_1p_2\). It has no nonzero-current coexistence switch between a uniform and a face-balanced state, nor an interval of two distinct strict local optima. The three-lane result therefore identifies the minimal symmetric-lane allocation setting with this *positive-current*, bistable optimization phenomenon.

## Verification

Run `python check.py` with Python 3 and SymPy installed. The standalone script checks exact polynomial identities, equality-boundary factorizations, strict-local-curvature formulas, 69,090 rational arithmetic checks, complete incoming-minus-outgoing mass cancellation for every configuration on short periodic rings under six signed couplings, and exact canonical one-bond currents across multiple sectors. All reported tests passed. These finite tests corroborate but do not substitute for the all-density proof above.

## Relationship to prior work

Popkov (2026) proves the bidirectional multilane product-measure rates and exact current law with interlane differences of *arbitrary* sign. That current law, not the sector measure or current formula itself, is the input here. Popkov, Schadschneider, Schmidt and Schütz (2015) studied related three-lane currents and nonlinear fluctuations with one-way nonnegative rates; Schmidt, Krajnik and Popkov (2026) investigated multiply degenerate hydrodynamic modes for a one-way multilane process. The sharp fixed-total-density global and local throughput-allocation classifications are not claimed by those sources in the inspected material. Classical Schur inequality is explicitly used and not claimed as new. Earlier two-lane unconstrained current optimization is a distinct problem: it neither imposes a fixed total occupation nor contains the uniform-versus-two-active-lane coexistence at positive current.

## Limitations

This theorem concerns an exact stationary **signed current** optimized over externally chosen conserved sectors, at a fixed total density of one particle per longitudinal column; it does not imply that a single sector dynamically changes its lane densities. It proves no kinetic transition rate, hysteresis time, domain structure, mixing-rate law, or hydrodynamic universality class. The sector optimization is continuous-density/thermodynamic; finite ring current formulas have a common factor but finite-ring allocation grids are discrete. Classical Schur inequality and the published current formula are strong prior ingredients, so a previously unindexed application to the same constrained objective remains an originality risk. The result is a sharp classification for this motivated three-lane model, not an arbitrary-lane theorem.

## References

1. V. Popkov, “Multilane Asymmetric Exclusion Process with stationary Bernoulli measure,” arXiv:2605.06949v1, first public May 7, 2026, https://arxiv.org/html/2605.06949.
2. V. Popkov, A. Schadschneider, J. Schmidt and G. M. Schütz, “Fibonacci family of dynamical universality classes,” *Proceedings of the National Academy of Sciences* 112 (2015), 12645–12650, https://pmc.ncbi.nlm.nih.gov/articles/PMC4611608/.
3. J. Schmidt, Ž. Krajnik and V. Popkov, “Universality in driven systems with a multiply-degenerate umbilic point,” arXiv:2601.04116v1, first public January 7, 2026, https://arxiv.org/abs/2601.04116.
4. Schur's cubic inequality for three nonnegative variables (classical inequality, used with its exact equality conditions).
