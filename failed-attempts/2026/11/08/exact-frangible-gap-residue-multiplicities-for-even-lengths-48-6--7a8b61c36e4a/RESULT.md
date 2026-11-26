# Exact frangible-gap residue multiplicities for even lengths \(48\)–\(64\)

## Finding
For the endpoint-coprime local frangible-gap residue classes defined below, the nine hitherto bounded values at even gap lengths \(48\le h\le64\) are exactly:

| Even gap length | \(\lvert\Omega(h)\rvert\) |
| ---: | ---: |
| \(48\) | \(270657148848\) |
| \(50\) | \(101307938184\) |
| \(52\) | \(25051650260\) |
| \(54\) | \(4828555093560\) |
| \(56\) | \(952248263928\) |
| \(58\) | \(747162295398\) |
| \(60\) | \(49562298435088\) |
| \(62\) | \(673737239242910\) |
| \(64\) | \(870323053429248\) |

Together with the exact values already known through \(h=46\), the truncated local series has the exact reduced value
\[
 S_{64}:=\sum_{\substack{4\le h\le64\\2\mid h}}\frac{\lvert\Omega(h)\rvert}{\prod_{2<q<h,\ q\,\mathrm{prime}}(q-2)}
 =\frac{61370211356863231369}{29555095284933631875}
 =2.0764680595750968\ldots.
\]
Both the nine counts and this rational truncation are unconditional exact integer and rational identities.

## Assumptions and scope
For any even integer \(h\ge4\), let \(P_h\) be the product of the primes \(p<h\). Define \(\Omega(h)\) to consist of those residue classes \(b\pmod{P_h}\) satisfying
\[
 \gcd(b,P_h)=\gcd(b+h,P_h)=1,
 \qquad \gcd(b+j,P_h)>1\quad (1\le j<h).
\]
The definition counts residue classes, not actual pairs of consecutive primes. The result is confined to the nine specified lengths; published exact results for shorter lengths enter only the computation of \(S_{64}\).

## Proof
Let \(E_h=\{2,4,\ldots,h-2\}\) and \(m=h/2-1\). The modulus includes the prime \(2\); endpoint coprimality forces \(b\) odd. Consequently \(b+j\) is even and automatically covered for each odd \(j\). It remains to require every even \(j\in E_h\) to be divisible by at least one odd prime \(p<h\).

For each subset \(T\subseteq E_h\) and each odd prime \(p<h\), put
\[
 R_p(T)=\{0,-h\}\cup\{-j:j\in T\}\pmod p,
 \qquad A_p(T)=p-\lvert R_p(T)\rvert.
\]
By the Chinese remainder theorem, exactly \(\prod_{3\le p<h,\ p\,\mathrm{prime}}A_p(T)\) residue classes obey the endpoint coprimality conditions while simultaneously avoiding divisibility by every listed \(b+j\), \(j\in T\). (The residue modulo \(2\) is uniquely fixed.) Inclusion–exclusion over the coverage events therefore proves
\[
 \boxed{\lvert\Omega(h)\rvert=\sum_{T\subseteq E_h}(-1)^{\lvert T\rvert}\prod_{\substack{3\le p<h\\p\,\mathrm{prime}}}\bigl(p-\lvert R_p(T)\rvert\bigr).}
\]
This formula holds for every even \(h\ge4\), without a hypothesis about prime distribution.

For \(h\le64\), \(m\le31\) and every odd prime involved is at most \(61\). The provided `verifier.cpp` represents each \(R_p(T)\) by a \(64\)-bit residue mask and evaluates the full inclusion–exclusion sum. It partitions the \(m\) interior positions into two halves, precomputes the union masks for each half, and enumerates all \(2^m\) subsets; in particular, the final case includes all \(2^{31}\) subsets. It uses signed \(128\)-bit integer arithmetic. Every absolute summand is bounded by \(\prod_{3\le p<64}(p-1)\), so the sum of their absolute values is bounded by \(2^{31}\prod_{3\le p<64}(p-1)<2^{105}<2^{127}\), and intermediate sums cannot overflow signed \(128\)-bit arithmetic.

Exact outputs of the exhaustive computation are tabulated above. Substitution of these nine counts and the published, independently reproduced counts through \(46\) into the rational definition of \(S_{64}\), followed by exact fraction reduction, gives the displayed numerator and denominator.

## Verification
Compile using `g++ -std=c++17 -O3 verifier.cpp -o verify_omega` and run `./verify_omega 4 64`. The output is reproduced in `counts.csv`. It agrees exactly with every one of the \(22\) published even-length values from \(4\) through \(46\), and each of the nine newly computed values lies strictly between the corresponding published lower and upper bounds.

An independent Gray-code implementation, `gray_check.cpp`, maintains prime-residue occupancy counters and revisits the inclusion–exclusion sum in a distinct order; a full independent run agreed on every new case from \(48\) through \(64\). Both implementations evaluate every one of the \(2^{31}\) subsets at length \(64\).

For the rational series, divide each exact value by its corresponding product \(\prod_{2<q<h}(q-2)\) and add exact fractions; the resulting reduced fraction is shown above.

## Relationship to prior work
Mossinghoff and Trudgian, *Frangible prime gaps*, arXiv:2610.34525v1, §2 and Table 1, give the exact coefficients only for even \(h\le46\). Their §3 and Table 2 give lower and upper bounds rather than exact counts for precisely the nine even \(h=48,50,\ldots,64\) values determined here. Their displayed interval for the truncated series was \(2.076468035<\sum_{h\le64}c_h<2.076469131\). The exact rational value above replaces that particular uncertainty, not the tail. The new method reorganizes the same local finite sieve as inclusion–exclusion over interior positions, instead of enumerating all endpoint residue classes.

Gafni and Tao, *Rough numbers between consecutive primes*, arXiv:2508.06463v1, supply the broader asymptotic framework and the conditional constant; Uğurdoğan, *Multiplicity Constants for Rough Numbers in Prime Gaps*, arXiv:2610.10582v1, treats more general rough-number multiplicities, not the nine exact entries of the bounded local table.

## Limitations
The counts and finite rational truncation are unconditional, but the predicted asymptotic density of frangible prime gaps remains conditional on the Dickson–Hardy–Littlewood prime-tuples conjecture. These calculations do not determine the infinite tail \(\sum_{h>64}c_h\), the exact full constant \(c\), or any counts for larger \(h\). The computation is an exhaustive finite certificate, not a proof of an unrelated infinite arithmetic statement. An equivalent computation in unindexed earlier material cannot be excluded by bibliographic searches alone.

## References
1. Michael J. Mossinghoff and Timothy S. Trudgian, *Frangible prime gaps*, arXiv:2610.34525v1, October 25, 2026, §§2–3, Tables 1–2, https://arxiv.org/html/2610.34525v1 .
2. Ayla Gafni and Terence Tao, *Rough numbers between consecutive primes*, arXiv:2508.06463v1, August 8, 2025, https://arxiv.org/abs/2508.06463 .
3. Bahar Uğurdoğan, *Multiplicity Constants for Rough Numbers in Prime Gaps*, arXiv:2610.10582v1, October 6, 2026, https://arxiv.org/abs/2610.10582 .
