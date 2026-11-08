# Exact degree distribution of the binary one-grain confusability graph

## Finding
For each integer \(n\ge 1\), let \(G_n\) be the simple confusability graph of the length-\(n\) binary channel permitting zero or one overwrite of a symbol by its immediate predecessor. Let \(P_n(z)=\sum_{x\in\{0,1\}^n} z^{\deg_{G_n}(x)}\). We determine \(P_n\) for **every** \(n\) by an explicit binomial run-composition sum, together with the individual degree formula, graph edge count, and all maximum-degree words.

For \(n=1\), \(P_1(z)=2\). For \(n\ge2\), write \(N=n-1\), \(t_i=x_i\oplus x_{i+1}\) for \(1\le i\le N\), \(k=\sum_i t_i\), and \(b=\sum_{i=1}^{N-1}{\bf1}_{t_i\ne t_{i+1}}\). Then
\[
\deg_{G_n}(x)=N+k(N-k+1)-t_1-b. \tag{1}
\]
The polynomial can be evaluated with no word-by-word search as follows. Begin with the two constant-derivative contributions
\[
P_n(z)=2z^N+2z^{2N-1}+\text{interior contributions}. \tag{2}
\]
For every \(1\le k\le N-1\), set \(m=N-k\) and \(Q=N+k(m+1)\). Add the following four contributions, summing over all nonnegative integers \(r\) and interpreting out-of-range binomial coefficients as zero:
\[
\begin{aligned}
&2\binom{k-1}{r}\binom{m-1}{r}z^{Q-(2r+1)};\\
&2\binom{k-1}{r}\binom{m-1}{r}z^{Q-(2r+2)};\\
&2\binom{k-1}{r-1}\binom{m-1}{r}z^{Q-2r}\qquad (r\ge1);\\
&2\binom{k-1}{r}\binom{m-1}{r-1}z^{Q-(2r+1)}\quad (r\ge1).
\end{aligned} \tag{3}
\]
All nonzero terms are nonnegative and have nonnegative integer exponents. Equations (2)–(3) are the **complete degree-distribution polynomial**, including multiplicities.

In particular, for \(n\ge2\),
\[
|E(G_n)|=2^{n-3}(n-1)(n+2). \tag{4}
\]
For \(n\ge3\), the maximum degree and its exact extremizers are
\[
\Delta(G_n)=n-2+\left\lfloor\frac{n^2}{4}\right\rfloor, \tag{5}
\]
attained precisely when the derivative is \(0^{N-k}1^k\) with \(k\) a maximizing integer in \(1\le k\le N\) for \(k(n-k)\). Consequently there are two maximum-degree words for every even \(n\ge4\), and four for every odd \(n\ge3\), allowing either initial source bit. At \(n=2\), all four words have degree one; at \(n=1\), both words have degree zero.

## Assumptions and scope
A word is an indexed, linear binary block \(x=(x_1,\ldots,x_n)\). At most one error may occur. An error at index \(j\in\{2,\ldots,n\}\) replaces \(x_j\) by the **original** \(x_{j-1}\); if these values are equal, the output is unchanged. The channel ball is
\[
B_n(x)=\{x\}\cup\{x\oplus e_j:2\le j\le n,\ x_{j-1}\ne x_j\},
\]
where \(e_j\) has its sole nonzero entry at index \(j\). Distinct vertices are adjacent precisely when their channel balls intersect. No circular boundary or two-error operation is allowed. The degree is the number of **other source words** confusable with a source word, not the number of outputs of its channel ball.

## Proof
**1. Characterize possible confusable pairs.** Every channel output differs from its input in at most one coordinate, never the first. Consequently, confusable distinct words must agree in their first coordinate and have Hamming distance either one or two. All single-coordinate changes at indices \(j\ge2\) are confusable: if \(x_{j-1}\ne x_j\), the original word can overwrite to its bit-flipped neighbor, while otherwise the neighbor can overwrite back to the original. This supplies \(N\) neighbors.

For words differing at exactly two indices \(i<j\), both must be at least two. A common output can only be one of the two intermediate bit-flips, so the conditions can be checked directly. If \(j\ge i+2\), the flip of \(i\) is permitted by one source and the flip of \(j\) by the other precisely when \(t_{i-1}\ne t_{j-1}\); the two possible intermediate outputs correspond to the two opposite orderings. Among all pairs of derivative positions, there are \(k(N-k)\) with unequal entries; excluding the \(b\) adjacent derivative pairs leaves \(k(N-k)-b\) eligible nonadjacent coordinate pairs. If \(j=i+1\), checking the two intermediates gives eligibility exactly when \(t_i=1\), independently of \(t_{i-1}\). These supply \(\sum_{i=2}^N t_i=k-t_1\) neighbors. There is no double counting between one-flip and two-flip cases, nor between distinct flipped coordinate pairs. Hence
\[
\deg(x)=N+(k-t_1)+(k(N-k)-b),
\]
which is (1), for every \(n\ge2\).

**2. Enumerate every degree multiplicity.** Each derivative of length \(N\) corresponds to exactly two source words, according to the freely chosen first symbol. The all-zero derivative has \(k=0\) and degree \(N\), while the all-one derivative has \(k=N\), \(t_1=1\), \(b=0\), and degree \(2N-1\); this gives the first two terms of (2). For \(0<k<N\), the derivative contains \(k\) ones and \(m=N-k\) zeros. A derivative starting with zero and having \(2r+1\) changes consists of \(r+1\) nonempty runs of each symbol, counted by \(\binom{k-1}{r}\binom{m-1}{r}\); the degree is \(Q-(2r+1)\). Starting with one gives the same count with degree \(Q-(2r+2)\). With \(2r\ge2\) changes, a derivative starting with zero has \(r\) one-runs and \(r+1\) zero-runs, counted by \(\binom{k-1}{r-1}\binom{m-1}{r}\), and degree \(Q-2r\). Starting with one interchanges these run counts, giving \(\binom{k-1}{r}\binom{m-1}{r-1}\) and degree \(Q-(2r+1)\). Multiplying each by two for the first source bit proves (2)–(3), exhaustively and without overcounting.

**3. Count graph edges.** Under uniform choice of the source word, its derivative bits are independent fair bits. Thus \(\mathbb E[k]=N/2\), \(\mathbb E[k^2]=N(N+1)/4\), \(\mathbb E[t_1]=1/2\), and \(\mathbb E[b]=(N-1)/2\). Equation (1) gives \(\mathbb E[\deg]=N(N+3)/4\). The handshaking lemma over all \(2^n\) vertices yields (4). For \(n=2\), the apparently fractional factor \(2^{-1}\) produces the integer two and agrees with the direct graph.

**4. Determine the extremizers.** If \(k=0\), the degree is \(N\). If \(k>0\), the nonnegative penalty \(t_1+b\) is at least one. Equality holds precisely for derivatives \(0^{N-k}1^k\): either there is a single transition from zero to one (if \(0<k<N\)), or all bits are one (if \(k=N\)). Hence for \(k>0\), \(\deg(x)\le N+k(n-k)-1\). For every \(n\ge3\), the global maximum beats the \(k=0\) degree and is attained by the indicated monotone derivatives with \(k\) maximizing \(k(n-k)\). This proves (5) and all extremizer counts. The two shorter lengths are checked directly from the definition.

## Verification
The self-contained scripts `verify_graph.py` and `verify_formula.py` use standard Python only. Running `python3 verify_graph.py` enumerates every channel ball and every pair of distinct binary words for \(1\le n\le9\) and independently checks (1), (4), (5), and the number of maximizers. Running `python3 verify_formula.py` independently enumerates all derivatives through \(n=18\), constructs the run-composition polynomial (2)–(3), and compares every coefficient and edge count. Both scripts completed successfully. These finite checks are **supplementary**; the proof above establishes the formulas for all positive lengths.

As concrete checkpoints the edge counts for \(n=2,3,4,5,6,7,8,9\) are \(2,10,36,112,320,864,2240,5632\). At \(n=6\), the complete histogram, as \((\text{degree},\text{number of words})\) pairs, is \((5,2),(8,8),(9,12),(10,16),(11,16),(12,8),(13,2)\).

## Relationship to prior work
Mazumdar–Barg–Kashyap (2010), Kashyap–Zémor (2013), and Gabrys–Yaakobi–Dolecek (2013) establish the granular overwrite channel, define its confusability graph, and study correcting-code bounds and constructions. Sharov–Roth (2013) additionally develop weighted path counts for confusable *pairs* in a wider grain channel and asymptotic code-rate bounds. These are significant prior work and may implicitly yield aggregate edge counts; the edge count (4) alone is not claimed as an independently new topic. The present result refines aggregate counts to **the exact degree of every source**, the **complete all-length degree distribution** and **every maximum-degree source**. The previously known one-grain output-ball cardinality \(1+k\) does not determine the degree of the input confusability graph: the new value depends additionally on the orientation and changes of the derivative. For instance at length \(n=5\), derivatives \(1100\) and \(1010\) both have \(k=2\) and identically sized output balls, but graph degrees \(8\) and \(6\), respectively.

The closest published searches concerned small optimal one-grain codebooks, deletion-channel confusability edges, and duplication-channel confusability edges. Those statements do not imply (1)–(3) for the present channel. An unindexed equivalent vertex-degree analysis remains a historical-priority risk.

## Limitations
The result is for at most **one** binary overwrite and linear, indexed blocks. It does not give optimal one-grain code sizes, chromatic numbers, asymptotic capacity, or the degree spectrum for more than one grain error, q-ary alphabets, or circular boundary conditions. A complete historical-priority assessment and independent mathematical audit remain outstanding. The degree distribution itself is proved rather than inferred only from computation.

## References
- A. Mazumdar, A. Barg, N. Kashyap, *Coding for High-Density Recording on a 1-D Granular Magnetic Medium*, arXiv:1012.1895, public preprint 2010-12-08. https://arxiv.org/abs/1012.1895
- N. Kashyap and G. Zémor, *Upper Bounds on the Size of Grain-Correcting Codes*, arXiv:1302.6154, public preprint 2013-02-25. https://arxiv.org/abs/1302.6154
- R. Gabrys, E. Yaakobi, L. Dolecek, *Correcting Grain-Errors in Magnetic Media*, arXiv:1307.7087, public preprint 2013-07-26. https://arxiv.org/abs/1307.7087
- A. Sharov and R. M. Roth, *Bounds and Constructions for Granular Media Coding*, IEEE Transactions on Information Theory (2013), lawful full text https://ronny.cswp.cs.technion.ac.il/wp-content/uploads/sites/54/2016/05/grains.pdf
- D. Cullina and N. Kiyavash, *Generalized Sphere-Packing and Sphere-Covering Bounds on the Size of Codes for Combinatorial Channels*, arXiv:1405.1464 (2014). https://arxiv.org/abs/1405.1464
