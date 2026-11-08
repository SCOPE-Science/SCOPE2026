# An exact random-idempotent law for weighted-permutation evolution algebras

## Finding

For every prime power \(q\ge2\) and integer \(n\ge1\), independently choose a uniform permutation \(\sigma\in S_n\) and uniform nonzero weights \(a_1,\ldots,a_n\in\mathbb F_q^\times\). Form the perfect evolution algebra with natural basis \(e_1,\ldots,e_n\), distinct-basis products zero and \(e_i^2=a_i e_{\sigma(i)}\). Let \(I_{n,q}\) count **all** \(\mathbb F_q\)-rational idempotents, including zero, and set

\[
d_\ell(q)=\gcd(2^\ell-1,q-1),\qquad
m_{\ell,q}(u)=1+\frac{(1+d_\ell(q))^u-1}{d_\ell(q)}.
\]

The following exact **moment transform**, valid for every real or complex \(u\), determines the complete law of \(I_{n,q}\):

\[
\boxed{\sum_{n\ge0}\mathbb E[I_{n,q}^{u}]z^n=
\exp\!\left(\sum_{\ell\ge1}\frac{m_{\ell,q}(u)}{\ell}z^\ell\right).}
\]

For an entirely finite expression of the individual probabilities, let \(\boldsymbol m=(m_1,m_2,\ldots)\) range over sequences of nonnegative integers with \(\sum_{\ell\ge1}\ell m_\ell=n\). Then, for every positive integer \(j\),

\[
\boxed{\begin{aligned}
\Pr(I_{n,q}=j)=
\sum_{\boldsymbol m:\,\sum\ell m_\ell=n}
\left(\prod_{\ell\ge1}\frac{1}{\ell^{m_\ell}m_\ell!}\right)
\sum_{0\le k_\ell\le m_\ell}
\left(\prod_{\ell\ge1}
{m_\ell\choose k_\ell}
\frac{(d_\ell(q)-1)^{m_\ell-k_\ell}}{d_\ell(q)^{m_\ell}}\right)
\mathbf1\!\left\{j=\prod_{\ell\ge1}(1+d_\ell(q))^{k_\ell}\right\}.
\end{aligned}}
\]

Only finitely many factors differ from one. In the finite probability formula, the combinatorial convention \(0^0=1\) applies when a cycle family has probability one of contributing nonzero idempotents. All possible values lie in \(\{1,\ldots,2^n\}\). In particular, for every field size and positive dimension,

\[
\boxed{\mathbb E[I_{n,q}-1]=n,\qquad
\sum_{n\ge0}\mathbb E[I_{n,q}^2]z^n=
\exp\!\left(\sum_{\ell\ge1}\frac{d_\ell(q)+3}{\ell}z^\ell\right).}
\]

The first genuinely field-sensitive case \(q=4\) admits a sharper closed form. The idempotent count is always a power of two, so let \(H_n=\log_2 I_{n,4}\) (a nonnegative integer). Its **complete** probability-generating function is

\[
\boxed{\sum_{n\ge0}\mathbb E[t^{H_n}]z^n=
\left(\frac{1+z}{1-z}\right)^{t/2}
(1-z^2)^{-(2+t^2)/6}.}
\]

Consequently the probability that the algebra has **no nonzero idempotent** is zero in odd dimension, while for \(n=2m\ge2\) it is exactly

\[
\boxed{\Pr(I_{2m,4}=1)=\frac{(1/3)_m}{m!}
\sim\frac{m^{-2/3}}{\Gamma(1/3)},}
\]

where \((u)_m=u(u+1)\cdots(u+m-1)\). The second moment and variance in this field satisfy

\[
\boxed{\sum_{n\ge0}\mathbb E[I_{n,4}^2]z^n=\frac1{(1-z)^5(1+z)},\qquad
\operatorname{Var}(I_{n,4}-1)=\frac{n^4}{48}+O(n^3).}
\]

By contrast, if \(q-1\) is a power of two, \(I_{n,q}=2^{c(\sigma)}\) deterministically conditional on the permutation, where \(c(\sigma)\) is its number of cycles; here \(\Pr(I_{n,q}=2^k)={n\brack k}/n!\), with unsigned Stirling numbers of the first kind.

## Assumptions and scope

The probability space consists of exactly \(n!(q-1)^n\) **labeled** weighted-permutation structure matrices with equal mass, not algebra-isomorphism classes. All their weights are nonzero, so the matrices are invertible and their evolution algebras perfect. Idempotents are counted over the coefficient field, not over an algebraic closure. The variable \(t\) in the quaternary formula records the binary logarithm of the idempotent count, **not** the count itself; \(u\) in the moment transform is an arbitrary complex exponent. All displayed power series in \(z\) are formal, although the asymptotic follows from an analytic coefficient estimate. The identity for \(n=0\) uses the convention \(I_{0,q}=1\) only to simplify generating functions.

## Proof

**Cycle reduction.** Fix a permutation and its disjoint cycle \(C=(i_0,i_1,\ldots,i_{\ell-1})\), with \(\sigma(i_j)=i_{j+1}\) cyclically. If \(x=\sum_i x_i e_i\) is idempotent, comparison of natural-basis coefficients gives

\[
x_{\sigma(i)}=a_ix_i^2\quad\text{for every }i.
\]

Following the cycle yields \(x_{i_j}=A_jx_{i_0}^{2^j}\), where \(A_0=1\) and \(A_{j+1}=a_{i_j}A_j^2\). Thus

\[
A_\ell=\prod_{j=0}^{\ell-1}a_{i_j}^{2^{\ell-1-j}},
\qquad x_{i_0}=A_\ell x_{i_0}^{2^\ell}.
\]

A cycle either contributes the all-zero vector or a nonzero root of \(X^{2^\ell-1}=A_\ell^{-1}\); every choice of this root uniquely propagates along that cycle. Distinct cycles have disjoint coordinates, so their numbers of choices multiply.

**Uniform multiplicative obstruction.** Conditional on the permutation, the weights on different cycles remain independent. In the above product, the final weight \(a_{i_{\ell-1}}\) has exponent exactly one. Holding the others fixed therefore makes \(A_\ell\) uniform in the cyclic group \(\mathbb F_q^\times\), and the \(A_\ell\) for different cycles are independent. The power homomorphism \(u\mapsto u^{2^\ell-1}\) has kernel of size \(d_\ell(q)\) and image of index \(d_\ell(q)\). With probability \(1/d_\ell(q)\) the cycle has exactly \(d_\ell(q)\) nonzero solutions, and otherwise none. Hence its number of idempotent choices is \(1+d_\ell(q)\) or \(1\), with those respective probabilities. For every exponent \(u\), its expected \(u\)-th power is exactly \(m_{\ell,q}(u)\).

**Cycle-index assembly.** For any sequence of formal weights \(v_\ell\), the standard labeled permutation cycle index gives

\[
\sum_{n\ge0}\frac{z^n}{n!}\sum_{\sigma\in S_n}
\prod_{C\in\operatorname{Cyc}(\sigma)}v_{|C|}
=\exp\!\left(\sum_{\ell\ge1}v_\ell\frac{z^\ell}{\ell}\right).
\]

Since the **total** number of idempotents is a **product** of independent cycle contributions, its \(u\)-th power is the product of their \(u\)-th powers. Taking \(v_\ell=m_{\ell,q}(u)\) proves the moment-transform identity. The transform determines the full probability distribution, because \(I_{n,q}\) is a positive integer bounded by \(2^n\), and distinct exponentials \(j^u\) are linearly independent as functions of \(u\). Alternatively, condition on the permutation cycle multiplicities \(m_\ell\). For each \(\ell\), the number \(k_\ell\) of cycles admitting nonzero idempotents is binomial with parameters \(m_\ell\) and \(1/d_\ell(q)\). The permutation cycle-type probability is \(\prod_\ell (\ell^{m_\ell}m_\ell!)^{-1}\); multiplying these probabilities proves the displayed finite law without an inversion step.

In particular, \(\mathbb E[Y_\ell]=2\) and \(\mathbb E[Y_\ell^2]=d_\ell(q)+3\), where \(Y_\ell\) is the number of solutions on one cycle. The mean follows from \(\exp(\sum_{\ell\ge1}2z^\ell/\ell)=(1-z)^{-2}\).

**Quaternary specialization.** For \(q=4\), \(d_\ell(4)=1\) when \(\ell\) is odd and \(d_\ell(4)=3\) when \(\ell\) is even. The cycle idempotent counts are \(2\) on an odd cycle and either \(1\) or \(4\) on an even cycle (with probabilities \(2/3\) and \(1/3\)). Thus \(H_n=\log_2 I_{n,4}\) is a **sum** of cycle contributions, respectively \(1\) and a random variable in \(\{0,2\}\). Its cycle probability-generating polynomials are \(t\) and \((2+t^2)/3\), respectively. Using the cycle-index identity and the formal logarithm sums

\[
\sum_{\ell\ \mathrm{odd}}\frac{z^\ell}{\ell}=\frac12\log\frac{1+z}{1-z},
\qquad\sum_{\ell\ \mathrm{even}}\frac{z^\ell}{\ell}=-\frac12\log(1-z^2)
\]

prove the closed generating function of \(H_n\), and therefore the full law of \(I_{n,4}\). To have only the zero idempotent, each cycle must have just its zero solution. This is impossible for an odd cycle; thus only even cycles contribute, each with probability \(2/3\). The probability-generating function in \(z\) for this event is

\[
\exp\!\left(\frac23\sum_{\ell\ \mathrm{even}}\frac{z^\ell}{\ell}\right)=(1-z^2)^{-1/3}.
\]

The generalized binomial theorem gives \(\Pr(I_{2m,4}=1)=(1/3)_m/m!\); the gamma ratio asymptotic gives the displayed decay. Since the conditional squared moments are \(4\) for odd cycles and \(6\) for even cycles, the second-moment series becomes

\[
\exp\!\left(4\sum_{\ell\ \mathrm{odd}}\frac{z^\ell}{\ell}+6\sum_{\ell\ \mathrm{even}}\frac{z^\ell}{\ell}\right)
=\frac{1}{(1-z)^5(1+z)}.
\]

At \(z=1\), the dominant pole has order five with leading factor \(1/2\), so \(\mathbb E[I_{n,4}^2]=n^4/48+O(n^3)\). Subtracting \((n+1)^2\) establishes the variance law. Finally, if \(q-1\) has no odd prime divisor, then every odd number \(2^\ell-1\) is coprime to \(q-1\). Hence each cycle contributes exactly two choices and the distribution reduces to that of the number of cycles of a uniform permutation, counted by unsigned Stirling numbers.

## Verification

The accompanying standalone Python checker constructs all \(n!(q-1)^n\) weighted-permutation algebras in each small test case, exhaustively enumerates all \(q^n\) vectors to count rational idempotents, and independently compares the observed histogram to the cycle-index law using exact rational arithmetic. It includes finite fields of orders \(4\) and \(8\), represented by explicit irreducible binary polynomials, rather than only prime fields. The completed checks cover \(21\) parameter pairs and \(6,559\) distinct structure matrices, including characteristics two, three, five and seven. They also independently check the universal mean. The recorded terminal line is `VERIFY_OK cases=21 matrices=6559`.

Reproduce with `python3 verify.py`. All computations are finite corroborations. The proofs above, not the finite enumerations, establish the arbitrary-field-size and arbitrary-dimension statements.

## Relationship to prior work

The survey of Kaygorodov, Martín González and Viruel (first submitted October 15, 2026) motivates distributional questions about idempotents of random perfect evolution algebras, especially for graph-constrained ensembles. Its whole-matrix sampling model differs from the monomial-matrix model here. Narkuziyev's earlier permutation-algebra work explicitly solves the idempotent equation along one permutation cycle and describes decomposition into cycles; those per-cycle structural facts are **not new here**. The new assertions are the uniform-weight probability law over all cycle lengths and permutations, its universal moments, and the exact quaternary zero-idempotent probability and fourth-order variance growth. Costoya–Mayorga–Viruel study automorphism/permutation representations of perfect evolution algebras rather than this random idempotent law.

The probability law may be derivable by combining older individual-cycle formulas with classical symmetric-group cycle indexing; this limits the historical novelty claim. No checked primary source or mathematical research record explicitly states the full weighted-permutation law or the quaternary asymptotics. Search failure by itself cannot establish priority.

## Limitations

The result applies only to uniformly weighted **monomial** evolution-algebra matrices. It does not determine the law for all invertible matrices, for triangular matrices, or for uniformly sampled algebra isomorphism classes. It distinguishes rational idempotents over \(\mathbb F_q\), not geometric idempotents over an algebraic closure. The original per-cycle idempotent formulas are previously known, and historical noncoverage of every possible prior combinatorial reformulation has not been established. No independent mathematical audit has been performed.

## References

1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first submitted 2026-10-15), https://arxiv.org/abs/2610.22248.
2. B. A. Narkuziyev, *On absolute nilpotent and idempotent elements of an evolution algebra corresponding to permutations*, arXiv:1803.11415 (2018), https://arxiv.org/abs/1803.11415. Author-uploaded complete text: https://www.researchgate.net/publication/324150680_On_absolute_nilpotent_and_idempotent_elements_of_an_evolution_algebra_corresponding_to_permutations.
3. B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793 (2020), https://arxiv.org/abs/2005.05793, later *Journal of Algebra and Its Applications* 21 (2022), 2250112, https://doi.org/10.1142/S0219498822501122.
4. C. Costoya, P. Mayorga, A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, *Mediterranean Journal of Mathematics* 22 (2025), 149, https://doi.org/10.1007/s00009-025-02924-0.
