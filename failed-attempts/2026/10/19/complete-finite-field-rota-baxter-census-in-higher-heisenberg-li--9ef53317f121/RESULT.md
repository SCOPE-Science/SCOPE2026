# Complete finite-field Rota–Baxter census in higher Heisenberg Lie algebras

## Finding
Let \(q\) be any prime power, \(n\ge 2\), and \(\lambda\in\mathbb F_q\). The complete linear weight-\(\lambda\) Rota–Baxter operator census for the \((2n+1)\)-dimensional Heisenberg Lie algebra consists of two sharply separated strata: a totally isotropic-image stratum on exactly the scalar fibers \(c(c-\lambda)=0\), and a symplectic-similitude stratum on all other scalar fibers.

Write
\[
U_{n,r}(q)=\frac{\prod_{i=0}^{r-1}(q^{2n-i}-q^i)}{\prod_{i=0}^{r-1}(q^r-q^i)},\qquad
S_{n,r}(q)=\prod_{i=0}^{r-1}(q^{2n}-q^i),
\]
where an empty product is one, and define
\[
I_n(q)=\sum_{r=0}^n U_{n,r}(q)S_{n,r}(q),\qquad
P_n(q)=q^{n^2}\prod_{j=1}^n(q^{2j}-1).
\]
Then **the total number of operators** equals
\[
\mathcal R_{n,q}(\lambda)=q^{2n}\begin{cases}
I_n(q)+(q-1)P_n(q),&\lambda=0,\\
2I_n(q)+(q-2)P_n(q),&\lambda\ne0.
\end{cases}
\]
For a fixed singular scalar fiber, the rank-\(r\) count is exactly \(q^{2n}U_{n,r}(q)S_{n,r}(q)\); for any fixed nonsingular scalar fiber the count is exactly \(q^{2n}P_n(q)\).

## Assumptions and scope
Fix a \(2n\)-dimensional \(\mathbb F_q\)-space \(V\) carrying a **nondegenerate alternating** bilinear form \(\omega\), and set \(H_n=V\oplus \mathbb F_q z\). Use the normalization
\[
[v+sz,w+tz]=\omega(v,w)z.
\]
There is no factor of one-half in this convention, so it applies unchanged in characteristic two. A weight-\(\lambda\) Lie Rota–Baxter operator is an \(\mathbb F_q\)-linear map \(R:H_n\to H_n\) satisfying, for all \(x,y\in H_n\),
\[
[R(x),R(y)]+\lambda R([x,y])=R([R(x),y]+[x,R(y)]).
\]
The sign convention puts \(\lambda R([x,y])\) on the left: relative to the also-common convention with \(\lambda[x,y]\) inside the argument of \(R\) on the right, replace the weight parameter by its negative. This change does not affect the zero-versus-nonzero total counts. No invertibility or augmentation condition is imposed on \(R\). Counts concern actual linear maps, not conjugacy classes. Although the proof of the structural parametrization works over arbitrary fields, the enumeration requires finite fields. The dimension assumption \(n\ge2\) excludes the previously enumerated three-dimensional case.

## Proof
**1. Center preservation.** Write an arbitrary linear map as
\[
R(v+tz)=Av+ta+(\ell(v)+ct)z,
\]
for \(A\in\operatorname{End}(V)\), \(a\in V\), \(\ell\in V^*\) and \(c\in\mathbb F_q\). Insert \(x=v\) and \(y=z\) into the defining identity. Since \([v,z]=0\), this gives
\[
\omega(Av,a)z=\omega(v,a)(a+cz).
\]
Comparing the \(V\)-components yields \(\omega(v,a)a=0\) for all \(v\). If \(a\ne0\), nondegeneracy supplies a \(v\) with \(\omega(v,a)\ne0\), contradiction. Hence \(a=0\), and \(R(z)=cz\).

**2. The symplectic multiplier equation.** For arbitrary \(v,w\in V\), the defining identity now becomes exactly
\[
\omega(Av,Aw)+\lambda c\omega(v,w)
=c\big(\omega(Av,w)+\omega(v,Aw)\big).
\]
Put \(B=A-cI\) and expand the left side of \(\omega(Bv,Bw)\). The displayed equation is equivalent to
\[
\boxed{\omega(Bv,Bw)=c(c-\lambda)\omega(v,w)}
\]
for every \(v,w\); no conditions involve \(\ell\). Bilinearity and the alternating property show that checking these equations on basis pairs suffices. The calculation is reversible, so the displayed condition is both necessary and sufficient.

**3. Singular fibers.** When \(c(c-\lambda)=0\), the condition says precisely that \(\operatorname{im}B\) is totally isotropic, hence its rank \(r\) lies between zero and \(n\). The number of ordered linearly independent \(r\)-tuples spanning an isotropic subspace equals \(\prod_{i=0}^{r-1}(q^{2n-i}-q^i)\): after \(i\) vectors have been selected, their common orthogonal complement has \(q^{2n-i}\) elements, and the existing span contributes \(q^i\) forbidden elements. Dividing by the number \(\prod_{i=0}^{r-1}(q^r-q^i)\) of ordered bases of an \(r\)-space gives \(U_{n,r}(q)\). For any fixed image space of dimension \(r\), the number of surjections \(V\twoheadrightarrow W\) is \(S_{n,r}(q)\): take the \(r\) coordinate functionals of the map as an independent ordered \(r\)-tuple in \(V^*\). Each \(B\) permits independently any of the \(q^{2n}\) functionals \(\ell\). This establishes the rank-refined formula.

**4. Nonsingular fibers.** When \(\mu=c(c-\lambda)\ne0\), the equation is the defining condition for a symplectic similitude of multiplier \(\mu\). Such maps exist for every nonzero \(\mu\): relative to a symplectic basis, multiply the vectors of one Lagrangian summand by \(\mu\), and fix the vectors of its dual Lagrangian. The set of all similitudes of prescribed multiplier is then a coset of \(\operatorname{Sp}_{2n}(q)\). Its cardinality is \(P_n(q)\), since choosing a nonzero first symplectic basis vector gives \(q^{2n}-1\) choices, choosing its partner pairing to one gives \(q^{2n-1}\) choices, and induction in the orthogonal complement gives
\[
|\operatorname{Sp}_{2n}(q)|=\prod_{j=1}^n q^{2j-1}(q^{2j}-1)=P_n(q).
\]
Again multiply by \(q^{2n}\) for the free \(\ell\).

**5. Scalar-fiber count.** If \(\lambda=0\), only \(c=0\) is singular and exactly \(q-1\) scalars are nonsingular. If \(\lambda\ne0\), the two singular fibers are \(c=0\) and \(c=\lambda\), leaving exactly \(q-2\) nonsingular scalars. Adding the disjoint fibers proves both asserted total formulas. No limiting or genericity arguments are involved.

## Verification
Run \(\texttt{python3 verify.py}\) using the attached, standalone Python checker (no third-party packages). It directly evaluates the original weight-\(\lambda\) identity for all linear maps on the three-dimensional Heisenberg algebra over fields of orders two and three and for weights zero and one over the field of order four. Its complete five-dimensional binary matrix census checks the singular rank profile \((1,225,3150)\), the weight-zero nonsingular fiber size \(720\), and both aggregate totals: \(65{,}536\) for weight zero and \(108{,}032\) for nonzero weight. It also performs randomized direct identity-versus-normal-form comparisons in dimensions five and seven, plus exact integer formula checks. Over \(\mathbb F_3\) in dimension five, the formulas give \(28{,}874{,}961\) operators at weight zero and \(45{,}152{,}802\) for every nonzero weight. A successful run ends with \(\texttt{ALL_HEISENBERG_RB_CHECKS_PASSED}\). The finite checks are independent tests, not substitutes for the argument for every \(n,q,\lambda\).

## Relationship to prior work
Ji and Hua (2018) classify three-dimensional Heisenberg Rota–Baxter operators; Zhu and Wu (2018) treat the associated three-dimensional Yang–Baxter formulation. Rathee's 2024 paper classifies weight-one operators in the three-dimensional complex Heisenberg setting and studies related group/brace structures. These results are not claimed as new here. A prior all-dimensional Nijenhuis classification already counts the *isotropic-image* linear maps arising in the singular scalar fibers; that portion of the present parametrization is likewise **not** independently claimed as new. The assessed extension is the **nonsingular symplectic-similitude branch for all higher Heisenberg ranks**, and the way it completes the exact weight-dependent operator census for every finite field and every \(n\ge2\). General Rota–Baxter Lie integration results give conceptual background but do not provide this finite-field census.

## Limitations
This is a census of all operators, not an orbit classification under Lie-algebra automorphisms; no formula for conjugacy classes is asserted. The full proof fixes a symplectic form and the stated bracket normalization. The rank strata are indexed by the rank of \(R|_V-cI\), not by the rank of \(R\) itself. No claim of independently certified historical uniqueness is made: unindexed or inaccessible earlier linear-algebra literature may contain equivalent all-rank statements. Three-dimensional and singular-isotropic classifications are known and excluded from the priority claim.

## References
1. G. Ji and X. Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean J. Math. **26** (2018), 53–66, DOI `10.11568/kjm.2018.26.1.53` (public 2018-03-30).
2. K. X. Zhu and M. Z. Wu, *The Classical Yang-Baxter Operator on the Heisenberg Lie Algebra and Its Applications*, Pure Mathematical Sciences **7** (2018), 45–52, DOI `10.12988/pms.2018.81012`.
3. N. Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg group*, arXiv:`2402.15428` (initial version 2024-02-23).
4. L. Guo, H. Lang and Y. Sheng, *Integration and geometrization of Rota–Baxter Lie algebras*, Advances in Mathematics **387** (2021), article 107834, DOI `10.1016/j.aim.2021.107834`.
