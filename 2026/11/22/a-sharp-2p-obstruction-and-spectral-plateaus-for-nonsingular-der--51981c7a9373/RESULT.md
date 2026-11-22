# A sharp \(2p\) obstruction and spectral plateaus for nonsingular derivations of free rank-two nilpotent Lie algebras

## Finding

Let \(q=p^f\) be a prime power, let \(c\ge 2\), and let \(L_{2,c}\) denote the free nilpotent Lie algebra of class \(c\) on two generators over \(\mathbb F_q\). A derivation is *nonsingular* if its underlying linear map is invertible. Put
\[
N_c=\sum_{n=1}^{c}\frac1n\sum_{d\mid n}\mu(d)2^{n/d}=\dim_{\mathbb F_q}L_{2,c}.
\]
For \(2\le c<2p\), define the finite set and parameters
\[
E_{c,p}=\{-j/i\in\mathbb F_p^\times: i,j\ge1,\ i+j\le c,\ p\nmid ij\},\quad e=|E_{c,p}|,\quad \delta=\mathbf1_{1\in E_{c,p}},\quad h=q-2-e+\delta.
\]
The division in the definition takes place in \(\mathbb F_p\), and \(\mathbb F_p\) is embedded in \(\mathbb F_q\). Let
\[
I(q)=\begin{cases}q^2(q-1)^2/2,&p=2,\\q(q-1)^3/2,&p\text{ odd}.\end{cases}
\]
Then the exact count of **labeled linear derivations** with invertible underlying map is
\[
\boxed{\#\operatorname{Der}(L_{2,c})^\times=
\begin{cases}
q^{2(N_c-2)}\left[I(q)+\dfrac{q(q+1)(q-1)h}{2}+(1-\delta)q^2(q-1)\right],&2\le c<2p,\\
0,&c\ge2p.
\end{cases}}
\]
Consequently a nonsingular derivation exists **if and only if** \(c<2p\). For all classes \(p\le c<2p\), the normalized nonsingular density is independent of \(c\): since \(E_{c,p}=\mathbb F_p^\times\), it is
\[
\frac1{q^4}\left[I(q)+\frac{q(q+1)(q-1)(q-p)}2\right].
\]
The density drops abruptly to zero at class \(2p\). For \(c<p\), the intermediate densities are controlled by the explicitly computable modular slope set \(E_{c,p}\).

## Assumptions and scope

The base field is an arbitrary finite field of order \(q=p^f\), including characteristic two. The Lie algebra is the ordinary (alternating-bracket, not restricted) free Lie algebra on two generators, quotient by all brackets of length greater than \(c\). The count concerns all ordinary derivations, not only semisimple, graded, inner, or skew-adjoint ones. The chosen free generators identify different linear maps; no automorphism-orbit quotient is taken. The Witt dimension formula above holds in all characteristics, using the integral Hall/Lyndon basis.

## Proof

**1. Reduction to the generator matrix.** The universal property of a free Lie algebra implies that any assignment of images to its two generators extends uniquely to a derivation, and the derivation descends to the length-\(c\) quotient. Its values on the generators can be selected independently in \(L_{2,c}\). Thus the derivation space has dimension \(2N_c\). Write the degree-one part of these images as a matrix \(A\in M_2(\mathbb F_q)\). Every choice of \(A\) has precisely \(q^{2(N_c-2)}\) lifts. Derivations preserve the lower central series. In a basis ordered by bracket length, the derivation is block triangular, and the diagonal block on degree \(n\) is the derivation induced by \(A\). Therefore its nonsingularity depends only on \(A\).

**2. All multidegrees occur.** Over an algebraic closure triangularize \(A\), with diagonal entries \(\lambda,\nu\). On a Lie monomial containing \(i\) copies of the first eigenvector and \(j\) copies of the second, the induced derivation has diagonal weight \(i\lambda+j\nu\). The one-generator weights \(\lambda,\nu\) also occur. For every \(i,j\ge1\), the two-letter word consisting of \(i\) first letters followed by \(j\) second letters is a Lyndon word. Its standard Lie bracketing belongs to the integral Lyndon basis, hence survives after reduction to any characteristic. Consequently **every** weight \(i\lambda+j\nu\) with \(i,j\ge1\) and \(i+j\le c\) occurs as an eigenvalue of the induced derivation. No other weights occur. Therefore the derived linear map is invertible exactly when
\[
\lambda\nu\ne0,\qquad i\lambda+j\nu\ne0\quad\text{for every }i,j\ge1\text{ with }i+j\le c.
\]
This conclusion does not assume that \(A\) is diagonalizable: triangularization and the degree filtration suffice.

**3. The sharp characteristic obstruction.** If \(c\ge2p\), the multidegree \((p,p)\) is present, and its weight is \(p\lambda+p\nu=0\). Every derivation is singular. Conversely, assume \(c<2p\). There is no pair of positive integers \(i,j\) within the range with both divisible by \(p\). An invertible \(A\) whose characteristic polynomial is irreducible over \(\mathbb F_q\) and whose trace is nonzero has nonzero weights: if some \(i\lambda+j\lambda^q=0\), then both residues \(i,j\) must be nonzero, and \(\lambda/\lambda^q\in\mathbb F_p^\times\). Raising this ratio to the \(q\)-th power makes it its reciprocal, forcing the ratio to equal \(\pm1\). The value \(+1\) contradicts irreducibility, while \(-1\) makes the trace zero (in characteristic two these two alternatives coincide). Such matrices exist for every finite field, as counted in Step 4. Hence a nonsingular derivation exists for every \(c<2p\).

**4. Exact finite-field count.** Classify the degree-one matrices by their characteristic polynomials. An irreducible monic quadratic gives a similarity class of size \(q(q-1)\). There are \((q^2-q)/2\) such polynomials. In odd characteristic, exactly \((q-1)/2\) of these have trace zero; in characteristic two, none does. The number of admissible irreducible matrices is therefore exactly \(I(q)\).

For split matrices with two distinct nonzero eigenvalues \(a,b\), all higher weights are nonzero precisely when the ratio \(a/b\) avoids \(E_{c,p}\). Excluding ratio \(1\) as well, the number of permitted ratios is \(h=q-2-e+\delta\). Each permitted unordered pair of eigenvalues is counted twice among the \((q-1)h\) ordered pairs, and each distinct-eigenvalue similarity class has size \(q(q+1)\). Hence this case contributes \(q(q+1)(q-1)h/2\).

Finally, a repeated nonzero eigenvalue \(a\) occurs in exactly \(q^2\) matrices with characteristic polynomial \((X-a)^2\), counting the scalar and nontrivial Jordan possibilities. These are admissible precisely when \(1\notin E_{c,p}\), contributing \((1-\delta)q^2(q-1)\). The three cases are disjoint and exhaustive. Multiplication by the lift count from Step 1 proves the formula.

**5. Plateau.** If \(p\le c<2p\), then for every nonzero residue \(r\in\mathbb F_p\), choose \(i=1\) and the unique \(1\le j\le p-1\) satisfying \(-j=r\). These pairs satisfy \(i+j\le p\le c\), hence \(E_{c,p}=\mathbb F_p^\times\). Therefore \(e=p-1\), \(\delta=1\), \(h=q-p\). Dividing by the total number \(q^{2N_c}\) of derivations gives the claimed class-independent density.

## Verification

The standalone file `verify_free_lie_spectrum.py` constructs integral Lyndon commutators inside the free associative tensor algebra, computes their induced derivation matrices over prime fields, and exhaustively compares actual determinants for *every* \(2\times2\) generator matrix against both a resultant criterion and the closed counting formula. Successful cases: \(q=2\) through class four, \(q=3\) through class six, \(q=5\) through class five, and \(q=7\) through class three. The independent arithmetic file `verify_extension_fields.py` enumerates the matrices over \(\mathbb F_4\) and \(\mathbb F_9\), including the characteristic thresholds and stabilization intervals. Run both with a standard Python 3 interpreter, without external libraries.

Representative admissible generator-matrix counts are \(2,2,0\) for \(q=2\) at classes two through four; \(30,12,12,12,0\) for \(q=3\) at classes two through six; \(380,260,260,160\) for \(q=5\) at classes two through five; and \(5112,4464,4464,4464,0\) for \(q=9\) at classes two through six. To obtain full derivation counts, multiply these numbers by \(q^{2(N_c-2)}\). The universal theorem is proved in Steps 1–5; finite checks are only independent tests.

## Relationship to prior work

Benito and Roldán-López's 2019 study supplies the general parametrization of derivations by generator images for free nilpotent Lie algebras, over characteristic zero. Benito, Rández-Ibáñez and Roldán-López's 2024 work develops computational derivation techniques for nilpotent quadratic Lie algebras, including the five-dimensional free rank-two, class-three example; its stated scope is characteristic zero and it emphasizes metric-skew derivations and double extensions. Benito, de-la-Concepción and Laliena's 2016/2017 work supplies the quadratic background for that example. Burde, Dekimpe and Verbeke (2019) treat *almost-inner* derivations, a different subspace. The class-two specialization is already covered by existing finite-field free-class-two derivation counts and is included here only as a boundary case of the uniform formula. None of the cited inspected treatments states the all-class positive-characteristic \(2p\) obstruction, the modular slope-set count, or the density plateau. The known general construction and classical Lyndon basis are used as established tools, not claimed as new. A more general published Lie-power or eigenvalue-avoidance enumeration could potentially subsume the claim; publication priority should therefore be checked independently.

## Limitations

The exact census is limited to two free generators and ordinary derivations of free nilpotent Lie algebras. It does not count similarity or automorphism-conjugacy classes, give individual determinant fibers, or apply automatically to quotient Lie algebras (where the multidegree \((p,p)\) may vanish). The first-source paper studies characteristic zero; the modular argument is established independently here. The finite test suites do not certify arbitrary fields or classes; the mathematical proof supplies the full quantification. Originality is judged relative to inspected sources, not as a guarantee of literature-wide priority. Independent validation has not been performed.

## References

1. P. Benito, J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897 (first posted 2019-11-05), https://arxiv.org/abs/1911.01897.
2. P. Benito, J. Rández-Ibáñez, J. Roldán-López, *Computing derivations on nilpotent quadratic Lie algebras*, arXiv:2401.14348 (first posted 2024-01-25), https://arxiv.org/abs/2401.14348.
3. P. Benito, D. de-la-Concepción, J. Laliena, *Free nilpotent and nilpotent quadratic Lie algebras*, arXiv:1604.02923 (first posted 2016-04-11), https://arxiv.org/abs/1604.02923.
4. D. Burde, K. Dekimpe, B. Verbeke, *Almost inner derivations of Lie algebras II*, arXiv:1905.08145 (first posted 2019-05-20), https://arxiv.org/abs/1905.08145.
