# Bicycle dimension gives the exact Walsh divisibility of regular-matroid bases

## Finding

Let \(A\in\mathbb Z^{r\times m}\) be totally unimodular and of full row rank, with \(r\ge1\). Its column matroid has basis family \(\mathcal B\subseteq\binom{[m]}r\). On the additive Boolean group \(\mathbb F_2^m\), form the indicator of basis-incidence vectors and its *unnormalized* Fourier coefficients
\[
W_A(t)=\sum_{S\in\mathcal B}(-1)^{\sum_{e\in S}t_e},\qquad t\in\mathbb F_2^m.
\]
Define the binary bicycle dimension
\[
 b(A)=\dim_{\mathbb F_2}\bigl(\operatorname{row}(\overline A)\cap\ker(\overline A)\bigr)
 =r-\operatorname{rank}_{\mathbb F_2}(\overline A\,\overline A^{\mathsf T}),
\]
where the bar denotes reduction modulo two. Then, **for every such matrix**, the exact positive greatest common divisor of all Fourier coefficients is
\[
\boxed{\gcd_{t\in\mathbb F_2^m} W_A(t)=2^{b(A)}.}
\]
Equivalently, every coefficient is divisible by \(2^{b(A)}\), and **at least one coefficient has exact two-adic valuation \(b(A)\)**. This does **not** assert that the least nonzero absolute coefficient is \(2^{b(A)}\).

In particular, \(b(A)=0\) implies that every multiplier is odd and basis-indicator convolution is invertible on \(\ell^2(\mathbb F_2^m)\). In general its Moore--Penrose pseudoinverse obeys \(\|T_A^\dagger\|_{2\to2}\le2^{-b(A)}\), with no claim that equality holds.

For the simple \(d\)-dimensional hypercube graph \(Q_d\), \(d\ge1\), applied to its reduced vertex-edge incidence matrix, this yields the explicit all-dimensional law
\[
\boxed{\gcd_{t\in\mathbb F_2^{d2^{d-1}}}\sum_{T\text{ spanning tree of }Q_d}(-1)^{|T\cap t|}=2^{2^{d-1}-1}.}
\]
Here \(t\) denotes the set of negatively signed edges and all sums are over labelled edge sets. The dimension exponent is sharp for **every** \(d\), not merely for tested examples.

## Assumptions and scope

A totally unimodular matrix has all square subdeterminants in \(\{0,1,-1\}\). Full row rank ensures that its reduction modulo two still has row rank \(r\), because at least one maximal minor is \(\pm1\). The matroid includes loops or coloops if the input does; neither must be excluded. The greatest common divisor is taken over integer Fourier multipliers, including zeros, with the conventional positive sign. The all-positive signing gives \(W_A(0)=|\mathcal B|>0\), so the gcd is nonzero. The binary bicycle dimension is a matroid invariant; the proof also works directly for a specified totally unimodular representation, without needing representation independence.

The result is a Fourier-arithmetic theorem, not an assertion about the number of vanishing multipliers or exact Banach-space projection norms.

## Proof

**1. Fourier determinants.** Let \(a_e\) be column \(e\) of \(A\), and put \(s_e=(-1)^{t_e}\). Cauchy--Binet and total unimodularity give
\[
W_A(t)=\det\!\left(A\operatorname{diag}(s_1,\ldots,s_m)A^{\mathsf T}\right)
=\det\!\left(\sum_{e=1}^m s_e a_ea_e^{\mathsf T}\right).
\]
Every nonzero maximal squared minor equals one, hence there are no unwanted multiplicities.

**2. Uniform divisibility.** Put \(M=AA^{\mathsf T}\), reduce modulo two and let \(k=b(A)\). Choose an integer unimodular row-change \(P\) lifting a binary basis that separates the radical and a nondegenerate complement of the symmetric bilinear form \(\overline M\). (Elementary binary row operations lift to integer unimodular operations.) Thus, in blocks of sizes \(r-k,k\),
\[
PMP^{\mathsf T}=\begin{pmatrix} H&2C\\2C^{\mathsf T}&2D\end{pmatrix},
\qquad \det H\equiv1\pmod2.
\]
For any edge signing, \(M_t=M-2\sum_{e:t_e=1}a_ea_e^{\mathsf T}\) has the same block divisibility structure, and its upper-left block stays invertible over the two-adic integers. The Schur complement has all entries even, so \(2^k\) divides \(\det(M_t)=W_A(t)\) for every \(t\). This also covers \(k=0\).

**3. Sharpness of the exponent.** The bottom \(k\) rows of \(PA\), reduced modulo two, have rank \(k\), because \(A\) has full binary row rank. Choose \(k\) columns whose bottom reductions \(z_1,\ldots,z_k\) form a basis of \(\mathbb F_2^k\). Change signs **only** on these \(k\) edges, with Boolean choices \(x_1,\ldots,x_k\). In the preceding Schur calculation, reduction of the determinant divided by \(2^k\) is
\[
\frac{W_A(x)}{2^k}\equiv
\det\!\left(D+\sum_{i=1}^k x_i z_i z_i^{\mathsf T}\right)\pmod2,
\]
where \(D\) is the integer bottom block of \(PMP^{\mathsf T}\) divided by two, reduced modulo two. Over \(\mathbb F_2\), the right side is a multilinear polynomial in the Boolean variables. Its coefficient of \(x_1\cdots x_k\) is \(\det[z_1\ \cdots\ z_k]^2=1\), by determinant multilinearity (or Cauchy--Binet for the highest-degree term). A nonzero multilinear polynomial cannot vanish at every point of \(\mathbb F_2^k\): its Boolean truth table determines all coefficients by Möbius inversion. Hence some signing has odd \(W_A(x)/2^k\). The gcd equals \(2^k\). For \(k=0\), the all-positive signing already has an odd determinant.

**4. Hypercubes.** Orient the edges of \(Q_d\) arbitrarily and remove one incidence row. The full binary Laplacian is
\[
\overline L=\sum_{j=1}^d(I+T_j),
\]
where \(T_j\) translates a cube vertex by its \(j\)-th coordinate unit. The group algebra of \(\mathbb F_2^d\) over \(\mathbb F_2\) is the truncated polynomial algebra \(\mathbb F_2[y_1,\ldots,y_d]/(y_1^2,\ldots,y_d^2)\), under which \(\overline L\) is multiplication by \(y_1+\cdots+y_d\). An invertible linear change of the nilpotent generators turns this into multiplication by \(y_1\), which has kernel dimension \(2^{d-1}\). Constant vertex vectors lie in this kernel and have nonzero root coordinate; restricting to root-coordinate zero reduces kernel dimension by exactly one. Because full-Laplacian rows sum to zero, a vector supported off the root is killed by the reduced Laplacian exactly when its root-extended vector is killed by the full Laplacian. Thus the reduced nullity is \(2^{d-1}-1\), completing the explicit formula.

## Verification

The standalone exact-integer checker `check_bicycle.py` enumerates all **771 connected simple labelled graphs on two through five vertices** and compares the direct Walsh-spectrum gcd with the bicycle nullity. It also checks the complete Fourier transforms for \(Q_1,Q_2,Q_3\), including \(384\) spanning trees and \(1{,}522\) Fourier zeros for \(Q_3\), and finds an exact sharpness witness for \(Q_4\) with a signed determinant of \(-128\) (edge-order bitmask `0xd48d385c`). A cographic representation dual to the cycle matroid of \(K_4\) is checked independently, including all its Boolean signings. The outputs verify examples but the all-dimensional theorem rests on the preceding algebraic proof, not on extrapolation.

To reproduce: `python3 check_bicycle.py` with a standard Python 3 interpreter; the script has no nonstandard dependencies, uses exact integer determinants and direct Walsh--Hadamard transforms, and aborts if an asserted identity fails.

## Relationship to prior work

The determinant representation of weighted spanning-tree sums and the totally-unimodular basis-count formula are classical. Pendavingh [P12, Section 4.1] explicitly gives the unweighted regular-matroid determinant \(\det(AA^{\mathsf T})\), and studies bicycle dimensions for binary matroids; he does not there give the present sharp gcd across **all independent edge signings**. Lamey--Silver--Williams [L14, Section 2] identify binary graph bicycle spaces with based Laplacian kernels, without the sharp signed-basis Fourier gcd. Klee--Stamps [K19, Sections 1--2] discuss the weighted Matrix--Tree Theorem, focusing on selected weight structures and known enumeration formulas, not the universal two-adic exactness over all signings. An earlier result of Berman [B86] relates the bicycle group to invariant factors of the unweighted tree count; divisibility of the *unsigned* tree count does not imply sharpness across arbitrary signs. The relationship to these prior results is an extension in the Fourier-signed direction, not a claim of rediscovering their underlying identities.

## Limitations

No claim is made that Fourier multipliers are zero-free when \(b(A)>0\), that their smallest positive absolute value is \(2^{b(A)}\), or that a complete spectrum or sharp \(\ell^1\)/\(\ell^\infty\) projection norm is determined. The finite checker is deliberately bounded; sharpness in arbitrary rank follows from the multilinear coefficient argument. Historical literature comparison is substantial but not an exhaustive proof of priority. Independent external mathematical validation has not been performed.

## References

- [P12] R. A. Pendavingh, *On the evaluation at \((-\mathrm i,\mathrm i)\) of the Tutte polynomial of a binary matroid*, arXiv:1203.0910, first public version 2012-03-05, Sections 2.2 and 4.1. https://arxiv.org/abs/1203.0910
- [L14] K. R. Lamey, D. S. Silver and S. G. Williams, *Vertex-Colored Graphs, Bicycle Spaces and Mahler Measure*, arXiv:1408.6570, first public version 2014-08-27, Section 2. https://arxiv.org/abs/1408.6570
- [K19] S. Klee and M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration*, arXiv:1903.03575, first public version 2019-02-27, Sections 1--2. https://arxiv.org/abs/1903.03575
- [B86] K. A. Berman, *Bicycles and Spanning Trees*, SIAM Journal on Algebraic Discrete Methods 7 (1986), 1--12, doi:10.1137/0607001 (bibliographic record and abstract consulted; complete text not inspected).
