# First third-order binomial ambiguity among binary palindromes

## Finding

For a binary word \(w\), let \(\binom{w}{v}\) denote the number of strictly increasing index sequences spelling the scattered subsequence \(v\). Two equal-length words are *third-order binomially equivalent* when \(\binom{w}{v}=\binom{w'}{v}\) for each nonempty binary \(v\) of length at most three. Among binary palindromes, the equivalence relation is the identity at every length \(1\le n\le13\), but fails for the first time at \(n=14\). Precisely \(128\) length-fourteen binary palindromes yield \(122\) observation profiles: \(116\) singleton classes and exactly six classes of cardinality two, with no larger classes. The six ambiguous pairs are *exactly*:

| First palindrome | Second palindrome |
|---|---|
| `01010000001010` | `10000011000001` |
| `01011000011010` | `10001011010001` |
| `01100011000110` | `10001100110001` |
| `01110011001110` | `10011100111001` |
| `01110100101110` | `10100111100101` |
| `01111100111110` | `10101111110101` |

## Assumptions and scope

The alphabet is the two labeled symbols `0` and `1`; initial and final zeroes are retained. Palindrome means literal equality under reversal, not equivalence under reverse complement or cyclic rotation. Scattered occurrences count embeddings, not distinct subsequence strings. The 14 observation coordinates correspond to all \(2+4+8=14\) nonempty binary target words of lengths one through three. The result concerns only palindromes of lengths \(1\) through \(14\), and makes no assertion about the cardinalities of fibers at larger lengths or about different alphabets.

## Proof

Let \(\mathcal P_n\) be the set of length-\(n\) binary palindromes. Every \(w\in\mathcal P_n\) has one and only one representation \(w=u\operatorname{rev}(u)\) when \(n\) is even, or \(w=u\operatorname{rev}(u_1\cdots u_{|u|-1})\) when \(n\) is odd, where \(u\in\{0,1\}^{\lceil n/2\rceil}\). Consequently \(|\mathcal P_n|=2^{\lceil n/2\rceil}\), and enumerating all such halves is exhaustive.

For every word \(w=w_1\cdots w_n\) and every target \(v=v_1\cdots v_k\) with \(1\le k\le3\), compute the integer
\[
B_v(w)=\sum_{1\le i_1<\cdots<i_k\le n}\prod_{j=1}^k [w_{i_j}=v_j].
\]
The vector \(\Phi(w)=(B_v(w))_{1\le|v|\le3}\), with target order lexicographic within increasing target length, is the complete observation; by definition, equal vectors are equivalent words. The complete finite enumeration is therefore the nested loop over \(n=1,\ldots,14\), the \(2^{\lceil n/2\rceil}\) halfwords, the 14 targets, and all increasing index tuples. The included `verify_direct.py` implements exactly these finite sums using integer counters, stores the vector as a dictionary key, and reports all fibers. Its complete fiber-cardinality table is:

| \(n\) | Palindromes | Distinct profiles | Non-singleton profile sizes |
|---:|---:|---:|---|
| 1 | 2 | 2 | none |
| 2 | 2 | 2 | none |
| 3 | 4 | 4 | none |
| 4 | 4 | 4 | none |
| 5 | 8 | 8 | none |
| 6 | 8 | 8 | none |
| 7 | 16 | 16 | none |
| 8 | 16 | 16 | none |
| 9 | 32 | 32 | none |
| 10 | 32 | 32 | none |
| 11 | 64 | 64 | none |
| 12 | 64 | 64 | none |
| 13 | 128 | 128 | none |
| 14 | 128 | 122 | six classes, each of size 2 |

This exhausts every palindrome of each specified length, proves injectivity for each smaller positive length, establishes exactly six nontrivial length-fourteen classes, and verifies the displayed six pairs are all of them. The separate `verify_dynamic.py` recomputes the complete classification without enumerating index tuples: it initializes \(C_{\varepsilon}=1\); on reading letter \(a\), it replaces \(C_{va}\) by \(C_{va}+C_v\) simultaneously for all \(|v|<3\), leaving counts of other targets unchanged. Induction on the prefix proves this recurrence counts all scattered embeddings. It reproduces the same \(122\) signatures, six pairs, and \(116\) singletons.

## Verification

Run `python3 verify_direct.py` and `python3 verify_dynamic.py` with Python 3 standard library only. Both independently construct all palindrome candidates and use different embedding-count methods. Both were executed successfully, and both check the \(n=14\) fiber distribution with assertions. The procedures terminate because the largest candidate set contains only \(128\) palindromes, and every combination length is at most three. The verification is exact integer arithmetic, not a random test or a sampling estimate.

## Relationship to prior work

Third-order binomial equivalence is the established relation of equality of all scattered subword counts through length three. Rigo and Salimov introduced the binomial-complexity approach for infinite words. Freydenberger and collaborators studied general algorithms for testing \(k\)-binomial equivalence. Lejeune, Rigo and Rosenfeld studied equivalence classes of finite words, with an explicit emphasis on second-order equivalence. Those results do not assert the finite palindrome-restricted injectivity threshold and six exact minimal collisions established here. Published computations of three-deck collisions on unrestricted binary words or fixed-weight layers address different domains; they do not by themselves give the exact restriction to palindromes.

## Limitations

This is a sharp, finite exhaustive result and not an all-length classification. Its novelty assessment is qualified by potential unindexed earlier computations and the fact that the 2013 original work was assessed via its accessible abstract and bibliographic material rather than a full-text inspection. The supplied programs independently verify the complete finite claim; there is no external independent mathematical audit.

## References

1. Michel Rigo and Pavel Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words* (2013), https://orbi.uliege.be/handle/2268/149313 (public repository availability recorded as 27 May 2013).
2. Dominik D. Freydenberger et al., *Testing k-binomial equivalence*, arXiv:1509.00622, https://arxiv.org/html/1509.00622v2.
3. Marie Lejeune, Michel Rigo and Matthieu Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732, https://arxiv.org/abs/2001.11732.
