# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/041`  
**Audit date (UTC):** 2026-09-24  
**Audited public head:** `5955a8f60269c6348a34bbedae9058725ac12f48`  
**Audited source-tree SHA:** `3926471381997b2ce7529e2d28fa6fd535f0fa91`  
**RESULT.md blob:** `475f6c7b096c6d1d1489e2423bd57ae251108405`  
**Reviewer:** separate AI independent audit for the SCOPE three-axis campaign.

## Scope and claim extracted

The record proves two existential statements about largest denominators of distinct-unit-fraction representations of 1. First, it constructs infinitely many odd integers that occur as the largest denominator of an expansion using distinct odd denominators. Second, it proves that no prime power can be the strict largest denominator of any distinct Egyptian-fraction expansion of 1. The construction starts from an explicit 11-term odd expansion and repeatedly replaces the current maximum using one of two parity-dependent three-term identities.

## Correctness — PASS

I independently checked the proof algebraically and computationally.

The base set
`{3,5,7,9,15,21,27,35,63,105,135}`
sums exactly to 1. For every odd `k >= 3` the two displayed splitting formulas are identities:

- if `k = 3 (mod 4)`, with `m=(3k+1)/2`, then `1/k = 1/(3k)+1/m+1/(3km)`;
- if `k = 1 (mod 4)`, with `m=3(k+1)/2` and `c=3k(k+1)/2=km`, then `1/k = 1/(3k)+1/m+1/c`.

In each case all three new denominators are odd, pairwise distinct, and strictly larger than `k`. Therefore replacing the current maximum preserves the exact sum, oddness, and distinctness while forcing a strictly larger maximum. Exact rational replay gives the stated maxima
`135, 82215, 30417001335, 4163372866005888522015, 78001531296273387817009252900320853961254035`.

The prime-power obstruction is also correct. Let the strict maximum be `M=p^a`, and let `L` be the lcm of all denominators. No smaller denominator has `p`-adic valuation `a`, so `L/M` is a unit mod `p`, whereas `L/d` is divisible by `p` for every other denominator `d`. Clearing denominators in `1=sum 1/d` gives `L=sum L/d`, which is `0 = nonzero (mod p)`, a contradiction.

## Originality — FAIL

Both headline existential conclusions are already covered by stronger prior results.

For the odd-denominator side, Christian Elsholtz, **“Egyptian Fractions with odd denominators”**, arXiv:1606.02117 / Q. J. Math. 67 (2016), studies the number `S(k)` of representations
`sum_{i=1}^k 1/x_i = 1`
with the `x_i` distinct odd positive integers. The paper's introduction and Corollary 1.2 give a doubly-exponential positive lower bound for all sufficiently large odd `k`. In particular, such representations exist for arbitrarily large `k`. Because `k` distinct odd denominators greater than 1 force the largest denominator to be at least `2k+1`, their maxima are unbounded; hence infinitely many odd integers already occur as largest denominators. This strictly covers the record's part (a) existential theorem, although the record gives a different elementary construction and explicit sample maxima. Elsholtz also cites earlier odd-denominator existence/counting work, so this is not a newly opened existence regime.

For the obstruction side, Greg Martin's **“Denser Egyptian Fractions”** discusses the Erdős–Graham largest-denominator problem, and the full text explicitly states that Erdős and Graham had already observed that a prime power can never be the largest denominator in an Egyptian-fraction representation of 1. OEIS A260402, the sequence of integers that cannot be the largest denominator of an Egyptian fraction for 1, likewise explicitly notes that it contains all primes and prime powers and cites Martin. Thus part (b) is established prior art, not a new obstruction theorem.

Searches included `largest denominator Egyptian fractions prime power`, `odd distinct Egyptian fractions largest denominator`, `Egyptian fractions with odd denominators all odd lengths`, and exact variants around the displayed splitting identities. The decisive sources above were available through ordinary open access/arXiv; no institutional fallback was required.

## Scientific value — FAIL

After subtracting the prior results, the surviving content is an elementary alternative proof/construction and an explicit rapidly growing sequence of example maxima. The prime-power argument is a clean modular proof of an old observation; the odd splitting identities provide a concrete constructive route to a qualitative existence fact already implied by much stronger counting theorems.

These are pedagogically neat, but they do not sharpen the known exceptional-set asymptotics, improve the known odd-denominator counting bounds, classify which odd integers occur, or establish a new quantitative/structural regime. Under this campaign's requirement that a reproof or routine corollary have substantive residual scientific value, the remaining contribution is insufficient.

## Bounded repair attempt

The result can be honestly reframed as an elementary constructive exposition: the two identities generate an explicit infinite family of odd maxima, and the lcm argument gives a short proof of the classical prime-power obstruction. That repair would make the provenance accurate, but it would not create a new theorem or a meaningful improvement over the prior literature. A scientifically viable retry would need a genuinely stronger result, such as a classification/density theorem for odd attainable maxima or a quantitative improvement not implied by existing counting and largest-denominator results.

## Final disposition

- **Correctness:** passed.
- **Originality:** failed.
- **Scientific value:** failed.
- **Disposition:** **failed / withdraw from accepted findings**.

This is a prior-coverage/value rejection, not a claim that the displayed identities or modular proof are wrong. Historical files should be preserved in the failed-attempt archive.
