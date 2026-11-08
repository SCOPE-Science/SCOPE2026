# Perfect evolution algebras with exactly \(n\) idempotents in dimension \(n\)

## Finding

**Theorem.** For every integer \(n\geq 2\) and every field \(K\) with \(\operatorname{char}K\neq 2\), there is an explicit perfect evolution \(K\)-algebra of dimension \(n\) having exactly \(n\) distinct idempotents, including zero. The construction works over the prime field, and every idempotent is \(K\)-rational. In particular, this realizes the previously unaccounted-for count \(n\), for every \(n\geq3\), in the complex idempotent-count problem of Kaygorodov, Martín González and Viruel.

## Assumptions and scope

An evolution algebra \(E\) over \(K\) has a *natural basis* \(e_1,\ldots,e_n\) with \(e_i e_j=0\) for distinct indices. Its structure matrix \(M=(m_{ij})\) is defined by \(e_i^2=\sum_jm_{ij}e_j\). The algebra is *perfect* if \(E^2=E\), equivalently if \(M\) is invertible. An *idempotent* is an element \(x\) satisfying \(x^2=x\); distinct means distinct elements, not scheme-theoretic multiplicities.

Fix \(n\ge2\). Put
\[
 m_{11}=m_{22}=\frac34,\qquad m_{12}=m_{21}=\frac14,
\]
\[
 m_{jj}=1\quad(3\le j\le n),\qquad
 m_{1j}=\frac14\left(\frac34\right)^{j-3}\quad(3\le j\le n),
\]
\[
 m_{ij}=\frac14\left(\frac34\right)^{j-i-1}\quad(3\le i<j\le n),
\]
with all unlisted entries zero. Fractions are interpreted in \(K\); only invertibility of \(2\) is assumed. Denote this algebra by \(E_n(K)\).

**Exact list of idempotents.** The complete list consists of zero, the element with coordinate vector
\[
 (1,1,\underbrace{\tfrac12,\ldots,\tfrac12}_{n-2}),
\]
and, for every \(k\) with \(3\le k\le n\), the vector
\[
 (\underbrace{0,\ldots,0}_{k-1},1,
 \underbrace{\tfrac12,\ldots,\tfrac12}_{n-k}).
\]
Empty strings are allowed. Thus the list has \(1+1+(n-2)=n\) elements and is valid for \(n=2\) as well.

For \(n=3\), the multiplication is particularly simple:
\[
 e_1^2=\tfrac34e_1+\tfrac14e_2+\tfrac14e_3,\qquad
 e_2^2=\tfrac14e_1+\tfrac34e_2,\qquad e_3^2=e_3,
\]
and its only idempotents are \(0\), \(e_3\), and \(e_1+e_2+\tfrac12e_3\).

## Proof

**Perfection.** The matrix is block upper triangular, with diagonal blocks
\[
 \begin{pmatrix}3/4&1/4\\1/4&3/4\end{pmatrix},1,\ldots,1.
\]
Its determinant is \((9-1)/16=1/2\), nonzero in \(K\). Therefore \(E_n(K)^2=E_n(K)\).

**The first two coordinates.** Write \(x=\sum_{i=1}^n x_i e_i\). Since mixed products of natural basis vectors vanish, \(x^2=x\) is equivalent to
\[
 x_j=\sum_{i=1}^n m_{ij}x_i^2\qquad(1\le j\le n).
\]
In particular,
\[
 x_1=\tfrac34x_1^2+\tfrac14x_2^2,\qquad
 x_2=\tfrac14x_1^2+\tfrac34x_2^2.
\]
Subtracting and adding yield
\[
 (x_1-x_2)\left(1-\frac{x_1+x_2}{2}\right)=0,
 \qquad x_1+x_2=x_1^2+x_2^2.
\]
If \(x_1=x_2=t\), the latter equation gives \(t=t^2\), hence \(t=0\) or \(t=1\). If \(x_1\neq x_2\), the first relation gives \(x_1+x_2=2\), and the second then gives \(x_1x_2=1\). Thus both coordinates are roots of \((T-1)^2\), forcing \(x_1=x_2=1\), a contradiction. Consequently the only possibilities are \((x_1,x_2)=(0,0)\) and \((1,1)\). This argument is valid in every field of characteristic other than \(2\).

**A two-state recursion.** For \(j\ge3\), let \(h_j\) be the sum of all terms other than \(x_j^2\) in the \(j\)-th idempotent equation. The explicit matrix gives
\[
 x_j=x_j^2+h_j,\qquad h_3=\tfrac14 x_1^2,
 \qquad h_{j+1}=\tfrac34h_j+\tfrac14x_j^2.
\]
If \(h_j=1/4\), then \(x_j^2-x_j+1/4=(x_j-1/2)^2=0\), so \(x_j=1/2\) uniquely; substitution gives \(h_{j+1}=1/4\) again. If \(h_j=0\), then \(x_j^2-x_j=x_j(x_j-1)=0\), so \(x_j=0\) or \(1\). The choice \(0\) leaves \(h_{j+1}=0\), whereas the choice \(1\) switches it to \(1/4\) permanently.

If \((x_1,x_2)=(1,1)\), then \(h_3=1/4\) and all subsequent coordinates are forced to be \(1/2\), producing precisely the listed first nonzero idempotent. If \((x_1,x_2)=(0,0)\), then \(h_3=0\): either every subsequent coordinate is zero, or there is a unique first position \(k\ge3\) at which \(x_k=1\), followed by \(1/2\) in every later coordinate. These are exactly the listed vectors and exhaust all possibilities. Distinctness is immediate from the position of the first nonzero coordinate and from the initial pair. Hence the number of distinct idempotents is exactly \(n\). \(\square\)

## Verification

The reproducible standard-library program `verify.py` builds the displayed rational matrices and explicit idempotent lists. For dimensions \(2\) through \(12\), it checks determinant-block data, every coordinate identity, the recursion, and the independence of the nonzero idempotents' squared-coordinate vectors. It also exhaustively checks every vector in \(\mathbb F_p^n\), for \(p\in\{3,5,7\}\) and \(2\le n\le5\), against the reduced structure matrices and the claimed exact lists. The output in `verification_output.txt` is:

`VERIFY_OK symbolic_dimensions=11 finite_fields_cases=12 brute_force_vectors=23860`

These finite checks do **not** constitute the arbitrary-dimensional proof; that is the preceding symbolic argument. The program uses only the Python standard library. Run `python3 verify.py` from the directory containing that file.

## Relationship to prior work

Kaygorodov, Martín González and Viruel, *Evolution algebras: a survey of results and a list of open problems* (arXiv:2610.22248v1, first public 2026-10-15), Conjecture 6, ask whether for each complex dimension \(n\), every count from \(2\) to \(2^n\) is realizable. Their accompanying discussion states that the triangular constructions considered there yield only counts at least \(n+1\); the case \(n=2\) with exactly two idempotents is known. The present construction realizes the count \(n\) in every dimension \(n\ge3\), by arranging a repeated quadratic root above each nonzero idempotent at each extension step. It does not settle the conjecture's remaining cases, in particular the count \(2\) when \(n\ge3\).

García-Martínez and Pérez-Rodríguez, *A note on complete evolution algebras* (2026), prove existence of nonzero idempotents for complex perfect evolution algebras but do not give these exact counts. Hu, *Full-Support Solutions and Rigidity for Three-Dimensional Evolution Algebras* (2026), studies existence of full-support idempotents and a classification of exceptional nonsingular quadratic systems, not the infinite family of exact cardinalities above. Existing three-dimensional isomorphism classifications do not by themselves determine the count in all dimensions. No general novelty guarantee follows from a failed search; potential implicit equivalents in earlier algebraic-geometry literature remain a priority risk.

## Limitations

The theorem is an **existence** construction, not a universal lower bound on numbers of idempotents. It does not classify all perfect evolution algebras with \(n\) idempotents, or rule out two idempotents in higher dimension. Characteristic \(2\) is excluded. It counts geometric points, not the lengths of local idempotent schemes; the repeated-root phenomenon produces nonreduced fibers. No independent mathematical audit is claimed.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, 2026-10-15, https://arxiv.org/abs/2610.22248, especially Section 2.3, Conjecture 6.
2. A. García-Martínez and Y. Pérez-Rodríguez, *A note on complete evolution algebras*, Archiv der Mathematik (2026), https://doi.org/10.1007/s00013-026-02251-0, Section 3.3.
3. X.-Y. Hu, *Full-Support Solutions and Rigidity for Three-Dimensional Evolution Algebras*, Preprints.org 202610.1039v2 (2026-10-15), https://www.preprints.org/manuscript/202610.1039, Introduction and Corollary 3.
