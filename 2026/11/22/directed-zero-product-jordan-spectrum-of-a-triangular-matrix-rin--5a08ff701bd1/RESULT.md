# Directed zero-product Jordan spectrum of a triangular matrix ring

## Finding
Let \(q\ge 2\) be any prime power, \(F=\mathbb F_q\), and \(R=\operatorname{UT}_2(F)\). Form the **loopless directed zero-divisor graph** \(\Gamma_q\): its vertices are the nonzero nonunits of \(R\), and there is an arc from distinct vertices \(X\) to \(Y\) exactly when \(XY=0\). Let \(A_q\) be its ordinary zero-one adjacency matrix, acting over \(\mathbb C\). Define
\[
P_q(z)=z^3-(q-2)z^2-q(q-1)^2(z+1).
\]
Then \(\Gamma_q\) has \((2q+1)(q-1)\) vertices and
\[
\det(zI-A_q)=z^{2q(q-1)-2}(z+1)^{q-2}P_q(z).
\]
Its **complete complex Jordan form** consists of exactly \(q-1\) blocks \(J_2(0)\), exactly \(2q(q-2)\) blocks \(J_1(0)\), exactly \(q-2\) blocks \(J_1(-1)\), and three simple one-dimensional blocks whose eigenvalues are the (pairwise distinct, nonzero, non-\(-1\)) roots of \(P_q\). In particular, for every \(q\),
\[
\operatorname{rank}_{\mathbb C}(A_q)=2q,\qquad
\operatorname{rank}_{\mathbb C}(A_q^m)=q+1\quad(m\ge2).
\]
The graph is strongly connected and its adjacency matrix is not diagonalizable. The powers in the rank assertion are ordinary integer matrix powers, not powers taken in the ring.

## Assumptions and scope
A vertex is a matrix \(X=\begin{pmatrix}a&b\\0&c\end{pmatrix}\) with \((a,b,c)\ne(0,0,0)\) and \(ac=0\). In this finite ring, nonunits are exactly the zero divisors; the zero matrix and all loops are removed. The relation is directed: \(XY=0\) is not replaced by \(YX=0\) or by the symmetric relation \(XY=0\) **or** \(YX=0\). Adjacency is evaluated in \(F\); the characteristic polynomial, Jordan form and ranks are evaluated over \(\mathbb C\), not over a field of characteristic dividing \(q\). These choices are essential.

## Proof
Put \(k=q-1\). Partition the vertices into \(\mathcal A=\{(a,b,0):a\ne0\}\), \(\mathcal B=\{(0,b,c):c\ne0\}\), and \(\mathcal C=\{(0,b,0):b\ne0\}\). The first two sets each have \(qk\) elements and the third has \(k\). For each \(t,s\in F\), introduce slope fibers \(\mathcal A_t=\{(a,at,0):a\in F^\times\}\) and \(\mathcal B_s=\{(0,sc,c):c\in F^\times\}\), each of size \(k\).

Multiplication gives \((a,b,c)(d,e,f)=(ad,ae+bf,cf)\). Thus the **complete list of arcs** is: every vertex in \(\mathcal A_t\) points to every vertex in \(\mathcal B_{-t}\); every vertex in \(\mathcal B_s\) points to every vertex in \(\mathcal A\) and every vertex in \(\mathcal C\); every vertex in \(\mathcal C\) points to every vertex in \(\mathcal A\) and every *other* vertex in \(\mathcal C\). No other arcs occur. This classification also proves strong connectivity: each \(\mathcal A_t\) reaches \(\mathcal B_{-t}\), each \(\mathcal B_s\) reaches all \(\mathcal A_t\) and \(\mathcal C\), and each \(\mathcal C\) reaches \(\mathcal A\).

Regard \(A_q\) as an operator on complex-valued functions on the vertices. In each slope fiber \(\mathcal A_t\), respectively \(\mathcal B_s\), the mean-zero subspace has dimension \(k-1\) and lies in \(\ker A_q\). These give \(2q(k-1)=2q(q-2)\) one-dimensional zero blocks. The mean-zero functions supported on \(\mathcal C\) form a \((k-1)\)-dimensional eigenspace of eigenvalue \(-1\), since the loopless complete digraph there contributes \(J_k-I_k\). This decomposition is direct over \(\mathbb C\) because \(k\ne0\).

The remaining subspace comprises functions constant on each slope fiber and on \(\mathcal C\). It has dimension \(2q+1\). Split the \(q\)-component fiber-value vectors into constants and coordinate-sum-zero vectors (directly over \(\mathbb C\), since \(q\ne0\)). A mean-zero vector on the \(\mathcal B_s\) fibers maps to the \(\mathcal A_t\) slope vector with entries \(k b_{-t}\); each mean-zero \(\mathcal A_t\) vector maps to zero. Hence there are precisely \(q-1\) zero-eigenvalue Jordan chains of length two.

On the remaining three-dimensional uniform space, with coordinates \((\alpha,\beta,\gamma)\) of constant values on all \(\mathcal A\), all \(\mathcal B\), and all \(\mathcal C\), respectively, the action is
\[
T_q=\begin{pmatrix}0&k&0\\qk&0&k\\qk&0&k-1\end{pmatrix}.
\]
A determinant expansion yields \(\det(zI_3-T_q)=P_q(z)\), \(\det T_q=qk^2\ne0\), and \(P_q(-1)=1-q\ne0\). All three roots are simple: the cubic discriminant is
\[
q(q-1)^2\bigl(4q^6-15q^5+38q^3-20q^2-35q+32\bigr).
\]
At \(q=2\), the parenthesis is \(-38\). For \(q=3+t\) and \(t\ge0\), it is
\[
4t^6+57t^5+315t^4+848t^3+1132t^2+628t+44>0.
\]
Therefore there are no repeated roots for any permitted \(q\).

The direct-sum dimensions add to \(2qk+k\), giving the stated characteristic and Jordan polynomials. Each \(J_2(0)\) contributes one to the rank of \(A_q\) but zero to all powers \(A_q^m\), \(m\ge2\); all \(-1\) and three cubic eigenvalues remain nonzero under powers. Thus \(\operatorname{rank}(A_q)=q-1+q-2+3=2q\) and \(\operatorname{rank}(A_q^m)=q-2+3=q+1\) for \(m\ge2\). Since \(q-1>0\), \(A_q\) is never diagonalizable.

## Verification
The included standalone `checker.py` constructs \(\Gamma_q\) directly from upper-triangular multiplication, independently of the slope-fiber proof, for \(q=2,3,4,5\) (using an explicit field \(\mathbb F_4\)). It checks the vertex count, complete characteristic polynomial, matrix rank, \(-1\)-eigenspace dimension, and number of nilpotent length-two chains using exact symbolic ranks. The saved `verification_output.txt` contains the actual output. These finite tests corroborate but do not prove the all-prime-power statement; the general proof is the preceding block decomposition.

## Relationship to prior work
Redmond introduced directed zero-divisor graphs of noncommutative rings. Li and Tucci (2013) describe the zero-divisor graph of triangular matrix rings and the finite-domain two-by-two case in particular, including elementary graph properties and an edge formula. Their graph structure is foundational here: neither the vertex classification nor the zero-product relation is claimed as new. Hemati (2020) gives adjacency eigenvalues for an undirected two-by-two triangular-ring graph in the two-element base case, which differs from the directed adjacency matrix studied here. The assessed finding is the all-finite-field **directed complex Jordan decomposition**, especially its nontrivial nilpotent blocks and exact rank stabilization, rather than the underlying graph's known construction. Additional relevant spectral literature on commutative zero-divisor graphs concerns different, symmetric matrices.

## Limitations
Only the two-by-two upper-triangular ring over a field is covered. The directed graph has no loops; retaining loops changes the answer. The spectrum is over \(\mathbb C\), not over \(\mathbb F_q\); reducing the matrix modulo the field characteristic can change ranks and Jordan blocks. The 2013 article's full text could not be inspected in this review beyond its accessible first-page abstract, although its reported full description of this directed graph creates a substantive implicit-priority risk. The conclusion is therefore a best-knowledge formula and proof, **not** a claim of independently established publication priority. No independent mathematical audit has been performed.

## References
1. A. Li and R. P. Tucci, *Zero Divisor Graphs of Upper Triangular Matrix Rings*, Communications in Algebra **41** (2013), 4622–4636. DOI: https://doi.org/10.1080/00927872.2012.706841. Publicly online 2013-09-20.
2. S. P. Redmond, *The Zero-Divisor Graph of a Non-Commutative Ring*, International Journal of Commutative Rings **1** (2002), 203–221.
3. H. Sherin, *Eigenvalue of Adjacent Matrix of Zero Divisor Graphs on Rings*, Engineering and Technology Quarterly Reviews **3** (2020), 63–66. DOI: https://doi.org/10.5281/zenodo.4011991.
4. K. Mönius, *Eigenvalues of zero-divisor graphs of finite commutative rings*, Journal of Algebraic Combinatorics **54** (2021), 787–802; online 2020-11-17. https://doi.org/10.1007/s10801-020-00989-6.
