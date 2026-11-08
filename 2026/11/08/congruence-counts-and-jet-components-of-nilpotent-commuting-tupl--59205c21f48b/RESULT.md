# Congruence counts and jet components of nilpotent commuting tuples in \(\mathfrak{sl}_2\)

## Finding
Let \(k=\mathbb F_q\) be any finite field of **odd characteristic**, let \(r\geq2\), and put \(R_m=k[t]/(t^m)\) for \(m\geq1\). Write
\[
\mathcal C_r(R_m)=\{(X_1,\ldots,X_r)\in\mathfrak{sl}_2(R_m)^r:\ X_i^2=0,\ [X_i,X_j]=0\ \text{for all }i,j\}.
\]
These are equations over the *ring*, not merely after reduction to the residue field. Set \(C_m=|\mathcal C_r(R_m)|\) and \(C_0=1\) as a formal initial convention. The **complete congruence-count generating series** is
\[
\boxed{\sum_{m\geq0}C_mT^m=\frac{(1-qT)(1+q^rT)}{(1-q^{r+1}T)(1-q^{3r}T^2)}.}
\]
Equivalently, with \(B=(q+1)(q^r-1)\),
\[
\boxed{C_m=q^{3r\lfloor m/2\rfloor}+B\sum_{j=0}^{\lfloor(m-1)/2\rfloor}q^{3rj+(m-2j-1)(r+1)}\quad(m\geq1).}
\]
For the **quadratic equation scheme** \(\mathcal C_r\subseteq\mathbb A_k^{3r}\) defined by these same conditions, when \(r\geq3\), the underlying reduced jet scheme of length \(m\) has exactly \(\lfloor m/2\rfloor+1\) irreducible components, with dimensions
\[
\boxed{(r+1)m+j(r-2),\qquad 0\leq j\leq\lfloor m/2\rfloor.}
\]
Here a length-\(m\) jet means a \(k[t]/(t^m)\)-point, corresponding to a conventional jet of order \(m-1\). In particular, for \(r\geq3\) and \(m\geq2\) the jet scheme is non-equidimensional, and the maximum dimension is \((r+1)m+\lfloor m/2\rfloor(r-2)\). The linear growth exponent of the counts as \(m\to\infty\) jumps at \(r=2\): for fixed \(q\), \(C_m=\Theta(mq^{3m})\) if \(r=2\), and \(C_m=\Theta(q^{3rm/2})\) if \(r\geq3\), with constants permitted to depend on parity of \(m\).

## Assumptions and scope
The field size \(q\) ranges over all odd prime powers; no assumption that \(q\) is prime is needed. The tuple length \(r\) is any integer at least two, and the truncation length \(m\) is any positive integer. The ring \(R_m\) is commutative with identity. The square-zero condition is imposed on each actual matrix over \(R_m\), not on its residue. The geometric component statement concerns the scheme cut out by the specified quadratic equations and the irreducible components of its underlying topological space; no claim of reducedness of its full jet scheme is made.

Write each traceless matrix as
\[
X_i=\begin{pmatrix}a_i&b_i\\c_i&-a_i\end{pmatrix}.
\]
Then \(X_i^2=0\) is the single equation \(a_i^2+b_ic_i=0\). Since 2 is invertible, the bracket equations say exactly that all two-by-two minors of the three-by-\(r\) matrix with columns \((a_i,b_i,c_i)^{\mathsf T}\) vanish.

## Proof
**1. The nonzero residue locus.** Over \(k\), the nonzero solutions to \(a^2+bc=0\) number \(q^2-1\). Their projectivization is the smooth split conic with \(q+1\) points: the affine cone has \(q^2\) points, since for every \(b\ne0\) there are \(q\) choices of \(a\) and one of \(c\), and for \(b=0\) there are \(q\) choices with \(a=0\). Commutation of traceless matrices in odd characteristic is equivalent to proportionality of their coordinate triples. Hence every nonzero residue tuple is a tuple of scalar multiples of a nonzero vector on one of the \(q+1\) isotropic projective lines. Its count is
\[
B=(q+1)(q^r-1).
\]

**2. Smooth primitive lifting.** If the reduction of a tuple modulo \(t\) is nonzero, select a matrix \(X_i\) with nonzero reduction. From \(a_i^2+b_ic_i=0\), at least one of \(b_i,c_i\) is a unit. The commutator equations, using that unit, force every \(X_j\) to be a unique scalar multiple \(u_jX_i\) in \(R_m\). All remaining square-zero equations then follow from \(X_i^2=0\). This is a scheme-theoretic chart: a primitive traceless square-zero matrix has two smooth parameters, since the derivative of \(a^2+bc\) has a unit coordinate, and each of the \(r-1\) remaining matrices supplies one free scalar. Consequently the nonzero-residue locus is smooth of dimension \(r+1\), with exactly \(q^{(m-1)(r+1)}\) lifts of each nonzero residue tuple. Thus it contributes \(Bq^{(m-1)(r+1)}\) points at length \(m\).

**3. The zero residue locus.** For \(m\geq2\), if all matrices reduce to zero, uniquely write \(X_i=tY_i\) where each \(Y_i\) is specified modulo \(t^{m-1}\). Every defining equation is homogeneous quadratic, so the original equations modulo \(t^m\) are equivalent to the identical equations for the \(Y_i\) modulo \(t^{m-2}\). The remaining highest coefficient in each of the \(3r\) coordinates is free. Therefore the zero-residue locus has exactly \(q^{3r}C_{m-2}\) points. This decomposition is scheme-theoretically the product of the length-\((m-2)\) jet scheme with affine \(3r\)-space. Combined with steps 1 and 2, it gives, for every \(m\geq2\),
\[
C_m=Bq^{(m-1)(r+1)}+q^{3r}C_{m-2},\qquad C_0=1,\quad C_1=1+B.
\]
Solving this recurrence gives the stated finite sum. Multiplying the ordinary generating function by \(1-q^{3r}T^2\), and substituting the geometric series for its inhomogeneous term, yields the stated rational function. Algebraically its numerator simplifies to \((1-qT)(1+q^rT)\).

**4. Components.** On the reduced field-valued locus, the nonzero tuples are parameterized by the smooth split conic of nilpotent directions together with the projective direction of a nonzero scalar \(r\)-tuple, and a common scaling. Therefore its closure is the irreducible affine cone over the Segre–Veronese embedding of \(\mathbb P^1\times\mathbb P^{r-1}\) by \(\mathcal O(2,1)\), of dimension \(r+1\). Its only possible singular point is the origin; step 2 shows that every other point is smooth for the defining scheme. The length-\(m\) jets above the nonzero locus consequently form an irreducible open set of dimension \((r+1)m\), whose closure is one irreducible component.

The closed jets above the origin are, by step 3, the product of the length-\((m-2)\) jet scheme with affine \(3r\)-space. Inductively, for \(r\geq3\), a component at length \(m-2\) of dimension \((r+1)(m-2)+j(r-2)\) becomes a component in the origin fiber of dimension \((r+1)m+(j+1)(r-2)\). Since \(r-2>0\), all these dimensions exceed the dimension of the nonzero-residue component; thus none is contained in its closure. The origin fiber has no other components, and any component of the full jet scheme is either in that fiber or meets the nonzero open set. Starting at lengths zero (a point) and one (the irreducible cone), induction proves the complete list \(0\le j\le\lfloor m/2\rfloor\). In particular every length \(m\ge2\) has components of different dimensions when \(r\ge3\).

**5. Growth distinction.** In the displayed finite sum, the ratio of successive \(j\)-summands is \(q^{r-2}\). For \(r=2\) it is one and there are \(\lfloor(m+1)/2\rfloor\) summands, giving \(\Theta(mq^{3m})\). For \(r\ge3\) it exceeds one, so the last summand dominates up to a bounded geometric factor. This gives \(\Theta(q^{3rm/2})\), with the separate terminal term of no larger order. These are asymptotics in truncation length at fixed field size and tuple length.

## Verification
The standalone scripts `verify_arithmetic.py`, `verify_gf9.py`, and `verify_geometry.py` require only Python 3 standard libraries. Execute each as `python3 verify_arithmetic.py`, `python3 verify_gf9.py`, and `python3 verify_geometry.py`. The first directly enumerates all traceless square-zero matrices and all pairwise commuting pairs/triples over prime fields at several truncation lengths, comparing actual counts with the recurrence and finite sum. The second repeats the base-field tests over \(\mathbb F_9\), represented as \(\mathbb F_3[\alpha]/(\alpha^2+1)\), to test that prime fields are not essential. The third computes the exact Jacobian ranks of all field-valued tuple solutions over \(\mathbb F_3\) and \(\mathbb F_5\), checking that the nonzero locus has tangent dimension \(r+1\). The observed outputs are in `verification_output.txt`.

Selected exact counts: \(C_2=1593\), \(C_3=47385\) for \((q,r)=(3,2)\); \(C_2=28107\) for \((q,r)=(3,3)\); and \(C_2=33625\) for \((q,r)=(5,2)\). Finite computation corroborates but does not replace the all-length proof.

## Relationship to prior work
Premet studies the geometry and equidimensionality of nilpotent commuting **pairs** in reductive Lie algebras over algebraically closed fields. Yuen studies jet schemes of determinantal varieties and gives a general homogeneous-equation recursion for jets centered at the origin (Proposition 5.2), which is acknowledged here as the general mechanism behind step 3; her rank-one determinantal component theorems concern unconstrained matrices and do not give the present conic-constrained series or component dimensions. Moreau and Yu study jet schemes of **single** nilpotent orbit closures and their irreducibility, mostly in characteristic zero. Levy, Ngo, and Šivic treat higher nilpotent commuting varieties for larger matrix dimensions and geometric dimensions, not these finite-field truncated-ring point counts. The theorem also uses standard finite-field conic point counts and local smooth lifting. No claim is made that these general tools are new.

## Limitations
Only characteristic different from two is covered. The matrices are traceless two-by-two and satisfy \(X_i^2=0\) as actual ring equations; this is stricter than being nilpotent as a matrix over a nonreduced ring. The component classification is for \(r\geq3\); no component assertion for \(r=2\) is included. Neither the nilpotent structure of jet schemes nor their multiplicities are classified. The count uses equal-characteristic truncated rings \(k[t]/(t^m)\), not mixed-characteristic Witt rings. Historical priority remains provisional; a more general unpublished or unidentified jet-count theorem might contain the exact specialization. No independent mathematical audit has been performed.

## References
- A. Premet, *Nilpotent commuting varieties of reductive Lie algebras*, arXiv:math/0302204, first submitted 18 February 2003. https://arxiv.org/abs/math/0302204
- C. Yuen, *Jet schemes of determinantal varieties*, arXiv:math/0608632, first submitted 25 August 2006; especially Proposition 5.2 and Section 5. https://arxiv.org/abs/math/0608632
- A. Moreau and R. W. T. Yu, *Jet schemes of the closure of nilpotent orbits*, arXiv:1411.6427, first submitted 24 November 2014. https://arxiv.org/abs/1411.6427
- P. D. Levy, N. V. Ngo, and K. Šivic, *Commuting varieties and cohomological complexity theory*, Journal of the London Mathematical Society 106 (2022), 2847–2883. https://doi.org/10.1112/jlms.12650
