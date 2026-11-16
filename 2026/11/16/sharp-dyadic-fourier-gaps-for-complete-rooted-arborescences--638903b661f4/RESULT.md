# Sharp dyadic Fourier gaps for complete rooted arborescences

## Finding
Let \(n\ge 2\), choose the distinguished root \(r=n\), and let
\[
E_n=\{(i,j):1\le i\le n-1,\ 1\le j\le n,\ j\ne i\}.
\]
The set \(\mathcal A_n\subseteq\mathbb F_2^{E_n}\) consists of the edge-incidence vectors of all directed spanning trees oriented *toward* \(r\): each nonroot vertex has exactly one outgoing parent arc and every directed path eventually reaches \(r\). Define the unnormalized Walsh coefficients
\[
W_n(a)=\sum_{T\in\mathcal A_n}(-1)^{\sum_{e\in T}a_e}
\quad(a\in\mathbb F_2^{E_n}).
\]
Then the sharp smallest nonzero multiplier magnitude is
\[
\boxed{\min_{a:W_n(a)\ne0}|W_n(a)|=
\begin{cases}1,&n\text{ odd},\\2^{n-2},&n\text{ even}.\end{cases}}
\]
For odd \(n\), every multiplier is odd and nonzero. For even \(n\), every multiplier is divisible by \(2^{n-2}\); for each even \(n\ge4\), some multiplier vanishes, while \(n=2\) is invertible. Consequently, counting convolution by \(1_{\mathcal A_n}\) on \(\ell^2(\mathbb F_2^{E_n})\) is invertible exactly for odd \(n\) or \(n=2\), and its Moore--Penrose pseudoinverse has the sharp norm
\[
\boxed{\|T_n^\dagger\|_{2\to2}=
\begin{cases}1,&n\text{ odd},\\2^{-(n-2)},&n\text{ even}.\end{cases}}
\]
Here the norm is for unnormalized counting convolution, not probability-normalized averaging.

## Assumptions and scope
All arcs in \(E_n\) are distinct ordered pairs. Arcs whose tail is \(r\) are omitted because they never belong to a tree oriented toward \(r\). Put \(m=n-1\), and associate to a character \(a\) the signs \(s_{ij}=(-1)^{a_{ij}}\) for \(i\ne r\), \(j\ne i\). The \(m\times m\) integer matrix \(L(s)\), with indices the nonroot vertices, is
\[
L(s)_{ii}=\sum_{j\ne i}s_{ij},\qquad L(s)_{ij}=-s_{ij}\quad(i\ne j,\ i,j\ne r).
\]
A tree contributes the product of its chosen signs. There are exactly \(n^{n-2}\) such trees by the rooted form of Cayley's formula. The transform is on the full Boolean group of \((n-1)^2\) directed-arc coordinates; no frequency restriction is imposed in the theorem.

## Proof
**1. Exact signed matrix-tree identity.** Expand \(\det L(s)\) by multilinearity in the rows, using that the \(i\)-th row equals \(\sum_{j\ne i}s_{ij}(e_i-e_j)^\top\), with \(e_r=0\) after deleting the root column. Choosing one parent \(j\) for each nonroot \(i\) yields a directed functional graph. A directed cycle makes its chosen row vectors dependent, hence contributes determinant zero. With no directed cycle, all paths reach the root and the chosen row vectors can be made triangular with diagonal ones by ordering vertices from their descendants toward the root. Such an arborescence contributes determinant one. Therefore
\[
\boxed{W_n(a)=\det L(s)}.
\]
This polynomial argument allows arbitrary real, including negative, arc weights.

**2. Universal arithmetic bounds.** If \(n\) is odd, \(n^{n-2}\) is odd, so each signed sum \(W_n(a)\equiv n^{n-2}\equiv1\pmod2\). If \(n\) is even, \(m=n-1\) is odd. Each diagonal entry of \(L(s)\) is a sum of \(n-1\) odd-many signs, and every offdiagonal entry is a sign. Thus every matrix entry is odd. Subtracting the first row from each of the remaining \(m-1\) rows shows that \(2^{m-1}=2^{n-2}\) divides every determinant. This establishes the lower bounds for nonzero magnitudes.

**3. Sharpness for odd \(n\).** We construct an even-order skew-symmetric matrix \(A\) with zero diagonal, all offdiagonal entries in \(\{\pm1\}\), all row sums in \(\{\pm1\}\), and \(\det A=1\). Start with
\[
A_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
If \(A\) has even order \(m\), select \(u\in\{\pm1\}^m\) with \(\sum_i u_i=0\), and form
\[
A'=\begin{pmatrix}A&u&-u\\-u^\top&0&1\\u^\top&-1&0\end{pmatrix}.
\]
Old row sums are unchanged and the new row sums are \(1,-1\). Because \(A\) is invertible and skew-symmetric, \(u^\top A^{-1}u=0\). The two columns \(u,-u\) therefore contribute a zero Schur-complement correction to the new lower-right skew block, which has determinant one. Hence \(\det A'=\det A=1\). Induction covers every even order \(m\). For this matrix, take the nonroot signs \(s_{ij}=A_{ij}\) and root signs \(s_{ir}=-\sum_{j\ne i,r}A_{ij}\in\{\pm1\}\). Then \(L(s)=-A\), so \(W_n(a)=\det(-A)=1\), proving the lower bound is attained for every odd \(n\).

**4. Sharpness for even \(n\).** Write \(m=n-1=2h+1\) and index the nonroot vertices by \(\mathbb Z/m\mathbb Z\). Set all root signs equal to \(+1\); among the nonroot vertices, put
\[
s_{ij}=\begin{cases}+1,&j-i\pmod m\in\{1,\ldots,h\},\\-1,&j-i\pmod m\in\{h+1,\ldots,2h\}.
\end{cases}
\]
The resulting skew-sign matrix \(A\) has row sums zero, so \(L=I-A\), whose first circulant row is \((1,-1,\ldots,-1,+1,\ldots,+1)\), with \(h\) occurrences of each nonzero sign. Its circulant polynomial is \(p(z)=1-\sum_{j=1}^h z^j+\sum_{j=h+1}^{2h}z^j\). At \(z=1\), \(p(1)=1\). At any nontrivial \(m\)-th root of unity \(\zeta\), \(p(\zeta)=-2\sum_{j=1}^h\zeta^j=-2\zeta(1-\zeta^h)/(1-\zeta)\). Because \(\gcd(h,m)=1\), multiplication by \(h\) permutes the nontrivial roots; their products of the numerator and denominator factors coincide. Their product and \(\prod_{\zeta\ne1}\zeta\) are both one. The eigenvalue product gives
\[
\boxed{\det(I-A)=2^{m-1}=2^{n-2}}.
\]
When \(n=2\), the one-dimensional case also has determinant one. Thus the even lower bound is sharp.

**5. A zero for every even \(n\ge4\).** Let \(k=(n-2)/2\), give exactly \(k\) arcs leading directly to the root sign \(-1\), and give every other arc sign \(+1\). The reduced Laplacian becomes \(D-J\), where \(J\) is all-one and \(D\) has \(k\) diagonal values \(n-2\) and \(n-1-k\) values \(n\). The determinant lemma gives
\[
\det(D-J)=n^{n-1-k}(n-2)^k\left(1-\frac{n-1-k}{n}-\frac{k}{n-2}\right)=0.
\]
No such negative-star construction is needed or possible for \(n=2\), when the single tree gives two nonzero Walsh multipliers \(\pm1\). Finally, real Boolean-group Walsh characters diagonalize unnormalized convolution; their eigenvalue magnitudes are singular values. Taking the reciprocal of the smallest positive multiplier proves the stated pseudoinverse norm and invertibility criterion.

## Verification
The file `verify_finite.py` reconstructs trees independently from Prüfer words, orients them toward the root and compares direct signed sums with an exact Bareiss determinant at *every* reduced frequency for \(n=3,4,5\). It checks 83 independently selected frequencies for \(n=6\), validates the two explicit extremizing constructions for \(2\le n\le18\), and checks the zero-star construction at every even \(n\in\{4,6,\ldots,18\}\). The program `verify_reduced_n6.cpp` exhausts the \(2^{20}\) row-gauge-reduced frequencies of \(n=6\), finding 514,800 zeros and smallest positive magnitude 16. These tests corroborate, but do not replace, the all-dimensional proof above. Run with `python3 verify_finite.py` and `g++ -O3 -std=c++17 verify_reduced_n6.cpp -o verify_n6 && ./verify_n6 6`.

## Relationship to prior work
The weighted directed matrix-tree theorem is classical, and the determinant formula is background, not a newly claimed identity. Biane and Chapuy (2015) discuss Laplacians and directed spanning-tree generating functions in a different lifted-tree setting; De Leenheer (2019) gives an elementary weighted directed matrix-tree proof. Zeng and You (2024) study skew-adjacency determinants of tournaments, including already-known unit determinants for even-order transitive tournaments. The present claim combines a *universal exact dyadic minimum for all directed-arborescence Fourier characters*, explicit attaining signings at every order, and a complete parity criterion for convolution invertibility; none is stated in the inspected sources. Existing exact spanning-tree Walsh results on undirected edges have a different frequency incidence rule and do not automatically cover ordered parent arcs.

## Limitations
This theorem concerns complete bidirected graphs and one fixed root, with counting convolution on Boolean directed-arc coordinates. It gives the sharp first positive Fourier level and singularity criterion, **not** the full multiplier histogram or kernel dimension in arbitrary order. Priority assessment is bounded by accessible literature and semantic search: unindexed equivalent formulations could exist. The verification programs are finite checks and do not constitute independent external proof validation.

## References
- P. Biane and G. Chapuy, *Laplacian matrices and spanning trees of tree graphs*, arXiv:1505.04806, first submitted 2015-05-18, https://arxiv.org/abs/1505.04806.
- P. De Leenheer, *An elementary proof of a matrix tree theorem for directed graphs*, arXiv:1904.12221, 2019, https://arxiv.org/abs/1904.12221.
- J. Zeng and L. You, *On determinants of tournaments and \(\mathcal D_k\)*, arXiv:2408.06992, 2024, https://arxiv.org/abs/2408.06992.
