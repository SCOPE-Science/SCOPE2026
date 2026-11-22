# A four-sheet symmetric-group law for cyclic predecessors of a nonlinear open cellular automaton

## Finding
For each \(n\ge 1\), consider the binary cellular automaton on the indexed cyclic ring \(\mathbb Z/n\mathbb Z\) defined by
\[
(F_nx)_i=x_i\oplus x_{i+2}\oplus x_{i+1}(1\oplus x_{i+3})(1\oplus x_{i+2}\oplus x_{i+4}),
\]
where all arithmetic is in \(\mathbb F_2\), and every subscript is taken modulo \(n\). For \(y\in\mathbb F_2^n\), let \(\nu_n(y)=|\{x\in\mathbb F_2^n:F_nx=y\}|\).

**Theorem.** For every \(n\ge1\) and every \(y\),
\[
\nu_n(y)\in\{0,1,2,4\}.
\]
Moreover, if \(Y_n\) is uniform on \(\mathbb F_2^n\), there exists \(0<\rho<1\) such that, simultaneously for all four possible values,
\[
\begin{aligned}
\Pr\{\nu_n(Y_n)=0\}&=\tfrac38+O(\rho^n),\\
\Pr\{\nu_n(Y_n)=1\}&=\tfrac13+O(\rho^n),\\
\Pr\{\nu_n(Y_n)=2\}&=\tfrac14+O(\rho^n),\\
\Pr\{\nu_n(Y_n)=4\}&=\tfrac1{24}+O(\rho^n).
\end{aligned}
\]
Thus the proportion of cyclic outputs with a same-period predecessor tends to \(5/8\), even though the underlying two-sided infinite cellular automaton is globally four-to-one. The four probabilities are precisely the proportions of permutations in \(S_4\) with \(0,1,2,4\) fixed points.

## Assumptions and scope
No additional genericity, coprimality, or parity restrictions on the ring size or target word are imposed. The binary rule is the first four-to-one, non-bipermutive, locally eventually onto diameter-five example in the appendix of Haugland–Larsen–Omland–Rustad (2026). The latter paper establishes its infinite-configuration four-to-one property; the finite-ring multiplicity distribution above is a different invariant. Cyclic configurations are indexed; they are not identified under spatial rotation. The constant \(\rho\) is existential, arising from finite primitive stochastic matrices; no optimal numerical convergence rate is asserted.

## Proof
**1. Backward transfer and fixed points.** Put \(s=(a,c,d,e)=(x_{i+1},x_{i+2},x_{i+3},x_{i+4})\) and, for \(b\in\mathbb F_2\), define a transformation of the sixteen possible four-bit states by
\[
T_b(a,c,d,e)=\bigl(b\oplus c\oplus a(1\oplus d)(1\oplus c\oplus e),\ a,c,d\bigr).
\]
If the desired output at site \(i\) is \(b\), the first coordinate is the unique value of \(x_i\) compatible with that output and the four future inputs. Therefore a predecessor of a cyclic output \(y\) is exactly a fixed point of \(T_{y_0}\circ T_{y_1}\circ\cdots\circ T_{y_{n-1}}\) on the sixteen-state set, with the natural right-to-left evaluation convention. Overlapping state coordinates ensure a one-to-one correspondence even for rings of lengths below five.

**2. Complete finite transformation certificate.** Generate the transformation monoid \(\mathcal M\) from the identity under left composition by \(T_0,T_1\). Its exact 16-state-table enumeration, implemented in the standalone `check.py`, has 491 transformations: one of rank 16, two of rank 10, two of rank 8, six of rank 6, and 480 of rank 4. All sixteen binary words of length four induce rank-four transformations. The rank-four set is closed under both generators. It splits into two invariant kernel-partition classes, each containing 240 transformations. Each class comprises exactly ten distinct four-element images, and for each image there are all 24 bijections from its four kernel blocks to the image. Every image is a transversal of the four kernel blocks.

Each rank-four transformation therefore restricts on its own image to a permutation of four points. Consequently its fixed-point number can be only 0, 1, 2, or 4 (never 3). Lengths one, two and three have no three-predecessor output either: exhaustive exact enumeration gives distributions \((1,0,1,0)\), \((3,0,0,1)\), and \((1,6,1,0)\) in the order \((0,1,2,4)\). This proves the first assertion for every ring length.

**3. Primitive four-sheet chains.** Give each letter probability \(1/2\). Within either kernel class, the 240-state left-composition transition graph is strongly connected: exact forward and reverse breadth-first searches from one representative visit all 240 states. Both graphs have at the representative a closed walk of length two labeled `00` and another of length eleven labeled `01001001000`; their coprime lengths prove aperiodicity. Since all products of four letters already lie in these closed classes, the random transformation induced by a uniform length-\(n\) word converges exponentially to a convex combination of the unique stationary laws on these two finite primitive chains.

**4. Symmetry and limiting law.** Fix a kernel partition \(K\) and one four-element image \(I\). The 24 transformations with these \(K,I\) correspond bijectively to the permutations of the four kernel blocks. Relabeling the kernel blocks commutes with left composition by \(T_0,T_1\). Therefore the transition graph has a free \(S_4\)-action on each fixed-image fiber, and uniqueness of the stationary law on a primitive kernel class forces equal stationary weight on its 24 fiber elements. Because \(I\) is a transversal to \(K\), fixed points of a transformation are the fixed points of the induced four-point permutation. Among 24 permutations, exactly 9 have zero fixed points, 8 have one, 6 have two, and 1 has four. Thus the limiting multiplicity probabilities are \((9,8,6,1)/24\), independent of the stationary image-set weights and of the initial mixture of the two classes. Exponential mixing on the finite primitive chains gives the stated error term.

## Verification
Run `python3 check.py` (Python 3 standard library only). The program independently constructs both sixteen-state transfer transformations directly from the polynomial rule, enumerates their complete 491-element finite transformation monoid, checks all rank/image/kernel/transversality assertions, verifies both primitive component properties using forward/backward graph traversal and coprime return cycles, and reproduces the \(S_4\) fixed-point histogram for every one of the 20 image fibers. It independently enumerates the original cyclic update and compares its full target-by-target predecessor count against the transfer fixed-point formula for every ring size from 1 through 12. These finite checks are exhaustive in the specified finite domains, whereas the all-length and asymptotic steps are proved above by the transducer correspondence and finite primitive Markov-chain theorem.

## Relationship to prior work
Haugland, Larsen, Omland and Rustad (arXiv:2610.33131v1, October 23, 2026), Section 4 and Appendix B, establish openness, locally eventually onto behavior and global four-to-one degree for precisely this local rule, but do not supply its indexed finite-ring inverse-fiber multiplicity law. A publicly indexed finding titled *An eight-sheet symmetric-group law for periodic predecessors of a nonlinear cellular automaton* concerns a distinct eight-to-one nonlinear rule: it establishes an analogous \(S_8\) fixed-point distribution, not the present four-to-one rule, two kernel classes, 491-transformation certificate, or \(S_4\) law. Other publicly indexed work on two open five-neighbor rules establishes exact cyclic obstructions for different two-to-one local rules. The general use of finite-state transducers and finite Markov chains is classical; no novelty is claimed for those techniques themselves.

## Limitations
The result is specific to the displayed nonlinear five-neighbor polynomial and to same-period preimages on indexed rings. It does not classify the temporal orbits of the cellular automaton or assert a universal symmetric-group law for all open automata. The exponential rate is not optimized. Historical-priority uncertainty remains for literature not accessible through the inspected search sources, particularly unpublished computations and general monodromy formulations. Independent validation has not been performed.

## References
1. J. K. Haugland, N. S. Larsen, T. Omland, H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1 (first public October 23, 2026), https://arxiv.org/abs/2610.33131. The local rule appears in Appendix B; global finite-to-one is established in Theorem 4.4.
2. *An eight-sheet symmetric-group law for periodic predecessors of a nonlinear cellular automaton*, published-finding corpus record `2026/11/8/SCOPE-an-eight-sheet-symmetric-group-law-for-periodic-predecessors-of--0106d4eac899` (indexed summary consulted; underlying full record could not be retrieved).
3. *Exact cyclic image obstructions for two open five-neighbor binary automata*, published-finding corpus record `2026/11/8/SCOPE-exact-cyclic-image-obstructions-for-two-open-five-neighbor-binar--b4fa1671dcc9` (indexed summary consulted).
