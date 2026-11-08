# Two-winding enumeration of Eulerian orientations on odd cycle squares

## Finding

For every odd integer \(n\ge5\), let \(C_n^2\) be the simple graph on the labelled vertices \(\mathbb Z/n\mathbb Z\), with edges joining each \(i\) to \(i+1\) and to \(i+2\) (indices modulo \(n\)). An Eulerian orientation directs each edge so that every vertex has indegree and outdegree both equal to \(2\). Let \(a_i=1\) if the edge from \(i\) to \(i+1\) is oriented forward and \(a_i=0\) otherwise. Let \(b_i\) similarly indicate a forward direction on the edge from \(i\) to \(i+2\). Set \(A=\sum_i a_i\), \(B=\sum_i b_i\), and define the two-winding enumerator
\[
E_n(u,v)=\sum_{\omega\ {\rm Eulerian}}u^{A(\omega)}v^{B(\omega)}.
\]
The complete enumerator is
\[
\boxed{E_n(u,v)=1+(uv)^n+
\sum_{j=0}^{(n-1)/2}\frac{n}{n-j}\binom{n-j}{j}
\left(u^{n-2j}v^j+u^{2j}v^{n-j}\right).}
\]
Thus exactly \(n+3\) distinct winding pairs \((A,B)\) are attainable. The two extreme pairs \((0,0)\) and \((n,n)\) occur once each. Every other attainable pair belongs to one of the two disjoint families \((n-2j,j)\) and \((2j,n-j)\), and occurs exactly \(\frac{n}{n-j}\binom{n-j}{j}\) times, where \(0\le j\le(n-1)/2\). In particular, the unweighted count is \(2+2L_n\), where \(L_0=2\), \(L_1=1\), and \(L_n=L_{n-1}+L_{n-2}\) are Lucas numbers.

## Assumptions and scope

The orientation variables refer to *labelled, fixed-position* edges, not isomorphism classes of orientations. Each edge is counted exactly once because \(n\ge5\). The polynomial remembers two distinct forward-edge counts relative to the specified cyclic order. The theorem claims the full polynomial for **odd** \(n\ge5\); its proof also yields the same identity for even \(n\ge6\), but the even-order case overlaps an existing explicit classification of Eulerian orientations of antiprism graphs and is not advanced as a new claim.

## Proof

For each vertex \(i\), its two outgoing forward edges contribute \(a_i+b_i\), while its two incident backward edges contribute \(2-a_{i-1}-b_{i-2}\). Hence the Eulerian condition is equivalent, with no omitted conditions, to
\[
a_i+b_i=a_{i-1}+b_{i-2}\qquad(i\in\mathbb Z/n\mathbb Z).
\]
Define the state before vertex \(i\) to be \(s_i=(a_{i-1},b_{i-2},b_{i-1})\in\{0,1\}^3\). A state \(s=(a,b,c)\) may transition to \(s'=(x,c,y)\) exactly when \(x+y=a+b\), and that transition has weight \(u^xv^y\). Cyclic state walks of length \(n\), with the starting index fixed at vertex \(0\), are in one-to-one correspondence with Eulerian orientations: recover all \(a_i,b_i\) from the successive edges, and the closed-state condition enforces the required index wrap-around. Thus \(E_n(u,v)=\operatorname{tr}(T^n)\), where
\[
T_{(a,b,c),(x,c,y)}=
\begin{cases}
u^xv^y,&x+y=a+b,\\
0,&\text{otherwise},
\end{cases}
\]
and all other entries vanish.

The eight states decompose into four closed transition classes: the singleton \(000\), the triple \(001,010,100\), the triple \(011,101,110\), and the singleton \(111\). There are no transitions between distinct classes. The singleton weights are \(1\) and \(uv\), respectively. With the triples in the displayed orders their weighted adjacency matrices are
\[
M_1=\begin{pmatrix}0&1&0\\v&0&u\\v&0&u\end{pmatrix},
\qquad
M_2=\begin{pmatrix}v&0&u\\v&0&u\\0&uv&0\end{pmatrix}.
\]
A direct determinant expansion gives
\[
\det(\lambda I-M_1)=\lambda(\lambda^2-u\lambda-v),
\qquad
\det(\lambda I-M_2)=\lambda(\lambda^2-v\lambda-u^2v).
\]
For indeterminates \(p,q\), let \(R_m(p,q)\) be the power sum of the roots of \(\lambda^2-p\lambda-q=0\). It satisfies \(R_0=2\), \(R_1=p\), \(R_m=pR_{m-1}+qR_{m-2}\). For every \(m\ge1\) its explicit expansion is
\[
R_m(p,q)=\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{m}{m-j}\binom{m-j}{j}p^{m-2j}q^j.
\]
This last formula follows either by induction from the recurrence or by counting cyclic monomer-dimer tilings of an \(m\)-cycle: a tiling with \(j\) dimers has \(m\binom{m-j}{j}/(m-j)\) placements. Taking traces of powers of the four diagonal blocks therefore yields
\[
E_n(u,v)=1+(uv)^n+R_n(u,v)+R_n(v,u^2v),
\]
which is precisely the displayed enumerator.

For odd \(n\ge5\), the listed pairs are distinct. Indeed, within each family the first coordinate changes strictly with \(j\). If \((n-2j,j)=(2k,n-k)\), then \(j=n-k\), giving \(n-2j=2n-2j\), impossible for positive \(n\). Neither special pair occurs in a family because the first family has \(A\ge1\) and \(B<n\), while the second has \(A<n\) and \(B\ge(n+1)/2\). This gives \(2+2((n+1)/2)=n+3\) supported pairs and their exact multiplicities. At \(u=v=1\), both quadratic power sums equal the Lucas number \(L_n\), proving the scalar consequence.

## Verification

The complete proof above is symbolic; the programs are finite cross-checks, not extrapolations. Run the embedded standalone scripts with Python 3:
```
python3 -S verify_direct.py
python3 -S verify_transfer.py
```
`verify_direct.py` independently enumerates all \(2^{2n}\) assignments of directions to the two jump classes for \(n=5,\ldots,9\), checks the two-in/two-out condition at every vertex and compares the bivariate coefficient dictionary with the formula. `verify_transfer.py` constructs the eight-state matrix from the local balance equation and multiplies exact two-variable polynomial matrices for \(n=5,\ldots,15\), comparing every coefficient. Both completed successfully. Their outputs are in `verify_direct.out` and `verify_transfer.out`. For odd orders \(n=5,7,9\), the total counts are \(24,60,154\), with respectively \(8,10,12\) supported winding pairs.

## Relationship to prior work

Felsner's 2004 paper establishes a general lattice theory of planar fixed-outdegree orientations, including Eulerian orientations, but not the stated two-direction enumerator. Golin and Leung (2004) prove that scalar Eulerian-orientation counts of fixed-jump circulants satisfy finite recurrences; their inspected conference paper explicitly treats the square of a cycle for other parameters, but does not give the two-variable support/multiplicity formula. Their cited longer technical report was not recovered. Isaev (first arXiv version 2011-10-12) proves asymptotics for graphs with algebraic connectivity proportional to order, a hypothesis inappropriate for fixed-degree cycle squares, and does not imply the formula.

A *separate prior classification* of balanced orientations of the \(m\)-antiprism determines their total count \(2+2L_{2m}\) and flip graph. Since the \(m\)-antiprism is isomorphic to \(C_{2m}^2\), that classification already covers the **unweighted even-order** count and some state structure. The present claim is explicitly restricted to the *odd-order two-winding distribution*, which is neither determined by the even-order count nor by an antiprism-only statement.

Zhang and Shen's 2007 work entitled *Counting the Eulerian orientations of one class of circulant graphs* is highly relevant, but only bibliographic metadata were accessible: no full text or statement of the graph class was recovered. It could cover the scalar count on the same graphs. The present claim does not rely on novelty of its unweighted specialization; whether that work contains the complete odd-order two-direction coefficient distribution remains an unresolved historical-priority risk.

## Limitations

This is a labelled-edge orientation count for odd squared cycles, not a result on orientation orbits under automorphisms. Nothing is claimed about the 2007 paper's uninspected contents. The method gives an even-order identity as a consistency check but does not seek priority for the already-covered even-order orientation count. Literature and database searches cannot certify absolute priority; no independent scholarly review has been performed.

## References

1. S. Felsner, *Lattice Structures from Planar Graphs*, Electronic Journal of Combinatorics **11** (2004), #R15, DOI `10.37236/1768`, publicly dated 2004-02-14. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r15/pdf/
2. M. J. Golin and Y.-C. Leung, *Unhooking Circulant Graphs: A Combinatorial Method for Counting Spanning Trees and Other Parameters*, WG 2004, LNCS 3353, 296–307 (2004). https://cse.hkust.edu.hk/~golin/pubs/golin_WG_04_new.pdf
3. M. Isaev, *Asymptotic behavior of the number of Eulerian orientations of graphs*, arXiv:`1110.2598`, first posted 2011-10-12. https://arxiv.org/abs/1110.2598
4. Y. Zhang and X. Shen, *Counting the Eulerian orientations of one class of circulant graphs* (2007); bibliographic record only, full text unavailable. https://www.researchgate.net/publication/266247805_Counting_the_Eulerian_orientations_of_one_class_of_circulant_graphs
