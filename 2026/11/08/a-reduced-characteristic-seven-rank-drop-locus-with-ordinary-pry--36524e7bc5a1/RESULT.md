# A reduced characteristic-seven rank-drop locus with ordinary Prym in a cyclic trigonal genus-four family

## Finding

Let \(k=\overline{\mathbb F}_7\). For \(t\in k\) satisfying \(t^2\ne 4\), write \(C_t\) for the smooth projective curve with function field
\[
k(C_t)=k(x,y),\qquad y^3=x^5+t x^3+x.
\]
The curve has genus four, and the involution \(\iota:(x,y)\mapsto(-x,-y)\) has a genus-two quotient \(D_t\), birationally given by
\[
D_t:\quad w^2=(v^3-t)^2-4.
\]
The Prym surface \(P_t=\ker(\operatorname{Nm}:J(C_t)\to J(D_t))^0\) is ordinary for **every** smooth parameter. The full arithmetic stratification is
\[
(f_7(C_t),a(C_t))=\begin{cases}(4,0)&t^2\ne-2,\\(2,2)&t^2=-2.\end{cases}
\]
At either exceptional parameter the quotient \(D_t\) is superspecial (its Cartier operator is zero); otherwise \(D_t\) is ordinary. The Cartier-rank-at-most-two determinantal subscheme is reduced and consists of two geometric points; by contrast the rank-at-most-three determinantal scheme is the doubled Hasse divisor. These two points determine one geometric isomorphism class of the original genus-four curves. In the displayed parameter coordinate the full Cartier Hasse determinant is \(2(t^2+2)^2(t^2+3)^2\), so its zero divisor on the smooth parameter line is twice the reduced exceptional divisor.

## Assumptions and scope

Throughout, the characteristic is seven, \(k\) is algebraically closed, and all nonzero \(t^2-4\) are allowed. The \(7\)-rank of a smooth projective curve means the \(7\)-rank of its Jacobian; the Cartier \(a\)-number is the dimension of the kernel of Cartier on regular differentials. A superspecial abelian surface has \(a=2\). The coefficient-parameter and scheme-theoretic assertions are made relative to \(\operatorname{Spec}k[t,(t^2-4)^{-1}]\); they do not assert that all parameter values give pairwise nonisomorphic curves. The Hasse divisor refers to the determinant in the displayed differential trivialization, whose order of vanishing is unaffected by invertible changes of trivialization.

## Proof

**Smoothness and genus.** Set \(F_t(x)=x(x^4+t x^2+1)\). Direct resultant evaluation gives
\[
\operatorname{disc}_x(F_t)=16(t^2-4)^2\quad\text{in }\mathbb F_7[t].
\]
Hence the five finite branch points are simple exactly when \(t^2\ne4\). Since the pole at infinity has order five, relatively prime to three, the cubic Kummer cover is smooth after projective normalization and ramified above all six points, giving \(2g-2=3(-2)+6(3-1)=6\), so \(g=4\).

**Involution and quotient.** Under \(\iota\), the ratios \(v=y/x\) and \(u=x^2\) are invariant. The defining equation gives \(v^3=u+t+u^{-1}\). Put \(w=u-u^{-1}\). Then \(w^2=(v^3-t)^2-4\), and \(u=(v^3-t+w)/2\); consequently \(k(C_t)^{\langle\iota\rangle}=k(v,w)\). The polynomial \((v^3-t)^2-4=(v^3-t-2)(v^3-t+2)\) has six distinct roots for \(t\ne\pm2\), giving genus \(2\) for the smooth quotient.

**Cartier matrix.** At the unique point over infinity, \(\operatorname{ord}(x)=-3\), \(\operatorname{ord}(y)=-5\), and \(\operatorname{ord}(dx)=-4\). Thus the four regular differential forms
\[
\omega_0=dx/y,\quad\omega_1=dx/y^2,\quad\omega_2=x\,dx/y^2,\quad\omega_3=x^2\,dx/y^2
\]
are holomorphic (the finite branch points are also regular); their number equals the genus, so they are a basis. For a power series in characteristic seven, Cartier sends \(\sum a_nx^n dx\) to \(\sum a_{7m+6}^{1/7}x^m dx\). Using \(y^{-1}=y^{-7}F_t^2\) and \(y^{-2}=y^{-14}F_t^4\), coefficient extraction shows that the Cartier operator, displayed as inverse-Frobenius roots of the coefficients, has the block matrix
\[
\left(\begin{array}{c|ccc}
t^2+2&0&0&0\\\hline
0&4t&0&1\\0&0&(t^2+2)(t^2+3)&0\\0&1&0&4t
\end{array}\right).
\]
The matrix entries in the operator are their seventh roots; all rank and zero assertions can be checked on the displayed coefficient matrix. More precisely, because the matrix is symmetric under interchange of \(\omega_1,\omega_3\) and the basis transformation is defined over \(\mathbb F_7\), this coefficient matrix splits over the constant basis
\[
\omega_0,\quad\omega_2,\quad\omega_1+\omega_3,\quad\omega_1-\omega_3
\]
into diagonal entries
\[
t^2+2,\quad(t^2+2)(t^2+3),\quad4t+1,\quad4t-1.
\]
For a diagonal inverse-Frobenius-semilinear operator the stable image dimension is the number of nonzero diagonal entries, and its kernel dimension is their number of zeros. In \(\mathbb F_7[t]\),
\[
(4t+1)(4t-1)=2(t^2+3),
\]
and \(t^2+3=t^2-4\) is a unit on the smooth parameter line. Therefore the last two diagonal entries are always nonzero; the first two vanish precisely and simultaneously when \(t^2+2=0\). This proves the \(7\)-rank and \(a\)-number formulas and the absence of any intermediate stratum.

**Prym and genus-two check.** The involution fixes \(\omega_0\) and \(\omega_2\), and negates \(\omega_1,\omega_3\). Hence its invariant subspace, corresponding to \(H^0(D_t,\Omega^1)\), carries the diagonal coefficients \(t^2+2\) and \((t^2+2)(t^2+3)\); the anti-invariant subspace carries the everywhere-nonzero coefficients \(4t\pm1\). Because two is invertible in characteristic seven, pullback and norm induce a prime-to-seven isogeny \(J(C_t)\sim J(D_t)\times P_t\); its prime-to-seven nature (or, equivalently, the decomposition of the \(7\)-divisible group under the idempotents \((1\pm\iota)/2\)) makes the stable ranks and Cartier-kernel dimensions additive. Therefore \(P_t\) is ordinary. Independently, for the genus-two quotient polynomial \(G_t(v)=(v^3-t)^2-4\), the hyperelliptic Hasse–Witt coefficient extraction from \(G_t(v)^3\) gives
\[
\begin{pmatrix}(t^2+2)(t^2+3)&0\\0&t^2+2\end{pmatrix}.
\]
It vanishes precisely at \(t^2=-2\), confirming the superspecial genus-two quotient.

**Scheme and isomorphism.** Let \(u=t^2+2\), \(v=t^2+3\), \(a=4t+1\), and \(b=4t-1\). Both \(v\) and \(ab=2v\) are units on the smooth parameter line. The \(3\)-minors of the diagonal Cartier coefficient matrix \(\operatorname{diag}(u,uv,a,b)\) include \(uab\) (omit the second diagonal entry), and all of them are divisible by \(u\); hence the ideal of its rank-at-most-two determinantal locus is exactly \((u)=(t^2+2)\). The rank-at-most-three locus is instead defined by its single determinant \(2u^2v^2\), a nonreduced doubled divisor. Because the derivative of \(t^2+2\) is \(2t\) and no root is zero, that ideal is radical and gives two reduced geometric points. The determinant is
\[
(t^2+2)^2(t^2+3)(4t-1)(4t+1)=2(t^2+2)^2(t^2+3)^2,
\]
with double zeros at those points. Finally, choose \(i\in k\) with \(i^2=-1\) and \(\beta\in k\) with \(\beta^3=i\). The transformation \((x,y)\mapsto(ix,\beta y)\) identifies \(C_{-t}\) with \(C_t\). The two roots of \(t^2=-2\) are negatives, hence give one geometric isomorphism class. The theorem does not classify all possible isomorphisms among ordinary members.

## Verification

Run `python3 verify_cartier.py` and `python3 verify_quotient.py` in the same directory, with SymPy installed. The first independently checks the defining discriminant, the four-dimensional Cartier block, determinant, and parameter gcd conditions over \(\mathbb F_7\). The second recomputes the genus-two Hasse–Witt coefficient matrix and counts points of the hyperelliptic quotient over \(\mathbb F_{49}\) at an exceptional and an ordinary parameter. The recorded successful checks are `TRIGONAL_GENUS4_CARTIER_PASS`, `GENUS2_QUOTIENT_HASSE_PASS`, and `GF49_QUOTIENT_POINTCHECK_PASS`. Symbolic calculation verifies the displayed identities; the geometric and semilinear steps are given above and not inferred from the finite point census alone.

## Relationship to prior work

Looijenga [1] studies global trigonal genus-four moduli and a ball quotient over the complex numbers; this is geometric motivation but does not determine characteristic-seven arithmetic strata. Borges and Gonçalves [2] determine \(p\)-ranks of Fermat-type curves, especially fixed binomial equations; their stated results do not imply the simultaneous rank stratification in the moving trinomial family here. Baldwin, Eilbeck, Gibbons, and Ônishi [3] study trigonal genus-four curve models in characteristic zero. The earlier cyclic-cover moduli work [4] supplies general trielliptic strata and existence theorems, with different hypotheses; the inspected results do not provide this explicit genus-four \((1,3)\)-signature family, its Prym, reduced rank-at-most-two determinantal ideal, or Hasse multiplicity. Kudo and Harashita [5] study superspecial genus-four curves in small characteristics; the rank-two exceptional Jacobians here are not superspecial. Established Cartier and involution formulas are used without claiming them as new.

## Limitations

The classification concerns this exact one-parameter family over an algebraic closure of the prime field of characteristic seven. It does not classify all cyclic trigonal genus-four curves, the Newton polygons of the two nonordinary fourfold Jacobians, or isomorphism classes of the ordinary parameter stratum. The rank-two exceptional Jacobians are not claimed supersingular. The two exceptional parameter points are not two different moduli points. Independent priority review may uncover an equivalent computation in older unindexed sources.

## References

[1] E. Looijenga, *A ball quotient parametrizing trigonal genus 4 curves*, arXiv:2211.09941 (first posted 2022-11-17), https://arxiv.org/abs/2211.09941.

[2] H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987 (first posted 2022-12-07), https://arxiv.org/abs/2212.03987.

[3] *Abelian Functions for Cyclic Trigonal Curves of Genus Four*, arXiv:math/0612654 (2006), https://arxiv.org/abs/math/0612654. (Background model only.)

[4] *The boundary of the p-rank 0 stratum of the moduli space of cyclic covers of the projective line*, *Nagoya Mathematical Journal*, Cambridge Core article 02D5FFF8FB89AC671E0F637D48BB1613, https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/02D5FFF8FB89AC671E0F637D48BB1613.

[5] M. Kudo and S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114, https://arxiv.org/abs/1607.01114.
