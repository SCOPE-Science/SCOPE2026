# Modular multiset corrections in finite-field averaging projection orbits

## Finding
Let \(k=\mathbb F_q\), where \(q=p^f\) and \(p\) is prime, and let \(A_n=k^n\) have coordinatewise multiplication, for any integer \(n\ge1\). Consider all \(k\)-linear maps \(P:A_n\to A_n\) satisfying simultaneously
\[
P^2=P,\qquad P(x)P(y)=P(P(x)y)=P(xP(y))\quad(x,y\in A_n).
\]
Write \(a_{n,r}(q)\) for the number of such maps of linear rank \(r\), and \(c_{n,r}(q)\) for their number of conjugacy classes under \(\operatorname{Aut}_{k\text{-alg}}(A_n)\cong S_n\).

**Complete classification.** Every map has a unique weighted-block presentation: choose a set \(Z\subseteq[n]\), an unordered partition \(\mathcal B\) of \([n]\setminus Z\) into \(r\) nonempty blocks, and for each \(B\in\mathcal B\) a weight vector \((w_j)_{j\in B}\in k^B\) satisfying \(\sum_{j\in B}w_j=1\). Then
\[
(Px)_i=\begin{cases}
\displaystyle\sum_{j\in B}w_jx_j,&i\in B\in\mathcal B,\\
0,&i\in Z.
\end{cases}
\]
The rank is precisely \(r\). All such data, including the empty block partition defining \(P=0\), satisfy the identities. **No nonzero-weight, positivity, or unitality hypothesis is imposed.**

**Labeled rank census.** Let \(\left\{\!\begin{smallmatrix}s\\r\end{smallmatrix}\!\right\}\) denote the Stirling number of the second kind. Then
\[
a_{n,r}(q)=\sum_{s=r}^{n}\binom ns q^{s-r}\left\{\!\begin{matrix}s\\r\end{matrix}\!\right\},
\qquad
\sum_{n,r\ge0}a_{n,r}(q)\frac{u^n}{n!}z^r
=\exp\left(u+\frac zq(e^{qu}-1)\right).
\]
Here \(a_{0,0}(q)=1\) is only a formal generating-function convention; the algebraic classification is stated for \(n\ge1\).

**The modular conjugacy census.** Define
\[
\mu_s(q)=\frac1q\left[\binom{q+s-1}{s}
-\mathbf 1_{p\mid s}\binom{q/p+s/p-1}{s/p}\right]\qquad(s\ge1).
\]
These are nonnegative integers: \(\mu_s(q)\) counts *unordered multisets of \(s\) elements of \(k\) whose sum is \(1\)*. The complete conjugacy-rank generating series is
\[
\boxed{\quad\sum_{n,r\ge0}c_{n,r}(q)u^nz^r
=\frac1{1-u}\prod_{s\ge1}(1-zu^s)^{-\mu_s(q)}.\quad}
\]
The product is a well-defined formal series. The correction term in \(\mu_s(q)\) is supported **exactly at block sizes divisible by the characteristic**. It records a finite-field orbit phenomenon not visible in positive real averaging weights or in the universal image/kernel criterion. For example, over \(\mathbb F_2\), the labeled rank polynomial at \(n=4\) is
\[
1+40z+58z^2+16z^3+z^4,
\]
while the corresponding automorphism-orbit polynomial is
\[
1+6z+5z^2+2z^3+z^4.
\]

## Assumptions and scope
The algebra \(A_n\) is the **split, commutative, semisimple** coordinate algebra, not a field extension of degree \(n\). Automorphisms are \(k\)-algebra automorphisms, hence coordinate permutations. The theorem counts ordinary linear maps; it does not assume \(P(1)=1\). The weight coordinates may vanish, and characteristic-divisible block sizes are allowed. All counts are over the given finite field; these are set-theoretic enumerations, not claims about scheme-theoretic multiplicity or singularities. The orbit statement concerns conjugacy under algebra automorphisms, not similarity under all linear changes of basis.

## Proof
**1. The averaging-projection condition.** Put \(B=\operatorname{im}P\) and \(K=\ker P\). Since \(P^2=P\), the vector space splits as \(A_n=B\oplus K\), with \(P|_B=\mathrm{id}_B\). The defining identity gives \(B^2\subseteq B\); and for \(b\in B\), \(v\in K\), it gives \(P(bv)=bP(v)=0\). Thus \(BK\subseteq K\). Conversely if \(B\) is a subalgebra, \(K\) is a \(B\)-submodule and \(A_n=B\oplus K\), the corresponding projection satisfies all averaging identities. This is the familiar general decomposition criterion; the finite-field classification and symmetry enumeration below are the specialized contributions.

**2. The subalgebra is supported on disjoint indicator blocks.** First note that for any \(b\in B\), \(b^{q-1}\in B\) is the indicator of the nonzero-coordinate support of \(b\). The Boolean join \(e+f-ef\) of two such indicator vectors is again in \(B\). Their join over all \(b\in B\) is an idempotent \(e\in B\) whose support \(U\subseteq[n]\) consists precisely of coordinates on which at least one member of \(B\) is nonzero. This \(e\) is the identity of \(B\); the case \(B=0\) gives \(U=\varnothing\). Since \(B\subseteq k^U\) is finite-dimensional, commutative and reduced, it is a product of finite field extensions of \(k\). Every field factor has an injective \(k\)-algebra homomorphism into \(k\) obtained by one coordinate projection, so every factor is actually \(k\). Hence the primitive idempotents of \(B\) are the characteristic vectors \(1_B\) of pairwise disjoint nonempty coordinate blocks, and their sum is \(e\). The complement \(Z=[n]\setminus U\) is the zero-output coordinate set. Different indicator blocks yield linearly independent elements, so their number equals \(\dim_kB=r\). The block partition and \(Z\) are intrinsic to \(B\).

**3. Classifying the compatible complements.** Multiplication by \(1_B\) on \(A_n\) projects onto the coordinate summand \(k^B\). Because \(K\) is stable under \(B\), the splitting \(A_n=B\oplus K\) restricts independently to each \(k^B\); and \(k^Z\subseteq K\). On \(k^B\), the image is the one-dimensional constant subspace \(k1_B\), so the projection has form \(x\mapsto(\sum_{j\in B}w_jx_j)1_B\). The equation \(P(1_B)=1_B\) is exactly \(\sum_{j\in B}w_j=1\), and imposes no other restrictions. The component \(k^Z\) is killed. This proves existence, completeness and uniqueness of the displayed form.

**4. Counting labeled maps.** Fix a support \(U\) of size \(s\) (there are \(\binom ns\) choices), and partition it into \(r\) nonempty unlabelled blocks (\(\left\{\!\begin{smallmatrix}s\\r\end{smallmatrix}\!\right\}\) choices). On a block of size \(b\), choose any \(b-1\) weights; the final weight is forced by the sum-one condition, giving \(q^{b-1}\) choices. The product across blocks is \(q^{s-r}\). Sum over \(s\) to get the exact coefficient formula. The exponential formula for labeled sets, with one arbitrary zero-output set and weighted nonempty blocks, gives the displayed two-variable exponential generating function.

**5. Conjugacy and the modular multiset term.** An automorphism of \(A_n\) permutes the coordinate primitive idempotents, and every coordinate permutation is an automorphism. Hence two averaging projections are conjugate if and only if their zero-output coordinate sets have the same size and the unordered multisets of their nonempty **weighted block types** agree. A type of size \(s\) is an unordered multiset of \(s\) elements of \(k\) with sum \(1\). Write its number as \(\mu_s(q)\).

To compute it, use Fourier inversion on the additive group \((k,+)\). The number \(A_s\) of unrestricted multisets of size \(s\) is \(\binom{q+s-1}{s}\). For any *nontrivial* additive character \(\chi\), its generating polynomial over multisets is
\[
\prod_{a\in k}(1-v\chi(a))^{-1}
=(1-v^p)^{-q/p}.
\]
Indeed a nontrivial additive character has image the group of \(p\)-th roots of unity, each appearing exactly \(q/p\) times. The coefficient \(B_s\) of \(v^s\) is zero unless \(p\mid s\), in which case it equals \(\binom{q/p+s/p-1}{s/p}\). Fourier inversion at the nonzero target \(1\in k\), together with \(\sum_{\chi\ne1}\chi(-1)=-1\), gives \(\mu_s(q)=(A_s-B_s)/q\). In particular this expression is integral for every prime power \(q\).

Finally, a conjugacy class consists of a freely chosen multiset of weighted block types plus an arbitrary number of indistinguishable zero-output coordinates. For each of the \(\mu_s(q)\) types of size \(s\), arbitrary multiplicity contributes \((1-zu^s)^{-1}\), and zero coordinates contribute \((1-u)^{-1}\). Multiplying proves the Euler product and exhausts all cases.

## Verification
The standalone `verification.py` evaluates the **original bilinear averaging identity and the idempotence equation** on every matrix over \(\mathbb F_2\) in dimensions \(1,2,3,4\), over \(\mathbb F_3\) in dimensions \(2,3\), and over \(\mathbb F_5\) in dimension \(2\). It independently enumerates ranks and conjugacy orbits under all coordinate permutations and matches both formulas. It additionally tests every matrix in dimension \(2\) over \(\mathbb F_4\) and \(\mathbb F_9\), with correctly implemented extension-field arithmetic, and directly enumerates weighted multisets over those fields for sizes up to six and five respectively. The finite tests validate examples and the implementation; the proof above, not finite enumeration, establishes the formulas for all fields and dimensions.

## Relationship to prior work
Guo and Pei (2014), Proposition 2.3, give the general subalgebra/compatible-kernel criterion for idempotent averaging operators. That criterion and classical connections with conditional expectation are **not** claimed as new. Das (2023) studies the structure and deformation theory of relative averaging operators and motivates finite-dimensional examples, but does not provide the finite-field split-coordinate conjugacy census. Bremner and Elgendy (2021) classify possible operator identities rather than solutions of this specific finite-field algebra. The present result specializes the existing splitting criterion to obtain the **exact mod-characteristic multiset count** and the **full algebra-automorphism orbit/rank series**. Related indexed results involve quadratic local, matrix, or Lie algebras; they do not imply this formula without an additional reduction not found in the accessible evidence.

## Limitations
No claim is made for arbitrary non-idempotent averaging operators, nonsplit semisimple algebras, noncommutative algebras, or arbitrary similarity classes. The proof describes reduced sets of solutions but does not determine geometric scheme structure. Prior universal subalgebra/kernel conditions and classical averaging interpretations remain prior art. Full publication priority is provisional: indexed material and accessible literature may omit another classification, and some related indexed full texts were inaccessible. Independent verification is not asserted.

## References
1. A. Das, *Controlling structures, deformations and homotopy theory for averaging algebras*, arXiv:2303.17798v1, publicly posted March 31, 2023. https://arxiv.org/abs/2303.17798 ; full text https://arxiv.org/html/2303.17798v1 .
2. L. Guo and J. Pei, *Averaging algebras, Schröder numbers, rooted trees and operads*, arXiv:1401.7386, 2014; Proposition 2.3. https://arxiv.org/abs/1401.7386 .
3. M. R. Bremner and H. A. Elgendy, *A new classification of algebraic identities for linear operators on associative algebras*, arXiv:2109.04391, 2021. https://arxiv.org/abs/2109.04391 .
