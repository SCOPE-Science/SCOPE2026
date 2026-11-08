# First-interaction law for sparse shifts in odd-prime binomial valuations

## Finding

Let \(p\ge 3\) be a prime. Fix \(s\ge 2\), integer positions \(0\le a_1<\cdots<a_s\), and nonzero base-\(p\) digits \(1\le d_i\le p-1\). Put
\[
 t=\sum_{i=1}^{s}d_ip^{a_i},\qquad
 g=\min_{1\le i<s}(a_{i+1}-a_i),\qquad
 V_t(n)=\nu_p\!\binom{n+t}{t}.
\]
For each \(r\ge0\), the natural density
\[
 D_t(r)=\lim_{X\to\infty}\frac1X\#\{0\le n<X:V_t(n)=r\}
\]
exists. Define a digit-local probability generating function
\[
 G_d(z)=\frac{p-d}{p}+\frac{d(p-1)z}{p^2(1-z/p)},\qquad
 Q_t(z)=\prod_{i=1}^{s}G_{d_i}(z).
\]
Then **the first departure from independent digit-local carry counts occurs exactly at the smallest gap**:
\[
 D_t(r)=[z^r]Q_t(z)\quad(0\le r<g),
\]
whereas
\[
 \boxed{\displaystyle
 D_t(g)=[z^g]Q_t(z)-\sum_{\substack{1\le i<s\\a_{i+1}-a_i=g}}
 \frac{d_id_{i+1}}{p^{g+2}}
 \prod_{\substack{1\le j\le s\\j\notin\{i,i+1\}}}\frac{p-d_j}{p}.}
\]
Every summand in the correction is strictly positive. Equivalently, the actual generating function agrees with \(Q_t(z)\) through degree \(g-1\), and has a strictly smaller coefficient in degree \(g\). This simultaneously gives an exact independent-product law for every valuation \(r\le R\) if all successive digit gaps exceed \(R\), and proves the uniform separation requirement cannot be weakened.

For example, when \(p=3\) and \(t=1+3\), the actual densities in valuations zero and one are \(4/9\) and \(7/27\); the independent product predicts \(4/9\) and \(8/27\). At \(p=5\) with \(t=1+2\cdot5^2\), the actual density at valuation two is \(74/625\), rather than \(76/625\).

## Assumptions and scope

The parameter \(t\) is fixed while \(n\to\infty\) in natural density. The prime \(p\) is odd; digit amplitudes \(d_i\) may vary and include \(p-1\); positions and gaps are unrestricted apart from strict increase. The result concerns the **fixed lower binomial argument** \(t\) in \(\binom{n+t}{t}\), not a complete row of Pascal's triangle. All rational probabilities are exact. No uniform density error estimate with growing \(t\) is claimed.

## Proof

**1. Density and carry normalization.** By Kummer's theorem, \(V_t(n)\) equals the number of carries when adding \(t\) to \(n\) in base \(p\). The base-\(p\) digits of a uniformly chosen nonnegative integer modulo a large power of \(p\) are independent and uniformly distributed. To have exactly \(r\) carries, no carry may persist above position \(a_s+r\): each upward step of a carry contributes at least one to the count, and all nonzero digits of \(t\) occur at or below \(a_s\). Thus the event \(V_t(n)=r\) is a union of residue classes modulo \(p^{a_s+r+2}\). Its natural density exists and equals its finite-digit probability. Since an infinite carry chain requires an infinite string of maximal digits, an event of probability zero, the densities sum to one.

**2. Single-position law.** Add one digit \(dp^a\), where \(1\le d<p\), to an independent uniform digit string. With probability \((p-d)/p\) the digit at position \(a\) does not initiate a carry. To obtain exactly \(j\ge1\) carries requires one of \(d\) initiating digits, then \(j-1\) consecutive digits equal to \(p-1\), followed by one of \(p-1\) terminating digits. Therefore
\[
 \Pr(L_d=0)=\frac{p-d}{p},\qquad
 \Pr(L_d=j)=\frac{d(p-1)}{p^{j+1}}\quad(j\ge1),
\]
whose generating function is \(G_d(z)\).

**3. All degrees below the minimum gap.** Add the shifted nonzero digit summands sequentially from lower to higher positions, and let \(L_i\) be the number of carries caused by summand \(d_ip^{a_i}\) at the stage it is added. The base-\(p\) digit-sum identity, or Kummer's theorem applied to each stage and then telescoped, gives \(V_t(n)=\sum_i L_i\) exactly. Consider any pattern with total \(r<g\). Every carry chain is shorter than \(g\), so it stops before the next active position. The digit intervals determining these chains are disjoint; earlier additions do not modify the digits subsequently examined. Such patterns therefore have the independent probabilities obtained by multiplying the single-digit laws. Conversely, a configuration with total at most \(r\) cannot contain a chain crossing an active-position gap of length at least \(g\). Summing over all partitions of \(r\) gives \(D_t(r)=[z^r]Q_t(z)\).

**4. The first interaction.** At total carry count \(g\), any discrepancy from independence must come from a carry chain starting at \(a_i\) that reaches the immediately following active position \(a_{i+1}\), and the intervening gap must equal \(g\). This uses all \(g\) permitted carries, so every other active digit has zero carries. Two distinct such interactions cannot occur at this degree. Write \(a=d_i\), \(b=d_{i+1}\), and consider this single minimal-gap pair. For exactly \(g\) lower carries and no upper carry in the true simultaneous addition, the lower initiating digit has \(a\) choices, the intervening \(g-1\) digits must all equal \(p-1\), and the upper digit must lie in \(\{0,\ldots,p-b-2\}\) to stop the incoming carry without creating another. Hence the true pair contribution is
\[
 \frac{a(p-b-1)}{p^{g+1}}.
\]
In the formally independent model the lower chain has \(g\) carries with probability \(a(p-1)/p^{g+1}\), and the upper digit has zero carries with probability \((p-b)/p\). Their product exceeds the true contribution by
\[
 \frac{a(p-1)(p-b)}{p^{g+2}}-\frac{a(p-b-1)}{p^{g+1}}=\frac{ab}{p^{g+2}}.
\]
This accounts for the complete difference at degree \(g\); all other local digit events have zero carry, contributing the factors \((p-d_j)/p\) for \(j\ne i,i+1\). Summation over minimal-gap pairs proves the boxed identity. Its correction is strictly positive since all digits are nonzero. \(\square\)

## Verification

The standalone script `verify.py` implements an exact finite-state carry automaton and computes each probability as a reduced rational number. It independently computes the predicted product, its first-defect correction, and eight complete residue-period censuses using actual binomial coefficients and exact prime valuations. Run `python verify.py` with an ordinary Python 3 installation. Verified output:

```
VERIFY_OK multidigit_cases=81 exact_rational_coefficients=243 complete_modulus_binomial_censuses=8 strict_first_defects=yes
```

The scripts test finitely many cases. The unrestricted theorem follows from the carry-cylinder counting proof above, not from those tests.

## Relationship to prior work

Kummer's classical theorem identifies prime-adic binomial valuations with carry counts; this equivalence is not new. Cheng (2026) and Sobolewski--Spiegelhofer (2024) investigate fixed-shift binary digit-sum distributions and their correlation laws. The sparse-binary-ones independent-carry law is also known and is **not** part of the novelty claimed here. The new claim concerns odd primes, arbitrary nonzero digit amplitudes, and the universal **first non-independent coefficient**, including its exact strictly negative pairwise correction.

Rowland's matrix formula (2017/2018), building on Barat--Grabner (2001), counts valuations across each **fixed binomial row** as the lower argument varies. That does not directly give the density across \(n\) with the lower argument \(t\) held fixed. The earlier general tools may inspire alternative derivations, and a historical equivalent in the broad digit-transducer literature remains possible.

## Limitations

This is a fixed-shift natural-density theorem and not a uniform count for shifts growing with the sampling cutoff. No independence claim is made beyond the first interaction degree. The 2001 Barat--Grabner article's abstract and its precise use in Rowland's full text were inspected, but its original full text could not be obtained for direct section-by-section comparison. That access gap leaves residual priority uncertainty. Independent mathematical validation has not occurred.

## References

1. K. Cheng, *A first-exit proof of Cusick's sum-of-digits conjecture*, arXiv:2606.23398, first posted 22 June 2026, https://arxiv.org/abs/2606.23398.
2. B. Sobolewski and L. Spiegelhofer, *Decomposing the sum-of-digits correlation measure*, arXiv:2411.07779, first posted 12 November 2024, https://arxiv.org/html/2411.07779v1.
3. E. Rowland, *A matrix generalization of a theorem of Fine*, arXiv:1704.05872, first posted 19 April 2017, https://arxiv.org/html/1704.05872v2.
4. G. Barat and P. J. Grabner, *Distribution of binomial coefficients and digital functions*, J. London Math. Soc. 64 (2001), 523--547, DOI:10.1112/S0024610701002630.
5. E. E. Kummer, classical carry-count interpretation of prime-adic binomial valuations (1852), as discussed in references 2--4.
