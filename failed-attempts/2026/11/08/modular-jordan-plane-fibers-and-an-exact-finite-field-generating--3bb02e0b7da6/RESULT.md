# Modular Jordan-plane fibers and an exact finite-field generating product

## Finding
Let \(q=p^f\) be any prime power, \(p\) its characteristic, and \(n\geq0\). Define
\[
R_{n,q}=\#\{(X,Y)\in M_n(\mathbb F_q)^2:XY-YX=Y^2\},\qquad G_n(q)=|\operatorname{GL}_n(\mathbb F_q)|,\quad G_0(q)=1.
\]
For a monic irreducible polynomial \(\phi\in\mathbb F_q[t]\), let \(\lambda_\phi\) be the partition of exponents of the \(\phi\)-primary cyclic summands of the \(\mathbb F_q[t]\)-module defined by \(Y\). There is a matrix \(X\) satisfying the equation **if and only if** every part of \(\lambda_\phi\) is divisible by \(p\) for each \(\phi\ne t\). The \(t\)-primary parts are unrestricted.

For every admissible \(Y\), the full solution set in \(X\) is an affine space over \(\mathbb F_q\) of dimension
\[
c(Y)=\sum_\phi (\deg\phi)\sum_{h\ge1}(\lambda'_{\phi,h})^2.
\]
The exact enumerator, as a formal power series in \(u\) with rational coefficients, is
\[
\boxed{\displaystyle
\sum_{n\ge0}\frac{R_{n,q}}{G_n(q)}u^n=
\left(\prod_{\substack{j\ge1\\p\nmid j}}\prod_{h\ge0}\frac{1}{1-u^j q^{-h}}\right)
\left(\prod_{j\ge1}\prod_{h\ge0}\frac{1}{1-u^{pj}q^{1-h}}\right).}
\]
For \(n<p\) every admissible \(Y\) is nilpotent. At the first possible nonnilpotent dimension \(n=p\), the number of pairs with nonnilpotent \(Y\) is exactly \(qG_p(q)\). The existence of nonnilpotent solutions and a closely related matrix-commutator solvability criterion were previously known. The arithmetic contribution assessed here is the all-dimensional generating product for labeled representations, with the modular criterion supplied as its necessary structural input.

## Assumptions and scope
All matrices are labeled, not counted up to similarity. Every field is \(\mathbb F_q\) with \(q=p^f\); both \(p=2\) and odd characteristic are included. Write \(\phi=t\) for the unique irreducible with zero constant term. The conjugate partition \(\lambda'_\phi\) counts columns of the Young diagram of \(\lambda_\phi\). The zero-dimensional convention is one empty matrix pair. Infinite products are coefficientwise well defined: for each coefficient of \(u^n\), only factors with \(j\le n\) contribute, and sums over \(h\) converge as rational geometric series for fixed integer \(q>1\).

## Proof
**1. Necessity of the block condition.** Extend the base field to an algebraic closure and put \(Y\) in Jordan form. Restrict the equation to a diagonal block of dimension \(e\) with eigenvalue \(a\). Its trace gives
\[
0=\operatorname{tr}([X_{ii},J_e(a)])=\operatorname{tr}(J_e(a)^2)=e a^2.
\]
Thus \(a\ne0\) implies \(p\mid e\). Every irreducible polynomial over a finite field is separable; a \(\phi^e\)-primary rational block becomes \(\deg\phi\) blocks of length \(e\) over the algebraic closure. Hence every exponent for \(\phi\ne t\) is divisible by \(p\).

**2. Sufficiency and affine fibers.** On \(\mathbb F_q[t]\), consider the derivation \(\delta=t^2\,d/dt\). On the cyclic module \(\mathbb F_q[t]/(\phi^e)\) it descends precisely when the ideal \((\phi^e)\) is \(\delta\)-stable. Since
\[
\delta(\phi^e)=e\,t^2\phi^{e-1}\phi',
\]
this is automatic when \(\phi=t\), and also when \(p\mid e\). By the block criterion it therefore descends on every direct summand of the module of \(Y\). Direct sum of the induced linear maps defines \(X_0\) with
\[
[X_0,Y]=Y^2,
\]
because \([\delta,m_t]=m_{t^2}\). Any other solution is \(X_0+Z\) for a unique \(Z\) commuting with \(Y\). Standard homomorphism counting between \(\mathbb F_q[t]\)-cyclic modules yields
\[
\dim_{\mathbb F_q}\operatorname{End}_{\mathbb F_q[t]}(\mathbb F_q^n)
=\sum_\phi(\deg\phi)\sum_{a,b}\min(\lambda_{\phi,a},\lambda_{\phi,b})
=c(Y).
\]
This proves the criterion and the fiber dimension, including zero blocks and mixed irreducible factors.

**3. Weighted rational-canonical enumeration.** Let \(m_j(\lambda_\phi)\) be the multiplicity of a part of size \(j\). The group of invertible elements in the module centralizer has size
\[
|C_{\operatorname{GL}_n(q)}(Y)|=
q^{c(Y)}\prod_\phi\prod_{j\ge1}\prod_{a=1}^{m_j(\lambda_\phi)}(1-q^{-a\deg\phi}).
\]
For each admissible conjugacy class, the number of labeled choices of \(Y\) is \(G_n(q)/|C_{\operatorname{GL}_n(q)}(Y)|\), and each choice admits \(q^{c(Y)}\) matrices \(X\). Thus the class weight in \(R_{n,q}/G_n(q)\) is the reciprocal of the finite product in the last display.

For \(Q=q^{-d}\), the elementary Euler identity gives
\[
\sum_{m\ge0}\frac{z^m}{\prod_{a=1}^m(1-Q^a)}
=\prod_{h\ge0}(1-zQ^h)^{-1}.
\]
For \(j\) not divisible by \(p\), only the primary factor \(\phi=t\) may have parts of size \(j\), giving \(\prod_{h\ge0}(1-u^j q^{-h})^{-1}\).
For sizes \(pj\), all irreducibles are allowed. The unique-factorization identity
\[
\prod_{\phi\text{ monic irreducible}}\bigl(1-z^{\deg\phi}\bigr)^{-1}=(1-qz)^{-1}
\]
turns their product, at \(z=u^{pj}q^{-h}\), into \((1-u^{pj}q^{1-h})^{-1}\). Multiplication over positive \(j\) proves the stated product. This step uses the full centralizer *unit-group* order, not merely the dimension of the commuting algebra.

**4. Sharp first nonnilpotent contribution.** If \(Y\) has any nonzero eigenvalue, the criterion forces a primary block of dimension at least \(p\). At \(n=p\), any nonnilpotent admissible \(Y\) is one Jordan block of size \(p\) with eigenvalue \(a\in\mathbb F_q^\times\). For each such \(a\), the centralizer units number \((q-1)q^{p-1}\) and the affine solution fiber has size \(q^p\). Therefore the total is
\[
(q-1)\frac{G_p(q)}{(q-1)q^{p-1}}q^p=qG_p(q).
\]
This also establishes the threshold statement.

## Verification
A standard-library checker directly forms all matrices \(Y\) over small prime fields, constructs \(\operatorname{ad}_Y\), performs modular elimination on the original equation, and sums the actual affine solution-fiber sizes. The checker separately extracts coefficients of the proposed generating product with exact rational arithmetic. For \(\mathbb F_4\) in dimension two it directly tests all ordered pairs using an explicit degree-two field polynomial. Prime-field tests cover dimensions up to three in characteristics two and three, and up to two in characteristic five; these tests are finite corroboration, not a substitute for the proof. Run \(\texttt{python3 artifacts/check_jordan_plane.py}\) from the package root; its expected output is stored in \(\texttt{artifacts/check_results.txt}\).

## Relationship to prior work
Iyudu's 2012 Jordan-plane representation-space theorem explicitly works over \(\mathbb C\); its characteristic-zero nilpotence and geometric stratification do not give the admissibility criterion for nonzero modular eigenvalues or the finite-field counting product. Its observation that a nonempty fixed-\(Y\) fiber is a centralizer translate is credited. Shirikov (2007) studies the Jordan plane in positive characteristic but emphasizes prime ideals, its primary spectrum, and automorphisms. Bourgeois (2014), Remark 6, already exhibits a nonnilpotent characteristic-three solution to a commutator-square equation. More strongly, Feinberg (1979) proves that \(I=[A,B]\) can be solved in characteristic \(p\) precisely when every Jordan block of \(A\) has size divisible by \(p\). On each invertible primary part of \(Y\), the present equation is equivalent to \([Y^{-2}X,Y]=I\). Thus the nonzero-eigenvalue criterion is a consequence of Feinberg, not an independently original theorem; its direct derivation is retained for self-containment. Classical Feit–Fine counts enumerate commuting matrix pairs, not the solvability-restricted Jordan-plane equation; their rational-canonical weighting is a methodological predecessor. The proposed original contribution is the explicit characteristic-dependent generating product for all labeled Jordan-plane representations, not the prior solvability theorem, existence examples, rational canonical form, or Euler methodology.

## Limitations
The theorem counts labeled \(\mathbb F_q\)-representations, not simultaneous-conjugacy classes, irreducible geometric components, scheme singularities, or indecomposable modules. The count is an identity of rational-coefficient formal series for each fixed finite field; it does not assert a universal polynomial in \(q\) when \(p\) varies. The source comparison cannot rule out an unlocated older enumeration in the broader literature of Ore extensions or centralizer-weighted representation counts. No independent mathematical audit has been carried out.

## References
1. N. K. Iyudu, *Representation spaces of the Jordan plane*, arXiv:1209.0746v1 (first public version September 4, 2012), https://arxiv.org/html/1209.0746v1. Primary MSC 16G30.
2. E. N. Shirikov, *The Jordan Plane over a Field of Positive Characteristic*, Mat. Zametki **82** (2007), 272–292, https://doi.org/10.4213/mzm3796.
3. G. Bourgeois, *The Matrix Equation \(XA-AX=X^{\alpha}g(X)\) over Fields or Rings*, Algebra (2014), article 745029, https://doi.org/10.1155/2014/745029, especially Remark 6.
4. R. B. Feinberg, *The Identity as a Matrix Commutator*, Linear and Multilinear Algebra **7** (1979), 121–122, https://doi.org/10.1080/03081087908817267.
5. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499v1 (November 16, 2016), https://arxiv.org/abs/1611.05499. Used only for methodological comparison with the classical Feit–Fine identity.
