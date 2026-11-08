# Sharp winding complexity of cyclotomic complex-time branch values

## Finding

Consider the polynomial differential equation
\[
\frac{dw}{dt}=w^d-1,\qquad d\in\mathbb Z,\quad d\ge3,
\]
in complex time. Its maximal analytic-continuation surface, based at the germ at \(w=\infty\) and \(t=0\), has ramified time-projection values equal to the additive group
\[
\mathcal P_d=\frac{2\pi i}{d}\,\mathbb Z[\zeta_d],
\qquad \zeta_d=e^{2\pi i/d};
\]
the local ramification index at each such value is \(d-1\). These underlying period-map and branching facts are established in [1].

A winding budget naturally truncates this period group. For an integer \(N\ge1\), let
\[
\Delta_d(N)=\frac{2\pi}{d}
\min\left\{\left|\sum_{j=0}^{d-1}a_j\zeta_d^j\right|:\;
(a_j)\in\mathbb Z^d,\quad0<\left|\sum_j a_j\zeta_d^j\right|,\quad
\sum_j|a_j|\le N\right\}.
\]
This is the smallest nonzero complex-time displacement of a branch value realizable by at most \(N\) signed elementary windings around the equilibrium punctures. The minimum exists: its defining coefficient set is finite, and choosing the coefficient of \(1\) to be one makes it nonempty.

**Theorem.** Let \(q=\varphi(d)\), Euler's totient. For every integer \(d\ge3\) and \(N\ge1\),
\[
\boxed{\frac{2\pi}{d}N^{-(q-2)/2}\ \le\ \Delta_d(N)\ \le\
\frac{2\pi}{d}C_qN^{-(q-2)/2},\qquad
C_q=6\sqrt2\,q(2q)^{(q-2)/2}.}
\]
The exponent \((q-2)/2\) is optimal in the two-sided asymptotic sense, with constants depending only on \(d\). There is a sharp dichotomy:

* For \(d\in\{3,4,6\}\), the *exact* value is \(\Delta_d(N)=2\pi/d\) for every \(N\ge1\), and the branch values form a discrete planar lattice.
* For every other \(d\ge3\), the branch values are dense in the entire complex-time plane, and \(\Delta_d(N)\asymp_d N^{-(\varphi(d)-2)/2}\). Equivalently, the smallest budget needed to produce a **nonzero** branch-value displacement of modulus at most \(\varepsilon\) grows as \(\Theta_d(\varepsilon^{-2/(\varphi(d)-2)})\), as \(\varepsilon\downarrow0\).

For example, the sharp decay power is \(1\) at \(d=5\), \(2\) at \(d=7\), and \(4\) at \(d=11\). The statement concerns the branch values of the maximal continuation projection, *not* the singular times of every chosen single-valued solution branch.

## Assumptions and scope

All coefficients \(a_j\) are signed integers. Their \(\ell^1\) budget counts total signed elementary windings, not net winding and not Euclidean length of an arbitrary geometric loop. Loops about all \(d\) punctures may be used, with the usual homology relation that their sum is zero; the minimization is over representing vectors and is unaffected by redundant presentations. Nonzero displacement is essential because many coefficient vectors represent zero.

The equation is a scalar holomorphic ODE with complex dependent variable and complex time. The Riemann surface is the maximal analytic continuation of the time integral from \(w=\infty\); no assertion about dynamical orbits in real time, a fixed inverse branch, or numerical path tracking is intended. The cyclotomic integer ring is \(\mathbb Z[\zeta_d]\), whose degree over \(\mathbb Q\) is \(q=\varphi(d)\).

## Proof

**1. Periods and the winding budget.** The equilibria are \(e_j=\zeta_d^j\). Since \(f'(e_j)=d\zeta_d^{-j}\), the residue of \(dw/f(w)\) at \(e_j\) is \(\zeta_d^j/d\). A signed meridian about \(e_j\) therefore adds \((2\pi i/d)\zeta_d^j\) to the complex-time integral. These are exactly all periods, because meridians generate first homology of the punctured sphere and \(\sum_{j=0}^{d-1}\zeta_d^j=0\). In particular, the budget above includes exactly the periods obtainable by signed meridian combinations of total coefficient length at most \(N\). Near the point at infinity, the local coordinate \(z=1/w\) satisfies
\[
t-t_0=-\frac{z^{d-1}}{d-1}+O(z^{2d-1}),
\]
so the corresponding time projection ramifies to order \(d-1\) at each \(t_0\in\mathcal P_d\). This agrees with the general theorem of [1]; the main new assertion is the sharp finite-winding separation law.

**2. Norm lower bound.** Fix any nonzero
\[
\alpha=\sum_{j=0}^{d-1}a_j\zeta_d^j,\qquad \sum_j|a_j|\le N.
\]
Because \(\alpha\) is a nonzero algebraic integer, its field norm is a nonzero rational integer:
\[
1\le\left|N_{\mathbb Q(\zeta_d)/\mathbb Q}(\alpha)\right|
=\prod_{\substack{1\le k\le d\\ \gcd(k,d)=1}}
\left|\sum_{j=0}^{d-1}a_j\zeta_d^{kj}\right|.
\]
The identity and complex-conjugation embeddings, corresponding to \(k=1\) and \(k=d-1\), contribute \(|\alpha|^2\). Every one of the other \(q-2\) factors is at most \(\sum|a_j|\le N\), by the triangle inequality. Hence
\[
1\le |\alpha|^2N^{q-2},\qquad
|\alpha|\ge N^{-(q-2)/2}.
\]
Multiplication by \(2\pi/d\) gives the lower bound, uniformly for *every* admissible coefficient vector and every integer \(d\ge3\).

**3. Pigeonhole upper bound.** For \(q\ge4\), the \(q\) powers
\(1,\zeta_d,\ldots,\zeta_d^{q-1}\) are linearly independent over \(\mathbb Q\), because the cyclotomic polynomial has degree \(q\). Fix an integer \(L\ge1\). The \((L+1)^q\) values
\[
s(h)=\sum_{j=0}^{q-1}h_j\zeta_d^j,
\qquad h_j\in\{0,1,\ldots,L\},
\]
are distinct and lie in the square \([-qL,qL]^2\subset\mathbb C\). Set
\[
K=\left\lfloor\frac{(L+1)^{q/2}}2\right\rfloor.
\]
Partition the square into \(K^2<(L+1)^q\) equal closed-sided square cells of side \(2qL/K\). Two of the distinct points must occupy one cell. Their difference is a nonzero cyclotomic integer with coefficient \(\ell^1\)-norm at most \(qL\) and modulus bounded by
\[
\sqrt2\frac{2qL}{K}\le6\sqrt2\,qL^{1-q/2},
\]
because \(K\ge (L+1)^{q/2}/3\) for \(q\ge4, L\ge1\). For \(N\ge q\), choose \(L=\lfloor N/q\rfloor\), so \(L\ge N/(2q)\) and \(qL\le N\). Since the exponent \(1-q/2\) is negative,
\[
\Delta_d(N)\le \frac{2\pi}{d}
6\sqrt2\,q(2q)^{q/2-1}N^{1-q/2}.
\]
When \(1\le N<q\), simply choose \(\alpha=1\); the same displayed bound remains valid after the stated (generous) choice of \(C_q\). This proves the upper inequality for all budgets. Together with step 2, it also shows the exponent cannot be improved in either direction.

**4. Discrete versus dense branch values.** For \(q=2\), the norm identity has just the conjugate pair, so every nonzero cyclotomic integer has \(|\alpha|\ge1\), with equality at \(\alpha=1\). The only integers \(d\ge3\) with \(\varphi(d)=2\) are \(3,4,6\). Their integer spans are the triangular or square lattice and give the exact fixed minimum.

For all other \(d\ge3\), \(q\ge4\), and step 3 gives nonzero elements \(\alpha_n\in\mathbb Z[\zeta_d]\) converging to zero. After taking a subsequence, the directions \(\alpha_n/|\alpha_n|\) converge to a unit complex number \(u\). For every real \(s\), integer multiples of \(\alpha_n\) can be chosen converging to \(su\), so the closure of the additive period group contains the full real line \(\mathbb Ru\). Multiplication by \(\zeta_d\) preserves that group; its closure also contains \(\mathbb R\zeta_du\). These lines are not collinear for \(d\ge3\), and their sum is \(\mathbb C\). Therefore the period group, and hence its set of branch values, is dense in \(\mathbb C\).

Finally, if \(q>2\), defining \(N_d(\varepsilon)\) as the least integer budget with \(0<\Delta_d(N)\le\varepsilon\), the lower and upper inequalities imply the claimed two-sided growth \(N_d(\varepsilon)=\Theta_d(\varepsilon^{-2/(q-2)})\). The finite-budget bound is uniform for fixed \(d\), and no assertion is made about uniformity as \(d\to\infty\). \(\square\)

## Verification

The accompanying `check_winding.py` is a standard-library-only finite checker. It enumerates signed coefficient vectors for the lattice cases \(d=3,4,6\), checks the claimed exact minimum through budget four, and checks small finite sets for \(d=5,7,8\). It also constructs explicit coefficient differences by the pigeonhole partition for \(d=5,7,8,10,12\). The exact algebraic norm inequality and the all-budget pigeonhole proof above, rather than finite floating-point checks, establish the theorem.

Execute `python3 check_winding.py` with Python 3.10 or newer. The numerical tolerance is deliberately used only in the finite illustrative checks; it does not enter any mathematical implication in the proof.

## Relationship to prior work

Fiedler [1] establishes the maximal continuation Riemann surface, the meridian-residue period map, the general possibilities for closure of the period group, and the ramification index at its time branch values. Section 1.8 explicitly introduces the cyclotomic family and examines its low-degree dynamics. These results are prerequisites, not claimed here as new. The result proved above instead identifies an exact rank-dependent *quantitative separation exponent* for the natural winding cutoff, with a corresponding conductor-by-conductor discrete/dense classification.

The algebraic norm and Dirichlet-pigeonhole arguments are standard arithmetic methods. The cyclotomic norm is used in other contexts, including [2]; the mathematical contribution here is the sharp combination of both estimates for a dynamically defined branch-value winding budget. No claim is made that the number-theoretic technique is new.

## Limitations

The result gives the correct power law and explicit but nonoptimal two-sided constants; it does not determine the exact asymptotic constant for \(q\ge4\), an optimal coefficient vector for a given budget, or a computable single-sheet singularity distribution. It distinguishes a dense set of branch *values* from singularities of any fixed branch. Bibliographic originality is based on the inspected sources and targeted mathematical searches, not an exhaustive proof of publication priority; equivalent statements in specialized Diophantine-approximation literature cannot be excluded absolutely.

## References

[1] B. Fiedler, *Scalar polynomial vector fields in real and complex time*, arXiv:2410.05043, first public version October 7, 2024; *Regular and Chaotic Dynamics* 30 (2025), 188–225, DOI 10.1134/S1560354725020030. Relevant parts: Sections 1.5, 1.6 and 1.8; Theorem 1.2.

[2] T. Do Duc, K. H. Leung and B. Schmidt, *Upper Bounds for Cyclotomic Numbers*, *Algebraic Combinatorics* 3 (2020), 39–53, DOI 10.5802/alco.86. Relevant material: arithmetic use of cyclotomic integer norms in Section 3, with a different mathematical objective.
