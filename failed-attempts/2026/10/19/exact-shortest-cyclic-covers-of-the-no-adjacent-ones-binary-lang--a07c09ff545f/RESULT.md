# Exact shortest cyclic covers of the no-adjacent-ones binary language

## Finding
For an integer \(k\ge 2\), let \(\mathcal L_k\) be the set of binary words of length \(k\) having no occurrence of `11`. Let \(B(k)\) be the minimum length of a **cyclic** binary word in which every member of \(\mathcal L_k\) occurs as a contiguous cyclic factor of length \(k\). The host word is not assumed to avoid `11`. With Fibonacci numbers \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\), one has

\[
\boxed{B(k)=F_{k+2}+F_k-1=L_{k+1}-1\qquad(k\ge2),}
\]
where \(L_j=F_{j-1}+F_{j+1}\) are the Lucas numbers. An optimum can be constructed with *no* cyclic occurrence of `11`. The additional cyclic factor occurrences required beyond the \(F_{k+2}\) distinct target factors are exactly \(F_k-1\). An explicit choice of repetitions is given in the proof.

## Assumptions and scope
A cyclic word of length \(N\) is a sequence of \(N\) binary symbols with indices modulo \(N\); its factor of length \(k\) at a position reads the next \(k\) symbols, allowing wraparound. The theorem concerns every integer \(k\ge2\) and unrestricted binary cyclic hosts. It is not a theorem about scattered subsequences, linear shortest common superstrings, or hosts required to contain every binary word. For \(k=2\), the optimum is the cyclic word `001`, of length \(3\).

Put \(m=k-1\). A length-\(k\) word \(z\) is a directed edge from its prefix \(z_0\cdots z_{m-1}\) to its suffix \(z_1\cdots z_m\) in the order-\(m\) binary de Bruijn digraph. A cyclic host traces a closed directed walk of length equal to its number of symbols, and its consecutive length-\(k\) factors are precisely the edge labels of that walk. The target edges \(E\) are exactly \(\mathcal L_k\), so \(|E|=F_{k+2}\).

## Proof
**1. A dual potential and the lower bound.** For a binary vertex \(v\in\{0,1\}^{m}\), let \(\lambda(v)\) be the zero-based position of its *first* `1` if one exists, and put \(\lambda(0^m)=0\). Define the integer potential \(p(v)=-\lambda(v)\). For every de Bruijn edge \(z:a\to b\), even if \(z\) contains `11`,

\[
p(b)-p(a)\le1.
\]
Indeed, if \(a\) begins with `0` and contains a `1`, shifting left moves its first `1` one position closer to the start, giving equality. Otherwise \(p(a)=0\) and \(p(b)\le0\).

Restrict now to the legal length-\(m\) vertices (those avoiding `11`). The outdegree and indegree from the required edges are respectively

\[
d_E^+(v)=1+\mathbf1_{\{v\text{ ends with }0\}},\qquad
 d_E^-(v)=1+\mathbf1_{\{v\text{ begins with }0\}}.
\]
Consequently,

\[
\begin{aligned}
\sum_{z\in E}\big(p(\operatorname{suffix}(z))-p(\operatorname{prefix}(z))\big)
&=\sum_v\big(d_E^-(v)-d_E^+(v)\big)p(v)\\
&=-\sum_{\substack{v\text{ legal};\;v\text{ begins }0\\v\text{ ends }1}}\lambda(v).
\end{aligned}
\]
For any such vertex, \(\lambda(v)\) counts the positive integers \(j\) for which the first \(j\) symbols are all `0`. The number of legal length-\(m\) words beginning with \(j\) zeros and ending in `1` is \(F_{m-j}\), for \(1\le j<m\). Hence

\[
\sum_{\substack{v\text{ legal};\;v\text{ begins }0\\v\text{ ends }1}}\lambda(v)
=\sum_{j=1}^{m-1}F_{m-j}=F_{m+1}-1=F_k-1,
\]
where the sum is empty for \(m=1\). Thus the potential increment over one occurrence of each required edge is exactly \(-(F_k-1)\).

In an arbitrary cyclic host, mark one occurrence of each edge in \(E\). There are \(N-|E|\) unmarked factor occurrences. The potential increments along *all* consecutive edges telescope to zero around the host. Every unmarked occurrence, legal or not, contributes at most \(1\). Therefore

\[
0\le -(F_k-1)+(N-|E|),\qquad N\ge F_{k+2}+F_k-1.
\]
The reasoning allows host factors containing `11`, so the bound applies without restrictions on the host.

**2. An Eulerian multiset giving equality.** For every legal binary middle word \(x\) of length \(k-2\) containing at least one `1`, add **one extra copy** of the legal edge `0x0`. Write \(D\) for this set of duplicated edges. Since there are \(F_k\) legal middle words, including the all-zero word,

\[
|D|=F_k-1.
\]
For any nonzero legal length-\(m\) vertex \(v\), its new extra outdegree is \(\mathbf1_{\{v\text{ begins with }0\}}\), and its new extra indegree is \(\mathbf1_{\{v\text{ ends with }0\}}\). They cancel the imbalance \(d_E^+(v)-d_E^-(v)\). At the all-zero vertex no extra copy is incident and the original indegree equals the original outdegree. Thus the directed multigraph with all edges \(E\), together with the extra copies \(D\), is balanced at every vertex.

The graph of required edges is strongly connected: from any legal vertex, append \(m\) zeros to reach \(0^m\); from \(0^m\), append the letters of any other legal vertex to reach it. Neither path creates `11`. Thus the augmented balanced graph has an Eulerian directed circuit. Reading successive final letters of its edge labels gives a binary cyclic word of length

\[
|E|+|D|=F_{k+2}+F_k-1
\]
whose cyclic length-\(k\) factors are precisely the required legal labels, counted with their multiplicities. In particular, the constructed cyclic host avoids `11`. The lower bound is met. Finally, the standard Fibonacci–Lucas identity \(F_{k+2}+F_k=L_{k+1}\) yields the stated form.

## Verification
The accompanying standalone `verify.py` requires only Python's standard library. For each \(2\le k\le12\), it constructs the stipulated multiset, verifies degree balance, produces an Eulerian circuit, enumerates every cyclic length-\(k\) factor of the resulting word, checks the potential identity on the target edges and its unit upper bound on *all* binary edges, and checks that the resulting length is \(F_{k+2}+F_k-1\). For \(2\le k\le5\), an independent exhaustive breadth-first search in the **full binary** de Bruijn graph, including `11`-containing factors, finds the same shortest possible cyclic host length. The search includes all possible cyclic walks because every feasible host contains the all-zero length-\(k\) factor, so it may be rooted at the all-zero vertex. Output ends in `VERIFICATION_OK`.

## Relationship to prior work
Yu Hin Au studied generalized de Bruijn words for primitive-word and power dictionaries, including lower bounds for covering power words. Those dictionaries are not the binary words avoiding `11`. Tan and Shallit studied representable factor sets and general shortest-witness bounds. Blanchet-Sadri and Lohr developed a min-cost flow reduction for finding shortest cyclic representations of given factor sets. This result uses that general covering-walk viewpoint but obtains a **closed Fibonacci–Lucas optimum for an infinite constrained-language family**, including a concrete sharp potential certificate and an explicit fixed-form set of repeated factors. The inspected published sources do not state this particular family formula or the unrestricted-host-to-restricted-host optimality conclusion. A general min-cost flow algorithm can calculate each individual instance but does not, by itself, evaluate this parameterized family symbolically. This is a literature-limited originality comparison, not a claim of global uniqueness.

## Limitations
The theorem concerns two symbols, the sole forbidden adjacent factor `11`, and cyclic rather than linear hosts. It does not count how many distinct optimal cyclic hosts exist, nor address other finite-type constraints. The exhaustive checks cover finite orders only and are supportive rather than the proof. Broader or unindexed prior literature may contain an equivalent Fibonacci–Lucas evaluation.

## References
- Yu Hin Au, *Generalized de Bruijn words for Primitive words and Powers*, arXiv:0904.3997 (first public 25 April 2009), https://arxiv.org/pdf/0904.3997 .
- Shuo Tan and Jeffrey Shallit, *Sets Represented as the Length-n Factors of a Word*, 2013 preprint, arXiv:1304.3666v1 (first public 12 April 2013), https://arxiv.org/pdf/1304.3666 .
- Francine Blanchet-Sadri and Andrew Lohr, *Computing Minimum Length Representations of Sets of Words of Uniform Length*, Theoretical Computer Science 596 (2015), 41–54, DOI:10.1016/j.tcs.2015.06.038; author-available manuscript https://www.researchgate.net/publication/281940256_Computing_Minimum_Length_Representations_of_Sets_of_Words_of_Uniform_Length .
