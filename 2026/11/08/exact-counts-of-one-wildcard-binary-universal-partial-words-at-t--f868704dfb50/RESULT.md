# Exact counts of one-wildcard binary universal partial words at the first two positions

## Finding

Fix the labeled binary alphabet \(\{0,1\}\) and the wildcard \(\diamond\). A *linear universal partial word of order* \(n\) contains each of the \(2^n\) ordinary binary length-\(n\) words at exactly one starting position, with \(\diamond\) allowed to match either digit. We require exactly one wildcard. Let \(N_k(n)\) count these literal linear words when the wildcard occupies position \(k\), without identifying complementary or reversed words.

**Theorem.** For every integer \(n\ge2\),
\[
N_1(n)=2^{\,2^{n-1}-n+1}.
\]
For the next position, \(N_2(2)=0\), \(N_2(3)=2\), and for every \(n\ge4\),
\[
N_2(n)=\frac{2^{n-2}-(-1)^n}{3}\,2^{\,2^{n-1}-2n+2}.
\]
A word counted by \(N_k(n)\) has exactly \(2^n+n-k-1\) symbols. The first counts for \(n=2,3,4,5,6,7\) are respectively \((2,4,32,4096,134217728,288230376151711744)\), and the second counts are \((0,2,4,768,20971520,49539595901075456)\).

## Assumptions and scope

Windows are linear and consecutive, not cyclic; a wildcard-covered window represents two ordinary words, whereas an ordinary window represents one. Different binary words are counted with their alphabet labels and end positions intact. Write \(B_m\) for the binary directed de Bruijn graph with vertices the \(m\)-bit strings, and an edge \(x_1\cdots x_m\to x_2\cdots x_m b\) for each appended digit \(b\). Parallel-edge bookkeeping is by the associated \((m+1)\)-bit string. A directed *in-arborescence rooted at* \(r\) has, from every other vertex, a unique oriented path leading to \(r\).

The prefix restrictions used below are the elementary forced-prefix lemma for one-wildcard upwords, stated and proved as Lemma 4 in Chen–Kitaev–Mütze–Sun (2016/2017). For completeness: comparing the two consecutive wildcard-containing windows with the ordinary windows immediately to their right forces the symbols outside the wildcard to repeat at period equal to its position, with the last symbol of the forced prefix complemented. When the wildcard is first, its normalized prefix is \(\diamond0^{n-1}1\); when second and \(n\ge3\), the prefix is \(0\diamond c(01,n)\), where \(c(01,n)\) is the alternating length-\(n\) word with its final bit complemented. Global bit complementation gives the only other possibilities. The alternative third bit zero in the second-position case repeats the constant word in the first two windows and is forbidden. The published proof supplies the unrestricted forced-prefix statement; nothing below assumes that mere existence implies an enumeration.

## Proof

**1. The full graph's tree count.** Put \(m=n-1\), \(Q=2^m\), and let \(A\) be the adjacency matrix of \(B_m\). It has constant in- and out-degree two. With \(P=A/2\), the \(m\)-step random walk is uniform, so \(P^m=J/Q\). Thus the eigenvalues of \(A\) are two once and zero \(Q-1\) times, counted algebraically. The directed matrix-tree theorem, together with the constant-root tree count for an Eulerian graph, gives exactly
\[
T_m=\frac{2^{Q-1}}{Q}=2^{\,2^m-m-1}
\]
in-arborescences at each specified root.

The open-trail form of the directed BEST theorem states that a directed graph with unique imbalance \(\operatorname{out}(s)-\operatorname{in}(s)=1\) and \(\operatorname{in}(r)-\operatorname{out}(r)=1\) has
\[
t_r\prod_v\bigl(\operatorname{out}(v)-1+\mathbf1_{v=r}\bigr)!
\]
Euler trails from \(s\) to \(r\), where \(t_r\) counts its in-arborescences at \(r\). In the graphs below, every remaining positive out-degree is one or two and the factorial product equals one. The directed graphs are connected by the existence constructions of Chen et al., Theorems 9–10, and, independently, positivity of the tree determinant computed below; all remaining edges are explicitly distinguished by their ordinary binary words.

**2. Wildcard in position one.** Normalize the first bit after the wildcard to zero. The first wildcard window represents the edges \(0^n\) (a loop at \(0^m\)) and \(10^{n-1}\) (from \(10^{m-1}\) to \(0^m\)). Remove both from \(B_m\). The remaining edges must, and conversely may, be traversed as one Euler trail from \(0^m\) to \(10^{m-1}\). At \(0^m\), its only available outgoing edge is the forced \(0^m1\), so the required longer initial prefix occurs automatically. The removed loop cannot belong to a spanning tree; the removed edge departs from the designated root \(10^{m-1}\) and likewise cannot occur in an in-arborescence rooted there. Consequently there are \(T_m\) permitted trails per normalized initial bit. Global complementation doubles the count, giving \(N_1(n)=2T_m\).

**3. Second-position residual graph.** For \(n\ge4\), normalize the prefix to \(w=0\diamond c(01,n)\) of length \(n+2\). The first three length-\(n\) windows specify five distinct edges: two completions of each wildcard window and the next ordinary window. Put
\[
C=(01\cdots)_{m},\quad a=0C_1\cdots C_{m-1},\quad b=1C_1\cdots C_{m-1},\quad r=0a_1\cdots a_{m-1}.
\]
The five deleted edges are exactly \(r\to a,\ a\to C,\ C\to b,\ b\to C,\ C\to z\), where \(z\) is the final \(m\)-bit suffix of \(w\). The vertex \(C\) becomes isolated. The remaining graph has an open Euler trail from \(z\) to \(r\). Its arborescence count \(t'_r\), hence the number of completions of this prefix, equals the rooted-tree count of the vertex-deleted graph \(B_m-C\): the further missing edge \(r\to a\) cannot belong to an in-arborescence rooted at \(r\). The graph \(B_m-C\) loses one outgoing edge at each of the two distinct in-neighbors \(a,b\) of \(C\). Every remaining vertex has positive out-degree one or two except the designated terminal root, and the open BEST factorial factor remains one.

**4. Evaluate the vertex deletion, without a growing determinant.** Use the full-graph Laplacian \(L=2I-A\) and delete root row and column \(r\) to obtain \(L_r\). For any \(m\)-bit words \(x,y\), define
\[
S(x,y)=\sum_{j=0}^{m-1}2^{-j}\mathbf1\{x_{j+1}\cdots x_m=y_1\cdots y_{m-j}\},
\]
\[
K(x,y)=\tfrac12\bigl[S(x,y)-S(r,y)-S(x,r)+S(r,r)\bigr].
\]
The matrix \(K\), restricted to vertices other than \(r\), equals \(L_r^{-1}\). Indeed \(S=I+P+\cdots+P^{m-1}\), so \((I-P)S=I-J/Q\). Taking the differences of the indicated rows and columns enforces zero at the deleted root; multiplying by \(2(I-P)\) gives the identity on the retained rows. Thus this is an explicit finite inverse rather than an asymptotic approximation.

Delete the row/column of \(C\) from \(L_r\), then decrease the two diagonal entries at \(a,b\) by one. The matrix determinant lemma together with the complementary-minor identity gives
\[
\frac{t'_r}{T_m}=
\det\begin{pmatrix}
K(C,C)&K(C,a)&K(C,b)\\
K(a,C)&K(a,a)-1&K(a,b)\\
K(b,C)&K(b,a)&K(b,b)-1
\end{pmatrix}.
\]
This equality can also be checked by multiplying the right side by \(\det L_r\) and expanding the three specified rows/columns. The removed edge exiting \(r\) does not affect the root-deleted Laplacian.

At \(n=4\), direct substitution in the finite overlap sum yields the unadjusted matrix
\[
K|_{(C,a,b)}=\begin{pmatrix}5/4&1/2&1\\1&1&1\\1&1/2&3/2\end{pmatrix},
\]
whose determinant after the two diagonal subtractions is \(1/8\). For every \(n\ge5\), the same overlap sum, summing the terminating alternating geometric progressions, gives
\[
K|_{(C,a,b)}=
\begin{pmatrix}
1&1/4&3/4\\
g&3/4&h\\
g&1/4&h+1/2
\end{pmatrix},
\quad g=\frac23+\frac{(-1)^n}{3\cdot2^{n-2}},\quad
h=\frac7{12}+\frac{(-1)^n}{3\cdot2^{n-3}}.
\]
For clarity, each displayed entry is obtained simply by testing whether the indicated suffix of one of \(r,C,a,b\) matches the indicated prefix of another, for each shift \(j=0,\ldots,m-1\), and adding \(2^{-j}\); no probabilistic independence assumption is used. Subtracting one from the last two diagonal entries gives determinant \((4g-4h+1)/8\). Both the exceptional \(n=4\) table and the generic expression simplify to
\[
\frac{t'_r}{T_m}=\frac{2^{n-2}-(-1)^n}{3\cdot2^{n-1}}
\qquad(n\ge4).
\]
There are two complementary normalized prefixes. Hence \(N_2(n)=2t'_r\), and substituting \(T_m\) yields the claimed formula. For \(n=3\), direct inspection of the two forced prefixes gives one completion apiece, namely `0*011100` and its bit complement. For \(n=2\), no second-position upword exists, because the two wildcard-covered length-two words would overlap the ordinary window; this also follows from Theorem 6 of Chen et al. This finishes all cases.

## Verification

The standalone, standard-library `verify.py` directly enumerates every possible word at wildcard positions one and two for \(n=2,3,4\), obtaining respectively \((2,0),(4,2),(32,4)\). Independently, a fraction-free integer determinant computes the second-position rooted-tree count for \(n=4,5,6,7\): \(2,384,10485760,24769797950537728\) per normalized prefix, each matching the formula. A third calculation evaluates the explicit three-by-three Green determinant for \(4\le n\le12\), matching the parity formula term by term. Execute `python3 verify.py` in the extracted package. These finite checks support, but do not replace, the all-order proof.

## Relationship to prior work

Chen, Kitaev, Mütze and Sun introduced universal partial words and proved forced-prefix constraints and existence at each of these two wildcard locations (Lemma 4 and Theorems 9 and 10). Existence is not a count. The new content is the exact count at both positions, including the parity-sensitive rooted-tree deletion formula for the second position. The de Bruijn graph, directed matrix-tree theorem and BEST theorem are classical, and their use alone is not asserted to be new. Subsequent literature on multiple wildcards and cyclic partial words addresses different domains. A comprehensive historical-priority guarantee is not claimed.

## Limitations

The result concerns one wildcard, two fixed positions, a binary alphabet and linear rather than cyclic windows. Counts at later wildcard positions and with multiple wildcards are not determined. The determinant evaluation is explicit but its closed form presumes the stated forced-prefix lemma from the cited primary literature; it is not a self-contained new proof of that published lemma. Finite computational checks do not certify all orders, and independent scientific review has not been performed.

## References

1. H. Z. Q. Chen, S. Kitaev, T. Mütze, B. Y. Sun, *On universal partial words*, arXiv:1601.06456, originally submitted 25 January 2016; *Discrete Mathematics & Theoretical Computer Science* 19 (2017), DOI: 10.23638/DMTCS-19-1-16. Primary open source: https://arxiv.org/abs/1601.06456 ; accessible full text: https://dmtcs.episciences.org/en/articles/2205/download . Relevant Lemma 4, Theorems 6, 9 and 10.
2. B. Goeckner, C. Groothuis, C. Hettle, B. Kell, P. Kirkpatrick, R. Kirsch, R. Solava, *Universal Partial Words over Non-Binary Alphabets*, arXiv:1611.03928 (first posted 12 November 2016), 2018 journal version. Related, but later, enumerative questions: https://arxiv.org/abs/1611.03928 .
3. N. G. de Bruijn, *A combinatorial problem*, *Proc. Koninklijke Nederlandse Akademie van Wetenschappen* 49 (1946), 758–764; classical full-graph sequence enumeration.
4. T. van Aardenne-Ehrenfest and N. G. de Bruijn, *Circuits and trees in oriented linear graphs*, *Simon Stevin* 28 (1951), 203–217; directed BEST formula and tree enumeration.
