# Linear-size identifying codes for undirected two-letter de Bruijn networks

## Finding
Let \(q\ge3\) be an integer. Write \(\mathcal B(q,2)\) for the undirected de Bruijn graph whose vertices are the ordered pairs in \(\{0,\ldots,q-1\}^2\), with an edge between \(ab\) and \(bc\) for any three symbols \(a,b,c\). Loops are immaterial because identifying signatures use closed neighborhoods. Let \(\gamma(q)\) be the minimum number of vertices in a radius-one identifying code: a selected set meeting each closed neighborhood in a nonempty, pairwise-distinct set.

**Theorem.** For every integer \(q\ge3\),
\[
q\le\gamma(q)\le q+\left\lfloor\frac q3\right\rfloor.
\]
The upper bound is attained by an explicit code constructible in \(O(q)\) time; thus its cardinality is at most \(4/3\) times optimum. Moreover,
\[
\gamma(3)=4,\qquad\gamma(4)=5,\qquad\gamma(5)=6.
\]
No assertion that the upper bound is optimal for \(q\ge6\) is made.

## Assumptions and scope
Symbols are labeled and the two coordinates are ordered. The graph is undirected, formed by forgetting orientations in the usual de Bruijn overlap digraph. For a candidate code \(C\) of ordered pairs, write
\[
R_b=\{(b,t)\in C\},\qquad K_a=\{(t,a)\in C\}.
\]
The identifying signature of vertex \((a,b)\) is exactly
\[
I_C(a,b)=R_b\cup K_a\cup (\{(a,b)\}\cap C).
\]
The unusual reversal of indices is essential: outgoing neighbors of \((a,b)\) start with \(b\), and incoming neighbors end with \(a\). All quantifiers include the diagonal vertices \((a,a)\) and all pairs of distinct vertices.

## Proof
**Lower bound.** Suppose \(|C|<q\). If two rows \(R_b,R_{b'}\) are empty, then for every \(a\), distinct vertices \((a,b),(a,b')\) can have different signatures only if at least one of \((a,b),(a,b')\) belongs to \(C\). These are distinct selected pairs as \(a\) varies, hence \(|C|\ge q\), contradiction. Thus at most one row is empty; the dual argument gives at most one empty column. Since \(|C|<q\), at least one row and one column are empty, so \(|C|=q-1\), with exactly one empty row \(r\) and one empty column \(c\). Every other row and column then contains exactly one code pair. To have \(I_C(c,r)\ne\varnothing\), the pair \((c,r)\) must belong to \(C\). Because \(q\ge3\), choose another code pair \((i,j)\). Necessarily \(i\ne r,c\) and \(j\ne r,c\). By uniqueness in occupied rows and columns,
\[
I_C(j,r)=\{(i,j)\}=I_C(c,i).
\]
These are different vertices, contradiction. Therefore \(|C|\ge q\).

**Three finite blocks.** On \(s\in\{3,4,5\}\) symbols, define the following sets of selected ordered pairs (using digits as symbols):

* \(T_3=\{01,02,10,20\}\).
* \(T_4=\{00,12,13,21,31\}\).
* \(T_5=\{01,02,13,24,30,41\}\).

Each block by itself is an identifying code. A self-contained finite certificate is the following table of signature masks. Assign bit \(2^h\) to the \((h+1)\)-st listed code pair and read each matrix in row-major order, with rows indexed by \(a\) and columns by \(b\). Every mask in each matrix is positive and occurs exactly once:

\[
M_3=\begin{pmatrix}15&13&14\\7&5&9\\11&6&10\end{pmatrix},
\]
\[
M_4=\begin{pmatrix}1&7&9&17\\25&30&26&28\\3&14&10&18\\5&22&12&20\end{pmatrix},
\]
\[
M_5=\begin{pmatrix}19&21&26&16&48\\35&37&41&53&33\\3&6&10&18&42\\23&4&12&20&36\\11&44&8&24&40\end{pmatrix}.
\]
These masks are derived by the preceding explicit signature formula, so they can also be checked without trusting an optimization solver. Every row support and column support of every template is nonempty. In \(T_3\) no row support equals any column support: its row supports are \(\{01,02\},\{10\},\{20\}\) and its column supports are \(\{10,20\},\{01\},\{02\}\).

**Combining blocks.** Partition the \(q\) symbols into blocks. For \(q=3k\) use \(k\) blocks of size three; for \(q=3k+1\) use one block of size four and \(k-1\) of size three; for \(q=3k+2\) use one block of size five and \(k-1\) of size three. Translate each block template to its assigned symbol labels and take their disjoint union \(C\). Code pairs never connect different blocks.

For vertices whose two symbols belong to the same block, signatures are precisely the verified local signatures, supported only in that block. For vertices \((a,b)\) with \(a,b\) in two different blocks \(A,B\), their signature is \(K_a\cup R_b\), with nonempty supports in both blocks. Such a signature cannot equal a within-block signature. The two involved blocks are recoverable from its support. Within a fixed ordered pair of distinct blocks, two signatures can agree only if both the selected columns and selected rows agree, forcing the same \(a,b\), since different columns (respectively rows) are disjoint and nonempty. If the two blocks are exchanged, equality would require some selected row to equal a selected column **inside both blocks**. This is impossible because there is at most one block of size four or five, and every pair of distinct blocks includes a size-three block, for which no such equality occurs. Hence every signature is nonempty and unique.

The code size is \(4k\), \(4k+1\), or \(4k+2\) respectively, exactly \(q+\lfloor q/3\rfloor\). The construction lists a constant number of pairs per block, giving linear construction time. Since \(\gamma(q)\ge q\), its size divided by optimum is at most \(1+\lfloor q/3\rfloor/q\le4/3\).

**First sharp cases.** For \(q=3,4,5\), the construction has \(q+1\) codewords. There is no \(q\)-element identifying code: a complete enumeration of the \(\binom{q^2}{q}\) candidates tests respectively \(84,1820,53130\) subsets, all failing the signature test. A smaller code could be extended to a \(q\)-element code because the defining property is preserved by adding sensors; hence no smaller code exists. The standalone checker implements the entire finite enumeration. A second program builds undirected graph adjacency explicitly and independently verifies the construction.

## Verification
Execute `python3 check_bounds.py` and `python3 check_adjacency.py` using Python 3 and the standard library. It verifies the three explicit signature matrices, exhaustively rejects all \(q\)-element code sets at \(q=3,4,5\), and independently reconstructs and checks the family at every \(3\le q\le100\). The universal statement for all larger \(q\) follows from the block-union proof, not from those numerical checks. The finite enumerator iterates every combination of the asserted size, without sampling or early cutoff.

## Relationship to prior work
Horan (2015, first arXiv version 3 August 2015) established identifiability for undirected \(\mathcal B(d,n)\) when \(d\ge3,n\ge2t\), including \(n=2,t=1\), and explicitly posed efficient and minimum-cardinality code construction as a future problem. That existence result does not give the present linear sensor bound or the small exact optima. Boutin, Horan Goliber and Pelto (2014) studied **directed** de Bruijn identifying codes: their neighborhood signatures and lower bounds do not transfer to undirected balls. This theorem uses the undirected graph and proves both a nontrivial scalable approximation guarantee and sharp first alphabet sizes.

## Limitations
The optimal value for \(q\ge6\) is not determined by this theorem; computations on additional alphabets would not prove an all-alphabet equality. The factor at most \(4/3\) is an upper bound against the proved elementary lower bound and may be improvable. No independent peer review has occurred. Historical priority under different graph or sensor terminology is not excluded.

## References
1. V. Horan, *On the Existence of \(t\)-Identifying Codes in Undirected De Bruijn Graphs*, arXiv:1508.00403v1, posted 2015-08-03. https://arxiv.org/abs/1508.00403
2. D. Boutin, V. Horan Goliber, M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842v1, posted 2014-12-18. https://arxiv.org/abs/1412.5842
