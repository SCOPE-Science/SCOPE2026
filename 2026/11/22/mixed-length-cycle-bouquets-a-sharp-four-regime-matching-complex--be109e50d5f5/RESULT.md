# Mixed-length cycle bouquets: a sharp four-regime matching-complex homotopy classification

## Finding

Let \(r\ge2\) and let \(m_1,\ldots,m_r\ge3\) be arbitrary integers. Form the cycle bouquet \(B(m_1,\ldots,m_r)\) by taking cycles of lengths \(m_1,\ldots,m_r\) and identifying one vertex from each to a single hub, with all other vertices distinct. Write \(\mathcal M(G)\) for the ordinary matching complex of a finite graph \(G\): vertices of \(\mathcal M(G)\) are graph edges, and simplices are sets of pairwise vertex-disjoint graph edges.

Set
\[
K=\sum_{i=1}^r\left\lfloor\frac{m_i}{3}\right\rfloor,\quad
u_0=\#\{i:3\mid m_i\},\quad
\nu_2=\#\{i:m_i\equiv2\pmod3\}.
\]
Then, with all equivalences integral homotopy equivalences,
\[
\boxed{\quad
\mathcal M(B(m_1,\ldots,m_r))\simeq
\begin{cases}
*, & \nu_0\ge2,\\
S^{K-1}\vee S^{K-1}, & \nu_0=1,\\
S^{K-1}, & \nu_0=0,\ \nu_2=0,\\
\displaystyle\bigvee^{2\nu_2-1}S^K, & \nu_0=0,\ \nu_2\ge1.
\end{cases}\quad}
\]
In particular, all reduced integral homology is free, and is concentrated in at most one degree. The criterion \(\nu_0\ge2\) is a sharp complete criterion for contractibility throughout this family. Noncontractible cases have exactly one of the multiplicities \(1,2,2\nu_2-1\) in the indicated dimensions.

## Assumptions and scope

Every petal is a simple cycle, and different petals share exactly their one common vertex. Parallel edges, loops, and any additional edges between petals are excluded. The number of petals is at least two; the statement is not the formula for a single cycle. The empty simplicial complex consisting only of the empty face is used in joins as the augmented \((-1)\)-sphere \(S^{-1}\), so the smallest petal \(m_i=3\) is covered without omitting its spoke link.

## Proof

**Step 1: fixed base and spoke cones.** Let \(h\) be the common vertex. Each length-\(m_i\) petal has exactly two graph edges incident to \(h\), called its spokes, and \(m_i-2\) internal edges. The internal edges form a path of \(m_i-2\) *edges*, whose line graph is a path \(P_{m_i-2}\) on \(m_i-2\) vertices. Put \(A_i=\operatorname{Ind}(P_{m_i-2})\), where \(\operatorname{Ind}\) denotes the independence complex. A matching avoiding the hub has a free choice of a matching in each internal path, and so the subcomplex of these matchings is
\[
A=A_1*\cdots*A_r.
\]
A matching contains at most one spoke. Choosing either spoke of petal \(i\) rules out exactly the neighboring end internal edge in that petal, leaving the internal matching complex \(B_i=\operatorname{Ind}(P_{m_i-3})\), included in \(A_i\) via deletion of the relevant end vertex of \(P_{m_i-2}\). For each of the \(2r\) spokes \(s\), let
\[
L_s=B_i*\mathop{\bigast}_{j\ne i}A_j\subseteq A.
\]
The complete matching complex is precisely \(A\) with the \(2r\) cones \(s*L_s\) attached along their bases. Distinct cone interiors are disjoint, and their intersections occur only in \(A\). Thus this description is a sequence of simplicial cofibration pushouts, not merely a numerical face count.

**Step 2: path complexes and critical inclusions.** The standard endpoint domination/deletion recurrence for path independence complexes gives, for \(k\ge0\) wherever the path size is nonnegative,
\[
\operatorname{Ind}(P_{3k})\simeq S^{k-1},\qquad
\operatorname{Ind}(P_{3k+1})\simeq *,\qquad
\operatorname{Ind}(P_{3k+2})\simeq S^k.
\]
For \(P_0\), the first formula uses the augmented join unit. To see the recurrence directly, split on the penultimate path vertex and use simplicial domination to collapse the endpoint deletion pair; the remaining complex is the suspension of the independence complex of the path with three fewer vertices. The base cases are \(P_0\) (augmented sphere), \(P_1\) (point), and \(P_2\) (two points).

It follows that a petal length \(m_i=3k\) has contractible \(A_i\) and spherical \(B_i\simeq S^{k-2}\); length \(3k+1\) has \(A_i\simeq S^{k-1}\) and contractible \(B_i\); length \(3k+2\) has both \(A_i\) and \(B_i\) of sphere type \(S^{k-1}\), and, crucially, **the natural inclusion** \(B_i\hookrightarrow A_i\) is a homotopy equivalence. Indeed, in the latter case \(A_i=\operatorname{Ind}(P_{3k})\) is obtained from \(B_i=\operatorname{Ind}(P_{3k-1})\) by adding the endpoint vertex, whose link is \(\operatorname{Ind}(P_{3k-2})\). That link is contractible because \(3k-2\equiv1\pmod3\), so attaching its cone is a homotopy equivalence. This also covers \(k=1\).

**Step 3: evaluate the cone attachments.** If at least two petal lengths are divisible by three, \(A\) is contractible, and for *every* spoke its link \(L_s\) is contractible, because at least one contractible factor \(A_j\) remains in the link. Attaching each cone preserves contractibility; hence the whole matching complex is contractible.

If exactly one petal length is divisible by three, \(A\) is contractible. Every spoke link except the two from the distinguished petal is contractible. Each of the two exceptional links is the join of \(B_i\simeq S^{k-2}\) with spheres from all other petals, hence is \(S^{K-2}\). Both attach by null-homotopic maps into the contractible base, creating two copies of its suspension \(S^{K-1}\). Any other, contractible, spoke links do not change the homotopy type.

If no petal length is divisible by three, all factors \(A_i\) are spheres, so \(A\simeq S^{K-1}\). Links for lengths congruent to one are contractible and can be discarded up to homotopy. For every length congruent to two, the corresponding two spoke links map to \(A\) by homotopy equivalences, by Step 2 and preservation under joins. If there are no such petals, nothing changes and the result is \(S^{K-1}\). Otherwise, the first such cone makes the union contractible (the mapping cone of a homotopy equivalence); every remaining spoke link maps through \(A\), which is now null-homotopic, and thus contributes the suspension of \(S^{K-1}\). There are exactly \(2\nu_2-1\) remaining cones, giving \(\bigvee^{2\nu_2-1}S^K\).

All joins and cone attachments are genuine simplicial cofibrations. Therefore these are integral homotopy equivalences, not merely equalities of Betti numbers or field-coefficient statements. \(\square\)

## Verification

The standalone `verify.py` enumerates exact faces of the ordinary matching complexes for 48 distinct mixed and repeated petal patterns of two or three cycles with total at most 19 graph edges, constructs signed simplicial boundary columns, and computes reduced homology ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\). All 48 patterns matched the four-case theorem in each field, with up to 3,937 nonempty faces in a tested complex. Important test cases: \((3,3)\) is contractible; \((3,4)\) has two circles; \((4,5)\) has one two-sphere; \((5,5)\) has three two-spheres; and \((3,3,5)\) is contractible. Run `python3 verify.py` and compare to `verify_output.txt`. These finite field checks are **not** a proof of torsion-freeness or of the infinite theorem; the integral homotopy argument above provides both.

## Relationship to prior work

Donovan and Scoville's Theorem 5.8 computes matching-complex homotopy types for **Dutch windmills with all petals the same cycle length**. Its three congruence cases are recovered here when \(m_1=\cdots=m_r\), and are not claimed as new. The present classification allows each petal to have an independently chosen length and, in particular, discovers the separate \(\nu_0=1\) regime and the mixed-residue interactions that are invisible in the homogeneous statement. Bayer, Jelić Milutinović, and Vega's general outerplanar theorem guarantees that matching complexes are contractible or wedges of spheres, but does not give dimensions, exact multiplicities, or the mixed-bouquet contractibility criterion. Their polygonal-line tiling results study edge-gluing rather than bouquets glued at a single vertex.

## Limitations

This theorem concerns ordinary matching complexes, not perfect-matching-extendability, multipath, or strong discrete-Morse matching complexes. It does not cover petals joined along edges, cycle chords, different hub vertices, or any persistence maps under graph modifications. The conclusion is homotopy nonequivariant: it does not determine the representation of petal permutations or reflections on homology. Literature searches and accessible comparisons do not logically establish global uniqueness; unindexed equivalent formulations or general gluing theorems that already imply these exact formulas remain a residual originality risk.

## References

1. C. Donovan and N. A. Scoville, *Star clusters in the matching, Morse, and generalized complex of discrete Morse functions*, arXiv:2207.13780, first public 2022-07-27; New York Journal of Mathematics 29 (2023), 1393–1412. Theorem 5.8: homogeneous Dutch windmills. https://nyjm.albany.edu/j/2023/29-54v.pdf
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601, first public 2024-11-07, Theorem 2 (general wedge-or-contractible result). https://arxiv.org/abs/2411.04601
3. M. Bayer, M. Jelić Milutinović and J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, first public 2022-11-22. https://arxiv.org/abs/2211.12559
