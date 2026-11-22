# Uniform parity of two-to-one index permutation binomials

## Finding

**Theorem.** Let \(q\ge3\) be any odd prime power, \(d,r\ge1\) integers satisfying \(\gcd(d,q+1)=2\), and \(a\in\mathbb F_{q^2}\). Assume that the polynomial
\[
f(X)=X^r\bigl(X^{d(q-1)}+a\bigr)
\]
induces a permutation on \(\mathbb F_{q^2}\). Then:

1. \(\gcd(r,q-1)=1\), hence \(r\) is odd;
2. if \(a\ne0\), then \(a\) is a square in \(\mathbb F_{q^2}\);
3. writing \(\operatorname{sgn}(f)\in\{-1,1\}\) for the ordinary parity of the permutation of all \(q^2\) field elements, one has
\[
\boxed{\operatorname{sgn}(f)=(-1)^{(r-1)/2}.}
\]

In particular, the parity depends only on \(r\bmod4\), not on the admissible coefficient, base field, or even-index exponent \(d\). The theorem includes the monomial case \(a=0\) when it is a permutation. It is a conditional theorem: it does not claim that every coefficient yields a permutation.

## Assumptions and scope

Let \(F=\mathbb F_{q^2}\), \(H=\mathbb F_q^*\), and \(U=\{t\in F^*:t^{q+1}=1\}\). These are cyclic groups of orders \(q-1\) and \(q+1\), respectively. The power map \(F^*\to U\), \(x\mapsto x^{q-1}\), has kernel \(H\). The assumption \(\gcd(d,q+1)=2\) implies \(q+1=2m\) for \(m=(q+1)/2\) and the map \(t\mapsto t^d\) on \(U\) is exactly two-to-one onto \(\mu_m\), the subgroup of order \(m\). No restriction on the characteristic beyond oddness and no restriction on \(r\) beyond positivity are imposed initially.

## Proof

**Step 1: cosetwise exponent rigidity.** For each \(x\in F^*\) and \(u\in H\), one has \(f(ux)=u^r f(x)\). Since \(f\) is injective and no nonzero \(x\) can map to zero, the map \(u\mapsto u^r\) is injective on \(H\). Hence \(\gcd(r,q-1)=1\) and \(r\) is odd.

Fix a primitive element \(\zeta\in F^*\), set \(\omega=\zeta^{q+1}\) (a generator of \(H\)), and choose representatives \(x_j=\zeta^j\) for \(j=0,1,\ldots,q\) of the \(q+1\) cosets of \(H\). Because \(f\) is bijective, it permutes those cosets, say by \(\sigma\), and acts on their fiber coordinates as
\[
f(x_ju)=x_{\sigma(j)}c_j u^r,
\qquad c_j=\frac{f(x_j)}{x_{\sigma(j)}}\in H.
\]

**Step 2: the block-sign identity.** Reordering \(q+1\) blocks each of even size \(q-1\) has sign \(\operatorname{sgn}(\sigma)^{q-1}=1\). The same fiber power permutation \(u\mapsto u^r\) occurs in each of the even number \(q+1\) of blocks, so all its signs cancel. Multiplication by an element \(c\in H\) acts on the cyclic group \(H\) with sign \(\chi_q(c)\), the quadratic character of \(\mathbb F_q\) (a direct cycle decomposition, or the elementary multiplication-sign lemma). Thus
\[
\operatorname{sgn}(f)=\prod_{j=0}^q\chi_q(c_j)
=\chi_q\!\left(\prod_{j=0}^q c_j\right).
\]
Here the zero element is fixed and contributes no sign.

The product of the fiber scalars is, by permutation of the denominator representatives,
\[
\prod_{j=0}^{q}c_j
=\zeta^{(r-1)q(q+1)/2}
\prod_{t\in U}(t^d+a).
\]
Since \(t\mapsto t^d\) maps \(U\) twice onto \(\mu_m\),
\[
\prod_{t\in U}(t^d+a)
=\left(\prod_{v\in\mu_m}(v+a)\right)^2
=\bigl(a^m-(-1)^m\bigr)^2.
\]
Write \(b=a^m\) and \(\varepsilon=(-1)^m\in\mathbb F_q^*\). Since \(r\) is odd, the first scalar in the preceding product is \(\omega^{q(r-1)/2}\in H\). But the entire product of the \(c_j\) lies in \(H\); therefore \((b-\varepsilon)^2\in\mathbb F_q^*\), and in particular \(b\ne\varepsilon\).

**Step 3: the known square-class condition, derived directly.** If \(a\ne0\) were a nonsquare in \(F\), then
\[
b^{q-1}=a^{(q^2-1)/2}=-1,
\qquad b^q=-b.
\]
The field-membership condition just obtained would imply
\[
(b-\varepsilon)^2=((b-\varepsilon)^2)^q
=(-b-\varepsilon)^2,
\]
so \(4b\varepsilon=0\), impossible in odd characteristic with \(b\varepsilon\ne0\). Thus \(a=0\) or \(a\) is a square in \(F\). In either case, \(b^q=b\), so \(b\in\mathbb F_q\) and \((b-\varepsilon)^2\) is a nonzero square in \(H\).

**Step 4: exact parity.** Consequently,
\[
\operatorname{sgn}(f)
=\chi_q\!\left(\omega^{q(r-1)/2}(b-\varepsilon)^2\right)
=(-1)^{q(r-1)/2}
=(-1)^{(r-1)/2},
\]
because \(q\) is odd. This proves all assertions. \(\square\)

## Verification

The accompanying standalone script `verify_finite.py` implements finite fields of orders \(9,25,49,81,121\) exactly, including the two-level extension used for the \(q=9\) case. It independently enumerates candidate coefficients, two-to-one exponents and coprime power exponents; for every actual permutation it computes the sign from its cycle decomposition and tests both the predicted sign and coefficient-square condition. The tested base-field orders are \(q=3,5,7,9,11\); the successful run compared \(8313\) candidate maps and \(1142\) actual permutations, including \(94\) admissible monomial cases. Finite checks are independent diagnostics, **not** an infinite proof; Steps 1–4 establish the theorem for every odd prime power.

Reproduce using `python3 verify_finite.py` with Python standard library only; the expected output begins `ODD_Q_INDEX_TWO_PARITY_OK`.

## Relationship to prior work

Tang and Fan's November 10, 2026 preprint classifies permutation binomials \(X^r(X^{2(q-1)}+a)\) and explains how to transfer the classification to \(\gcd(d,q+1)=2\). The present theorem addresses a different invariant: the **sign of the induced permutation**, for all permissible coefficients at once. In particular, Lemma 2.2 of Tang–Fan already establishes the square-class restriction for nonzero coefficients; this supporting fact is **not** claimed as new here. We give a direct derivation to make the signature argument self-contained. It needs no casewise classification of those coefficients and includes the sporadic quadratic-extension cases. Fan's preceding classification covers the coprime-index family \(X^r(X^{q-1}+a)\), whose index is \(1\) rather than \(2\); it does not imply this theorem. The standard coset-permutation criterion and elementary multiplication-sign formula are established tools; novelty is claimed only for their sharp consequence for the new two-to-one index family, not for the underlying block-sign method.

An accessible full-text treatment of general quadratic-extension cyclotomic permutation mappings is Ding and Zieve (2023). A later account by Feng and Wang (2026) treats permutation polynomials of index \(q+1\). Neither accessed material supplied this coefficient-uniform two-to-one sign law. The full 26-page motivating manuscript was accessible in a PDF text rendering; its main theorems, Corollary 1.4, Lemma 2.2, relevant sections and full-text search matches were inspected. Its classification and coefficient-square lemma do not state the induced-permutation signature. No direct sign or cycle-parity theorem was found; an unindexed broader theorem remains a residual risk.

## Limitations

The theorem applies only to odd \(q\), quadratic extensions, and indices satisfying \(\gcd(d,q+1)=2\). It assumes the polynomial is already a permutation, and does not count how many coefficients qualify or classify their cycles. It does not claim an extension to characteristic two, higher extension degrees, or other common divisors. The inspiring manuscript's full text was available for a direct comparison; its coefficient-square lemma is prior work, not a new contribution. Unindexed or more general parity theorems remain an originality risk. All computational checks cover only explicitly stated finite fields.

## References

- Z. Tang and X. Fan, *A complete classification of permutation binomials of the form \(X^r(X^{2(q-1)}+a)\) over finite fields*, arXiv:2611.14162, first posted November 10, 2026. https://arxiv.org/abs/2611.14162
- X. Fan, *A complete classification of permutation binomials of the form \(X^r(X^{q-1}+a)\) over finite fields*, arXiv:2609.20354, first posted September 17, 2026. https://arxiv.org/abs/2609.20354
- X.-D. Hou and V. Pallozzi Lavorante, *A General Construction of Permutation Polynomials of \(\mathbb F_{q^2}\)*, arXiv:2204.01545 (2022). https://arxiv.org/abs/2204.01545
- Z. Ding and M. E. Zieve, *Determination of a class of permutation quadrinomials*, Proc. London Math. Soc. 127 (2023), 221–260, doi:10.1112/plms.12540. https://doi.org/10.1112/plms.12540
- H. Bian, S. Chen and D. Zheng, *Cycle structures and parities of linearized permutation polynomials*, arXiv:2610.11574 (2026). https://arxiv.org/abs/2610.11574
