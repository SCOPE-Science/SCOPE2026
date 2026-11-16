# First nontrivial Walsh singularity of complete-graph forests: exact six-vertex cancellation orbits and sharp range projection

## Finding

Let \(E_n=\binom{[n]}2\), and identify each edge set \(F\subseteq E_n\) with its incidence vector in \(G_n=\mathbb F_2^{E_n}\). Write \(\mathcal F_n\) for all **acyclic** edge sets, including the empty set and all disconnected spanning forests (isolated vertices are allowed). For a frequency \(S\subseteq E_n\), define the *unnormalized* Walsh multiplier
\[
W_n(S)=\sum_{F\in\mathcal F_n}(-1)^{|F\cap S|}.
\]
Let \(T_nu=1_{\mathcal F_n}*u\) be the unnormalized counting-convolution operator on \(\ell^2(G_n)\). Then:

1. For \(n=3,4,5\), all Walsh multipliers are nonzero, and \(|\mathcal F_n|=7,38,291\), respectively. In contrast, \(n=6\) has \(|\mathcal F_6|=2932\) and exactly \(3105\) zero multipliers among the \(32768\) characters. Thus \(\operatorname{rank}T_6=29663\) and \(\dim\ker T_6=3105\).
2. The \(3105\) vanishing frequencies form exactly **ten** vertex-relabeling orbits. Their support-size distribution is
\[
\begin{array}{c|rrrr}
|S|&5&7&9&11\\\hline
\#\{S:W_6(S)=0\}&180&1080&1800&45.
\end{array}
\]
In particular, the minimum support size is five; all \(180\) minimum-support vanishing frequencies form one orbit, whose frequency graph is the disjoint union of a **paw** (a triangle with one pendant edge) and an isolated edge \(K_2\).
3. The six-vertex Walsh multipliers take precisely \(49\) distinct signed integer values. Their positive greatest common divisor and smallest nonzero magnitude are **both** four:
\[
\gcd_{S\subseteq E_6}|W_6(S)|=\min_{W_6(S)\ne0}|W_6(S)|=4.
\]
Consequently
\[
\|T_6\|_{2\to2}=2932,\qquad
\|T_6^{\dagger}\|_{2\to2}=\tfrac14,
\]
and the ratio of the largest to smallest positive singular value is \(733\).
4. Let \(P_6\) be the orthogonal projection onto the range of \(T_6\). Its sharp endpoint norms are
\[
\boxed{\|P_6\|_{\ell^1\to\ell^1}=\|P_6\|_{\ell^\infty\to\ell^\infty}=\frac{605029}{16384}}.
\]

The complete signed spectrum and a representative of each of the ten zero orbits appear in `SPECTRUM.tsv` and `ZERO_ORBITS.csv`. All entries are exact integers.

## Assumptions and scope

The vertex labels are \(0,1,\dots,n-1\), and edge coordinates are ordered lexicographically as \((0,1),(0,2),\dots,(4,5)\) when \(n=6\). The mask of an edge set is the sum of \(2^j\) over its included edges at coordinate \(j\), using zero-based coordinate indices. Each graph is simple and undirected; only *edge acyclicity*, not induced-forest acyclicity, is considered. The multiplier is not divided by \(|G_n|\), and the Fourier inverse has normalization \(2^{-|E_n|}\).

The result is finite and concerns the specific orders \(3,4,5,6\). It makes no assertion of invertibility or orbit classification for all higher orders. The term "first" refers to the transition from the three consecutive invertible orders \(3,4,5\) to order six; order two itself is singular.

## Proof

**Exact forest indicator.** For a mask \(A\in\{0,\dots,2^{\binom n2}-1\}\), process the selected edges in lexicographic order with disjoint-set union. When the endpoints of an added edge already lie in the same component, the new edge closes a cycle, so that mask is rejected. Otherwise merge the components. This criterion is equivalent, in both directions, to acyclicity: a finite undirected graph has a cycle exactly when an edge connects vertices already joined by earlier selected edges. Thus the resulting length-\(2^{\binom n2}\) zero-one array is exactly \(1_{\mathcal F_n}\).

The forest counts \(7,38,291,2932\) for \(n=3,4,5,6\) are also independently characterized by the labelled-component identity
\[
|\mathcal F_n|=\sum_{\pi\text{ a set partition of }[n]}
\prod_{B\in\pi}t(|B|),\qquad
 t(1)=1,\quad t(j)=j^{j-2}\ (j\ge2),
\]
which follows by choosing the connected components and applying Cayley's formula to each component.

**All Walsh coefficients.** Apply \(\binom n2\) stages of exact integer Hadamard butterflies to the indicator array. At every stage, a pair \((a,b)\) is replaced with \((a+b,a-b)\). Induction on the processed bit positions proves that the final array at index \(S\) equals the displayed sum \(W_n(S)\), without approximation. The complete finite loops for \(n=3,4,5,6\) are implemented by `verify_walsh.py` and can be inspected and rerun. The computed order-four signed values are already nonzero on all eleven unlabeled frequency-graph orbits. Orders three and five have odd forest counts, and therefore every multiplier is odd, since \(W_n(S)\equiv|\mathcal F_n|\pmod2\).

At order six, every one of the \(32768\) frequencies is tested. The exact frequency histogram recorded in `SPECTRUM.tsv` has total multiplicity \(32768\), zero multiplicity \(3105\), precisely \(49\) distinct values, and smallest nonzero absolute value four. Divisibility by four also follows directly from this exhaustive histogram, which lists every signed level and its frequency multiplicity. The checksum-like identity
\[
\sum_{S\subseteq E_6}W_6(S)^2=2^{15}|\mathcal F_6|=96075776
\]
is an independent Fourier orthogonality consistency check, not a substitute for the finite enumeration.

**Symmetry-orbit exhaustion.** All \(6!=720\) permutations of the vertex labels permute the fifteen edge coordinates and preserve the forest indicator. Consequently, each Walsh coefficient and the property of vanishing are constant on a frequency-graph isomorphism orbit. Enumerating the image of each least remaining zero mask under all \(720\) permutations and deleting the entire orbit partitions the zero set with no overlap. `ZERO_ORBITS.csv` gives the ten least-mask representatives in this exhaustive procedure, each support size and orbit cardinality. Their orbit sizes sum to \(3105\). The sole size-five representative is mask `662`, with edge set \(\{02,03,05,14,23\}\); its isomorphism type is a triangle with a pendant leaf, disjoint from one edge. All other zero orbits have size seven or more. No inference about untested sizes or orders is made.

**Operator norms.** Every character of \(G_6\) is an eigenvector of counting convolution with eigenvalue \(W_6(S)\). The real symmetric Walsh diagonalization shows that all singular values are \(|W_6(S)|\), so the rank, kernel dimension, operator norm, Moore–Penrose norm and condition number follow exactly. For the range projection,
\[
P_6u=k*u,\qquad
k(x)=2^{-15}\sum_{S:W_6(S)\ne0}(-1)^{|S\cap x|}.
\]
On a finite group, convolution by \(k\) has \(\ell^1\) and \(\ell^\infty\) operator norms exactly \(\sum_x|k(x)|\), with equality attained on point masses and appropriate sign functions. Thus the norm is
\[
2^{-15}\sum_{x\in G_6}\left|\sum_{S:W_6(S)\ne0}(-1)^{|S\cap x|}\right|.
\]
An exact integer Hadamard inverse of the Boolean support array gives numerator \(1210058\). An independent computation groups the \(32768\) arguments into the \(156\) vertex-relabeling orbits of six-vertex simple graphs, evaluates each inner signed sum **directly**, and weights by orbit size, yielding the same numerator. Reduction of the fraction gives \(605029/16384\), as stated.

**Independent exhaustive confirmation.** The second implementation, `verify_direct.cpp`, uses graph traversal with parent-edge exclusion rather than disjoint-set union to recognize acyclicity. For every one of the \(32768\) frequencies it then sums signs **directly over all 2932 forests**, without a Walsh transform; its complete signed-level frequency table agrees with the Python Hadamard result. It also computes the range-projection norm by the independent orbit-weighted character-sum method. Both procedures use exact integer arithmetic and have finite loops whose bounds are fully specified in the source files.

## Verification

Run from the directory containing the four supporting artifacts:

```sh
python3 verify_walsh.py
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct
./verify_direct
```

`verify_walsh.py` must finish with `VERIFY_WALSH_OK`; `verify_direct.cpp` must print `DIRECT_CHECK_OK`. Both print `SIGNED_LEVELS=` followed by the complete signed-value histogram, and these lines must agree exactly apart from the final optional semicolon. The programs check the entire finite frequency space and exact Parseval identity, and calculate orbit sizes and endpoint norms as described above. Their code is part of the delivered artifact; there is no reliance on an undisclosed or precomputed data service.

## Relationship to prior work

The weighted spanning-forest polynomial is classical and is explicitly identified as a multivariate Tutte-polynomial degeneration in Sokal's 2005 survey, Section 2.3 (equations 2.13–2.14), with unrooted-forest formulas in Section 8. The 2007 Caracciolo–Sokal–Sportiello paper supplies a general Grassmann integral representation for weighted spanning forests. Erickson's paper, first submitted in August 2010, studies Rayleigh differences and sum-of-squares formulas for the forest polynomial, particularly for series-parallel graphs; its mention of \(K_7\) concerns a *different* Rayleigh problem. Stănică's 2007 analysis gives the general Cayley-graph/Walsh spectral correspondence, without the evaluated six-vertex forest spectrum.

These sources make the signed-forest sum **definable and computable**, so this work does **not** claim a new general forest generating function, a new Fourier-diagonalization theorem, or first discovery of signed weight specializations. The particular evaluated complete six-vertex zero-orbit classification, first-cancellation graph type, sharp smallest positive multiplier and range-projection endpoint constant are distinct additional finite facts, not stated in the inspected relevant primary sections. Separate existing results for complete-graph *spanning trees*, *matchings*, matroid bases and *triangle-free graphs* concern different indicator functions and do not imply this classification without a new forest calculation.

## Limitations

The finding is an exact finite classification, not a formula for all \(n\), a bound for arbitrary graphic matroids, or a determination of the general graph family. Prior-art checks were bounded; an unindexed table of signed forest-polynomial evaluations or a differently titled treatment of \(K_6\) could affect priority. The arithmetic checkers provide exhaustive deterministic finite certificates; they are not independent expert review. In particular, neither a search with no covering hits nor an exact calculation alone proves worldwide originality.

## References

- A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, first publicly posted 2005-03-25, https://arxiv.org/abs/math/0503607, especially Sections 2.3 and 8.
- S. Caracciolo, A. D. Sokal and A. Sportiello, *Grassmann Integral Representation for Spanning Hyperforests*, first publicly posted 2007-06-11, https://arxiv.org/abs/0706.1509, especially Sections 1–2 and 5.
- A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, first publicly posted 2010-08-21, https://arxiv.org/abs/1008.3660, Sections 1–2.
- P. Stănică, *Graph eigenvalues and Walsh spectrum of Boolean functions*, *Integers* 7(2) (2007), article A32, https://hdl.handle.net/10945/38865. The general Walsh/convolution connection is background, not an attribution of the finite results above.
