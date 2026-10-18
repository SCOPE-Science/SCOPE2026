# Exact coordinate Fourier frames on invertible finite-field matrices

## Finding
For each prime power \(q\ge2\), integer \(m\ge3\), and nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\), consider the uniformly weighted finite set \(\mathrm{GL}_m(\mathbb F_q)\). On that set restrict the constant function and the one-coordinate plane waves
\[
\chi_{ij,t}(X)=\psi(tX_{ij}),\qquad 1\le i,j\le m,\quad t\in\mathbb F_q^\times.
\]
Their normalized Gram matrix has order \(1+m^2(q-1)\). Put
\[
 a=\frac1{q^m-1},\qquad b=\frac1{(q^m-1)(q^{m-1}-1)},
\]
\[
\begin{aligned}
 C&=1+a,\\
 R&=1+a-(q-1)(m-1)(a+b),\\
 D&=1+a+(q-1)(a+b),\\
 B&=1+a+(q-1)\bigl(-(2m-1)a+(m-1)^2b\bigr),\\
 h&=-m\sqrt{q-1}\,a,\\
 L_\pm&=\frac{1+B\pm\sqrt{(1-B)^2+4h^2}}2.
\end{aligned}
\]
The **complete eigenvalue multiset**, with multiplicities, is
\[
\boxed{\quad L_-\ [1],\quad L_+\ [1],\quad C\ [m^2(q-2)],\quad R\ [2(m-1)],\quad D\ [(m-1)^2].\quad}
\]
A zero multiplicity contributes nothing; when eigenvalues coincide, their listed multiplicities are added. The family is linearly independent for every permitted pair of parameters. Its sharp lower and upper Riesz bounds are
\[
\boxed{\quad A_{q,m}=L_-,\qquad
 B_{q,m}=\begin{cases}D,&3\le m<2q,\\ L_+,&m\ge2q.\end{cases}\quad}
\]
Both regimes occur, and equality at the threshold is **strictly** on the second branch: \(L_+>D\) when \(m=2q\). The squared condition number is \(B_{q,m}/A_{q,m}\).

For fixed field size and increasing matrix dimension,
\[
\boxed{\quad\frac{B_{q,m}}{A_{q,m}}=1+\frac{2\sqrt{q(q-1)}\,m}{q^m-1}+o\!\left(\frac m{q^m}\right)\quad(m\to\infty).\quad}
\]
For fixed \(m\ge3\) and \(q\to\infty\) through prime powers the ratio is \(1+2m q^{1-m}+o(q^{1-m})\).

## Assumptions and scope
The inner product is \(\langle f,g\rangle=|\mathrm{GL}_m(\mathbb F_q)|^{-1}\sum_{X\in\mathrm{GL}_m(\mathbb F_q)}\overline{f(X)}g(X)\). Thus columns have norm one and a Riesz bound refers to squared \(L^2\) norm divided by the squared Euclidean coefficient norm. All prime characteristics, including characteristic two, and all prime powers are included. The theorem concerns these \(1+m^2(q-1)\) characters, not every additive character on the matrix space. No independence or stability assertion for larger frequency bands is made.

## Proof
**Rank-one and rank-two Fourier coefficients.** For a nonzero coefficient matrix \(H\in M_m(\mathbb F_q)\), define \(F(H)=\mathbb E_{X\in\mathrm{GL}_m}\psi(\sum H_{ij}X_{ij})\). Invariance under invertible left and right multiplication shows that \(F(H)\) depends only on \(\operatorname{rank}H\). When \(\operatorname{rank}H=1\), the first column of \(X\) is uniformly distributed among the \(q^m-1\) nonzero columns, and elementary additive-character orthogonality gives
\[
 F(H)=-\frac1{q^m-1}=-a.
\]
When \(\operatorname{rank}H=2\), reduce the character to \(\psi(X_{11}+X_{22})\) and denote the first two columns by \(u,v\). They are uniformly distributed among ordered linearly independent pairs. For fixed \(u\ne0\),
\[
\sum_{v\notin\mathbb F_q u}\psi(v_2)
 =-\sum_{t\in\mathbb F_q}\psi(tu_2)
 =-q\mathbf1_{u_2=0}.
\]
Moreover \(\sum_{u\ne0,\ u_2=0}\psi(u_1)=-1\), so the numerator of the rank-two average is \(q\). Dividing by \((q^m-1)(q^m-q)\) yields
\[
 F(H)=\frac q{(q^m-1)(q^m-q)}=b.
\]
These two rank values, known within the more general bilinear-forms Fourier theory, suffice here.

**Gram matrix and complete eigenspaces.** Distinct frequencies at the same coordinate, or at two coordinates sharing a row or column, differ by a rank-one coefficient matrix. Two coordinates in different rows and columns give rank two. Thus all nondiagonal Gram entries are \(-a\) in the first case and \(b\) in the second; diagonal entries are one. The constant-frequency column has inner product \(-a\) with every other column.

Split the coefficient space at each coordinate into the one-dimensional direction constant in the nonzero-frequency index and its \(q-2\) dimensional zero-sum complement. All coordinatewise zero-sum contrasts have eigenvalue \(C\), accounting for \(m^2(q-2)\) dimensions. Write the remaining coefficients as \(c_{ij,t}=u_{ij}/\sqrt{q-1}\). The \(m\times m\) array space splits orthogonally into: doubly centered arrays (all row and column sums zero), dimension \((m-1)^2\); arrays \(u_{ij}=r_i+s_j\), with \(\sum_i r_i=\sum_j s_j=0\), dimension \(2(m-1)\); and the constant array, dimension one. The rook-graph adjacency eigenvalues \(-2\), \(m-2\), and \(2(m-1)\) on these three spaces imply respectively \(D\), \(R\), and \(B\). Only the constant array couples to the scalar coefficient of the constant Fourier character. With its unit vector \(u_{ij}=1/m\), this coupling is \(h\); the remaining block is exactly
\[
\begin{pmatrix}1&h\\h&B\end{pmatrix},
\]
with eigenvalues \(L_\pm\). This proves the listed spectrum and identifies **all** equality coefficient spaces: arbitrary coordinatewise contrasts for \(C\), row/column contrasts for \(R\), doubly centered arrays for \(D\), and the eigenlines of this displayed real symmetric block for \(L_-\) and \(L_+\).

**Positivity and endpoint ordering.** The quantities \(C,D\) are greater than one. Writing \(e=q^{m-1}-1\), one has
\[
 R=\frac{q^{m-1}}{q^m-1}\left(q-\frac{m-1}{1+q+\cdots+q^{m-2}}\right)>0.
\]
Also \(B<1\), because \(e\ge m-1\) implies \(B\le1+a-m(q-1)a<1\). The Schur complement \(B-h^2\) is the variance of the coordinate-summed character \(\sum_{i,j,t\ne0}\psi(tX_{ij})\), with fixed positive normalization, after subtracting its mean. That sum equals \(q\) times the number of zero entries of \(X\), minus \(m^2\); it is not constant on invertible matrices, as \(I\) and \(I+E_{12}\) show. Hence \(B-h^2>0\), proving \(L_->0\). Finally
\[
 B-R=m(q-1)a\left(\frac{m-1}{e}-1\right)\le0,
\]
so \(L_-<B\le R\). Since \(L_-<B<1<C<D\) and \(L_+>1\), the smallest eigenvalue is always \(L_-\). The largest is either \(D\) or \(L_+\).

For \(D>\max\{1,B\}\), the sign of the characteristic polynomial of the two-dimensional block at \(D\) decides whether \(D>L_+\). A direct simplification gives
\[
(D-1)(D-B)-h^2=m(q-1)a^2\,\Theta_{q,m},
\quad\Theta_{q,m}=\left(q+\frac{q-1}e\right)\left(2-\frac{m-2}e\right)-m.
\]
Since \(e=q^{m-1}-1\ge q(m-2)\), if \(m\le2q-1\) the first factor is strictly larger than \(q\) and the second at least \(2-1/q\); thus \(\Theta_{q,m}>2q-1-m\ge0\). Conversely
\[
\Theta_{q,m}=2q-m+\frac{4q-2-qm}{e}-\frac{(q-1)(m-2)}{e^2}<0
\]
when \(m\ge2q\), because the three displayed terms are nonpositive and the middle one is strictly negative. This proves the sharp branch transition and its strictness.

**Asymptotic expansion.** With fixed \(q\) and \(m\to\infty\), \((1-B)/(ma)\to2(q-1)\) and \(h/(ma)\to-\sqrt{q-1}\). The eigenvalues of the last block therefore give
\[
 L_\pm=1+ma\left[-(q-1)\pm\sqrt{q(q-1)}+o(1)\right].
\]
For large \(m\), the upper branch is \(L_+\), so their ratio has the stated expansion. At fixed \(m\) and growing \(q\), \(1-L_-=(2m-1)q^{1-m}+o(q^{1-m})\) while \(D-1=q^{1-m}+o(q^{1-m})\), proving the other limit.

## Verification
The standalone script `verify.py` enumerates invertible matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\) and over \(\mathbb F_4\) using polynomial arithmetic. It directly forms all character columns, computes their normalized Gram matrix, and independently compares every entry and the full eigenspectrum with the formulas. Eight parameter cases are checked, including \((q,m)=(2,4)\), where the upper-bound regime changes. It also checks the transition inequality by exact rational arithmetic at 576 parameter pairs. The numerical eigenvalue comparison has maximal observed absolute discrepancy below \(3\cdot10^{-15}\). The unrestricted proof above is algebraic; a finite checker is supporting corroboration, not an infinite proof.

## Relationship to prior work
Delsarte's 1978 bilinear-forms association scheme supplies general rank-dependent additive Fourier character sums; its Section 3 and Appendix do not give the present one-coordinate restricted Gram spectrum, its equality eigenspaces, or the dimension-field threshold \(m=2q\). Kahn–Komlós (2001) study singularity probabilities of random finite-field matrices rather than this deterministic Fourier-frame conditioning problem. Coordinate-character spectra on rank-one matrix sets and on determinant-one \(2\times2\) matrix sets concern different supports; the new claim is for the full group of invertible \(m\times m\) matrices with \(m\ge3\). The distinction is in the exact resulting spectral and extremizer statements, not merely the names of the supports.

## Limitations
The result covers only the coordinate-frequency band; no claim is made for characters supported on two or more entries simultaneously. The sharp transition is specific to the uniform measure on invertible matrices and this band. The rank-one/two character-sum ingredients themselves are classical. The possibility of an equivalent older diagonalization under alternative terminology, including association-scheme compressions, is a residual historical-priority risk; novelty has not received independent certification.

## References
1. P. Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory, Series A **25** (1978), 226–241, DOI: 10.1016/0097-3165(78)90015-8. In particular, Sections 2–3 and the Appendix.
2. J. Kahn and J. Komlós, *Singularity Probabilities for Random Matrices over Finite Fields*, Combinatorics, Probability and Computing **10** (2001), 137–157, DOI: 10.1017/S096354830100462X.
