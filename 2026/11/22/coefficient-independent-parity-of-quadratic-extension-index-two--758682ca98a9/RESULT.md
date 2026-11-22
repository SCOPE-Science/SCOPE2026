# Coefficient-independent parity of quadratic-extension index-two permutation binomials

## Finding

Let \(q\) be any odd prime power, and let \(d,r\geq 1\) be integers satisfying \(\gcd(d,q+1)=2\). For any nonzero \(a\in\mathbb F_{q^2}\), suppose that
\[
F_{r,d,a}(X)=X^r\bigl(X^{d(q-1)}+a\bigr)
\]
permutes \(\mathbb F_{q^2}\). Necessarily \(r\) is odd, and the sign of the induced permutation is
\[
\boxed{\operatorname{sgn}(F_{r,d,a})=(-1)^{(r-1)/2}.}
\]
Consequently **every admissible nonzero coefficient has exactly the same permutation parity** for fixed \(q,d,r\): the permutation is even for \(r\equiv1\pmod4\), and odd for \(r\equiv3\pmod4\). The assertion includes all prime powers, not just prime fields, and all indices with the stated gcd condition; it does not require a separate classification of admissible coefficients.

## Assumptions and scope

Throughout, \(q\) is odd, \(m=q-1\), \(h=(q+1)/2\), \(N=q^2-1=m(q+1)\), and \(D=d(q-1)\). Thus \(\gcd(D,N)=2m\), and the image of \(x\mapsto x^D\) on \(\mathbb F_{q^2}^{\times}\) is \(\mu_h\), the cyclic group of \(h\)-th roots of unity. The coefficient \(a\) is nonzero; the theorem is conditional on \(F_{r,d,a}\) actually being a permutation, and is not a new criterion for when that occurs. Permutation sign counts the parity of a bijection on all \(q^2\) elements, with zero a fixed point.

## Proof

**1. The induced root-of-unity permutation.** For any \(u\) with \(u^D=1\) and \(x\neq0\),
\[
F_{r,d,a}(ux)=u^r F_{r,d,a}(x).
\]
Because \(F_{r,d,a}\) is injective, its restriction to each fiber of \(x\mapsto x^D\), a coset of \(\mu_{2m}\), is injective. Hence \(\gcd(r,2m)=1\), so \(r\) is odd. Raising the image to the \(D\)-th power induces a permutation of \(\mu_h\) given by
\[
H(y)=y^r(y+a)^D.
\]
No factor \(y+a\) vanishes, because a nonzero root of \(F_{r,d,a}\) would contradict the fixed zero.

**2. A coefficient-square constraint.** Set \(\varepsilon=(-1)^h\), \(w=a^h\), and \(B=w-\varepsilon\). Multiplication of \(H(y)\) over all \(y\in\mu_h\) gives
\[
\prod_{y\in\mu_h}H(y)=\prod_{y\in\mu_h}y,
\qquad
\prod_{y\in\mu_h}(y+a)=a^h-(-1)^h=B.
\]
Because \(r\) is odd and \(\prod_{y\in\mu_h}y\in\{1,-1\}\), it follows that \(B^D=1\). Moreover \(w^{2m}=a^{q^2-1}=1\); and \(B^{2m}=1\) because the order of \(B\) divides \(\gcd(D,N)=2m\). Thus there are \(s,t\in\{1,-1\}\) with \(w^q=sw\) and \(B^q=tB\). Taking the \(q\)-th power in \(B=w-\varepsilon\) yields
\[
(s-t)w=(1-t)\varepsilon.
\]
Since \(w\neq0\), \(B\neq0\), and the characteristic is odd, the only possible choice is \(s=t=1\): \((s,t)=(-1,-1)\) would force \(2\varepsilon=0\); \((1,-1)\) would force \(w=\varepsilon\), making \(B=0\); and \((-1,1)\) would force \(w=0\). In particular,
\[
\boxed{B\in\mathbb F_q^\times.}
\]
The related square-coefficient restriction is established in Tang–Fan's Lemma 2.2 for \(d=2\); the argument here directly covers every \(d\) with \(\gcd(d,q+1)=2\).

**3. A coset-sign lemma.** Choose a primitive element \(\gamma\in\mathbb F_{q^2}^{\times}\) and write \(\delta=\gamma^{q+1}\), a generator of \(\mathbb F_q^\times\). The \(q+1\) cosets \(\gamma^i\mathbb F_q^\times\), \(0\leq i\leq q\), all have even cardinality \(m\). Since
\[
F_{r,d,a}(tx)=t^r F_{r,d,a}(x)\quad(t\in\mathbb F_q^\times),
\]
there is a permutation \(\sigma\) of these cosets and uniquely determined \(b_i\in\mathbb F_q^\times\) such that
\[
F_{r,d,a}(\gamma^i t)=\gamma^{\sigma(i)}b_it^r.
\]
Reordering blocks of even size contributes sign \((\operatorname{sgn}\sigma)^m=1\). The internal power map \(t\mapsto t^r\) occurs \(q+1\) times, an even number, so its total sign is also one. Multiplication by \(b_i\) on the cyclic group \(\mathbb F_q^\times\) has sign \(\chi_q(b_i)\), where \(\chi_q\) is its quadratic character: with \(b_i=\delta^k\), this is translation by \(k\) modulo the even integer \(m\) and has sign \((-1)^k\). Therefore
\[
\operatorname{sgn}(F_{r,d,a})=\chi_q\left(\prod_{i=0}^{q}b_i\right).
\]

**4. Cancellation of the coefficient.** By the definition of \(b_i\),
\[
\prod_{i=0}^{q}b_i=\gamma^{(r-1)q(q+1)/2}
\prod_{i=0}^{q}\left(\gamma^{iD}+a\right).
\]
The element \(\gamma^D\) has order exactly \(h\), because \(\gcd(D,N)=2m\). As \(q+1=2h\), the sequence \(\gamma^{iD}\), \(0\leq i\leq q\), lists every element of \(\mu_h\) exactly twice. Consequently
\[
\prod_{i=0}^{q}(\gamma^{iD}+a)=
\left(\prod_{y\in\mu_h}(y+a)\right)^2=B^2.
\]
Since \(r\) is odd,
\[
\prod_{i=0}^{q}b_i=\delta^{q(r-1)/2}B^2.
\]
Step 2 makes \(B^2\) an actual square in \(\mathbb F_q^\times\). Since \(q\) is odd and \(\chi_q(\delta)=-1\),
\[
\operatorname{sgn}(F_{r,d,a})=
(-1)^{q(r-1)/2}\chi_q(B^2)=(-1)^{(r-1)/2},
\]
which proves the theorem.

## Verification

The standalone standard-library script `verify_sign.py` constructs extension fields through explicit irreducible polynomials, performs all field operations, evaluates the binomial on every field element, checks bijectivity directly, and computes parity independently by cycle decomposition. Its tests cover \(q=3,5,7,11,9\) (including nonprime \(q=9\)), several permitted values of \(d\), and all small exponent choices satisfying \(\gcd(r,2(q-1))=1\). There were **16,064** direct parameter evaluations, including **2,132** actual permutations; every permutation had the predicted sign, and both signs occurred. Run `python3 verify_sign.py` from this directory. This bounded computation supports but does not prove the general theorem.

## Relationship to prior work

Tang and Fan (arXiv:2611.14162v1, submitted 10 November 2026) completely classify which index-two binomials permute, including the general \(d\)-extension in Corollary 1.4. Their Lemma 2.2 establishes a square-coefficient constraint. Neither the main statements nor the inspected full text specifies the permutation sign or proves that it is independent of the admissible coefficient. The present finding asks for a different invariant after a permutation is known to exist, and derives the exact character using the duplicate root-of-unity product and even-fiber cancellation.

Bors and Wang (arXiv:2103.00664) develop the general coset/wreath-product description of cyclotomic permutations. That framework explains the sign decomposition in Step 3, which is not claimed as new. It does not by itself impose the special coefficient-square constraint or the resulting constant-parity formula for this index-two binomial family. A previously published result, *A universal sign bias for classified finite-field permutation binomials* (2026), gives a quadratic-character-dependent sign for the distinct index-one family \(X^r(X^{q-1}+a)\), together with an unequal even/odd coefficient count; that is not an index-two formula. The contrast between coefficient-varying index-one signs and fixed index-two signs is the structural distinction.

## Limitations

This is a conditional parity classification, not an enumeration of admissible coefficients or a new permutation criterion. It concerns odd characteristic, quadratic extensions, \(\gcd(d,q+1)=2\), and nonzero coefficients. General cyclotomic/wreath methods supply part of the proof; therefore the possible existence of an earlier implicit, unpublished, or differently indexed specialization is a genuine originality risk. Finite tests do not establish universal validity, and no claim of independent validation is made.

## References

1. Zhichao Tang and Xiang Fan, *A complete classification of permutation binomials of the form \(X^r(X^{2(q-1)}+a)\) over finite fields*, arXiv:2611.14162v1, 10 November 2026. https://arxiv.org/html/2611.14162v1
2. Alexander Bors and Qiang Wang, *Generalized cyclotomic mappings: Switching between polynomial, cyclotomic, and wreath product form*, arXiv:2103.00664v1, 1 March 2021; published 2022. https://arxiv.org/abs/2103.00664
3. *A universal sign bias for classified finite-field permutation binomials*, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-a-universal-sign-bias-for-classified-finite-field-permutation-bi--2c4a64ac82f2/RESULT.md
4. *Collision rigidity and exact enumeration for coprime-index permutation binomials*, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/9/18/SCOPE-coprime-index-permutation-binomial-collisions--249fad2fb294/RESULT.md
