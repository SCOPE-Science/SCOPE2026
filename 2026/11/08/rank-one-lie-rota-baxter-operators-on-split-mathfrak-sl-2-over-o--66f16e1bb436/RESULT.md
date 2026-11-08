# Rank-one Lie Rota–Baxter operators on split \(\mathfrak{sl}_2\) over odd finite fields

## Finding
Let \(k=\mathbb F_q\) be any finite field of odd order, and set \(\mathfrak g=\mathfrak{sl}_2(k)\). Let \(\mathcal R_1(k)\) denote the set of **nonzero rank-one** \(k\)-linear operators \(R:\mathfrak g\to\mathfrak g\) obeying the weight-zero Lie Rota–Baxter identity
\[
 [R(x),R(y)]=R([R(x),y]+[x,R(y)])\quad(x,y\in\mathfrak g).
\]
Writing \(B(x,y)=\operatorname{tr}(xy)\), each rank-one operator uniquely determines two projective lines and can be represented as \(R(x)=B(b,x)a\), with \(a,b\ne0\) and simultaneous rescaling \((a,b)\mapsto(ta,t^{-1}b)\). It lies in \(\mathcal R_1(k)\) if and only if \([a,b]\in kb\).

There are exactly two intrinsically defined families:

* The **self-adjoint family** \(\mathcal C\), characterized by \([a,b]=0\), equivalently \(b\in ka\) and \(B(Rx,y)=B(x,Ry)\).
* The **square-zero family** \(\mathcal N\), characterized by \(R^2=0\), equivalently \(B(b,b)=0\) and \([a,b]\in kb\). This is the family of operators parametrized by a nonzero nilpotent line \(kb\) and a nonzero vector \(a\) in the two-dimensional normalizer of that line.

Their sizes and overlap are exactly
\[
 |\mathcal C|=q^3-1,\qquad
 |\mathcal N|=(q+1)(q^2-1),\qquad
 |\mathcal C\cap\mathcal N|=q^2-1.
\]
Consequently,
\[
 \boxed{|\mathcal R_1(k)|=2q^3-q-1.}
\]
There are exactly \(q^2\) rank-one idempotent solutions \(R^2=R\), and exactly \(q^2(q-1)\) solutions with \(R^2\ne0\). Every latter solution is a nonzero scalar multiple of a unique rank-one idempotent.

Over an algebraic closure of any characteristic-not-two field, the **reduced rank-at-most-one** solution variety, including the zero operator, has precisely two irreducible components of dimension three: the cones over the self-adjoint and square-zero projective families. They intersect in an irreducible two-dimensional cone (including zero) of self-adjoint square-zero operators. The finite-field counts above refer to labeled linear maps, not conjugacy orbits.

## Assumptions and scope
The characteristic is different from two, and for the point counts the field is \(\mathbb F_q\) with \(q\) odd (including odd prime powers). No restrictions on rank-two or rank-three operators are asserted. The trace pairing \(B\) is nondegenerate on \(\mathfrak{sl}_2(k)\) in this characteristic. A nilpotent element \(b\in\mathfrak g\) means \(b^2=0\), or equivalently \(B(b,b)=0\) for traceless two-by-two matrices. The normalizer of the line \(kb\) is \(\mathfrak n(kb)=\{a\in\mathfrak g:[a,b]\in kb\}\).

## Proof
**Step 1: reduce the operator equation.** The pairing \(B\) identifies \(\mathfrak g^*\) with \(\mathfrak g\). Every nonzero rank-one operator is \(R(x)=B(b,x)a\), with \(a,b\ne0\), unique up to \((a,b)\mapsto(ta,t^{-1}b)\). Its image is abelian, so the left side of the Rota–Baxter identity vanishes. The right side is
\[
 a\{B(b,x)B(b,[a,y])-B(b,y)B(b,[a,x])\}.
\]
The displayed alternating expression vanishes for every \(x,y\) precisely when the functionals \(B(b,-)\) and \(B(b,[a,-])\) are linearly dependent. Invariance and nondegeneracy of \(B\) identify the latter condition with \([a,b]\in kb\). This proves necessity and sufficiency in every characteristic different from two.

**Step 2: distinguish the two types.** For a nonzero traceless \(2\times2\) matrix \(b\), its centralizer in \(M_2(k)\) is \(kI+kb\). The trace-zero condition, since \(2\ne0\), gives \(\mathfrak z_{\mathfrak g}(b)=kb\). Thus, if \([a,b]=0\), then \(a\) and \(b\) are proportional. Suppose instead \([a,b]=\lambda b\) with \(\lambda\ne0\). Invariance gives \(\lambda B(b,b)=B([a,b],b)=B(a,[b,b])=0\), so \(B(b,b)=0\) and \(b\) is nilpotent. Conversely, if \(b\ne0\) is nilpotent and \(a\in\mathfrak n(kb)\), the criterion of Step 1 holds. A nonzero nilpotent element is conjugate over an algebraic closure to a nonzero multiple of \(e=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)\). Its line normalizer is the trace-zero upper-triangular Borel, which is two-dimensional; this also holds for rational nilpotent lines over finite fields.

**Step 3: distinguish square-zero from scalar projections.** Directly, \(R^2=B(a,b)R\). If \(b\) is nilpotent and \(a\in\mathfrak n(kb)\), the upper-triangular normal form shows \(B(a,b)=0\), so \(R^2=0\). If \(b=ta\) and \(a\) is not nilpotent, then \(B(a,b)=tB(a,a)\ne0\), so \(R^2\ne0\). If \(a\) is nilpotent, proportionality gives both the self-adjoint and square-zero conditions. Hence \(\mathcal N\) is exactly the square-zero part, \(\mathcal C\) is the self-adjoint part, and their intersection is the self-adjoint square-zero part. For every \(R\notin\mathcal N\), the unique scalar \(\lambda=B(a,b)\) is nonzero and \(P=\lambda^{-1}R\) is the unique associated nonzero rank-one idempotent.

**Step 4: finite-field populations.** The lines of \(\mathfrak g\) are the \(q^2+q+1\) points of \(\mathbb P^2(\mathbb F_q)\). For each such line, the nonzero self-adjoint rank-one maps with that image are a one-dimensional punctured vector space of size \(q-1\). Thus \(|\mathcal C|=(q^2+q+1)(q-1)=q^3-1\). The nilpotent projective lines form the nonsingular conic \(\det b=0\), having exactly \(q+1\) rational points. For each such line \(kb\), the allowed tensors \(a\otimes B(b,-)\), as \(a\) runs through its two-dimensional normalizer, are unique and give \(q^2-1\) nonzero maps. Distinct lines \(kb\) yield distinct functionals up to scalar, so \(|\mathcal N|=(q+1)(q^2-1)\). Intersecting with \(\mathcal C\) forces \(a\in kb\), yielding \((q+1)(q-1)=q^2-1\) maps. Inclusion–exclusion proves the total count. Exactly \(q^2\) projective lines are non-nilpotent; every one has a unique self-adjoint rank-one map with \(B(a,b)=1\), proving the idempotent count and the \(q^2(q-1)\) non-square-zero count.

**Step 5: reduced geometry.** Within projective rank-one tensors \(\mathbb P(\mathfrak g)\times\mathbb P(\mathfrak g^*)\), the self-adjoint solutions are the Veronese image of \(\mathbb P(\mathfrak g)\cong\mathbb P^2\), a closed irreducible surface. For the square-zero part, the functional line \(kb\) ranges over the smooth nilpotent conic \(C\cong\mathbb P^1\), while the image line is in the rank-two vector bundle whose fiber is \(\mathfrak n(kb)\). Its projectivization is an irreducible projective surface, mapping injectively onto its image because the functional line is recoverable from the rank-one tensor. Its image is closed (properness). The projective components intersect exactly when \(ka=kb\) is a nilpotent line, i.e. along the Veronese image of \(C\). Passing to affine cones and adjoining zero raises dimensions by one, yielding two irreducible three-dimensional cones and their irreducible two-dimensional intersection. As stated, this is a claim about the reduced underlying varieties, not their possibly nonreduced schemes.

## Verification
The accompanying standalone programs `verify_prime_fields.py` and `verify_gf9.py` construct the original \(\mathfrak{sl}_2\) bracket and trace form. They enumerate **all ordered nonzero factorizations** \((a,b)\) over \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_9\), evaluate the unmodified Rota–Baxter identity on all three unordered basis pairs, compare with both structural families, and divide counts by the known factor \(q-1\) (there is no double counting after this quotient).

The output in `direct_checks.txt` records, in order, for \(q=3,5,7,9\), the numbers of rank-one solutions \(50,244,678,1448\), the square-zero counts \(32,144,384,800\), and the rank-one idempotent counts \(9,25,49,81\). All tests passed. This finite verification supports but does not prove the statements for all fields; Steps 1–5 supply that proof. To replay with Python 3, run the two programs separately from the directory containing them.

## Relationship to prior work
Pei, Bai and Guo (arXiv:1311.0612v1, posted 2013-11-04) classify **all** weight-zero Rota–Baxter operators on the complex Lie algebra \(\mathfrak{sl}_2(\mathbb C)\), up to scalar multiplication, by explicit matrices. Their complex classification is stronger for the full complex operator problem, and the complex rank-one special case is **not** claimed new here. The present statement instead makes the rational characteristic-not-two two-component description explicit and determines the complete rank-one finite-field population, the square-zero/idempotent split, and the two component counts in every odd prime power. A classification over the complex numbers does not itself count rational points or establish formulas in positive characteristic, particularly characteristic three.

Gubarev and Kozlov (2023) treat Rota–Baxter operators on the **complex Lie conformal algebra** associated with \(\mathfrak{sl}_2\); that is a different ambient operator problem. Gubarev (arXiv:1811.08219) counts Rota–Baxter operators on finite direct products of fields, not on this Lie algebra. Broader unseen results on Lie Rota–Baxter varieties or rational tensor orbits could imply some of the stated arithmetic conclusions; historical priority remains subject to independent verification.

## Limitations
This is the nonzero rank-one stratum and its closure only. No census of rank-two or rank-three Rota–Baxter operators is asserted; the full Rota–Baxter scheme is not analyzed. The geometric conclusions concern reduced varieties and do not claim scheme-theoretic reducedness or smoothness. No automorphism-orbit census is asserted. The named finite-field computations do not substitute for the characteristic-independent proof. Historical-priority verification and independent mathematical validation have not been performed.

## References
1. J. Pei, C. Bai and L. Guo, *Rota-Baxter operators on sl(2,C) and solutions of the classical Yang-Baxter equation*, arXiv:1311.0612v1 (2013-11-04), https://arxiv.org/abs/1311.0612 . Theorem 2.1, Section 2, and conclusions.
2. V. Gubarev and R. Kozlov, *Rota-baxter operators on Cur(sl2(C))*, International Electronic Journal of Algebra 33 (2023), 247–269, https://doi.org/10.24330/ieja.1218727 . Different (conformal) algebra.
3. V. Gubarev, *Rota-Baxter operators on a sum of fields*, arXiv:1811.08219 (2018-11-20), https://arxiv.org/abs/1811.08219 . Different (associative semisimple) algebra.
