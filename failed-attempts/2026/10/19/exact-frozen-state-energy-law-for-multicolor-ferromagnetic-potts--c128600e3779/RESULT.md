# Exact frozen-state energy law for multicolor ferromagnetic Potts ladders

## Finding
Fix integers \(q\ge 3\) and \(n\ge 3\). In the zero-temperature single-site recoloring dynamics of the ferromagnetic \(q\)-state Potts model on the circular two-leg ladder \(C_n\square K_2\), the strictly frozen configurations admit a complete classification, an exact microcanonical energy polynomial, and a Gaussian frozen-state energy law.

Let \(J>0\), let each vertex have one of \(q\) colors, and put \(H(s)=J\sum_{\{v,w\}\in E}\mathbf 1\{s_v\ne s_w\}\). A configuration is *strictly frozen* when changing any one spin to any different color strictly increases \(H\). Then precisely one of the following holds:

1. All rungs are monochromatic, with common rung color \(a_i\), and the cyclic word \((a_1,\ldots,a_n)\) has no isolated letter (every maximal monochromatic run has length at least two); or
2. Both rows are individually constant, with two different colors (there are exactly \(q(q-1)\) such states).

Define integer polynomials \(L_0(v)=2\), \(L_1(v)=1\), and \(L_k(v)=L_{k-1}(v)-vL_{k-2}(v)\) for \(k\ge2\). The frozen-state energy polynomial \(Z_{n,q}(z)=\sum_{s\;\mathrm{strictly\ frozen}}z^{H(s)/J}\) satisfies, **for every** \(q\ge3\) and \(n\ge3\),

\[
Z_{n,q}(z)=q(q-1)z^n+L_n(-(q-1)z^2)+(q-1)L_n(z^2).
\]

The exact polynomial for the number \(W\) of color changes on the upper row is

\[
F_{n,q}(u)=q(q-1)+L_n(-(q-1)u)+(q-1)L_n(u).
\]

Write \(\lambda_q=(1+\sqrt{4q-3})/2\), \(\rho_q=(\lambda_q-1)/(2\lambda_q-1)\), and \(\nu_q=\lambda_q(\lambda_q-1)/(2\lambda_q-1)^3\). Under the uniform distribution on strictly frozen configurations, as \(n\to\infty\) for fixed \(q\ge3\),

\[
\frac{1}{2n}\log Z_{n,q}(1)\longrightarrow\frac12\log\lambda_q,
\qquad \frac{W}{n}\xrightarrow{\mathbb P}\rho_q,
\qquad \frac{W-n\rho_q}{\sqrt n}\Longrightarrow\mathcal N(0,\nu_q).
\]

Moreover the frozen-energy density obeys \(H/(2Jn)\xrightarrow{\mathbb P}\rho_q\), and \((H/J-2n\rho_q)/(2\sqrt n)\Longrightarrow\mathcal N(0,\nu_q)\). The probability of the \(q(q-1)\) two-color constant-row states is asymptotic to \(q(q-1)\lambda_q^{-n}\). For \(q=3\), \(\lambda_3=2\), \(\rho_3=1/3\), and \(\nu_3=2/27\).

## Assumptions and scope
The graph is the simple Cartesian product \(C_n\square K_2\) for \(n\ge3\): each vertex has exactly three distinct neighbors, two in its own row and one across its rung. Colors are labeled, vertices are labeled, and rotations or global permutations of colors are **not** quotiented out. The energy counts each undirected edge once. Every allowed recoloring is a change of one site's color to any of the other \(q-1\) colors. At zero temperature, energy-neutral moves are allowed by the usual Glauber update convention, so the term strictly frozen deliberately excludes neutral directions. Neither reaching probabilities nor positive-temperature equilibration are asserted.

The variable \(z\) counts energy in integer units of \(J\); \(u\) marks one horizontal color-change edge per rung pair (not both parallel leg edges). The two-colored constant-row states have \(H/J=n\) and \(W=0\). For the all-monochromatic-rung family, \(H/J=2W\).

## Proof
**1. Local stability.** If a vertex has current color \(a\) and a proposed different color \(b\), only its three incident edges change. The energy change equals \(J(N_a-N_b)\), with \(N_c\) the number of its three neighbors of color \(c\). All recolorings have positive cost if and only if \(N_a\ge2\). Indeed \(N_a=2\) or \(3\) gives strict superiority, whereas \(N_a\le1\) leaves some other neighbor color with at least the same multiplicity. This includes the boundary cases where the other two neighbor colors differ.

**2. Geometry.** Write the two rung colors \(s_i,t_i\). If \(s_i\ne t_i\), neither site gets a like-colored neighbor from its rung, so both horizontal neighbors of each site must agree with that site's color. Hence \((s_{i-1},t_{i-1})=(s_i,t_i)=(s_{i+1},t_{i+1})\). Iterating around the connected cycle proves that every rung is this same bichromatic ordered pair. Conversely each such constant-row state has two like-colored horizontal neighbors at each site, and is strictly frozen.

If no rung is bichromatic, write \(s_i=t_i=a_i\). Each site then has one like-colored rung neighbor. It has another like-colored neighbor exactly when \(a_{i-1}=a_i\) or \(a_{i+1}=a_i\). This is equivalent to the cyclic color word having no singleton run. These states are strictly frozen and the two classes are disjoint, exhausting all configurations.

**3. Polynomial transfer and exact spectrum.** For the monochromatic-rung class, consider directed memory states \((a,b)\in\{1,\ldots,q\}^2\). Set

\[
T_{(a,b),(b,c)}(u)=\mathbf 1\{a=b\ \text{or}\ b=c\}\,u^{\mathbf 1\{b\ne c\}},
\]

with all other entries zero. A closed walk of length \(n\) in this directed-pair transfer records exactly a cyclic \(n\)-letter word with no singleton run and weights each horizontal color change by \(u\). Thus the monochromatic-rung polynomial is \(\operatorname{tr}T(u)^n\).

For a nonzero eigenvalue \(x\) with right eigenvector components \(e_a\) at states \((a,a)\), the components \(d_{ab}\) at \((a,b)\), \(a\ne b\), satisfy \(xd_{ab}=e_b\). The equations at diagonal states become

\[
x(x-1)e_a=u\sum_{b\ne a}e_b.
\]

On the one-dimensional constant-color subspace this gives \(x^2-x-(q-1)u=0\); on the \((q-1)\)-dimensional zero-sum subspace, \(x^2-x+u=0\). All other eigenvalues vanish. The characteristic polynomial is therefore

\[
x^{q(q-2)}\bigl(x^2-x-(q-1)u\bigr)\bigl(x^2-x+u\bigr)^{q-1}.
\]

The identity follows for generic \(u\) where the two factors have nonzero distinct roots, and hence by polynomial identity for every \(u\). The trace of a positive power is the sum of powers of its eigenvalues, including algebraic multiplicity even when a Jordan block occurs. Since \(L_n(v)\) is the sum of the \(n\)th powers of the two roots of \(x^2-x+v\),

\[
\operatorname{tr}T(u)^n=L_n(-(q-1)u)+(q-1)L_n(u).
\]

Adding the \(q(q-1)\) exceptional stripes gives \(F_{n,q}(u)\). Replacing \(u\) with \(z^2\) in the monochromatic-rung contribution and weighting each exceptional stripe by \(z^n\) gives \(Z_{n,q}(z)\).

**4. Thermodynamic and Gaussian laws.** For positive \(u\) near \(1\), the uniquely dominant eigenvalue of the transfer is \(\lambda_q(u)=(1+\sqrt{1+4(q-1)u})/2\). At \(u=1\), the other root of its quadratic has smaller absolute value, both roots of \(x^2-x+1\) have absolute value one, and the exceptional contribution is constant. Thus there exists a complex neighborhood of \(u=1\) and a \(\theta\in(0,1)\) in which the uniformly frozen state's moment generating function is

\[
\mathbb E\,e^{tW}=\left(\frac{\lambda_q(e^t)}{\lambda_q(1)}\right)^n\bigl(1+O(\theta^n)\bigr),
\]

uniformly for complex \(t\) close to zero. Derivative evaluation gives

\[
\left.\frac{d}{dt}\log\lambda_q(e^t)\right|_{t=0}=\rho_q,
\qquad
\left.\frac{d^2}{dt^2}\log\lambda_q(e^t)\right|_{t=0}=\nu_q>0.
\]

The first two cumulants and Chebyshev's inequality give the law of large numbers. Expanding the analytic log moment-generating function at arguments \(t/\sqrt n\) gives the Gaussian limit by convergence of moment-generating functions. The asymptotic \(F_{n,q}(1)\sim\lambda_q^n\) gives the entropy and exponential rarity of constant unequal rows. On nonexceptional states \(H/J=2W\); the probability of exceptional states decays exponentially, so the energy limits follow by Slutsky's theorem.

## Verification
The accompanying standalone Python 3 program `verify_potts_ladder.py` enumerates the original spin Hamiltonian directly, testing all recolorings independently of the transfer-matrix construction. Across twelve parameter pairs \((q,n)\), it exhaustively tests \(2{,}123{,}582\) labeled configurations and compares the complete wall-count and direct-energy histograms with the recurrence formulas, while separately checking the geometric classification. It independently constructs the unweighted directed-pair transfer matrix for \(q=2,3,4,5,6\) and checks 40 nonzero-power trace identities, including formal powers for lengths one and two. The program prints `VERIFY_OK` on success. The finite tests corroborate the exact polynomial, while the infinite-volume limits rely on the proof above.

For \(q=3\) the direct frozen-state counts at lengths \(n=3,4,5,6\) are \(9,21,39,75\). No Monte Carlo estimate or finite search is used as proof for unbounded \(n\).

## Relationship to prior work
Olejarz, Krapivsky and Redner (2013) investigate zero-temperature \(q\)-state Potts coarsening in two dimensions and identify nontrivial static domain mosaics, pinned junctions and blinker behavior. Their results motivate asking which of those structures survive on a three-regular width-two cylinder, but their square-lattice dynamics and asymptotics neither provide nor imply the present full \(q,n\) frozen-state energy polynomial. Derrida and Zeitak (1996) derive time-dependent domain-size distributions for the one-dimensional Potts chain; these concern dynamical sampling and do not enumerate locally stable cylinder states. Biggs and Shrock (2000) analyze antiferromagnetic ground-state chromatic polynomials on square strips; proper coloring and ground-state degeneracy differ fundamentally from ferromagnetic single-spin local-minimum counting.

The \(q=2\) circular Ising-ladder case and general transfer-matrix methods are pre-existing; the stated claim concerns the complete multicolor \(q\ge3\) classification with its two geometric classes, exact energy polynomial, and asymptotic wall statistics. A literature search did not identify an equivalent all-color theorem, but absence from the searched literature is not a proof of novelty.

## Limitations
The result does not calculate the probability that any frozen state is reached from a specified initial law, does not treat energy-neutral recurrent classes, and does not extrapolate to two-dimensional strips of growing width. The uniform measure on frozen states is not the long-time law of the kinetic model. Bibliographic coverage is incomplete for older specialized finite-width metastability enumerations, which could contain an equivalent formula. The Gaussian result takes \(n\to\infty\) with fixed integer \(q\ge3\), not a joint growing-color limit.

## References
- J. Olejarz, P. L. Krapivsky, and S. Redner, *Zero-Temperature Coarsening in the 2d Potts Model*, arXiv:1305.1038 (first posted 2013-05-05), https://arxiv.org/abs/1305.1038.
- B. Derrida and R. Zeitak, *Distribution of domain sizes in the zero temperature Glauber dynamics of the 1 D Potts model*, arXiv:cond-mat/9606042 (first posted 1996-06-07), https://arxiv.org/abs/cond-mat/9606042.
- N. Biggs and R. Shrock, *T=0 Partition Functions for Potts Antiferromagnets on Square Lattice Strips with (Twisted) Periodic Boundary Conditions*, arXiv:cond-mat/0001407 (first posted 2000-01-27), https://arxiv.org/abs/cond-mat/0001407.
