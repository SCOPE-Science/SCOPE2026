# Unequal two-camp oscillations in cubic complete-graph opinion dynamics: the sharp one-third barrier

## Finding

**Theorem (complete two-camp antipodal-cycle stability criterion).** Fix an integer \(N\ge3\), positive integers \(m,\ell\) with \(m+\ell=N\), and positive parameters \(a,\gamma\). Consider the synchronous minimally nonlinear opinion map on the unweighted complete graph with stochastic neighbor weights \(W=(\mathbf1\mathbf1^\top-I)/(N-1)\):
\[
F(v)=\bigl[(1-\gamma)I+\gamma W\bigr]v+\gamma a[(I-W)v]^{\circ3},\qquad v\in\mathbb R^N.
\]
Put
\[
\nu=\frac{N\gamma}{N-1},\quad \beta=\nu-2,\quad k=\gamma a\bigl(\tfrac{N}{N-1}\bigr)^3,
\quad D=m^2-m\ell+\ell^2.
\]
If \(\beta>0\), each specified partition into blocks of sizes \(m,\ell\) carries a primitive period-two orbit \(\{v_*,-v_*\}\), unique among orbits that exactly reverse the block difference and have zero mean over the two phases. Its interblock difference in the first phase is
\[
d_*=\sqrt{\frac{\beta N^2}{kD}},
\]
and its two block values are explicit in the proof. Common translations of this orbit are also period-two orbits.

The orbit is **linearly exponentially attracting transverse to the uniform-translation direction**, in the full \(N\)-agent system, if and only if
\[
\boxed{\quad\frac12<\frac m\ell<2,\qquad 0<\beta<\beta_c(m,\ell):=
\frac{2(m^2-m\ell+\ell^2)}{(m+\ell)(2\max\{m,\ell\}-\min\{m,\ell\})}.\quad}
\]
Here 'linearly exponentially attracting' means that every eigenvalue of the two-step return map on the quotient \(\mathbb R^N/\mathrm{span}\{\mathbf1\}\) lies strictly inside the unit circle. In that regime, all sufficiently nearby states approach **some translate** of the same two-phase orbit. The translation multiplier itself equals one, so an individual orbit is not isolated or asymptotically attracting in the full state space. Outside the strict conditions, the return map has a quotient multiplier of modulus at least one; strict inequalities violating the upper bound or the cluster-balance condition yield linear instability, whereas equality cases are nonhyperbolic and are not classified nonlinearly here.

In particular, at least five agents are needed for an odd-sized complete graph to support such a **transversely exponentially attracting unequal two-camp antipodal cycle**. The minimum is attained by block sizes \((m,\ell)=(2,3)\), when \(0<\beta<7/10\). At \(N=5\), \(\gamma=9/5\), \(a=16/63\), the exact cycle is
\[
\left(\frac{81}{140},\frac{81}{140},-\frac{59}{140},-\frac{59}{140},-\frac{59}{140}\right)
\longleftrightarrow
-\left(\frac{81}{140},\frac{81}{140},-\frac{59}{140},-\frac{59}{140},-\frac{59}{140}\right).
\]
Its four nontrivial one-step quotient eigenvalues are \(-1/2,-2/7,-23/28,-23/28\).

## Assumptions and scope

The state space is \(\mathbb R^N\) with \(N\ge3\), and every complete-graph off-diagonal weight is \(1/(N-1)\). Both parameters \(a,\gamma\) are strictly positive; there are no external stubborn agents, time-varying interactions or saturation/clipping. The proposed solutions have exactly two homogeneous blocks, each nonempty. A two-camp orbit here means a block-invariant orbit whose interblock difference reverses sign on each step, with no assertion about other, possibly more complicated, period-two orbits.

For \(\nu\le2\), a nonzero sign-reversing two-block difference does not exist: the scalar equation derived below would require a nonpositive square. For \(\nu>2\), the square root \(d_*\) is positive. At the displayed spectral boundaries, eigenvalues may have modulus one; the theorem asserts no nonlinear attracting/repelling classification there. The opinion vector of the exact five-agent witness remains in \([-1,1]^5\) at both phases, but no globally invariant opinion cube is assumed for arbitrary parameters.

## Proof

**1. Exact two-block reduction.** Write \(P=I-\mathbf1\mathbf1^\top/N\) and \(c=N/(N-1)\). Since \(I-W=cP\),
\[
F(v)=v-\nu Pv+k(Pv)^{\circ3}.
\]
A two-block vector has values \(u\) repeated \(m\) times and \(z\) repeated \(\ell\) times. Define the interblock difference \(d=u-z\) and mean \(s=(mu+\ell z)/N\). The deviations are \(u-s=(\ell/N)d\) and \(z-s=-(m/N)d\). Substitution gives the **exact**, two-dimensional polynomial map
\[
\begin{aligned}
d'&=(1-\nu)d+\frac{kD}{N^2}d^3,\\
s'&=s+\frac{k m\ell(\ell-m)}{N^3}d^3.
\end{aligned}
\tag{1}
\]
The identity \(\ell^3+m^3=N(m^2-m\ell+\ell^2)=ND\) proves the cubic difference coefficient. The second identity follows by summing the blockwise cubes with multiplicity.

**2. The exact antipodal orbit.** For nonzero \(d\), the constraint \(d'=-d\) in (1) is equivalent to \(kDd^2/N^2=\nu-2=\beta\). Therefore it has exactly two signed solutions when \(\beta>0\), and none when \(\beta\le0\). Choose \(d=d_*>0\) and set
\[
H=\frac{k m\ell(\ell-m)}{N^3}d_*^3,\qquad s_*=-\frac H2.
\]
Then equation (1) yields \(d'=-d_*\) and \(s'=s_*+H=-s_*\), so both block values switch to their negatives. Explicitly,
\[
(u_*,z_*)=\left(-\frac H2+\frac\ell N d_*,\;-\frac H2-\frac mN d_*\right),
\quad F(v_*)=-v_*.
\]
Because \(F\) is odd, \(F(-v_*)=v_*\). Since \(d_*>0\), the period is exactly two. Given a choice of sign for \(d\), the condition \(F(v)=-v\) fixes the mean to \(-H/2\), so the antipodal representatives are unique within the specified two-block invariant space. Finally, \(P(v+t\mathbf1)=Pv\) proves \(F(v+t\mathbf1)=F(v)+t\mathbf1\) for every real \(t\). This gives the one-parameter family of translated period-two orbits.

**3. The entire \(N\)-dimensional Floquet spectrum.** Differentiate:
\[
J(v)=DF(v)=I-\nu P+3k\,\mathrm{diag}\bigl((Pv)_i^2\bigr)P.
\]
Since \(P(-v_*)=-Pv_*\) and the formula uses their squares, the two phase Jacobians coincide: \(J(v_*)=J(-v_*)=:J_*\). Thus the two-step Jacobian is \(J_*^2\).

The permutation symmetry within blocks decomposes the tangent space into: the uniform direction (dimension one), an \(m-1\) dimensional within-first-block zero-sum subspace, an \(\ell-1\) dimensional within-second-block zero-sum subspace, and one interblock quotient direction. The first subspace has multiplier one. In the two within-block subspaces, direct use of the fixed block deviations gives
\[
\begin{aligned}
\lambda_m&=1-\nu+3k\ell^2d_*^2/N^2
=-1+\frac{\beta N(2\ell-m)}{D}&&\text{(multiplicity \(m-1\))},\\
\lambda_\ell&=1-\nu+3km^2d_*^2/N^2
=-1+\frac{\beta N(2m-\ell)}{D}&&\text{(multiplicity \(\ell-1\))}.
\end{aligned}
\]
The derivative of the scalar difference equation at \(d_*\) is
\[
\lambda_d=1-\nu+3kDd_*^2/N^2=-1+2\beta.
\]
The mean can respond to an interblock perturbation, but cannot change the quotient eigenvalues; the full matrix is block triangular in the mean/difference splitting. Consequently, the complete **two-step spectrum** is
\[
1,\quad \lambda_d^2,\quad \lambda_m^2\ \text{(\(m-1\) copies)},\quad \lambda_\ell^2\ \text{(\(\ell-1\) copies)}.
\tag{2}
\]
It is valid also when a block has size one, in which case the corresponding within-block eigenvalue is absent.

**4. Exact Schur inequalities and boundaries.** The interblock condition \(|\lambda_d|<1\) means \(0<\beta<1\). For a nontrivial within-block subspace, \(\lambda_m>-1\) if and only if \(2\ell>m\); similarly, \(\lambda_\ell>-1\) if and only if \(2m>\ell\). At \(N\ge3\), even when one block is a singleton, the nontrivial other block imposes the missing inequality. Together these are equivalent to \(m<2\ell\) and \(\ell<2m\).

The upper inequalities \(\lambda_m<1\) and \(\lambda_\ell<1\), when their modes are present, are equivalent to
\[
\beta<\frac{2D}{N(2\ell-m)},\qquad
\beta<\frac{2D}{N(2m-\ell)}
\]
respectively, given positive denominators. Their joint sharp limit is \(\beta_c=2D/[N(2\max\{m,\ell\}-\min\{m,\ell\})]\). Writing \(M=\max(m,\ell)\), \(q=\min(m,\ell)\),
\[
N(2M-q)-2D=3q(M-q)\ge0,
\]
so \(\beta_c\le1\), with equality exactly for balanced blocks. Thus this upper bound automatically incorporates the difference-mode restriction. If the block-balance condition fails, a present within-block multiplier is \(\le-1\). If the balance condition holds but \(\beta\ge\beta_c\), a within-block or interblock multiplier reaches or exceeds \(+1\). This proves the necessary-and-sufficient **strict spectral** criterion, and also the distinctions between equality and strict-instability cases.

When the quotient spectrum is strictly inside the unit disk, the induced two-step map on the quotient is locally contracting in an equivalent norm. The mean increment is smooth and vanishes on the cycle; its successive increments are bounded by a summable geometric series along nearby quotient trajectories. Hence the mean converges and the full orbit approaches a (generally initial-condition-dependent) common translate of the two-phase cycle. This proves normal attraction without incorrectly claiming contraction along the translation direction.

**5. Odd-size minimum and exact instance.** For \(N=3\), the only nonempty two-block sizes are \((1,2)\) and \((2,1)\), exactly at the excluded ratio boundary; a present within-block one-step multiplier equals \(-1\). For \(N=5\), \((m,\ell)=(2,3)\) lies strictly inside the ratio window, and \(D=7\), \(\beta_c=7/10\). The particular rational choices \(\gamma=9/5\) and \(a=16/63\) give \(\nu=9/4\), \(\beta=1/4\), \(k=25/28\), \(d_*=1\), and \(H=3/70\). Inserting these into the block formula produces the stated rational vector. The one-step quotient eigenvalues are exactly \(-1/2,-2/7,-23/28,-23/28\), so all return multipliers have modulus strictly less than one. This proves the minimum among odd sizes and the constructive witness.

## Verification

The accompanying `checker.py` uses Python's exact `fractions.Fraction` arithmetic, with no numerical tolerances or third-party dependencies. It verifies \(F(v_*)=-v_*\), \(F^2(v_*)=v_*\), the Jacobian actions on within-block and interblock modes, and agreement of the strict spectral inequalities for **65** combinations \(3\le N\le12\) and \(1\le m<N\). The independent rational five-agent parameters, vector, and eigenvalues are checked separately. Execution from this package returned: `PASS: 65 exact two-cluster checks, plus exact five-agent witness and multipliers`. These finite tests corroborate the algebra; the all-\(N\) statement follows from steps 1–4, not exhaustive enumeration.

## Relationship to prior work

Kumar and Yao (2026) introduce precisely the cubic opinion update and analyze complete, even-size networks through balanced two-camp states; their Theorem 2 gives the balanced oscillation stability interval. Their asymmetric-clustering analysis instead perturbs directed influence weights. Here the graph remains undirected and uniformly weighted, while block sizes and within-block opinion magnitudes differ. The explicit imbalance-dependent stability frontier, the exact treatment of neutral translation, and the odd-size minimum are the assessed extensions; the equal-block formula is a recovered known case, not a new claim.

Cosenza and Parravano (2001) analyze two-cluster dynamics and cluster-size effects for generally coupled **quadratic local maps** with common forcing. Glendinning's *Stability of Asymmetric Cluster States in Globally Coupled Maps* gives general cluster reductions and transverse linearization tools for a class allowing nonlinear coupling; its stated hyperbolic persistence result invokes a strictly attracting local map, whereas the identity local map here has a neutral uniform-translation direction. These works motivate, but do not in the inspected results state, the exact \(N\)-agent cubic-deviation criterion above. Published findings on cubic network averaging and on two-cluster cycles in discrete Kuramoto networks concern, respectively, near-consensus drift and a distinct sine-coupled phase map. Similar fractions in the latter are not an implication about this model.

## Limitations

The result is a local spectral and normal-attraction statement, not global convergence from arbitrary initial opinions. It does not classify all period-two or higher-period states, nor the nonlinear dynamics on the equality boundaries. It assumes exact complete-graph coupling and a polynomial update on real-valued opinions, not empirical bounded media exposure. The neutral translation multiplier must be retained rather than called an asymptotically stable isolated orbit. Historical priority cannot be established by a finite literature search, particularly because some older general coupled-map papers may contain equivalent specializations.

## References

1. Rajul Kumar and Ningshi Yao (2026), *Analysis and Consensus Control of Emergent Dynamic Polarization in Minimally-Nonlinear Opinion Dynamics*, arXiv:2608.09724v1, first public August 10, 2026. https://arxiv.org/abs/2608.09724
2. M. G. Cosenza and A. Parravano (2001), *Dynamics of Coupling Functions in Globally Coupled Maps: Size, Periodicity and Stability of Clusters*, arXiv:nlin/0107046. https://arxiv.org/abs/nlin/0107046
3. Paul Glendinning, *Stability of Asymmetric Cluster States in Globally Coupled Maps*, publicly accessible author manuscript, https://personalpages.manchester.ac.uk/staff/paul.glendinning/preprints/clust.pdf
