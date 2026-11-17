# Arithmetic support and sharp rare-idempotent asymptotics in monomial evolution algebras

## Finding
Fix a prime power \(q\). For each \(n\ge1\), select a uniformly random permutation \(\sigma\in S_n\) and independent uniformly random weights \(a_1,\ldots,a_n\in\mathbb F_q^\times\). Let \(E_n\) be the evolution algebra on the natural basis \(e_1,\ldots,e_n\) defined by \(e_i e_j=0\) for distinct indices and \(e_i^2=a_i e_{\sigma(i)}\). Its structure matrix is monomial and invertible. Write \(p_n(q)\) for the probability that \(0\) is its **only** idempotent element, and set \(p_0(q)=1\).

Write \(m\) for the odd part of \(q-1\). If \(m=1\), then \(p_n(q)=0\) for every \(n\ge1\). If \(m>1\), let \(L=\operatorname{ord}_m(2)\), and set
\[
 g_j=\gcd(2^j-1,m),\qquad
 a_j=1-\frac1{g_j},\qquad
 b_d=\sum_{e\mid d}\mu(d/e)a_e\quad(d\mid L).
\]
Then the exact ordinary probability generating series is the **finite cyclotomic product**
\[
 \boxed{\sum_{n\ge0}p_n(q)z^n
 =\prod_{d\mid L}(1-z^d)^{-b_d/d}.}
\]
For each distinct odd prime \(r\mid m\), put \(h_r=\operatorname{ord}_r(2)\) and let \(D=\gcd_{r\mid m}h_r\). The exact positive support is
\[
 \boxed{p_n(q)>0\ \Longleftrightarrow\
 n=\sum_{r\mid m,\ r\text{ prime}}k_rh_r
 \text{ for some integers }k_r\ge0.}
\]
In particular, \(p_n(q)=0\) whenever \(D\nmid n\), and \(p_n(q)>0\) for every sufficiently large multiple of \(D\).

Define
\[
 \beta=\frac1L\sum_{j=1}^L a_j
 =\sum_{d\mid L}\frac{b_d}{d},\qquad
 C=\prod_{d\mid L}d^{-b_d/d}.
\]
These satisfy \(0<\beta<1\) and \(C>0\). Along every sequence of integers \(n\to\infty\) with \(D\mid n\),
\[
 \boxed{p_n(q)\sim \frac{D C}{\Gamma(\beta)}n^{\beta-1}.}
\]
The factor \(D\), which accounts for equally dominant roots of unity, cannot in general be discarded.

For instance, over \(\mathbb F_{16}\),
\[
 \sum_{n\ge0}p_n(16)z^n=(1-z^2)^{-1/3}(1-z^4)^{-1/15},\quad
 \beta=\frac25,\quad D=2.
\]
Over \(\mathbb F_{64}\),
\[
 \sum_{n\ge0}p_n(64)z^n
 =(1-z^2)^{-1/3}(1-z^3)^{-2/7}(1-z^6)^{17/189},
 \quad\beta=\frac{100}{189},\quad D=1.
\]
Hence the probability is positive in **every dimension \(n\ge2\)** for the latter field, and it decays with leading power \(n^{-89/189}\). In contrast, over \(\mathbb F_{16}\) it vanishes in every odd dimension and, along even dimensions, decays with leading power \(n^{-3/5}\).

## Assumptions and scope
The field order \(q\) is fixed while \(n\to\infty\). Probability is uniform on **labeled monomial structure matrices**, equivalently on the independent permutation-and-weight choices above. It is not uniform over isomorphism classes and not uniform over all invertible matrices. Idempotent means an algebra element \(x\) with \(x^2=x\); the zero element always qualifies. Fractional powers are defined by their Taylor series at \(z=0\).

## Proof
**1. The cycle event.** If \(x=\sum_i x_i e_i\), the equation \(x^2=x\) reads \(x_{\sigma(i)}=a_i x_i^2\) for each \(i\). Along a \(\sigma\)-cycle of length \(\ell\), the coordinates are all zero or all nonzero. Going once around the cycle produces \(x_i^{2^\ell-1}=B^{-1}\), where \(B\in\mathbb F_q^\times\) is a product of the original weights with positive integral exponents and includes one weight to the first power. Consequently \(B\) is uniform over \(\mathbb F_q^\times\). Since that multiplicative group is cyclic, the equation has \(g_\ell=\gcd(2^\ell-1,q-1)\) nonzero solutions with probability \(1/g_\ell\), and no nonzero solution otherwise. Weight sets on disjoint cycles are independent. Thus, conditional on the permutation, the probability of no nonzero idempotent is \(\prod_{c}(1-1/g_{|c|})\).

**2. Cycle index and finite product.** The exponential formula for permutations, with each \(\ell\)-cycle weighted by \(a_\ell=1-1/g_\ell\), gives
\[
 \sum_{n\ge0}p_n(q)z^n=\exp\Big(\sum_{\ell\ge1}\frac{a_\ell z^\ell}{\ell}\Big).
\]
As \(2^\ell-1\) is odd, \(g_\ell=\gcd(2^\ell-1,m)\). If \(m=1\), every \(a_\ell=0\), proving the first case. Otherwise \(g_\ell\) depends only on \(\gcd(\ell,L)\): for each odd prime power \(r^s\mid m\), divisibility of \(2^\ell-1\) by \(r^s\) is equivalent to \(\operatorname{ord}_{r^s}(2)\mid\ell\), and this order divides \(L\). Möbius inversion on divisors of \(L\) therefore yields \(a_\ell=\sum_{d\mid L,\ d\mid\ell}b_d\). Substitution gives
\[
 \sum_{\ell\ge1}\frac{a_\ell z^\ell}{\ell}
 =\sum_{d\mid L}\frac{b_d}{d}\sum_{k\ge1}\frac{z^{dk}}{k}
 =-\sum_{d\mid L}\frac{b_d}{d}\log(1-z^d),
\]
proving the finite product.

**3. Exact support.** Here \(a_\ell>0\) precisely when some odd prime \(r\mid m\) divides \(2^\ell-1\), equivalently \(h_r\mid\ell\). The exponential permutation expansion has nonnegative coefficients, so \([z^n]\exp(\sum_{\ell\ge1}a_\ell z^\ell/\ell)>0\) exactly when \(n\) is a sum of allowed lengths. Such a sum is also, and conversely, a nonnegative combination of the \(h_r\): replace any allowed length by copies of a suitable divisor \(h_r\). The elementary numerical-semigroup argument then gives eventual positivity on multiples of their gcd \(D\).

**4. Asymptotics and competing roots.** The only possible singularities of the finite product on the unit circle are the \(L\)-th roots of unity. Near \(z=1\), \(1-z^d\sim d(1-z)\), whence
\[
 F(z)=C(1-z)^{-\beta}(1+O(1-z))
\]
with the stated \(C\) and \(\beta\). Since the periodic sequence \((a_j)\) has a positive entry and all its entries are strictly less than one, \(0<\beta<1\).

At a root \(\xi^L=1\), the local singular exponent is
\[
 \theta_\xi=\frac1L\sum_{j=1}^L a_j\xi^j.
\]
Its real part is at most \(\beta\), with equality precisely when \(\xi^j=1\) for every \(j\) with \(a_j>0\), i.e. precisely when \(\xi^D=1\). At these \(D\) roots the exponent equals \(\beta\), and the support statement implies \(F(\xi z)=F(z)\); their local leading coefficients are therefore all \(C\), in corresponding local coordinates. At every other root, the real part of the exponent is strictly smaller. The standard coefficient transfer for algebraic singularities at finitely many roots of unity then gives
\[
 [z^n]F(z)=\frac{C}{\Gamma(\beta)}n^{\beta-1}
 \sum_{\xi^D=1}\xi^{-n}+o(n^{\beta-1}).
\]
On multiples of \(D\) the root sum equals \(D\). Off that progression the coefficients vanish **exactly** by Step 3. This proves the asymptotic claim. No assertion of an optimal error term is made.

**5. Field specializations.** For \(q=16\), the odd part of \(q-1\) is \(15\), the period is \(4\), and the positive divisor coefficients are \(b_2=2/3\), \(b_4=4/15\). For \(q=64\), the odd part is \(63\), the period is \(6\), and the nonzero divisor coefficients are \(b_2=2/3\), \(b_3=6/7\), \(b_6=-34/63\). They give the displayed products. The allowed lengths \(2\) and \(3\) for the latter field generate all integers at least two.

## Verification
The accompanying dependency-free `verify.py` performs literal finite-field arithmetic to enumerate every monomial algebra and solve its idempotence equations in the cases \(\mathbb F_4\) with dimensions \(1\) through \(4\), \(\mathbb F_8\) with dimensions \(1\) through \(3\), and \(\mathbb F_{16}\) with dimensions \(1\) through \(2\). It independently computes the probability coefficients through dimension \(28\) using (i) the logarithmic-derivative recurrence and (ii) finite-product series multiplication for twelve valid field orders. The two routes agree exactly as rational numbers. Numerical coefficients at dimension \(1200\) illustrate the limiting constant in the \(\mathbb F_{16}\) and \(\mathbb F_{64}\) cases; their convergence can be slow due to secondary root-of-unity terms. The program ends with `VERIFY_OK`. Finite verification does not replace Step 4.

## Relationship to prior work
Wei and Zou (arXiv:2310.12368, first public version October 18, 2023, primary MSC 17D92) study classification and finite-field isomorphism-class counts for nonsingular evolution algebras; that is a different probability space and invariant. Narkuziyev (arXiv:2005.05793, May 9, 2020) analyzes evolution algebras associated with permutations and particular idempotent equations, but does not give this all-field rare-event asymptotic. The general theory of cycle-weighted random permutations and singularity methods is well established; the new assertion here is the arithmetic support and explicit all-field leading exponent and coefficient for this particular algebraic rare event.

An earlier calculation for the **same uniform monomial ensemble** already established the cycle-by-cycle idempotent-count law, integer moment generating functions, and the complete \(q=4\) specialization. None of those are claimed as new. The present result adds the exact support semigroup and sharp asymptotic constants for *all* fixed finite fields, including the coprime-length interaction visible over \(\mathbb F_{64}\). It follows from, but is not explicitly contained in, the earlier exact finite-cycle law; its additional ingredient is the analysis of competing root-of-unity singularities. This derivation may be considered a natural analytic continuation of that existing work rather than an independent classification theorem.

## Limitations
The theorem does not concern uniformly sampled invertible structure matrices, isomorphism-class sampling, or field orders varying with dimension. The full cycle-level random-idempotent law is previous knowledge; novelty is restricted to the support and general sharp asymptotics. This work has not established publication priority against all possible singularity-analysis or monomial-dynamical-system results, and no independent mathematical audit has been performed.

## References
1. Yangjiang Wei and Yi Ming Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023), https://arxiv.org/abs/2310.12368.
2. B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793 (2020), https://arxiv.org/abs/2005.05793.
3. Nicolas Robles and Dirk Zeindler, *Random permutations with logarithmic cycle weights*, arXiv:1806.04700 (2018), https://arxiv.org/abs/1806.04700. Used as background on cycle weights and singularity methods, not as a source of the specific algebraic formula.
4. Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapter VI (multiple-singularity transfer).
