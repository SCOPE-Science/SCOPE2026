# Quadratic dyadic contact for an odd-weight binomial-square transform

## Finding
For any integer \(t\equiv3\pmod4\), define the weighted central Delannoy/binomial-square transform
\[
F_n(t)=\sum_{j=0}^{n}\binom nj^2(2t)^j\qquad(n\ge0).
\]
For every positive integer \(n\) divisible by eight,
\[
\boxed{\nu_2(F_n(t)-1)=2\nu_2(n)+2.}
\]
The valuation is finite for every such \(n\). Thus the exact valuation spectrum on the indices divisible by eight is \(\{8,10,12,\ldots\}\), with valuation \(2r+2\) occurring at relative density \(2^{-(r-2)}\) within those indices, for each \(r\ge3\). Both the weight congruence class and the index threshold are material: at \(t=3,n=4\), one has \(F_4(3)=6145\), so the difference has valuation eleven rather than six. The ordinary central Delannoy specialization \(t=1\) has a different, cubic contact law already established in prior work.

## Assumptions and scope
The parameter \(t\) is any positive or negative integer with \(t\equiv3\pmod4\); \(n\in8\mathbb Z_{>0}\). The convention is \(\nu_2(2)=1\) and \(\nu_2(0)=+\infty\). For context, \(F_n(1)=\sum_j2^j\binom nj^2\) is the classical central Delannoy number. The polynomial family is also related to Legendre polynomials by
\[
F_n(t)=(1-2t)^nP_n\!\left(\frac{1+2t}{1-2t}\right),
\]
which is valid because \(1-2t\ne0\) for integral \(t\). Hence this is a natural one-parameter binomial-square deformation rather than an arbitrary collection of congruences.

## Proof
Put \(X=8Y\), with \(Y\in\mathbb Z_2\). For each \(j\ge1\), the polynomial identity
\[
\binom Xj=\frac{X}{j}(-1)^{j-1}\prod_{i=1}^{j-1}\left(1-\frac Xi\right)
\]
shows that
\[
F_{8Y}(t)=1+64Y^2\sum_{j\ge1}\frac{(2t)^j}{j^2}\prod_{i=1}^{j-1}\left(1-\frac{8Y}{i}\right)^2.
\tag{1}
\]
Every sum and product in this identity is an element of the appropriate 2-adic ring: for fixed \(Y\in\mathbb Z_2\), the series converges uniformly by the coefficient bound below; and for nonnegative integral \(X\), the terms vanish when \(j>X\), so (1) recovers the original finite binomial sum.

Define
\[
A(t)=\sum_{j\ge1}\frac{(2t)^j}{j^2}\in\mathbb Z_2.
\]
For every \(j\ge9\), \(j-2\nu_2(j)\ge3\), and for \(j=3,5,6,7\) the same inequality holds. Consequently, modulo eight only \(j=1,2,4,8\) contribute:
\[
A(t)\equiv2t+t^2+t^4+4t^8\equiv2t+6\equiv4\pmod8
\tag{2}
\]
when \(t\equiv3\pmod4\). Thus \(\nu_2(A(t))=2\).

We next establish that every coefficient of degree at least three in (1), as a power series in \(Y\), is divisible by \(512\). The \(j\)-th summand in (1) is
\[
64Y^2\frac{(2t)^j}{j^2}\prod_{i=1}^{j-1}\left(1-\frac{8Y}{i}\right)^2.
\]
For \(j\ge9\), every coefficient of this summand has valuation at least
\[
6+j-2\nu_2(j)-2\sum_{r\ge4}\left\lfloor\frac{j-1}{2^r}\right\rfloor.
\tag{3}
\]
Indeed, in each factor, negative coefficient valuations can come only from indices \(i\) with \(\nu_2(i)>3\), and their total possible loss is bounded by the final sum. Since \(\nu_2(j)\le j/4\) for \(j\ge9\) and the sum of the floors is at most \((j-1)/8\), (3) is at least \(6+(j+1)/4>8\). Moreover, this lower bound grows to infinity, verifying uniform convergence coefficientwise.

For \(1\le j\le8\), direct factor-wise bounds suffice, without any unproved cancellation. The minimum valuation of the prefactor \(64(2t)^j/j^2\) is respectively
\[
7,6,9,6,11,10,13,8.
\]
For \(j=1\) the product is constant. For \(j=2\), any nonconstant coefficient of \((1-8Y)^2\) has valuation at least four. For \(j=4\), every nonconstant coefficient of \(\prod_{i=1}^{3}(1-8Y/i)^2\) has valuation at least three. For \(j=8\), every nonconstant coefficient of the corresponding product has valuation at least one. For \(j=3,5,6,7\), the prefactor already has valuation at least nine and all product coefficients are integral. These statements exhaust the indices \(1\le j\le8\); therefore all coefficients of degree at least three in (1) lie in \(512\mathbb Z_2\). Since every summand has an explicit factor \(Y^2\), there exists a restricted series \(G_t(Y)\in\mathbb Z_2\langle Y\rangle\) with
\[
F_{8Y}(t)=1+64A(t)Y^2+512Y^3G_t(Y).
\tag{4}
\]
Write \(A(t)=4u\) with \(u\in\mathbb Z_2^\times\). For nonzero \(Y\in\mathbb Z_2\), the first nonconstant term in (4) has valuation \(8+2\nu_2(Y)\), whereas the last term has valuation at least \(9+3\nu_2(Y)\), strictly larger. Thus
\[
\nu_2(F_{8Y}(t)-1)=8+2\nu_2(Y)=2\nu_2(8Y)+2,
\]
proving the assertion for every indicated integer \(n\). The geometric relative densities follow from the elementary count of integers with prescribed binary valuation.

## Verification
Run `python3 verify.py` using Python 3 and only the standard library. The checker evaluates the binomial-square sum and a separate Legendre three-term recurrence, compares 945 value pairs, and checks the exact valuation law for 735 pairs with \(-41\le t\le41\), \(t\equiv3\pmod4\), and \(8\le n\le280\), \(8\mid n\). It also verifies the small coefficient valuations, the modulo-eight formula for \(A(t)\), the tail-bound arithmetic for \(9\le j\le4096\), and the explicit sharpness witness \((t,n)=(3,4)\). These are finite reproducibility checks only; the infinite result follows from the analytic estimates in the proof.

## Relationship to prior work
Sun's 2016/2018 work develops the full Delannoy polynomial \(D_n(x)=\sum_j\binom nj^2x^j(x+1)^{n-j}\) and integrality and odd-prime congruences of its sums. Our family is its transformed specialization \(F_n(t)=(1-2t)^nD_n(2t/(1-2t))\), but its sharp all-index, even-prime *difference-from-one* valuation on the indicated parameter class does not follow from those theorems as stated. Jia and Huang (2024) prove odd-integrality results for Delannoy–Schröder mixed sums and odd-prime congruences, not this two-parameter local valuation. Earlier exact dyadic contact analysis for the classical central Delannoy sequence covers the exceptional specialization \(t=1\), giving a cubic rather than quadratic contact order; it does not cover \(t\equiv3\pmod4\). The general theorem for valuations of generalized central trinomial coefficients concerns the valuations of the coefficients themselves, which are odd here, and does not settle the valuation of their *difference from one*. Thus the stated implication is not furnished by the inspected stronger results. These distinctions concern mathematical statements, not similarity of titles.

## Limitations
The result is restricted to \(t\equiv3\pmod4\) and \(8\mid n\). It does not classify the exceptional layer \(\nu_2(n)=2\), weights \(t\equiv1\pmod4\), or any odd-prime analogue. At \(t=3,n=4\), the proposed valuation formula fails, so the cutoff cannot simply be removed. Although exact and uniform for an infinite two-parameter family, this is a narrow 2-adic contact result and not a classification of the full residue image. Literature priority remains subject to unindexed or implicitly formulated older work.

## References
- Chen-Bo Jia and Jia-Qing Huang, *Congruences involving Delannoy numbers and Schröder numbers*, arXiv:2410.17522v1 (first public 2024-10-23), https://arxiv.org/html/2410.17522v1 .
- Zhi-Wei Sun, *Arithmetic properties of Delannoy numbers and Schröder numbers*, arXiv:1602.00574 (2016; journal 2018), https://arxiv.org/html/1602.00574v5 .
- Zhi-Wei Sun, *On Delannoy numbers and Schröder numbers*, arXiv:1009.2486 (2010), https://arxiv.org/abs/1009.2486 .
- *Exact dyadic contact orders of central Delannoy numbers with their alternating signs* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-dyadic-contact-orders-of-central-delannoy-numbers-with-the--56e382985cf4/RESULT.md .
- *Two-adic phases and a sharp boundary for generalized central trinomial coefficients* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-two-adic-phases-and-a-sharp-boundary-for-generalized-central-tri--835ab7526d97/RESULT.md .
