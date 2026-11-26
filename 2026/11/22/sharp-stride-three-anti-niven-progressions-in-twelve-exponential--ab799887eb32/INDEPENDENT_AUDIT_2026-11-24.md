# Independent mathematical audit

## correctness

PASS

Even terms require odd digit sums of their base-b quotients. Adding one without changing digit-sum parity requires an odd number of trailing b−1 digits, so the next quotient ends in zero and the following increment flips parity. With b≥6, successive even progression terms are spaced six apart and their quotients cannot skip a block. Hence they occupy at most two adjacent blocks, containing at most ceil(b/3) such even terms, proving the stated bound. For the listed seeds the carry in the low digit starts at one at j=1, runs through two, and reaches three only at the last term, with final remainder one. Subtraction of the digit sum gives (b−1) times U, U+2 and U+3 on these three cases. The factor b−1=3^k is harmless because every term is K modulo 3. Independently parsed the twelve rows from RESULT.md, checked the two endpoint gcds and prime-factor tests by trial division, and checked all 1,594,356 terms with exact gcd and base-b digit sums. The largest row has 1,062,885 terms. The low block stays below b^3 throughout; a common multiple of the multiplicative orders for primes dividing the finitely many digit sums and not dividing b preserves all relevant residues when shifting the leading one to b^m. Primes dividing b see both powers as zero. Arbitrarily large m preserve all gcds and give distinct starts.

## originality

PASS

Credit prior work on anti-Niven progressions and even-base odd-stride upper bounds; the pass concerns matching attainment certified for the twelve specified even bases, and the exact lifting of those witnesses. No available distinct statement implied these attainments. The modular lifting principle and parity obstruction are not assessed as independently new.

## value

PASS

The stride and base family are motivated by the even-base extremal problem and the identity b−1=3^k, which isolates one forced carry prime. This is a meaningful finite cutoff: the same small certificate shape works for twelve exponentially growing bases, including a maximal progression of over one million terms. The extension from a seed to infinitely many maximal starts shows more than existence of isolated computer hits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
