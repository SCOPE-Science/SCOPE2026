# Exact odd-torus frustration energy and flux-branch rigidity for compact \(U(1)\) lattice gauge fields

## Finding

On every three-dimensional periodic rectangular lattice with side lengths \(L_1,L_2,L_3\geq2\), the negative-coupling pure compact \(U(1)\) plaquette energy has an exact finite-volume minimum. Let \(V=L_1L_2L_3\), \(A_{ij}=L_iL_j\), and
\[
H_g^-=g\sum_{x\in\Lambda}\sum_{1\leq i<j\leq3}\operatorname{Re}P_{ij}(x),\qquad g>0.
\]
Then
\[
\min_U H_g^-=-gV\sum_{i<j}c(A_{ij}),\qquad
c(A)=\begin{cases}1,&A\text{ even},\\ \cos(\pi/A),&A\text{ odd}.\end{cases}
\]
Every minimizer has *spatially constant* oriented plaquettes \(P_{ij}(x)\) independently for each orientation: they equal \(-1\) if \(A_{ij}\) is even, and otherwise equal one of the two phases \(\exp[i(\pi\pm\pi/A_{ij})]\). All choices of the two signs for the odd-area orientations are attained. For a fixed plaquette choice, link configurations modulo sitewise \(U(1)\) gauge transformations form a \(U(1)^3\) family of flat Wilson-loop holonomies. Hence there are precisely \(2^s\) discrete plaquette branches, where \(s\) is the number of odd products among \(A_{12},A_{13},A_{23}\).

In particular, the normalized minimum average plaquette on an odd cubic torus is \(W_{\min}=-\cos(\pi/L^2)\), and its energy excess over the formal infinite-volume all-minus-one bound is
\[
\Delta E=3gL^3[1-\cos(\pi/L^2)]
=\frac{3g\pi^2}{2L}+O_g(L^{-5})\quad(L\to\infty\text{ through odd integers}).
\]
For even \(L\), the corresponding excess is exactly zero.

## Assumptions and scope

The vertex set is \(\Lambda=\prod_{i=1}^3\mathbb Z/L_i\mathbb Z\), with each \(L_i\geq2\). An independent complex unit-modulus variable \(U_i(x)\) is attached to every positive directed link. The oriented plaquette is defined by
\[
P_{ij}(x)=U_i(x)U_j(x+e_i)\overline{U_i(x+e_j)}\overline{U_j(x)}\quad(i<j).
\]
There are no matter-field terms or twisted boundary conditions. In the convention \(H_g=-2\sum\operatorname{Re}P\) and negative gauge coupling \(K<0\) used by Bonati and Vicari, \(g=2|K|\) and \(H_g^-=KH_g\). The theorem is about the pure-gauge term at fixed finite volume, not the complete interacting gauge–matter ground state at nonzero matter coupling.

## Proof

**1. Exact plane constraint.** Fix an orientation \(i<j\) and a transverse coordinate. Multiplying all \(A=L_iL_j\) plaquettes in that periodic coordinate plane cancels every link with its reverse, hence
\[\prod_{a=1}^{A}P_a=1.\]
If \(A\) is even, the lower bound \(\sum_a\operatorname{Re}P_a\geq-A\) is achieved only when every plaquette equals \(-1\).

If \(A\) is odd, write \(P_a=-e^{i\delta_a}\), taking \(\delta_a\in[-\pi,\pi]\). The product constraint becomes \(\sum_a\delta_a\equiv\pi\pmod{2\pi}\); consequently \(\sum_a|\delta_a|\geq\pi\). The excess above the formal lower bound \(-A\) is \(\sum_a[1-\cos\delta_a]\). Since \(1-\cos t\) strictly increases on \([0,\pi]\), scale the nonnegative magnitudes \(|\delta_a|\) to a vector \(x_a\geq0\) with \(\sum x_a=\pi\); this does not increase the excess and decreases it strictly unless the original magnitudes already sum to \(\pi\). For any two entries with \(x+y\leq\pi\),
\[
[1-\cos x]+[1-\cos y]-2[1-\cos((x+y)/2)]
=2\cos((x+y)/2)[1-\cos((x-y)/2)]\geq0.
\]
On the simplex of \(A\geq3\) entries summing to \(\pi\), every nonuniform vector except a vertex has an unequal pair whose sum is strictly less than \(\pi\): choose a positive and a zero entry if zeros occur, or any unequal pair if all entries are positive. At a vertex \((\pi,0,\ldots,0)\), averaging the first two entries preserves the excess, but the resulting \((\pi/2,\pi/2,0,\ldots)\) has a pair admitting a strict improvement. Hence no nonuniform vector minimizes the excess. Compactness supplies a minimizer, so its unique magnitude pattern is \(x_a=\pi/A\) for all \(a\). Equality in the initial absolute-value inequality forces all \(\delta_a\) to have the same sign, giving precisely the two equal-plaquette phases \(P_a=e^{i(\pi\pm\pi/A)}\). The minimum plane sum is \(-A\cos(\pi/A)\).

**2. The global lower bound is attained.** Every \(i,j\) plane gives the preceding lower bound. There are \(L_k\) parallel planes of that orientation, with \(k\) the remaining coordinate, so adding the bounds yields \(-gV\sum_{i<j}c(A_{ij})\). To construct links attaining all bounds simultaneously, for each \(i<j\) choose an integer \(k_{ij}\) equal to \(A_{ij}/2\) if \(A_{ij}\) is even and to either \((A_{ij}-1)/2\) or \((A_{ij}+1)/2\) otherwise. Set \(\phi_{ij}=2\pi k_{ij}/A_{ij}\). On the ordered \((i,j)\) coordinate pair, use angular link contributions
\[
a_i^{ij}(x)=-\phi_{ij}x_j,\qquad
 a_j^{ij}(x)=\phi_{ij}L_jx_i\,\mathbf1_{\{x_j=L_j-1\}},
\]
with all other contributions zero. Exponentiate the sum of these contributions over the three coordinate pairs to define \(U_i(x)\). An elementary seam computation shows that each oriented \(ij\)-plaquette has curl \(\phi_{ij}\) modulo \(2\pi\), including the wraparound plaquette (where a multiple of \(2\pi k_{ij}\) appears). Contributions from other pairs have zero \(ij\)-curl. Thus all three plane bounds are simultaneously sharp.

**3. Rigidity across transverse slices.** Any minimizer must attain every plane bound. Its \(ij\)-plaquette therefore depends at most on the third coordinate, and for odd \(A_{ij}\) can only take the two displayed signs. The elementary-cube Bianchi identity states that the oriented product of the six face plaquettes equals one. Write its three transverse increments in principal angles. An increment is zero for an even-area orientation, and is zero or \(\pm 2\pi/A_{ij}\) for an odd-area orientation. Since each odd \(A_{ij}\geq9\), the absolute sum of the three increments is less than \(2\pi\); hence their sum is exactly zero, not merely zero modulo \(2\pi\). Each of the three increments depends on a different single coordinate. Their sum being zero for every lattice vertex forces each increment to be a constant, and summation around its periodic coordinate forces that constant to be zero. Therefore the sign is independent of the transverse coordinate. This proves global plaquette uniformity and precisely \(2^s\) plaquette patterns.

**4. Residual gauge degrees of freedom.** For a fixed plaquette pattern, divide any two realizing link fields. The quotient has plaquettes identically one. Parallel transport around contractible lattice loops is consequently trivial. Choose a spanning tree and gauge its links to one; the remaining independent transport is exactly the three commuting cycle holonomies around the coordinate torus, each an arbitrary element of \(U(1)\). Thus the mod-gauge set is \(U(1)^3\) on each discrete plaquette branch.

**5. Cubic asymptotics.** If all three sides are odd and equal to \(L\), all three oriented plaquette areas equal the odd number \(L^2\), giving the stated energy. Expanding \(1-\cos z=z^2/2+O(z^4)\) at \(z=\pi/L^2\) yields the \(L^{-1}\) leading correction and the \(O_g(L^{-5})\) remainder.

## Verification

The standalone dependency-free script `check_flux.py` constructs the link phases, checks every oriented plaquette including all periodic seams, and confirms the exact energy for multiple even, odd, and mixed-parity rectangular tori and all allowed flux-branch sign choices. It passes 5,892 individual plaquette tests. These finite tests support the construction but do not substitute for the all-size proof above.

## Relationship to prior work

Bonati and Vicari (2026) introduce the negative-coupling compact \(U(1)\) lattice Abelian Higgs model, define the plaquette Hamiltonian in equations (3)–(4), and explicitly exhibit a fully frustrated \(-1\)-plaquette background compatible with periodic **even** sizes in equation (20). Their analysis does not give the exact odd-periodic-area minimum, all rectangular parity cases, or the associated ground-state branch classification. Standard periodic-flux quantization and seam-gauge constructions already appear in lattice gauge field treatments and are used here as known ingredients; the new assertion is the sharp global negative-coupling minimization and rigid classification in three dimensions. The negative-coupling \(SU(N)\) Wilson study of Li and Meurice (2005) treats a different non-Abelian group, not this \(U(1)\) odd-torus optimization.

## Limitations

The result assumes strictly periodic link variables, side lengths at least two, a pure compact \(U(1)\) plaquette energy with a common positive coefficient, and exactly three spatial dimensions. It does not solve the scalar-coupled Hamiltonian for \(J>0\), establish finite-temperature phase transitions, compare twisted boundary sectors, or quantify thermal fluctuations. Flux integers attached to constant plaquette branches should not be mistaken for globally invariant topological labels of arbitrary compact-link configurations: monopole processes may connect them away from the minimum-energy manifold. Although targeted literature checks did not reveal an equivalent theorem, implicit coverage in older broad lattice-gauge literature cannot be excluded without independent subject-expert review.

## References

1. C. Bonati and E. Vicari, *Lattice spin systems coupled to a compact U(1) gauge field with negative gauge coupling favoring frustration*, arXiv:2611.03837v1 (first public 2026-11-02), https://arxiv.org/html/2611.03837v1, especially Sections II.1 and III.1.
2. L. Li and Y. Meurice, *Lattice gluodynamics at negative \(g^2\)*, Phys. Rev. D 71, 016008 (2005), https://doi.org/10.1103/PhysRevD.71.016008. Its \(SU(2)\)/\(SU(3)\) theory is distinct.
3. G. Douzas, *Gauge theories*, subsection “A uniform field on the torus,” https://georgedouzas.github.io/posts/fundamentals-of-theoretical-physics/part-ii-06-gauge-theories.html, which describes standard uniform-flux quantization and a seam construction.
