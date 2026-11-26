# Linear-size identifying codes for undirected two-letter de Bruijn networks

## Finding

For an integer \(q\ge3\), let \(\mathcal B(q,2)\) be the undirected graph with vertices \((a,b)\in\{0,\ldots,q-1\}^2\) and overlap edges \(ab\)--\(bc\). A radius-one identifying code \(C\) is a set of vertices such that every closed neighborhood has a nonempty intersection with \(C\), and all these intersections are different. If \(\gamma(q)\) is the minimum size, then
\[
q\le\gamma(q)\le q+\lfloor q/3\rfloor.
\]
The upper bound is attained by the explicit code below. Listing the code uses \(O(q)\) operations on alphabet labels (in the word-RAM model); its size is at most \(4/3\) times optimum. The contribution is the uniform bound and construction, not the known small-alphabet optima.

## Assumptions and scope

Coordinates of words are ordered and adjacency is undirected. Loops are irrelevant for closed neighborhoods, and diagonal words \((a,a)\) are vertices. For any selected set \(C\) let \(R_b=\{(b,u)\in C\}\) and \(K_a=\{(u,a)\in C\}\). Then the signature is exactly
\[
I_C(a,b)=R_b\cup K_a\cup(\{(a,b)\}\cap C).
\]
Indeed the two possible overlaps start with \(b\) or end with \(a\), and the closed neighborhood also contains \((a,b)\).

## Proof

**Lower bound.** Suppose \(|C|<q\). If two rows \(R_b,R_{b'}\) are empty, then for every \(a\) the signatures of \((a,b)\) and \((a,b')\) differ only if at least one of those two vertices belongs to \(C\). These are disjoint pairs for distinct \(a\), forcing \(|C|\ge q\), a contradiction. By exchanging coordinates, at most one column is empty. Since \(|C|<q\), there is exactly one empty row \(r\) and one empty column \(c\); \(|C|=q-1\) and every other row and column contains one selected pair. Domination of \((c,r)\) requires \((c,r)\in C\); in particular \(c\ne r\). There is another codeword \((i,j)\) since \(q\ge3\), with \(i\notin\{r,c\}\) and \(j\notin\{r,c\}\). The distinct vertices \((j,r)\) and \((c,i)\) both have signature \(\{(i,j)\}\). Their own membership cannot add a codeword because row \(j\) cannot contain \((j,r)\) (column \(r\) is occupied solely by \((c,r)\)), and row \(c\) is occupied solely by \((c,r)\). This contradiction proves the lower bound.

**Templates.** On blocks of \(s=3,4,5\) symbols use the indicated ordered lists:
\[
T_3=(01,02,10,20),\quad T_4=(00,12,13,21,31),\quad T_5=(01,02,13,24,30,41).
\]
Assign bit \(2^h\) to entry \(h+1\). Direct evaluation of the signature formula gives these masks (row \(a\), column \(b\)):
\[
M_3=\begin{pmatrix}15&13&14\\7&5&9\\11&6&10\end{pmatrix},\quad
M_4=\begin{pmatrix}1&7&9&17\\25&30&26&28\\3&14&10&18\\5&22&12&20\end{pmatrix},\quad
M_5=\begin{pmatrix}19&21&26&16&48\\35&37&41&53&33\\3&6&10&18&42\\23&4&12&20&36\\11&44&8&24&40\end{pmatrix}.
\]
Each matrix has distinct positive entries. Every row support and column support in all three templates is nonempty. The row supports in \(T_3\) are \(\{01,02\},\{10\},\{20\}\); its column supports are \(\{10,20\},\{01\},\{02\}\). Thus no \(T_3\) row support equals a \(T_3\) column support.

**Block composition.** For \(q=3m\), partition into \(m\) triples. For \(q=3m+1\) or \(q=3m+2\), use one block of size four or five respectively and \(m-1\) triples. Take the union of the relabeled templates; no selected pair joins two different blocks. A word with both symbols in one block has its checked local signature, supported only in that block. If \((a,b)\) uses distinct blocks \(A,B\), its signature is \(K_a\cup R_b\), supported nontrivially in both blocks; its unordered pair of blocks is therefore recoverable. For fixed ordered blocks \((A,B)\), equality of signatures forces equality of columns and of rows, since different columns are disjoint and nonempty, as are different rows. If the order of blocks is reversed, equality would require a row to equal a column inside *each* block, impossible because at least one of the two blocks is a triple. Thus domination and separation hold across the graph. The code size is \(4m,4m+1,4m+2\) respectively, giving \(q+\lfloor q/3\rfloor\), and the templates can be listed in one pass. The claimed approximation ratio follows from the lower bound.

## Verification

The masks and block argument prove the uniform claim. The supplementary programs `check_bounds.py` and `check_adjacency.py` are standard-library Python diagnostics of the signature and adjacency formulations; they check the construction for \(3\le q\le100\). The first program's exhaustive exclusions for \(q=3,4,5\) reproduce known values and are not needed for the uniform theorem.

## Relationship to prior work and limitations

Horan [1, Theorem 2.1 and §4] proves existence for the relevant undirected graph and poses efficient construction and minimum-cardinality questions. Horan, Adachi and Bak [2, Figures 8–9] give minimum sizes by finite computation. In particular, their tables already give \(\gamma(3)=4,\gamma(4)=5,\gamma(5)=6\); Figure 9 also reports exact \(\gamma(6)=8,\gamma(7)=9\) and a size-ten code for \(q=8\) without certifying it as minimum. Those entries are benchmarks, not claims of novelty here. They do not give the uniform approximation or block construction above. The directed problem studied by Boutin, Horan Goliber and Pelto [3] uses different neighborhoods. The lower bound is a baseline: there are at most \(|C|\) singleton signatures, and each selected word appears in at most \(2q\) signatures, giving \(2q^2-|C|\le 2q|C|\) and hence \(|C|\ge q\) by rounding. The bound here is not an exact all-alphabet formula; a smaller code can exist where the two bounds differ. This comparison does not exclude historical equivalences outside the sources inspected.

## References

1. V. Horan, *On the Existence of \(t\)-Identifying Codes in Undirected De Bruijn Graphs*, https://arxiv.org/abs/1508.00403.
2. V. Horan, S. Adachi and M. Bak, *A Comparison of Approaches for Finding Minimum Identifying Codes on Graphs*, https://arxiv.org/abs/1504.08011v2, Figures 8–9.
3. D. Boutin, V. Horan Goliber and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, https://arxiv.org/abs/1412.5842.
