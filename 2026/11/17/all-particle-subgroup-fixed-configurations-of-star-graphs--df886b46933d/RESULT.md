# All-particle subgroup-fixed configurations of star graphs

## Finding

Let \(S_m\) be the topological star consisting of \(m\geq3\) closed unit intervals meeting only at their common initial point. Let \(H\leq\mathfrak S_m\) act by permuting whole arms, preserving each distance from the center. For \(k\geq0\), let \(\operatorname{UConf}_k(S_m)\) be the space of unordered sets of exactly \(k\) distinct points, with \(\operatorname{UConf}_0\) a singleton.

Write \(f\) for the number of singleton arm orbits of \(H\), and \(t_1,\dots,t_q\geq2\) for the sizes, with multiplicities, of the nonsingleton arm orbits. Denote by \(S_f\) the union of the \(f\) fixed arms and the center; \(S_0\) is the one-point space. For \(a\geq0\) set
\[
P_a=\{(r_1,\dots,r_a):0<r_1<\cdots<r_a\leq1\},\qquad P_0=\{\ast\}.
\]

**Theorem (all-particle fixed-space decomposition).** There is a natural homeomorphism
\[
\boxed{\displaystyle
\operatorname{UConf}_k(S_m)^H\ \cong\
\coprod_{\substack{a_1,\ldots,a_q\geq0\\\sum_{j=1}^q t_j a_j\leq k}}
\operatorname{UConf}_{k-\sum_jt_ja_j}(S_f)\times\prod_{j=1}^qP_{a_j}.}
\]
Every \(P_a\) is contractible. When \(f=0\), the factors \(\operatorname{UConf}_n(S_0)\) are nonempty precisely for \(n=0,1\); all other indicated summands are understood to be empty. Each nonempty summand is a path component.

Let \(b_i(k)=\operatorname{rank} H_i(\operatorname{UConf}_k(S_m)^H;\mathbb Z)\), with ordinary (not reduced) singular homology. For \(f\geq1\) the complete integral homology is torsion-free, zero in degrees \(i\geq2\), and its all-particle generating functions are
\[
\boxed{\displaystyle
\sum_{k\geq0}b_0(k)z^k
=\frac1{1-z}\prod_{j=1}^q\frac1{1-z^{t_j}},\qquad
\sum_{k\geq0}b_1(k)z^k
=\frac{(1-z)^{f-1}-1+(f-1)z}{(1-z)^f}
\prod_{j=1}^q\frac1{1-z^{t_j}}.}
\]
If \(f=0\), then
\[
\boxed{\displaystyle
\sum_{k\geq0}b_0(k)z^k=(1+z)\prod_{j=1}^q\frac1{1-z^{t_j}},\qquad b_i(k)=0\ (i\geq1).}
\]
For each \(k\), the fixed space is consequently a finite disjoint union of contractible spaces and spaces homotopy equivalent to finite wedges of circles. Its **entire homeomorphism type**, not only its Betti numbers, is determined by the multiset of arm-orbit sizes, independently of the abstract isomorphism type of \(H\).

For example, let \(m=5\) and let \(H\) swap two arms and fix the other three. Then \(f=3\), \((t_1)=(2)\), and at \(k=4\) the fixed space has exactly three components, with circle ranks \(6\), \(1\), and \(0\). Hence it is homotopy equivalent to \((\bigvee^6S^1)\sqcup S^1\sqcup\{\ast\}\). This mixed connectedness and cycle count is stronger information than an equivariant Lefschetz number.

## Assumptions and scope

The branch lengths are identified with \([0,1]\), with the central point at radius zero. The only group action considered is permutation of whole arms, never permutation of particle labels. Particles are unordered but distinct; a point at an arm endpoint is permitted, while two points at the common center are forbidden. The topological configuration space is given its usual quotient topology from the ordered collision-free space. All group actions are finite because \(H\leq\mathfrak S_m\). All formulas include \(k=0\). Factors corresponding to no particles are singletons. The classification does not concern positive minimum-clearance constraints, unequal arm lengths, or general finite trees.

## Proof

**1. Orbit-radial rigidity.** Write \(o\) for the central vertex. Every point of \(S_m\setminus\{o\}\) is uniquely an arm label together with its radius in \((0,1]\). An \(H\)-invariant finite configuration has the same set of occupied radii in every arm of a given \(H\)-orbit: if one arm contains a point at radius \(r\), transitivity of the arm orbit forces the corresponding points at radius \(r\) in all its arms. Conversely, any such synchronized selection of radii is invariant. In a nonsingleton arm orbit of cardinality \(t_j\), each selected radius consumes exactly \(t_j\) distinct particles.

**2. Component invariance and topology.** For a nonsingleton orbit \(j\), let \(a_j\) be the number of its occupied radii. This integer is locally constant on the \(H\)-fixed configuration space: around any collision-free finite configuration, sufficiently small disjoint neighborhoods of its particle positions preserve the number of particles in each open arm, and invariance makes those counts equal across the orbit. In particular, an entire orbit of \(t_j\geq2\) particles cannot pass through the central vertex, since at radius zero all \(t_j\) positions would coincide there. Thus \((a_1,\dots,a_q)\) is constant on connected components.

Remove all points on nonsingleton arm orbits from an invariant configuration. The remaining \(k-\sum_jt_ja_j\) particles are an arbitrary unordered collision-free configuration on \(S_f\), with the center included. The removed points are uniquely encoded by an increasing radius list in each \(P_{a_j}\). The union map from the displayed product to the fixed space is a continuous bijection with continuous inverse, because sorting distinct radii, restricting to individual arms, and adjoining disjoint finite configurations are continuous on every locally constant occupancy stratum. The finitely many strata are open and closed in the fixed space. This establishes the claimed homeomorphism. Each \(P_a\) is convex under linear interpolation and hence contractible.

**3. Ordinary star factors.** For \(f=0\), the space \(S_f\) is a point, giving exactly the two singleton possibilities for residual particle number zero or one. For \(f=1,2\), \(S_f\) is an interval, so each ordinary unordered configuration space is contractible. For \(f\geq3\), the established radial-tree configuration-space theorem of Farley and Sabalka shows that every \(\operatorname{UConf}_n(S_f)\) is connected and has the homotopy type of a finite graph, with free first-homology rank
\[
R_f(n)=\sum_{i=2}^{f-1}
\left[\binom{n+f-2}{n-1}-\binom{n+f-i-1}{n-1}\right]\qquad(n\geq1).
\]
Equivalently, for \(f\geq3\), \(n\geq0\),
\[
R_f(n)=1+(f-2)\binom{n+f-2}{f-1}-\binom{n+f-2}{f-2},
\]
using the ordinary convention that a binomial coefficient is zero when its lower index exceeds a nonnegative upper index. The second formula gives \(R_f(0)=0\). Since an ordinary connected graph is homotopy equivalent to a wedge of circles, each summand of the decomposition is connected with first Betti number \(R_f(n)\), and all its higher homology vanishes. For \(f=1,2\) take \(R_f(n)=0\).

**4. Exact all-particle series.** The ordinary star factors are nonempty for every \(n\geq0\) when \(f\geq1\), so one obtains one component for each allowed nonnegative integer vector \((a_j)\). The generating function for such vectors, including the residual particle count, is \((1-z)^{-1}\prod_j(1-z^{t_j})^{-1}\). For \(f\geq3\), the binomial generating series gives
\[
\sum_{n\geq0}R_f(n)z^n=
\frac{1}{1-z}+(f-2)\frac{z}{(1-z)^f}-\frac{1}{(1-z)^{f-1}}
=\frac{(1-z)^{f-1}-1+(f-1)z}{(1-z)^f}.
\]
The final rational function is zero for \(f=1,2\) as well. Multiplication by \(\prod_j(1-z^{t_j})^{-1}\) yields the asserted first-Betti series. When \(f=0\), the only residual counts are zero and one, yielding \((1+z)\prod_j(1-z^{t_j})^{-1}\) for components and zero positive-degree homology. This completes the classification.

## Verification

The included standard-library-only program `verify_star_fixed.py` constructs a finite graph spine for ordinary unordered star configurations. Its A-vertices are nonnegative arm occupancy vectors totaling \(k\); its B-vertices are vectors totaling \(k-1\), representing one central particle. Each B-vertex is joined to its A-neighbors obtained by adding one particle to a single arm. It computes the geometric fixed subgraph under several arm-permutation generating sets, with fixed edges restricted to individually fixed arms, and independently counts all connected components and graph cycle ranks. Those results are compared against the orbit-size decomposition and the closed binomial-rank formula.

The script checks 245 combinations with \(3\leq m\leq7\) and \(0\leq k\leq6\), including transitive cyclic and dihedral groups, nontransitive subgroups, group actions without fixed arms, and trivial actions. The recorded output is in `verification_output.txt` and includes `STAR_FIXED_GRAPH_SPINE_PASS instances=245`. The five-arm, four-particle transposition example is checked separately. These computations are finite corroboration and do not replace the all-parameter proof. Replay using `python3 verify_star_fixed.py` from the directory containing the two files.

## Relationship to prior work

Farley and Sabalka's first public 25 October 2004 preprint, specifically the radial-tree result in Section 4 and Corollary 4.2, supplies the ordinary connected-star graph homotopy type and Betti rank. Neither the ordinary theorem nor this rank is claimed new. Ghrist's earlier graph-configuration results supply a broader nonequivariant background. Rourke and Sanderson (2000) study finite-group-equivariant labelled configurations in manifolds and representation spaces, including variable-cardinality configurations; their theorems are not the fixed-cardinality star-arm fixed-locus decomposition above. An and Maciążek (2021) treat graph braid group generators and star-group presentations, not the geometric fixed spaces of unordered arm-permutation actions.

The closest publicly indexed related star results give the *arm action on ordinary homology* (including a full rational character) or *arm-orbit quotients of ordered configurations*. A rational character can recover fixed-point Euler characteristics under suitable hypotheses but does not determine the numbers of connected components and independent circles in each geometric subgroup-fixed space. Quotients are not fixed loci, and labeled configurations are not unordered ones. A prior two-particle classification for arbitrary finite trees includes the \(k=2\) specialization; the new assertion concerns the uniform **all-particle** star homeomorphism, especially \(k\geq3\), and both all-degree generating functions. An equivalent statement in previously unindexed literature remains a residual priority risk.

## Limitations

The decomposition is specialized to equal-length stars with group actions permuting arms radially. It does not determine natural integral equivariant homology *modules* of the entire configuration space, homotopy types of orbit quotients, or higher-branching-tree fixed spaces at arbitrary particle number. The graph-spine computational test verifies selected finite parameters only; the infinite result follows from orbit-radial rigidity and the cited ordinary radial-tree theorem. Independent mathematical review has not been performed. The historical novelty assessment is provisional; in particular, generalized equivariant configuration frameworks may encode the result implicitly.

## References

1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv `math/0410539v1`, first public 25 October 2004; *Algebraic & Geometric Topology* 5 (2005), 1075–1109, Section 4, Corollary 4.2, https://arxiv.org/abs/math/0410539 and https://msp.org/agt/2005/5-3/agt-v5-n3-p09-s.pdf.
2. C. P. Rourke and B. J. Sanderson, *Equivariant configuration spaces*, *Journal of the London Mathematical Society* 62 (2000), 544–552, https://wrap.warwick.ac.uk/id/eprint/828/1/WRAP_Rourke_Equivariant_configuration.pdf.
3. B. H. An and T. Maciążek, *Geometric presentations of braid groups for particles on a graph*, *Communications in Mathematical Physics* 384 (2021), 1109–1140, https://doi.org/10.1007/s00220-021-04095-x, especially Section 3.2.
4. *Hook-Schur homology and the first symmetric cycle for particles on star graphs*, published mathematical record `2026/11/1/SCOPE-hook-schur-homology-and-the-first-symmetric-cycle-for-particles--9c57549dcfff`, especially Finding and Proof sections. The referenced prior theorem is the ordinary \(\mathfrak S_m\)-homology representation, not the geometric fixed-space decomposition.
5. *Sharp stabilization of symmetry quotients of ordered star-graph configuration spaces*, published mathematical record `2026/11/8/SCOPE-sharp-stabilization-of-symmetry-quotients-of-ordered-star-graph--b2f11a665451`, especially Finding and Proof. It concerns ordered configurations and their orbit quotients.
