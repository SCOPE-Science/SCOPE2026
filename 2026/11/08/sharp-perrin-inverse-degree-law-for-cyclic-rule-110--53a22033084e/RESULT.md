# Sharp Perrin inverse-degree law for cyclic Rule 110

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous, indexed cyclic elementary cellular automaton Rule 110, defined for every integer \(n\ge1\) by
\[
 F_n(x)_i=f(x_{i-1},x_i,x_{i+1}),\qquad
 f(abc)=\begin{cases}0,&abc\in\{000,100,111\},\\1,&abc\in\{001,010,011,101,110\},\end{cases}
\]
with indices modulo \(n\). Define the one-step inverse degree \(d_n(y)=|\{x\in\{0,1\}^n:F_n(x)=y\}|\). Let \(P_0=3\), \(P_1=0\), \(P_2=2\), and \(P_n=P_{n-2}+P_{n-3}\) for \(n\ge3\), the Perrin sequence.

**Theorem.** For every \(n\ge5\),
\[
 \max_{y\in\{0,1\}^n}d_n(y)=P_n,
 \qquad d_n(y)=P_n\ \Longleftrightarrow\ y=1^n.
\]
For the exceptional sizes \(1\le n\le4\), the maximum inverse degrees are respectively \(2,2,3,2\). The maximizing outputs are respectively \(\{0\}\), \(\{00,11\}\), \(\{111\}\), and \(\{0000,1111,0111,1011,1101,1110\}\). These are indexed configurations; no quotient by rotation is taken.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), the update is synchronous, every site is indexed, and the boundary is cyclic even at sizes one and two. Each predecessor is a distinct indexed binary word. There are no boundary padding cells, no probabilistic errors, and exactly one update.

## Proof

**1. The labeled pair graph.** Order the pair states as \(00,01,10,11\). A transition \(ab\to bc\) has label \(f(abc)\). The adjacency matrices for labels zero and one are
\[
M_0=\begin{pmatrix}1&0&0&0\\0&0&0&0\\1&0&0&0\\0&0&0&1\end{pmatrix},\quad
M_1=\begin{pmatrix}0&1&0&0\\0&0&1&1\\0&1&0&0\\0&0&1&0\end{pmatrix}.
\]
Each indexed predecessor is exactly one closed length-\(n\) path with prescribed edge labels. Hence for any \(y\),
\[
d_n(y)=\operatorname{tr}(M_{y_0}M_{y_1}\cdots M_{y_{n-1}}).\tag{1}
\]
This remains true for \(n=1,2\), where repeated indices are interpreted cyclically.

**2. All-one output.** The only recurrent states of the label-one graph are \(01,10,11\), with adjacency matrix
\[
 B=\begin{pmatrix}0&1&1\\1&0&0\\0&1&0\end{pmatrix},
 \qquad\det(tI-B)=t^3-t-1.
\]
Consequently \(d_n(1^n)=\operatorname{tr}(B^n)=P_n\) for all \(n\ge1\), by Cayley--Hamilton and the initial traces \(3,0,2\) at exponents zero, one and two.

**3. Every output containing zero.** Immediately after traversing an edge labeled zero, the only possible pair states are \(00\) and \(11\). If \(k\) consecutive ones occur before the next zero, the transfer on these two states is
\[
H_0=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
H_1=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
H_2=\begin{pmatrix}1&1\\0&0\end{pmatrix},
\quad H_{k+3}=H_{k+1}+H_k\ (k\ge0).\tag{2}
\]
For \(k\ge1\), specifically,
\[
H_k=\begin{pmatrix}(M_1^k)_{00,10}&(M_1^k)_{00,11}\\(M_1^k)_{11,10}&(M_1^k)_{11,11}\end{pmatrix}.
\]
The recurrence in (2) follows from the cubic characteristic polynomial of the recurrent label-one subgraph, with its \(k=0\) instance checked directly from \(H_3=H_1+H_0\). If the output has \(r\ge1\) zeros, and \(k_1,\ldots,k_r\ge0\) are the cyclic numbers of intervening ones, then
\[
d_n(y)=\operatorname{tr}(H_{k_1}\cdots H_{k_r}),\qquad n=r+\sum_{i=1}^rk_i.\tag{3}
\]

**4. A sharp matrix-merging inequality.** For all positive integers \(a,b\), except \((a,b)=(1,2)\), there is an entrywise inequality
\[
H_aH_b\ \le\ H_{a+b+1}.\tag{4}
\]
Here entrywise means every difference entry is nonnegative. To verify (4) without an infinite search, put \(D(a,b)=H_{a+b+1}-H_aH_b\). Equation (2) implies the two *exact* recurrences
\[
D(a+3,b)=D(a+1,b)+D(a,b),\quad
D(a,b+3)=D(a,b+1)+D(a,b).\tag{5}
\]
Thus it suffices to check the following 19 explicit base pairs by integer \(2\times2\) multiplication:
\[
\begin{gathered}
(a,b)\in\{4,5,6\}\times\{0,1,2\},\\
(a,b)\in\{2,3\}\times\{1,2,3\},\\
(a,b)\in\{(1,1),(1,3),(1,4),(1,5)\}.
\end{gathered}
\]
All 19 yield entrywise nonnegative differences, as reproduced exactly by `verify_certificate.py`. The recurrences first extend the nine checks in the first rectangle to \(a\ge4,b\ge0\); the next six checks cover \(a\in\{2,3\},b\ge1\); and the final four cover \(a=1,b=1\) or \(b\ge3\). The single excluded difference is
\[
D(1,2)=\begin{pmatrix}1&1\\0&-1\end{pmatrix}.
\]
This proves (4), including its precise exception, from finite arithmetic and (5).

Discard every \(H_0=I\) factor in (3). If no factors remain, then \(d_n(y)=2\). Otherwise suppose the remaining \(s\ge1\) factors have strictly positive indices \(\ell_1,\ldots,\ell_s\), and put \(m=s+\sum_j\ell_j\le n\). For \(s\ge2\), a cyclic list of positive indices always has some adjacent ordered pair other than \((1,2)\): otherwise every index would simultaneously have to be one and two. Rotate the trace to place such a pair first, use (4), and repeat. Nonnegative matrix multiplication and monotonicity of trace preserve the inequality. Each merger replaces \(H_aH_b\) by \(H_{a+b+1}\), keeps \(m\) invariant, and reduces the number of factors by one. Hence
\[
 d_n(y)\le h_{m-1},\qquad h_k:=\operatorname{tr}(H_k),\qquad 2\le m\le n,\tag{6}
\]
for all non-all-zero outputs with at least one zero.

**5. Strict bound and equality.** From (2), \(h_{k+3}=h_{k+1}+h_k\), with \((h_1,h_2,h_3)=(0,1,2)\). Therefore the sequence \(P_{k+1}-h_k\) has the same recurrence and starts \((2,2,0)\) for \(k=1,2,3\). It is nonnegative for every \(k\ge1\), strictly positive for every \(k\ge4\), and zero only at \(k=3\). For \(n\ge5\), \(P_n\ge5\), and \(P_n\) is nondecreasing with \(n\) from index five onward. If \(m\le4\), (6) is at most \(2<P_n\). If \(m\ge5\), it is strictly less than \(P_m\le P_n\). The all-zero output has exactly two predecessors, also strictly below \(P_n\). Thus every output with a zero has strictly fewer than \(P_n\) predecessors when \(n\ge5\). Combined with step 2, this proves the theorem and uniqueness. The four exceptional cases follow directly from (1) or the complete enumerator in the accompanying package. \(\square\)

## Verification

Execute `python3 verify_certificate.py` to reconstruct the two labeled adjacency matrices, all initial transfer matrices, the 19 entrywise base comparisons, the recurrence and Perrin comparisons, and the zero-run transfer identity on every output for lengths up to eleven. The executable also performs extra larger-instance spot checks, which are not substituted for the all-length proof.

Independently run `python3 verify_direct.py` to evaluate Rule 110 directly on every one of the \(2^n\) input words for each \(1\le n\le18\), then compute every output's inverse degree and compare the maxima, extremizers and Perrin values. This second implementation does not use adjacency or transfer matrices. The infinite result rests on the explicit recurrence and finite-base argument above, not on the bounded enumeration.

## Relationship to prior work

The de Bruijn preimage trace formula and the homogeneous-output enumeration method are established in Powley (2009), especially Chapter 9, Theorem 9.5 and Example 9.2. In particular, the Perrin sequence for the all-one output follows from known homogeneous-output transfer matrices; it is not claimed as a new recurrence. The freely accessible Rule 110 worked example in Wikibooks also gives the same two labeled adjacency matrices and concrete periodic examples. Neither inspected discussion establishes that this output is the **global unique worst-case inverse fiber** among all \(2^n\) indexed outputs for every \(n\ge5\). The entrywise merger inequality and its exceptional orientation supply that missing all-output comparison. McIntosh (2000) studies periodic motifs and glider structures rather than inverse-degree extremizers. Related cellular-automaton results for other local rules are not substitutes for this specific cyclic Rule 110 extremal comparison.

## Limitations

The result concerns only one synchronous predecessor step on finite binary cyclic rings. It does not determine the complete inverse-degree histogram, multistep predecessor counts, or arbitrary-boundary systems. It does not claim that the Perrin numbers themselves are newly discovered. The first verified public date used for historical scoping is the explicit June 4, 2000 date displayed on the McIntosh source; other earlier general literature may exist, and independent historical-priority verification remains necessary.

## References

1. E. J. Powley, *Global properties of cellular automata*, University of York PhD thesis, October 2009, especially Chapter 9, §§9.1–9.3 and Theorem 9.5. https://www.cs.york.ac.uk/nature/group/theses/EdPowley.pdf
2. H. V. McIntosh, *A Concordance for Rule 110*, originally dated June 4, 2000, additions May 14, 2002. https://delta.cs.cinvestav.mx/~mcintosh/comun/ccord/ccord.html
3. *Cellular Automata/Examples on Rule 110*, Wikibooks, sections on preimage matrices, boundary conditions and cyclic preimages. https://en.wikibooks.org/wiki/Cellular_Automata/Examples_on_Rule_110
4. E. W. Weisstein, *Rule 110*, MathWorld, mathematical definition and bibliographic background. https://mathworld.wolfram.com/Rule110.html
5. *MSC2020 Database*, Mathematical Reviews, classification 68Q80. https://mathscinet.ams.org/mathscinet/msc/msc2020.html
