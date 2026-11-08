# Palette-sensitive threshold-colouring stability under deletion of a bipartite star

## Finding
Let \(2\le m,n\) and \(0\le d\le n\). Obtain \(G_{m,n,d}\) from \(K_{m,n}\) by deleting \(d\) edges incident with one fixed vertex on the \(m\)-vertex shore. Let \(T_{m,n,d}(q)\) count assignments of \(q\) named colours, unused colours allowed, whose every induced monochromatic graph is threshold. For nonnegative integers \(a,b,c\), write the exponential generating series
\[
F(x,y,z)=(1+x)e^{y+z}+(1+y+z)e^x-(1+x)(1+y+z),
\]
\[
H(x,y,z)=e^{y+z}+(e^x-1)(1+y+z),\qquad E(y)=e^y-1-y.
\]
Then for every integer \(q\ge1\),
\[
\boxed{T_{m,n,d}(q)=q(m-1)!d!(n-d)![x^{m-1}y^dz^{n-d}]\bigl(H+xE(y)\bigr)F^{q-1}.}
\]
Consequently the **exact increase under deletion** is
\[
\boxed{\Delta_{m,n,d}(q)=q(m-1)!d!(n-d)![x^{m-2}y^dz^{n-d}]E(y)F^{q-1}.}
\]
A coefficient with negative exponent is defined as zero. For \(d\le1\), this increase vanishes for every palette size. For \(d\ge2\) it is positive for each \(q\ge3\), while for \(q=2\) it is positive exactly when \(m\le3\) or \(n-d\le1\). For \(q=1\), it is positive exactly when \(m=2\) and \(d=n\). Thus, when \(m\ge4\), one can delete as many as \(n-2\) edges at a vertex without changing the two-colour count, although the three-colour count changes after just two deletions. These thresholds are sharp, for every indicated integer parameter range.

## Assumptions and scope
All graphs are finite, simple and labelled. A threshold graph is one with no induced \(P_4\), \(C_4\), or \(2K_2\). A colour class may be empty. The distinguished vertex is on the \(m\)-shore; precisely \(d\) of its neighbours are deleted. The exponential series are formal; the displayed coefficients involve finitely many terms. Each \(q\) counts named (not necessarily surjective) colourings. The result is exact for all \(m,n\ge2\), \(0\le d\le n\), \(q\ge1\).

## Proof
Call the distinguished left vertex \(u\), the other \(m-1\) left vertices ordinary, the \(d\) deleted-edge endpoints \(D\), and the other \(n-d\) right vertices \(R\). Consider any monochromatic colour class with \(a\) ordinary vertices, \(b\) in \(D\), and \(c\) in \(R\).

**Ordinary classes.** If the class does not contain \(u\), its induced graph is \(K_{a,b+c}\). Such a graph is threshold precisely if \(a\le1\) or \(b+c\le1\): the larger case contains an induced \(C_4\), while a star or independent set is threshold. Its exponential weight sum is \(F\). The subtraction in \(F\) removes the intersection \(a\le1,b+c\le1\) counted twice.

**The class containing \(u\).** If \(a=0\), its graph is a star with \(c\) edges and \(b\) isolates and is threshold. If \(a\ge1\) and \(b+c\le1\), it is a star together with possible isolates and is threshold. These cases contribute \(H\). When \(a\ge2\) and \(b+c\ge2\), two ordinary left vertices and two right vertices induce \(C_4\), so such a class cannot be threshold. When \(a=1\) and \(b+c\ge2\), any selected right vertex in \(R\), together with one selected vertex in \(D\) or another in \(R\), induces respectively \(P_4\) or \(C_4\) on the two left and two right vertices; hence the class is threshold exactly when \(c=0\) and \(b\ge2\). In this last case its graph is a star plus the isolate \(u\), contributing the extra term \(xE(y)\). These cases exhaust all possibilities.

Select the named colour of \(u\) in \(q\) ways and independently distribute the remaining labelled vertices among that special class (weight \(H+xE(y)\)) and \(q-1\) ordinary classes (weight \(F\)). Multivariate exponential coefficient extraction with factorial factors proves the first formula. For the undeleted graph the special class has generating function \(H\); subtracting yields the correction \(\Delta\), proving the second formula.

Since \(E(y)\) has no monomial below degree two, \(\Delta=0\) for \(d\le1\). For \(q\ge3\) and \(d\ge2\), choose \(u\) with exactly one ordinary vertex and two deleted right neighbours, put all remaining ordinary vertices into a second colour, and all remaining right vertices into a third colour. Both latter classes are independent, giving a strict increase. For \(q=2\), the extraordinary class must contain \(u\), one ordinary vertex and at least two deleted right neighbours, and no right vertices in \(R\). The opposite class consists of \(m-2\) ordinary left vertices and the remaining right vertices, whose count is at least \(n-d\). It is threshold if and only if the left count is at most one (equivalently \(m\le3\)) or its right count can be made at most one (equivalently \(n-d\le1\), by choosing every deleted neighbour for the special class). This proves the two-colour threshold and its sharpness. For \(q=1\), the only possible extraordinary class is the whole graph, requiring exactly one ordinary left vertex and all right vertices in \(D\); equivalently \(m=2,d=n\). No other configurations give a new colouring.

## Verification
The standalone Python verifier `artifacts/verify.py` independently enumerates named assignments, constructs the bipartite graph, tests every induced four-vertex subgraph for forbidden \(P_4,C_4,2K_2\), and compares the resulting total with the exact multivariate exponential-coefficient expression. It tests all \(m,n\in\{2,3,4\}\), all \(0\le d\le n\), and all \(q\in\{1,2,3\}\) for which there are at most 20,000 assignments. The last replay ended `VERIFY_OK`. The infinite theorem rests on the preceding structural argument, not on this finite enumeration.

## Relationship to prior work
Bang-Jensen, Bessy and Reinald, *Acyclic 2-edge-coloured graphs: polynomial-time linkages and colouring hardness* (first posted 2026-10-23, arXiv:2610.32954v1), establish the equivalence between alternating-acyclic induced classes and threshold classes, and the hardness of finding two-class partitions on general inputs. Classical threshold-graph theory characterizes the forbidden induced four-vertex graphs. Previous enumerations of threshold colourings on complete multipartite graphs supply the undeleted \(K_{m,n}\) baseline, but a missing-edge star is not complete multipartite when \(d>0\) and \(n-d>0\). The exact coefficient correction and contrasting sharp two-/three-colour thresholds are not part of that baseline. No claim of independence or exhaustive historical priority is made.

## Limitations
This theorem treats deletions incident with a single vertex, not arbitrary deleted bipartite edge sets. It counts named assignments with empty classes allowed, not colourings subject to conventional adjacent-vertex propriety. Priority remains provisional pending wider historical review; independent validation has not been performed.

## References
1. J. Bang-Jensen, S. Bessy and L. Reinald, *Acyclic 2-edge-coloured graphs: polynomial-time linkages and colouring hardness*, arXiv:2610.32954v1 (2026-10-23), https://arxiv.org/abs/2610.32954 .
2. Classical threshold-graph forbidden induced-subgraph characterization (Chvátal–Hammer); see https://mathworld.wolfram.com/ThresholdGraph.html .
3. M. Demange, T. Ekim and D. de Werra, *A tutorial on the use of graph coloring for some problems in analysis and optimization*, European Journal of Operational Research (2009), DOI:10.1016/j.ejor.2007.09.018 .
