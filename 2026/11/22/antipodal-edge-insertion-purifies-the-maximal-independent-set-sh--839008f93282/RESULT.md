# Antipodal edge insertion purifies the maximal-independent-set shattering complex of the four-cube

## Finding
Let \(Q_4\) have vertex set \(V=\mathbb F_2^4\), with adjacent vertices differing in one coordinate, and let \(F\) be obtained by adjoining the eight edges \(\{x,x+(1,1,1,1)\}\). Thus \(F\) is the sixteen-vertex, five-regular folded five-cube, also called the five-regular Clebsch graph. For a graph \(G\) on \(V\), define \(\mathcal M(G)\) as the family of its **inclusion-maximal independent vertex subsets**, and say that \(S\subseteq V\) is shattered if \(\{M\cap S:M\in\mathcal M(G)\}=2^S\).

**Theorem.** The shattered supports for \(\mathcal M(F)\) are *exactly* the independent sets of \(F\) having at most four vertices. In particular,
\[
\Phi_F(z)=\sum_{S\text{ shattered}}z^{|S|}=1+16z+80z^2+160z^3+120z^4,
\qquad \operatorname{VCdim}(\mathcal M(F))=4.
\]
The shattering complex is pure of dimension three, although the ordinary independence complex of \(F\) is nonpure: \(F\) has forty inclusion-maximal independent four-sets and sixteen inclusion-maximal independent five-sets. The 120 maximal shattered four-sets comprise precisely two automorphism orbits of sizes 40 and 80, respectively the maximal independent affine planes and the four-subsets of open neighborhoods.

For comparison, the same definition on the original four-cube gives
\[
\Phi_{Q_4}(z)=1+16z+88z^2+160z^3+104z^4,
\]
with 104 maximal shattered four-sets and eight additional maximal shattered two-sets, exactly the antipodal vertex pairs. Thus inserting the eight antipodal edges **removes eight shattered pairs, adds sixteen shattered four-sets, and turns a nonpure shattering complex into a pure one**, without changing VC dimension four. These two finite polynomials and the facet claims form one comparison theorem.

## Assumptions and scope
All arithmetic on vertices is in \(\mathbb F_2^4\). An integer label from 0 to 15 represents the corresponding four-bit vector, and \(\oplus\) denotes bitwise exclusive-or. Put \(D=\{1,2,4,8,15\}\). Distinct vertices of \(F\) are adjacent exactly when their exclusive-or is in \(D\). There are exactly sixteen vertices; the assertions concern the fixed graphs \(F\) and \(Q_4\), not all folded cubes or all graph-independent-set concept families. A support is a set of query vertices, and a concept is a maximal independent set, not an arbitrary independent set or a graph neighborhood.

## Proof
**1. Geometry and independent sets.** The five nonzero vectors of \(D\) have exclusive-or zero, and any four are linearly independent. Every other nonzero vector is the sum of exactly two distinct members of \(D\). Hence, after translating one vertex of an independent triple to zero, its other two vectors correspond to two different two-element subsets of \(D\) with a common member: disjoint pairs would have a sum in \(D\) and hence give adjacent vertices. Permutations of the five directions and translations preserve \(F\), and act transitively on its independent triples. These maps form the full group of order \(16\cdot120=1920\); only their transitive action is needed below.

Take the representative independent triple \(T=\{0,3,5\}\). A direct exclusive-or check with \(D\) shows that the **only** vertices independent from each member of \(T\) are \(6,9,14\). Its unique common neighbor is 1, whose open neighborhood is \(N(1)=\{0,3,5,9,14\}\). The candidate 6 is adjacent to both 9 and 14. Consequently, each independent triple belongs to a unique five-element neighborhood and has exactly three independent fourth-vertex extensions: its two unused neighborhood vertices and its exclusive-or sum \(a\oplus b\oplus c\).

There are \(\binom{16}{2}-40=80\) independent pairs. Each independent pair has exactly six third-vertex extensions: adjacent vertices have no common neighbors and nonadjacent vertices have two common neighbors, so for nonadjacent \(u,v\), exactly \(16-2-(5+5-2)=6\) vertices avoid \(u,v\) and all their neighbors. Hence the numbers of independent triples and quadruples are \(80\cdot6/3=160\) and \(160\cdot3/4=120\). The quadruples split into two disjoint types: 80 subsets of the form \(N(v)\setminus\{w\}\), \(w\in N(v)\) (each unique because distinct neighborhoods intersect in at most two vertices), and 40 affine planes \(\{a,b,c,a\oplus b\oplus c\}\). Every independent five-set is a full \(N(v)\), because a triple together with two further compatible extensions cannot use its affine-sum fourth vertex. There are sixteen such five-sets, and none of greater size. Exactly these sixteen neighborhoods and forty affine planes are inclusion-maximal independent sets, so \(|\mathcal M(F)|=56\). The ordinary independence face numbers are therefore \(1,16,80,160,120,16\).

**2. Explicit witnesses for every four-point trace.** The 40 independent affine planes form one orbit, represented by \(A=\{0,3,5,6\}\). The other 80 independent quadruples form one orbit, represented by \(B=\{1,2,4,8\}\) (four of the five neighbors of zero). Translations and permutations of \(D\) are transitive on each type. In the following table a concept is encoded by a four-digit *hexadecimal* mask: bit \(x\) signifies membership of vertex \(x\). For each support ordered as displayed, the label \(b_3b_2b_1b_0\) means that the required trace contains its \(j\)-th vertex precisely when \(b_j=1\). Each listed mask is an independent dominating set (hence maximal independent), as checked directly by XOR with \(D\), and its trace is the requested four-bit label.

| Trace label | Witness for \(A=(0,3,5,6)\) | Witness for \(B=(1,2,4,8)\) |
|---|---|---|
| `0000` | `0096` | `0069` |
| `0001` | `1681` | `1482` |
| `0010` | `2418` | `1284` |
| `0011` | `0609` | `1886` |
| `0100` | `1824` | `0690` |
| `0101` | `1221` | `2492` |
| `0110` | `4128` | `4294` |
| `0111` | `4229` | `0096` |
| `1000` | `1842` | `0960` |
| `1001` | `1441` | `2942` |
| `1010` | `2148` | `4924` |
| `1011` | `2449` | `0906` |
| `1100` | `0960` | `6118` |
| `1101` | `1861` | `2112` |
| `1110` | `8168` | `4114` |
| `1111` | `0069` | `8116` |

The table shatters both representative quadruples, and therefore all 120 independent quadruples. Every smaller independent set is contained in an independent quadruple and is shattered by downward closure. Any support containing an edge cannot be shattered, since its all-positive trace is absent. Finally an independent five-set \(N(v)\) cannot be shattered: every one of its four-subsets belongs to no other maximal independent set (it extends only to \(N(v)\)), so a trace with exactly four positives on \(N(v)\) is impossible. Therefore no support of size five or more is shattered. This proves the complete classification, polynomial, purity, two orbits and VC dimension.

**3. Antipodal perturbation comparison.** For \(Q_4\), the full finite certificate `verify_folded.py` enumerates all 65,536 vertex subsets, tests independence and domination (equivalent to maximal independence), and computes distinct traces on each of the same 65,536 query supports. The independently constructed `verify_quotient.cpp` uses five-bit antipodal quotient adjacency for \(F\), and ordinary Hamming distance one for \(Q_4\); it separately enumerates all subsets, concepts, traces, and inclusion-maximal shattered supports. Both obtain 42 maximal-independent-set concepts for \(Q_4\), partitioned by size into 24 four-sets, 16 five-sets, and 2 eight-sets; exactly 8 maximal shattered pairs and 104 maximal shattered quadruples. Those eight pairs are precisely \(\{x,x\oplus15\}\). This is an exhaustive finite proof by auditable terminating algorithms, not an inference from a sample or statistical experiment; no claim is made about larger cubes.

## Verification
Using Python 3 (standard library only), run `python3 verify_folded.py`. The code checks all Boolean supports and additionally constructs all 1,920 affine direction-permutation symmetries, verifies the two facet orbits and rechecks every witness above. Independently compile and run `c++ -std=c++17 -O2 verify_quotient.cpp -o verify_quotient && ./verify_quotient`. The verification output is:

```
FOLDED_FIVECUBE_MIS_SHATTER_PASS concepts=56 faces=1,16,80,160,120 facets=40+80
ANTIPODAL_PERTURBATION_PASS q4_facets=8x2+104x4 folded_facets=120x4
QUOTIENT_CLEBSCH_Q4_EXHAUSTIVE_PASS 65536_supports_per_graph
```

The Python program also prints the exact two witness arrays listed in the proof. The code computes finite counts exhaustively; the structural argument above explains their geometry and the negative boundary.

## Relationship to prior work
Kahn and Park's 2019 public preprint studies the asymptotic number of maximal independent sets in Hamming cubes; it does not determine this particular membership-shattering complex or the folded-cube perturbation. Krivelevich, Mészáros, Michaeli and Shikhelman's 2023 study concerns random greedy maximal independent sets via local limits, not all Boolean traces on fixed small cubes. Benediktsson, Macpherson and Adler's 2020 VC study addresses **graph neighborhood** set systems, not the family of all maximal independent sets. The folded-cube and the 16-vertex graph's 1,920 symmetries are classical. Existing work on the ordinary independence complex of the folded cube is about independent subsets and their topology, and does not by itself imply which supports are shattered by its maximal faces.

The new object is the incidence-shattering complex of the maximal independent sets, together with its exact relation to the ordinary independence complex and the antipodal edge perturbation. Computations or older unpublished tables could conceivably contain these coefficients; no claim of priority is made beyond the inspected comparisons.

## Limitations
The theorem concerns precisely two sixteen-vertex graphs and the specified vertex-membership concept class. It gives no all-dimension formula and no online/Littlestone dimension. The comparison for \(Q_4\) uses complete finite computational certificates, rather than a separately derived structural trace classification. Prior-work searches cannot prove historical uniqueness. Independent external mathematical validation has not been performed.

## References
1. J. Kahn and J. Park, *The number of maximal independent sets in the Hamming cube*, arXiv:1909.04283 (first publicly posted 2019-09-10), https://arxiv.org/abs/1909.04283.
2. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, first published 2023-12-18, https://doi.org/10.1002/rsa.21200.
3. B. G. Benediktsson, D. Macpherson and I. Adler, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, arXiv:2007.16042 (2020-07-31), https://arxiv.org/abs/2007.16042.
4. A. E. Brouwer, *Clebsch graph*, distance-regular graph notes, https://aeb.win.tue.nl/drg/graphs/Clebsch.html (graph construction and automorphism group).
