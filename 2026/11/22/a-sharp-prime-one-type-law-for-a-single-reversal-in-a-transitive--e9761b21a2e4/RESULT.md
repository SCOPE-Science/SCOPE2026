# A sharp prime-one-type law for a single reversal in a transitive tournament

## Finding
Let \(n\ge4\), label the parameter vertices \(0,1,\ldots,n-1\), initially orient every edge \(i\to j\) for \(i<j\), and reverse exactly the arc \(p\to q\), where \(0\le p<q<n\). Write \(A_{n;p,q}\) for this tournament. In the countable homogeneous random tournament, name the vertices of \(A_{n;p,q}\) individually. A nonalgebraic singleton type is called *prime* when the tournament induced by the named parameters and a realization of the type has no nontrivial module (homogeneous set).

The number \(N(n;p,q)\) of prime singleton types is exactly
\[
N(n;p,q)=\begin{cases}
1& q=p+1,\quad n\text{ even},\\
0& q=p+1,\quad n\text{ odd},\\
6& q-p=2,\\
6& (p,q)=(0,n-1),\\
8& 3\le q-p\le n-2.
\end{cases}
\]
The cases are disjoint for \(n\ge4\). Thus the total number of prime types summed over all possible choices of the one reversed arc is
\[
\sum_{0\le p<q<n}N(n;p,q)=4n^2-14n+10+(n-1)\mathbf1_{2\mid n}.
\]
For \(n\ge5\), the largest count attainable by one reversal is the constant eight. In contrast the original transitive base has just one prime singleton type for even \(n\), and none for odd \(n\).

## Assumptions and scope
A tournament is a finite complete irreflexive orientation. A *module* is a set \(S\) of vertices such that each vertex outside \(S\) either dominates every vertex in \(S\) or loses to every vertex in \(S\). The empty set, all vertices and singletons are trivial; *prime* means no other modules. There is no quotient by the automorphisms of the named base: all old vertices remain individually named. The countable homogeneous random tournament is the Fraïssé limit of all finite tournaments, so every vector of orientations from a new point to the \(n\) named points is realized and gives a distinct complete nonalgebraic singleton type. The assertion is a uniform statement for all integers \(n\ge4\), all permitted \(p,q\), and all binary new-point orientations.

Put \(b_i=1\) if \(i\to x\), and \(b_i=0\) if \(x\to i\), for the added vertex \(x\). In particular there are \(2^n\) singleton types before imposing primality.

## Proof
**1. Adjacent reversal.** When \(q=p+1\), reversing the arc simply exchanges the two adjacent points of the transitive order. In that resulting total order, each consecutive pair of old vertices is a module. To destroy every such pair, the \(b\)-word must alternate. The first old vertex dominates all other old vertices; if its bit were one, the remaining old vertices together with \(x\) would form a module. Hence its bit is zero. Likewise the final old vertex has bit one, or its complement with \(x\) would be a module. Exactly one alternating word meets both boundary conditions when \(n\) is even, and none when \(n\) is odd. The one word is prime: any module missing \(x\) contradicts alternation on an old consecutive pair, and a module containing \(x\) and a nonempty proper old interval would need to omit either the first old source or last old sink, contradicting its prescribed boundary bit.

**2. Decomposition after a nonadjacent reversal.** Assume \(q\ge p+2\). Put \(L=\{0,\dots,p-1\}\), \(M=\{p+1,\dots,q-1\}\), \(R=\{q+1,\dots,n-1\}\), and \(B=\{p\}\cup M\cup\{q\}\). Each of \(L,M,R\) is transitive. The middle block is the cyclic three-vertex tournament with the transitive middle class inflated: \(p\to M\to q\to p\), and the outer tournament is the ordinal sum \(L\to B\to R\). A direct module analysis (or the elementary modular-substitution rule) shows that every nonempty module of the old tournament is of one of these forms: a consecutive interval wholly inside one of \(L,M,R\); one of the singletons \(\{p\},\{q\}\); or a consecutive interval in the quotient order \(0,\ldots,p-1,B,q+1,\ldots,n-1\) that includes the *whole* block \(B\). To see this directly, a module meeting two cyclic classes of \(B\) must meet all three (the omitted class distinguishes them); when it includes all three, it includes every vertex of the inflated class \(M\). The transitive outside quotient then forces consecutive blocks. Inside a transitive class, modules are exactly consecutive intervals.

**3. Necessary and sufficient bit conditions.** The extended tournament is prime precisely when:

* On each nonempty outer run \(L,R\), the bits alternate. If \(L\ne\varnothing\), its first bit is \(b_0=0\). If \(R\ne\varnothing\), its last bit is \(b_{n-1}=1\).
* On \(M\), the bits alternate.
* If \(|M|=1\), the three bits \(b_p,b_{p+1},b_q\) are not all equal.
* If \(L=R=\varnothing\), the combination \(b_p=1,b_q=0\) is forbidden.

Necessity: every consecutive pair in a transitive run is an old module, so its bits must differ. If \(L\) is nonempty, vertex \(0\) dominates the old tournament. Taking \(b_0=1\) would make all vertices except \(0\) a module; the dual argument gives \(b_{n-1}=1\) when \(R\) is nonempty. When \(|M|=1\), \(B\) is a module of the old tournament and is proper because \(n\ge4\), so the new point must split it. Finally if \(L=R=\varnothing\), the set \(M\cup\{x\}\) is a module when \(b_p=1,b_q=0\).

Sufficiency: A proposed nontrivial module not containing \(x\) is an old module. Any run interval with at least two elements is split by alternation; any larger module containing \(B\) is split on \(B\) (alternation in \(M\), or the explicit three-bit condition when \(|M|=1\)). The entire old base is similarly split. Now suppose a proper module contains \(x\), and let \(K\) be its nonempty set of old vertices. Necessarily \(K\) is an old module. If \(K\subseteq L\), then every point of \(B\) must receive bit zero, contrary to the nonconstant bit pattern on \(B\); if \(K\subseteq R\), the corresponding bits must all be one, also impossible. If \(K=\{p\}\) or \(K=\{q\}\), the required constant bits on \(M\) are impossible when \(|M|\ge2\); when \(|M|=1\), the required outer orientations contradict \(b_0=0\) or \(b_{n-1}=1\), at least one of which applies since \(n\ge4\). If \(K\subseteq M\), vertices \(p,q\) force \(b_p=1,b_q=0\); then a nonempty \(L\) or \(R\) violates the relevant outer boundary bit, while if both are empty the final condition forbids the combination. Finally if \(K\) contains all of \(B\) and extends along consecutive outer quotient blocks, any omitted initial source from \(L\) would require \(b_0=1\), and any omitted final sink from \(R\) would require \(b_{n-1}=0\). Since neither is possible, \(K\) must be the entire old base, making the proposed module the entire extension. This completes the equivalence.

**4. Count.** Each nonempty outer run has its phase fixed by its boundary bit, so contributes one choice. The nonempty middle run \(M\) contributes exactly two alternating phases. The bits at \(p\) and \(q\) are initially independent, giving \(2\cdot2\cdot2=8\) assignments. If \(|M|=1\), exclude the two assignments constant on \(B\), leaving six. If \(L=R=\varnothing\) (equivalently \(p=0,q=n-1\)), exclude the two assignments with \(b_p=1,b_q=0\), also leaving six. For \(n\ge4\) these exceptional regimes do not overlap. Otherwise all eight remain. Summing by span \(q-p\) gives the displayed quadratic total: \(n-1\) adjacent pairs, \(n-2\) span-two pairs, one spanning pair, and \(((n-3)(n-2)/2-1)\) remaining pairs.

## Verification
Two self-contained implementations are supplied: `verify.cpp` enumerates every orientation vector and **every** potential proper module for all \(4\le n\le12\), comparing it against the four necessary-and-sufficient bit conditions (458720 parameter/vector cases). `verify.py` independently implements module testing using explicit vertex sets and counts each reversed-arc case for \(4\le n\le8\) (80 parameter pairs). Run `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify` and `python3 verify.py`. The included `CHECKS.txt` records the observed successful outputs. These finite checks support, but do not replace, the all-size module argument above.

## Relationship to prior work
The classical one-point simple-extension theorem of Erdős, Hajnal and Milner (1972), independently approached by Moon, decides *existence* of prime one-point extensions for general finite tournaments. Brignall, Ruškuc and Vatter (arXiv:0911.4378, especially Section 2) give a complete modular-decomposition proof of the existence criterion. Their inspected argument does not derive the labelled prime-type cardinalities for each single reversed arc, nor the bounded \(1,6,8\) law. The 1972 paper *Some remarks on simple tournaments* proves two-point existence and results about modules and is not a counting classification for the stated near-transitive bases. Some historically relevant original full texts were not completely accessible; a publication-priority gap remains.

## Limitations
Only the exact family with one reversed arc of a transitive tournament is classified, not arbitrary near-transitive perturbations or all finite tournament bases. The count is for individually named old vertices (not unlabelled extensions), and includes all possible new vertex orientations. Independent external mathematical validation and complete historical-priority certification have not been performed.

## References
1. R. Brignall, N. Ruškuc and V. Vatter, *Simple extensions of combinatorial structures*, arXiv:0911.4378 (first posted 2009-11-23), Section 2, https://arxiv.org/abs/0911.4378.
2. P. Erdős, A. Hajnal and E. C. Milner, *Simple one-point extensions of tournaments*, Mathematika 19 (1972), 57–62, https://doi.org/10.1112/S0025579300004939.
3. P. Erdős, E. Fried, A. Hajnal and E. C. Milner, *Some remarks on simple tournaments*, Algebra Universalis 2 (1972), 238–245, https://combinatorica.hu/~p_erdos/1972-24.pdf.
4. J. W. Moon, *Embedding tournaments in simple tournaments*, Discrete Mathematics 2 (1972), 389–395, https://doi.org/10.1016/0012-365X(72)90016-7.
