# Exact antipodal transport and a nonattained dodecahedral fidelity supremum

## Finding

For each of the five ordinary unweighted Platonic skeletons, let \(A\) be its real adjacency matrix, let \(U(t)=\exp(-itA)\), and define the one-excitation transfer probability from a vertex \(u\) to a distinct vertex \(v\) by \(F_{uv}(t)=|U(t)_{v,u}|^2\), where \(t\in\mathbb R\). Pretty good state transfer (PGST) means \(\sup_{t\in\mathbb R}F_{uv}(t)=1\); perfect state transfer (PST) requires equality at a finite time.

**Complete PGST classification.** Among all distinct ordered vertex pairs on all five Platonic graphs, PGST occurs *only* between opposite vertices in the cube and the icosahedron. Cube antipodes have PST at \(t=\pi/2\); icosahedral antipodes have PGST, never PST. No two distinct vertices of the tetrahedron, octahedron, or dodecahedron have PGST. Non-antipodal pairs in the four graphs with unique opposite vertices cannot have PGST.

**Quantitative antipodal statement.** The following are squared probabilities. All values are exact.

| Graph | Relevant vertex pair | \(\sup_{t\in\mathbb R}F_{uv}(t)\) | Supremum attained? |
| --- | --- | ---: | --- |
| Tetrahedron | Any distinct pair | \(1/4\) | Yes |
| Cube | Unique antipodes | \(1\) | Yes, PST |
| Octahedron | Unique antipodes | \(3/4\) | Yes |
| Dodecahedron | Unique antipodes | \(243/400\) | **No** |
| Icosahedron | Unique antipodes | \(1\) | **No**, PGST |

The previously known cube and cross-polytope/octahedral transfer facts are not asserted as new. The specific dodecahedral supremum and the five-graph PGST classification are the claims assessed here.

## Assumptions and scope

The Hamiltonian is precisely the uniform, onsite-potential-free, single-excitation adjacency matrix of each Platonic graph. No Laplacian dynamics, coins, edge weights, controls, disorder, many-particle effects, or thermal averaging are included. The dodecahedral value \(243/400\) is for its **antipodal pair**, not an assertion about maximal fidelity over all other pairs. For the tetrahedron, all distinct pairs are symmetry equivalent. The spectral and antipodal assertions use ordinary combinatorial graphs, not geometric interaction weights.

## Proof

### 1. Exact eigenspace decomposition and exclusion of other pairs

For an eigenvalue \(\lambda\), write \(E_\lambda\) for the orthogonal adjacency spectral projector. Each graph is vertex transitive, so \((E_\lambda)_{u,u}=m_\lambda/N\), with \(m_\lambda\) the eigenvalue multiplicity and \(N\) the vertex count. The exact spectra and the signs of the antipodal involution \(P\) in each eigenspace are:

| Graph | \(\lambda:(m_\lambda,\text{antipodal sign})\) |
| --- | --- |
| Tetrahedron | \(3:(1,\mathrm{N/A}),\ -1:(3,\mathrm{N/A})\) (no unique antipodal involution) |
| Cube | \(3:(1,+),\ -3:(1,-),\ 1:(3,-),\ -1:(3,+)\) |
| Octahedron | \(4:(1,+),\ -2:(2,+),\ 0:(3,-)\) |
| Dodecahedron | \(3:(1,+),\ -2:(4,+),\ 1:(5,+),\ \sqrt5:(3,-),\ -\sqrt5:(3,-),\ 0:(4,-)\) |
| Icosahedron | \(5:(1,+),\ -1:(5,+),\ \sqrt5:(3,-),\ -\sqrt5:(3,-)\) |

For the tetrahedron, both signs are not applicable because there is no unique antipodal involution; its two eigenvalue multiplicities are \(1\) and \(3\). All other signs satisfy \(PE_\lambda=\pm E_\lambda\), hence their antipodes are strongly cospectral. In each graph, the attached exact-arithmetic verifier builds \(E_\lambda=\prod_{\mu\ne\lambda}(A-\mu I)/(\lambda-\mu)\) and, exhaustively for every distinct non-antipodal pair, finds an eigenvalue with
\[
 \left|(E_\lambda)_{u,v}\right|<(E_\lambda)_{u,u}=m_\lambda/N.
\]
By the triangle and Cauchy--Schwarz inequalities, \(\sup_t F_{uv}(t)<1\) for such a pair. This finite exhaustive computation is a rigorous, exact check of the remaining 282 non-antipodal unordered pairs (including all six tetrahedral pairs); no floating-point threshold is used.

### 2. Amplitudes for representative distinct/antipodal pairs

Using \(U(t)=\sum_\lambda e^{-it\lambda}E_\lambda\) and the signs above, the amplitudes are
\[
\begin{aligned}
a_{K_4}(t)&=\tfrac14(e^{-3it}-e^{it}),\\
a_{Q_3}(t)&=i\sin^3t\quad\text{(up to an irrelevant global phase)},\\
a_O(t)&=\tfrac16(e^{-4it}+2e^{2it}-3),\\
a_D(t)&=\tfrac1{20}(e^{-3it}+4e^{2it}+5e^{-it}-4-6\cos(\sqrt5t)),\\
a_I(t)&=\tfrac1{12}(e^{-5it}+5e^{it}-6\cos(\sqrt5t)).
\end{aligned}
\]
For \(K_4\), the squared modulus is \(\sin^2(2t)/4\); for the cube it is \(\sin^6t\), yielding the first two rows. For the octahedron, with \(x=\cos(2t)\),
\[
36|a_O(t)|^2=4(x-1)^2(4x+5).
\]
The derivative is \(24(x-1)(2x+1)\), so the maximum on \([-1,1]\) is \(27\) at \(x=-1/2\). This gives \(3/4\) at \(t=\pi/3\), agreeing with the known cross-polytope case [2].

### 3. The dodecahedron's sharp *unattained* supremum

Set \(B(t)=e^{-3it}+4e^{2it}+5e^{-it}-4\). Then \(20a_D(t)=B(t)-6y\), where \(y=\cos(\sqrt5t)\). Since \(\sqrt5\) is irrational, \((t\bmod 2\pi,\sqrt5t\bmod 2\pi)\) is dense in the two-torus, so the required supremum equals the maximum with \(t\bmod2\pi\) and \(y\in[-1,1]\) independently variable. For each fixed \(t\), the function \(|B-6y|^2\) is a strictly convex quadratic in real \(y\), hence its maximum occurs at \(y=1\) or \(y=-1\).

At \(y=-1\), the triangle inequality gives \(|B+6|\le1+4+5+2=12\), so \(|B+6|^2\le144\). At \(y=1\), let \(x=\cos t\); direct expansion gives
\[
|B-6|^2=4(x-1)^2(32x^3+64x^2+76x+53).
\]
Its derivative is exactly \(40(x-1)(2x+1)(8x^2+4x+3)\). The quadratic is everywhere positive; the unique maximum on \([-1,1]\) is \(243\) at \(x=-1/2\). Consequently
\[
\sup_{t\in\mathbb R}|a_D(t)|^2=\frac{243}{400}.
\]
The value cannot be attained: attaining \(243>144\) requires both \(\cos t=-1/2\) and \(\cos(\sqrt5t)=1\), making \(t/(2\pi)\) a nonzero rational with denominator three and simultaneously \(\sqrt5t/(2\pi)\) an integer, impossible. Density still guarantees arbitrarily close approaches.

Since any dodecahedral antipodal PGST would require fidelity tending to one, \(243/400<1\) excludes it. Equivalently, its negative zero-eigenspace requires phase \(-1\), while the positive eigenvalues \(1\) and \(-2\) force mutually incompatible limits \(e^{-it}\to-1\) and \(e^{2it}\to-1\).

### 4. The icosahedron's proper pretty good transfer

For integers \(r\ge0\), define Pell pairs
\[
(p_0,q_0)=(2,1),\quad(p_1,q_1)=(9,4),\quad p_{r+2}=4p_{r+1}+p_r,\quad q_{r+2}=4q_{r+1}+q_r.
\]
Indeed, \(p_r+q_r\sqrt5=(2+\sqrt5)^{r+1}\), as follows from the recurrence and the first two pairs; taking field norms proves \(p_r^2-5q_r^2=(-1)^{r+1}\). Reduction of the same recurrence modulo two gives, for odd \(r\), even \(q_r\) and odd \(p_r\). At \(t_r=\pi q_r\),
\[
|a_I(t_r)|^2=\cos^4\!\left(\frac{\pi}{2(p_r+\sqrt5q_r)}\right)\longrightarrow1,
\]
which proves PGST constructively. PST cannot occur: the two positive-parity eigenvalues \(5,-1\) would have to agree in phase, while the two negative-parity eigenvalues \(\pm\sqrt5\) would have to share a phase opposite to the positive one. The former forces \(6t\in2\pi\mathbb Z\), the latter \(2\sqrt5t\in2\pi\mathbb Z\); irrationality makes their only simultaneous solution \(t=0\), which cannot provide the opposite phases.

## Verification

Run `python verify_spectral.py` and `python verify_coordinates.py` after extracting both files next to this document (dependencies: SymPy and NetworkX for the first; SymPy and NumPy for the second). The first reconstructs every graph's exact eigenvalues, eigenspace projector diagonals, antipodal projector signs, and every non-antipodal cospectrality exclusion, then symbolically checks both extremum polynomials and sixteen Pell samples; the infinite Pell formula is separately proved by the quadratic-unit identity in the proof. The second independently builds all five graphs from exact Euclidean coordinates rather than prebuilt graph constructors, verifies the spectra, and compares antipodal amplitudes against independent numerical diagonalizations at three separate times. The exact classification does not rely on numerical diagonalization; it is an independent corroboration.

## Relationship to prior work

The adjacency-quantum-transfer framework and cube perfect transfer belong to [1]. The octahedron is a six-vertex cross-polytope instance of prior cross-polytope transport work [2]; the \(3/4\) value is therefore not a priority claim. [3] develops a wider framework for pretty good transfer on cycles and related circulant graphs; its particular cyclic hypotheses do not establish the icosahedral result. [4] supplies general theory for peak transfer in continuous walks, with examined examples involving paths and smaller generic graphs; it is not the dodecahedral antipodal \(243/400\) supremum and does not classify this five-graph family. These are statement-level scope comparisons, not title-only searches.

## Limitations

This is a finite collection of unweighted graphs and a single-excitation unitary model. The dodecahedral numerical value is an exact **supremum, never an attained maximum**, and concerns the antipodal pair only. No assertion is made about global non-antipodal transfer maxima, state-transfer waiting-time optimality, decoherence, interactions, or uniqueness in all existing literature. The novelty assessment is limited to the identified, inspected public sources; independent validation has not been performed.

## References

[1] M. Christandl, N. Datta, A. Ekert, A. J. Landahl, *Perfect state transfer in quantum spin networks*, arXiv:quant-ph/0309131 (first posted 2003-09-17), https://arxiv.org/abs/quant-ph/0309131.
[2] D. I. Tsomokos, M. B. Plenio, I. de Vega, S. F. Huelga, *State Transfer in Highly Connected Networks and a Quantum Babinet Principle*, arXiv:0808.2261 (2008), https://arxiv.org/abs/0808.2261.
[3] H. Pal, B. Bhattacharjya, *Pretty Good State Transfer on Circulant Graphs*, arXiv:1607.03598 (2016), https://arxiv.org/abs/1607.03598.
[4] G. Coutinho, K. Guo, V. Schmeits, *Peak state transfer in continuous quantum walks*, arXiv:2505.11986 (2025), https://arxiv.org/abs/2505.11986.
