# Integral splitting of unit-distance type compatibility in the diameter-four Urysohn space

## Finding

Let \(\mathbb U_4\) be the countable homogeneous universal metric space with distance set \(\{0,1,2,3,4\}\). For every integer \(n\ge1\), individually name an equilateral parameter set \(A=\{a_1,\ldots,a_n\}\) with \(d(a_i,a_j)=4\) for distinct indices. Index a symmetric integer matrix \(M_n\) by all complete nonalgebraic one-point types over \(A\), with an entry equal to one precisely when representatives of the two types can be realized as **distinct points at distance one**.

Put \(q=2^{n-1}\), \(N_n=3^n+nq\), and
\[
T=\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix},\qquad
J_q=\begin{pmatrix}1&\cdots&1\\\vdots&\ddots&\vdots\\1&\cdots&1\end{pmatrix}.
\]
There is an explicit **integer-unimodular congruence**
\[
\boxed{M_n\cong_{\mathbb Z}T^{\otimes n}\oplus\bigoplus_{i=1}^nJ_q.}
\]
Consequently the complete Smith normal form, rational and modular rank, and real inertia are
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(M_n)
=\operatorname{diag}(I_{3^n+n},0_{n(2^{n-1}-1)}),}
\]
\[
\boxed{\operatorname{rank}_{\mathbb F}(M_n)=3^n+n\quad\text{for every field }\mathbb F,}
\]
\[
\boxed{\operatorname{inertia}_{\mathbb R}(M_n)
=\left(\frac{3^n+1}{2}+n,\frac{3^n-1}{2},\,n(2^{n-1}-1)\right).}
\]
In particular, the cokernel has no nontrivial finite torsion, and the signature is \(n+1\). A natural principal submatrix of order \(3^n+n\) has determinant \((-1)^n\).

## Assumptions and scope

A nonalgebraic one-type is a map \(u:A\to\{1,2,3,4\}\) satisfying the metric triangle inequalities relative to the individually named parameters. Since all pairwise parameter distances are four, this is equivalent to \(u_i+u_j\ge4\) for every pair of different indices; the other triangle inequalities are automatic. Its admissible vectors are the disjoint union
\[
\mathcal C=\{2,3,4\}^n,
\qquad
\mathcal S_i=\{u:u_i=1,\ u_j\in\{3,4\}\text{ for }j\ne i\},\quad i=1,\ldots,n.
\]
Each \(\mathcal S_i\) has \(q\) vectors. This gives precisely \(N_n=3^n+nq\) types, including the \(n=1\) boundary. The universal extension property realizes every such type and every finite metric two-point extension satisfying the triangle inequalities. Therefore, for admissible vectors \(u,v\),
\[
(M_n)_{u,v}=\prod_{i=1}^n\mathbf1_{\{|u_i-v_i|\le1\}},
\]
including the diagonal, because distinct representatives of one type can be at unit distance.

No assertion is made about other parameter metrics, larger distance alphabets, different requested mutual distances, or joint realizations of more than two new points.

## Proof

**Step 1: the core block.** Order the types with \(\mathcal C\) first, then \(\mathcal S_1,\ldots,\mathcal S_n\). Write
\[
M_n=\begin{pmatrix}D&H^{\mathsf T}\\H&B\end{pmatrix}.
\]
Index the coordinates of \(\mathcal C\) in the order \(2,3,4\). Their one-coordinate compatibility matrix is \(T\), so \(D=T^{\otimes n}\). Direct integer arithmetic gives
\[
\det T=-1,\qquad
T^{-1}=\begin{pmatrix}0&1&-1\\1&-1&1\\-1&1&0\end{pmatrix}.
\]
Thus \(D\) and \(D^{-1}=(T^{-1})^{\otimes n}\) are integral and unimodular.

**Step 2: the exceptional block.** If \(u\in\mathcal S_i\) and \(v\in\mathcal S_j\), compatibility holds if and only if \(i=j\). For \(i=j\), both have a one at coordinate \(i\) and all other coordinates are threes or fours, whose differences are at most one. For \(i\ne j\), at coordinate \(i\) the two values are one and at least three, so compatibility fails. Hence
\[
B=\bigoplus_{i=1}^nJ_q.
\]

**Step 3: an integral isotropy identity.** Every row of \(H\) is a tensor product of one-coordinate row vectors. At its exceptional coordinate the factor is \(e=(1,0,0)\); at all other coordinates the factor is either \(r_3=(1,1,1)\) or \(r_4=(0,1,1)\), according as the exceptional type has value three or four. A direct multiplication with the displayed integer inverse shows
\[
eT^{-1}e^{\mathsf T}=0,
\qquad eT^{-1}r_3^{\mathsf T}=0,
\qquad eT^{-1}r_4^{\mathsf T}=0.
\]
For two arbitrary rows of \(H\), choose the exceptional coordinate of the first row. In the second row that factor is one of \(e,r_3,r_4\). Since the bilinear form defined by \(D^{-1}\) is the tensor product of the one-coordinate bilinear forms, the corresponding entry of \(HD^{-1}H^{\mathsf T}\) is zero. Therefore
\[
\boxed{HD^{-1}H^{\mathsf T}=0}\qquad\text{as an exact integer matrix identity.}
\]

**Step 4: explicit congruence.** The block integer matrix
\[
P=\begin{pmatrix}I_{3^n}&-D^{-1}H^{\mathsf T}\\0&I_{nq}\end{pmatrix}
\]
has determinant one and an integral inverse. By ordinary block multiplication,
\[
P^{\mathsf T}M_nP
=\begin{pmatrix}D&0\\0&B-HD^{-1}H^{\mathsf T}\end{pmatrix}
=D\oplus\bigoplus_{i=1}^nJ_q.
\]
This proves the claimed integral congruence for every positive integer \(n\), without a finite-size extrapolation.

**Step 5: arithmetic, inertia, and the principal core.** A unimodular integer matrix has all Smith factors equal to one. Each all-ones block \(J_q\) is integrally congruent to \(\operatorname{diag}(1,0_{q-1})\) by replacing each basis vector after the first by its difference from the first. The Smith form and field-independent rank therefore follow from Step 4. The eigenvalues of \(T\) are \(1+\sqrt2,1,1-\sqrt2\), with two positive and one negative. Tensor multiplication gives \((3^n+1)/2\) positive and \((3^n-1)/2\) negative eigenvalues of \(D\): their difference is \((2-1)^n=1\). Each \(J_q\) adds one positive and \(q-1\) zero eigenvalues. Sylvester's law of inertia gives the stated inertia and signature.

Finally, select all \(3^n\) core types and exactly one type from each \(\mathcal S_i\). The corresponding principal block has Schur complement \(I_n\) by Step 3. Its determinant is \(\det D=(\det T)^{n3^{n-1}}=(-1)^n\), proving the advertised unimodular principal core.

## Verification

The standalone `VERIFY.py` reconstructs the admissible Katětov vectors by testing every original triangle inequality, independently enumerates unit-distance compatible pairs, verifies the core tensor and exceptional blocks, computes the full integer Schur cancellation, and checks ranks modulo \(2\), \(3\), and \(5\) for every \(1\le n\le4\). It reports sizes \(4,13,39,113\); ranks \(4,11,30,85\); and nullities \(0,2,9,28\), and terminates with `VERIFY_OK`. These finite computations corroborate, but do not replace, the all-parameter integral proof above.

## Relationship to prior work

Sauer's 2010 paper develops Katětov type functions and the possible distances between their realization orbits. In particular, its Section 4 identifies possible mutual distances from the coordinatewise triangle inequalities. The present compatibility predicate follows from that known criterion; its new content is the exact, all-parameter **integral congruence and Smith/inertia classification** of the resulting exponentially sized matrix on an equilateral distance-four parameter base.

Conant's 2015 treatment identifies the integral Urysohn space of bounded diameter as a Fraïssé limit, supplying the wider model-theoretic framework, but the inspected material treats classification properties rather than these integral compatibility matrices.

Previously available related results include a diameter-three one-type polynomial identified with a Widom–Rowlinson partition function; a diameter-four scalar one-type census over randomly sampled parameter metrics; and a unit-distance compatibility matrix over an all-distance-three base in the diameter-three Urysohn space. Respectively, these provide different metric alphabets, scalar counts rather than an integral two-type compatibility matrix, or a distinct compatibility matrix. None of these stated results implies the \(T^{\otimes n}\oplus J_q^{\oplus n}\) congruence. Searches did not identify an exact previous formula; absence from a searched index does not establish priority.

## Limitations

The parameter set must be individually named and equilateral at distance four; the ambient distance alphabet is exactly \(\{0,1,2,3,4\}\). All assertions concern the existence of two distinct realizations at mutual distance one, not a globally consistent graph on all type realizations. The proof determines inertia, not the complete nonzero eigenvalue multiset of the full matrix. An unindexed equivalent combinatorial principal-submatrix result remains possible; independent mathematical validation has not been carried out.

## References

1. N. W. Sauer, *Partitions of metric spaces with finite distance sets*, initial arXiv posting 20 October 2010, arXiv:1010.4212, https://arxiv.org/abs/1010.4212. Relevant material: Sections 2 and 4.
2. G. Conant, *Neostability in countable homogeneous metric spaces*, initial arXiv posting 9 April 2015, arXiv:1504.02427, https://arxiv.org/abs/1504.02427. Relevant material: Introduction, Example 1.1.
3. *Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space*, previously published report, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-widom-rowlinson-partition-functions-as-1-type-polynomials-of-the--ec80747a5989/RESULT.md. Used only for overlap comparison.
