# Fractional Markovian repair and sharp positivity horizons for antagonistic complete networks

## Finding
Consider a complete network with disjoint antagonistic vertex blocks and strictly attractive edges everywhere else. Although its signed combinatorial Laplacian \(L\) is positive semidefinite, the ordinary heat semigroup \(e^{-tL}\) fails to preserve positivity for sufficiently small \(t>0\). Its *fractional powers* nevertheless admit an exact, nontrivial restoration of the Markov property.

Let \(N\ge3\). Choose pairwise disjoint nonempty blocks \(B_1,\ldots,B_r\subseteq\{1,\ldots,N\}\) of sizes \(2\le k_j<N\), with other vertices permitted as singleton blocks. For \(u\ne v\), assign edge conductance \(-a_j\) if \(u,v\in B_j\), and conductance \(+1\) otherwise. Suppose
\[
0<a_j<\frac{N}{k_j}-1,
\qquad \lambda_j=N-k_j(1+a_j)>0.
\]
Let \(L\) be the **signed row-sum** Laplacian \(L_{uv}=-w_{uv}\) for distinct vertices, and \(L_{uu}=\sum_{v\ne u}w_{uv}\). Put
\[
u_j=\frac{k_j}{N},\qquad q_j=1-u_j,
\qquad d_j=\frac{\lambda_j}{N}\quad(0<d_j<q_j<1),
\qquad \alpha_j=\frac{\log q_j}{\log d_j}\in(0,1),
\qquad \alpha_*=\min_{1\le j\le r}\alpha_j.
\]
Here and below fractional powers are the nonnegative **spectral** powers of \(L\), and all times and exponents are positive real numbers.

**Sharp fractional Markov boundary.** The family \(S_\alpha(t)=\exp(-tL^\alpha)\), \(t\ge0\), is a conservative positive semigroup (equivalently, \(-L^\alpha\) is a continuous-time Markov generator) if and only if
\[
\boxed{\quad0<\alpha\le\alpha_* .\quad}
\]
For every exponent in this range, all entries of \(S_\alpha(t)\) are **strictly positive** when \(t>0\). At \(\alpha=\alpha_*\) some direct jump rates within antagonistic blocks vanish, without losing strict heat-kernel positivity. For \(\alpha>\alpha_*\), the semigroup has negative entries for every sufficiently small positive time but becomes strictly positive after a finite, explicitly specified recovery time.

**Exact recovery horizon and endpoint norm.** Define
\[
F_j(\alpha,t)=u_j+q_j e^{-N^\alpha t}-e^{-\lambda_j^\alpha t}.
\]
For \(\alpha>\alpha_j\), there is exactly one root \(\tau_j(\alpha)>0\) of \(F_j(\alpha,t)=0\) apart from \(t=0\). Put \(\tau_j(\alpha)=0\) when \(\alpha\le\alpha_j\). Then, with \(\tau(\alpha)=\max_j\tau_j(\alpha)\),
\[
\boxed{\quad S_\alpha(t)\text{ is entrywise nonnegative precisely for }
 t=0\text{ or }t\ge\tau(\alpha).\quad}
\]
For \(\alpha>\alpha_*\), \(\tau(\alpha)>0\), and strict positivity holds for every \(t>\tau(\alpha)\). In counting-measure \(\ell^1\) and \(\ell^\infty\) norms, every \(t\ge0\) satisfies
\[
\boxed{\quad
\|S_\alpha(t)\|_{1\to1}=\|S_\alpha(t)\|_{\infty\to\infty}
=1+2\max_{1\le j\le r}\left(1-\frac1{k_j}\right)[-F_j(\alpha,t)]_+,\quad}
\]
where \([x]_+=\max\{x,0\}\). If \(\alpha>\alpha_j\), the maximum of \(-F_j(\alpha,t)\) over nonnegative times occurs uniquely at
\[
t_j^{\mathrm{peak}}(\alpha)=
\frac{\log\bigl(q_jN^\alpha/\lambda_j^\alpha\bigr)}{N^\alpha-\lambda_j^\alpha}.
\]
Thus the exact global peak of the \(\ell^1\) and \(\ell^\infty\) norms is obtained by replacing the bracketed quantity in the preceding display with \(-F_j(\alpha,t_j^{\mathrm{peak}})\), taking the maximum over active blocks \(\alpha>\alpha_j\), and assigning peak one if no block is active.

**Sharp near-critical and near-degenerate laws.** For each fixed antagonistic block, as \(\varepsilon\downarrow0\),
\[
\boxed{\quad
\tau_j(\alpha_j+\varepsilon)=
\frac{2N^{1-\alpha_j}}{k_j}\log\frac{N}{\lambda_j}\,\varepsilon
+O(\varepsilon^2).\quad}
\]
Writing \(J_* = \{j:\alpha_j=\alpha_*\}\), the complete network consequently has
\[
\tau(\alpha_*+\varepsilon)=A\varepsilon+O(\varepsilon^2),
\qquad
A=\max_{j\in J_*}\frac{2N^{1-\alpha_*}}{k_j}\log\frac{N}{\lambda_j}>0.
\]
There is also a sharp quadratic onset of transient norm amplification:
\[
\boxed{\quad
\sup_{t\ge0}\|S_{\alpha_*+\varepsilon}(t)\|_{\infty\to\infty}
=1+B\varepsilon^2+O(\varepsilon^3),\quad
B=\max_{j\in J_*}\left(1-\frac1{k_j}\right)
\frac{q_j}{u_j}\left(\log\frac{N}{\lambda_j}\right)^2>0.\quad}
\]
Finally, keeping \(N,k_j,\alpha>0\) fixed and letting the repulsive conductance approach the edge of positive semidefiniteness so that \(\lambda_j\downarrow0\), the block recovery horizon diverges with the exact constant
\[
\boxed{\quad\lambda_j^\alpha\tau_j(\alpha)\longrightarrow\log\frac{N}{k_j}.\quad}
\]

## Assumptions and scope
The integer \(r\ge1\) is finite; the antagonistic blocks are disjoint, have sizes at least two, and leave at least one vertex outside each individual block. Their total size is at most \(N\), and leftover vertices are treated as singletons. Edges **inside** an antagonistic block carry negative conductance, not negative sign-normalized graph degrees. The signed row-sum Laplacian can have negative edge contributions but is positive semidefinite under the displayed strict parameter bounds. No statement is made about the absolute-degree signed Laplacian, arbitrary signed graphs, arbitrary inter-block conductances, or the limiting singular case \(\lambda_j=0\).

The leading zero spectral eigenvalue is set to zero in every fractional power. The phrase "Markov generator" means a real matrix with nonnegative off-diagonal rates and zero row sums. All operator norms use counting measure; stochasticity is asserted only when entrywise nonnegativity holds. A time at which one within-block entry is zero is correctly treated as *nonnegative*, not strictly positive. The \(O(\cdot)\) constants in the onset laws depend on the fixed network; no graph-size-uniform assertion is intended.

## Proof
**1. Exact orthogonal projectors.** Let \(J\) be the all-ones matrix and let
\[
P_0=\frac{J}{N},\qquad
P_j=I_{B_j}-\frac{J_{B_j}}{k_j},\qquad
Q=I-P_0-\sum_{j=1}^rP_j.
\]
Here \(I_{B_j}\) and \(J_{B_j}\) are the identity and all-ones operators supported on \(B_j\). These are mutually orthogonal projections, and \(Q\) projects onto the block-constant vectors with global coordinate sum zero. Direct evaluation of \(Lx\) on each subspace gives
\[
LP_0=0,\qquad LP_j=\lambda_j P_j,
\qquad LQ=NQ.
\]
Thus
\[
\boxed{\quad L=NQ+\sum_j\lambda_jP_j,\quad
L^\alpha=N^\alpha Q+\sum_j\lambda_j^\alpha P_j.\quad} \tag{1}
\]
All \(\lambda_j>0\) and \(N>0\). The zero eigenspace has exactly the span of the all-ones vector, establishing positive semidefiniteness and a simple stationary mode. Formula (1) holds even when different eigenvalues coincide.

**2. Fractional Markov boundary.** For distinct coordinates \(u,v\in B_j\), applying (1) yields
\[
(L^\alpha)_{uv}
=\frac{N^\alpha}{k_j}
\left(q_j-d_j^\alpha\right).
\]
For distinct coordinates in different blocks (including singletons), it yields \((L^\alpha)_{uv}=-N^{\alpha-1}\). All row sums of \(L^\alpha\) vanish. A finite-dimensional matrix exponential \(e^{-tM}\) preserves the nonnegative cone for every \(t\ge0\) exactly when the off-diagonal entries of \(-M\) are nonnegative: necessity follows from the right derivative at \(t=0\), and sufficiency from shifting the diagonal and expanding the exponential into nonnegative matrix powers. Hence the condition is \(d_j^\alpha\ge q_j\) for every \(j\). Since \(0<d_j<q_j<1\), this is equivalent to \(\alpha\le\alpha_j\) for all \(j\), proving the stated sharp boundary.

**3. Exact heat-kernel entries.** Taking the exponential of (1) gives
\[
S_\alpha(t)=e^{-N^\alpha t}I+
(1-e^{-N^\alpha t})P_0+
\sum_j(e^{-\lambda_j^\alpha t}-e^{-N^\alpha t})P_j. \tag{2}
\]
All cross-block off-diagonal entries are \((1-e^{-N^\alpha t})/N>0\). Distinct entries \(u,v\in B_j\) are exactly \(F_j(\alpha,t)/k_j\). All diagonal entries are strictly positive for all finite \(t\ge0\), because \(S_\alpha(t)\) is positive definite and symmetric. Formula (2) gives row and column sums one.

Fix a block, write \(u=u_j\), \(q=q_j\), \(d=d_j^\alpha\), and \(s=N^\alpha t\). The scalar sign problem is
\[
F_j=u+qe^{-s}-e^{-ds},\qquad u+q=1.
\]
If \(d\ge q\), strict convexity of the exponential at the convex combination \(qs+u\cdot0\) gives \(u+qe^{-s}>e^{-qs}\ge e^{-ds}\) for \(s>0\). If \(0<d<q\), multiply by \(e^{ds}\):
\[
e^{ds}F_j=u e^{ds}+q e^{-(1-d)s}-1.
\]
This is a strictly convex function starting at zero, with derivative \(d-q<0\) at zero and tending to infinity. It has exactly one additional positive zero and is negative before that zero, positive after. This proves the exact recovery interval and strict positivity claims, including every boundary exponent. The derivative of \(-F_j\) has one zero in the active regime, namely the displayed \(t_j^{\mathrm{peak}}\), and switches from positive to negative there.

**4. Exact endpoint norms.** Every row of \(S_\alpha(t)\) sums to one and has a positive diagonal. A row in block \(B_j\) can have negative entries only in its \(k_j-1\) other coordinates within that block, and each such entry is \(F_j/k_j\). Hence its absolute row sum is
\[
1+2(k_j-1)\left[-\frac{F_j}{k_j}\right]_+
=1+2(1-k_j^{-1})[-F_j]_+.
\]
Singleton rows have absolute row sum one. Maximizing over rows proves the \(\ell^\infty\) norm identity; symmetry gives the \(\ell^1\) identity. Maximizing each single-block contribution separately proves the sharp global peak.

**5. Two near-critical rates.** Let \(\alpha=\alpha_j+\varepsilon\) with \(\varepsilon>0\) small, and set \(d=q-\delta\). By definition of \(\alpha_j\),
\[
\delta=q\left(1-d_j^{\varepsilon}\right)
=q\log(1/d_j)\,\varepsilon+O(\varepsilon^2).
\]
A uniform Taylor expansion near \(s=0\) gives
\[
F_j(s)=-\delta s+\frac{qu}{2}s^2
+O(\delta s^2+s^3).
\]
Its unique positive zero is therefore \(s=2\delta/(qu)+O(\delta^2)\), and its unique negative minimum is \(-\delta^2/(2qu)+O(\delta^3)\). Converting the dimensionless time by \(N^{-\alpha}\), substituting the expansion for \(\delta\), and multiplying the minimum by \(2(1-1/k_j)\) proves both blockwise coefficients. Since the number of blocks is finite, only the blocks in \(J_*\) can be active sufficiently near \(\alpha_*\), and maximizing their positive coefficients yields exactly the displayed \(A\) and \(B\), with the asserted remainder orders.

**6. Slowing near spectral degeneracy.** Fix \(N,k_j,\alpha>0\). For sufficiently small positive \(\lambda_j\), the block is active. At the positive recovery root, equation \(F_j=0\) reads
\[
e^{-\lambda_j^\alpha\tau_j}
=u_j+q_j e^{-N^\alpha\tau_j}.
\]
This root tends to infinity as \(\lambda_j\downarrow0\): in dimensionless time \(s=N^\alpha t\), the strictly convex crossing function \(u_j e^{d s}+q_j e^{-(1-d)s}-1\) converges at every fixed \(s>0\) to \(q_j(e^{-s}-1)<0\) as \(d=(\lambda_j/N)^\alpha\downarrow0\). Thus its unique positive root exceeds every fixed \(s\) for sufficiently small \(d\). Consequently \(e^{-N^\alpha\tau_j}\to0\). Taking logarithms in the equality gives \(\lambda_j^\alpha\tau_j\to-\log u_j=\log(N/k_j)\). This completes the proof.

## Verification
The accompanying `checker.py` builds the signed conductance Laplacian directly, computes its independent symmetric eigendecomposition, and tests the projector heat-kernel identity, the eigenvalue multiplicities, row stochasticity, Markov sign conditions, sharp endpoint norm, numerical positivity recovery, near-critical linear coefficient, and near-degenerate slowing constant. It returns `VERIFICATION_OK 2941` using Python 3 with NumPy and SciPy. Numeric eigensolvers can return a tiny nonzero round-off for the exact stationary eigenvalue, which the checker replaces by zero before taking small fractional powers. Finite testing supplements, and is not substituted for, the exact projector and scalar convexity proof.

## Relationship to prior work
Chen, Wang, Liu, Chen, Khong, Başar, Johansson and Qiu (first publicly posted 8 September 2020) establish the connection between the positive-semidefinite signed row-sum Laplacian and eventual exponential positivity, but do not give the above fractional-power threshold or exact positivity-time and norm laws for antagonistic block networks. Fontan and Altafini (2021) study pseudoinversion and eventual positivity of signed Laplacians, rather than their noninteger spectral powers. Arora (2021) treats qualitative eventual positivity for semigroups rather than sharp structured finite-dimensional phase boundaries.

Published fractional-graph heat classifications for **unsigned** complete multipartite networks obtain the universal transition at exponent one; their graph hypotheses exclude negative intra-block conductances, and their formulas do not imply the continuously varying, subunit sharp threshold here. Likewise, published all-step positivity regions for a fourth-order Gauss–Legendre **rational time-stepping method** on internally nonnegative weighted complete networks concern a different functional calculus and different allowed weights. The above statement does not claim novelty for spectral-projector algebra or the standard Metzler-generator criterion in isolation. Its claim is the exact signed-network fractional Markovization threshold together with the sharp recovery, amplification and singular-parameter laws.

## Limitations
This theorem applies only to the stated structured *signed row-sum* Laplacians, with strictly positive complementary eigenvalues. It does not classify arbitrary signed network diffusion, and does not analyze the zero-eigenvalue collision \(\lambda_j=0\) itself. The near-critical expansions hold for each fixed finite network, not uniformly over increasing size or collapsing spectral gaps. The smallest possible recovery time over perturbed network classes is not addressed. The cited literature comparisons do not establish absolute historical priority against unindexed or differently formulated work, and the independent audit has not been performed.

## References
1. W. Chen, D. Wang, J. Liu, Y. Chen, S. Z. Khong, T. Başar, K. H. Johansson and L. Qiu, *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity*, arXiv:2009.03581v1 (first public 2020-09-08), especially the connection between signed Laplacian semidefiniteness and eventual positivity. https://arxiv.org/abs/2009.03581
2. A. Fontan and C. Altafini, *On the properties of Laplacian pseudoinverses*, arXiv:2109.14587v1 (2021-09-29). https://arxiv.org/abs/2109.14587
3. S. Arora, *Locally Eventually Positive Operator Semigroups*, arXiv:2101.11386 (first public 2021-01-27). https://arxiv.org/abs/2101.11386
4. M. Benzi and I. Simunec, *Rational Krylov methods for fractional diffusion problems on graphs*, arXiv:2012.08389 (2020-12-15), particularly Section 3 on fractional graph operators. https://arxiv.org/abs/2012.08389
5. *A sharp positivity transition for fractional graph heat on complete multipartite networks*, public mathematical finding (2026), for the unsigned complete multipartite case. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1
6. *Independent sharp positivity thresholds for fourth-order diffusion on block-homogeneous complete networks*, public mathematical finding (2026), for the rational Gauss–Legendre endpoint method. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-independent-sharp-positivity-thresholds-for-fourth-order-diffusi--c547ef29de73
7. *Sharp entrywise spectral-window envelopes and the exact eventual-positivity horizon*, public mathematical finding (2026), for general fixed-window symmetric generators. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-entrywise-spectral-window-envelopes-and-the-exact-eventual--aea2a1d10bf1
