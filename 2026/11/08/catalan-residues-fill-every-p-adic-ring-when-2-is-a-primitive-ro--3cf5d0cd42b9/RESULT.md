# Catalan residues at primitive-root primes: a corrected block proof

## Finding

Let \(C_n=\binom{2n}{n}/(n+1)\). If \(p\) is an odd prime and \(2\) has multiplicative order \(p(p-1)\) modulo \(p^2\), then for every \(k\geq1\), the set \(\{C_n\bmod p^k:n\geq0\}\) is the entire ring \(\mathbb Z/p^k\mathbb Z\), and each residue occurs at infinitely many indices. Thus the set of Catalan values is dense in \(\mathbb Z_p\). The hypothesis holds for \(p=3,5,11\). It is sufficient, not claimed necessary, and no infinitude of such primes is asserted.

## Proof

Write \(B_n=\binom{2n}{n}\), \(h=(p+1)/2\), and \(v_p\) for the usual valuation. We first establish a large-block multiplication lemma; this replaces an incorrect fixed-window unit congruence in an earlier version of this argument.

**Lemma 1 (isolated addition of a large block).** For fixed integers \(a\ge0\), \(d\ge1\), and \(s\ge1\), if \(M=d p^T\) and \(T\) is sufficiently large in terms of \(a,s\), then
\[
\frac{B_{a+M}}{B_aB_M}\equiv1\pmod{p^s}
\]
in \(\mathbb Z_p\). Indeed, cancellation of the three factorial ratios gives the exact identity
\[
\frac{B_{a+M}}{B_aB_M}
=\frac{\prod_{i=1}^{2a}(1+2M/i)}{\prod_{i=1}^{a}(1+M/i)^2}.
\]
For \(T\ge s+\max_{1\le i\le2a}v_p(i)\), every factor on the right is a \(p\)-adic unit congruent to one modulo \(p^s\). The case \(a=0\) is immediate from the empty products. In particular, if \(B_M\) is a \(p\)-adic unit, \(v_p(B_{a+M})=v_p(B_a)\), and their normalized unit parts multiply to the claimed precision.

**Lemma 2 (primitive limiting unit).** Put \(u_T=B_{p^T}\). Kummer's theorem shows \(v_p(u_T)=0\). By cancellation of multiples of \(p\) in the factorials,
\[
\frac{B_{pN}}{B_N}=\prod_{\substack{1\le i\le pN\\p\nmid i}}\left(1+\frac{pN}{i}\right).
\]
With \(N=p^{T-1}\), each factor for \(T\ge2\) is congruent to one modulo \(p^T\), so \(u_T/u_{T-1}\equiv1\pmod{p^T}\). The sequence \(u_T\) therefore converges to a unit \(\gamma_p\in\mathbb Z_p^\times\). For \(T=1\), expansion of the same product gives
\[
\frac{u_1}{B_1}\equiv1+p\sum_{i=1}^{p-1}i^{-1}\equiv1\pmod{p^2},
\]
because inversion permutes the nonzero residues modulo \(p\) and their sum vanishes for odd \(p\). Consequently \(\gamma_p\equiv B_1=2\pmod{p^2}\). Under the hypothesis on \(2\), the standard primitive-root lifting theorem shows that \(\gamma_p\) generates \((\mathbb Z/p^s\mathbb Z)^\times\) for every \(s\ge1\). The limit assertion does **not** say \(B_{p^T}\equiv2\pmod{p^s}\) for every \(s\) and large \(T\); in general this is false once \(s>2\).

**Lemma 3 (prescribed initial valuation).** Fix \(k\ge1\). For any \(v\ge0\), take
\[
 n_v=\sum_{j=1}^{v}h p^{jL},\qquad L=2k+3
\]
(the empty sum is \(n_0=0\)). Each base-\(p\) digit \(h\) produces exactly one carry when doubling, and the next zero digit absorbs it. Kummer's theorem gives \(v_p(B_{n_v})=v\), while \(n_v\equiv0\pmod{p^k}\). The gaps between the digits and their precise length are not used in any claim of multiplicativity of their unit parts.

**Surjectivity and infinitely many witnesses.** Fix a target residue \(z\pmod{p^k}\). For nonzero \(z\), let \(v=v_p(z)<k\), and take the seed \(n_v\) of Lemma 3. The normalized unit \(u=B_{n_v}/p^v\) is invertible modulo \(p^{k-v}\). Since \(\gamma_p\) generates the units modulo that power, choose \(t\ge0\) with
\[
 \gamma_p^t\equiv (z/p^v)u^{-1}\pmod{p^{k-v}}.
\]
Successively add \(t\) blocks \(p^{T_1},\ldots,p^{T_t}\) to the index, with each exponent larger than all previous ones and large enough to apply Lemma 1 at precision \(k\) and Lemma 2 at precision \(k-v\). At every addition the old central binomial coefficient retains valuation \(v\), and its unit part is multiplied by \(\gamma_p\) modulo \(p^{k-v}\). The final index \(n\) remains divisible by \(p^k\), and hence
\[
 C_n=B_n/(n+1)\equiv p^v u\gamma_p^t\equiv z\pmod{p^k}.
\]
Appending further groups of \(\varphi(p^{k-v})\) widely separated blocks produces arbitrarily large indices with the same residue, because \(\gamma_p^{\varphi(p^{k-v})}\equiv1\pmod{p^{k-v}}\). For \(z=0\), start with \(n_k\) and append arbitrarily distant unit blocks: Lemmas 1 and 3 preserve its valuation \(k\), so all resulting Catalan values are zero modulo \(p^k\). Thus every residue occurs infinitely often, as required.

For the examples, \(2\) is primitive modulo \(3^2=9\), \(5^2=25\), and \(11^2=121\) (its respective orders are \(6,20,110\)); the lifting criterion applies at all higher powers.

## Verification and scope

The companion standard-library file `verify_catalan.py` tests actual Catalan residue coverage for bounded powers and indices, compares an independent modular factorial-unit evaluation with exact central binomial coefficients, checks the seed carry valuations and block-limit congruences, and includes a regression counterexample to the superseded fixed-window congruence. These checks corroborate the proof but cannot establish its infinite quantifiers; those follow from Lemmas 1–3 and unit generation. The arithmetic is entirely in the standard \(p\)-adic integer ring for odd primes.

## Relation to known work and limitations

Rowland–Yassawi, *Automatic congruences for diagonals of rational functions* (arXiv:1310.8635), analyze Catalan congruence automata and raise the no-forbidden-residue question at three-powers. Burns, *The Catalan numbers have no forbidden residue modulo primes* (arXiv:1703.02705), proves prime-modulus surjectivity, not every higher power. Published results for all three-power residues already cover the \(p=3\) specialization. Berend–Harmse, *On some arithmetical properties of middle binomial coefficients* (1998), establish unrestricted central-binomial \(p\)-adic density; this does not alone assert Catalan coverage at every prime power with the required index congruence. A separately developed all-odd-prime central-binomial index–value fiber theorem, in the contemporaneous research corpus, mathematically implies the present Catalan conclusion in even greater generality. Its recorded source commit follows that of this claim by 46 seconds and the two public records entered the same bulk publication commit; their substantial overlap remains a priority and publication-coordination risk, not a claim that the stronger theorem is an earlier source. The proof above avoids reliance on that stronger theorem.

This finding does not classify primes where full Catalan coverage holds, estimate minimal witness indices or index frequencies, establish uniformity of residue distributions, or prove that infinitely many primes satisfy the primitive-root hypothesis. The correction replaces a demonstrably false prime-power unit-block simplification; it does not assert that finite computations establish an unrestricted theorem. The record's earlier scientific history is preserved separately.
