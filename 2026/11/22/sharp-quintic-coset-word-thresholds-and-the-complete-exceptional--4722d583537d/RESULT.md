# Sharp quintic coset-word thresholds and the complete exceptional-prime classification

## Finding
For primes \(p\equiv1\pmod5\), color nonzero residues by their fifth-power coset, relative to any primitive root. Let \(N_{\mathbf c}(p)\) count starting values \(x\in\mathbb F_p\) for which \(x,x+1,x+2\) are all nonzero and their ordered colors equal \(\mathbf c\in\{0,1,2,3,4\}^3\).

**Theorem.** Every one of the 125 words is realized if and only if \(p\) is not among the following 48 primes:

\[\{11,31,41,61,71,101,131,151,181,191,211,241,251,271,281,311,331,401,421,431,461,491,521,541,571,601,631,641,661,691,701,751,761,811,821,911,941,971,1181,1231,1291,1531,1811,1871,2311,2411,2731,3331\}.\]

The sharp all-word threshold is \(p=3361\): every eligible prime at least 3361 realizes all words, and the preceding eligible prime 3331 does not. More sharply, **all 124 words other than \((0,0,0)\)** occur for every eligible \(p\ge2341\); this is sharp since \(p=2311\) omits a mixed word. Exactly 43 primes omit at least one of those 124 words, namely

\[\{11,31,41,61,71,101,131,151,181,191,211,241,251,271,281,311,331,401,421,431,461,491,521,541,571,601,631,641,661,691,701,751,761,811,821,911,941,1181,1231,1291,1531,1871,2311\}.\]

At \(p=2311\), for the smallest primitive root, the two missing patterns are \((0,0,0)\) and \((2,0,2)\). At the remaining exceptional primes above 2311, namely 2411, 2731, and 3331, only \((0,0,0)\) is missing. The all-zero obstruction at 3331 was already known in classical literature; the complete mixed-color classification and its distinct sharp threshold are the focus here.

## Assumptions and scope
Let \(p\) be a prime with \(p\equiv1\pmod5\), and let \(g\) be an arbitrary generator of \(\mathbb F_p^\times\). Define \(\lambda_g(g^j)=j\bmod5\), and leave \(\lambda_g(0)\) undefined. A word is present only when all three values are nonzero, so the three excluded starting values are \(0,-1,-2\). A different primitive root permutes the four nonzero colors by multiplication modulo five and fixes zero; presence of all words, number of missing words and the distinction between all-zero and mixed words are therefore independent of \(g\). The single displayed mixed pattern \((2,0,2)\) uses the least primitive root.

## Proof
Fix a fifth-order complex character \(\chi\) with \(\chi(g)=\zeta\), where \(\zeta=e^{2\pi i/5}\). On \(\mathbb F_p^\times\), the indicator of color \(c\) is \(5^{-1}\sum_{a=0}^4\zeta^{-ac}\chi(u)^a\). Multiply three indicators and sum only over admissible starting values. The principal contribution to \(125N_{\mathbf c}(p)\) is \(p-3\).

For a nonzero exponent vector \(\mathbf a\in\{0,1,2,3,4\}^3\), let \(s\) be its number of nonzero components. The associated polynomial

\[P_{\mathbf a}(X)=X^{a_0}(X+1)^{a_1}(X+2)^{a_2}\]

has precisely \(s\) distinct roots, with nonzero multiplicities less than five, so it is not a fifth power. The Weil character-sum estimate (see Wu--Wei--Li, Lemma 2.1) gives \(\left|\sum_{x\in\mathbb F_p}\chi(P_{\mathbf a}(x))\right|\le(s-1)\sqrt p\). The restricted sum omits at most \(3-s\) additional points where the polynomial does not vanish; its magnitude is therefore at most \((s-1)\sqrt p+3-s\).

There are \(\binom{3}{s}4^s\) nonzero exponent vectors of support size \(s\). Hence the sum of absolute values of all nonprincipal contributions is at most

\[12\cdot2+48(\sqrt p+1)+64\cdot2\sqrt p=176\sqrt p+72.\]

Consequently, for every color word,

\[125N_{\mathbf c}(p)\ge p-176\sqrt p-75.\]

The right side is strictly positive for every real \(p\ge31126\). Every eligible prime at or above that bound therefore realizes every word. For the remaining eligible primes \(11\le p<31126\), the standalone finite checker enumerates the primes, finds a primitive root by the usual prime-factor criterion, colors each element by its discrete logarithm modulo five, computes the 125-bin histogram for every admissible \(x\), and reports all absent words. An independent second construction obtains the cosets by enumerating nonzero fifth powers and multiplying them by successive powers of the same generator. It checks equality of all element colors and all histograms, and exhausts all 836 eligible primes. Both enumerations produce exactly the two exception lists in the theorem and the specified boundary patterns. Combining the analytic cutoff with exhaustive finite enumeration proves the claims for all primes.

## Verification
Compile and execute the included program with `g++ -std=c++17 -O2 -Wall -Wextra verify_quintic.cpp -o verify_quintic && ./verify_quintic`. The program checks independent fifth-power-coset and discrete-log colorings, every one of the 125 counts for all 836 eligible primes below 31126, the 48 exceptional primes, the 43 mixed exceptions, and the critical patterns at 2311, 2341, 2411, 2731, 3331 and 3361. It also checks positivity of the analytic bound at 31126. No finite check is treated as an infinite proof: infinitude is resolved by the character-sum inequality.

## Relationship to prior work
The 1963 work of Lehmer--Lehmer--Mills treats *pairs* of consecutive power residues, and Rabung--Jordan (1970) studies the first occurrence of longer *single-color* runs. Lehmer's 1966 account already establishes the all-zero three-quintic exceptional maximum at 3331. The 1983 paper *Patterns of power residues* concerns first locations of patterns consisting only of power residues, according to its accessible mathematical review; its full text was not available for detailed comparison. Wu--Wei--Li (public preprint dated 2023-04-24) studies the additive structure of higher-power residue classes and provides a convenient standard character-sum lemma, but does not present an all-125-word prime classification. The present theorem instead simultaneously classifies *all* quintic coset words, including mixed words and a new sharp mixed-word cutoff. Earlier classifications for different character orders do not imply this result.

## Limitations
This concerns three consecutive **nonzero** residues over prime fields, not longer words, zero-inclusive words, or prime-power rings. The proof uses the classical Weil bound and exhaustive finite computation; the uniform analytic bound is far from the observed sharp threshold. The complete bibliographic comparison is limited by an inaccessible 1983 primary full text and the possibility of unindexed equivalent classifications. A separate independent audit has not been performed.

## References
1. Hai-Liang Wu, Ning-Liu Wei and Yu-Bo Li, *On sumsets involving kth powers of finite fields*, arXiv:2304.11789, first public 2023-04-24, especially Lemma 2.1. https://arxiv.org/abs/2304.11789
2. D. H. Lehmer, Emma Lehmer and W. H. Mills, *Pairs of Consecutive Power Residues*, Canad. J. Math. 15 (1963), 172--186. https://doi.org/10.4153/CJM-1963-020-4
3. J. R. Rabung and J. H. Jordan, *Consecutive Power Residues or Nonresidues*, Math. Comp. 24 (1970), 737--740. https://www.jstor.org/stable/2004850
4. D. H. Lehmer, *Mechanized mathematics*, Bull. Amer. Math. Soc. 72 (1966), 739--759, including the known 3331 all-quintic obstruction, independently noted at https://oeis.org/A184986
5. Emma Lehmer, *Patterns of power residues*, J. Number Theory (1983), DOI:10.1016/0022-314X(83)90004-5. Accessible abstract/review: https://portal.mardi4nfdi.de/wiki/Item:Q1055803
