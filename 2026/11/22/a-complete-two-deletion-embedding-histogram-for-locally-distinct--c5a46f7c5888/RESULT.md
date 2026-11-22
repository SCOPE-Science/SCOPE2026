# A complete two-deletion embedding histogram for locally distinct words

## Finding
Let \(Q\) be an alphabet of size \(q\ge 3\), let \(m\ge1\), and let \(y=y_1\cdots y_m\in Q^m\) satisfy
\[
y_i\ne y_j\qquad\text{whenever }1\le |i-j|\le2.
\]
For each \(x\in Q^{m+2}\), let \(e_y(x)\) be the number of increasing \(m\)-position embeddings of \(y\) into \(x\). Write \(N_r=|\{x\in Q^{m+2}:e_y(x)=r\}|\), and put
\[
S=1+(m+2)(q-1)+\binom{m+2}{2}(q-1)^2.
\]
The complete embedding-multiplicity histogram is
\[
\begin{aligned}
N_0&=q^{m+2}-S,\\
N_1&=S-(m+2)\bigl(m(q-2)+1\bigr)-(2m-1)-\binom m2,\\
N_2&=(m+2)\bigl(m(q-2)+1\bigr),\\
N_3&=2m-1,\\
N_4&=\binom m2,\\
N_r&=0\qquad(r\ge5).
\end{aligned}
\]
These counts depend only on \(q,m\), not on the chosen locally distinct word. More precisely, the multiplicity-four hosts are exactly the \(\binom m2\) words obtained by duplicating each of two distinct positions of \(y\) adjacently. The multiplicity-three hosts are exactly the \(m\) words obtained by replacing one symbol with three consecutive copies and the \(m-1\) words obtained by replacing an adjacent pair \(ab\) by \(abab\).

For the uniform-input, exactly-two-deletion channel, conditioned on received word \(y\), the posterior input entropy (bits) is exactly
\[
H(X\mid Y=y)=\log_2 Z-\frac{2N_2+3N_3\log_2 3+8N_4}{Z},
\qquad Z=q^2\binom{m+2}{2}.
\]
In particular, for fixed \(q\ge3\) as \(m\to\infty\),
\[
H(X\mid Y=y)=\log_2\!\left(q^2\binom{m+2}{2}\right)-\frac4q+O_q(m^{-1}),
\]
uniformly over this word family. For \(m\ge2\), the family contains exactly \(q(q-1)(q-2)^{m-2}\) words. At \(q=3\), its six members at each length \(m\ge2\) are prefixes of the two periodic three-cycle directions under alphabet relabeling.

## Assumptions and scope
The word \(y\) is fixed, the alphabet is finite and labeled, and embeddings are **indexed** increasing subsequences, not distinct resulting strings. Exactly two symbols are inserted into \(y\) to create a host of length \(m+2\), equivalently exactly two positions of a host are deleted to recover \(y\). For the entropy statement, the transmitted \(x\in Q^{m+2}\) is uniform, two deletion positions are chosen uniformly among all \(\binom{m+2}{2}\) possibilities, and the received string is observed with its positions in order. The claim is not an assertion of entropy maximization over arbitrary received words.

## Proof
**1. A disjoint set of potential match positions.** Use one-based indices, and fix a host \(x\) with at least one embedding. For each \(i\in\{1,\dots,m\}\), define
\[
S_i(x)=\{j\in\{i,i+1,i+2\}:x_j=y_i\},\qquad c_i=|S_i(x)|.
\]
Every embedding has its \(i\)-th matched position in \(S_i(x)\): its position is at least \(i\), and at most \(i+2\) because only two host positions are skipped. The sets \(S_i(x)\) are pairwise disjoint. Indeed, if a host position belonged to both \(S_i\) and \(S_j\), then \(|i-j|\le2\) and \(y_i=y_j\), contrary to the hypothesis. Hence
\[
\sum_{i=1}^m c_i\le m+2.
\]
As there is an embedding, each \(c_i\ge1\). Any embedding picks one position from each \(S_i\), in strictly increasing order. Thus at most two excess candidate positions exist, and \(e_y(x)\le4\), except possibly a single three-candidate index, which has at most three choices. More explicitly, the only ways to have three or more embeddings are: one \(c_i=3\), or two indices \(i<j\) with \(c_i=c_j=2\). In both cases all other candidate sets are singletons; the inequality is an equality and all host positions belong to one of the candidate sets.

**2. Three choices for one index.** If \(c_i=3\), then \(x_i=x_{i+1}=x_{i+2}=y_i\), and all other source symbols occur once and in source order. Therefore \(x\) is exactly the word formed by tripling the \(i\)-th symbol of \(y\). Each of its three copies can serve as the \(i\)-th match, and no other choices exist. There are exactly \(m\) distinct hosts of this form.

**3. Two indices with two choices.** If \(c_i=c_j=2\) for \(i<j\), all source positions other than \(i,j\) have fixed matches. When \(j\ge i+2\), the allowable choices for position \(i\) and for position \(j\) cannot cross one another: their position ranges meet at most at an endpoint, and the sets are disjoint. Each of the two duplicated indices has either one or two choices compatible with its singleton neighbors. Consequently the total is a product in \(\{1,2,4\}\), never three. Four choices occur exactly when the two copies of each duplicated symbol are consecutive between its neighboring fixed source symbols. For each \(i<j\) with \(j\ge i+2\), precisely one host has this form.

When \(j=i+1\), the four candidate positions necessarily exhaust the consecutive block \(\{i,i+1,i+2,i+3\}\). Its first letter is \(a=y_i\) and its last is \(b=y_{i+1}\), with the two middle positions occupied by one additional \(a\) and one additional \(b\). Thus the block is either \(aabb\), giving four embeddings of \(ab\), or \(abab\), giving exactly three embeddings. All other source letters have unique fixed matches. Hence for each adjacent pair there is one additional multiplicity-four host and one multiplicity-three host.

The cases in steps 2 and 3 cannot collide: for a given host the vector \((c_1,\dots,c_m)\) uniquely determines which source index or pair has extra choices. We therefore have \(N_4=\binom m2\) and \(N_3=m+(m-1)=2m-1\). The same proof includes \(m=1\), for which only the tripling case occurs.

**4. Determine the other classes.** Counting all indexed insertion histories gives
\[
T:=\sum_{x\in Q^{m+2}}e_y(x)=q^2\binom{m+2}{2}.
\]
The number \(S\) of distinct hosts with at least one embedding is the ordinary single-word two-insertion-sphere cardinality, independent of \(y\):
\[
S=\sum_{r=0}^{2}\binom{m+2}{r}(q-1)^r.
\]
One elementary proof is to scan a host greedily against a fixed infinite continuation of \(y\). At each scanned position exactly one letter advances the next target position and \(q-1\) letters do not. The host contains \(y\) precisely when at least \(m\) advances occur among \(m+2\) scans. Counting the complementary number of nonadvances gives the displayed sum. It follows that
\[
T-S=N_2+2N_3+3N_4.
\]
Substituting the established values of \(N_3,N_4\), and simplifying, yields \(N_2=(m+2)(m(q-2)+1)\). The formulas for \(N_1,N_0\) follow by counting positive and all hosts, respectively.

**5. Entropy.** By Bayes' rule and uniform input and deletion masks, the conditional probability of a host is \(e_y(x)/T\). Substitution into Shannon entropy gives the displayed exact formula, because only multiplicities two, three and four contribute to \(\sum_x e_y(x)\log_2 e_y(x)\). At fixed \(q\), the numerator of the correction is \(2qm^2+O_q(m)\) and its denominator is \(q^2m^2/2+O_q(m)\). This proves the claimed \(4/q\) limit and error term.

## Verification
The standalone script `verify.py`, requiring only the Python standard library, independently enumerates every indexed two-insertion history and also enumerates host words using a dynamic-programming subsequence counter in the smaller parameter ranges. It verifies the complete histogram and explicitly checks every multiplicity-three and -four host against the proof's structural families. The run covered all \(1{,}226\) locally distinct words for \(q=3\), \(1\le m\le8\); \(q=4\), \(1\le m\le6\); and \(q=5\), \(1\le m\le5\), amounting to \(513{,}126\) indexed insertion histories and \(484{,}024\) independent host-DP evaluations. The captured stdout is supplied in `verify_output.txt`. These computations are finite cross-checks of the all-parameter combinatorial argument, not substitutes for it.

At the boundary, \(y=010\) over three letters has positive multiplicity counts \(N_1=23,N_2=21,N_3=3,N_4=4\), different from the locally distinct prediction; \(y=001\) even has hosts of multiplicity six. Thus the local hypothesis is substantive.

## Relationship to prior work
Ma and Zhang (arXiv:2611.01064, first public October 31, 2026) settle the **binary** two-deletion entropy-maximizer question and give histograms for binary alternating received words. The present classification instead concerns every fixed nonbinary alphabet \(q\ge3\), all lengths, and all words with distinct letters at distance one and two; it neither uses nor claims the binary entropy-maximization theorem. Singhvi, Sabary, Bar-Lev and Yaakobi (arXiv:2407.10026, first public July 13, 2024) develop the embedding-entropy framework. Tavakoli, Nguyen and Bose (arXiv:2607.19559, first public July 21, 2026) study nonbinary deletion-channel embedding scalars and normalization, but not this restricted received-word histogram. Menon and Singh (arXiv:2306.07870, first public June 13, 2023) enumerate subsequence frequencies in binary words. No inspected result directly supplies the nonbinary locally distinct formula. General normalization alone does not determine the multiplicity-three and multiplicity-four classes, on which the result depends.

## Limitations
The theorem applies only to exact deletion radius two, uniformly transmitted words for the entropy formula, and received words with distinct symbols in every consecutive triple. It does not establish a global entropy maximum over all received words, any nonuniform source theorem, or a formula at three or more deletions. The literature comparison is bounded; a previously unindexed equivalent specialization could exist.

## References
1. H. Ma and W. Zhang, *Maximal input entropy for binary two-deletion and two-insertion channels*, arXiv:2611.01064, first submitted October 31, 2026. https://arxiv.org/abs/2611.01064
2. S. Singhvi, O. Sabary, D. Bar-Lev and E. Yaakobi, *Conditional Entropies of k-Deletion/Insertion Channels*, arXiv:2407.10026, first submitted July 13, 2024; *IEEE Transactions on Information Theory* 71 (2025), 6503–6516. https://arxiv.org/abs/2407.10026
3. H. Tavakoli, T. Nguyen and B. Bose, *Combinatorial Capacity Bounds for the q-ary Deletion Channel*, arXiv:2607.19559, first submitted July 21, 2026. https://arxiv.org/abs/2607.19559
4. K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, first submitted June 13, 2023; *Discrete Mathematics* 347 (2024), 113928. https://arxiv.org/abs/2306.07870
