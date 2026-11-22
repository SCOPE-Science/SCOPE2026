# A six-periodic seam law for degree-two cuts of cubic ladders

## Finding
For each integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the \(n\)-rung circular ladder. Let \(M_{2n}\) be the cubic Möbius ladder obtained from the same two-row strip by interchanging the two rail connections at its closing seam. A *degree-two cut* (or *2-cut*) is an unordered bipartition into two nonempty vertex classes such that every vertex has at most two neighbors in the opposite class. Write \(N_P(n)\) and \(N_M(n)\) for the numbers of such cuts in these labelled graphs.

**Theorem.** Define three integer sequences by
\[
\begin{aligned}
 B_0&=4,&B_1&=3,&B_2&=11,&B_3&=36,\\
 B_n&=3B_{n-1}+B_{n-2}-2B_{n-4} &&(n\ge4),\\
 A_0&=2,&A_1&=0,&A_n&=-2A_{n-2} &&(n\ge2),\\
 C_0&=2,&C_1&=1,&C_n&=C_{n-1}-C_{n-2} &&(n\ge2).
\end{aligned}
\]
Then, for every \(n\ge3\),
\[
 N_P(n)=\frac{B_n+A_n+C_n-2}{2},\qquad
 N_M(n)=\frac{B_n+A_n-C_n-2}{2}.
\]
In particular, the *exact* effect of twisting the closing seam is
\[
 \boxed{N_P(n)-N_M(n)=C_n=2\cos(n\pi/3).}
\]
This difference is six-periodic, taking the values \(-2,-1,1,2,1,-1\) as \(n\equiv3,4,5,0,1,2\pmod6\), respectively. Its absolute value never exceeds two, although both counts are at least \(2^{n-1}-1\).

## Assumptions and scope
All graphs are simple and their two vertex rows and \(n\) columns are labelled. The vertices are \((i,j)\) with \(0\le i<n\) and \(j\in\{0,1\}\). Rungs join \((i,0)\) to \((i,1)\); ordinary rail edges join equal rows in consecutive columns. The two seam edges from column \(n-1\) to column zero preserve rows for \(P_n\), and cross the rows for \(M_{2n}\). At \(n=3\), these are the triangular prism and \(K_{3,3}\), respectively. A bipartition is counted only once when its two classes are interchanged; monochromatic two-colourings do not count because the classes must both be nonempty.

Since these graphs are cubic, a vertex has at most two neighbors across the cut if and only if it has at least one neighbor in its own part. Thus the ordered version of the problem is to count binary vertex colourings in which every vertex has a same-coloured neighbor.

## Proof
**1. The exact transfer.** Write the colour pair in column \(i\) as \(a_i\in\mathcal A=\{00,01,10,11\}\), with each symbol recording the colours of the upper and lower vertices. The local admissibility predicate for three successive columns \(a,b,c\in\mathcal A\) is
\[
 L(a,b,c)=[b_0=b_1]\ \lor\
 \bigwedge_{j=0}^{1}\bigl([b_j=a_j]\lor[b_j=c_j]\bigr).
\]
Indeed, a monochromatic rung supplies a same-coloured neighbor to both middle vertices. Otherwise, each of those two vertices must find such a neighbor along at least one rail.

Index a \(16\times16\) integer matrix \(U\) by ordered pairs \((a,b)\in\mathcal A^2\) and set
\[
 U_{(a,b),(b',c)}=\begin{cases}1,&b'=b\text{ and }L(a,b,c),\\0,&\text{otherwise.}\end{cases}
\]
Let \(J\) simultaneously interchange the upper and lower coordinates in both columns of a pair. It is an involution commuting with \(U\). A closed walk of length \(n\) in \(U\) is exactly a labelled locally valid binary colouring of \(P_n\), so the number is \(\operatorname{tr}(U^n)\). A walk closing after application of \(J\) is exactly a locally valid binary colouring of \(M_{2n}\), giving \(\operatorname{tr}(U^nJ)\). These bijections also hold for \(n=3\), when the strip closes around three columns.

The \(+1\) and \(-1\) eigenspaces of \(J\) have respective dimensions ten and six. The exact integral restrictions \(U_+\) and \(U_-\) are obtained by using, for every two-element row-swap orbit \(\{s,Js\}\), the vectors \(e_s+e_{Js}\) and \(e_s-e_{Js}\), and by retaining the four fixed singleton vectors only in the positive space. Direct integer determinant calculation gives
\[
 \det(xI-U_+)=x^4(x^2+2)(x^4-3x^3-x^2+2),\qquad
 \det(xI-U_-)=x^4(x^2-x+1).
\]
The accompanying standalone verifier constructs both restrictions from the displayed local predicate, computes their characteristic polynomials exactly with integer arithmetic, and checks these two factorizations. This is a finite, fully specified certificate, not an extrapolation from sampled graph sizes.

Let \(B_n\) be the power sum of the four roots of \(x^4-3x^3-x^2+2\), \(A_n\) the power sum of the two roots of \(x^2+2\), and \(C_n\) the power sum of the two roots of \(x^2-x+1\). Newton identities and the respective characteristic equations yield precisely the stated integer recurrences and initial values. The four zero eigenvalues in each block contribute nothing to a trace of a positive matrix power. Consequently, for every \(n\ge1\),
\[
 \operatorname{tr}(U^n)=B_n+A_n+C_n,\qquad
 \operatorname{tr}(U^nJ)=B_n+A_n-C_n.
\]
Each trace includes both constant colourings, corresponding to partitions with an empty class. Every other valid colouring is paired with its global colour complement, which has the same unordered cut. Subtracting two and dividing by two proves the two exact counting formulas. Since \(x^2-x+1\) has roots \(e^{\pm i\pi/3}\), their power sum is \(C_n=2\cos(n\pi/3)\).

**2. Why only mixed rungs detect the seam twist.** A second, structural explanation isolates the bounded correction. Suppose a valid binary colouring contains at least one monochromatic rung. Let \(j\) be its last such rung in the linear column order, and interchange the two row colours in every column strictly after \(j\), retaining columns through \(j\). Rung monochromaticity is unchanged. Away from column \(j\), both sides of a local predicate are simultaneously row-interchanged. At \(j\), the predicate is automatic; at \(j+1\), the predecessor has equal entries in both rows, so its effect is unaffected by interchanging the middle row labels. The seam simultaneously changes from straight to crossed. Thus the transformed colouring is valid for the opposite seam, and applying the map twice recovers the original. It bijects all valid straight-seam and twisted-seam colourings that have a monochromatic rung.

For colourings whose every rung is mixed, encode each column by its upper bit. A middle bit must equal at least one of its two neighbors. The four-state transfer on consecutive upper bits, in the order \(00,01,10,11\), is
\[
 T=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
Complementing both bits commutes with this matrix. Its symmetric and antisymmetric two-dimensional blocks have respective characteristic polynomials \(x^2-x-1\) and \(x^2-x+1\). Hence exactly the antisymmetric block contributes to the seam difference: the ordered-colouring counts differ by \(2C_n\), which becomes \(C_n\) for unordered cuts. This independently explains the period-six cancellation without relying on the 16-state absolute census.

**3. Nontrivial size.** Every choice of one bit per column with upper and lower bits equal gives a valid colouring on either graph, since each rung protects both its endpoints. Removing the two constant choices and identifying global complements yields at least \(2^{n-1}-1\) distinct degree-two cuts in each graph. The correction of absolute size at most two is therefore exponentially small relative to either count.

## Verification
Run `python3 verify.py` using the standard Python library. The script constructs the \(16\)-state matrix from the local predicate, verifies the two rational-block characteristic polynomials exactly using integer Faddeev–LeVerrier recursion, checks all binary colourings on both graphs for \(3\le n\le8\) using a separate explicit adjacency-list enumeration, tests the monochromatic-rung seam bijection exhaustively on the same lengths, and checks both complete counting formulas and the period-six difference for \(3\le n\le100\). The direct graph counts for \(n=3,4,5,6,7,8\) are respectively \((16,18),(58,59),(181,180),(581,579),(1912,1911),(6230,6231)\), where each pair is \((N_P,N_M)\). The unrestricted result follows from the exact transfer and matrix identity, not from these finite samples.

## Relationship to prior work
Kwon, Park and Sano study partitions into *two total dominating sets* and related four-colourings. Their condition demands that **both** colours occur in every open neighborhood; the present degree-two-cut condition on a cubic graph requires only a neighbor in the vertex's **own** colour. The two-total-dominating-set condition implies the degree-two-cut condition on a cubic graph, but its converse fails; their theorems concern existence and structure on planar triangulations, not the enumeration of the larger class on these cubic ladder families. Lopez-Bonilla, Allagan and Morgan already develop the ordinary and twisted transfer-trace method for the **proper-colouring chromatic polynomials** of these very two graph families. Their state space demands adjacent vertices have different colours; the current two-colour states require a same-coloured neighbor, so neither their four chromatic spectral branches nor their chromatic polynomials give these degree-two-cut counts. The cyclic/twisted trace principle itself is therefore not claimed as new. Gomes and Sau define general \(d\)-cuts and investigate algorithmic decision complexity; their results do not state these two exact enumerators or the seam correction. Rotenberg, Rutschmann and Thomassen prove an existence result for partitions into two total dominating sets in planar graphs, not counts of degree-two cuts.

The novelty claim is restricted to the explicit enumeration and the exact bounded six-periodic twist law for these graph families; it does not assert the novelty of transfer matrices, the graph families, or the existence of degree-two cuts.

## Limitations
No classification is claimed for all cubic graphs, for fixed cut size, or for partitions with an additional requirement that each side itself totally dominate the entire graph. The graph families are labelled, and the theorem counts nonempty unordered bipartitions, not equivalence classes under graph automorphisms. The finite program provides an exact reproducible certificate for the stated matrix identities; no independent mathematical audit has been conducted. Historical priority beyond the inspected literature remains provisional.

## References
1. R. Lopez-Bonilla, J. D. Allagan and G. C. Morgan, *Quartic Equimodular Curves and Spectral Reductions in Prism-Derived Chromatic Polynomials*, first public preprint June 9, 2026, https://www.preprints.org/manuscript/202606.0590 ; published in *Symmetry* 18(7), 1180 (2026), https://doi.org/10.3390/sym18071180
2. H. Kwon, B. Park and Y. Sano, *Total dominating sets and four-colorings of planar triangulations*, arXiv:2611.00572, first posted October 31, 2026. https://arxiv.org/abs/2611.00572
3. G. C. M. Gomes and I. Sau, *Finding Cuts of Bounded Degree: Complexity, FPT and Exact Algorithms, and Kernelization*, arXiv:1905.03134 (2019). https://arxiv.org/abs/1905.03134
4. E. Rotenberg, M. Rutschmann and C. Thomassen, *Disjoint Total Dominating Sets in Planar Graphs*, Journal of Graph Theory (2026), DOI:10.1002/jgt.70032. https://doi.org/10.1002/jgt.70032
