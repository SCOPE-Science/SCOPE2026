# Complete shortest-absent-subsequence language of finite Tribonacci words

## Finding
Let \(\sigma\) be the ternary Tribonacci substitution
\[\sigma(0)=01,\qquad \sigma(1)=02,\qquad \sigma(2)=0,\]
and put \(T_k=\sigma^k(0)\), with \(T_0=0\). A scattered subsequence preserves symbol order without requiring adjacency. Write \(\operatorname{SAS}(w)\) for the set of *shortest absent scattered subsequences* of a finite word \(w\), over the full alphabet \(\{0,1,2\}\).

For every integer \(k\ge4\), define \(r=|T_{k-3}|\). Then
\[
\boxed{\operatorname{SAS}(T_k)=
\begin{cases}
\{2^{r+1}\},&k\equiv0,1\pmod3,\\
\{2^r0,2^r1,2^{r+1}\},&k\equiv2\pmod3.
\end{cases}}
\]
The shortest missing length is precisely \(r+1\). Hence, out of all \(3^{r+1}\) ternary words of that length, exactly one or three are absent, respectively.

## Assumptions and scope
The source word is the finite, unshifted substitution iterate \(T_k\); the target alphabet is always all three letters, not merely the letters seen in a short prefix. Exponents on words mean repetition. Indices \(k\) are integers, with the theorem asserted for all \(k\ge4\). The infinite fixed point is \(x=\sigma^\omega(0)\). A greedy arch is the shortest prefix of the unconsumed suffix that contains each of \(0,1,2\); repeat until no such prefix exists.

## Proof
**1. Exact arch alphabet and prefix endpoints.** The known multinacci arch-factorization theorem [1] for alphabet size three yields the infinite concatenation
\[x=P B_{x_0}B_{x_1}\cdots,\qquad P=0102,\quad B_0=0100102,\quad B_1=010102,\quad B_2=0102.\]
Every displayed piece is one greedy arch; each ends in its unique symbol \(2\), and each piece contains all alphabet letters. Thus every complete arch in any finite prefix belongs to
\[\mathcal A=\{0102,0100102,010102\}.\]
The exact number of complete arches in \(T_k\) is \(r=|T_{k-3}|\) for \(k\ge3\), again by [1]. As the shortest absent scattered-subsequence length is one greater than the complete-arch count [2], it is \(r+1\).

**2. Exact final partial arch and last full arch.** The substitution identity \(T_k=T_{k-1}T_{k-2}T_{k-3}\) holds for every \(k\ge3\). In particular, for \(k\ge7\), \(T_k\) has the same final nine letters as \(T_{k-3}\) because \(|T_{k-3}|\ge13\). Direct expansion for \(k=4,5,6\) gives the nine-letter suffixes, respectively,
\[010010201,\qquad 020100102,\qquad010102010.\]
Consequently the trailing incomplete piece \(R\) after the last complete arch is, for every \(k\ge4\), respectively \(01\), the empty word, or \(010\) as \(k\equiv1,2,0\pmod3\). Moreover, in all three cases the final complete arch is either \(0100102\) or \(010102\), so its prefix before \(2\) has the scattered subsequence \(11\). The complete arches number at least two for \(k\ge4\).

**3. A near-universality lemma.** Consider any word
\[W=A_1A_2\cdots A_rR,\qquad r\ge2,\]
where every \(A_i=Q_i2\) lies in \(\mathcal A\), the last \(Q_r\) contains \(11\) as a subsequence, and \(R\) contains no \(2\). The \(r\) complete arches imply every ternary word of length at most \(r\) is a subsequence. We claim every length-\(r+1\) word is also a subsequence, except exactly those of the form \(2^r a\) whose final letter \(a\) does not occur in \(R\).

Take a word \(u=u_1\cdots u_{r+1}\). If some adjacent symbols are \(a2\) with \(a\in\{0,1\}\), say at positions \(j,j+1\), place its preceding \(j-1\) letters separately into arches \(A_1,\ldots,A_{j-1}\), place the pair \(a2\) in arch \(A_j\), and place the remaining \(r-j\) letters separately into arches \(A_{j+1},\ldots,A_r\). Each arch contains every single letter, and \(a2\) is a subsequence of every arch, so the embedding exists.

Otherwise no binary letter immediately precedes a \(2\) in \(u\). All its \(2\)'s therefore precede its binary letters, so \(u=2^tB\) with \(B\in\{0,1\}^b\), \(b=r+1-t\). If \(b=0\), \(u=2^{r+1}\) is absent because \(W\) has only \(r\) copies of \(2\). If \(b=1\), then \(t=r\), and all \(r\) copies of \(2\) must be used; \(u\) occurs exactly when the trailing letter occurs in \(R\). Finally let \(b\ge2\). Map the initial \(t\) twos to the terminals of the first \(t\) arches. To fit the remaining \(b\) binary symbols into the remaining \(r-t=b-1\) arches, map one adjacent pair to one arch and all other symbols to separate arches, respecting their order. Every \(Q_i\) contains \(00\), \(01\), and \(10\) as scattered subsequences. Thus any adjacent pair other than \(11\) can be grouped in its corresponding arch. If no such pair exists, \(B=1^b\), and its last two symbols can instead be grouped in \(Q_r\), which contains \(11\). In every case \(u\) embeds. This proves the lemma.

**4. Apply the lemma.** By Step 2, the final arch in \(T_k\) satisfies the lemma for every \(k\ge4\). For \(k\equiv0,1\pmod3\), the incomplete suffix contains both \(0\) and \(1\), hence the only shortest absent word is \(2^{r+1}\). For \(k\equiv2\pmod3\), the incomplete suffix is empty and all three words \(2^r0\), \(2^r1\), and \(2^{r+1}\) are absent, with all other words present. This is the claimed complete classification. \(\square\)

## Verification
The standalone `verify.py` expands the substitution, independently computes the greedy arch decomposition and the number of missing length-\(r+1\) subsequences via a deterministic next-occurrence dynamic program, and compares that count to the asserted one for ranks four through ten. It also verifies, without using the derived normal form, the precise set of missing shortest subsequences by exhaustive enumeration for ranks four and five. These finite checks support but do not replace the proof for all ranks.

## Relationship to prior work
The exact 2026 multinacci arch factorization [1] gives the arch count, types, and endpoint structure, but does **not** determine the shortest absent-subsequence language. The present contribution is the sharp *one-or-three* absence classification at its first incomplete length; it uses the all-arch structural result as an input and proves a separate near-universality embedding lemma. Foundational absent-subsequence terminology and arch/universality equivalence come from [2]. The occurrence-preserving-morphism study [3] concerns contiguous factor counts and minimal unique substrings, not missing scattered-subsequence languages. The 2026 epistandard net-occurrence study [4] concerns repeated contiguous factors, not the claimed scattered language. Related published classifications of missing scattered subsequences in other morphic words provide context, but do not logically cover the Tribonacci formulation.

## Limitations
The result assumes the exact unshifted Tribonacci substitution and full three-letter alphabet; it does not claim the same absence language for arbitrary morphic words, shifted prefixes, or general \(m\)-bonacci words. The cited arch theorem supplies the exact arch count and alphabet; the near-universality step is self-contained. Finite verification cannot establish the infinite claim. Unindexed equivalent subsequence-automaton consequences of existing multinacci return-word results remain a literature-priority risk; independent validation has not been performed.

## References
1. *A self-similar arch factorization for all multinacci words*, public research record (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-a-self-similar-arch-factorization-for-all-multinacci-words--06c42dc2835a.
2. M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (2021), https://arxiv.org/abs/2108.13968.
3. K. Kishi, P. Guo, C. Urbina, and H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034 (first public 2026-05-18), https://arxiv.org/abs/2605.18034.
4. S. Faro and A. Pavone, *Exact Net-Occurrence Counts in Purely Morphic Regular Epistandard Words*, arXiv:2610.04298 (first public 2026-10-03), https://arxiv.org/abs/2610.04298.
