# Sharp reentrant invertibility and open triple inverse fibers in a two-cell spiking map

## Finding
Consider the deterministic, exact-real two-cell discrete map introduced by Buscarino, Famoso and Fortuna [1], at the coefficients used for their numerical study:
\[
 F_{T,\alpha}(z)=(1-T)z+T\bigl(M\Theta_\alpha(z)+b\bigr),\qquad
 M=\begin{pmatrix}17/10&-1\\1&17/10\end{pmatrix},\quad
 b=\begin{pmatrix}-3/10\\3/10\end{pmatrix},\quad
 \Theta_\alpha(z)=\begin{pmatrix}\tanh(\alpha z_1)\\\tanh(\alpha z_2)\end{pmatrix}.
\]
The state space is the entire real plane; \(T>0\) is the Euler step and \(\alpha>0\) is the sigmoid gain.

**Theorem (complete global reversibility diagram).**

1. If \(0<T<1\), the map is a \(C^\infty\) diffeomorphism of \(\mathbb R^2\) onto \(\mathbb R^2\), for every \(\alpha>0\).
2. At \(T=1\), it is a \(C^\infty\) diffeomorphism onto the **proper open parallelogram** \(b+M(-1,1)^2\); targets in that parallelogram have one predecessor and all other targets have none.
3. If \(T>1\), it is a global \(C^\infty\) diffeomorphism of the plane **if and only if**
\[
 \boxed{\alpha\le \frac{10(T-1)}{17T}.}
\]
At equality every finite Jacobian is nonsingular, but the inverse is not globally Lipschitz. If the strict reverse inequality holds, there is a nonempty open set of output states, each with **at least three distinct regular predecessors**. Critical points exist, separating regions of positive and negative Jacobian determinant.
4. For every \(T\ne1\), the map is proper, has topological degree \(+1\), and every regular target has a finite, **odd** number of real predecessors. Thus the three-or-more inverse fibers in part 3 are not isolated accidents.

For \(0<\alpha<10/17\), increasing \(T\) beyond one first produces multiple inverse branches and then restores global invertibility at
\[
 T_*(\alpha)=\frac{1}{1-17\alpha/10}.
\]
For \(\alpha\ge10/17\), no step \(T>1\) restores invertibility. In particular, the gain \(\alpha=1/2\) has the exact restoration boundary \(T_*=20/3\), although a documented moderate-step example \((T,\alpha)=(23/10,1/2)\) already has an open three-preimage region.

## Assumptions and scope
The map is exactly equations (4)–(5) of [1] with \((\mu,s,i_1,i_2)=(7/10,1,-3/10,3/10)\), interpreted on the unrestricted \(\mathbb R^2\), without clipping, finite-precision rounding, stochastic forcing, or an imposed absorbing box. Every use of *inverse* means a one-step predecessor in this real plane, not an entire backward orbit within a forward attractor. *Regular target* means that the Jacobian is nonsingular at each of its preimages. At \(T\ne1\), properness makes the regular fiber finite. The topological-degree statement uses the standard orientation of \(\mathbb R^2\).

## Proof
**1. Properness and degree.** Since the two coordinates of \(\Theta_\alpha\) lie strictly between \(-1\) and \(1\), the nonlinear term \(M\Theta_\alpha(z)+b\) is bounded uniformly in \(z\). For \(T\ne1\),
\[
 \|F_{T,\alpha}(z)\|\ge |1-T|\,\|z\|-T C
\]
for a finite constant \(C\). Thus \(F_{T,\alpha}\) is proper. The homotopy \((1-T)z+\tau T(M\Theta_\alpha(z)+b)\), \(0\le\tau\le1\), is uniformly proper. Its degree is that of the linear map \((1-T)I\), namely \(+1\), since the dimension is two. Consequently every regular target has a nonempty finite fiber and its signed Jacobian count is \(+1\). In particular its fiber cardinality is odd.

**2. Exact Jacobian and all nonsingular regimes.** Put \(d_j=\alpha\operatorname{sech}^2(\alpha z_j)\in(0,\alpha]\). Direct differentiation gives
\[
 DF_{T,\alpha}(z)=\begin{pmatrix}
 1-T+17Td_1/10&-Td_2\\
 Td_1&1-T+17Td_2/10
 \end{pmatrix}.
\]
For \(0<T<1\), its determinant is
\[
 (1-T+17Td_1/10)(1-T+17Td_2/10)+T^2d_1d_2>0.
\]
The proper local diffeomorphism therefore has exactly one inverse point for each target, by the degree computation, and is a global diffeomorphism.

At \(T=1\), \(F_{1,\alpha}=M\Theta_\alpha+b\). Since \(\Theta_\alpha\) diffeomorphically maps \(\mathbb R^2\) onto \((-1,1)^2\) and \(\det M=389/100>0\), the image and single-predecessor property follow exactly.

For \(T>1\), set \(q=T-1\). Then
\[
 \det DF_{T,\alpha}(z)
 =\bigl(q-17Td_1/10\bigr)\bigl(q-17Td_2/10\bigr)+T^2d_1d_2.
\]
If \(q\ge17T\alpha/10\), both factors in the first product are nonnegative and the final term is strictly positive. The degree argument again gives a diffeomorphism of the plane onto itself. For an independent injectivity check, if two distinct states had the same image, writing their difference as \(\delta\) and their sigmoid-output difference as \(\eta\) would give \(q\delta=TM\eta\), and hence
\[
 q\,\delta\cdot\eta=\frac{17T}{10}\|\eta\|^2.
\]
Strict monotonicity of \(\tanh\) and its derivative bound \(\alpha\) imply \(\delta\cdot\eta>\|\eta\|^2/\alpha\) for distinct states, contradicting \(q\ge17T\alpha/10\).

**3. Nonuniform critical boundary.** At \(q=17T\alpha/10\), the above Jacobian determinant is strictly positive at every finite state. Along \(z=(0,R)\), however, \(d_1=\alpha\) and \(d_2\to0\) as \(R\to\infty\), and the Jacobian tends to
\[
 \begin{pmatrix}0&0\\ T\alpha&-q\end{pmatrix},
\]
a rank-one matrix. The least singular value therefore tends to zero; the derivative of the smooth inverse has unbounded operator norm along the corresponding output states. A globally Lipschitz inverse is impossible.

**4. Open triple fibers beyond the boundary.** Suppose \(q<17T\alpha/10\). Along \(z=(0,R)\),
\[
 \lim_{R\to\infty}\det DF_{T,\alpha}(0,R)
 =q(q-17T\alpha/10)<0,
\]
whereas \(\det DF_{T,\alpha}(R,R)\to q^2>0\). A nonempty open region of negative local orientation exists, as does a positive region; continuity also guarantees a nonempty critical set. Choose a negative-orientation regular *preimage* \(z_0\). The inverse-function theorem maps a neighborhood of \(z_0\) diffeomorphically onto an open set of targets. By Sard's theorem, choose within that set a regular target \(y\) for the entire map. One predecessor of \(y\) has local degree \(-1\). As the total degree is \(+1\), at least two further predecessors of positive orientation are required. The three regular inverse branches persist on a common neighborhood of \(y\). This establishes the open three-or-more-preimage claim and proves the sharp converse.

**5. Exact rational sign witness.** For \((T,\alpha)=(23/10,1/2)\), at \(z=(0,6)\) one has \(d_1=1/2\), \(d_2=(1/2)\operatorname{sech}^2(3)\). The positive first five terms of the hyperbolic-cosine power series give \(\cosh(3)>9005/896>10\), so \(0<d_2<1/200\). Direct substitution yields
\[
 \det DF_{23/10,1/2}(0,6)
 =-\frac{1703}{2000}+\frac{104121}{20000}d_2
 <-\frac{3301879}{4000000}<0.
\]
Thus the negative orientation is demonstrated by exact rational inequalities, without any floating-point assumption. The reentrant boundary at gain \(1/2\) follows by solving \(T-1=17T/20\), giving \(T=20/3\). All claimed cases follow.

## Verification
Run `python3 check_inverse.py` using only the Python standard library. It checks the determinant identity at reproducible parameter-state samples, the positivity of all specified diffeomorphic regimes, the rational Taylor certificate just above, and three distinct numerically reconstructed inverse branches at the rational moderate-step example. It also checks the vanishing determinant along the critical boundary. The completed checker reports **1,105 finite diagnostics passed**. These calculations illustrate and detect implementation errors; the global statements and exact parameter boundaries are proved by the displayed inequalities, properness, local inversion and degree, not by finite sampling.

## Relationship to prior work
The originating full-text paper [1] develops the two-cell sigmoid Euler map and reports numerical equilibrium, bifurcation, spiking, bursting and hardware behavior; it gives the Jacobian for local stability, but not the all-parameter global inverse-fiber classification. Two subsequent public technical findings for exactly this map concern a global-attractor step threshold [2] and a primitive-two-cycle obstruction [3]. Their mathematical conclusions do not determine the one-step inverse multiplicities, reentrant reversibility, or the nonsingular-but-nonuniform critical boundary. Standard noninvertible-planar-map theory [4] explains degree, critical curves, and inverse-sheet regions in general; the sharp \((T,\alpha)\) boundary and its exceptional endpoint use the specific sigmoid, coupling matrix and saturation structure here.

## Limitations
The open inverse-fiber region is guaranteed to have **at least** three predecessors, not exactly three everywhere; no complete upper bound or full caustic topology is asserted. Numerical roots at a sample target do not constitute a rigorous census for that target. Surjectivity and inverse statements for \(T\ne1\) apply to the entire real plane, and should not be construed as claims about predecessor sets confined to a compact chaotic attractor. Reversibility here does not imply stability or bounded forward orbits. The theorem neither establishes spiking statistics nor quantifies physical inverse-reconstruction robustness under measurement noise. Publication priority has been checked against the identified sources but cannot exclude unindexed equivalent results.

## References
[1] A. Buscarino, C. Famoso, L. Fortuna, *Bifurcations in a new two-cell spiking map: a numerical and experimental study*, Nonlinear Dynamics 111 (2023), 20361–20375. First published 2023-09-27. DOI: https://doi.org/10.1007/s11071-023-08897-7 . Full authorized open text: https://www.iris.unict.it/bitstream/20.500.11769/596535/2/Bifurcations%20in%20a%20new%20two%20cell%20spiking%20map%20a%20numerical%20and%20experimental%20study.pdf .

[2] *A sharp global-attractor threshold for the two-cell sigmoid spiking map*, publicly available mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-global-attractor-threshold-for-the-two-cell-sigmoid-spik--8f9bdcdcb9f6 .

[3] *Sharp prime-two exclusion and a saturated repelling cycle in a two-cell spiking map*, publicly available mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-prime-two-exclusion-and-a-saturated-repelling-cycle-in-a-t--d40768f347f0 .

[4] *Noninvertible maps*, Scholarpedia, https://www.scholarpedia.org/article/Noninvertible_maps (general background on critical sets and inverse multiplicity).
