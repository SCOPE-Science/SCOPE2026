# Sharp static and online shattering thresholds for four-point Cartesian rectangles

## Finding
Fix integers \(m,n\ge2\). On the point domain \([m]\times[n]\), each concept is a Cartesian product \(A\times B\) with exactly two distinct rows in \(A\) and two distinct columns in \(B\). The points in each four-point rectangle are its positive labels. Writing \(V\) for VC dimension and \(L\) for Littlestone dimension, the complete classification is
\[
(V,L)=\begin{cases}(0,0)&m=n=2,\\(1,1)&\{m,n\}=\{2,3\},\\(2,2)&\min\{m,n\}=2,\ \max\{m,n\}\ge4,\\(2,3)&m,n\ge3.\end{cases}
\]
In particular, fixed-shape four-point rectangles first exhibit a strict adaptive-over-static gap on a \(3\times3\) grid.

## Assumptions and scope
The row and column sets are arbitrary **two-element subsets**, not adjacent intervals. Empty concepts are excluded. Every query is one cell; the learner may adapt the next cell to earlier Boolean responses. A complete mistake tree of depth \(d\) is a full rooted binary tree whose internal nodes are queried cells and whose every root-to-leaf response sequence is realized by a rectangle. The statement covers all integers \(m,n\ge2\); it is invariant under swapping axes. It does not address variable-size rectangles or general real-plane axis-parallel boxes.

## Proof
**VC upper bound.** If a three-cell support were shattered, its all-positive trace would lie in a \(2\times2\) rectangle. Any three distinct corners contain a diagonally opposite pair. Every allowed rectangle containing that diagonal pair must use their two rows and two columns and hence also contains the third point. Thus the desired trace positive on the diagonal pair and negative on the remaining corner is impossible. Hence \(V\le2\).

**VC lower bounds.** If \(m,n\ge3\), choose \(u=(1,1)\), \(v=(1,2)\). The following allowed rectangles supply all four traces: for \(11\), row pair \(\{1,2\}\), column pair \(\{1,2\}\); for \(10\), the same row pair and columns \(\{1,3\}\); for \(01\), the same row pair and columns \(\{2,3\}\); for \(00\), rows \(\{2,3\}\) and columns \(\{1,2\}\). If \(m=2,n\ge4\), the same pair is shattered: use the first three choices and replace the \(00\) witness with both rows and columns \(\{3,4\}\). Symmetry handles \(n=2,m\ge4\). If \(m=n=2\), there is only one concept, so \(V=0\). If \(\{m,n\}=\{2,3\}\), there are three distinct concepts: a singleton is shattered, but two points cannot be shattered by fewer than four concepts, hence \(V=1\).

**Online upper bound.** Consider any root query at \((i,j)\). On a positive answer the remaining possible rectangles have row sets \(\{i,r\}\), \(r\ne i\), and column sets \(\{j,c\}\), \(c\ne j\). A subsequent query \((u,v)\) can do only one of the following: it is constant when \((u,v)=(i,j)\); its positive answer fixes \(r=u\) if \(u\ne i,v=j\); fixes \(c=v\) if \(u=i,v\ne j\); or fixes both when \(u\ne i,v\ne j\). In the fixed-one-parameter case, the residual hypotheses are a one-hot categorical class (or a singleton), of Littlestone dimension at most one: no query can have two branches each admitting a further split. In the fixed-both case it is a singleton. Thus the positive child of every query in this root-positive class has dimension at most one; therefore the entire root-positive class has dimension at most two. A full depth-four mistake tree would require a root-positive subtree of depth three, impossible. Thus \(L\le3\) for all sizes.

When \(m=2\), a root-positive class varies only in the second column and is a one-hot class; so it has Littlestone dimension at most one, and \(L\le2\). When both dimensions are two, only one concept exists, giving \(L=0\). When the grid is \(2\times3\) or \(3\times2\), there are only three concepts, which precludes a complete depth-two tree; so \(L\le1\).

**Online lower bound.** Every VC-shattered support yields a complete mistake tree of the same depth by querying its cells in a fixed order, so the VC lower bounds give \(L\ge2\) when relevant. For \(m,n\ge3\), it remains to exhibit depth three. In \([3]\times[3]\), the fully explicit eight-leaf tree in `checker.py` is checked against the actual row-and-column-set rectangles. Every leaf contains a distinct realizing concept. Embedding the same three rows and columns into all larger grids preserves every branch. This yields \(L\ge3\), matching the upper bound. The displayed cases follow.

## Verification
Run `python3 checker.py` without third-party dependencies. It independently constructs every two-row/two-column rectangle for each of six small sizes; enumerates all cell supports up to size three and checks their observed traces; computes exact Littlestone ranks by a recursive minimax split for the small cases; and explicitly verifies the depth-three tree including all eight leaf witnesses for the \(3\times3\) case. The recorded run result appears in `checker_output.txt`. The exhaustive computations cover only specified finite cases; the proof supplies the all-parameter statement.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (2021) study VC and Littlestone dimensions of linear zero-set families; their hypotheses do not assert dimensions of uniform four-point Cartesian rectangles. Ghazi and collaborators (2021) give general results about closure and aggregation of online dimensions, not this sharp fixed-shape classification. Manurangsi (2022) considers approximation of general shattering dimensions rather than the four-point family. Classical unrestricted Cartesian rectangle results, including the Hamming-product convexity result, involve a **larger** hypothesis family with arbitrary row/column subsets: its VC and online ranks do not determine those of the present fixed-two-by-two subfamily. Both the additional fixed-shape constraint and the sharp \(3\times3\) separation are essential to this statement. The search evidence is not an exhaustive historical-priority guarantee.

## Limitations
The theorem does not classify larger fixed-size rectangles, higher-dimensional Cartesian products, alternative query models, or restriction to consecutive rows and columns. Small exhaustive checks corroborate but do not establish the universal theorem. Complete priority under alternative terminology has not been proven. Independent mathematical audit has not been performed.

## References
1. Guingona, Kolesnikov, Nierwinski and Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1 (2021).
2. Ghazi et al., results on closure bounds for Littlestone and threshold dimensions, PMLR 132, `ghazi21a` (2021).
3. Manurangsi, work on hardness of approximation of VC/Littlestone dimensions, arXiv:2211.01443 (2022).
