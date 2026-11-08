# Exact magnetic response and first excitation of the McGee Ising antiferromagnet

## Finding
Let \(G\) be the McGee graph, the unique cubic cage of girth seven, and consider the classical antiferromagnetic Ising Hamiltonian
\[
H_{J,h}(\sigma)=J\sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v-h\sum_{v\in V(G)}\sigma_v,
\qquad J>0,\quad h\in\mathbb R,\quad \sigma\in\{-1,1\}^{24}.
\]
Write \(b=|h|/J\). Its complete zero-temperature energy and degeneracy are
\[
\frac{E_0(h)}J=\begin{cases}-28,&0\le b\le1,\\-24-4b,&1\le b\le3,\\36-24b,&b\ge3,\end{cases}
\]
\[
\Omega(h)=\begin{cases}
2,&0\le |h|<J,\\18,&|h|=J,\\8,&J<|h|<3J,\\34{,}305,&|h|=3J,\\1,&|h|>3J.
\end{cases}
\]
For \(0<h<J\) the magnetization is \(0\); for \(J<h<3J\) it is \(4\), one-sixth of saturation; for \(h>3J\) it is \(24\). For \(h<0\), magnetizations reverse. At \(h=0\) the two ground configurations differ by global spin reversal, and exactly four bonds are frustrated. At the first crossing \(h=J\), the \(18\) ground states have magnetizations \(0,2,4\) with multiplicities \(2,8,8\). At the saturation crossing \(h=3J\), all \(34{,}305\) independent vertex sets of \(G\) are ground states; that independence-set count is previously known.

At zero field the first excitation gap is exactly \(2J\). Its full degeneracy is \(16\), with eight states each of magnetization \(2\) and \(-2\). In particular, with \(\beta=(k_BT)^{-1}\), the zero-field susceptibility per vertex obeys
\[
\chi_{\mathrm{site}}(T)=\frac{\beta}{24}\operatorname{Var}_{T,0}(\sum_v\sigma_v)
=\frac43\beta e^{-2\beta J}+O\!\left(\beta e^{-4\beta J}\right)
\quad(T\downarrow0).
\]

## Assumptions and scope
Use vertices \(0,1,\ldots,23\). Include the Hamiltonian cycle edges \(\{i,i+1\bmod24\}\), and for each \(i\) an undirected chord \(\{i,i+s_i\bmod24\}\), with \((s_0,\ldots,s_{23})=(-12,7,-7)\) repeated eight times. Duplicated chord descriptions are represented by one edge. This is the standard McGee LCF representation and has exactly \(24\) vertices, \(36\) edges, degree three, and girth seven. All spins are classical \(\pm1\) variables; there is no next-nearest coupling, disorder, or transverse field. Configurations are labelled by these fixed vertices; symmetry-related or spin-reversed configurations are counted separately.

For a configuration let \(S=\{v:\sigma_v=-1\}\) and \(q=|S|\). Let \(c(S)\) denote the number of edges crossing from \(S\) to its complement and \(e(S)\) the number of edges internal to \(S\). Since \(G\) is cubic,
\[
c(S)=3q-2e(S),\qquad H_{J,h}/J=36-2c(S)-(h/J)(24-2q).
\]

## Proof
The critical exact finite lemma is the following complete maximum-cut-by-cardinality census. Let \(C_q=\max_{|S|=q}c(S)\), and let \(N_q\) be the number of labelled \(q\)-sets attaining \(C_q\). Complete integer enumeration gives

| \(q\) | \(C_q\) | \(N_q\) |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 3 | 24 |
| 2 | 6 | 240 |
| 3 | 9 | 1,304 |
| 4 | 12 | 4,212 |
| 5 | 15 | 8,328 |
| 6 | 18 | 10,024 |
| 7 | 21 | 7,072 |
| 8 | 24 | 2,668 |
| 9 | 27 | 424 |
| 10 | 30 | 8 |
| 11 | 31 | 8 |
| 12 | 32 | 2 |

Spin complement gives \(C_{24-q}=C_q\) and \(N_{24-q}=N_q\), specifying all twenty-five cardinalities. The first eleven rows count independent sets because \(c(S)=3q\) precisely when \(e(S)=0\). Their counts, already available from the published McGee independence-complex computation, sum to \(34{,}305\). The new critical counts lie at \(q=11,12\).

The two maximizing twelve-sets are the even-index and odd-index vertices of the LCF cycle. Every cycle edge and length-seven chord crosses this partition; the four length-twelve chords \(\{0,12\},\{3,15\},\{6,18\},\{9,21\}\) do not. Each parity class contains two disjoint such chords, so its induced edge count is two and its cut size is thirty-two. The eight maximizing eleven-sets arise by deleting one endpoint of either internal chord from one parity class; the eight maximizing ten-sets arise by deleting one endpoint from each of the two internal chords. The exhaustive certificate proves these families exhaust all relevant maximizers, not merely that they are feasible.

For \(h>0\), global spin inversion shows that no minimizer with \(q>12\) can be preferred to its complement. For \(0\le q\le10\), the minimum energy in the \(q\)-sector is \(36-6q-b(24-2q)\) in units of \(J\). Its minimum over these sectors is attained at \(q=10\) for \(0<b<3\), at \(q=0\) for \(b>3\), and at every independent set for \(b=3\). The \(q=11\) and \(q=12\) sector energies are \(-26-2b\) and \(-28\), respectively, while the \(q=10\) energy is \(-24-4b\). Comparing these three affine functions and the polarized one yields exactly the stated piecewise ground energy, all magnetizations, and the endpoint degeneracies.

At \(h=0\), the two \(q=12\) configurations attain \(c=32\), hence energy \(-28J\). The next cut value is \(31\), attained exactly eight times at \(q=11\) and eight times at \(q=13\), giving \(16\) states at energy \(-26J\) and magnetizations \(\pm2\). A two-level Boltzmann expansion, with higher states at least \(4J\) above the ground energy, then yields the stated susceptibility asymptotic.

The finite lemma is an exact proof by exhaustion, not sampling. In `verify_masks.cpp`, the 24-cycle and periodic LCF chords are generated, all \(2^{24}=16{,}777{,}216\) subsets are visited, and every cut is evaluated directly from the 36 undirected edges. In `verify_recursive.cpp`, an independently specified 36-edge list is used in an incremental depth-first transfer over the twenty-four spin assignments. Both programs check all \(C_q,N_q\), the full maximum cut, and the number and squared magnetizations of the first excited configurations. All integer comparisons are exact, with no floating-point threshold.

## Verification
With a C++17 compiler, run:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_masks.cpp -o verify_masks
./verify_masks
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_recursive.cpp -o verify_recursive
./verify_recursive
```

The first program returns `VERIFY_MASKS_OK`; the second returns `VERIFY_RECURSIVE_OK`. Their checked expected cut-count table is reproduced above. The independent 36-edge representation also agrees with the published LCF convention. Unlike a truncated search, both programs enumerate every binary spin assignment and perform exact integer checks.

## Relationship to prior work
The 2015 analysis of regular Ising polyhedra establishes the graph-theoretic method for finite-cluster magnetic plateaux, but treats the tetrahedron, octahedron, cube, icosahedron, and dodecahedron, not the McGee cage. The 2015 mathematical exposition of the McGee graph and the MathWorld graph reference give its uniqueness, construction, and spectral properties, but not the stated Ising response. The published McGee independence-complex calculation already gives the full independent-set size vector for \(q\le10\); therefore the \(34{,}305\)-fold saturation crossing and the eight independent ten-sets are explicitly **not** independent novelty claims. The present exact magnetic response additionally depends on the induced-one-edge eleven-sets and induced-two-edge twelve-sets, the unique zero-field minimizing cut, and the resulting low-field crossing and excitation structure. A public graph database may contain unindexed related cut tables, so unexamined equivalences remain a priority risk.

## Limitations
This is a finite, labelled, uniform-coupling classical Ising result, not a thermodynamic-limit phase transition or a claim for other cubic cages. It gives no nonzero-temperature closed partition function, quantum dynamics, or transverse-field behavior. Its exhaustive proof is complete for this 24-vertex graph, but originality is based on the explicitly inspected sources and searches rather than a guarantee against all unindexed databases or historical publications. The low-temperature error term assumes fixed \(J>0\) and zero field.

## References
- J. Strečka, K. Karľová, and T. Madaras, *Giant magnetocaloric effect, magnetization plateaux and jumps of the regular Ising polyhedra*, arXiv:1502.04449v1, first submitted 2015-02-16. https://arxiv.org/abs/1502.04449
- J. Baez, *McGee Graph*, AMS Visual Insight, 2015-09-15. https://blogs.ams.org/visualinsight/2015/09/15/mcgee-graph/
- E. W. Weisstein, *McGee Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/McGeeGraph.html (LCF form and spectrum; no assumed first-publication date).
- *The McGee graph independence complex is a five-sphere*, public result and complete independent-set vector, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-mcgee-graph-independence-complex-is-a-five-sphere--5daca7995d97/RESULT.md (the previously determined independent-set counts are credited).
