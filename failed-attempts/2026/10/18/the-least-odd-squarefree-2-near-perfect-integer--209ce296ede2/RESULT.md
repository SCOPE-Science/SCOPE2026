# The least odd squarefree \(2\)-near-perfect integer

## Finding
An integer \(n\) is \(2\)-near-perfect when two **distinct proper** positive divisors \(d_1,d_2\) can be omitted from its proper-divisor sum to leave \(n\); equivalently, \(\sigma(n)=2n+d_1+d_2\). The least **odd squarefree** \(2\)-near-perfect positive integer is
\[
\boxed{39585=3\cdot5\cdot7\cdot13\cdot29}.
\]
Indeed, \(\sigma(39585)=80640\) and the two proper divisors \(105\) and \(1365\) satisfy
\[
80640=2\cdot39585+105+1365.
\]
Moreover, an odd squarefree \(2\)-near-perfect integer must have at least five distinct prime factors, and the example attains this sharp support threshold.

## Assumptions and scope
All integers are positive. The divisor-sum function \(\sigma(n)\) includes \(n\) itself. An omitted divisor is required to be proper and the two omitted divisors must be different. This theorem concerns **odd squarefree** integers only; it does not classify arbitrary odd or arbitrary squarefree \(2\)-near-perfect numbers.

## Proof
**Step 1: a prime-support obstruction.** If \(n\) is odd and squarefree with \(r\) distinct prime factors, then \(\sigma(n)/n=\prod_{p\mid n}(1+1/p)\). For \(r\le4\), the product is at most the one on the first four odd primes:
\[
\frac{\sigma(n)}n\le\frac43\frac65\frac87\frac{12}{11}=\frac{2304}{1155}<2.
\]
(The same bound applies with fewer than four factors.) But \(2\)-near-perfectness demands \(\sigma(n)>2n\). Thus \(r\ge5\). For \(n\le39585\), there cannot be six distinct odd prime factors, since their smallest possible product is \(3\cdot5\cdot7\cdot11\cdot13\cdot17=255255\). It remains to consider exactly five factors.

**Step 2: a finite and explicitly bounded candidate list.** Write \(n=p_1p_2p_3p_4p_5\) with increasing odd primes. Monotonicity of \((1+1/p)\) gives the following strict upper bounds when the first, second, or third prime differs from the minimal choices:
\[
\prod_{p\in\{5,7,11,13,17\}}(1+1/p)<2,\quad
\prod_{p\in\{3,7,11,13,17\}}(1+1/p)<2,\quad
\prod_{p\in\{3,5,11,13,17\}}(1+1/p)<2.
\]
Consequently any candidate with \(\sigma(n)>2n\) must have \((p_1,p_2,p_3)=(3,5,7)\). Similarly, if \(p_4\ge23\), the ratio is at most \(\prod_{p\in\{3,5,7,23,29\}}(1+1/p)<2\). Hence \(p_4\in\{11,13,17,19\}\). These bounds leave eleven potentially abundant five-prime integers with first factors \((3,5,7)\). The **complete** five-prime list below \(39585\) has one additional, already-deficient integer \(36465=3\cdot5\cdot11\cdot13\cdot17\); no other first-three-prime pattern fits the bound. The inequality \(p_1p_2p_3p_4p_5\le39585\) therefore yields the following twelve entries (the extra deficient entry is included to make the finite census complete):

| \(n\) | \(\sigma(n)-2n\) |
|---:|---:|
| 15015 | 2226 |
| 19635 | 2202 |
| 21945 | 2190 |
| 23205 | 1974 |
| 25935 | 1890 |
| 26565 | 2166 |
| 31395 | 1722 |
| 33495 | 2130 |
| 33915 | 1290 |
| 35805 | 2118 |
| 36465 | -354 |
| 39585 | 1470 |

**Step 3: exhaustive divisor-pair test.** For each candidate \(n=p_1\cdots p_5\), the complete set of proper divisors is
\[
\left\{\prod_{i\in I}p_i:I\subsetneq\{1,2,3,4,5\}\right\}.
\]
It has exactly \(31\) elements. Form \(D=\prod_i(p_i+1)-2n\) and check each \(d\) in this set with \(d<D-d\); the required pair exists precisely when \(D-d\) also lies in the set. The complete finite test gives no pairs for the eleven candidates below \(39585\); at \(39585\), it gives exactly \((105,1365)\) and \((455,1015)\). This finite calculation is fully specified by the self-contained `verify.py` and its checked output. The candidate list, all arithmetic, and every divisor-pair comparison are independently reproduced there using integer arithmetic. Together with Steps 1–2, this exhaustive finite test establishes the claimed global minimum.

## Verification
Run `python3 verify.py` (Python standard library only). The program independently regenerates the twelve prime products via increasing five-prime combinations, computes \(\sigma(n)\) from the squarefree factorization, enumerates all \(31\) proper divisors of each, tests every possible omitted pair, and checks the exact short list of \((n,\sigma(n)-2n)\) above. A second independent scan trial-factors **every odd integer up to \(39585\)** and reproduces the candidate list. Exact rational inequalities and the two working divisor pairs are asserted. The accompanying `verification_output.txt` records a successful local execution. The proof's infinite portion is the prime-support and monotonicity reduction; the finite enumeration is exhaustive only because that reduction bounds the candidates.

## Relationship to prior work
Aryan, Madhavani, Parikh, Slattery and Zelinsky (first public preprint 2 October 2023) define \(2\)-near-perfect numbers and classify the families with prime support \(\{2,p\}\), including \(2^kp^i\) for \(i\in\{1,2\}\). Their theorem does not supply a minimum in the odd squarefree category. A separate published classification of squarefree three-prime numbers \(2pq\) concerns **even** integers and gives \(30\) and \(66\), so it does not imply this result. OEIS A341475 tabulates unrestricted \(2\)-near-perfect numbers, but its visible entry does not classify the least odd squarefree member. The key new facts are the sharp odd-squarefree five-prime support threshold and the complete minimum below \(39585\).

## Limitations
No classification of all odd squarefree \(2\)-near-perfect numbers or of their asymptotic density is claimed. The first example has two different omitted pairs; uniqueness of omitted divisors is not asserted. Literature non-detection is not a proof of absolute novelty. A broader table or an unindexed publication might already contain the minimum, and independent scientific audit has not been performed.

## References
1. V. Aryan, D. Madhavani, S. Parikh, I. Slattery and J. Zelinsky, “On \(2\)-Near Perfect Numbers,” arXiv:2310.01305v1, first posted 2 October 2023; sections 1–5.
2. OEIS A341475, “\(2\)-near-perfect numbers,” https://oeis.org/A341475.
3. “Squarefree \(2\)-near-perfect numbers with three prime factors,” publicly available research note, public mathematical note (identifier ab9cfade94ac).
