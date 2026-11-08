# Fourier support and exact singular spectrum of finite-field matrix-commutator graphs

## Finding
For a prime power \(q\ge2\) and an integer \(n\ge2\), consider the **matrix-commutator graph**
\[
\Gamma_{n,q}=\{(X,Y,XY-YX):X,Y\in M_n(\mathbb F_q)\}\subseteq M_n(\mathbb F_q)^3.
\]
The unnormalized additive convolution operator by its indicator has a complete Fourier-support criterion, exactly computable singular-value multiplicities in every matrix size, and a sharp condition number on its nonzero spectral subspace.

Write \(d=n^2\), \(L_C(X)=CX-XC\), and \(c(C)=\dim\ker L_C\). For frequencies \((A,B,C)\) the coefficient is zero unless **both \(A,B\in\operatorname{im}L_C\)**. In the nonzero case, take any \(X_0\) with \(L_C(X_0)=-B\); then
\[
\widehat{\mathbf1}_{\Gamma_{n,q}}(A,B,C)
=q^{d+c(C)}\psi(\operatorname{tr}(AX_0)).
\]
In particular, for each fixed \(C\) the number of nonzero frequencies \((A,B)\) is exactly \(q^{2(d-c(C))}\), all with singular modulus \(q^{d+c(C)}\). The sharp condition number among the positive singular values is \(q^{n^2-n}\), and the smallest positive singular value is \(q^{n^2+n}\).

There is also an explicit **all-dimensional Euler product**. Let \(I_q(r)=r^{-1}\sum_{e\mid r}\mu(e)q^{r/e}\), the number of monic irreducible polynomials of degree \(r\) over \(\mathbb F_q\). For any partition \(\lambda\), write \(\lambda'\) for the conjugate partition, \(m_j(\lambda)\) for the multiplicity of the part \(j\), and
\[
 c_{r,\lambda}=r\sum_{i\ge1}(\lambda_i')^2,\qquad
 a_{r,\lambda}=q^{c_{r,\lambda}}
 \prod_{j\ge1}\prod_{k=1}^{m_j(\lambda)}(1-q^{-rk}).
\]
Empty partitions contribute \(c_{r,\varnothing}=0\), \(a_{r,\varnothing}=1\). Define the formal bivariate series
\[
 \mathcal H_q(z,t)=\prod_{r\ge1}\left(
  \sum_\lambda \frac{z^{r|\lambda|}t^{c_{r,\lambda}}}{a_{r,\lambda}}
 \right)^{I_q(r)}.
\]
For every \(n\ge2\), put \(g_n=|\operatorname{GL}_n(\mathbb F_q)|=\prod_{j=0}^{n-1}(q^n-q^j)\). The positive singular value \(q^{n^2+c}\) occurs precisely
\[
 M_{n,c}=g_n\,q^{2(n^2-c)}[z^nt^c]\mathcal H_q(z,t)
\]
times. Thus the entire convolution rank is the finite coefficient extraction
\[
 \boxed{\operatorname{rank}T_{n,q}=g_nq^{2n^2}[z^n]\mathcal H_q(z,q^{-2}).}
\]
For any fixed \(n\), only polynomial degrees \(r\le n\) and partitions with \(|\lambda|\le n/r\) enter the extraction. The formula is exact and uses no matrix enumeration.

The first genuinely nontrivial closed census is for \(n=3\). Put \(N_5=q(q^2+q+1)(q^3-1)\). Then the only possible centralizer dimensions are \(3,5,9\), and the exact singular values and their multiplicities are

| Positive singular value | Multiplicity |
|:--|:--|
| \(q^{12}\) | \((q^9-q-N_5)q^{12}\) |
| \(q^{14}\) | \(N_5q^8\) |
| \(q^{18}\) | \(q\) |

All remaining \(q^{27}-\operatorname{rank}T_{3,q}\) singular values are zero, with
\[
 \boxed{\operatorname{rank}T_{3,q}=q+(q^9-q-N_5)q^{12}+N_5q^8.}
\]
In particular the ranks at field sizes \(q=2\) and \(q=3\) are respectively \(1{,}712{,}642\) and \(9{,}926{,}530{,}563\).

## Assumptions and scope
All matrices have entries in a finite field \(\mathbb F_q\), not in a local ring. No assumption on parity or primality of \(q\) is made. The additive Fourier transform uses the trace pairing \(\langle A,X\rangle=\operatorname{tr}(AX)\) and a fixed nontrivial character \(\psi:\mathbb F_q\to\mathbb C^\times\). The full ambient additive group has cardinality \(q^{3n^2}\); the convolution operator uses counting measure with no normalization. The graph includes each \((X,Y)\) once. Singular values refer to the usual complex Hilbert space with counting inner product. The bivariate coefficient extraction is a formal-power-series identity, not an assertion of analytic convergence.

## Proof
**1. The Fourier support and phase.** By definition,
\[
F(A,B,C)=\sum_{X,Y\in M_n(\mathbb F_q)}
 \psi(\operatorname{tr}(AX+BY+C(XY-YX))).
\]
Cyclicity of matrix trace converts the dependence on \(Y\) to \(\operatorname{tr}((B+CX-XC)Y)\). Nondegeneracy of the trace pairing and additive-character orthogonality therefore give
\[
F(A,B,C)=q^d\sum_{X:L_C(X)=-B}\psi(\operatorname{tr}(AX)).
\]
The solution fibre, when nonempty, is \(X_0+\ker L_C\). Its character sum is \(q^{c(C)}\psi(\operatorname{tr}(AX_0))\) if \(A\) annihilates \(\ker L_C\), and zero otherwise. As
\[
\operatorname{tr}(A L_C(X))=\operatorname{tr}((AC-CA)X),
\]
the adjoint of \(L_C\) for the trace pairing is \(-L_C\). Hence \((\ker L_C)^\perp=\operatorname{im}L_C\) in every characteristic. This proves the exact support, nonzero formula and, by Fourier diagonalization of additive convolution, the nonzero singular-value magnitudes and per-\(C\) multiplicities.

**2. Rational-canonical enumeration.** Regard an \(n\)-square matrix as a finite torsion \(\mathbb F_q[t]\)-module. For each monic irreducible \(f\) of degree \(r\), its \(f\)-primary module is indexed by a partition \(\lambda_f\). The dimension of its commuting endomorphism algebra is \(r\sum_i(\lambda'_{f,i})^2\); different primary summands have no nonzero intertwiners. The automorphism group of one primary summand has order
\[
a_{r,\lambda}=q^{r\sum_i(\lambda_i')^2}
\prod_{j\ge1}\prod_{k=1}^{m_j(\lambda)}(1-q^{-rk}).
\]
To verify the factor, its endomorphism ring has vector-space dimension \(r\sum_i(\lambda_i')^2\), and its quotient by the Jacobson radical is \(\prod_j M_{m_j(\lambda)}(\mathbb F_{q^r})\). Elements are units precisely when their reductions in every matrix block are units. Consequently a rational-canonical module type corresponds to \(g_n/\prod_fa_{\deg f,\lambda_f}\) labelled matrices. Multiplying its terms \(t^{c(C)}\), grouping irreducibles by degree, and extracting \(z^n\) gives
\[
\sum_{C\in M_n(\mathbb F_q)}t^{c(C)}=g_n[z^n]\mathcal H_q(z,t).
\]
Substituting \(t=q^{-2}\) and multiplying by \(q^{2n^2}\) yields the convolution-rank formula and all singular-value multiplicities.

**3. Sharp conditioning.** For every primary partition, \(\sum_i(\lambda_i')^2\ge\sum_i\lambda_i'=|\lambda|\), hence \(c(C)\ge n\). Equality occurs for cyclic matrices, for example a companion matrix of a monic irreducible polynomial of degree \(n\). The maximum \(c(C)=n^2\) occurs exactly for scalar matrices, since their centralizer is the whole matrix algebra. The least and greatest positive singular values are therefore \(q^{n^2+n}\) and \(q^{2n^2}\). Their ratio is \(q^{n^2-n}\).

**4. The closed three-by-three census.** A non-scalar \(3\)-square matrix is noncyclic exactly in two disjoint cases: it is a scalar translate of a nonzero rank-one square-zero operator, or it has two distinct eigenvalues with a two-dimensional eigenspace and a complementary one-dimensional eigenspace. Both have centralizer dimension five. The first family has \(q(q^3-1)(q^2-1)/(q-1)\) elements: choose a nonzero image vector and a nonzero annihilating functional, then quotient by common scaling, and choose the scalar shift. The second has \(q(q-1)(q^2+q+1)q^2\) elements: choose ordered eigenvalues, a plane, and one of its \(q^2\) complementary lines. Their sum is \(N_5=q(q^2+q+1)(q^3-1)\). There are exactly \(q\) scalar matrices with centralizer dimension nine. Every remaining matrix is cyclic and has centralizer dimension three. Substitution into step 1 proves the explicit three-level spectrum and rank.

## Verification
The accompanying standalone Python program `check_commutator.py` reconstructs \(\operatorname{ad}_C\) over prime fields; exhaustively enumerates centralizer ranks for all \(3\)-square matrices over \(\mathbb F_2\) and \(\mathbb F_3\); directly sums character phases over all matrix pairs for multiple test frequencies at sizes \(2\) and \(3\); and independently expands the exact rational-canonical bivariate series at matrix sizes \(1,2,3\) and field orders \(2,3,4\). In particular, the exact series tests include the nonprime field order four without enumerating that field's matrices.

The direct character sums use double-precision evaluation of roots of unity with stated tolerances, while all centralizer counts and formal-series coefficients are integer/rational exact. These checks are finite corroboration only. The all-field, all-dimension conclusion is proved algebraically above.

## Relationship to prior work
Finite-field matrix centralizers, commuting class types, and rational-canonical methods are classical; see Britnell--Wildon and the earlier counting theorem of Feit--Fine. Feichtinger--Kozek--Luef develop finite-abelian harmonic analysis and operator-spreading methods. The present Fourier spectrum is for the additive indicator of the **graph of the binary commutator** in three matrix variables, rather than for commuting pairs themselves or Gabor frames. In particular, the Feit--Fine counting quantity involves counts of commuting pairs and does not by itself determine the inverse-weighted centralizer statistic entering this convolution rank. The general bilinear-character orthogonality method is standard and is not asserted to be new; the assessed result is the complete all-size spectral organization and explicit three-by-three centralizer-stratum census for this canonical graph.

## Limitations
The result does not classify complex phases jointly across frequencies beyond the explicit phase formula, does not treat matrix rings of nonzero nilpotency length, and makes no assertion about nonabelian convolution on matrix groups. Its proof uses standard finite-field character orthogonality and rational-canonical classification. A more general pre-existing theorem on Fourier transforms of bilinear graphs, combined with matrix centralizer tables, might imply portions or all of this classification. No claim of independent mathematical validation or exhaustive priority is made.

## References
1. H. G. Feichtinger, W. Kozek, F. Luef, *Gabor analysis over finite Abelian groups*, first public preprint 2007-03-08, arXiv:math/0703228; https://arxiv.org/abs/math/0703228.
2. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, first public preprint 2010-01-06, arXiv:1001.0811; https://arxiv.org/abs/1001.0811.
3. W. Feit and N. J. Fine, *Pairs of commuting matrices over a finite field*, Duke Math. J. 27 (1960), 91–94; https://doi.org/10.1215/S0012-7094-60-02709-5.
