# Coefficient-independent parity of quadratic-extension permutation binomials

## Finding

Let \(q\) be any odd prime power, \(r,d\) positive integers with \(\gcd(d,q+1)=2\), and \(a\in\mathbb F_{q^2}\). Suppose that
\[
F_{r,d,a}(X)=X^r\bigl(X^{d(q-1)}+a\bigr)
\]
permutes \(\mathbb F_{q^2}\). Then \(r\) is odd and the sign of the resulting permutation of its \(q^2\) field elements is
\[
\boxed{\operatorname{sgn}(F_{r,d,a})=(-1)^{(r-1)/2}.}
\]
Equivalently, the permutation lies in the alternating group if and only if \(r\equiv1\pmod4\); it is odd if and only if \(r\equiv3\pmod4\). The sign is independent of \(q\), \(d\), and the admissible coefficient \(a\), including \(a=0\).

For a nonzero-coefficient example, in \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\), both \(X(X^4+u)\) and \(X^3(X^4+u)\) are permutations, with signs \(+1\) and \(-1\) respectively.

## Assumptions and scope

The sign means the ordinary alternating character on the finite set \(\mathbb F_{q^2}\); it does not depend on any ordering of the elements. Write \(h=q-1\), \(t=q+1\), \(m=t/2\), and \(D=d(q-1)\). The assumption \(\gcd(d,t)=2\) gives \(\gcd(D,q^2-1)=2h\). We discuss only parameters for which \(F_{r,d,a}\) really is a permutation; no permutation criterion is asserted here.

## Proof

**1. Necessary parity and a coefficient lemma.** The homomorphism \(x\mapsto x^D\) on \(\mathbb F_{q^2}^{\times}\) has kernel of order \(2h\), and image \(\mu_m\), the \(m\)-th roots of unity. On a fiber \(x^D=y\), the formula is \(F_{r,d,a}(x)=x^r(y+a)\). Bijectivity forces \(\gcd(r,2h)=1\), so \(r\) is odd. It also forces \(y+a\ne0\) for every \(y\in\mu_m\), and induces the permutation
\[
y\longmapsto y^r(y+a)^D\quad\text{of }\mu_m.
\]
Set \(\epsilon=(-1)^m\) and \(B=a^m-\epsilon=\prod_{y\in\mu_m}(y+a)\); thus \(B\ne0\). Taking the product of all images of this permutation and using oddness of \(r\) yields \(B^D=1\). Consequently \(B^{2h}=1\), since \(\gcd(D,q^2-1)=2h\).

We prove the crucial assertion \(B\in\mathbb F_q^{\times}\). For \(a=0\) it is immediate. Otherwise put \(w=a^m\ne0\). As \(2m=t\), \(w^{2h}=a^{q^2-1}=1\). Thus both \(w^q=\pm w\) and \(B^q=\pm B\), because in odd characteristic \(z^{2(q-1)}=1\) implies \((z^q/z)^2=1\). If \(w^q=-w\), then \(B^q=-w-\epsilon\). Equality to \(B=w-\epsilon\) would force \(w=0\), while equality to \(-B=-w+\epsilon\) would force \(\epsilon=0\). Both are impossible. Hence \(w^q=w\), and \(B=w-\epsilon\in\mathbb F_q^{\times}\).

**2. Signs from multiplicative cosets.** Choose a generator \(g\) of \(\mathbb F_{q^2}^{\times}\), and let \(H=\langle g^t\rangle=\mathbb F_q^{\times}\), of even cardinality \(h\). The \(t\) cosets \(g^jH\), for \(0\le j<t\), are permuted by \(F_{r,d,a}\). Represent the image of the coset \(g^jH\) by \(g^{\sigma(j)}H\) and write uniquely, modulo \(h\),
\[
F_{r,d,a}(g^j)=g^{\sigma(j)+tc_j},\qquad 0\le\sigma(j)<t.
\]
The map on the internal exponent of \(g^{j+tv}\) is \(v\mapsto rv+c_j\pmod h\). Permuting blocks of even size contributes sign \(+1\). The common multiplication map \(v\mapsto rv\) occurs in each of the even number \(t\) of blocks and cancels in the sign. A translation \(v\mapsto v+c_j\) on \(\mathbb Z/h\mathbb Z\), with \(h\) even, has sign \((-1)^{c_j}\). Therefore
\[
\operatorname{sgn}(F_{r,d,a})=(-1)^{\sum_{j=0}^{t-1}c_j}.
\]
The fixed zero contributes sign \(+1\).

**3. The product identity fixes the parity.** Put \(S=\sum_{j=0}^{t-1}j=t(t-1)/2\). Multiplication over the coset representatives gives
\[
(g^t)^{\sum_jc_j}=g^{(r-1)S}
\prod_{j=0}^{t-1}\bigl(g^{jD}+a\bigr).
\]
The element \(g^D\) has order \(m=t/2\), so the last product runs through every element of \(\mu_m\) exactly twice and equals \(B^2\). As \(r\) is odd,
\[
(g^t)^{\sum_jc_j-(r-1)(t-1)/2}=B^2.
\]
Since \(g^t\) generates \(H\) and \(B\in H\), the right side has even discrete logarithm to base \(g^t\). Thus \(\sum_jc_j\equiv(r-1)(t-1)/2\pmod2\). Because \(t-1=q\) is odd, \(\sum_jc_j\equiv(r-1)/2\pmod2\). Substitute this in the displayed sign formula. This completes the proof for every stated field and all admissible parameters.

## Verification

The attached `verify_parity.py` constructs exact quadratic extensions of the prime fields of sizes \(3,5,7,11,13\), and exhaustively checks all coefficients, all \(d\) with \(1\le d\le q+1\) and \(\gcd(d,q+1)=2\), and odd \(r\) with \(1\le r<2(q+1)\) and \(\gcd(r,q-1)=1\). It independently determines whether the polynomial is a permutation by enumerating its images and its sign by cycle decomposition, then compares the predicted sign and checks \(a^{(q+1)/2}\in\mathbb F_q\). Exactly \(1251\) permutation instances passed, partitioned into \(707\) even and \(544\) odd cases. Run: `python3 verify_parity.py`. These finite checks are not a proof for general prime powers; the proof above supplies that conclusion.

## Relationship to prior work

Tang and Fan [1] classify the permutation binomials \(X^r(X^{2(q-1)}+a)\) and extend their classification to \(\gcd(d,q+1)=2\); their necessary coefficient condition is consistent with Step 1 above. The new statement determines the alternating character of *each* permutation in this classified family, with a coefficient-independent formula. Bors and Wang [2] give a much broader wreath-product representation for generalized cyclotomic permutations, which supplies general block-cycle machinery but does not state the special coefficient rigidity or this sign formula. The proof above independently derives the needed coefficient restriction and evaluates the product, rather than assuming a generic mapping has the claimed sign. Related index-one binomial sign results have coefficient-dependent factors and do not subsume this even-index family.

## Limitations

This is a conditional classification of signs, not a new test for when a binomial permutes. It does not classify individual cycle lengths, and does not address other values of \(\gcd(d,q+1)\) or characteristic two. A corresponding general formula may be implicit in broader cyclotomic-wreath literature; that remains an originality risk. No independent mathematical audit has been performed.

## References

[1] Zhichao Tang and Xiang Fan, *A complete classification of permutation binomials of the form \(X^r(X^{2(q-1)}+a)\) over finite fields*, arXiv:2611.14162v1, publicly submitted 10 November 2026. https://arxiv.org/abs/2611.14162

[2] Alexander Bors and Qiang Wang, *Generalized cyclotomic mappings: Switching between polynomial, cyclotomic, and wreath product form*, arXiv:2103.00664v1 (2021), published in *Communications in Mathematics Research* 38 (2022), 246–318. https://arxiv.org/abs/2103.00664
