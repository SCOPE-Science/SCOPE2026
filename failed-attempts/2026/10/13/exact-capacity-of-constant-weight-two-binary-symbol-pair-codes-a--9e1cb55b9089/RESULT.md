# Exact capacity of constant-weight-two binary symbol-pair codes at distance four

## Finding

**Theorem.** For every integer \(n\ge3\), let \(A_{\rm pw2}(n,4)\) be the largest cardinality of a set \(\mathcal C\subseteq\{0,1\}^{n}\) with every word of Hamming weight exactly two and every pair of distinct words at *cyclic symbol-pair distance* at least four. Then
\[
A_{\rm pw2}(n,4)=\left\lfloor\frac{n\lfloor n/2\rfloor}{2}\right\rfloor.
\]
Every bound is attained by an explicit construction, including both congruence classes of odd lengths. In particular, the optimum equals \(n^2/4\) for even \(n\), and \(\lfloor n(n-1)/4\rfloor\) for odd \(n\).

## Assumptions and scope

Indices are the cyclic group \(\mathbb Z/n\mathbb Z\), and all alphabets are binary. For \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\), define the pair-read map by \(\pi(x)_i=(x_i,x_{i+1})\). The symbol-pair distance \(d_{\rm p}(x,y)\) is the number of indices \(i\) for which \(\pi(x)_i\ne\pi(y)_i\). A binary word of Hamming weight exactly two is identified with the unordered two-element set of coordinates holding ones. Empty codes are allowed but are never optimal. The minimum-distance condition quantifies over distinct pairs; it is vacuous for a singleton code (in particular at \(n=3\)). No linearity, cyclic invariance of the code, or additional pair-weight restriction is imposed.

## Proof

**1. Reduction to a graph with independent neighborhoods.** Identify each word with an edge \(\{a,b\}\) in a simple graph \(G\) on the cyclically ordered vertex set \(\mathbb Z/n\mathbb Z\). For two words, let \(T\) be the symmetric difference of their supports. Their pair-read vectors differ at precisely the indices in \(T\cup(T-1)\). If the supports are disjoint, then \(|T|=4\), so the pair-distance is at least four. If the supports meet at a single vertex, their symmetric difference is \(T=\{j,k\}\). In that case \(|T\cup(T-1)|\) is three when \(j\) and \(k\) are adjacent on the coordinate cycle, and four otherwise. Consequently, the code has minimum pair-distance at least four **if and only if**, for every vertex \(i\), no two vertices in its graph neighborhood \(N_G(i)\) are consecutive on the coordinate cycle \(C_n\).

**2. Upper bound.** Each \(N_G(i)\) is an independent vertex set of \(C_n\). Since \(\alpha(C_n)=\lfloor n/2\rfloor\) for every \(n\ge3\), we have \(\deg_G(i)\le \lfloor n/2\rfloor\). Summing degrees gives
\[
2|E(G)|\le n\lfloor n/2\rfloor,
\]
and thus the required upper bound after taking the integer part.

**3. Construction for even lengths.** Let \(n=2k\) with \(k\ge2\). Take the complete bipartite graph between even and odd residue classes in \(\mathbb Z/n\mathbb Z\). Every neighborhood is entirely in one parity class, hence is independent in \(C_n\). There are exactly \(k^2=n\lfloor n/2\rfloor/2\) edges.

**4. Construction for odd lengths with even half-length.** Let \(n=2k+1\), where \(k\) is positive and even. Set
\[
D=\{\pm1,\pm3,\ldots,\pm(k-1)\}\subset\mathbb Z/n\mathbb Z,
\]
and join each vertex \(i\) to all \(i+d\), for \(d\in D\). The elements of \(D\) have successive circular gaps equal to two, apart from one gap of three. Thus no two are adjacent on \(C_n\). This graph is \(k\)-regular and has \(nk/2\) edges, attaining the bound.

**5. Construction for odd lengths with odd half-length.** Let \(n=2k+1\), where \(k\) is odd. Begin with the circulant graph with step set
\[
D_0=\{\pm1,\pm3,\ldots,\pm(k-2)\};
\]
for \(k=1\), this set is empty. It is \((k-1)\)-regular and every neighborhood is independent in \(C_n\). Because \(\gcd(k,2k+1)=1\), the graph \(H\) of step-\(k\) edges \(\{i,i+k\}\) is a single odd cycle on all \(n\) vertices. Select a matching of size \(k\) in \(H\) and add its edges to the original graph. Every vertex receives at most one additional neighbor, at displacement either \(+k\) or \(-k\). For \(k\ge3\), the only originally large circular gap in \(D_0\) has length five, and either new displacement \(\pm k\) divides it into gaps of lengths two and three. Hence the neighborhood-independence property is preserved. When \(k=1\), the initial graph is empty and the same property is immediate. The added matching is edge-disjoint from the base graph. The final edge count is
\[
\frac{n(k-1)}2+k=\frac{nk-1}{2}=\left\lfloor\frac{nk}{2}\right\rfloor.
\]
This is again exactly the upper bound. All integer \(n\ge3\) are covered, proving the theorem.

## Verification

The standalone standard-library script `verify_pairweight2.py` constructs the above graphs for every \(3\le n\le120\) and checks the exact cardinality and cyclic-neighborhood condition. For \(n\le15\), it additionally computes pair-read sequences of all codewords and checks every distinct pair directly. It independently constructs the full conflict graph on the \(\binom n2\) candidate supports and carries out exhaustive, memoized maximum-independent-set branching for \(3\le n\le11\); these exact optima equal the formula in every case. All script checks completed successfully. Finite computation is supplementary: the proof above establishes the infinite-family result without numerical extrapolation.

For reproducibility, run `python3 verify_pairweight2.py` with an ordinary Python 3 interpreter. The initial exact values for \(n=3,4,\ldots,11\) are \(1,4,5,9,10,16,18,25,27\).

## Relationship to prior work

Cassuto and Blaum introduced symbol-pair coding and its storage-channel motivation [1]. Chee and coauthors developed Singleton bounds and unrestricted MDS constructions [2]. Elishco, Gabrys, and Yaakobi developed further unrestricted bounds, including Johnson-type inequalities, and constructions [3]. Zhao and Chang studied codes of *constant symbol-pair weight*, including separate pair-weights three and four [4]. Here the restriction is instead **constant Hamming weight two**. Such words have symbol-pair weight three when their two ones are adjacent, and weight four otherwise, so the present optimization allows a mix of those pair-weight layers. The cited sources do not, in the material inspected, establish the exact mixed-layer all-length formula or its parity-sensitive construction. The full text of [4] was not accessible for definitive comparison, leaving a residual bibliographic uncertainty.

## Limitations

The theorem applies only to binary words of **Hamming weight exactly two**, cyclic pair reads, minimum pair-distance four, and length at least three. It does not determine maxima for other Hamming weights, distances or alphabets; it does not assert the number of extremal codes or their symmetry classes. The structural neighborhood condition is an equivalence in this narrowly defined domain, not a general reduction for arbitrary symbol-pair codes. Originality comparisons cannot rule out obscure or unindexed earlier results; specifically, the full text of [4] was unavailable.

## References

[1] Y. Cassuto and M. Blaum, “Codes for symbol-pair read channels,” IEEE ISIT (2010), pp. 988–992, DOI `10.1109/ISIT.2010.5513753`.

[2] Y. M. Chee, L. Ji, H. M. Kiah, C. Wang, and J. Yin, “Maximum Distance Separable Codes for Symbol-Pair Read Channels,” arXiv:1211.1728 (first submitted November 7, 2012), DOI `10.1109/TIT.2013.2276615`.

[3] O. Elishco, R. Gabrys, and E. Yaakobi, “Bounds and Constructions of Codes over Symbol-Pair Read Channels,” IEEE Transactions on Information Theory 66 (2020), 1385–1395, DOI `10.1109/TIT.2019.2942283`.

[4] M. Zhao and Y. Chang, “Bounds and constructions of optimal symbol-pair codes with constant pair-weight,” Designs, Codes and Cryptography 93 (2025), 2297–2316, DOI `10.1007/s10623-025-01598-9`.
