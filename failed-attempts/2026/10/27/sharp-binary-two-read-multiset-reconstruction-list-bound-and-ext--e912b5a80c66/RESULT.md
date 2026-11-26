# Sharp binary two-read multiset reconstruction-list bound and extremal profiles
## Finding
For each binary word \(w=w_1\cdots w_n\) of length \(n\ge3\), the observation \(\mathcal S_2(w)\) is the **multiset** of its \(n-1\) consecutive two-symbol substrings, without their positions but retaining their multiplicities. Write \(\mathcal F(s)=\{w\in\{0,1\}^n:\mathcal S_2(w)=s\}\). The worst possible reconstruction-list size is \(M_n=\max_s|\mathcal F(s)|\), over attainable observations.

Set \(m=n-1\), \(u=\lfloor(m-2)/2\rfloor\), and \(v=\lceil(m-2)/2\rceil\). For every integer \(0\le k\le u\), put
\[
F_m(k)=\frac{m}{k+1}\binom uk\binom vk.
\]
Then the **exact worst reconstruction list** and every maximizing observation are
\[
M_n=\max_{0\le k\le u}F_m(k),\qquad
k_*=\max\left\{0,\left\lceil\frac{uv-2}{u+v+3}\right\rceil\right\},\qquad M_n=F_m(k_*).
\]
The only maximizing indices are \(k_*\) and, when the displayed fraction is an integer and \(k_*+1\le u\), also \(k_*+1\).

To classify the maximizing observations, write \(a,b,c,d\) for the multiplicities of \(00,01,10,11\). For every maximizing index \(k\), let \(t=k+1\). Necessarily and sufficiently \(b=c=t\), \(a+d=m-2t\), and either (i) \(k=0\), with **every** nonnegative split \((a,d)\) allowed, or (ii) \(k\ge1\), with \(|a-d|\le1\). No imbalanced transition-count observation maximizes.

The theorem provides an exact worst-case uncertainty bound for reconstruction from unordered, multiplicity-preserving adjacent reads. For example \(M_{10}=54\), attained by four observations, whereas \(M_{18}=8330\), attained by four observations.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), the source is a **linear** (not cyclic) word, every adjacent read is observed once, and only the positions of reads are forgotten. The observation is a multiset, not merely a set of distinct reads. No read errors, losses, or insertions are permitted. Length \(n\) is known and satisfies \(n\ge3\).

For clarity, an attainable multiplicity profile is a nonnegative integer quadruple \((a,b,c,d)\) summing to \(m\). The labels represent counts of reads \(00,01,10,11\). A profile can arise only when \(|b-c|\le1\), except that with \(b=c=0\) there are only the two constant-word profiles.

## Proof
**Step 1 (exact fibers).** Decompose any word into its maximal constant runs and distribute the same-symbol adjacent-pair counts as nonnegative extra symbols among the runs. If \(b=c=t\ge1\), there are \(t+1\) runs of the first endpoint symbol and \(t\) of the other. Both endpoint symbols are possible, so stars-and-bars gives
\[
|\mathcal F(a,t,t,d)|=\binom{a+t}{t}\binom{d+t-1}{t-1}
 +\binom{a+t-1}{t-1}\binom{d+t}{t}
 =\frac{m}{t}\binom{a+t-1}{t-1}\binom{d+t-1}{t-1}.
\]
The last equality uses \(a+d+2t=m\). If \(b=c+1=t\ge1\), the endpoints are forced (start at zero, end at one) and each symbol has \(t\) runs, giving
\[
|\mathcal F(a,t,t-1,d)|=\binom{a+t-1}{t-1}\binom{d+t-1}{t-1}.
\]
The case \(c=b+1\) is symmetric. When \(b=c=0\), only the constant words occur, each with a singleton fiber. These formulas characterize every attainable profile.

**Step 2 (optimize the balanced class).** Put \(k=t-1\), \(L=a+k\), \(R=d+k\); then \(L+R=m-2\) and the fiber is \(m\binom Lk\binom Rk/(k+1)\). For \(k\ge1\), the ratio of the products for \((L+1,R-1)\) and \((L,R)\) is
\[
\frac{L+1}{L+1-k}\frac{R-k}{R}.
\]
It strictly favors moving one unit toward balance until \(|L-R|\le1\). Thus the maximum at fixed \(k\ge1\) has \(L=u,R=v\) in either order; for \(k=0\) every split gives \(m\). This yields the stated \(F_m(k)\) and equality profiles.

**Step 3 (identify maximizing transition counts).** Direct cancellation gives
\[
\frac{F_m(k+1)}{F_m(k)}=\frac{(u-k)(v-k)}{(k+1)(k+2)}\quad(0\le k<u).
\]
The numerator minus denominator in this ratio is \(uv-2-(u+v+3)k\), strictly decreasing in \(k\). Hence the sequence first increases and then decreases, with a tie only at an integral threshold. This proves the explicit value of \(k_*\) and the complete tie rule.

**Step 4 (imbalanced classes cannot maximize).** By exchanging symbols, take \(b=t\), \(c=t-1\), and write \(U=\binom{a+t-1}{t-1}\binom{d+t-1}{t-1}\). If \(t=1\), then \(U=1<M_n\), because a balanced profile with one transition each has size \(m\ge2\).

Suppose \(t\ge2\). If \(a\ge t-1\), compare with balanced \((a-1,t,t,d)\), having the same total number \(m\) of adjacent reads. The ratio of its fiber size to \(U\) is
\[
\frac{ma}{t(a+t-1)}\ge1,
\]
since \(m=a+d+2t-1\ge3t-2\ge2t\) and \(a\ge t-1\). Equality can occur only when \(t=2\), \(a=1\), \(d=0\), \(m=4\); then \(U=2<M_5=4\).

If instead \(a\le t-2\), compare with balanced \((a+1,t-1,t-1,d)\). The ratio is
\[
\frac{m(t-1)}{(a+1)(d+t-1)}>1,
\]
because the numerator-minus-denominator of this last ratio is \(2(t-1)^2+d(t-2-a)>0\). Thus every imbalanced fiber is strictly smaller than some balanced fiber, or is the exceptional size-two fiber dominated by the balanced maximum. Constant fibers have size one. Steps 1–4 establish the exact maximum and **all** equality observations for every \(n\ge3\).

## Verification
The standalone pure-Python checker `verify_bigram.py` constructs all source words of lengths \(3\) through \(18\), groups them by their literal four-count profiles, and compares the complete frequency tables with the exact formulas and the classified maximizing profiles. It checks \(524280\) words and \(1524\) observed profiles. A further exact-integer parameter sweep checks \(1718065\) realizable profiles for lengths \(19\) through \(190\). The checked output is saved in `verify_bigram.out`; it ends with `VERIFY_OK`. Execute with `python3 verify_bigram.py` in the extracted artifact directory. The infinite-parameter result is proved by the preceding inequalities, not inferred from enumeration.

## Relationship to prior work
The published study *Exact binary two-multispectrum code size and singleton classification* determines how many **different** two-read multispectra are realizable, and characterizes the fibers of size one. Its run decomposition also gives the individual-fiber counting mechanism used as background here. Neither that count of spectral classes nor its singleton classification establishes the **largest** fiber among all profiles or the exact complete family of maximizers; those require the two-variable binomial optimization, threshold, and global exclusion of imbalanced endpoint counts above.

He, Kari, and Millan Arias (2025) connect complete k-mer multiplicities with Eulerian traversal in de Bruijn graphs, establishing reconstruction feasibility and an individual reconstruction route. Chakraborty et al. (2026) study spectrum-preserving string-set presentations and compression, not worst-case binary inverse fibers with length-two read counts. Classical Markov-type enumeration offers related individual-class-count formulas, often in cyclic/endpoint-conditioned variants. The present calculation isolates the full **linear, free-endpoint** reconstruction ambiguity rather than counting the number of types or giving one witness per type.

## Limitations
The result does not cover longer reads, nonbinary alphabets, cyclic strings, partial spectra, noise, or efficient general-purpose reconstruction. The fiber formula has precedents in elementary stars-and-bars/Markov-type calculations; **the new claim is the sharp global maximization and exact extremal classification**, not discovery of run decompositions. An equivalent optimizer could occur under Markov-type or graph-trail terminology in literature not indexed by the checked databases.

## References
1. H. He, L. Kari, and P. Millan Arias, *Bridging Chaos Game Representations and k-mer Frequencies of DNA Sequences*, arXiv:2506.22172v1 (first public version June 27, 2025). https://arxiv.org/html/2506.22172v1
2. S. Chakraborty and collaborators, *Variations on the Problem of Identifying Spectrum-Preserving String Sets*, arXiv:2602.19408v1 (February 2026). https://arxiv.org/html/2602.19408v1
3. *Exact binary two-multispectrum code size and singleton classification*, published mathematical result (October 2026), published-finding corpus record 13779c08da71. https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71/RESULT.md
4. P. Jacquet, C. Knessl, and W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768.
5. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548v1 (2018), DOI:10.1109/TIT.2019.2935973.
