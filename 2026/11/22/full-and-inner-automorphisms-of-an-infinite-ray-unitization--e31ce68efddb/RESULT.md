# Full and inner automorphisms of an infinite-ray unitization

## Finding

Let \(k\) be any field and let \(R\) be the unital algebra with \(k\)-basis \(1,e_0,e_1,\ldots,a_0,a_1,\ldots\), where every element is a **finite** linear combination, and
\[
e_i e_j=\delta_{ij}e_i,\quad e_i a_j=\delta_{ij}a_j,\quad a_j e_i=\delta_{i,j+1}a_j,\quad a_i a_j=0.
\]
This is the one-sided infinite-ray radical-square-zero path algebra with an identity adjoined. For arbitrary sequences \(c=(c_i)_{i\ge0}\in k^{\mathbb N_0}\) and \(\lambda=(\lambda_i)_{i\ge0}\in(k^\times)^{\mathbb N_0}\), define
\[
\Phi_{c,\lambda}(1)=1,\qquad
\Phi_{c,\lambda}(e_i)=e_i+c_{i-1}a_{i-1}-c_i a_i,\qquad
\Phi_{c,\lambda}(a_i)=\lambda_i a_i,
\]
with the term indexed \(-1\) interpreted as zero. Every unital \(k\)-algebra automorphism of \(R\) has **exactly one** such form, and
\[
\Phi_{c,\lambda}\circ\Phi_{d,\mu}=\Phi_{c+\lambda d,\,\lambda\mu}.
\]
Therefore, writing \(\operatorname{Aff}_1(k)=k\rtimes k^\times\),
\[
\operatorname{Aut}_{k\text{-alg}}(R)\cong\prod_{i\ge0}\operatorname{Aff}_1(k),\qquad
\operatorname{Inn}(R)\cong\bigoplus_{i\ge0}\operatorname{Aff}_1(k),
\]
and the **outer automorphism group** is the reduced product
\[
\operatorname{Out}_{k\text{-alg}}(R)\cong
\left(\prod_{i\ge0}\operatorname{Aff}_1(k)\right)
\Big/\left(\bigoplus_{i\ge0}\operatorname{Aff}_1(k)\right).
\]
The direct sum is embedded as the finite-support subgroup. Every automorphism is **locally inner**: for each finite subset \(F\subset R\), some unit \(u_F\in R^\times\) has \(\Phi(x)=u_Fxu_F^{-1}\) for all \(x\in F\). Nevertheless, the inner subgroup is proper. If \(k\) is finite, the outer group has cardinality \(2^{\aleph_0}\), including for \(k=\mathbb F_2\).

## Assumptions and scope

The field is arbitrary, including characteristic two. Only **unital, \(k\)-linear algebra automorphisms** are classified; ring automorphisms that act nontrivially on \(k\) are outside the claim. All ring elements and units have finite support, but the automorphism parameters \(c,\lambda\) may have infinite support. The product and sum above are algebraic group constructions, with no topological completion of \(R\).

## Proof

**1. The radical determines every vertex.** Put \(J=\bigoplus_{i\ge0}ka_i\). We have \(J^2=0\). The quotient \(R/J\) is the algebra of eventually constant \(k\)-valued functions on \(\mathbb N_0\), where \(e_i\) is the characteristic function of \(\{i\}\) and \(1\) is the constant-one function. This quotient has zero Jacobson radical: the coordinate evaluations (including the eventual value) distinguish every nonzero element and have field quotients. Therefore \(J=\operatorname{Jac}(R)\), so every automorphism preserves \(J\). The nonzero primitive idempotents of \(R/J\) are precisely the \(e_i+J\). Any automorphism thus permutes them, say by \(\sigma\). Its induced map on the Peirce spaces preserves their dimensions. Since
\[
\dim_k(e_iJe_j)=\begin{cases}1,&j=i+1,\\0,&\text{otherwise},\end{cases}
\]
\(\sigma\) is a directed-graph automorphism of the one-sided ray. Its unique source is vertex zero, and induction along the unique outgoing edge gives \(\sigma(i)=i\) for all \(i\).

**2. Idempotent lifts.** Write \(f_i=\Phi(e_i)=e_i+w_i\), with \(w_i\in J\). The equation \(f_i^2=f_i\), together with \(J^2=0\), forces \(w_i\) to be supported only on \(a_{i-1}\) (when \(i>0\)) and \(a_i\). Indeed, the coefficient of every other arrow in \(e_iw_i+w_ie_i\) is zero and must equal its coefficient in \(w_i\). Thus \(f_i=e_i+r_{i-1}a_{i-1}+s_i a_i\). The orthogonality equation \(f_if_{i+1}=0\) gives \(r_i+s_i=0\) for all \(i\). Defining \(c_i=-s_i=r_i\) gives the displayed formula for the vertex images.

**3. Arrow images and converse.** Since \(J^2=0\), the Peirce space \(f_iJf_{i+1}\) equals \(e_iJe_{i+1}=ka_i\). Consequently \(\Phi(a_i)=\lambda_i a_i\) with \(\lambda_i\in k^\times\). Conversely, for any sequences \(c,\lambda\), the prescribed images satisfy all the displayed multiplication relations: vertex images remain orthogonal idempotents and have the same left/right actions on each scaled arrow. Each image of a basis element contains only finitely many terms, so this gives a well-defined unital algebra map on the **direct-sum** vector space, even when the parameters have infinite support. Its inverse is \(\Phi_{-\lambda^{-1}c,\lambda^{-1}}\), and composition gives the claimed coordinatewise affine law. Uniqueness follows by comparing the coefficients of \(a_i\) in \(\Phi(e_i)\) and \(\Phi(a_i)\).

**4. Inner automorphisms have exactly finite support.** An arbitrary unit is, after division by a nonzero central scalar, of the form
\[
u=1+\sum_i(d_i-1)e_i+\sum_i s_i a_i,
\]
with only finitely many nonzero \(d_i-1,s_i\), and each \(d_i\in k^\times\). Conversely all such expressions are units, because the diagonal part is invertible and the arrow part is square-zero. Direct multiplication using the inverse of the diagonal-plus-arrow element yields
\[
\operatorname{Ad}_u(e_i)
=e_i+\frac{s_{i-1}}{d_i}a_{i-1}-\frac{s_i}{d_{i+1}}a_i,
\qquad
\operatorname{Ad}_u(a_i)=\frac{d_i}{d_{i+1}}a_i.
\]
Thus the parameters of an inner automorphism are \(c_i=s_i/d_{i+1}\) and \(\lambda_i=d_i/d_{i+1}\), which are eventually \(0\) and \(1\), respectively. Conversely, given any sequences \(c,\lambda\) with finite support, take
\[
d_i=\prod_{j=i}^{\infty}\lambda_j,\qquad s_i=c_i d_{i+1}.
\]
These products are finite, \(d_i=1\) eventually, and the preceding formula realizes \(\Phi_{c,\lambda}=\operatorname{Ad}_u\). Hence the inner subgroup is exactly the restricted direct product (direct sum), and the quotient formula follows.

**5. Local-versus-global innerness.** For a finite set of elements of \(R\), their supports involve only finitely many vertices and arrows. Truncate \(c\) and \(\lambda-1\) to the finitely many indices needed to match the images of those basis elements. Step 4 realizes the resulting finite-support automorphism by conjugation, agreeing with the original map on the given elements. To see that innerness fails globally, choose \(c_i=1\) at every index and \(\lambda_i=1\). This automorphism exists by Step 3 but has infinite support, so Step 4 rules out conjugation by any unit. For finite \(k\), each factor \(\operatorname{Aff}_1(k)\) has at least two elements, so its countable product has size continuum, while its finite-support direct sum is countable; therefore its quotient also has continuum cardinality.

## Verification

The independent finite-interval test script `verify_ray_automorphisms.py` models the multiplication table of the finite truncated ray, tests all basis-product relations, constructs the inverse map, and explicitly constructs conjugating units. Exhaustive parameter runs were performed for \((|k|,m)=(2,4),(3,3),(5,2)\), where \(m\) counts arrows, and 100 seeded random parameter samples each at \((5,8),(7,7),(11,6)\). All 932 cases passed; the output is `INFINITE_RAY_UNITIZATION_AUTOMORPHISMS_OK cases=932`. Finite tests corroborate the formulas but the proof of the infinite statement is the preceding ring-theoretic argument, not the enumeration.

## Relationship to prior work

Chen and Ding introduce exactly this unitized countable-ray algebra to separate two homological dimensions, with defining relations in Section 2; their work does not determine its algebra automorphisms or the inner/outer distinction [1]. Ford's structural treatment of automorphisms of locally string algebras is close in subject, but Definition 2.1 and Notation 2.2 explicitly **require a finite vertex quiver**, even in the locally string case; its infinite-dimensionality arises in a different way. Its stated decomposition therefore does not cover the countably many primitive vertices here [2]. Finite radical-square-zero quiver results also do not entail the infinite-support automorphisms or the reduced-product outer group. The present classification follows directly from the special multiplication in [1] and is self-contained.

## Limitations

This is an exact invariant of one naturally occurring countably generated algebra, not a classification of automorphisms for arbitrary infinite quivers or arbitrary square-zero unitizations. The stated outer group is for \(k\)-linear automorphisms; general field-semilinear ring automorphisms are excluded. Historical originality is provisional: an older, unindexed infinite-quiver theorem or direct computation could imply the same normal form. No independent mathematical audit has been performed.

## References

[1] X. Chen and H. Ding, *Rings with unequal silp–spli*, arXiv:2611.17132, first posted 12 November 2026, Section 2 and Theorem 1.2. https://arxiv.org/html/2611.17132v2

[2] S. Ford, *Automorphisms of locally string algebras*, arXiv:2510.08701, 9 October 2025, Definition 2.1, Section 3 and Theorem 6.2. https://arxiv.org/html/2510.08701v1
