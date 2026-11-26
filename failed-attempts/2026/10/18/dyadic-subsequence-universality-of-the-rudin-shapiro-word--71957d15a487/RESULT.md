# Dyadic subsequence universality of the Rudin–Shapiro word

## Finding
Let \(r=r_0r_1\cdots\) be the binary Rudin–Shapiro word: \(r_n\) is the parity of the number of overlapping occurrences of `11` in the canonical base-two representation of \(n\), and \(r_0=0\). For \(N\ge1\) write \(W_N=r_0\cdots r_{N-1}\), and let \(U(N)\) be the largest integer \(h\) such that every member of \(\{0,1\}^h\) occurs as a scattered subsequence of \(W_N\).

**Theorem.** For every integer \(k\ge4\),
\[
U(2^k)=
\begin{cases}
5\cdot2^{k-4}-1,&k\text{ even},\\
5\cdot2^{k-4},&k\text{ odd}.
\end{cases}
\]
Furthermore, for every integer \(N\ge1\),
\[
\left|U(N)-\frac{5N}{16}\right|\le\lfloor\log_2 N\rfloor+16.
\]
In particular, \(\lim_{N\to\infty}U(N)/N=5/16\), and the minimum length of an absent binary scattered subsequence of \(W_{2^k}\) is \(U(2^k)+1\). The dyadic values for \(k=4,5,6,7,8\) are \(4,10,19,40,79\).

## Assumptions and scope
All indices start at zero. Subsequence means an order-preserving selection of positions, not a contiguous factor. An empty word is a subsequence. The alphabet for universality is exactly \(\{0,1\}\). A level-\(k\) block has length \(2^k\). No probabilistic assumptions or unproved automaton assertions are used. The theorem concerns the indicated Rudin–Shapiro normalization, not arbitrary generalized Rudin–Shapiro words.

## Proof
**1. Binary greedy arches.** Scan any binary word from left to right while remembering a pending symbol \(p\in\{\varnothing,0,1\}\). Reading a symbol into an empty state sets \(p\) to it; reading the same symbol leaves \(p\) unchanged; reading the opposite symbol completes an *arch*, increments a count, and resets \(p\) to \(\varnothing\). If exactly \(h\) arches are completed, every binary word of length \(h\) is a subsequence, because each completed arch contains both letters. Conversely, take the final letter of each arch, followed by a letter absent from the incomplete final remainder (choose either letter when the remainder is empty). The greedy match of this length-\(h+1\) pattern ends its first \(h\) letters at the arch ends, since each terminal symbol first appears in its arch at its end; its last letter cannot then be matched. Therefore \(h=U(|w|)\). This also proves that the shortest absent-subsequence length is \(h+1\).

**2. A four-letter substitution.** The binary-overlap definition gives
\[
r_{2n}=r_n,\qquad r_{2n+1}=r_n\oplus(n\bmod2).
\]
Label the states \(A=(0,0)\), \(B=(0,1)\), \(C=(1,0)\), \(D=(1,1)\), with state \((r_n,n\bmod2)\). These recurrences show that the state word is the fixed point beginning in \(A\) of
\[
\tau(A)=AB,\quad\tau(B)=AD,\quad\tau(C)=CD,\quad\tau(D)=CB.
\]
The output coding maps \(A,B\) to \(0\) and \(C,D\) to \(1\). Consequently \(W_{2^k}\) is the binary coding of \(\tau^k(A)\).

**3. Exact block transfer.** For \(X\in\{A,B,C,D\}\), scan the binary coding of \(\tau^k(X)\) from an arbitrary pending state and record the number of completed arches and final state. Directly scanning the 16-letter images at \(k=4\) gives the following complete table. The three counts are for incoming states \(\varnothing,0,1\), respectively:

| Image | Completed arches | Final pending letter |
| --- | --- | --- |
| \(\tau^4(A)\) | \(4,4,5\) | \(1\) |
| \(\tau^4(B)\) | \(5,5,6\) | \(0\) |
| \(\tau^4(C)\) | \(4,5,4\) | \(0\) |
| \(\tau^4(D)\) | \(5,6,5\) | \(1\) |

We prove by induction that the following pattern holds for all \(k\ge4\). Let \(a_k\) be the empty-state count of either \(A\) or \(C\), \(b_k\) the empty-state count of either \(B\) or \(D\), and \(e_k\in\{0,1\}\) the final pending letter of \(A\) or \(D\). The other final pending letter, for \(B\) or \(C\), is \(1-e_k\). The final state is independent of the incoming state. Starting with incoming \(1\) adds one completed arch for \(A,B\); starting with incoming \(0\) adds one for \(C,D\); all other incoming states give their empty-state count.

This is true in the table. To pass from level \(k\) to \(k+1\), use \(\tau^{k+1}(X)=\tau^k(Y)\tau^k(Z)\) for \(\tau(X)=YZ\). The first block erases dependence of its *outgoing* state on the incoming state. The first output bit of the level-\(k\) blocks \(A,B\) is \(0\), and that of \(C,D\) is \(1\). Hence concatenating the transfers yields the complete recurrence
\[
 a_{k+1}=a_k+b_k+e_k,\qquad
 b_{k+1}=a_k+b_k+1-e_k,\qquad
 e_{k+1}=1-e_k.
\]
The same concatenation preserves the stated dependence on incoming states and the four outgoing-state identities. At level four, \(a_4=4\), \(b_4=5\), \(e_4=1\). Thus
\[
a_k+b_k=10\cdot2^{k-4}-1,
\qquad
b_k-a_k=\begin{cases}1,&k\text{ even},\\-1,&k\text{ odd}.
\end{cases}
\]
Solving gives \(a_k=5\cdot2^{k-4}-1\) for even \(k\), and \(a_k=5\cdot2^{k-4}\) for odd \(k\). Since the prefix \(W_{2^k}\) starts at empty state and equals the image of \(\tau^k(A)\), its arch count is \(a_k\), as claimed.

**4. Arbitrary prefixes.** Each prefix of the fixed point of a length-two substitution decomposes, according to the binary expansion of \(N\), into at most one aligned level-\(j\) block for each \(j\le\lfloor\log_2 N\rfloor\). For \(j\ge4\), the proved transfer identities imply that, regardless of its incoming state, each such block completes a number of arches differing by at most one from \(5\cdot2^{j}/16\). The at most four smaller blocks together have total length at most \(15\); both their count and their reference term lie between \(0\) and \(15\), so their total absolute discrepancy is at most \(15\). Summing the at most \(\lfloor\log_2 N\rfloor+1\) block errors proves the displayed upper bound with room to spare. Division by \(N\) proves the limit.

## Verification
The accompanying `verify.py` constructs the Rudin–Shapiro prefix independently by binary overlapping-pair parity and by the four-state substitution, checks agreement through length \(65536\), verifies the four block-transfer identities for all levels \(4\le k\le11\) and all three incoming states, verifies the dyadic formula through \(k=16\), and checks the all-prefix error estimate through \(N=131072\). It also directly enumerates all binary scattered subsequences for small prefixes to confirm the greedy-arch invariant. Execute with `python3 verify.py`; the expected terminal line begins `VERIFY_OK`. These finite checks are corroboration; the unlimited quantifiers rest on the preceding induction and binary-block argument.

## Relationship to prior work
The binary Rudin–Shapiro word and its automatic substitution representations are classical. Lü, Chen, Wen, and Wu compute its *abelian factor complexity* and related maximal consecutive sums (arXiv:1606.06935v1, 2016); these count contiguous-factor Parikh vectors and do not determine scattered-subsequence universality of individual prefixes. Kosche, Koß, Manea, and Siemer provide general structural results about arch factorization and shortest absent subsequences (arXiv:2108.13968, initially 2021). The greedy-arch characterization is prior knowledge and is not a novelty claim here. The result here is the explicit, parity-dependent Rudin–Shapiro dyadic index and the all-prefix density with logarithmic error.

## Limitations
The theorem does not enumerate all shortest absent subsequences and gives no closed form for every individual \(U(N)\) beyond the dyadic case. The error estimate is not asserted optimal. General structural arch theory may permit other proofs. An equivalent Rudin–Shapiro specialization in unindexed literature cannot be excluded; independent scientific validation has not been carried out.

## References
1. X. Lü, J. Chen, Z. Wen, and W. Wu, *On the abelian complexity of the Rudin–Shapiro sequence*, arXiv:1606.06935v1, first public version 2016-06-22, https://arxiv.org/abs/1606.06935 .
2. M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, initially 2021-08-31, https://arxiv.org/abs/2108.13968 .
