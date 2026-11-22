# Optimal power-domination mobility in the quaternary projective plane

## Finding

Let \(G\) be the point–line incidence graph of the unique projective plane of order four, \(\operatorname{PG}(2,4)\). Write \(\gamma_P(G)\) for the least cardinality of a power-dominating vertex set. Then

\[\gamma_P(G)=6.\]

There are exactly \(566{,}160\) minimum power-dominating sets. Their initial point-count and final observation-time distribution is:

| Selected points | Selected lines | Observation time 2 | Observation time 3 |
|---:|---:|---:|---:|
| 2 | 4 | 0 | 65,520 |
| 3 | 3 | 52,080 | 383,040 |
| 4 | 2 | 0 | 65,520 |

All other profiles are empty. The token-jumping graph of minimum configurations is connected with \(19{,}706{,}400\) undirected edges. The token-sliding graph contains \(2{,}257{,}920\) undirected edges, one component on \(535{,}920\) vertices, and \(30{,}240\) isolated vertices. The latter are exactly the slide-frozen sets and have three selected points and three selected lines; \(10{,}080\) have time two and \(20{,}160\) have time three.

## Assumptions and scope

The projective plane is Desarguesian. Its points and lines are the one- and two-dimensional subspaces of \(\mathbb F_4^3\); the incidence graph has 21 point-vertices and 21 line-vertices, each of degree five. For a nonempty starting set \(S\), define \(O_1=N[S]\). For each integer \(j\ge1\), let

\[O_{j+1}=O_j\cup\{w:\exists v\in O_j,\ N(v)\setminus O_j=\{w\}\}.\]

All forcings in a round use the preceding round's observed set. A starting set power dominates if \(O_j=V(G)\) for some finite \(j\), and the least such \(j\) is its observation time. Two distinct minimum sets are token-jump adjacent if their symmetric difference has size two. They are token-slide adjacent if, in addition, the exchanged vertices are adjacent in \(G\). All sets and edges are labeled and unordered respectively; no quotient by collineations or dualities is taken.

## Proof

This is a finite exhaustive proof with independently constructed adjacency tables and full enumeration, not an extrapolation from sampled configurations. A transparent implementation of the two exhaustive certificates is attached. The mathematical justification of the algorithms is as follows.

**Plane construction.** The first program enumerates the 21 normalized nonzero homogeneous vectors of \(\mathbb F_4^3\) and connects a point to a line exactly when their scalar product is zero. It uses the irreducible relation \(\alpha^2=\alpha+1\). The second program independently indexes the sixteen affine points, five points at infinity, sixteen slope-intercept lines, four vertical lines and the line at infinity, using the explicit affine incidence rule. Both give 42 vertices of degree five and the standard Desarguesian plane.

**Complete seed search.** Every five-subset of the 42 vertices is generated exactly once by a strictly increasing sequence of five indices. There are \(\binom{42}{5}=850{,}668\) such subsets, and each is non-power-dominating. Success is upward closed (adding initially observed vertices cannot block forcing), so no subset of size at most five can succeed. Every six-subset is then generated exactly once; there are \(\binom{42}{6}=5{,}245{,}786\). Its observation times are determined by the exact recurrence above until full observation or a fixed point. Counting by the number of point-indices and terminal time yields the four nonzero populations in the theorem, totaling \(566{,}160\). In particular, at least one six-set succeeds, completing the lower and upper bounds on \(\gamma_P(G)\).

**Exact reconfiguration search.** Store each successful six-subset as a 42-bit integer in a lookup table. For every such subset \(S\), enumerate all pairs \(v\in S\), \(w\notin S\). The replacement \((S\setminus\{v\})\cup\{w\}\) is a legal token jump precisely when it is in the successful-set lookup. Count directed replacements and divide by two. For token sliding, additionally require that \(v\) and \(w\) are adjacent in the incidence graph. A union–find traversal in one implementation and a separate breadth-first traversal in the affine-coordinate implementation compute connected components exactly. They return \(19{,}706{,}400\) jump edges and one jump component, versus \(2{,}257{,}920\) slide edges, \(30{,}240\) singleton slide components and one slide component of size \(535{,}920\). The singleton classification follows by calculating the point-count and observation-time of every degree-zero slide vertex. Both implementations agree on the numerical assertions.

## Verification

The embedded `power_plane.cpp` program constructs the plane using homogeneous coordinates and proves minimum size and all propagation profiles by a complete combinatorial loop. Compile with `g++ -O3 -std=c++17 power_plane.cpp -o power_plane` and run `./power_plane 4 6`.

The separate `power_slides_stats.cpp` program (which imports `power_plane.cpp` in the same directory) enumerates all minimum placements again and computes both movement rules with union–find; compile with `g++ -O3 -std=c++17 power_slides_stats.cpp -o power_slides_stats` and run `./power_slides_stats`.

The independent-coordinate `verify_affine_full.cpp` is standalone and checks seed counts, time profiles, jump connectivity, jump edges, slide connectivity, slide edges and the frozen sets. Compile with `g++ -O3 -std=c++17 verify_affine_full.cpp -o verify_affine_full` and run `./verify_affine_full`. It prints `PASS` only after assertions on all claimed cardinalities. These sources were compiled and executed before inclusion and then are suitable for exact replay in their decoded form.

## Relationship to prior work

Ferrero–Hogben–Kenter–Young, arXiv:1512.06413, introduce the observation-time convention and correct an earlier general lower bound; the paper supplies definitions, not these projective-plane counts. Brimkov–Patel–Suriyanarayana–Teich, arXiv:1805.10984, introduce the power-domination polynomial; the coefficient for six is not supplied for \(\operatorname{PG}(2,4)\). Bjorkman and collaborators, arXiv:2201.01798, develop power-domination token jumping and examples of disconnected state graphs but do not compute this incidence graph. Earlier finite-projective-plane domination and incidence-graph reconfiguration results address different predicates and thus do not determine these numbers. Exact literature priority remains a distinct, independently revisable question.

## Limitations

The theorem is a finite, exact census for \(\operatorname{PG}(2,4)\), with no assertion about arbitrary finite projective planes, higher dimensions, general propagation-time bounds, component diameters or symmetry-orbit classifications. The exhaustive programs and their enumeration logic are the correctness certificates; a few successful examples or partial runs would not establish the result. Some archival or unindexed references may contain an earlier equivalent calculation. No independent scholarly audit has been performed.

## References

- D. Ferrero, L. Hogben, F. H. J. Kenter, M. Young, *Note on power propagation time and lower bounds for the power domination number*, first posted 2015-12-20, https://arxiv.org/abs/1512.06413.
- B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, first posted 2018-05-28, https://arxiv.org/abs/1805.10984.
- B. Bjorkman et al., *Power domination reconfiguration*, first posted 2022-01-05, https://arxiv.org/abs/2201.01798.
