# Integral torsion-freeness at the ninth Stirling rook complex

## Finding
Let \(\operatorname{St}(9)\) be the simplicial complex of all nonattacking rook placements on the staircase Ferrers board with nine rows of lengths \(1,2,\ldots,9\). Then its **complete reduced integral homology** is
\[
\widetilde H_j(\operatorname{St}(9);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{402},&j=4,\\
\mathbb Z^{815},&j=5,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, this explicitly studied first case beyond the published table is **torsion-free**. No assertion about its complete homotopy type is made.

## Assumptions and scope
Label board positions by \((i,j)\) for \(0\le i\le j\le8\). A face is a subset in which the two coordinates of any two chosen positions are distinct. This is the complex \(\operatorname{St}(9)\) of Clark and Zeckner (2010), comprising \(45\) vertices and \(115975\) faces including the empty face. The alternative strict triangular convention on \(1\le i<j\le10\) gives the same complex after shifting the second coordinate. All statements concern ordinary integral simplicial homology, with reduced degree \(-1\) represented by the empty simplex.

## Proof
**1. Exact cell enumeration.** Scan the nine rows in increasing order. In each row either place no rook or select one column not used by earlier rows. Enumerating these mutually exclusive choices produces each face exactly once. For placements with \(k\) rooks the counts, for \(k=0,1,\ldots,9\), are
\[
(1,45,750,5880,22827,42525,34105,9330,511,1).
\]
They independently agree with the Stirling-number formula \(S(10,10-k)\).

**2. A complete acyclic matching.** Fix lexicographic order on the 45 positions. At each position in turn, match every as-yet-unmatched face not using that position to the face obtained by adding it, provided both remain unmatched. This is a matching on the full augmented face poset. Directly orient each matched cover upward and every other cover downward. An exhaustive directed topological sort visits all \(115975\) vertices across all \(597155\) Hasse incidences, proving acyclicity for this finite complex. The critical-face counts, indexed by **number of rooks**, are
\[
 c_5=1096,\qquad c_6=1728,\qquad c_7=220,\qquad c_8=1,
\]
with every other count zero. Discrete algebraic Morse reduction over \(\mathbb Z\) therefore yields free chain groups in topological degrees \(4,5,6,7\) of those ranks and no other nonzero groups.

**3. Exact signed Morse differentials.** In increasing position order the incidence sign when deleting the \(r\)-th rook is \((-1)^{r-1}\). For a critical face \(x\), define its projection to the Morse basis to be \(x\); for a face that is the *upper* member of a matched pair, the projection is zero. If a lower matched face \(x\) is paired with \(y\), use the unit-coefficient boundary relation
\[
 p(x)=-[x:y]\sum_{\substack{z\subset y,\ |z|=|x|\\z\ne x}}[z:y]p(z),
\]
where \([z:y]\in\{+1,-1\}\). Acyclicity makes this finite recursion well founded. Projecting the signed boundary of every critical face gives the complete integer Morse boundary matrices. In increasing degrees, their respective dimensions and nonzero-entry counts are
\[
\begin{array}{c|r|r}
\text{boundary}&\text{matrix dimensions}&\text{nonzero entries}\\\hline
\partial_5&1096\times1728&4036\\
\partial_6&1728\times220&1019\\
\partial_7&220\times1&6
\end{array}
\]
Here matrix subscripts denote the **topological source degree**. Multiplication verifies both successive boundary compositions are zero, entry by entry.

**4. Unimodular elimination.** Integer elementary row and column operations at entries equal to \(\pm1\) eliminate respectively \(694\), \(219\), and \(1\) pivots in these three matrices; all remaining entries vanish. The exact operations use integral Schur updates and are verified in the attached executable. Consequently every nonzero Smith invariant factor is one: the boundary images are primitive and no integral homology group has torsion. The reduced Betti ranks are
\[
1096-694=402,\qquad 1728-694-219=815,\qquad220-219-1=0,\qquad1-1=0.
\]
No other reduced chain groups survive. This proves the claim.

## Verification
Run `python3 stirling9_verify.py` with the Python standard library only. The program generates every face, proves the matching is acyclic by a complete topological-sort check, constructs all signed Morse matrices via recursive elimination, verifies that consecutive differentials compose to zero, and performs integer unit-pivot eliminations until the residual matrices vanish. Its output is included in `stirling9_check_output.txt`; the final marker is `STIRLING_INTEGRAL_CERTIFICATE_OK`.

As a cross-check, the same procedure for \(\operatorname{St}(8)\) reproduces the previously published reduced Betti ranks \((24,292,1)\) in degrees \((3,4,5)\). The direct reduced Euler characteristic for \(\operatorname{St}(9)\) is \(-413=402-815\).

## Relationship to prior work
Ehrenborg and Hetyei (2006) introduced the triangular rook/Stirling independence complex and asked about its topology. Barmak (first public July 2, 2010) established connectivity bounds for this matching-complex family. Clark and Zeckner (first public August 26, 2010), Sections 5–6, gave a partial Morse description and integral Betti data through \(\operatorname{St}(8)\), explicitly identifying \(\operatorname{St}(9)\) as the first uncomputed case and asking whether it has torsion. Their partial statements neither determine the above two ranks nor settle its integral torsion question. The present calculation addresses that precise finite case. The later cubical resource-allocation spaces called *Stirling complexes* (Kozlov, 2022/2023) are a differently defined family, not the staircase rook complex considered here.

## Limitations
This proof gives complete **integral homology**, not a wedge decomposition or attaching-map/homotopy classification. The algorithm is exhaustive only for the stated finite nine-row board; there is no extrapolation to larger boards. The code is an exact, reproducible computational certificate rather than an independent formal proof assistant. A related 2011 dissertation by Zeckner is identifiable, but its full text could not be inspected; it remains a priority-comparison risk. Searches of available literature and indexed findings cannot certify absolute publication novelty.

## References
1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European J. Combin. 27 (2006), 906–923. https://doi.org/10.1016/j.ejc.2005.04.010
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2010-07-02), Section 5. https://arxiv.org/abs/1007.0418
3. E. Clark and M. Zeckner, *Simplicial Complexes of Triangular Ferrers Boards*, arXiv:1008.4525v1 (2010-08-26), especially Sections 5–6 and Table 1. https://arxiv.org/abs/1008.4525
4. M. Zeckner, *Topological and combinatorial properties of neighborhood and chessboard complexes*, dissertation, University of Kentucky (2011), https://uknowledge.uky.edu/gradschool_diss/163/ (full text not inspected).
5. D. N. Kozlov, *Stirling complexes*, J. Appl. Comput. Topol. 7 (2023), 57–74, https://doi.org/10.1007/s41468-022-00096-4 (different definition).
