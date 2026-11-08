# Complete FAT-coloring spectrum of binary hypercubes

## Finding

For every integer \(d\ge1\), let \(Q_d\) be the graph on \(\mathbb F_2^d\) in which two words are adjacent when they differ in exactly one coordinate. A Fair and Tolerant (FAT) \(k\)-coloring has nonempty color classes, and each vertex has exactly \(\alpha d\) neighbors of each *different* color and \(\beta d\) neighbors of its *own* color, for global \(\alpha,\beta\in[0,1]\) with \(\beta+(k-1)\alpha=1\).

**Theorem.** Fix integers \(d\ge1\) and \(k\ge2\), and a real \(\alpha\in[0,1]\). A FAT \(k\)-coloring of \(Q_d\) with parameter \(\alpha\) exists **if and only if** there are integers \(r,t\ge1\) such that

\[
 k=2^r,\qquad \alpha=\frac{t}{d},\qquad (k-1)t\le d.
\]

For these parameters the own-color neighbor count is exactly \(d-(k-1)t\), or \(\beta=1-(k-1)t/d\). A FAT one-coloring always exists separately.

Consequently,

\[
 \chi^{\mathrm{FAT}}(Q_d)=2^{\lfloor\log_2(d+1)\rfloor}.
\]

Moreover, for \(k\ge2\), a *proper* FAT \(k\)-coloring (zero own-color neighbors) exists precisely when \(k\) is a power of two and \(k-1\) divides \(d\); in this case \(t=d/(k-1)\). In particular \(\chi(Q_d)=2\), whereas \(\chi^{\mathrm{FAT}}(Q_d)\) grows without bound.

## Assumptions and scope

The graph is the unweighted, loopless binary Hamming cube \(Q_d\), \(d\ge1\). All \(k\) colors must occur. Adjacency means Hamming distance one, not any larger distance. Color names are arbitrary and do not affect feasibility. FAT is the degree-normalized notion of Beers and Mulas, not a proper-coloring requirement. The theorem classifies feasible color *counts and parameters*; it does not classify individual colorings up to automorphism.

## Proof

**Necessity: positive cross-color counts.** Assume \(k\ge2\), with coloring classes \(V_1,\ldots,V_k\). If \(\alpha=0\), no edge joins distinct colors, forcing a constant coloring because \(Q_d\) is connected, contradicting the nonempty \(k\) classes. Thus \(\alpha>0\). Each vertex has degree \(d\), and \(\alpha d\) is the number of neighbors of any given other color. It is a positive integer, say \(t\ge1\). Since \(\beta d=d-(k-1)t\) is a nonnegative integer, \((k-1)t\le d\).

**Necessity: number of colors.** For each pair \(i\ne j\), count edges between \(V_i\) and \(V_j\) in both directions. There are \(t|V_i|\) from the \(V_i\) side and \(t|V_j|\) from the \(V_j\) side. As \(t>0\), \(|V_i|=|V_j|\). Thus each color class has size \(2^d/k\), which is an integer. Consequently \(k\mid 2^d\), and therefore \(k=2^r\) for an integer \(r\ge1\).

**Sufficiency: an explicit syndrome coloring.** Let \(k=2^r\), \(t\ge1\), and \(s=d-(k-1)t\ge0\). List the \(d\) columns \(a_1,\ldots,a_d\in\mathbb F_2^r\) so that each nonzero vector of \(\mathbb F_2^r\) occurs exactly \(t\) times and the zero vector exactly \(s\) times. Define

\[
 c(x_1,\ldots,x_d)=\sum_{i=1}^d x_i a_i\in\mathbb F_2^r.
\]

Because \(t\ge1\), all standard basis vectors appear among the columns, so this linear map is surjective and all \(k\) colors are used. The neighbors of a vertex \(x\) are \(x+e_i\), and

\[
 c(x+e_i)=c(x)+a_i.
\]

For any desired different color \(y\ne c(x)\), the difference \(y-c(x)\) is a unique nonzero vector, repeated among columns exactly \(t\) times. Thus \(x\) has exactly \(t\) neighbors colored \(y\). Exactly the \(s\) zero columns preserve \(c(x)\), hence its own-color neighbor count is \(s\). Setting \(\alpha=t/d\) and \(\beta=s/d\) verifies every FAT equation, for every vertex and every color. This proves the equivalence for all \(d,k,\alpha\) in scope.

**Chromatic and proper thresholds.** Feasibility requires \(k\) a power of two and \(k-1\le d\); conversely \(t=1\) constructs every such \(k\). The largest is \(2^{\lfloor\log_2(d+1)\rfloor}\). A FAT coloring is proper if and only if \(\beta=0\), equivalent to \(s=0\) and hence \((k-1)t=d\). The divisibility criterion follows. Finally \(Q_d\) is bipartite and has an edge, so its ordinary chromatic number is two.

## Verification

The standalone `verify.py` independently reconstructs the edges by one-coordinate bit flips. It tests the explicit syndrome construction against the defining FAT neighbor counts for all feasible triples with \(1\le d\le12\) and \(k\le16\), a total of 106 parameter triples. A separate exhaustive enumeration of surjective colorings for \(1\le d\le3\) and \(2\le k\le d+1\) verifies the feasibility criterion for 14 small parameter triples. The command is `python verify.py`; expected final line is `VERIFY_OK`. This finite verification is corroboration only: the proof above establishes the unrestricted theorem.

## Relationship to prior work

Beers and Mulas introduced FAT colorings and proved, for connected regular graphs, equal color-class sizes and general degree bounds [1]. Those theorems give the restrictions \(k\mid2^d\) and \(k\le d+1\) for the hypercube but by themselves do not establish that every allowable power of two, and every allowable integral off-color count, can be realized. Their primary discussion treats complete graphs, cycles, certain book/petal graphs, and regular Turán graphs rather than a hypercube feasibility spectrum.

Beers and Mulas [2, Section 7.2] obtain product **lifts** preserving the number of colors, including Cartesian products; their stated constructions do not directly supply the simultaneous spectrum of powers-of-two color counts and all allowable \(t\). Shaebani [3,4] proves broad FAT existence and gap constructions on other families and likewise does not state this exact cube criterion. The same colorings can be called *perfect colorings* or *equitable partitions* of the Hamming cube, with quotient matrix having diagonal \(d-(k-1)t\) and all off-diagonal entries \(t\). Work of Krotov and Valyuzhenich [5] studies degree-limited and correlation-immune classes of such colorings, not this all-parameter existence statement. The sufficiency is a classical-style linear-syndrome construction, and prior coding-theory constructions with special parameters (such as Hamming codes) are acknowledged rather than claimed as invented here.

## Limitations

This is an existence and parameter-spectrum theorem, not a classification or enumeration of all FAT colorings. It is restricted to binary cubes, not nonbinary Hamming graphs or arbitrary Cartesian products. The elementary construction is linear and does not imply every FAT coloring is linear. Related results in the broader older perfect-coloring/equitable-partition literature could establish the same existence criterion under different terminology; priority should be regarded as provisional pending specialist review. The accessible primary comparison does not exhaust every historical coding-theory source, and a late revision of [1] could not be checked as completely as the accessible version. No independent mathematical audit is claimed.

## References

[1] L. Beers and R. Mulas, *Fair and Tolerant (FAT) Graph Colorings*, arXiv:2510.18494, first public 2025-10-21, https://arxiv.org/abs/2510.18494.

[2] L. Beers and R. Mulas, *Spectral Perspectives on FAT Graph Colorings*, arXiv:2604.21665, 2026, https://arxiv.org/abs/2604.21665.

[3] S. Shaebani, *On Fair and Tolerant Colorings of Graphs*, arXiv:2511.14871, 2025, https://arxiv.org/html/2511.14871v2.

[4] S. Shaebani, *Concerning FAT Colorings of Graphs*, arXiv:2512.11153, 2025, https://arxiv.org/html/2512.11153v1.

[5] D. S. Krotov and A. A. Valyuzhenich, *On degree-3 and (n-4)-correlation-immune perfect colorings of n-cubes*, arXiv:2311.05566, 2023, https://arxiv.org/abs/2311.05566.
