# Exact substitution graph and detecting-code capacity of ternary short-tandem-irreducible words

## Finding
Let \(\mathcal I_n\) be all words of length \(n\) over \(\{0,1,2\}\) containing neither a repeated adjacent symbol \(aa\) nor an adjacent repeated two-symbol block \(abab\). Join two words if their Hamming distance is exactly one, and denote this graph by \(G_n\). Write \(K_j\) for a complete graph, \(P_3\) for the three-vertex path, \(C_4\) for the four-cycle, and let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\).

**Component classification (every \(n\ge4\)).**
\[
G_4\cong 6P_3,\qquad
G_5\cong 6K_1\sqcup6C_4,
\]
\[
G_n\cong(6F_{n-6})K_1\sqcup(12F_{n-5})K_2\sqcup(6F_{n-4})C_4
\quad(n\ge6).
\]
In particular no component contains more than four vertices, despite \(|\mathcal I_n|=6F_n\).

**Full error-detecting codebook enumerator.** A subset \(\mathcal C\subseteq\mathcal I_n\) has distinct codewords at Hamming distance at least two exactly when it is an independent set in \(G_n\). With \(J_n(z)=\sum_{\mathcal C\text{ independent}}z^{|\mathcal C|}\),
\[
J_4(z)=(1+3z+z^2)^6,\qquad
J_5(z)=(1+z)^6(1+4z+2z^2)^6,
\]
\[
J_n(z)=(1+z)^{6F_{n-6}}(1+2z)^{12F_{n-5}}
(1+4z+2z^2)^{6F_{n-4}}\quad(n\ge6).
\]
Consequently the largest one-substitution-*detecting* code inside \(\mathcal I_n\) has size
\[
\alpha(G_4)=12,\qquad\alpha(G_5)=18,\qquad
\alpha(G_n)=6F_{n-6}+12F_{n-5}+12F_{n-4}\quad(n\ge6).
\]
The numbers of labeled maximum codebooks are respectively \(1\), \(2^6\), and \(2^{12F_{n-5}+6F_{n-4}}\). Moreover,
\[
\lim_{n\to\infty}\frac{\alpha(G_n)}{|\mathcal I_n|}
=5-2\sqrt5.
\]

## Assumptions and scope
The alphabet is *ternary* and the forbidden factors are contiguous, literal repeats \(aa\) and \(abab\), with distinct symbols allowed or not in the notation (the prohibition on \(aa\) makes any occurring \(abab\) have \(a\ne b\)). Coordinates are indexed, and words are not quotiented by rotation, reversal, or alphabet relabeling. Graph edges are only length-preserving, **one-symbol substitutions** between admissible words. An altered word outside \(\mathcal I_n\) is rejected. This is error detection, not correction, and includes no duplication, insertion, or deletion channel operations.

## Proof
**1. Sign representation.** Because adjacent letters differ, set \(d_i=x_{i+1}-x_i\pmod3\in\{+1,-1\}\) for all \(0\le i\le n-2\). The block \(x_ix_{i+1}x_{i+2}x_{i+3}\) is \(abab\) exactly when \((d_i,d_{i+1},d_{i+2})\) alternates, i.e. equals \((+,-,+)\) or \((-,+,-)\). Thus \(t_j=\mathbf1_{d_j\ne d_{j+1}}\), of length \(n-2\), has no two consecutive ones. Every initial symbol (three choices), initial sign (two choices), and such binary word reconstruct exactly one admissible word; hence \(|\mathcal I_n|=6F_n\).

**2. Interior rigidity.** Suppose a Hamming-one mutation at a nonendpoint position \(i\), where \(1\le i\le n-2\), keeps both adjacent inequalities. In a ternary alphabet this is possible only if the two old neighboring symbols coincide; in the sign sequence the affected pair is \((s,-s)\) and after mutation is \((-s,s)\). If a sign exists immediately on the right, the old alternating-triple prohibition forces that next sign to be \(-s\); then the mutated triple \((-s,s,-s)\) is forbidden. If instead no sign exists on the right, one exists immediately on the left since \(n\ge4\). The old condition forces the preceding sign to be \(s\), making the mutated triple \((s,-s,s)\) forbidden. Hence no interior coordinate can change along an edge.

**3. Components over a fixed core.** Set the interior core \(c=x_1\cdots x_{n-2}\). By step 2, components lie within fibers of the core. For \(n\ge5\), conditions on the first and last symbols are independent: a four-letter forbidden factor cannot meet both endpoints. The first endpoint has two allowed letters if \(x_1\ne x_3\), and one otherwise; likewise the last endpoint has two allowed letters if \(x_{n-4}\ne x_{n-2}\), and one otherwise. Within a fiber, changing one endpoint changes one coordinate, so the graph is \(K_a\square K_b\) for \(a,b\in\{1,2\}\), giving only \(K_1,K_2,C_4\).

**4. Fibonacci fiber census.** For the core, let \(k=n-4\), the number of comparison bits between successive core signs. There are six choices of its first letter and first sign, times any binary word \(t\) of length \(k\) without consecutive ones. The left endpoint has two possibilities exactly when the first comparison bit is zero, and the right endpoint does so exactly when the final comparison bit is zero. For \(k\ge2\), the number of no-consecutive-ones binary strings with both endpoints zero is \(F_k\), with exactly one endpoint one is \(2F_{k-1}\), and with both endpoints one is \(F_{k-2}\). Multiplying by six and translating \(k=n-4\) proves the formula for \(n\ge6\). For \(k=1\) the single bit zero gives \(6C_4\) and bit one gives \(6K_1\), proving the length-five case.

**5. Length four.** Fixing the ordered core \((x_1,x_2)\) with unequal letters leaves two choices at each endpoint, except the unique pair of endpoints that makes \(x_0x_1x_2x_3=abab\). Thus each of six cores supports a square with one vertex deleted, namely \(P_3\).

**6. Detection enumerator.** The independent-set polynomials of \(K_1,K_2,C_4,P_3\) are respectively \(1+z\), \(1+2z\), \(1+4z+2z^2\), and \(1+3z+z^2\). Independence polynomials multiply across disjoint components. Each \(K_2\) admits two maximum independent sets, each \(C_4\) admits two, and \(P_3,K_1\) admit only one. This yields the complete enumerator, its degree, and maximum-codebook counts. Finally the Fibonacci ratio limit and \(\varphi=(1+\sqrt5)/2\) give \(\varphi^{-6}+2\varphi^{-5}+2\varphi^{-4}=5-2\sqrt5\).

## Verification
The included dependency-free Python 3 `verify.py` exhaustively enumerates all admissible words at every \(4\le n\le16\), creates Hamming-one edges by attempting both alternate symbols at each coordinate, computes connected components by graph traversal, and checks the predicted shapes, multiplicities, largest independent-set sizes, and number of maximum independent sets. The test passed in the present package. The all-length result comes from the proof, not from finite enumeration.

## Relationship to prior work
Irreducible words avoiding short tandem repeats are standard in duplication coding, with efficient enumeration/encoding studied by Chee, Chrisnata, Kiah and Nguyen (2018). Kovačević (2019) studies maximum nonconfusability under repeated tandem duplications. Tang, Yehezkeally, Schwartz and Farnoud (2019) develop codes detecting or correcting a substitution in the presence of tandem duplications. Tang and coauthors (2022) analyze mixed duplication/edit correction, and Yu and Schwartz (2024) construct duplication-free code families. Their channel operations, error-detection objectives, and asymptotic bounds differ from this exact induced Hamming-one graph and its complete independent-set polynomial; prior duplication-code results do not imply this claim without a separate structural argument. Exhaustive historical novelty cannot be inferred from searching, and an equivalent independently published result may exist.

## Limitations
Ternary alphabet, linear (noncyclic) words, and forbidden repetitions of lengths one and two only. A maximum one-substitution detecting code is not asserted to correct any substitution, nor to detect substitutions followed by tandem duplications. The finite checker is corroboration, not an infinite proof. Literature-priority certainty and independent mathematical audit are not claimed.

## References
1. Y. M. Chee, J. Chrisnata, H. M. Kiah, T. T. Nguyen, *Efficient Encoding/Decoding of Irreducible Words for Codes Correcting Tandem Duplications*, arXiv:1801.02310 (first posted 2018-01-08), https://arxiv.org/abs/1801.02310.
2. Y. Tang, Y. Yehezkeally, M. Schwartz, F. Farnoud, *Single-Error Detection and Correction for Duplication and Substitution Channels*, arXiv:1911.05413 (first posted 2019-11-13), https://arxiv.org/abs/1911.05413.
3. M. Kovačević, *On the Maximum Number of Non-Confusable Strings Evolving Under Short Tandem Duplications*, arXiv:1911.06561 (first posted 2019-11-15), https://arxiv.org/abs/1911.06561.
4. Y. Tang et al., *Low-redundancy codes for correcting multiple short-duplication and edit errors*, arXiv:2208.02330 (first posted 2022-08-03), https://arxiv.org/abs/2208.02330.
5. W. Yu, M. Schwartz, *On Duplication-Free Codes for Disjoint or Equal-Length Errors*, arXiv:2401.04675 (first posted 2024-01-09), https://arxiv.org/abs/2401.04675.
