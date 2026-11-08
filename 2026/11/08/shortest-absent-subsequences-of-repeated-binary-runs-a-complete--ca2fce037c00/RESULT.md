# Shortest absent subsequences of repeated binary runs: a complete phase diagram

## Finding
For arbitrary integers \(a,b,m\ge 1\), let \(W_{a,b,m}=(0^a1^b)^m\). A word is a *subsequence* of another if its letters can be selected in increasing position order, without requiring adjacency. Let \(\operatorname{SAS}(W)\) be the set of shortest **absent subsequences**, where absence is relative to the fixed alphabet \(\{0,1\}\). Define \(F_0=0\), \(F_1=1\), \(F_{n+2}=F_{n+1}+F_n\).

The shortest absent length is \(m+1\) when \(\min(a,b)=1\), and \(2m\) otherwise. The complete exact cardinality is
\[
|\operatorname{SAS}(W_{a,b,m})|=\begin{cases}
m+2,&a=b=1,\\
2,&\min(a,b)=1<\max(a,b),\\
F_{2m},&a=b=2,\\
2^{m-1},&\min(a,b)=2<\max(a,b),\\
1,&a,b\ge3.
\end{cases}
\]
More strongly, every shortest absent word is explicitly characterized:

- When \(a=b=1\), the set is \(\{1^j0^{m+1-j}:0\le j\le m+1\}\).
- When \(a=1<b\), the set is \(\{0^{m+1},10^m\}\).
- When \(b=1<a\), the set is \(\{1^{m+1},1^m0\}\).
- When \(a,b\ge2\), it consists of the length-\(2m\) binary words beginning with \(1\) and whose maximal runs obey the following constraint: a maximal \(0\)-run has positive **odd** length if \(a=2\), and has length one if \(a\ge3\); a maximal \(1\)-run has positive **odd** length if \(b=2\), and has length one if \(b\ge3\).

This yields an exact transition between linear, constant, Fibonacci, and exponential enumeration regimes without a limit on the number of repeated blocks.

## Assumptions and scope
All run lengths and the repetition number are positive integers. The alphabet stays binary even at parameter boundaries. Every instance contains both letters; absent words are counted as *distinct strings*, not embeddings or witnesses. Runs refer to **maximal homogeneous runs of a candidate word**, not the prescribed runs of its host. The position of the last symbol used by the leftmost (greedy) subsequence embedding is what controls absence. The empty word occurs as a subsequence, so no empty word is absent.

## Proof
**1. Greedy run-index lemma.** Let \(u=c_1^{\ell_1}\cdots c_h^{\ell_h}\) be any nonempty binary word decomposed into its maximal constant-letter runs. For each \(i\), put \(d_i=a\) if \(c_i=0\) and \(d_i=b\) if \(c_i=1\). Index the consecutive homogeneous runs of the infinite periodic host \((0^a1^b)^\omega\) starting at zero. The leftmost greedy embedding of \(u\) ends in host-run index
\[
J(u)=\mathbf1_{\{c_1=1\}}+(h-1)+2\sum_{i=1}^{h}\left(\left\lceil\frac{\ell_i}{d_i}\right\rceil-1\right).\tag{1}
\]
To see this, an initial \(1\)-run skips the first host \(0\)-run, giving the indicator. Each switch of letter advances to the next host run, giving \(h-1\). When a maximal candidate run needs more than one host run of its own letter, each further same-letter host run costs two host-run positions. The greedy embedding always uses the earliest available occurrence; at every candidate run boundary it enters the next available opposite-letter host run at its beginning. Induction on the candidate runs proves (1), including runs of length exceeding the corresponding host capacity. The finite host has precisely runs indexed \(0,\ldots,2m-1\); hence
\[
u\text{ is a subsequence of }W_{a,b,m}\quad\Longleftrightarrow\quad J(u)\le2m-1.\tag{2}
\]

**2. Both capacities at least two.** For integers \(d\ge2\) and \(\ell\ge1\),
\[
2\left(\left\lceil\frac{\ell}{d}\right\rceil-1\right)\le\ell-1.\tag{3}
\]
For \(d=2\), equality holds precisely when \(\ell\) is odd. For \(d\ge3\), equality holds precisely when \(\ell=1\). (Write \(\ell=qd+r\), or compare consecutive ranges \((q-1)d+1\le\ell\le qd\), to check both equality cases.) Applying (3) term by term to (1) gives
\[
J(u)\le |u|-1+\mathbf1_{\{c_1=1\}}.\tag{4}
\]
Thus every binary candidate of length at most \(2m-1\) is present by (2). At length \(2m\), a word starting with \(0\) is present; a word starting with \(1\) is absent **exactly when** equality holds in (3) for each maximal candidate run. This is precisely the stated complete run-language characterization. It is nonempty because \((10)^m\) is one of its members. Consequently the shortest absent length is exactly \(2m\).

For counting, form the ordinary length-generating functions of permitted runs:
\[
R_0(z)=\begin{cases}\frac{z}{1-z^2},&a=2,\\z,&a\ge3,\end{cases}\qquad
R_1(z)=\begin{cases}\frac{z}{1-z^2},&b=2,\\z,&b\ge3.\end{cases}
\]
Every permitted run length is odd, so a word of even length starting with \(1\) must end with \(0\). Its run sequence is a positive concatenation of \(1\)-run, \(0\)-run pairs. The generating function for these words is
\[
G(z)=\sum_{j\ge1}(R_1(z)R_0(z))^j=\frac{R_1(z)R_0(z)}{1-R_1(z)R_0(z)}.\tag{5}
\]
If \(a=b=2\), (5) is \(z^2/(1-3z^2+z^4)\), whose coefficient of \(z^{2m}\) is \(F_{2m}\). This identification follows from \(F_{2m}=3F_{2m-2}-F_{2m-4}\), the initial \(F_0=0,F_2=1\), and the same rational generating function. If exactly one of \(a,b\) equals two, (5) becomes \(z^2/(1-2z^2)\), giving \(2^{m-1}\). If both are at least three, (5) is \(z^2/(1-z^2)\), giving one.

**3. Both capacities one.** With \(a=b=1\), all \(d_i=1\), and (1) reduces to
\[
J(u)=2|u|-h-1+\mathbf1_{\{c_1=1\}}.\tag{6}
\]
For \(|u|\le m\), \(J(u)\le2m-1\), so all such candidates occur. For \(|u|=m+1\), (2) and (6) show absence exactly if \(h\le1\) for a word starting with \(0\), or \(h\le2\) for a word starting with \(1\). These are exactly \(1^j0^{m+1-j}\), \(0\le j\le m+1\); the list has \(m+2\) distinct members.

**4. Exactly one capacity one.** Let \(a=1<b\). Write \(|u|=L\), and let \(Z\) be its number of zeroes. When there is at least one zero, write \(h_0,h_1\) for the numbers of maximal zero and one runs, and \(\delta=\mathbf1_{\{c_1=1\}}\). Equation (1) and (3) for one-runs yield
\[
J(u)\le 2(Z-h_0)+(L-Z-h_1)+(h_0+h_1-1)+\delta=L+Z-h_0-1+\delta.\tag{7}
\]
For \(L\le m\), all words containing a zero therefore embed, because \(Z\le L\), \(h_0\ge1\), and \(\delta\le1\), giving \(J(u)\le2L-1\le2m-1\). The all-one words of length at most \(m\) embed because the host contains \(mb\ge m\) ones. Thus the shortest absent length is at least \(m+1\). Now set \(L=m+1\). If \(1\le Z\le m-1\), (7) gives \(J(u)\le2m-1\), so the word embeds. If \(Z=0\), the candidate is \(1^{m+1}\), which embeds because \(mb\ge m+1\). If \(Z=m+1\), the candidate is \(0^{m+1}\), which is absent because the host has only \(m\) zeroes. If \(Z=m\), the word is \(0^i10^{m-i}\). For every \(1\le i\le m\) one can take one zero from each of the first \(i\) zero blocks, the one immediately after the \(i\)-th such block, and one zero from each remaining block: it embeds. The remaining \(i=0\) word \(10^m\) is absent because after its initial one only \(m-1\) zero blocks remain. The complete shortest-absent set is therefore \(\{0^{m+1},10^m\}\). The transformation that reverses a word and complements every letter maps \((0^a1)^m\) to \((01^a)^m\), preserving scattered-subsequence membership and shortest absence. Applying it to the preceding case gives \(\operatorname{SAS}((0^a1)^m)=\{1^{m+1},1^m0\}\) for \(a\ge2\). This completes every parameter case.

## Verification
The standalone `verify.py` uses three logically distinct checks: direct left-to-right subsequence membership; formula (1) evaluated from candidate maximal runs; and the explicit candidate-language test. It tests all \(175\) triples \(1\le a,b\le5\), \(1\le m\le7\), comparing \(354{,}076\) candidates and independently confirming all shorter binary patterns occur. It independently computes the shortest-absent cardinality with a greedy-subsequence finite-state dynamic program and checks \(49\) additional instances with \(m\in\{8,10,12,16,20,30,40\}\). Execution: `python3 verify.py`. Expected output: `RUN_BLOCK_SAS_VERIFY_OK 175 354076 49`.

These finite checks corroborate the symbolic proof but are not used to extrapolate to untested parameters. The infinite proof relies on equations (1) through (7).

## Relationship to prior work
Kosche, Koß, Manea, and Siemer (2021/2023) establish the fundamental arch decomposition and general structural/algorithmic characterizations of shortest absent subsequences. Their text includes the single word \(0011\) and general extremal constructions, but the inspected statements do not classify the exact set for all \((0^a1^b)^m\). Manea, Ringleb, Siemer, and Winkler (2025) develop output-sensitive enumeration algorithms for arbitrary input strings; these are applicable to each instance but do not give the uniform run-language characterization or the five-branch closed form. Adamson and collaborators (2024) study general bounds and extremal counts of absent subsequences, not the complete repeated-run family.

A separately checked published mathematical record, *Fibonacci extremals for shortest absent subsequences of binary words* (2026), optimizes the count over **all** binary words of a fixed total length, rather than evaluating the specific repeated-run host. Its global maximum does not imply the exact family-specific five-case formula. Classical Fibonacci enumeration of compositions explains the sequence once the run constraint is proved, but does not itself prove that constraint. The results here describe a particular structured family and do not improve the general output-sensitive enumeration bounds.

## Limitations
This is specific to the binary alphabet and exact alternating host blocks with constant positive capacities and a whole number of periods. It does not directly cover nonperiodic capacities, larger alphabets, or minimal absent subsequences of nonminimal length. The statement gives *string* counts, not numbers of embeddings. Independent mathematical audit and definitive historical priority assessment have not been performed; a prior equivalent derivation hidden under other subsequence terminology remains possible.

## References
1. F. Manea, T. Ringleb, S. Siemer, and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, first public version 30 April 2025, https://arxiv.org/html/2504.21471v1 .
2. M. Kosche, T. Koß, F. Manea, and S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first public version August 2021; *Fundamenta Informaticae* 189 (2023), https://arxiv.org/html/2108.13968v6 .
3. B. Adamson and collaborators, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, first public version July 2024, https://arxiv.org/html/2407.18599v2 .
4. *Fibonacci extremals for shortest absent subsequences of binary words* (2026), mathematical research record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-fibonacci-extremals-for-shortest-absent-subsequences-of-binary-w--1a6556f14d28/RESULT.md .
