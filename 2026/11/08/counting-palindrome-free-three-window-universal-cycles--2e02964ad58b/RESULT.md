# Counting palindrome-free three-window universal cycles

## Finding

Let \(q\ge2\) be an integer and let \(\Sigma_q=\{0,1,\ldots,q-1\}\) be a labeled alphabet. Call a cyclic word *palindrome-free three-window universal* when its consecutive cyclic windows of length three are exactly the distinct triples \(abc\in\Sigma_q^3\) with \(a\ne c\), each once. Two cyclic words are identified precisely when one is a rotation of the other, not under reversal or alphabet relabeling. The length is necessarily \(q^2(q-1)\).

**Theorem.** The number \(C_q\) of such cyclic words is \(C_2=1\) and, for every integer \(q\ge3\),
\[
C_q=q^{(q+3)(q-2)/2}(q-1)^{q-1}
(q-2)^{(q-1)(q-2)/2}\bigl((q-2)!\bigr)^{q^2}.
\]
In particular, \(C_3=108\), \(C_4=231928233984\), and \(C_5=1295354998363672018944000000000000\).

## Assumptions and scope

A word is indexed over the fixed alphabet \(\Sigma_q\). Positions of a cyclic word are taken modulo its length. A *cyclic three-window* at position \(i\) is the ordered triple of symbols at positions \(i,i+1,i+2\). The condition \(a\ne c\) removes exactly the palindromic triples of length three (including constant triples). A cyclic word is represented once per orbit of cyclic rotation; no other equivalence relation is imposed. Every admissible triple must occur, not merely a maximal subset.

## Proof

**1. Directed overlap graph and Euler correspondence.** Define a directed graph \(G_q\) whose \(q^2\) vertices are the ordered pairs \((a,b)\in\Sigma_q^2\), with one arc
\[
 (a,b)\longrightarrow(b,c)\qquad\text{for each }a\ne c.
\]
Label the arc by its unique triple \(abc\). Each vertex has indegree and outdegree \(q-1\). For distinct \(a,b\), the two-edge path
\[
(a,a)\to(a,b)\to(b,b)
\]
connects diagonal vertices, and every off-diagonal vertex \((a,b)\) lies on such a path. Hence \(G_q\) is strongly connected. Every Euler circuit lists the admissible triples exactly once and produces the required cyclic word by reading their overlapping symbols. Conversely every required word gives an Euler circuit. Since every triple is a distinct labeled arc, every Euler circuit has a unique rotation placing any fixed arc first. This identifies the rotational quotient correctly even for potentially periodic symbol strings; no nontrivial period can repeat the distinct arcs.

**2. Characteristic polynomial.** Let \(B\) be the adjacency matrix of \(G_q\), with rows and columns indexed by pairs. Define the \(q^2\times q\) matrix \(U\), the \(q\times q^2\) matrix \(V\), and the reversal permutation \(R\) by
\[
U_{(a,b),j}=\mathbf1_{b=j},\qquad
V_{j,(d,e)}=\mathbf1_{j=d},\qquad
R_{(a,b),(d,e)}=\mathbf1_{(d,e)=(b,a)}.
\]
Then \(B=UV-R\), \(VU=J_q\), and \(VRU=qI_q\), where \(J_q\) is the all-ones matrix. The reversal permutation has \(q(q+1)/2\) positive and \(q(q-1)/2\) negative eigenvalues. For indeterminate \(t\), the determinant lemma and
\[
(tI+R)^{-1}=\frac{tI-R}{t^2-1}
\]
give
\[
\begin{aligned}
\det(tI-B)
&=\det(tI+R)\det\!\left(I_q-\frac{tVU-VRU}{t^2-1}\right)\\
&=(t+1)^{q(q+1)/2}(t-1)^{q(q-1)/2}
\frac{(t-1)(t-(q-1))(t^2+q-1)^{q-1}}{(t^2-1)^q}\\
&=(t-(q-1))(t-1)^{(q-1)(q-2)/2}
(t+1)^{q(q-1)/2}(t^2+q-1)^{q-1}.
\end{aligned}
\]
The rational identity is first valid away from \(t=\pm1\) and extends polynomially there.

**3. Exact arborescence count.** Let \(L=(q-1)I_{q^2}-B\). This is the outdegree Laplacian of a strongly connected balanced digraph. By the directed matrix-tree theorem, every root has the same number \(\tau_q\) of spanning in-arborescences, since \(L\) has a one-dimensional zero eigenspace and its adjugate is \(\tau_qJ_{q^2}\). If \(p_q(t)=\det(tI-B)\), then
\[
\tau_q=\frac{p'_q(q-1)}{q^2}.
\]
For \(q\ge3\), substitution of the factored polynomial yields
\[
\begin{aligned}
\tau_q
&=\frac{(q-2)^{(q-1)(q-2)/2}
q^{q(q-1)/2}\bigl(q(q-1)\bigr)^{q-1}}{q^2}\\
&=q^{(q+3)(q-2)/2}(q-1)^{q-1}
(q-2)^{(q-1)(q-2)/2}.
\end{aligned}
\]
For \(q=2\) the same derivative computation gives \(\tau_2=1\), avoiding an ambiguous \(0^0\) notation.

**4. Euler-circuit multiplicity.** The directed BEST theorem, with a fixed labeled first arc to eliminate cyclic starting-point multiplicity, counts Euler circuits as
\[
C_q=\tau_q\prod_{v\in V(G_q)}(\deg^+(v)-1)!
=\tau_q\bigl((q-2)!\bigr)^{q^2}.
\]
Combining this with the preceding evaluation proves the formula for all \(q\ge2\). For \(q=2\) the overlap graph is one directed four-cycle, so \(C_2=1\) directly. \(\square\)

## Verification

The standalone script `verify.py` independently creates the complete directed overlap graph, evaluates a directed Laplacian cofactor by exact Bareiss integer elimination, compares it with the formula for every \(2\le q\le6\), and enumerates all labeled Euler circuits from a fixed arc by direct edge-subset search for \(q=2,3\). The independent C++17 program `crosscheck.cpp` enumerates all local orders of outgoing arcs and counts those producing one Euler circuit for \(q=2,3\). Its output agrees with the closed formula. Both programs require no datasets or libraries beyond the Python standard library and a C++17 compiler, respectively. Exact counts through \(q=6\) are also in `counts.csv`.

Run from this directory:

```sh
python3 verify.py
c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck
./crosscheck
```

Expected last lines are `VERIFY_OK` and `CROSSCHECK_OK`. The finite checks are supplementary: the proof establishes the result for every integer alphabet size in the stated range.

## Relationship to prior work

Leitner and Godbole (2008 preprint; 2010 journal article) established existence of universal cycles in several restricted families, notably non-bijections and equitable words. Their publicly available paper does not evaluate the number of cycles for the present length-three nonpalindromic family. Chen, Kitaev, and Sun (2019 preprint; 2020 article) study probabilities of existence when words are removed from the full collection and give special small deletion cases, not this exact count. Sawada and Gabrić (2025 preprint) give general methods to sample universal cycles via graph arborescences, including several de Bruijn variants, but not this evaluated product. The directed matrix-tree and BEST theorems are classical tools, not newly claimed. The new result here is the particular spectral factorization, evaluated spanning-tree count, and resulting all-alphabet cyclic enumeration.

## Limitations

The theorem concerns windows of length exactly three, disallows every palindromic three-window, and identifies rotations alone. It does not count longer-window palindrome restrictions, reversal classes, or alphabet relabeling classes. Neither the general BEST theorem nor existence of restricted universal cycles is a novelty claim. Earlier unindexed calculations or equivalent consequences of more general nonbacktracking-operator results remain possible; this result has not undergone independent historical-priority or mathematical audit.

## References

1. A. Leitner and A. Godbole, *Universal Cycles of Restricted Classes of Words*, arXiv:0808.1309, first posted 2008-08-08. https://arxiv.org/abs/0808.1309
2. H. Z. Q. Chen, S. Kitaev, and B. Y. Sun, *On the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, arXiv:1908.01116, first posted 2019-08-03. https://arxiv.org/abs/1908.01116
3. J. Sawada and D. Gabrić, *Random Generation of Universal Cycles and de Bruijn Sequences*, arXiv:2510.16545, first posted 2025-10-18. https://arxiv.org/abs/2510.16545
4. N. G. de Bruijn, T. van Aardenne-Ehrenfest and classical directed BEST/matrix-tree counting results (standard graph-enumeration tools).
