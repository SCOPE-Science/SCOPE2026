# Sharp eight-parameter loss of graded singleton-type reconstruction in the homogeneous two-graph

## Finding

Let \(\mathcal H\) be the countable universal homogeneous *two-graph*: its ternary relation \(R\) holds of unordered triples, and every four distinct points contain an even number of \(R\)-triples. For a finite named induced two-graph \(T\subseteq\mathcal H\), define the *singleton-type grade polynomial*
\[
P_T(z)=\sum_{q\in S_1^{\mathrm{na}}(T)}z^{\gamma(q)},\qquad
\gamma(q)=\#\{\{a,b\}\subseteq T:R(x,a,b)\in q\},
\]
where \(S_1^{\mathrm{na}}(T)\) is the set of complete nonalgebraic singleton types over the individually named parameters of \(T\). For every \(n=|T|\ge1\), there are exactly \(2^{n-1}\) such types.

**Finite sharp reconstruction and collision classification.** For all \(n\le7\), the polynomial \(P_T\) determines the isomorphism class of \(T\) among \(n\)-point two-graphs. At \(n=8\), the \(243\) isomorphism classes yield exactly \(219\) distinct polynomials: \(198\) singleton fibers, \(18\) two-member fibers and \(3\) three-member fibers. Thus the first failure occurs at exactly eight named parameters. Moreover, in each of the \(21\) nonsingleton fibers, all members have different sorted vertex incidence sequences
\[
D_T=\operatorname{sort}\Bigl(\bigl(\#\{\{a,b\}\subseteq T\setminus\{v\}:R(v,a,b)\}\bigr)_{v\in T}\Bigr).
\]
Consequently, the pair \((P_T,D_T)\) reconstructs all two-graphs with at most eight points.

An explicit three-member collision is obtained from the graph-on-seven-vertices masks \(39516,39527,43885\) under the encoding in the next section. Their common polynomial is
\[
\begin{aligned}
&2z^8+4z^9+6z^{10}+12z^{11}+14z^{12}+16z^{13}+20z^{14}\\
&\qquad+16z^{15}+14z^{16}+12z^{17}+6z^{18}+4z^{19}+2z^{20}.
\end{aligned}
\]
Their respective sorted vertex incidences are
\[
(8,8,10,10,11,11,13,13),\quad
(8,9,10,10,11,11,12,13),\quad
(9,9,10,10,11,11,12,12),
\]
proving the three parameter structures nonisomorphic. They even have *distinct* Seidel characteristic polynomials (see Verification), so the collision is not a pre-existing cospectral identification.

## Assumptions and scope

A finite *two-graph* is a three-uniform relation \(R\) on a finite set such that the sum of its incidence indicators on every four-set is zero modulo two. Choose a designated old vertex \(0\); write the remaining vertices as \(1,\ldots,n-1\). Set \(g_{ij}=1\) precisely when \(R(0,i,j)\). The parity law then forces, for any \(i,j,k\ne0\),
\[
R(i,j,k)=g_{ij}\oplus g_{ik}\oplus g_{jk},
\]
with \(\oplus\) meaning addition modulo two. Thus any simple graph \(G\) on \(1,\ldots,n-1\) uniquely encodes an \(n\)-point two-graph: the designated point is isolated in the associated switching representative.

A *mask* is the nonnegative integer having the edge indicators \(g_{ij}\) as bits in lexicographic pair order \((1,2),(1,3),\ldots,(6,7)\) for \(n=8\). For other \(n\), use the same lexicographic order truncated appropriately. The grade counts coherent triples that contain the new point and two *distinct named* points; it does not count all triples in the resulting larger structure or all formulas in the complete type. The parameters remain individually named when counting types; they are considered up to unordered two-graph isomorphism only in the reconstruction question.

## Proof

**Type normal form.** Let \(x\) be a new point and put \(s_i=R(x,0,i)\in\{0,1\}\). The parity condition on \(\{x,0,i,j\}\) gives
\[
R(x,i,j)=g_{ij}\oplus s_i\oplus s_j.
\]
Conversely, for every binary vector \(s=(s_1,\ldots,s_{n-1})\), these equations define a valid one-point extension: take the graph on old points whose representative isolates \(0\), add \(x\) with no edge to \(0\) and an edge to old point \(i\) exactly when \(s_i=1\), then define every coherent triple by odd edge parity. These extensions belong to the age of \(\mathcal H\) and are realized there. Homogeneity in the finite relational language makes their atomic diagrams complete types. Distinct binary vectors differ on an atomic formula. Hence there are exactly \(2^{n-1}\) nonalgebraic singleton types.

Let \(\delta(s)\) be the subset of edges \(\{i,j\}\) among \(1,\ldots,n-1\) with \(s_i\ne s_j\). The exact grade polynomial is therefore
\[
\boxed{P_T(z)=\sum_{s\in\{0,1\}^{n-1}}z^{|s|+|E(G)\triangle\delta(s)|},}
\]
where \(\triangle\) denotes symmetric difference. This is an intrinsic isomorphism invariant because it counts intrinsic, grade-refined types; the chosen anchor only affects its computation.

**Exhaustive isomorphism quotient.** For each \(n\le8\), enumerate all \(2^{\binom{n-1}{2}}\) simple graphs \(G\) in the designated-anchor normal form. Given one such graph, form its entire isomorphism orbit by selecting each possible new anchor \(r\) and permuting all other \(n-1\) vertices. The transformed descendant has edge indicators
\[
g^{(r)}_{uv}=g_{uv}\oplus g_{ru}\oplus g_{rv},
\]
where the original full graph includes the isolated anchor \(0\). This enumerates *exactly* the normal forms of all relabelings of the same two-graph: every relabeling has some preimage of the new anchor and a permutation of its other labels, and each enumerated transformation preserves the odd-edge-parity triple relation. Therefore identifying every code in these orbits is a complete, exhaustive isomorphism test, not a sample.

For each previously unseen orbit representative, compute the displayed polynomial using all \(2^{n-1}\) vectors \(s\). The resulting isomorphism-class totals for \(n=1,\ldots,8\) are
\[
(1,1,2,3,7,16,54,243),
\]
and the distinct-polynomial totals are
\[
(1,1,2,3,7,16,54,219).
\]
At eight points the fiber-size distribution is \((198,18,3)\) for sizes \(1,2,3\), respectively. A separate algorithm enumerates every rooted graph *without quotienting by isomorphism* and independently finds exactly \(219\) different eight-point polynomials.

**Separation and complete certificates.** From each representative graph compute all coherent triples using odd edge parity, then count for each old vertex how many coherent triples contain it. Sort the eight counts. Repeating this for each of the \(45\) representatives in the \(21\) nonsingleton polynomial fibers yields pairwise distinct sequences within every fiber; all sequences and mask representatives are supplied in `collision_catalogue.json`. The executable `verify.cpp` independently recomputes these sequences and verifies the fiber census; `check_catalogue.py` recomputes every supplied certificate directly from the bitmasks. This proves the strengthened reconstruction assertion at eight points. No implication at higher orders is asserted.

## Verification

Compile `verify.cpp` with any C++17 compiler and run it. It checks the complete \(n\le8\) isomorphism-orbit quotient, grades, fiber sizes, and all nonsingleton-fiber degree separations, finishing `VERIFY_OK`. Compile and run the independently structured `independent_count.cpp`: it enumerates all \(2^{21}=2{,}097{,}152\) eight-point rooted graph encodings without constructing isomorphism classes and finishes `INDEPENDENT_VERIFY_OK` at \(219\) polynomial values. Run `check_catalogue.py` alongside `collision_catalogue.json`; it reconstructs all \(45\) collision certificates and finishes `CATALOGUE_VERIFY_OK`.

For the explicit three-member fiber, the separate `spectrum_witness.py` check (requiring SymPy) calculates the Seidel characteristic polynomials, in mask order:
\[
\begin{aligned}
&(t-1)(t+1)(t^2-5)(t^4-22t^2+101),\\
&(t^2-5)(t^6-23t^4+123t^2-37),\\
&(t-1)(t+1)(t^2-13)(t^4-14t^2+29).
\end{aligned}
\]
They are distinct. Recorded reproducibility outputs are packaged as `verify_output.txt`, `independent_output.txt`, `catalogue_output.txt`, and `spectrum_output.txt`.

## Relationship to prior work

The equivalence between two-graphs, odd-edge-parity triple relations, and Seidel switching is classical. Bussemaker, Mathon and Seidel (1979), *Tables of two-graphs*, provide all two-graphs through nine vertices and a **cospectral** table; their table of eight-point classes contains \(243\) objects. Their spectral equivalence is not the coherent-triple singleton-type polynomial here. The full-report introduction, construction paragraphs, switching normal form and eight-point table were compared. The complete prior tabulation allows an independent starting enumeration, but does not state or tabulate this polynomial's \(219\) values, its \(21\) collision fibers, or their separation by vertex-incidence signatures.

Andrén and Markström (2009) study the *bivariate Ising polynomial of an ordinary graph*, including first seven-vertex examples with the same Ising polynomial. Their coefficients jointly record sizes of vertex cuts and numbers of crossing edges of a graph. Here the complete-graph switching-coset grade involves the signed count \(|s|+|E(G)\triangle\delta(s)|\), which is a different specialization and is defined on switching classes rather than individual graph isomorphism classes. For example, the three displayed descendants have different edge counts, so they have different bivariate Ising polynomials despite having equal \(P_T\). Their ordinary-graph collision classification does not imply the two-graph result.

Greaves, Koolen, Munemasa and Szöllősi (arXiv:1403.2155, first posted March 10, 2014) develop Seidel-matrix structural results and small two-graph classifications, again not this extension-type polynomial. The asserted contribution is only the sharp graded-type reconstruction boundary and its complete eight-parameter fiber classification, not the known switching formalism or original two-graph class counts.

## Limitations

The exhaustive cutoff and refined reconstruction theorem cover at most eight named parameters; no claim is made that the incidence degree sequence resolves all larger polynomial collisions. This is a finite mathematical classification with a reproducible exact exhaustive certificate, not a claim that a finite census proves asymptotic behavior. The possibility of an unindexed prior equivalent switching-coset weight-enumerator calculation remains a historical-priority risk. A separate independent mathematical audit has not been carried out.

## References

1. F. C. Bussemaker, R. A. Mathon and J. J. Seidel, *Tables of two-graphs*, EUT report 79-WSK-05, Eindhoven, October 1979. https://pure.tue.nl/ws/portalfiles/portal/2498383/252951.pdf
2. D. Andrén and K. Markström, *The bivariate Ising polynomial of a graph*, Discrete Applied Mathematics 157 (2009), 2515–2524; available online March 28, 2009. https://doi.org/10.1016/j.dam.2009.02.021
3. G. Greaves, J. H. Koolen, A. Munemasa and F. Szöllősi, *Equiangular lines in Euclidean spaces*, arXiv:1403.2155, version 1, March 10, 2014. https://arxiv.org/abs/1403.2155
