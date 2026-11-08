# Sharp weight-two symbol-pair codes and four-regular Euler tours

## Finding

Let \(n\ge2\) be an integer. For binary words \(x,y\in\{0,1\}^n\), write
\[
d_{\mathrm p}(x,y)=\left|\left\{i\in\mathbb Z/n\mathbb Z:(x_i,x_{i+1})\ne(y_i,y_{i+1})\right\}\right|.
\]
Define \(A^{(2)}_{\mathrm p}(n,7)\) to be the maximum cardinality of a code consisting solely of binary words of **Hamming weight exactly two**, any distinct pair at symbol-pair distance at least seven. A singleton code is permitted. Then
\[
\boxed{A^{(2)}_{\mathrm p}(n,7)=
\begin{cases}
1,&2\le n\le6,\\
2,&n=7,8,\\
3,&n=9,\\
\lfloor n/2\rfloor,&n\ge10.
\end{cases}}
\]

There is also an exact characterization of all optimal codebooks when \(n=2k\ge10\). Label their \(k\) codewords with distinct vertices \(0,\ldots,k-1\), and at each of the \(2k\) coordinates record the label of the unique codeword having a one there. The resulting cyclic label sequence is an Euler tour of a **connected simple four-regular graph** on those labels. Conversely, any Euler circuit of any connected simple four-regular graph on \(k\) labeled vertices, read as a cyclic sequence of departing vertices, defines such an optimal binary weight-two code. These constructions are inverse with a fixed cyclic coordinate origin and a fixed labeling of the codewords. Rotating the coordinates, or relabeling codewords, gives the corresponding natural equivalence.

## Assumptions and scope

All coordinates are indexed modulo \(n\), the channel reads **ordered**, overlapping cyclic pairs, and codewords remain indexed rather than quotiented by rotation. The Hamming weight is **exactly** two for every codeword, and the threshold seven is an integer minimum distance. The result is about arbitrary codes with this constant-Hamming-weight constraint, not linearity or all-codeword constant pair-weight alone. In particular the graph correspondence is claimed only for optimal even lengths \(n\ge10\), not for the generally nonunique odd-length extremizers.

For a two-element subset \(A\subseteq\mathbb Z/n\mathbb Z\), let \(x_A\) denote its binary indicator. For a set \(S\) of coordinates let \(e_n(S)\) be the number of edges of the labeled cycle \(C_n\) having both endpoints in \(S\). The graph argument below only applies to \(n\ge5\), where the two incident read edges at each coordinate are distinct.

## Proof

**1. Disjointness and exact distance.** If two weight-two indicators share a one-coordinate, their Hamming distance is two and their symbol-pair distance is at most four, since each differing coordinate lies in at most two reads. Thus distinct codewords in a code of minimum pair distance seven have disjoint supports. For two disjoint two-element supports \(A,B\) and \(n\ge5\), a read pair differs exactly when its edge meets \(A\cup B\). The four marked coordinates contribute eight endpoint incidences to these read edges; an edge whose endpoints are both marked has been counted twice. Hence
\[
 d_{\mathrm p}(x_A,x_B)=8-e_n(A\cup B).
\]
Consequently the minimum-distance condition is equivalent to \(e_n(A\cup B)\le1\) for every two distinct codewords.

**2. Upper bound.** Disjoint two-element supports immediately imply \(|\mathcal C|\le\lfloor n/2\rfloor\). If \(k\ge3\) codewords have disjoint supports, place their labels on the \(2k\) occupied cycle positions and leave the remaining \(z=n-2k\) positions blank. Among the \(n\) cycle edges, at least \(2k-z=4k-n\) have both endpoints occupied: every empty coordinate is incident to at most two edges, so there are at most \(2z\) edges touching an empty coordinate. Edges between any given two labels occur at most once, and at most one codeword can have an internally adjacent pair. In the latter case that codeword has no adjacency to any other occupied label, since such an adjacency together with its internal adjacency would violate the two-codeword criterion. Therefore, in all cases,
\[
 e_n(\text{all occupied positions})\le\binom{k}{2}
 \quad(k\ge3).
\]
(The case of one internal adjacency has at most \(1+\binom{k-1}{2}\le\binom{k}{2}\).)

For \(n=7,8\), a hypothetical three-word code would force at least \(4\cdot3-n=5\) or \(4\) occupied edges, respectively, exceeding \(\binom32=3\). For \(n=9\), a hypothetical four-word code would force at least \(4\cdot4-9=7>\binom42=6\). For \(n=5,6\), any two disjoint two-element supports occupy four vertices and induce at least \(8-n\ge2\) cycle edges, so cannot satisfy the pair-distance condition. The same two-word impossibility is immediate for \(n=2,3,4\) by lack of four disjoint support positions or by the four-cycle. This establishes all the exceptional upper bounds.

**3. Small sharp witnesses.** For \(2\le n\le6\), use the singleton support \(\{0,1\}\). For \(n=7,8\), use \(\{0,1\}\) and \(\{3,5\}\). For \(n=9\), use the three supports \(\{0,2\}\), \(\{3,7\}\), and \(\{5,8\}\). The distance identity from Step 1 verifies the minimum threshold in each case.

**4. Construction for every larger length.** For \(k\ge5\), form the simple circulant graph \(G_k\) on \(\mathbb Z/k\mathbb Z\) having edges of differences \(\pm1\) or \(\pm2\). It is connected, simple, four-regular, and has \(2k\) edges. By Euler's theorem it admits an Euler circuit. List its \(2k\) departing vertices cyclically; each of the \(k\) vertices appears exactly twice. Give the corresponding codeword ones at those two positions. Every pair of distinct labels occurs on at most one adjacent position pair because the Euler circuit traverses distinct edges of a simple graph. Thus every two codewords satisfy \(e_n(A\cup B)\le1\) and have pair distance at least seven. This attains \(|\mathcal C|=k\) at length \(n=2k\). To obtain length \(2k+1\), insert one all-zero coordinate into every codeword at a common cut. No existing adjacent pair of marked positions is created by insertion; an old adjacency can only disappear. The formula in Step 1 therefore shows no pair distance decreases. The code still has \(k\) words, attaining \(\lfloor(2k+1)/2\rfloor\).

**5. Characterization at equality for even lengths.** In an optimal code at \(n=2k\ge10\), disjointness and cardinality imply that every coordinate belongs to exactly one codeword. If both ones of a codeword were adjacent, its support would contribute one occupied edge; an edge from either outer neighbor to another codeword would contribute a second forbidden edge in their four-point union. Therefore successive labels are different. Any unordered label pair occurs as a consecutive pair at most once, again by the distance criterion. The \(2k\) consecutive label pairs are hence distinct edges of a simple graph. Every label appears twice, and each appearance has one incoming and one outgoing edge; distinctness gives degree four. The cyclic label sequence traverses every edge exactly once, making the graph connected and the sequence an Euler circuit. Conversely the construction in Step 4 works for **any** connected simple four-regular graph, completing the characterization.

## Verification

The accompanying standalone Python program, `verify.py`, independently computes pair distance directly from the ordered read pairs. It exhaustively rules out every code one word larger than the claimed optimum for all lengths \(2\) through \(9\), validates all exceptional witnesses, and generates/checks Euler-tour codebooks for lengths \(10\) through \(150\). For every generated even-length code it also verifies four-regularity and simplicity of the label-transition graph. Execution prints `VERIFY_OK exhaustive_sizes=2..9 graph_witness_sizes=10..150`.

This finite verification is a consistency check, **not** an exhaustive infinite proof; the all-length result relies on the five mathematical proof steps above.

## Relationship to prior work

Cassuto and Blaum introduced the overlapping symbol-pair channel and its distance. Chee, Ji, Kiah, Wang and Yin established a general **Eulerian-graph lift** for constructing MDS symbol-pair codes from classical MDS codes (Proposition 3.2 of their article), including a ten-edge example based on \(K_5\). The graph-lift idea and that example are therefore **not claimed as new**. Their result assumes an MDS source code and a girth hypothesis, and does not explicitly state the sharp cardinality for binary **Hamming-weight-two** codes at pair distance seven, its finite cutoff, or the converse classification of all even-length optimizers. The present code is neither claimed to be MDS nor to improve unrestricted symbol-pair code bounds.

Zhao and Chang (2025) study codes of **constant symbol-pair weight**, including pair weight four and pair distance seven, a substantially overlapping *superset* parameter problem. Their public abstract is available, but the full text was inaccessible at the time of review; thus whether their constructions or proofs already imply any part of the narrower exact constant-Hamming-weight-two result remains a historical-priority risk. Unlike constant pair weight four, constant Hamming weight two excludes weight-three runs and other possible supports. The structural equality classification here is an additional scope not stated in their abstract.

## Limitations

No claim is made for other Hamming weights, other minimum pair distances, or maximum cardinalities of unrestricted/constant-pair-weight codes. The statement does not classify all odd-length optimizers. The sharp size follows from the disjoint-support obstruction only for \(n\ge10\); special shorter values require separate occupancy arguments. Existing Eulerian symbol-pair construction methods overlap the proof method. No independent audit has been performed, and novelty is qualified by incomplete access to some relevant recent literature.

## References

1. Y. Cassuto and M. Blaum, *Codes for symbol-pair read channels*, IEEE ISIT (2010), 988–992. DOI: 10.1109/ISIT.2010.5513753. First day-verifiable conference presentation: 2010-06-13.
2. Y. Cassuto and M. Blaum, *Codes for symbol-pair read channels*, IEEE Transactions on Information Theory 57 (2011), 8011–8020. DOI: 10.1109/TIT.2011.2164891. Author-hosted full text: https://ycassuto.net.technion.ac.il/files/2018/05/1-7.pdf.
3. Y. M. Chee, L. Ji, H. M. Kiah, C. Wang and J. Yin, *Maximum distance separable codes for symbol-pair read channels*, IEEE Transactions on Information Theory 59 (2013), 7259–7267; arXiv:1211.1728, Proposition 3.2 and Example 3.1. https://ar5iv.labs.arxiv.org/html/1211.1728.
4. M. Zhao and Y. Chang, *Bounds and constructions of optimal symbol-pair codes with constant pair-weight*, Designs, Codes and Cryptography 93 (2025), 2297–2316. DOI: 10.1007/s10623-025-01598-9 (abstract inspected; full article unavailable).
