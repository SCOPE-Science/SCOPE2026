# Arithmetic rank and exact failure distribution for two-line finite Fourier sampling

## Finding
Let \(q\) be any prime power, let \(\mathbb F_q\) be the field of that order, and let \(L_1,L_2\) be distinct one-dimensional linear subspaces of \(\mathbb F_q^2\). Set \(S=L_1\cup L_2\), so \(|S|=2q-1\), and let \(\psi\) be any nontrivial additive character of \(\mathbb F_q\). The self-restricted Fourier sampling matrix is
\[
H_S=(\psi(x\cdot y))_{x,y\in S},\qquad x\cdot y=x_1y_1+x_2y_2.
\]
Choose nonzero generators \(v\in L_1\), \(w\in L_2\), and write \(a=v\cdot v\), \(b=w\cdot w\), \(c=v\cdot w\). These values obey \(ab-c^2\ne0\). If at least one of \(a,b,c\) vanishes, then \(H_S\) is nonsingular. If all three are nonzero, let
\[
r=ab/c^2\in\mathbb F_q^*\setminus\{1\},\qquad d=\operatorname{ord}_{\mathbb F_q^*}(r).
\]
Then
\[
\boxed{\dim_{\mathbb C}\ker H_S=(q-1)/d,\qquad \operatorname{rank}H_S=2q-1-(q-1)/d.}
\]
The formula holds in odd and even characteristic, independently of \(\psi\) and of generator choices. A basis of the kernel is indexed by the multiplicative characters \(\chi\) satisfying \(\chi(r)=1\): its vector indexed by \(S\) has entries
\[
f_\chi(0)=0,\qquad f_\chi(tv)=\chi(t),\qquad f_\chi(tw)=-\chi(c/a)\chi(t),\quad t\in\mathbb F_q^*.
\]
In particular, every singular example has nullity at least one, and the possible nonzero nullities are divisors of \(q-1\).

Among the \(q(q+1)/2\) unordered pairs of distinct projective lines, the total number giving nonsingular \(H_S\) is exactly
\[
\boxed{F_q=\begin{cases}(q+1)/2,&q\equiv3\pmod4,\\(5q-3)/2,&q\equiv1\pmod4,\\3q/2,&q\text{ even}.\end{cases}}
\]
More precisely, for every divisor \(d>1\) of \(q-1\), the number of pairs with nullity exactly \((q-1)/d\) is
\[
\boxed{M_q(d)=\begin{cases}
(q+1)\#\{r\in\mathbb F_q^*: \operatorname{ord}(r)=d,\ r-1\text{ is a nonzero square}\},&q\equiv3\pmod4,\\
(q-1)\#\{r\in\mathbb F_q^*: \operatorname{ord}(r)=d,\ r-1\text{ is a nonzero square}\},&q\equiv1\pmod4,\\
(q/2)\varphi(d),&q\text{ even}.
\end{cases}}
\]
Here \(\varphi\) is Euler's totient function. Together, \(F_q\) and \(M_q(d)\) give the complete nullity distribution. The criterion specifies exactly which pairs of two lines allow unique reconstruction from the same set of Fourier samples.

## Assumptions and scope
All vectors, dot products, line relations and multiplicative orders are over \(\mathbb F_q\); linear-algebra ranks and kernels are over \(\mathbb C\). The additive character can be obtained by composing a nonzero field trace functional with a primitive prime-th root of unity. There is no restriction on the characteristic or extension degree. Zero is included in each line union exactly once. The order \(d\) is the least positive integer with \(r^d=1\); it is defined only when \(a,b,c\ne0\). For \(q=2\), all three line pairs give invertible matrices, consistent with the formulas.

## Proof
**1. The invariant and character blocks.** Since \(v,w\) form a basis, their Gram determinant is \(ab-c^2=(\det[v\ w])^2\ne0\), also in characteristic two. If both generators are rescaled by nonzero field elements, \(ab/c^2\) is unchanged. Decompose functions on the \(2q-1\) points into the value at zero and the two copies of each multiplicative character on the nonzero scalar parameters of \(L_1,L_2\).

For any nontrivial multiplicative character \(\chi\), define its Gauss sum \(G(\chi)=\sum_{t\ne0}\chi(t)\psi(t)\). Orthogonality shows \(|G(\chi)|^2=q\); in particular it is nonzero. At a nonzero scalar row parameter, the Fourier image of \(\chi\) is a multiple of \(\chi^{-1}\). On the two line copies its coefficient matrix, after dividing by \(G(\chi)\), is
\[
M_\chi=\begin{pmatrix}
J_\chi(a)&J_\chi(c)\\
J_\chi(c)&J_\chi(b)
\end{pmatrix},\quad
J_\chi(z)=\begin{cases}\chi(z)^{-1},&z\ne0,\\0,&z=0.\end{cases}
\]
The zero entry for \(z=0\) follows from \(\sum_{t\ne0}\chi(t)=0\). If any of \(a,b,c\) is zero, then \(M_\chi\) is invertible: when \(c=0\), both diagonal entries are nonzero; when \(a=0\) or \(b=0\), the off-diagonal entries are nonzero. If all are nonzero, its determinant vanishes exactly when \(\chi(ab/c^2)=1\), in which case it has rank one. The matrix can map the \(\chi\)-input space to the \(\chi^{-1}\)-output space without affecting its rank or kernel count.

**2. The constant-character block.** Write \(E(z)=q-1\) for \(z=0\), and \(E(z)=-1\) otherwise. For the origin and the constant values on each of the two nonzero line copies, the Fourier map is represented by
\[
M_0=\begin{pmatrix}1&q-1&q-1\\1&E(a)&E(c)\\1&E(c)&E(b)\end{pmatrix}.
\]
Subtracting its first row from the last two rows gives
\[
\det M_0=q^2\bigl(\mathbf1_{a\ne0}\mathbf1_{b\ne0}-\mathbf1_{c\ne0}\bigr).
\]
Nondegeneracy of the Gram matrix makes this determinant nonzero whenever one of \(a,b,c\) vanishes. If all are nonzero, \(M_0\) has rank exactly two (the last two reduced rows coincide). Thus the trivial character contributes precisely one kernel dimension in the all-nonzero case, and none otherwise.

**3. Exact kernel.** In the all-nonzero case, for any multiplicative character \(\chi\) with \(\chi(r)=1\), the two-dimensional block's null vector has line coefficients \(1\) and \(-\chi(c/a)\). This remains valid for \(\chi=1\), with the origin coefficient equal to zero by the first equation. These nonzero vectors are independent for distinct characters by multiplicative orthogonality. Since \(\mathbb F_q^*\) is cyclic, exactly \((q-1)/d\) of its \(q-1\) characters annihilate the element \(r\) of order \(d\). No other kernel directions occur by the preceding complete block analysis.

**4. Projective-line census.** An isotropic line (with \(v\cdot v=0\)) yields only nonsingular pairs. For a nonisotropic line generated by \(v=(v_1,v_2)\), the vector \(v^\perp=(-v_2,v_1)\) is perpendicular to \(v\), has the same nonzero squared norm \(a\), and gives an independent direction. Every other nonperpendicular line has unique representation \(\mathbb F_q(v+zv^\perp)\) for \(z\ne0\). For this pair, \(c=a\), \(b=a(1+z^2)\) and \(r=1+z^2\). It is singular exactly when \(1+z^2\ne0\). For odd \(q\), there are either zero or two isotropic lines according as \(-1\) is nonsquare or square, respectively. If \(-1\) is nonsquare, each of \(q+1\) nonisotropic first lines has \(q-1\) singular partners; if it is square, each of \(q-1\) nonisotropic first lines has \(q-3\) singular partners. Dividing by two and subtracting from \(q(q+1)/2\) proves the first two formulas for \(F_q\). For even \(q\), precisely one line is isotropic, and each of the other \(q\) lines has \(q-2\) singular partners, giving \(F_q=3q/2\).

For a fixed \(r\in\mathbb F_q^*\setminus\{1\}\), equation \(z^2=r-1\) has two solutions when \(q\) is odd and \(r-1\) is a square, otherwise none; in even characteristic it has exactly one solution. Count these ordered choices for all nonisotropic first lines and divide by two. This gives the multiplicities \(q+1\), \(q-1\), or \(q/2\) per admissible value \(r\), respectively. Grouping the values by their multiplicative order yields \(M_q(d)\). In even characteristic the multiplicative group is cyclic of odd order, so the number of elements of order \(d\) is \(\varphi(d)\), proving the final line of the formula.

## Verification
A standalone Python checker (`check_two_lines.py`) enumerates all unordered projective line pairs, constructs the complete complex Fourier matrix from a field-trace additive character, independently computes numerical singular values, and compares the nullities with the arithmetic order formula. It also checks the nonsingular incidence total. Tested fields are prime orders \(3,5,7,11,13,17\) and extension orders \(4,8,9,16,25\), with explicit irreducible-polynomial models. All \(q(q+1)/2\) pairs per field passed at a fixed numerical threshold; this is corroboration rather than proof of the unrestricted finite-field theorem. The proof above is algebraic and requires no numerical extrapolation.

## Relationship to prior work
Mockenhaupt and Tao initiated the finite-field restriction-theory framework, including the importance of lines and algebraic varieties [1]. Their results provide context but do not formulate the present exact self-restricted two-line rank and incidence distribution. Biswas, Dasgupta, Jacob and Mudumbai [2] analyze spark of two-dimensional DFT submatrices with rows on a single line or rectangular grid and explicitly describe several-line extensions as an open direction; their matrices retain the full column domain and therefore do not imply the same-row-and-column principal matrix theorem stated here. Iosevich and Koh [3] establish restriction estimates for nondegenerate quadratic surfaces, not the exact principal spectrum or nullities of a pair of lines. No claim of general first priority follows from this bounded comparison.

## Limitations
The result concerns the standard bilinear dot product and the same two-line set on both the sampling and reconstruction sides. It does not give singular values or condition numbers beyond the exact rank, nor does it classify three or more lines or the rank of rectangular sampling matrices with different row and column supports. Novelty is assessed against the specifically inspected literature and searchable research summaries, not exhaustive historical priority or independent expert review. Finite numerical checks are not an infinite certificate.

## References
[1] G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (first public submission 2002-04-18), https://arxiv.org/abs/math/0204234.

[2] S. Biswas, S. Dasgupta, M. Jacob and R. Mudumbai, *Spark under 2-D Fourier Sampling*, 23rd European Signal Processing Conference (2015), https://www.eurasip.org/Proceedings/Eusipco/Eusipco2015/papers/1570103923.pdf.

[3] A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505 (2008), https://arxiv.org/abs/0804.4505.
