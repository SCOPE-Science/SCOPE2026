# Three exceptional quartet orbits and a rank-five shattering plateau in the Paley graph of order 81

## Finding

Let \(K=\mathbb F_3[t]/(t^4+t+2)\), \(R=\{u^2:u\in K^\times\}\), and \(\mathcal N=\{v+R:v\in K\}\). Thus \(\mathcal N\) is the family of **open** neighborhoods of the Paley graph on the \(81\) elements of \(K\). A support \(S\subseteq K\) is *shattered* when every \(T\subseteq S\) occurs as \(S\cap(v+R)\) for some \(v\in K\); the center \(v\) is allowed to belong to \(S\), but \(0\notin R\).

**Exact finite theorem.** Writing \(\Phi(z)=\sum_{k\ge0}f_kz^k\), where \(f_k\) counts shattered \(k\)-element supports, one has

\[
\boxed{\Phi(z)=1+81z+3240z^2+85320z^3+1658880z^4+9515880z^5.}
\]

In particular, \(\operatorname{VCdim}(\mathcal N)=5\), strictly below the cardinality bound \(\lfloor\log_2 81\rfloor=6\). Every triple is shattered, but exactly \(4860\) of the \(\binom{81}{4}=1663740\) four-element supports fail to be shattered.

Use the base-three coefficient encoding
\[
\iota(a_0+a_1t+a_2t^2+a_3t^3)=a_0+3a_1+9a_2+27a_3\qquad(a_i\in\{0,1,2\}).
\]
For the explicit affine-semilinear subgroup
\[
G=\{x\mapsto ax^{3^j}+b:\ a\in R,\ b\in K,\ 0\le j<4\},
\]
of order \(12960\), the **nonshattered four-supports comprise exactly three orbits**. Their representative index tuples and their sizes as families of ordinary (not translation-normalized) supports are

| Representative | Orbit cardinality |
|---|---:|
| \((0,1,42,43)\) | 810 |
| \((0,3,6,46)\) | 3240 |
| \((0,3,46,52)\) | 810 |

Furthermore, the shattering complex is **not pure**: it has exactly \(4860\) inclusion-maximal four-supports in addition to its \(9515880\) maximal five-supports. The maximal four-supports consist of exactly two \(G\)-orbits, represented by \((0,1,2,42)\) (size \(3240\)) and \((0,1,42,44)\) (size \(1620\)).

## Assumptions and scope

The graph is the **simple undirected Paley graph** on \(\mathbb F_{81}\): zero is *not* a quadratic residue for adjacency, although a queried point may equal the neighborhood center, producing a negative answer at that point. The numerical coefficients refer to indexed points and unordered supports, not to quotient orbits or to fuzzy-zero shattering. The result concerns this one finite field and makes no assertion for all prime powers.

The polynomial \(p(t)=t^4+t+2\) is irreducible over \(\mathbb F_3\). It has no linear root; its remainders upon division by the three monic irreducible quadratics \(t^2+1\), \(t^2+t+2\), and \(t^2+2t+2\) are \(t\), \(t+1\), and \(t+1\), respectively. Thus the representation is a field with \(81\) elements. Because its nonzero multiplicative group has order \(80\), the nonzero-square set has size \(40\); and \(-1\in R\), so this is an undirected simple graph.

## Proof

**1. Exhaustive trace criterion.** Encode each field element as above. For a point \(y\in K\), define the \(81\)-bit center mask
\[
M_y=\{v\in K:y-v\in R\}.
\]
Starting with the singleton family \(\{K\}\), process a support \(S=(y_1,\ldots,y_k)\) in order. For every current center set \(A\), replace it with both \(A\cap M_{y_i}\) and \(A\setminus M_{y_i}\). At stage \(i\), these are **exactly** the sets of centers realizing the \(2^i\) binary strings on the first \(i\) queries. This follows inductively from the definition of \(M_y\). Consequently, \(S\) is shattered precisely when all \(2^k\) terminal center sets are nonempty. This is an exhaustive finite decision procedure, not a heuristic estimate.

**2. Count normalization.** Translation by \(b\in K\) simultaneously changes \(S\) to \(S+b\) and the centers to \(v+b\), preserving every trace. Write \(h_k\) for the number of shattered \(k\)-supports containing the field element \(0\). Counting pairs \((S,s)\) with \(s\in S\) and translating \(s\) to zero gives
\[
 kf_k=81h_k\qquad(k\ge1).
\]
It is therefore enough to enumerate increasing index tuples \((0,a_1,\ldots,a_{k-1})\) with \(1\le a_1<\cdots<a_{k-1}\le80\). The full enumeration, using the exact trace criterion, yields

| \(k\) | Normalized supports examined \(\binom{80}{k-1}\) | Shattered \(h_k\) | Total \(f_k\) |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 81 |
| 2 | 80 | 80 | 3240 |
| 3 | 3160 | 3160 | 85320 |
| 4 | 82160 | 81920 | 1658880 |
| 5 | 1581580 | 587400 | 9515880 |
| 6 | 24040016 | 0 | 0 |

Every entry is independently reproduced by the complete executable enumerators `verify_bitmask.cpp` and `verify_direct.cpp`. The former represents each trace class as a bitset of candidate centers, whereas the latter independently generates all \(81\) restrictions and checks the presence of every possible pattern. Their agreement is a reproducible finite certificate, with the full finite range specified above. The support \((0,1,2,3,4)\) is, for example, shattered. No six-support is shattered, and no support of size seven or more can be shattered because it would require at least \(2^7=128\) distinct center patterns from just \(81\) centers. This proves the complete polynomial and the VC-dimension claim.

**3. Orbit and facet classification.** Multiplication by \(a\in R\), the Frobenius transformations \(x\mapsto x^{3^j}\), and translations all preserve \(R\)-difference adjacency and hence all traces. Their composition forms \(G\), which has \(81\cdot40\cdot4=12960\) elements. For an arbitrary four-support containing zero, applying its \(G\)-orbit and then translating each possible member to zero produces a finite orbit of normalized four-supports. The executable `verify_orbits.py` enumerates **all** \(82160\) normalized four-supports, forms their complete disjoint normalized \(G\)-orbits, and checks shattering at every member. It obtains precisely the three nonshattered orbits above, of normalized sizes \(40,160,40\).

For each shattered normalized four-orbit representative \(S\), the same program tests all \(x\in K\setminus S\) for the shattering of \(S\cup\{x\}\). Existence of such an extension is invariant under \(G\). Exactly two shattered four-orbits admit **no** shattered five-extension: the representatives stated above, with normalized orbit sizes \(160,80\). For any four-support orbit \(O\), counting the \(4\) choices of a zero-normalizing point gives \(|O|=81|O_0|/4\). These normalized sizes therefore yield the full orbit sizes claimed. Every shattered five-support is maximal because no six-support is shattered. Thus both face dimensions occur, proving nonpurity and the facet census.

## Verification

Three independent executable source artifacts accompany this statement. Compile and execute either C++ enumerator with `g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct` or `g++ -O3 -std=c++17 verify_bitmask.cpp -o verify_bitmask && ./verify_bitmask`. Execute the orbit classifier using `python3 verify_orbits.py`. All computations use integer arithmetic only, and every enumerated combination occurs in an explicit bounded loop. No random seed, external package, network access, lookup table or black-box algebra engine is required.

Expected terminal checks: `DIRECT_OK` from the direct implementation, zero shattered normalized six-supports from both enumerators, and `ORBIT_OK` with normalized bad-four-orbit sizes \((40,160,40)\) and nonextendable-four-orbit sizes \((160,80)\). The programs perform complete finite enumerations rather than sampling; their source and the simple translation-orbit counting argument provide the finite proof of the stated numbers.

## Relationship to prior work

McDonald, Sahay and Wyman (first publicly available October 7, 2022) study VC dimension of quadratic-residue translates over finite fields, prove asymptotic lower bounds and report **numerical searches restricted to prime fields**; they do not give the exact order-81 open-neighborhood polynomial or the five finite orbit/facet classes here. Their numerical treatment uses a modified convention addressing zero, so quantitative comparisons require respecting the explicit open-neighborhood convention above.

Coudert, Csikós, Ducoffe and Viennot study practical algorithms for VC dimension of graph **closed** neighborhoods, a different set system; the theorem here gives exact coefficients and orbit representatives for this particular graph's open neighborhoods. Related exact Paley-25 neighborhood and finite-field online-shattering classifications address different field orders or a different learning invariant, respectively; neither statement by itself implies the coefficients or the orbit classification at order \(81\).

## Limitations

This is a fully finite, computationally certified classification for a single natural field order, not an asymptotic theorem. The exhaustive algorithms have independently reproducible source, but have not been independently mathematically audited. Generalizations to other extension degrees and a theory explaining the three exceptional orbit shapes without exhaustive classification remain open. Unindexed equivalent treatments, including alternative names for quadratic-residue translate concepts, are a publication-priority risk.

## References

1. B. McDonald, A. Sahay and E. L. Wyman, *The VC-dimension of quadratic residues in finite fields*, public preprint dated 2022-10-07, https://arxiv.org/abs/2210.03789 (subsequently *Discrete Mathematics* 348 (2025), article 114192).
2. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, 2024, https://arxiv.org/abs/2405.07588 and https://doi.org/10.4230/LIPIcs.SEA.2024.8.
3. *The exact Paley-25 shattering polynomial and its exceptional triples*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-exact-paley-25-shattering-polynomial-and-its-exceptional-tri--d709a1a3fcdd (related field order, distinct result).
4. *Near-information-theoretic online shattering of quadratic-residue translates*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-near-information-theoretic-online-shattering-of-quadratic-residu--e4d8e40a4b13 (online dimension, distinct invariant).
