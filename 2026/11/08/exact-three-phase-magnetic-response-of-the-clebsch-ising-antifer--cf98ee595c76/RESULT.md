# Exact three-phase magnetic response of the Clebsch Ising antiferromagnet

## Finding

Let \(G\) be the 16-vertex, 5-regular Clebsch graph, in its folded-cube realization. For Ising spins \(\sigma_v\in\{-1,+1\}\), consider the uniform antiferromagnetic Hamiltonian
\[
 H_h(\sigma)=\sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v-h\sum_{v\in V(G)}\sigma_v,\qquad h\in\mathbb R.
\]
Write \(M(\sigma)=\sum_v\sigma_v\). For all nonnegative fields the complete zero-temperature ground-state classification is:

| Field | Ground energy | Allowed magnetizations | Number of labelled ground states |
| --- | ---: | --- | ---: |
| \(0\le h<7/3\) | \(-24\) | \(0\) | 10 |
| \(h=7/3\) | \(-24\) | \(0,6\) | 26 (10 and 16) |
| \(7/3<h<5\) | \(-10-6h\) | \(6\) | 16 |
| \(h=5\) | \(-40\) | \(6,8,10,12,14,16\) | 393 |
| \(h>5\) | \(40-16h\) | \(16\) | 1 |

At \(h=5\), the multiplicity by magnetization \(16-2k\), for \(k=0,1,2,3,4,5\), is respectively \(1,16,80,160,120,16\). For negative fields apply global spin reversal: \(H_{-h}(-\sigma)=H_h(\sigma)\). The nontrivial positive transition at \(h=7/3\) skips all magnetizations strictly between zero and six: the magnetization jumps directly from zero to \(3/8\) of saturation. The transition has an exact coexistence multiplicity of 26.

The new mathematical content is the complete field-dependent classification and the sharp intermediate-cardinality obstruction in the proof. The known zero-field maximum-cut classification and the elementary independent-set interpretation of the saturation field are not presented as independent novel discoveries.

## Assumptions and scope

Identify \(V(G)\) with \(\mathbb F_2^4\) and join \(x\) to \(x+e_i\) for \(i=1,2,3,4\), as well as to \(x+(1,1,1,1)\), with additions modulo two. There are exactly 16 vertices and 40 undirected edges; every edge appears once in the Hamiltonian. The exchange strength is one. For an arbitrary positive common exchange \(J\), multiply both the energies and critical field values by \(J\). All statements concern classical Ising spins and zero temperature; no thermodynamic-limit or quantum assertion is made.

The graph is the degree-five folded 5-cube, not its degree-ten complementary graph, which is also sometimes called the Clebsch graph.

## Proof

**1. Rewriting the Hamiltonian as an induced-edge problem.** Let \(S=\{v:\sigma_v=-1\}\), \(k=|S|\), and let \(e(S)\) count edges of the induced subgraph on \(S\). The regular degree is five and the number of edges is 40. The cut between \(S\) and its complement has \(5k-2e(S)\) edges. Consequently
\[
 H_h(S)=40-16h+(2h-10)k+4e(S). \tag{1}
\]
For positive \(h\), flipping all spins strictly improves any configuration with \(k>8\), so only \(0\le k\le8\) can minimize. At \(h=0\) the spectral argument below handles every \(k\).

**2. Maximum independent sets.** The even-weight and odd-weight vertices each form four antipodal pairs, with the pair members adjacent. An independent set therefore has at most four vertices of either parity. For a vertex \(y\) of odd weight, its four even nonneighbors are precisely those at Hamming distance three. For two nonadjacent odd vertices, the sets of such even nonneighbors intersect in precisely two points. Thus if an independent set contains two vertices of one parity, it contains at most two of the other parity. Every independent set of size five must therefore have parity profile \((4,1)\) or \((1,4)\), with its four-vertex side forced by the single opposite-parity vertex. There are exactly sixteen such sets. They are the neighborhoods \(N(v)\) of the sixteen vertices.

For distinct vertices \(u,v\), the five-element neighborhoods \(N(u)\) and \(N(v)\) intersect in either zero or two vertices: differences of graph generators give the strongly regular parameters \((16,5,0,2)\). In particular, two distinct maximum independent sets never intersect in four vertices.

**3. A sharp obstruction for intermediate sizes.** Every six-vertex set spans at least two edges: with zero or one edge, deleting an endpoint leaves at least five independent vertices, and in the one-edge case the two endpoint deletions give distinct maximum independent sets with four vertices in common. Every seven-vertex set spans at least three edges: at most two edges either have a one-vertex cover, leaving an independent six-set, or are disjoint, when two endpoint choices produce maximum independent five-sets differing by one vertex. Likewise, an eight-vertex set spans at least four edges: if at most three edges are not a matching, two vertices cover all of them and leave an independent six-set; if they form a three-edge matching, different endpoint selections produce maximum independent five-sets intersecting in four vertices. All possibilities contradict the preceding paragraph. Hence
\[
 e(S)\ge2\ (k=6),\qquad e(S)\ge3\ (k=7),\qquad e(S)\ge4\ (k=8). \tag{2}
\]
The final bound is sharp, as is also shown by the spectral calculation below. Together with \(e(S)\ge0\) for \(k\le5\), these bounds exclude every intermediate magnetization from the lower convex envelope of (1).

**4. Zero-field extremizers.** Since \(G\) is the Cayley graph of \(\mathbb F_2^4\) with generators \(e_1,e_2,e_3,e_4,(1,1,1,1)\), a Walsh character of weight \(s\) is an adjacency eigenvector with eigenvalue \(4-2s+(-1)^s\). The smallest eigenvalue is \(-3\), occurring at weights three and four. Therefore
\[
 \sum_{\{u,v\}\in E(G)}\sigma_u\sigma_v=\tfrac12\sigma^{\mathsf T}A\sigma\ge -24.
\]
Equality requires \(\sigma\) to lie in the \(-3\) eigenspace. Multiplying by the weight-four character reduces such a spin assignment to an affine-linear function \(g(x)=a_0+\sum_{i=1}^{4}a_ix_i\) on \(\{-1,+1\}^4\) that takes only values \(\pm1\). Comparing the nonconstant Fourier coefficients of \(g^2=1\) forces \(a_i a_j=0\) for distinct indices and \(a_0a_i=0\); hence exactly one coefficient is nonzero and equal to \(\pm1\). There are exactly ten such spin configurations, all with zero magnetization. In terms of down sets they have \(k=8\) and \(e(S)=4\).

**5. Lower envelope and degeneracies.** By (1), for \(0\le k\le5\) and \(h<5\) the lowest possible energy is attained at \(k=5\), giving \(-10-6h\), and there are sixteen such configurations. The two endpoint energies \(-24\) and \(-10-6h\) coincide only at \(h=7/3\). Bounds (2) give, for the intervening cardinalities, the lower lines \(-12-4h\) at \(k=6\), \(-18-2h\) at \(k=7\), and \(-24\) at \(k=8\). Direct comparison shows that neither intermediate line reaches the envelope at \(h\ge0\). At \(h=7/3\) only the ten \(k=8\) configurations and the sixteen \(k=5\) configurations minimize, yielding 26.

At \(h=5\), (1) reduces to \(H_5(S)=-40+4e(S)\): exactly the independent sets minimize. Their polynomial can be counted by parity. Sets of size two have 80 choices (48 same-parity, 32 opposite-parity), those of size three have 160 choices (64 single-parity, 96 mixed), and those of size four have 120 choices (32 single-parity, 64 of profile \((3,1)\) or \((1,3)\), and 24 of profile \((2,2)\)). Along with the 1 empty, 16 singleton, and 16 maximum independent sets, this gives
\[
 I_G(z)=1+16z+80z^2+160z^3+120z^4+16z^5,
 \qquad I_G(1)=393.
\]
For \(h>5\) equation (1) is uniquely minimized at the empty down set. This proves every field case.

## Verification

The accompanying self-contained `verify.py` enumerates all \(2^{16}=65,536\) labeled spin states using exact integer arithmetic. It checks the 40-edge definition, degree-five regularity, common-neighbor counts, the complete independent-set polynomial, the minimum energy in every fixed down-spin sector, and the exact minimizers at six rational field values including both transitions. It also verifies that the sixteen maximum independent sets are precisely the neighborhoods and checks the sharp induced-edge bounds for sizes six through eight. All assertions passed in the delivered package.

The finite enumeration is exhaustive for this fixed sixteen-vertex model, but the proof of the theorem is the structural argument above; no claim for larger dimensions follows from the enumeration.

## Relationship to prior work

The Clebsch/projective-cube graph and its relation to cuts are established in the literature, including DeVos and Samal (2006). The classical Ising zero-field ground-state classification on weighted folded hypercubes was previously available; our derivation of its ten extremizers is used only as a premise and cross-check, not as a new zero-field theorem. Honecker, Schulenburg and Richter (2003/2004) investigate magnetization plateaux on frustrated quantum lattices, including the classical Ising limit of triangular-lattice models, but do not state a magnetic-field classification for the Clebsch graph. The defining Clebsch graph is sometimes confused with its 10-regular complement; the explicit adjacency rule here prevents that ambiguity.

The two-parameter task of knowing a maximum cut and the independence number does not alone exclude intervening magnetization sectors: the additional induced-edge inequalities for six- and seven-vertex down sets are needed. No priority claim is made for the independent-set polynomial separately or for the already established zero-field count.

## Limitations

This is an exact result only for a sixteen-spin, uniform-coupling classical model. There is no quantum, finite-temperature, disorder, larger-folded-cube, or infinite-volume conclusion. Searches and material comparisons found no stronger field-dependent theorem for the same object, but absence from indexed sources does not establish global historical novelty. Independent bibliographic priority and scientific review remain unperformed.

## References

1. A. Honecker, J. Schulenburg and J. Richter, *Magnetization plateaus in frustrated antiferromagnetic quantum spin models*, original public arXiv submission 18 September 2003, https://arxiv.org/abs/cond-mat/0309425 .
2. M. DeVos and R. Šámal, *High-girth cubic graphs are homomorphic to the Clebsch graph*, original public arXiv submission 27 February 2006, https://arxiv.org/abs/math/0602580 .
3. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html . This is a graph-description reference, not an asserted research-priority source.
