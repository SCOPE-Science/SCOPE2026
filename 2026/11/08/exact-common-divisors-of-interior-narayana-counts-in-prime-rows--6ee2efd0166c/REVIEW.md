# Review of the prime-row Narayana gcd classification

## Correctness

**PASS.** The proof checks the precise domain \(p\) odd prime and \(2\le k\le p-1\). The base identity is \(\mathcal N(p,k)=p^{-1}\binom pk\binom p{k-1}\). Both binomials have exactly one factor \(p\), leaving exactly one in every interior Narayana number. The entry at \(k=2\) bounds all other possible common prime factors by those of \(p-1\). For each odd \(\ell\mid p-1\), a specified interior witness \(k=\ell^{\nu_\ell(p-1)}+1\) is nonzero modulo \(\ell\), by Lucas's theorem. When the odd part of \(p-1\) exceeds one, the analogous binary witness is odd. When \(p=2^r+1\), all remaining binary valuations are calculated explicitly and minimized, with equality witnesses. These steps establish all exponents of the gcd. The checker independently computes exact rows for primes up to \(257\). Risk: finite computation alone cannot certify the general prime-index theorem; the proof supplies the general argument.

## Originality

**PASS within the stated archival search limits.** Bóna–Sagan's 2005 result concerns divisibility of individual Narayana numbers by a prime and includes the weaker fact that prime-power-indexed rows have divisible interior entries. It does not supply the exact gcd or higher binary exponents. The accessible descriptions of Eu–Liu–Yeh's 2006 congruence work and OEIS A335965's odd-entry census do not state this classification. Targeted source searches for interior-row gcd, Fermat primes and Narayana valuations found no covering statement. The closest prior theorem is compared by logical implication, not title similarity. Residual risk: an equivalent exact gcd formula may occur in less easily located literature; the full text of the Eu–Liu–Yeh paper was not obtained, although its available abstract has a different emphasis.

## Mathematical value

**PASS.** The full gcd of the interior Narayana row is the maximal modulus that divides every nontrivial peak-counting statistic for Dyck paths of a fixed prime semilength. This is the exact higher-power strengthening naturally suggested by prime-divisibility results: the common factor is almost always just the row prime, but at the Fermat primes it gains a sharply bounded extra power of two. The exact exceptions distinguish a natural arithmetic subclass and are not supplied by the older prime-divisibility theorem. No general classification of composite rows is claimed.

Self-review: passed. Independent audit: not yet performed.
