# Joint arm-and-particle characters and the Young-lattice quotient of star configurations

## Finding
For integers \(m\ge3\) and \(k\ge4\), let \(F_k(S_m)\) be the space of ordered configurations of \(k\) pairwise distinct labeled points on an equal-length topological star with \(m\) branches. Branch permutations \(\alpha\in S_m\) and particle permutations \(\beta\in S_k\) commute. Write \(a_d\) and \(c_d\) for their respective numbers of cycles of length \(d\). Define
\[
F(\alpha,\beta)=\prod_{d:c_d>0}d^{c_d}c_d!\binom{c_d+a_d-1}{a_d-1}.
\]
Any factor with \(c_d>0=a_d\) is declared zero; an empty product is one. If \(\beta\) fixes no particle, define \(B(\alpha,\beta)=0\). Otherwise choose any fixed particle \(q\) and put
\[
B(\alpha,\beta)=c_1F(\alpha,\beta|_{[k]\setminus\{q\}}).
\]
The notation is independent of the chosen fixed particle because it depends only on cycle type. Then the complete first-homology character is
\[
\boxed{\operatorname{tr}\big((\alpha,\beta)|H_1(F_k(S_m);\mathbb Q)\big)=1-F(\alpha,\beta)+(a_1-1)B(\alpha,\beta).}
\]
The space is connected; its integral homology is torsion-free and concentrated in degrees zero and one. Its first Betti number (included as a known consistency check, not the new contribution) is
\[
1+\frac{(k+m-2)!}{(m-1)!}(km-2k-m+1).
\]

There is also a precise classification of the **simultaneous symmetry quotient**: \(F_k(S_m)/(S_m\times S_k)\) is homotopy equivalent to the graph whose vertices are the integer partitions of \(k\) and of \(k-1\) into at most \(m\) positive parts, with an edge between \(\mu\vdash k-1\) and \(\lambda\vdash k\) exactly when \(\lambda\) covers \(\mu\) in Young's lattice. If \(p_m(n)\) denotes the count of such partitions and \(d(\mu)\) the number of distinct positive part sizes, its first Betti number is
\[
\boxed{r_m(k)=1+\sum_{\substack{\mu\vdash k-1\\\ell(\mu)\le m}}\big(d(\mu)+\mathbf1_{\ell(\mu)<m}\big)-p_m(k-1)-p_m(k).}
\]
In particular the quotient is a tree for \(k\le4\) and contains a cycle for every \(k\ge5\); its first cyclic case has \(r_m(5)=1\) for every \(m\ge3\). The previous two- and three-particle cases serve only as checks, not claims of priority.

For \(k=4\), write \(f=a_1\), \(t=a_2\), \(u=a_3\), and \(v=a_4\). A particularly explicit specialization is the five-value character table as the particle cycle type runs through \((1^4),(2,1^2),(2^2),(3,1),(4)\):
\[
1+f(f+1)(f+2)(3f-7),\quad 1+2tf(f-3),\quad 1-4t(t+1),\quad 1-3u,\quad 1-4v.
\]

## Assumptions and scope
An \(m\)-arm star is a metric tree formed by joining \(m\) equal closed intervals at one endpoint; its other endpoints are leaves. Its center and the labeled particles are allowed to coincide only when the particle at the center is unique; any two particles may never coincide. \(F_k\) is the ordinary **ordered, collision-free** configuration space (not a sink configuration space). The symmetry permutes isometric arms and independently relabels particles. We calculate ordinary homology and the topology of a finite-group orbit space, not equivariant cohomology or an integral module decomposition.

The graph model has two vertex types. An \(A\)-vertex records, for every arm, the ordered word of its particle labels from center toward leaf, with no particle at the center. A \(B\)-vertex records the unique particle at the center together with the corresponding ordered arm words of the remaining labels. Each \(B\)-vertex has one graph edge to the \(A\)-vertex obtained by inserting the center label at the inward end of each possible arm. Let this graph be \(\Gamma_{m,k}\). Its graph edges correspond to a unique central particle moving slightly along the selected arm, with the orders of all other particles unchanged.

## Proof
**1. Equivariant graph model.** Partition the configuration space into radial-order strata according to the ordered arm words and whether a particle occupies the center. Each stratum is given by strict linear radial inequalities (with possible closed leaf endpoints), hence is contractible. Its only codimension-one incidence with another stratum is the approach of the innermost particle to the center, yielding the stated \(B\)-to-\(A\) adjacency. Simultaneous, symmetry-invariant collars of these strata give a homotopy-colimit graph model. On every fixed-point locus for a subgroup of \(S_m\times S_k\), the stratum-coordinate conditions remain convex: a symmetry fixes a configuration exactly when its radial coordinates satisfy the corresponding equalities. Consequently the collar/nerve construction gives an equivariant homotopy equivalence \(F_k(S_m)\simeq\Gamma_{m,k}\), valid also on all subgroup-fixed sets, and hence induces the indicated homotopy equivalence on orbit spaces. The same construction can be seen geometrically by choosing equally spaced radial coordinates for each word and linearly moving the center label inward along the selected arm on every graph edge. Equal arm lengths make all choices invariant under arm permutations.

**2. Connectivity and counts.** For \(m\ge3\), any pair of consecutive labels in an arm can be exchanged by moving one temporarily through either of two other arms; using these moves, all word distributions are joined. More formally, successive transfers of each innermost label through the center and a spare third arm generate adjacent transpositions of the ordered labels and permit any prescribed arm allocation. Thus the graph is connected. Distributing \(k\) distinguishable labels as \(m\) ordered arm words gives \(k!\binom{k+m-1}{m-1}\) vertices of type \(A\). Choosing the center label and distributing the other \(k-1\) gives \(k!\binom{k+m-2}{m-1}\) vertices of type \(B\). Every \(B\) has \(m\) incident edges, and no edge is reversed by the symmetry because it connects two different types. The Euler characteristic yields the displayed Betti number; graph homology is integral free and vanishes above degree one.

**3. Simultaneous fixed-word enumeration.** Suppose \(\alpha\) and \(\beta\) have cycle counts \(a_d\), \(c_d\). For a word distribution to be fixed, each particle cycle of length \(d\) must occupy an arm cycle of exactly the same length: otherwise distinct labels would need to occupy the same point or one label would occupy two arms. For each \(d\), choose a multiset of \(c_d\) particle cycles distributed among \(a_d\) arm cycles, order the cycles in their chosen arm words, and choose one of \(d\) starting phases per particle cycle. This contributes \(d^{c_d}c_d!\binom{c_d+a_d-1}{a_d-1}\) configurations. The product is exactly the number of fixed \(A\)-vertices. A fixed \(B\)-vertex requires a fixed center particle, giving \(B(\alpha,\beta)\) such vertices. Each fixed \(B\)-vertex has one fixed incident edge for each fixed arm; hence the fixed edge count is \(a_1B\). Since the graph is connected, the cellular Lefschetz trace identity \(\operatorname{tr}(H_0)-\operatorname{tr}(H_1)=\#A^{(\alpha,\beta)}+\#B^{(\alpha,\beta)}-\#E^{(\alpha,\beta)}\) yields the character formula. Specializing the five conjugacy types of \(S_4\) gives the displayed table.

**4. Orbit graph and sharp transition.** Under \(S_k\), the labels in an arm word are irrelevant; under \(S_m\), only the multiset of arm occupancies remains. Thus \(A\)-orbits correspond to partitions of \(k\) of length at most \(m\), \(B\)-orbits to partitions of \(k-1\) of length at most \(m\), and edge orbits to a partition cover. The graph is connected as a quotient of a connected graph. From a partition \(\mu\), increasing one of its distinct positive parts or adding a new part of size one if fewer than \(m\) parts are present gives all neighboring rank-\(k\) partitions; no different operation gives the same neighbor. Its degree is therefore \(d(\mu)+\mathbf1_{\ell(\mu)<m}\), proving the rank formula by \(E-V+1\). A direct enumeration of partitions of \(k\le4\) gives a tree. For every \(k\ge5\), the six vertices
\[
\mu_1=(k-2,1),\ \mu_2=(k-3,2),\ \mu_3=(k-3,1,1),\quad
\lambda_1=(k-2,2),\ \lambda_2=(k-3,2,1),\ \lambda_3=(k-2,1,1)
\]
form the simple cycle \(\mu_1-\lambda_1-\mu_2-\lambda_2-\mu_3-\lambda_3-\mu_1\); all have at most three parts. There is therefore a nonzero first quotient homology class for every \(m\ge3\), \(k\ge5\). Directly at \(k=5\), the rank formula gives one for every \(m\ge3\). Since the quotient is a graph, it has no higher homology and is a wedge of its first-Betti-number many circles.

## Verification
The complete standalone script `verify.py` is included with recorded output `verify_output.txt`. It independently enumerates every ordered-word configuration, every elementary transfer edge, checks connectivity by graph search, enumerates every arm and label permutation for \((m,k)=(3,2),(3,3),(4,4),(3,5)\), and compares exact fixed \(A\)-, \(B\)-, and edge counts against the derived formulas. The program also checks the integer partition cover graph, independently identifies actual edge orbits by their occupancy pairs, and verifies the averaged character equals the quotient's first Betti number. The full-group checks comprise 12, 36, 576, and 720 cases, respectively. These bounded computations corroborate the uniform proof but do not substitute for the all-parameter statements.

## Relationship to prior work
Ghrist (first public version May 5, 1999) established general topology of graph configuration spaces; these spaces on a star have a known graph homotopy type and first Betti numbers. Lütgehetmann (2014, §3.3) computed the particle-permutation module and the graph model, and later investigated representation stability under arm permutations. Wawrykow (2024 preprint; subsequently published) established generators and relations for the particle-stabilization modules. Those results motivate the refinement but do not state the simultaneous arbitrary arm-and-particle character or the two-level Young-partition quotient and its sharp five-particle transition. The established two- and three-particle characters are not asserted novel; the present scope is all \(k\ge4\). No definitive priority claim is made against literature not inspected.

## Limitations
The character determines the rational representation, not a canonical integral \(S_m\times S_k\)-lattice. The theorem does not describe braid-group presentations, spectral decompositions of transfer operators, or non-equal-arm metric symmetries. The Young-graph quotient concerns ordinary topological orbit spaces and their homotopy types, not Borel equivariant homology. The proof assumes finite \(m\ge3\) and \(k\ge4\). Published work might contain an equivalent formulation not detected by the checks.

## References
- R. Ghrist, *Configuration spaces and braid groups on graphs in robotics*, arXiv:math/9905023 (first submitted 1999-05-05).
- D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539 (first submitted 2004-10-25).
- D. Lütgehetmann, *Configuration Spaces of Graphs*, master's thesis (2014), https://userpage.fu-berlin.de/luetge/pdfs/masters-thesis-luetgehetmann.pdf; §3.3.
- D. Lütgehetmann, *Representation Stability for Configuration Spaces of Graphs*, arXiv:1701.03490 (first submitted 2017-01-12).
- N. Wawrykow, *Homology Generators and Relations for the Ordered Configuration Space of a Star Graph*, arXiv:2401.13821 (first submitted 2024-01-24).
