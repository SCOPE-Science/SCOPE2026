# A forbidden Motzkin–trinomial ratio modulo thirteen and exact laws at zero-free primes

## Finding

Let \(T_n=[x^0](x^{-1}+1+x)^n\) be the central trinomial coefficient and \(M_n\) the classical Motzkin number. For any odd prime \(p\) with \(T_d\not\equiv0\pmod p\) for every \(0\le d<p\), every \(T_n\) is a unit modulo \(p\); the normalized Motzkin values
\[
R_p(n)=M_nT_n^{-1}\pmod p\qquad(n\ge0)
\]
have an explicit, finitely computable complete residue image and a rational natural-density law, given below. Each allowed residue occurs infinitely often, and the count of every residue up to an arbitrary cutoff \(N\) differs from its prescribed density times \(N\) by \(O_p(1+\log(N+1))\).

The first striking instance is \(p=13\). In this case the **exact** image is
\[
\boxed{\{R_{13}(n):n\ge0\}=\{0,1,2,3,4,5,6,7,8,9,10,12\}.}
\]
In particular, \(M_n\not\equiv11T_n\pmod{13}\) for **every** nonnegative integer \(n\), whereas every other ratio occurs infinitely often. Write \(H_k(r)=\#\{0\le n<13^k:R_{13}(n)=r\}\) for \(k\ge1\). Define vectors indexed by \(r=0,1,\ldots,12\):
\[
\begin{aligned}
F&=(0,2,0,0,0,2,0,2,2,0,0,0,3),\\
G&=(2,2,2,4,3,0,2,2,2,2,2,0,1),\\
E&=(1,0,1,0,0,0,0,0,0,0,0,0,0).
\end{aligned}
\]
Then every ternary-free thirteen-power block has the exact full histogram
\[
\boxed{H_k(r)=13^{k-1}F_r+\frac{13^{k-1}-1}{12}G_r+E_r\quad(k\ge1).}
\]
In particular, the limiting probabilities in residue order \(0,\ldots,12\) are
\[
\boxed{(\nu_{13}(r))_{r=0}^{12}=\frac1{156}(2,26,2,4,3,24,2,26,26,2,2,0,37).}
\]

## Assumptions and scope

The first statement applies to every **odd prime** \(p\) satisfying the displayed zero-free digit condition; it does not assert any formula for primes with a vanishing central-trinomial digit. The values \(T_n,M_n\) are the standard integer sequences with \(T_0=T_1=M_0=M_1=1\). All inverses in congruences are taken in \(\mathbb F_p\). The notation \(\nu_p(r)\) here denotes a residue frequency, **not** a prime-adic valuation. The exact block histogram is specific to \(p=13\), not to arbitrary primes.

For the universal law, let \(w_d=T_d\bmod p\), \(0\le d<p\); put \(v_s=w_{s+1}w_s^{-1}\) for \(0\le s<p-1\), and \(A(u)=\#\{s:v_s=u\}\) for \(u\in\mathbb F_p^\times\). Set \(c=w_{p-1}^{-1}\), necessarily \(c\in\{1,-1\}\) by the classical last-digit identity \(T_{p-1}\equiv(-3)^{(p-1)/2}\pmod p\). Define
\[
\mu(u)=\begin{cases}
A(u)/(p-1),&c=1,\\
\bigl(pA(u)+A(-u)\bigr)/(p^2-1),&c=-1.
\end{cases}
\]
For \(0\le d<p-2\) and \(u\in\mathbb F_p^\times\), define
\[
\begin{aligned}
h_d&=(3w_d+2w_{d+1}-w_{d+2})(2w_d)^{-1},\\
f(u)&=(3w_{p-2}+2w_{p-1}-u)(2w_{p-2})^{-1},\\
g(u)&=(3w_{p-1}+u)(2w_{p-1})^{-1}.
\end{aligned}
\]
The general theorem asserts that for every \(r\in\mathbb F_p\),
\[
\boxed{\nu_p(r)=\frac1p\#\{0\le d<p-2:h_d=r\}
+\frac1p\sum_{u\in\mathbb F_p^\times}\mu(u)
\bigl(\mathbf1_{f(u)=r}+\mathbf1_{g(u)=r}\bigr).}
\]
Its positivity set is exactly the complete infinite-index image of \(R_p\). These are finite formulas involving only the first \(p\) central trinomial coefficients.

## Proof

**1. Published congruence inputs.** The Lucas congruence for the central trinomial sequence gives
\[
T_{pm+d}\equiv w_dT_m\pmod p\quad(0\le d<p).
\]
This also follows immediately by applying the freshman's dream to \((x^{-1}+1+x)^{pm+d}\), since the exponents of the second factor lie strictly between \(-p\) and \(p\). Thus \(T_n\equiv\prod_iw_{d_i}\not\equiv0\) for the base-\(p\) digits \(d_i\) of \(n\), under the zero-free hypothesis. The classical identity, used explicitly in Kohen's work, is
\[
2M_n=3T_n+2T_{n+1}-T_{n+2}.
\]
Both identities hold for all nonnegative indices. In particular, no modular division by zero occurs.

**2. A complete carry-ratio classification.** Put \(U(m)=T_{m+1}T_m^{-1}\pmod p\). Splitting \(m=pq+s\), Lucas congruence gives
\[
U(pq+s)=\begin{cases}v_s,&s\le p-2,\\cU(q),&s=p-1.\end{cases}
\]
Every nonnegative integer has finitely many trailing digits \(p-1\) followed by some digit \(s\le p-2\) (allowing leading zeros), so the image of \(U\) is exactly \(\bigcup_{j\ge0}c^j\{v_0,\ldots,v_{p-2}\}\). A specified trailing-digit cylinder of length \(j+1\) has natural density \(p^{-(j+1)}\). For each fixed residue \(u\), summing the resulting geometric distribution gives \(\mu(u)\), with the two displayed cases when \(c=\pm1\). Each cylinder has infinitely many members, so every value with positive \(\mu\) occurs infinitely often.

The cylinder counts have discrepancy at most one per complete congruence class and length. For cutoffs \(X\), summing the errors over \(j\le\lceil\log_p(X+1)\rceil\) and observing that at most one smaller index has a longer run of maximal digits gives \(\#\{m<X:U(m)=u\}=\mu(u)X+O_p(1+\log(X+1))\). This statement includes arbitrary cutoffs, not only full digit blocks.

**3. Push the carry law through Motzkin ratios.** Writing \(n=pq+d\) in the Motzkin identity and applying Lucas congruence at offsets zero, one and two yields the pointwise identity
\[
R_p(pq+d)=\begin{cases}
h_d,&0\le d\le p-3,\\
f(U(q)),&d=p-2,\\
g(U(q)),&d=p-1.
\end{cases}
\]
The final case uses \(w_0=w_1=1\). Every fixed digit position has density \(1/p\); the two boundary positions inherit the law \(\mu\). Counting full groups of \(p\) indices and adding at most \(p-1\) leftovers proves the formula for \(\nu_p\) and the uniform-in-cutoff \(O_p(1+\log(N+1))\) discrepancy. Every positive term in the formula has an infinite cylinder of witnessing indices, while a zero term cannot occur at any index. This proves the all-prime assertion.

**4. Exact base-thirteen evaluation.** Integer central-trinomial values give
\[
(w_0,\ldots,w_{12})=(1,1,3,7,6,12,11,3,2,6,9,4,1)\pmod{13}.
\]
Thus \(c=1\), and the successive unit ratios are
\[
(v_0,\ldots,v_{11})=(1,3,11,12,2,2,5,5,3,8,12,10).
\]
Their image is \(V=\{1,2,3,5,8,10,11,12\}\). The eleven fixed-digit outputs are
\[
(h_0,\ldots,h_{10})=(1,1,5,8,8,5,7,12,12,7,12).
\]
The two boundary maps simplify to \(f(u)=5(1-u)\) and \(g(u)=7(3+u)\) modulo thirteen. Neither fixed outputs nor \(f(V),g(V)\) contain eleven: \(f(u)=11\) would require \(u=4\), and \(g(u)=11\) would require \(u=6\), neither in \(V\). Direct evaluation of the displayed finite sets shows every other residue does occur; infinitely many indices witness each such residue by Step 2.

For \(k\ge1\), set \(L=k-1\). Among \(0\le q<13^L\), each of the twelve ratios \(v_s\) occurs in each cylinder with \(j=0,\ldots,L-1\) trailing maximal digits exactly \(13^{L-j-1}\) times. The single remaining index, with all \(L\) digits equal to twelve, has \(U(q)=1\), because \(w_{12}=1\). Thus the weighted boundary-output histogram is \(G(13^L-1)/12+E\), where \(G\) counts \(f(v_s),g(v_s)\) with multiplicity and \(E\) counts \(f(1),g(1)\); the \(p-2\) fixed outputs contribute \(13^LF\). Evaluating them gives exactly the three stated vectors and the boxed all-level formula. Dividing by \(13^k\) and letting \(k\to\infty\) gives \((12F+G)/156\). All counts are integers because \(13^L-1\) is divisible by twelve.

## Verification

The reproducible standard-library script `verify_ratio.py` builds 2,501 **independent exact integer terms** of both sequences from their recurrences, checks the full integer Motzkin/trinomial relation, verifies the Lucas digital product and pointwise quotient rule against integer data for seven zero-free odd primes, recomputes the complete base-thirteen finite vectors, and independently enumerates all ratio values for the complete cutoffs \(13\), \(169\), \(2197\), and \(28561\) using digit products and the original three-term identity rather than the proposed \(f,g\) maps. It reported:

`VERIFY_OK independent_integer_terms=2501 direct_modular_ratios=all_admissible_primes`

`prime_samples= 7 p13_complete_power_levels=4 p13_max_index= 28560 forbidden_ratio=11`

The all-prime, all-index proof is in the preceding section; these finite tests do not replace it.

## Relationship to prior work

The base-\(p\) Lucas factorization and the Motzkin/central-trinomial identity are **pre-existing** results, not new assertions. Kohen (2024) derives zero-density formulas for generalized Motzkin numbers and symmetry laws for central trinomial coefficients. Kohen (2024) also analyzes uniform recurrence, and Rampersad–Shallit (2022) describe modular automata and congruences. Earlier separate research gives all-lag central-trinomial pair distributions modulo five and consecutive Motzkin pair distributions modulo five; these cover neither the general normalized-quotient law for all zero-free primes nor the explicit thirteen-modulus obstruction and complete thirteen-power histogram. In particular, simply computing individual Motzkin zero frequencies does not provide the thirteen separate quotient frequencies or the exclusion of the linear congruence \(M_n\equiv11T_n\pmod{13}\). This theorem uses their established inputs and adds the complete carry-ratio pushforward and its exact first explicit non-full quotient spectrum.

## Limitations

The all-prime theorem is conditioned on nonvanishing of the first \(p\) central-trinomial residues; no division is asserted at excluded primes. The block histogram, missing ratio and displayed density vector concern modulus thirteen, not thirteen-powers or arbitrary primes. The discrepancy constant may depend on \(p\); no sharp error constant is asserted. All priority conclusions concern examined sources: implicit equivalent material in the existing general automata framework, other unpublished tables, or unindexed work remains possible. This result has not undergone independent scientific audit.

## References

1. N. Kohen, *Density and Symmetry in the Generalized Motzkin Numbers mod p*, arXiv:2411.03681, first public 2024-11-06, https://arxiv.org/abs/2411.03681.
2. N. Kohen, *Uniform Recurrence in the Motzkin Numbers and Related Sequences mod p*, arXiv:2403.00149, first public 2024-02-29, https://arxiv.org/abs/2403.00149.
3. N. Rampersad and J. Shallit, *Congruence Properties of Combinatorial Sequences via Walnut and the Rowland–Yassawi–Zeilberger Automaton*, arXiv:2110.06244, https://arxiv.org/abs/2110.06244.
4. E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin Numbers and Related Sequences*, arXiv:math/0407326, https://arxiv.org/abs/math/0407326.
5. J.-C. Liu, *Supercongruences Involving Motzkin Numbers and Central Trinomial Coefficients*, arXiv:2208.10275, https://arxiv.org/abs/2208.10275.
6. *All-lag two-point laws and exact logarithmic bias for central trinomial residues modulo five*, published research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-all-lag-two-point-laws-and-exact-logarithmic-bias-for-central-tr--fa9f646a7cb7/RESULT.md.
7. *Complete consecutive-residue law for Motzkin numbers modulo five*, published research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-complete-consecutive-residue-law-for-motzkin-numbers-modulo-five--7159a644b09a/RESULT.md.
