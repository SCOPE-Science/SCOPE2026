# Universal nonvanishing and sharp divisibility of matrix-complex Fourier coefficients

## Finding
For every finite field \(\mathbb F_q\), with \(q\ge2\), and every integer \(n\ge2\), the zero-composition variety
\[
E_{n,q}=\{(X,Y)\in M_n(\mathbb F_q)^2:XY=0\}
\]
has **no additive Fourier zeros**. More precisely, if \(c=\binom n2\), each of its \(q^{2n^2}\) unnormalized Fourier coefficients is an integer satisfying
\[
F_{n,q}(A,B)\equiv(-1)^n q^c\pmod{q^{c+1}}.
\]
Thus every coefficient is divisible by exactly \(q^c\) but not by \(q^{c+1}\). The additive convolution operator by \(\mathbf1_{E_{n,q}}\) is invertible. Its exact least singular value is \(q^c\), attained when both frequency matrices are invertible, while the maximal singular value is \(\lvert E_{n,q}\rvert\).

## Assumptions and scope
Here \(q=p^f\) is an arbitrary prime power, \(n\ge2\), and \(\psi:\mathbb F_q\to\mathbb C^\times\) is *any* nontrivial additive character. For matrices of size \(n\), let \(\langle A,X\rangle=\sum_{i,j}A_{ij}X_{ij}\). Define the unnormalized coefficient
\[
F_{n,q}(A,B)=\sum_{XY=0}\psi(\langle A,X\rangle+\langle B,Y\rangle), \qquad A,B\in M_n(\mathbb F_q).
\]
Convolution is on the additive group \(G=M_n(\mathbb F_q)^2\) of cardinality \(q^{2n^2}\). All singular values below refer to unnormalized convolution, which is diagonal in the orthonormal Fourier basis with diagonal entries \(F_{n,q}(A,B)\). The modular congruence is in the ordinary integers. If \(q=p^f\), the exact ordinary \(p\)-adic valuation of every coefficient is \(f\binom n2\).

## Proof
**1. Sum over the second matrix.** Fix \(X\), let \(r=\operatorname{rank}X\), and write \(W=\operatorname{row}(X)\subseteq\mathbb F_q^n\). The condition \(XY=0\) says each column of \(Y\) belongs to \(\ker X=W^\perp\). Columnwise additive-character orthogonality gives
\[
\sum_{Y:XY=0}\psi(\langle B,Y\rangle)
=\begin{cases}q^{n(n-r)},&\operatorname{im}B\subseteq W,\\0,&\text{otherwise.}\end{cases}
\]
Write \(H=\operatorname{im}B\) and define \(S_W(A)=\sum_{\operatorname{row}(X)=W}\psi(\langle A,X\rangle)\). Then
\[
F_{n,q}(A,B)=\sum_{r=\dim H}^{n}q^{n(n-r)}\sum_{\substack{W\supseteq H\\\dim W=r}} S_W(A).\tag{1}
\]
**2. Exact integer-valued row-space transform.** For every subspace \(U\subseteq\mathbb F_q^n\), orthogonality over all \(n\)-row matrices with row space *contained in* \(U\) yields
\[
\sum_{\operatorname{row}(X)\subseteq U}\psi(\langle A,X\rangle)
=q^{n\dim U}\mathbf1_{U\subseteq\ker A}.
\]
Apply Möbius inversion on the lattice of subspaces of \(W\) using
\(\mu(U,W)=(-1)^{r-u}q^{\binom{r-u}{2}}\) for \(u=\dim U\) and \(r=\dim W\). One obtains the **exact** formula
\[
S_W(A)=\sum_{U\subseteq W\cap\ker A}(-1)^{r-u}q^{\binom{r-u}{2}+nu}.\tag{2}
\]
In particular, all \(S_W(A)\), and therefore all Fourier coefficients in (1), are ordinary integers. The contribution \(U=0\) to (2) is \((-1)^r q^{\binom r2}\). For each \(u\ge1\), the extra exponent is
\[
\binom{r-u}{2}+nu-\binom r2=u(n-r)+\frac{u(u+1)}2\ge1.
\]
It follows, with exact divisibility for each summand, that
\[
S_W(A)\equiv(-1)^r q^{\binom r2}\pmod{q^{\binom r2+1}}.\tag{3}
\]
**3. Uniform divisibility and nonvanishing.** In (1), the term at \(r=n\) has the single subspace \(W=\mathbb F_q^n\) and is congruent to \((-1)^n q^{\binom n2}\) modulo \(q^{\binom n2+1}\), by (3). Every term with \(r<n\) is divisible by \(q^{n(n-r)+\binom r2}\), and
\[
n(n-r)+\binom r2-\binom n2=\binom{n-r+1}{2}\ge1.
\]
This proves the claimed uniform integer congruence. Since its residue class is nonzero modulo \(q^{\binom n2+1}\), no Fourier coefficient can vanish.

**4. Sharp singular values and cardinality.** If \(B\) is invertible, then \(H=\mathbb F_q^n\) and (1) consists only of \(S_{\mathbb F_q^n}(A)\). If \(A\) is also invertible, (2) has only \(U=0\), giving \(F_{n,q}(A,B)=(-1)^n q^{\binom n2}\). The congruence implies every absolute value is at least \(q^{\binom n2}\), so this is the exact minimum. By the triangle inequality, every Fourier magnitude is at most \(F_{n,q}(0,0)=\lvert E_{n,q}\rvert\), attained at the trivial frequency. For each fixed rank-\(r\) matrix \(X\), the number of \(Y\) satisfying \(XY=0\) is \(q^{n(n-r)}\). The number of such \(X\) is
\[
N_{n,r}(q)=\frac{\prod_{i=0}^{r-1}(q^n-q^i)^2}{\prod_{i=0}^{r-1}(q^r-q^i)},
\]
with empty products equal to one. Hence
\[
\lvert E_{n,q}\rvert=\sum_{r=0}^nN_{n,r}(q)q^{n(n-r)},\qquad
\kappa(T_{E_{n,q}})=\frac{\lvert E_{n,q}\rvert}{q^{\binom n2}}.
\]
All Fourier eigenvalues are real because \((X,Y)\mapsto(-X,-Y)\) preserves \(XY=0\), and (2) more strongly proves they are integers.

## Verification
The standalone `check_zero_product_fourier.py` uses exact finite-field arithmetic and integer-valued Fourier transforms. Its independently implemented tests exhaust every frequency for \((n,q)=(2,2),(2,3),(2,4),(3,2)\), corresponding respectively to \(256\), \(6561\), \(65536\), and \(262144\) coefficients. For characteristic two, Walsh transforms are exact integers; for characteristic three, an exact Eisenstein-integer Fourier transform is used and its nonrational coordinate is checked to vanish. It verifies the cardinality formula, modular congruence, Fourier nonvanishing and the extrema, with completion marker `ALL_ZERO_PRODUCT_FOURIER_CHECKS_OK`. Run `python3 check_zero_product_fourier.py` from the directory containing that file. The finite computations are evidence of implementation consistency, **not** a substitute for the all-parameter proof above.

## Relationship to prior work
Subspace-lattice Möbius inversion and finite-field Fourier orthogonality are standard established tools. Li and Hu (2011), Theorem 2.1, determine character sums over the invertible matrix group; that explains a possible treatment of the full-row-rank contribution but does not itself classify all zero-composition pairs or their Fourier support. Letellier (2011) studies Fourier transforms in finite-field general-linear and quiver contexts; its character-theoretic and quiver results have different objects from the present additive transform of \(XY=0\). Achar, Kulkarni, and Matherne (2018) classify Fourier–Sato transforms of simple perverse sheaves on representation spaces of type-A quivers; those sheaf-theoretic transforms are not an all-frequency character sum of the zero-composition locus. The congruence here depends on comparing all ranks through a subspace-lattice divisibility gap.

## Limitations
This statement concerns **square** matrices over finite fields, with unnormalized complex additive convolution. It does not establish an analogous statement for rectangular complexes, nonfield rings, or nonzero product fibres. The stated literature comparison is bounded, not a proof of historical priority. An unlocated general theorem for quiver-relation varieties or a specialized rank-character identity might imply this result; independent mathematical review remains outstanding.

## References
- E. Letellier, *Quiver varieties and the character ring of general linear groups over finite fields*, arXiv:1103.2759v1 (first public version 2011-03-14), https://arxiv.org/abs/1103.2759.
- Y. Li and S. Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1 (first public version 2011-05-23), https://arxiv.org/abs/1105.4513.
- P. N. Achar, M. C. Kulkarni, and J. P. Matherne, *Combinatorics of Fourier transforms for type A quiver representations*, arXiv:1807.10217v1 (first public version 2018-07-26), https://arxiv.org/abs/1807.10217.
