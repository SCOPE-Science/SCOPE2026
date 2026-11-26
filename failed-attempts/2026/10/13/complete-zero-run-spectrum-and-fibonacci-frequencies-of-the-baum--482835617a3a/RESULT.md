# Complete zero-run spectrum and Fibonacci frequencies of the Baum–Sweet word

## Finding
Let \(b(0)=1\); for \(n\ge1\), let \(b(n)=1\) precisely when all maximal blocks of zeros in the ordinary binary expansion of \(n\) have even length. Let \(F_0=0\), \(F_1=1\), and \(F_{r+2}=F_{r+1}+F_r\). For \(j\ge4\) put
\[
 h_j=2^{j-2}+\mathbf{1}_{\{j\ \mathrm{even}\}}.
\]
The nonempty maximal zero-block lengths in the infinite Baum–Sweet word \(b(0)b(1)\cdots\) are **exactly**
\[
 \boxed{\{1,2\}\ \cup\ \{h_j:j\ge4\}=\{1,2,5,8,17,32,65,128,257,\ldots\}.}
\]
Each listed length occurs infinitely often; no unlisted length occurs.

For every integer \(K\ge2\), the prefix \(b(0)\cdots b(2^K-1)\) begins and ends in \(1\). Denoting by \(Z_K(\ell)\) its number of maximal zero blocks of length \(\ell\), the **exact simultaneous frequency formula** is
\[
 \boxed{\begin{aligned}
 Z_K(1)&=\lfloor K/2\rfloor,\\
 Z_K(2)&=F_{K+1}-2,\\
 Z_K(h_j)&=F_{K-j+2}-1\quad(4\le j<K),
 \end{aligned}}
\]
with all other counts zero; a displayed \(h_j\) with \(j\ge K\) has count zero. Let \(\varphi=(1+\sqrt5)/2\). Among the completed nonempty zero blocks of these prefixes, the relative frequencies converge as \(K\to\infty\) to
\[
 \boxed{\Pr(\ell=1)=0,\qquad\Pr(\ell=2)=\varphi^{-1},\qquad
 \Pr(\ell=h_j)=\varphi^{-j}\ (j\ge4).}
\]
These probabilities sum to one.

## Assumptions and scope
The digit test ignores leading zeros. The special value \(b(0)=1\) corresponds to the empty binary representation convention. A maximal zero block is a nonempty contiguous set of zero-valued sequence positions adjacent on either side to ones (the right neighbor exists in this nonperiodic infinite word). The exact counts and limiting frequencies refer to dyadic prefixes of length \(2^K\), **not** an asserted arbitrary-cutoff frequency limit. Every dyadic prefix ends with a one, so there is no censored final zero block.

## Proof
**1. Binary language of one positions.** A positive integer has \(b(n)=1\) exactly when its ordinary binary expansion belongs to \(1(1\mid00)^*\). Indeed, after the leading one, each run of zeros is a concatenation of the token \(00\), while each further one is the token \(1\). In particular, if \(\mathcal L_L\) is the ascending list of length-\(L\) binary strings belonging to \((1\mid00)^*\), then \(|\mathcal L_L|=F_{L+1}\), with \(\mathcal L_0=\{\varepsilon\}\), \(\mathcal L_1=\{1\}\), and, for \(L\ge2\), the lexicographically ordered disjoint union
\[
 \mathcal L_L=00\mathcal L_{L-2}\ \sqcup\ 1\mathcal L_{L-1}.
\]
Within each piece, consecutive numerical differences are those of the shorter list. At their single interface, the last word in the left piece is \(00\,1^{L-2}\), representing \(2^{L-2}-1\). The first word in the right piece is \(1\,u\), where \(u\) is the smallest admissible length-\((L-1)\) suffix: it is \(0^{L-1}\) when \(L-1\) is even and \(0^{L-2}1\) otherwise. Thus the interface difference is
\[
 G_L=2^{L-2}+1+\mathbf{1}_{\{L\ \mathrm{even}\}},\qquad L\ge2.
\]
By induction the possible differences between consecutive entries inside any \(\mathcal L_L\) are precisely interface differences \(G_j\) from recursive suffix lists of lengths \(2\le j\le L\), with multiplicities counted below.

**2. Between successive binary lengths.** At binary length \(t\ge1\), the largest one-position is \(2^t-1\) (all digits one). The smallest one-position of length \(t+1\) is \(2^t\) when \(t\) is even and \(2^t+1\) when \(t\) is odd. Consequently the intervening gaps have respective differences one and two. There is also the initial difference one between positions zero and one. Since \(G_2=G_3=3\), while the strictly increasing \(G_j\), \(j\ge4\), begin \(6,9,18,33,66,129,\ldots\), the complete consecutive-one gap spectrum is \(\{1,2,3\}\cup\{G_j:j\ge4\}\). Subtracting one from each gap above one proves the asserted zero-block spectrum and its exclusion clause.

**3. Exact multiplicities.** For \(K\ge2\), the ones in \([0,2^K)\) consist of zero and all binary-length groups \(1,\ldots,K\). Their number is
\[
 1+\sum_{L=0}^{K-1}F_{L+1}=F_{K+2}.
\]
The \(K\) gaps between groups (including zero to one) yield \(\lceil K/2\rceil\) gaps of size one and \(\lfloor K/2\rfloor\) of size two. For a fixed suffix interface length \(j\ge2\) appearing inside a length-\(L\) suffix list, there is exactly one such interface for each legal token prefix of length \(L-j\), hence exactly \(F_{L-j+1}\) instances. Summing over \(j\le L\le K-1\) gives
\[
 C_{K,j}=\sum_{r=0}^{K-1-j}F_{r+1}=F_{K-j+2}-1\quad(2\le j<K),
\]
interpreting an empty sum as zero. The two interfaces \(j=2,3\) both have difference three; their combined count is \(C_{K,2}+C_{K,3}=F_{K+1}-2\). Every \(j\ge4\) has its distinct interface difference \(G_j\), giving the other formula. Because \(F_{K-j+2}-1>0\) for \(K\ge j+1\), each \(G_j\) occurs in all sufficiently large dyadic prefixes. The boundary gap two also occurs for arbitrarily many binary lengths; hence every nonempty listed zero-block length occurs infinitely often.

**4. Frequency limit.** Among the \(F_{K+2}-1\) consecutive-one gaps, just \(\lceil K/2\rceil\) have size one. Thus the number of nonempty zero blocks is \(F_{K+2}-1-\lceil K/2\rceil\). Binet asymptotics yield
\[
 \frac{F_{K+1}-2}{F_{K+2}-1-\lceil K/2\rceil}\longrightarrow\varphi^{-1},\qquad
 \frac{F_{K-j+2}-1}{F_{K+2}-1-\lceil K/2\rceil}\longrightarrow\varphi^{-j}
\]
for each fixed \(j\ge4\). The length-one count grows only linearly in \(K\), hence has limit frequency zero. Finally \(\sum_{j\ge4}\varphi^{-j}=\varphi^{-2}\), and \(\varphi^{-1}+\varphi^{-2}=1\), establishing that there is no escaped mass.

## Verification
The accompanying standalone Python 3 script `verify.py` computes \(262144\) terms independently from the binary zero-run definition and from the exact three-branch recurrence, and checks every exact dyadic formula for \(1\le K\le18\). It also tests the two-group interface identity by independently enumerating admissible fixed-length binary strings up to length thirteen. Run `python3 verify.py`. Its expected output is `VERIFY_OK direct_terms=262144 dyadic_cutoffs=18 symbolic_central_boundaries=12 exact_counts=all`. These finite tests do not establish the infinite theorem; the token decomposition and Fibonacci sum above do.

## Relationship to prior work
Merta, *Composition inverses of the variations of the Baum–Sweet sequence* (2018), §2, supplies the classical recurrence, unbounded-zero-run fact and a two-group decomposition of one positions, and proves parity/Fibonacci structure. Its Theorem 4.6 concerns first differences of the one positions of a **different formal-inverse sequence**; it is not a gap-spectrum theorem for the original Baum–Sweet word. OEIS A060142 lists the Baum–Sweet one-position set, including its basic generator, but does not give this exact zero-run spectrum or dyadic frequency law. Shallit and Xu (2023) investigate repetition factorizations for other automatic words, a distinct factorization problem. The zero-block spectrum and its exact multiscale frequency profile are not statements established by these inspected sources.

## Limitations
This result concerns one specific infinite binary automatic word, and the frequency law is established along dyadic cutoffs. The proof does not assert a global frequency limit for arbitrary prefix lengths, any limit law for starting positions scaled by index, or a probabilistic model of independent runs. It does not settle new formal-inverse questions. An earlier equivalent derivation, especially one not indexed by standard bibliographic search, cannot be excluded by the present comparison alone.

## References
- Ł. Merta, *Composition inverses of the variations of the Baum–Sweet sequence*, arXiv:1803.00292v1, first posted 2018-03-01, https://arxiv.org/html/1803.00292v1 (especially §2 and Theorem 4.6).
- J. Shallit and X. Xu, *Repetition factorization of automatic sequences*, arXiv:2311.14961v1, first posted 2023-11-25, https://arxiv.org/html/2311.14961v2.
- OEIS A060142, *Ordered set defined by \(0\in S\), \(x\in S\Rightarrow 2x+1,4x\in S\)*, https://oeis.org/A060142 (one-position set).
- C. Kimberling, *A Self-Generating Set and the Golden Mean*, Journal of Integer Sequences 3 (2000), Article 00.2.8, https://cs.uwaterloo.ca/journals/JIS/VOL3/goldentext.html (a different Fibonacci-related generated set).
