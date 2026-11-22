# Sharp field-induced sitewise colour inversion on the Frucht Potts antiferromagnet

## Finding

Let the twelve vertices of the Frucht graph have spins in \(\{0,1,2\}\). Give equal colours on an edge an antiferromagnetic cost \(J>0\), and favour colour \(0\) with a uniform magnetic field \(H>0\). Write \(h=H/J\), let \(m(\sigma)\) count monochromatic edges, and let \(k(\sigma)\) count colour-\(0\) vertices. The reduced zero-temperature energy is \(m(\sigma)-h k(\sigma)\).

For the explicit vertex labelling below, define the complementary sets
\[
 A=\{0,2,5,9,11\},\qquad B=\{1,3,4,6,7,8,10\}.
\]
For every \(h>0\), the complete ground-state energy and its labelled multiplicity are

| Field range | Ground energy in units of \(J\) | Number of ground states | Set of vertices in colour \(0\) |
|---|---:|---:|---|
| \(0<h<3/2\) | \(-5h\) | 16 | exactly \(A\) |
| \(h=3/2\) | \(-15/2\) | 48 | either \(A\) or \(B\) |
| \(3/2<h<3\) | \(3-7h\) | 32 | exactly \(B\) |
| \(h=3\) | \(-18\) | 1377 | complements of independent vertex sets |
| \(h>3\) | \(18-12h\) | 1 | all twelve vertices |

The first transition is a **complete sitewise inversion**: as the field increases through \(h=3/2\), the preferred-colour occupation indicator switches from \(1\) to \(0\) at every vertex of \(A\), and from \(0\) to \(1\) at every vertex of \(B\), although its total increases from five to seven. In each strict interval these are identities in every ground state, not merely ensemble averages. No assertion is made about a finite-temperature discontinuity.

## Assumptions and scope

The Frucht graph here is the simple, undirected, three-regular graph on \(V=\{0,\ldots,11\}\) with eighteen edges, written as ordered endpoint pairs only for reproducibility:

```
(0,1) (0,6) (0,7) (1,2) (1,7) (2,3) (2,8)
(3,4) (3,9) (4,5) (4,9) (5,6) (5,10) (6,10)
(7,11) (8,11) (8,9) (10,11)
```

The Hamiltonian is \(E(\sigma)=J\sum_{\{u,v\}\in E}\mathbf1_{\sigma_u=\sigma_v}-H\sum_{v\in V}\mathbf1_{\sigma_v=0}\), with \(J>0\) and \(H>0\), with no other couplings or fields. Ground states mean global energy minimizers among all \(3^{12}=531441\) labelled spin assignments. The labels do not imply any nontrivial graph symmetry. Three colours are distinct; exchanging colours \(1\) and \(2\) generates different labelled states.

## Proof

**A unique five-site independent set.** The graph contains the disjoint triangles \(\{0,1,7\}\), \(\{3,4,9\}\), and \(\{5,6,10\}\). The remaining sites \(\{2,8,11\}\) contain the path \(2-8-11\). Every independent set contains at most one site from each triangle and at most two from the residual path, so its size is at most five. Equality forces residual vertices \(2\) and \(11\), hence excludes \(1,3,7,10\). The first triangle then forces \(0\); since \(0\) meets \(6\), the third forces \(5\); since \(5\) meets \(4\), the second forces \(9\). Therefore \(A\) is the **unique** independent set of size five. Its complement \(B\) induces precisely three disjoint edges \(\{1,7\}\), \(\{3,4\}\), \(\{6,10\}\), plus isolated vertex \(8\). Each vertex of \(B\) meets at least two vertices of \(A\).

**Uniform lower bounds.** For a configuration with \(k\) favoured sites, denote the favoured set by \(S\) and its number of internal edges by \(e(S)\). Always \(m(\sigma)\geq e(S)\). If \(k=6\), then \(e(S)\geq2\): otherwise deleting at most one endpoint of an internal edge would leave an independent five-set, necessarily \(A\). Thus \(S=A\cup\{v\}\) for some \(v\in B\), but \(v\) has at least two edges into \(A\), a contradiction. For any \(k\), three-regularity gives
\[
3k=2e(S)+|\partial S|\leq2e(S)+3(12-k),
\qquad e(S)\geq 3(k-6).
\]
For \(k\leq5\), simply use \(m(\sigma)\geq0\).

**Comparing fields.** The two explicit candidates have \((k,m)=(5,0)\) for \(S=A\) and \((7,3)\) for \(S=B\), with energy lines \(-5h\) and \(3-7h\). For \(0<h<3/2\), every \(k\leq4\) has energy strictly greater than \(-5h\), every \(k=6\) has energy at least \(2-6h>-5h\), and every \(k\geq7\) has energy at least \(3(k-6)-hk\geq3-7h>-5h\). Thus all minimizers have \(S=A\), and the three edges of \(B\) must be bichromatically coloured with colours \(1,2\). This gives \(2^4=16\) states.

For \(3/2<h<3\), the bounds similarly exclude \(k\leq5\), exclude \(k=6\) because \(2-6h>3-7h\), and exclude \(k\geq8\) because \(3(k-6)-hk>3-7h\). Equality for \(k=7\) requires \(e(S)=3\) and \(|\partial S|=3(12-k)\). The latter says that \(V\setminus S\) is independent, hence it is the unique five-set \(A\). So \(S=B\). The five sites of \(A\) can independently receive colour \(1\) or \(2\); this gives \(2^5=32\) states. At \(h=3/2\), these two classes alone tie, yielding 48 states.

For \(h>3\), the bound \(m(\sigma)\geq3(k-6)\) implies \(m-hk\geq(3-h)k-18\geq18-12h\), with strict inequality unless \(k=12\), hence the unique all-zero configuration. At \(h=3\), write \(T=V\setminus S\) for the nonfavoured sites, and let \(m_T\) count equal-colour edges inside \(T\). Counting degrees gives \(e(S)=18-3|T|+e(T)\), whence
\[
 m-3k=-18+e(T)+m_T.
\]
Thus equality holds if and only if \(T\) is independent, and its sites can each take one of two nonfavoured colours. The independence polynomial of the explicitly specified graph is
\[
 I_G(t)=1+12t+48t^2+73t^3+34t^4+t^5,
\]
so the \(h=3\) degeneracy is \(I_G(2)=1377\). The polynomial is verified independently by all \(2^{12}\) vertex subsets in the standalone program; the source graph and test are fully specified here.

## Verification

Run `python verify_frucht.py` from the containing directory, using Python 3 and only standard-library modules. It exhaustively checks all \(2^{12}=4096\) subsets for the independence polynomial and unique maximum independent set, then independently enumerates every one of the \(3^{12}=531441\) labelled configurations, computing the minimum monochromatic-edge count and degeneracy for every favoured population. It also checks the sitewise favoured-occupation supports and the exact rational-field ground-sector witnesses. The expected terminal message is `EXACT_FRUCHT_POTTS_CERTIFICATE_OK 531441 configurations 4096 subsets`. The structural arguments above, not a numerical sample, prove the stated all-real-positive-field classification.

## Relationship to prior work

Shrock and Xu (2010) give the general formalism for a Potts model in a single-colour or generalized external field, including the weighted-set chromatic polynomial in the strictly proper-colouring limit. Their general partition-function framework applies to arbitrary graphs, but it does not give this Frucht-graph finite-exchange ground-state envelope or establish a complete reversal of all sitewise preferred-colour indicators. The conventional description of the Frucht graph and its symmetry/independence properties does not provide magnetic-response data. Other published three-colour field computations treat distinct graphs such as the truncated tetrahedron and the Grötzsch graph; they do not imply the explicitly characterized complementary Frucht configurations. This is a narrow, exact finite-graph result, not a claim of a general antiferromagnetic monotonicity theorem.

## Limitations

Only the equal-coupling three-state antiferromagnet on the specified twelve-site graph with one positive field is classified. No smallest-possible-graph claim for complete inversion is made. The transition is a zero-temperature ground-state crossing; there is no discontinuity in finite-temperature Gibbs observables on a finite graph. Historical priority against unindexed or inaccessible equivalent treatments remains uncertain. There has been no independent scientific audit.

## References

1. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings* (initial arXiv posting 2010-09-07), https://arxiv.org/abs/1009.1182.
2. R. Frucht, *Graphs of Degree Three with a Given Abstract Group*, Canadian Journal of Mathematics **1** (1949), 365–378, https://doi.org/10.4153/CJM-1949-033-6.
3. E. W. Weisstein, *Frucht Graph*, MathWorld, https://mathworld.wolfram.com/FruchtGraph.html.
