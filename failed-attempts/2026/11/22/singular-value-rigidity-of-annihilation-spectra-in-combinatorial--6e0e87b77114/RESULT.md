# Singular-value rigidity of annihilation spectra in combinatorial Rees semigroups

## Finding

Let \(I\) and \(\Lambda\) be nonempty finite sets, with \(|I|=m\) and \(|\Lambda|=n\). Let \(P\in\{0,1\}^{\Lambda\times I}\) have at least one nonzero entry in every row and column. Form the combinatorial completely \(0\)-simple semigroup \(S=M^0[1;I,\Lambda;P]\), with nonzero elements \((i,\lambda)\) and multiplication
\[
(i,\lambda)(j,\mu)=\begin{cases}(i,\mu),&P_{\lambda j}=1,\\0,&P_{\lambda j}=0.\end{cases}
\]
Remove the zero element, and define the *mutual-annihilation relation matrix* \(B\) on \(I\times\Lambda\) by
\[
B_{(i,\lambda),(j,\mu)}=\mathbf1\{(i,\lambda)(j,\mu)=(j,\mu)(i,\lambda)=0\}.
\]
This is a real symmetric \(mn\)-by-\(mn\) zero-one matrix; it includes diagonal entries precisely for square-zero elements. Put \(Z_{\lambda i}=1-P_{\lambda i}\), and let \(s_1,\ldots,s_r>0\) be the positive singular values of the real \(n\)-by-\(m\) matrix \(Z\), counted with multiplicity, where \(r=\operatorname{rank}_{\mathbb R}Z\).

**Exact spectral theorem.** The characteristic polynomial of \(B\) is
\[
\boxed{\det(tI-B)=t^{mn-r^2}\prod_{a=1}^r(t-s_a^2)\prod_{1\le a<b\le r}(t^2-s_a^2s_b^2).}
\]
Thus its positive, negative and zero inertia is exactly
\[
\boxed{\left(\frac{r(r+1)}2,\frac{r(r-1)}2,mn-r^2\right).}
\]
The spectral energy and all positive closed-walk moments reduce to the much smaller sandwich zero-pattern matrix:
\[
\sum_{\theta\in\operatorname{Spec}(B)}|\theta|=\left(\sum_{a=1}^r s_a\right)^2=\|Z\|_*^2,
\]
\[
\operatorname{tr}(B^{2k})=\bigl(\operatorname{tr}((ZZ^{\mathsf T})^k)\bigr)^2\quad(k\ge1),
\qquad
\operatorname{tr}(B^{2k+1})=\operatorname{tr}((ZZ^{\mathsf T})^{2k+1})\quad(k\ge0).
\]
For fixed \((m,n)\), two such semigroups have cospectral mutual-annihilation matrices **if and only if** their zero-pattern matrices have the same nonzero singular values, including multiplicities.

Writing \(z=\sum_{\lambda,i}Z_{\lambda i}\), the total number of ordered nonzero-element pairs with both products zero is \(z^2\); the associated simple mutual-annihilation graph has \((z^2-z)/2\) edges. The looped degree at vertex \((i,\lambda)\) is the number of zeros in row \(\lambda\) multiplied by the number of zeros in column \(i\).

## Assumptions and scope

The sets \(I,\Lambda\) are finite and nonempty. The entries of \(P\) lie in \(\{0,1\}\), and \(P\) is regular (no zero row or column), so the semigroup is completely \(0\)-simple with trivial maximal subgroups. All spectral statements concern the **real** symmetric relation matrix on the \(mn\) *nonzero* semigroup elements, not the standard simple commuting graph's adjacency matrix. In particular, an entry \(B_{x,x}\) equals one only if \(x^2=0\); no universal self-commutation loops are added. The theorem also remains algebraically true without regularity, but complete \(0\)-simplicity is then not asserted. When \(Z=0\), interpret empty products as one and all spectra as zero.

## Proof

**1. The semigroup-to-matrix identity.** The two products of \((i,\lambda)\) and \((j,\mu)\) are zero precisely when \(P_{\lambda j}=P_{\mu i}=0\). Consequently
\[
B_{(i,\lambda),(j,\mu)}=Z_{\lambda j}Z_{\mu i}.
\]
Identify \(\mathbb R^{I\times\Lambda}\) with real \(m\)-by-\(n\) matrices, with coordinates \(X_{j\mu}\). Multiplication by \(B\) is the self-adjoint linear map
\[
\mathcal B(X)=(ZXZ)^{\mathsf T}.
\]
The dimensions match: \(Z\) is \(n\)-by-\(m\), so \(ZXZ\) is \(n\)-by-\(m\).

**2. Rectangular singular-value decomposition.** Take an orthogonal singular-value decomposition \(Z=U\Sigma V^{\mathsf T}\), with \(U\) of size \(n\)-by-\(n\) and \(V\) of size \(m\)-by-\(m\). The isometry \(Y\mapsto VYU^{\mathsf T}\) identifies \(\mathbb R^{m\times n}\) with itself and transforms the operator to
\[
Y\longmapsto(\Sigma Y\Sigma)^{\mathsf T}.
\]
For \(1\le a\le r\), the matrix unit \(E_{aa}\) is an eigenvector with eigenvalue \(s_a^2\). For every \(1\le a<b\le r\), the two vectors \(E_{ab}+E_{ba}\) and \(E_{ab}-E_{ba}\) have eigenvalues \(s_as_b\) and \(-s_as_b\). All other matrix units are annihilated. These form a basis of \(\mathbb R^{m\times n}\), establishing the full characteristic polynomial, the exact number \(r^2\) of nonzero eigenvalues, and the inertia, including repeated singular values and rectangular dimensions. Summing absolute eigenvalues gives \(\|Z\|_*^2\), and summing powers gives the two trace formulas.

**3. Reverse spectral rigidity.** Put \(t_a=s_a^2>0\). Every odd trace of \(B\) is \(\sum_at_a^{2k+1}\), because paired positive and negative eigenvalues cancel. Hence \(\operatorname{Spec}(B)\) determines the rational generating function
\[
\sum_{k\ge0}\operatorname{tr}(B^{2k+1})u^k=\sum_{a=1}^r\frac{t_a}{1-t_a^2u}.
\]
Every pole is positive and equal to \(1/t_a^2\) for some positive \(t_a\); its coefficient determines the multiplicity of that value. Thus the nonzero singular values and their multiplicities are uniquely recovered. Conversely step 2 constructs \(\operatorname{Spec}(B)\) from those singular values. With the matrix size fixed, this proves the cospectrality equivalence.

**4. Combinatorial counts.** Each ordered choice of a zero position \((\lambda,j)\) and a second zero position \((\mu,i)\) determines exactly one ordered pair \(((i,\lambda),(j,\mu))\) with both products zero. There are \(z^2\) such pairs. Precisely \(z\) have coinciding elements, so there are \((z^2-z)/2\) unordered pairs of distinct elements. For fixed \((i,\lambda)\), \(j\) ranges over zeros in row \(\lambda\), independently of \(\mu\) ranging over zeros in column \(i\), proving the stated degree product.

## Verification

The accompanying standalone file `check_spectrum.py` constructs each \(0\)-Rees product directly, forms \(B\) from products, independently computes the singular values of the zero-pattern matrix, and compares all eigenvalues, energy, rank-related moments, diagonal and ordered-pair counts. It exhaustively tests all **327** regular binary sandwich patterns with both dimensions between one and three, and another **400** randomly seeded patterns of dimensions \((4,4),(4,5),(5,4),(6,6)\). Both test groups pass; see `checker_output.txt`. These finite tests corroborate but do not replace the dimension-independent proof above.

## Relationship to prior work

Jackson and Volkov (2009) define the adjacency/Rees semigroup construction and study universal Horn classes and unary semigroup varieties, not spectral annihilation invariants. Giudici and Kuzma (2015) study realizability of general semigroup commuting graphs. Paulista (2025, Section 3, Lemma 3.2) supplies the general commuting criterion for completely \(0\)-simple Rees semigroups and studies connectivity, diameter, cliques, girth and chromatic bounds; in the trivial-group case, this directly yields the zero-pattern **adjacency criterion** used in step 1. The spectral factorization, inertia, moments, energy, and reverse cospectrality implication are not stated in the inspected portions of those works. Related spectral decompositions for mutual-inverse and other annihilation graphs involve different semigroups and different relation matrices; their singular-value techniques are conceptually relevant but do not by themselves provide this Rees-family classification.

## Limitations

This is a real spectral classification for the looped mutual-zero-product relation, not for arbitrary group-labelled Rees matrices, the usual loopless commuting graph, or nonzero-product commutation. The matrix-spectrum result follows from a precise transpose-twisted singular-value factorization once the Rees multiplication is unpacked. It does not assert a new singular-value-decomposition theorem, a uniqueness theorem for semigroup isomorphism classes, or historical uniqueness. The previously published commuting criterion is explicitly used rather than newly claimed. A historical formulation of this same spectral reduction may exist in spectral graph or semigroup literature outside the inspected references.

## References

1. M. Jackson and M. Volkov, *The algebra of adjacency patterns: Rees matrix semigroups with reversion*, arXiv:0907.2634v1, first publicly posted 2009-07-15. https://arxiv.org/pdf/0907.2634
2. M. Giudici and B. Kuzma, *Realizability problem for commuting graphs*, arXiv:1505.05397, first posted 2015-05-20. https://arxiv.org/abs/1505.05397
3. T. Paulista, *Commuting graphs of completely 0-simple semigroups*, arXiv:2510.23871v1, first posted 2025-10-27, especially Lemma 3.2 and Section 3. https://arxiv.org/pdf/2510.23871
4. A. Nagy, *Commuting graphs of Rees matrix semigroups*, *Semigroup Forum*, online 2025-11-18. https://doi.org/10.1007/s00233-025-10597-0
