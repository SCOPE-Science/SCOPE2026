# A first Moore summand in dihedral quotients of squared-cycle independence complexes

## Finding
For every integer \(6\le n\le20\), let \(C_n^2\) have vertex set \(\mathbb Z/n\mathbb Z\), with distinct vertices adjacent when their cyclic distance is at most two. Let \(K_n=\operatorname{Ind}(C_n^2)\), and let the full polygon dihedral group \(D_n\) of order \(2n\) act by \(r(i)=i+1\) and \(s(i)=-i\). The ordinary geometric orbit space \(X_n=|K_n|/D_n\) has the **complete homotopy classification**
\[
 X_n\simeq\begin{cases}
 *,& 6\le n\le11\ \text{or}\ 13\le n\le15,\\
 S^2,&n=12,\\
 S^3,&n=16,\\
 S^3\vee S^3,&17\le n\le19,\\
 S^3\vee M(\mathbb Z/2\mathbb Z,3),&n=20.
 \end{cases}
\]
Here \(M(\mathbb Z/2\mathbb Z,3)=S^3\cup_{\deg 2}e^4\). In particular, \(H_3(X_{20};\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z\), and \(H_4(X_{20};\mathbb Z)=0\). The twentieth cycle is the first with positive-degree integral homology torsion in this entire natural sequence starting at six. The cutoff at twenty includes precisely the nondegenerate cycle powers for which the independence complex has dimension at most five.

## Assumptions and scope
The objects are unordered independent **vertex sets**; there is no independence-size truncation. The full group includes reflections. The quotient is the topological orbit space on the realization, not a naive vertex-orbit simplicial quotient. The graph has \(n\ge6\), so the circular-distance condition defines the usual second power of a cycle. The maximal possible independent-set size is \(\lfloor n/3\rfloor\); thus \(n\le20\) is equivalent to dimension at most five. No claim about larger lengths, a uniform recurrence for homotopy groups, or the quotient by the rotation subgroup alone is made.

## Proof
**Orbit cells.** Let \(F_n\) be the collection of nonempty independent subsets of \(\mathbb Z/n\mathbb Z\). A \(d\)-simplex of the barycentric subdivision \(\mathrm{sd}(K_n)\) is a strict inclusion flag \(F_0\subsetneq\cdots\subsetneq F_d\) with all \(F_j\in F_n\). The action of \(D_n\) on such a flag preserves the cardinality of each member, hence any group element preserving the flag fixes its vertices individually. The quotient therefore has an admissible simplicial-orbit delta-complex with one \(d\)-cell per group orbit of flags. Orient cells by increasing face cardinality. Their exact cellular differential, for a representative flag, is
\[
 \partial[F_0<\cdots<F_d]=\sum_{j=0}^d(-1)^j[F_0<\cdots<\widehat{F_j}<\cdots<F_d],
\]
where every displayed face is replaced by its canonical dihedral-orbit representative. There is no stabilizer division or rationalization. The supplied programs reconstruct all faces, flag orbits and signed boundary matrices from these definitions and explicitly check \(\partial^2=0\).

**Elementary collapses and integral differentials.** For each length, the checker removes a highest-dimensional free-face/coface pair whenever it exists; the pair is certified by direct enumeration of all current cofaces. The collapsed complexes have the following exact numbers of cells, indexed by dimension zero upwards (the initial counts for the final length are displayed separately):

| \(n\) | Post-collapse cell numbers | Integral chain outcome |
|---|---|---|
| \(6,7,8,9,10,11\) | One vertex, no higher cells | Contractible |
| \(12\) | \((5,9,6)\) | One free degree-two class |
| \(13,14,15\) | One vertex, no higher cells | Contractible |
| \(16\) | \((15,68,109,56)\) | One free degree-three class |
| \(17\) | \((21,116,202,108)\) | Two free degree-three classes |
| \(18\) | \((27,164,308,172)\) | Two free degree-three classes |
| \(19\) | \((30,202,381,210)\) | Two free degree-three classes |
| \(20\) | \((36,297,851,962,372)\) | One free degree-three class and one order-two class |

The twentieth case begins with \((74,926,3717,6267,4662,1260)\) orbit cells. Exactly 7,194 certified elementary collapses remove every five-cell. On the remaining integer chain complex, unit-pivot elimination has respectively \((35,262,589,371)\) pivots in degrees one through four; it leaves chain ranks \((1,0,0,2,1)\) with one nonzero boundary coefficient, exactly \(\pm2\) from degree four to degree three. Every elimination uses an explicit entry \(\pm1\) and integral row/column basis operations, so no hidden odd-primary or higher-power torsion is possible. Independent ranks of the post-collapse boundaries are \((35,262,589,371)\) over \(\mathbb F_2\) and \((35,262,589,372)\) over \(\mathbb F_3\). In particular, one two-primary class is genuine. The same exact unit-pivot procedure gives the remaining rows of the table with no nonunit boundary coefficients.

**Fundamental groups.** After the certified collapses, contractible cases already consist of a point. In every other case, the checker contracts a spanning tree in the remaining one-skeleton and constructs the exact edge-word relator associated with each surviving triangle. It then eliminates a generator that appears exactly once in a relator, replacing it in all other relators by the equivalent word and freely reducing. These are valid Tietze transformations. The complete eliminations use respectively \(5,54,96,138,173,262\) generators for lengths \(12,16,17,18,19,20\), and all finish with the trivial presentation. The quotient is therefore simply connected in each of those cases.

**From algebra to homotopy.** For length twelve the collapsed complex is two-dimensional, simply connected, and has exactly one free second-homology class. Hurewicz and the homological Whitehead theorem give \(S^2\). For lengths sixteen to nineteen the collapsed complexes are three-dimensional and simply connected, with zero second homology; they are consequently two-connected and equivalent to the stated wedges of three-spheres. At length twenty the collapsed complex is four-dimensional. Its three-skeleton is simply connected with vanishing second homology, hence a wedge of three-spheres. Attaching its remaining four-cells is classified, up to change of integer bases, by the degree matrix of \(\partial_4\). The above unimodular reduction has 371 unit invariant factors and one factor two, with one further free three-sphere. Cancelling the unit summands yields precisely \(S^3\vee M(\mathbb Z/2\mathbb Z,3)\). This is a homotopy classification, not an inference from mod-two ranks alone.

## Verification
The standalone Python 3 standard-library sources in `code/` enumerate every independent face and every orbit of its barycentric flags for all listed lengths. Execute from the `code/` directory: `python3 verify.py 6 15`, `python3 verify.py 16 19`, `python3 verify.py 20 20`, and `python3 verify.py mod20`. The runs verify oriented boundary compositions, legal elementary collapses, exact integer unit pivots, surviving nonunit coefficients, fundamental-group Tietze eliminations and an independent modular cross-check. For larger lengths the exhaustive enumeration takes longer; there are no external software or network dependencies.

## Relationship to prior work
Adamaszek, *Splittings of independence complexes and the powers of cycles* (arXiv:1106.6250, first public 2011-06-30), Sections 1 and 6, gives nonequivariant homotopy splittings for these cycle powers but no integral orbit-space presentation. Rinaldo and Romeo, *On the reduced Euler characteristic of independence complexes of circulant graphs* (arXiv:1706.00863), addresses nonequivariant Euler characteristics. The published mathematical record *Dihedral quotient Euler characteristics of squared-cycle independence complexes* (published-finding corpus/2026, record 8ff019b4f221) determines the rational alternating quotient Euler characteristic for all cycle lengths but expressly does not determine individual Betti numbers, integral torsion or quotient homotopy type. Its zero value at length twenty cannot imply contractibility or exclude the exhibited two-torsion. The present statement is a strictly stronger **finite-range integral homotopy** result and does not reclaim any earlier alternating-character formulas.

## Limitations
The classification stops at twenty; neither periodicity nor persistence of torsion at later lengths is asserted. The finite certificate establishes these fifteen sizes only. A potentially unindexed equivalent computation remains possible; research-literature searches cannot prove uniqueness. No independent external mathematical audit has been performed.

## References
1. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250, first submitted 2011-06-30, https://arxiv.org/abs/1106.6250.
2. G. Rinaldo and F. Romeo, *On the reduced Euler characteristic of independence complexes of circulant graphs*, arXiv:1706.00863, first submitted 2017-06-02, https://arxiv.org/html/1706.00863v5.
3. *Dihedral quotient Euler characteristics of squared-cycle independence complexes*, published published-finding corpus mathematical record 8ff019b4f221, https://github.com/published-finding corpus/2026.
