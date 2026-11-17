# Four-state Euclidean distance spectrum and antipodal rigidity of linked type-C snake polytopes

## Finding

Fix an integer \(n\ge 3\) and a subset \(S\subseteq[n-1]\). Put \(T=S\cup\{n\}\), and let \(P_S\subset\mathbb R^n\) be the feasible polytope of the type-C Gale interval \([S,T]\), realized in standard zero-one coordinates. For \(i\in[n]\) put \(s_i=\mathbf 1_{i\in S}\), so \(s_n=0\), and define its ordered vertex-pair squared-distance enumerator
\[
F_S(z)=\sum_{u,v\in\operatorname{Vert}(P_S)} z^{\|u-v\|_2^2}.
\]
Index matrix rows and columns in the order \(00,01,10,11\). Define
\[
M_0(z)=\begin{pmatrix}1&0&0&0\\z&1&0&0\\z&0&1&0\\1&z&z&1\end{pmatrix},\quad
M_1(z)=\begin{pmatrix}1&z&z&1\\0&1&0&z\\0&0&1&z\\0&0&0&1\end{pmatrix}.
\]
Then for **every** profile \(S\), its **entire** exact squared-distance spectrum, including multiplicities, is
\[
\boxed{F_S(z)=\mathbf1^{\mathsf T} M_{s_1}(z)M_{s_2}(z)\cdots M_{s_n}(z)e_{00}.}
\]
Consequently, the squared Euclidean diameter is \(\deg F_S\), and the coefficient of its top degree counts ordered diameter-realizing pairs (twice the number of unordered pairs).

There is a sharp, explicit classification of the profiles reaching the largest possible squared diameter \(n\). They are **exactly** those \(S\) such that
\[
\boxed{|S\cap\{n-2j,n-2j+1\}|=1\quad(1\le j\le\lfloor(n-1)/2\rfloor).}
\]
There are precisely \(2^{\lfloor n/2\rfloor}\) such profiles among the \(2^{n-1}\) linked type-C snake profiles, a proportion \(2^{1-\lceil n/2\rceil}\). For each of them there are precisely
\[
\boxed{2^{\lceil n/2\rceil-1}}
\]
unordered diametral pairs. Every such pair is \((\mathbf1_A,\mathbf1_{[n]\setminus A})\), where \(A\) contains exactly one element from every adjacent pair \(\{n-2j+1,n-2j+2\}\) counted from the right; if \(n\) is odd its first coordinate is arbitrary. No nonvertex point belongs to a diametral pair.

## Assumptions and scope

The type-C Gale order on subsets of \([n]\) is characterized by suffix cardinalities: \(A\preceq B\) if and only if \(|A\cap[i,n]|\le |B\cap[i,n]|\) for every \(i\in[n]\). The vertices of \(P_S\) are the distinct zero-one vectors \(\mathbf1_A\) with \(S\preceq A\preceq S\cup\{n\}\). Equivalently, writing \(a_i=|S\cap[i,n]|\), a binary vector \(x\) is a vertex if and only if
\[
a_i\le\sum_{j=i}^n x_j\le a_i+1\quad(1\le i\le n).
\]
Every such binary point is extreme because no distinct binary point can be a nontrivial convex combination of other binary points. The Euclidean metric is the unscaled ambient standard coordinate metric. Both the orientation and the normalization matter: the distance formula concerns the *feasible polytope in its native zero-one coordinates*, not an affinely equivalent order polytope equipped with its own standard metric. The linked toric-interval correspondence \(T=S\cup\{n\}\) is established in Chen–Sanchez–Veliz–Ying (Proposition 5.3).

## Proof

**1. Binary suffix-state encoding.** For a feasible binary vector \(x\), define \(y_{n+1}=0\) and \(y_i=\sum_{j=i}^n x_j-a_i\in\{0,1\}\). As \(a_i-a_{i+1}=s_i\), we have \(x_i=s_i+y_i-y_{i+1}\). When \(s_i=0\), the binary condition \(x_i\in\{0,1\}\) is equivalent to \(y_i\ge y_{i+1}\). When \(s_i=1\), it is equivalent to \(y_i\le y_{i+1}\). This also holds at \(i=n\), since \(s_n=0\). Conversely, any binary sequence \((y_1,\ldots,y_n)\) with these local relations and terminal state \(y_{n+1}=0\) determines a feasible binary \(x\), by telescoping the defining identity. Hence the correspondence is bijective.

**2. Exact transfer formula.** For two feasible vertices \(x,x'\), take pair states \(b_i=(y_i,y'_i)\in\{00,01,10,11\}\). Each transition \(b_i\to b_{i+1}\) is componentwise weakly decreasing when \(s_i=0\) and componentwise weakly increasing when \(s_i=1\). Its squared-distance contribution is
\[
(x_i-x'_i)^2=|(y_i-y'_i)-(y_{i+1}-y'_{i+1})|\in\{0,1\}.
\]
Enumerating the 16 possible transitions gives exactly the displayed matrices: the entry in row \(b_i\), column \(b_{i+1}\) is either zero or \(z\) raised to this contribution. Multiplication sums the weights over all internal pair states, terminal \(b_{n+1}=00\), and arbitrary initial \(b_1\); hence it equals \(F_S(z)\). All entries have nonnegative integer coefficients. For any two vertices, the squared distance equals their Hamming distance. Strict convexity of squared Euclidean distance separately in each endpoint shows that any maximizing pair of points of \(P_S\) must consist of vertices. Thus the polynomial degree is exactly the squared diameter, and its top coefficient counts the ordered diametral pairs. The transfer formula can be evaluated with polynomial coefficient vectors of length at most \(n+1\), in \(O(n^2)\) integer arithmetic operations and \(O(n)\) stored coefficients.

**3. Characterization of full-diameter pairs.** As \(P_S\subset[0,1]^n\), the squared diameter is at most \(n\); equality requires one vertex \(x\) and its coordinate complement \(\mathbf1-x\). For any suffix of length \(L\), write \(a\) for the number of elements of \(S\) in that suffix and \(k\) for the number of ones of \(x\). Both endpoints are feasible exactly when \(k\) and \(L-k\) belong to \(\{a,a+1\}\). If \(L=2h+1\) is odd, this is possible only for \(a=h\); then \(k\in\{h,h+1\}\). If \(L=2h\) is even, it is possible only for \(a\in\{h-1,h\}\), and necessarily \(k=h\).

The last coordinate is absent from \(S\), so its length-one suffix has \(a=0\). For each subsequent odd suffix of length \(3,5,\ldots\), the condition \(a=(L-1)/2\) is equivalent to exactly one member of the newly added two-position block \(\{n-2j,n-2j+1\}\) lying in \(S\). Every intervening even suffix automatically meets the required \(a\)-condition regardless of its one newly added \(S\)-bit. Therefore these block conditions are necessary and sufficient for complementary feasible vertices.

Under them, feasibility of both \(x\) and \(\mathbf1-x\) is equivalent to having exactly one selected coordinate in each two-position block \(\{n-2j+1,n-2j+2\}\), beginning with \(\{n-1,n\}\), and an arbitrary remaining first coordinate if \(n\) is odd. There are \(2^{\lceil n/2\rceil}\) such ordered first endpoints. Coordinate complementation has no fixed binary point, so division by two yields the asserted unordered-pair count. Each complete \(S\)-block contributes two choices; if \(n\) is even the leftover position \(1\) contributes another two. This gives \(2^{\lfloor n/2\rfloor}\) extremal profiles and the stated proportion. Necessity of vertex endpoints was established in step 2.

## Verification

The standalone `snake_metric_checker.py` implements the transfer product over exact integer polynomial coefficients independently of an exhaustive zero-one suffix enumeration. It compares the *full polynomial*, not just its degree, for every \(S\subseteq[n-1]\) and every \(2\le n\le11\), also independently checking the full-diameter classification and both counting formulas. Its successful output is

```
TYPE_C_SNAKE_METRIC_PASS n=2..11 profiles=2046 ordered_pairs=19684660 full_diameter_profiles=124
```

For example, \(n=5\) and \(S=\{2,4\}\) give
\[
F_S(z)=13+24z+52z^2+48z^3+24z^4+8z^5,
\]
so there are four unordered full-diameter pairs. These finite checks are corroboration only; the proof above establishes the statements for every \(n\ge3\).

## Relationship to prior work

Chen, Sanchez, Veliz and Ying (arXiv:2311.15441, first posted 2023-11-26) introduce lattice-path delta matroids, prove the suffix-inequality polytope description (Section 4), classify linked toric snake intervals by \([S,S\cup\{n\}]\) (Proposition 5.3), and give their triangulations and volumes (Section 5). The present result uses that established model but determines a different, ambient Euclidean **all-vertex-pairs distance enumerator** and its extremal profiles. Eur, Fink, Larson and Spink (arXiv:2209.06752, Section 2) study delta-matroid polytopes and Schubert lower intervals; their volume and lattice-point results do not supply the metric enumerator here. The generalized snake-poset work of von Bell et al. (arXiv:2102.11306) studies order-polytope volumes and triangulations; an order-polytope affine transformation does not preserve the native Euclidean metric. A targeted published-record and literature search did not identify prior statements implying the four-state metric formula or the block-rigidity and counts. This is a bounded priority comparison, not a proof of global novelty.

## Limitations

The explicit extremal-profile formula concerns linked type-C *toric snake* intervals only, not arbitrary lattice-path delta-matroid intervals. The four-state product enumerates squared distances between vertices, not distances between arbitrary interior points. No claim is made about independent validation or about exhaustive coverage of unindexed literature. The code verifies only dimensions up to eleven; its finite reach is not used to infer the unbounded theorem.

## References

1. D. M. Chen, M. Sanchez, J. Veliz and Z. Ying, *Lattice Path Delta Matroids*, arXiv:2311.15441 (initial public version 2023-11-26). https://arxiv.org/abs/2311.15441
2. C. Eur, A. Fink, M. Larson and H. Spink, *Signed permutohedra, delta-matroids, and beyond*, arXiv:2209.06752 (initial version 2022-09-14). https://arxiv.org/abs/2209.06752
3. M. von Bell, B. Braun, D. Hanely, K. Serhiyenko, J. Vega, A. R. Vindas-Meléndez and M. Yip, *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306 (initial version 2021-02-22). https://arxiv.org/abs/2102.11306
