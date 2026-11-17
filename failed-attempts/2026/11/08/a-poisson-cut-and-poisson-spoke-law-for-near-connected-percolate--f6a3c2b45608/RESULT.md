# A Poisson-cut and Poisson-spoke law for near-connected percolated wheels

## Finding

Let \(W_n=K_1\vee C_n\), with \(n\ge3\) rim vertices and one hub. Keep every rim edge independently with probability \(p\in[0,1]\) and every spoke independently with probability \(q\in[0,1]\). Write \(R_n(p,q)\) for the probability that the resulting graph is connected and \(S_n\) for the fraction of rim vertices belonging to the hub's open component.

**Exact two-edge-type identity.** Define
\[
T(p,q)=\begin{pmatrix}p(1-q)+(1-p)q & pq\\1-p&p\end{pmatrix}.
\]
For every \(n\ge3\),
\[
R_n(p,q)=\operatorname{tr}(T(p,q)^n)-2[p(1-q)]^n,\qquad
\Pr(S_n=0)=(1-q)^n.
\]

**Simultaneous rare-defect limit.** Suppose \(n(1-p_n)\to\mu\) and \(nq_n\to\lambda\), where \(\lambda,\mu\in[0,\infty)\) are finite. Let \(J\sim\operatorname{Pois}(\mu)\). Independently sample a rate-\(\lambda\) homogeneous Poisson process of seeds on the unit circle. If \(J=0\) or \(1\), define a single arc of length \(1\); otherwise the \(J\) cut points divide the circle into \(J\) arcs with random lengths \((L_1,\ldots,L_J)\), distributed as \(\operatorname{Dirichlet}(1,\ldots,1)\) conditionally on \(J\) when indexed from a uniformly chosen cut point. An arc is *seeded* when it contains at least one seed. Set \(S\) equal to the total length of the seeded arcs. Then
\[
S_n\ \xrightarrow{\mathrm d}\ S.
\]
Conditional on the arc lengths, their seeded indicators are independent Bernoulli variables of probabilities \(1-e^{-\lambda L_i}\). Thus this description specifies the *entire* limiting law, including its continuously distributed component when \(\lambda\mu>0\).

Its endpoint atoms are explicit:
\[
\Pr(S=0)=e^{-\lambda},\qquad
\Pr(S=1)=F(\lambda,\mu)
=2e^{-(\lambda+\mu)}\left[e^{\lambda/2}
\cosh\!\left(\tfrac12\sqrt{\lambda^2+4\lambda\mu}\right)-1\right].
\]
In particular \(R_n(p_n,q_n)\to F(\lambda,\mu)\). For \(\lambda+\mu>0\), the mean is
\[
\mathbb ES=1-(1+\mu)e^{-(\lambda+\mu)}
-\frac{\mu^2}{(\lambda+\mu)^2}
\left[1-(1+\lambda+\mu)e^{-(\lambda+\mu)}\right],
\]
with \(\mathbb ES=0\) at \(\lambda=\mu=0\). If both parameters are strictly positive, \(\Pr(0<S<1)>0\). For example, at \(\lambda=\mu=1\) the endpoint masses are approximately \(0.36787944\) and \(0.48479382\); the remaining mass \(0.14732674\) is in \((0,1)\).

## Assumptions and scope

All bond states are mutually independent. A closed rim edge is a *cut*, whereas an open spoke is a *seed*. The positive integer \(n\) counts rim vertices, not all wheel vertices. A connected percolated wheel is equivalent to every rim component having an open spoke; for no or one cut, the rim consists of one component. The limits concern finite nonnegative \(\lambda,\mu\), not diverging intensities or correlated edges. Convergence of \(S_n\) is in distribution, not total variation: \(S_n\) lies on a lattice while the limit has interior continuous mass.

## Proof

**1. Finite two-state transfer.** Traverse rim vertices cyclically. Immediately before inspecting a vertex, let state \(0\) mean no spoke has yet been seen after the last cut and state \(1\) mean a spoke has been seen. Examine that vertex's spoke, then its outgoing rim edge. A cut is allowed only if a spoke has been seen by then; after a cut the state resets to \(0\). An open rim edge retains the updated state. The permitted one-step transition weights are precisely \(T_{00}=p(1-q)+(1-p)q\), \(T_{01}=pq\), \(T_{10}=1-p\), \(T_{11}=p\).

When at least one cut is present, each admissible cyclic bond configuration has exactly one consistent cyclic state history. If there are no cuts but at least one seed, it again has exactly one such history, the constant state \(1\). The sole exceptional configuration, with all rim edges open and all spokes closed, has two cyclic histories (constant \(0\) and constant \(1\)), but is disconnected. Its probability is \([p(1-q)]^n\). Subtracting its two weights from the trace proves the displayed formula for \(R_n\). The hub has no rim neighbors exactly when all spokes are closed, proving \(\Pr(S_n=0)=(1-q)^n\).

**2. Joint rare-event convergence and the full law.** Mark every closed rim edge by its angular position in \([0,1)\), and every open spoke by its vertex position. The two independent Bernoulli point processes converge jointly to independent homogeneous Poisson point processes of respective rates \(\mu\) and \(\lambda\). One direct proof tests each finite family of disjoint angular intervals: multinomial generating functions for the independent Bernoulli indicators tend to the Poisson generating functions, and the total number of marks is tight. Almost surely the limiting point processes have no coincidences; every cut and every seed is distinct. The operation of forming cut arcs, identifying arcs containing seeds, and summing their lengths is continuous at each such finite configuration (including zero or one cut). Therefore the continuous-mapping theorem gives \(S_n\Rightarrow S\).

Conditioning on \(J=j\) uniform cut locations and choosing a uniform cut point as the cyclic indexing origin gives gap lengths with the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution for \(j\ge2\); for \(j=0,1\) the whole circle is one component. Independent Poisson restrictions to disjoint arcs give the asserted Bernoulli seeded indicators. There are no unseeded vertices if and only if every cut arc is seeded; for the finitely many random cut and seed positions, this event is almost surely stable under sufficiently small perturbations, so its probability also converges under the point-process coupling. The zero mass is \(e^{-\lambda}\), since any seed makes a positive-length arc hub-connected.

**3. Closed limiting connectivity formula.** With \(r_n=1-p_n\), the transfer matrix satisfies
\[
T(p_n,q_n)=I+\frac1n A+o(n^{-1}),\qquad
A=\begin{pmatrix}-(\lambda+\mu)&\lambda\\\mu&-\mu\end{pmatrix}.
\]
Consequently \(T(p_n,q_n)^n\to e^A\), and \([p_n(1-q_n)]^n\to e^{-(\lambda+\mu)}\). Writing \(A=-(\lambda+\mu)I+B\), where \(B=\bigl(\begin{smallmatrix}0&\lambda\\\mu&\lambda\end{smallmatrix}\bigr)\), the eigenvalues of \(B\) are \(\tfrac12(\lambda\pm\sqrt{\lambda^2+4\lambda\mu})\). Thus \(\operatorname{tr}(e^A)=2e^{-(\lambda+\mu/2)}\cosh(\tfrac12\sqrt{\lambda^2+4\lambda\mu})\). Subtraction proves the stated \(F\).

**4. Explicit expectation and interior mass.** Fix a uniformly selected point on the limiting rim. Let \(L\) be the length of its cut arc. If there are at most one cuts, \(L=1\), an event of probability \((1+\mu)e^{-\mu}\). Otherwise, the two nearest cuts flanking the point occur at clockwise and anticlockwise distances \(u,v>0\), whose joint density before wraparound is \(\mu^2e^{-\mu(u+v)}\), for \(u+v<1\). Therefore \(L\) has density \(\mu^2\ell e^{-\mu\ell}\) on \(0<\ell<1\), together with the atom above at \(1\). Conditional on \(L\), the arc is unseeded with probability \(e^{-\lambda L}\). Hence
\[
1-\mathbb ES=(1+\mu)e^{-(\lambda+\mu)}
+\mu^2\int_0^1\ell e^{-(\lambda+\mu)\ell}\,d\ell,
\]
which evaluates to the displayed mean. For \(\lambda,\mu>0\), the positive-probability event of exactly two cuts with seeds in exactly one of their two positive-length arcs yields \(0<S<1\).

## Verification

The standalone standard-library program `verify.py` independently enumerates all open/closed rim and spoke configurations for \(3\le n\le6\) at six rational probability pairs, compares weighted exact probabilities to the matrix formula, checks hub isolation, tests boundary identities for additional orders, and checks numerical consistency of the explicit limiting formula. Run `python3 verify.py` from this directory. Its output is `VERIFY_OK 295 exact/boundary/limit consistency assertions`. Finite enumeration and numerical checks are corroboration, not proofs of convergence or historical novelty.

## Relationship to prior work

Mann, Smith, Mitchell, Jefferson and Dobson (arXiv:2102.09261v1, first public 2021-02-18) give exact percolation counting formulas for homogeneous cycles and cliques within a configuration-network setting. Their simple-cycle section concerns cycle-component attachment to a giant component, not the two-intensity finite-wheel connectivity and hub-fraction law here.

Wheel all-terminal reliability polynomials and their homogeneous edge-probability recurrences are classical (e.g. the Wheel row of MathWorld's *Reliability Polynomial*). The finite transfer formula above is consistent with that general theory, but the established one-variable recurrence does not itself state the two-intensity rare-event limit or its full mixed distribution.

Cohen, Dawid, Kardar and Bar-Yam (arXiv:0802.1055v1) analyze nearest-neighbor percolation supplemented by independent long-range bonds and introduce ghost bonds linking sites to a common super-site. This is an important conceptual precursor to the hub, but their reported thermodynamic transition involves extensive long-range random edges, with fixed-parameter infinite-volume limits; the finite-intensity Poisson cut-and-seed circle and its endpoint-mass law are not reported there. This comparison does not establish exhaustive historical priority.

## Limitations

The conclusion is specific to independent edge failures on the wheel, with distinct rim and spoke retention probabilities at finite Poisson intensities. It does not establish a critical exponent for a growing-dimensional network, a total-variation limit for \(S_n\), or a result for correlated faults. The exact homogeneous wheel reliability recurrence is known; the claimed added content is the joint two-type critical window, full limit law and explicit limiting atom and mean formulas. Historical priority remains subject to further independent literature assessment.

## References

1. P. Mann, V. A. Smith, J. B. O. Mitchell, C. Jefferson, S. Dobson, *An exact formula for percolation on higher-order cycles*, arXiv:2102.09261v1 (2021-02-18), https://arxiv.org/abs/2102.09261 . Journal title: *Exact formula for bond percolation on cliques*, Phys. Rev. E 104, 024304 (2021).
2. R. Cohen, D. J. Dawid, M. Kardar, Y. Bar-Yam, *Unusual percolation in simple small-world networks*, arXiv:0802.1055v1 (2008), https://arxiv.org/abs/0802.1055 .
3. E. W. Weisstein, *Reliability Polynomial*, MathWorld, https://mathworld.wolfram.com/ReliabilityPolynomial.html , wheel reliability recurrence.
