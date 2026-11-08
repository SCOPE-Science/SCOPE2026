# Exact shattering polynomial for convex equivalence relations on a finite chain

## Finding

Let \(\mathcal E_n\) denote the family of all convex equivalence relations on the finite order \([n]=\{1,\dots,n\}\), where convex means each equivalence class is a nonempty interval. Use pair-equality queries: \(q_{ij}\) asks whether \(i\sim j\), for \(1\le i<j\le n\). For \(N=n-1\), let \(s_k(N)\) be the number of shattered supports comprising exactly \(k\) distinct pair queries, and put \(\Phi_N(z)=\sum_{k\ge0}s_k(N)z^k\).

**Exact support criterion.** Associate \(q_{ij}\) with the interval \(I_{ij}=\{i,i+1,\ldots,j-1\}\) of potential cut sites in \([N]\). A set \(S\) of queries is shattered if and only if every interval in \(\{I_q:q\in S\}\) contains a *private site*, a member not belonging to any other interval in that family.

**Complete polynomial.** For formal variables \(t,z\),
\[
\sum_{N\ge0}\Phi_N(z)t^N=\frac{1-2t+(1-z)t^2}{(1-t)(1-(2+z)t+(1-z)t^2)}.
\]
Equivalently, \(s_0(N)=1\), and when \(1\le k\le N\),
\[
s_k(N)=\sum_{j=0}^{\min(k-1,N-k)}\binom{k-1}{j}\binom{N+k-j}{2k};\quad s_k(N)=0\text{ for }k>N.
\]
For \(n\ge2\), \(\operatorname{VCdim}(\mathcal E_n)=n-1\), and the only maximum support is all \(n-1\) adjacent-pair queries. The total number of shattered supports, including the empty one, is
\[
\Phi_{n-1}(1)=\frac{3^{n-1}+1}{2}.
\]
For every \(n\ge3\), the shattering complex has inclusion-maximal faces of cardinalities one and \(n-1\), a nonpurity gap of \(n-2\).

## Assumptions and scope

The ground set is a *fixed, labeled, linearly ordered* \([n]\). Equivalence classes must be consecutive blocks, but the number and sizes of blocks are unrestricted. The universe of binary questions consists of unordered distinct-element pairs, with each pair used at most once in a support. The labels are Boolean **same block**, rather than a membership or a named-block label. Empty query supports are allowed; \(n=1\) has the single empty support and dimension zero. No claim is made about cyclic orders, arbitrary partitions, or bounded numbers of classes.

## Proof

**1. Cut representation and shattering.** Choose a cut set \(C\subseteq[N]\). It defines an equivalence relation by declaring two elements to be equivalent exactly when there is no cut between them. Thus \(q_{ij}\) returns one if and only if \(C\cap I_{ij}=\varnothing\). This is a bijection between all \(2^N\) cut sets and all convex equivalence relations. Suppose \(S\) is shattered. For each interval \(I\in S\), apply the labeling which requires the query associated with \(I\) to return zero and *all other* queries of \(S\) to return one. The witnessing cut set has a site in \(I\) and no site in any other support interval, yielding a private site. Conversely, if each \(I\) has a private site \(p_I\), then to realize any labeling take as cuts exactly \(\{p_I:I\text{ is prescribed zero}\}\). This intersects precisely the intervals prescribed zero and avoids every interval prescribed one. Hence the criterion is necessary and sufficient, including the empty family.

**2. Structure of private-site families.** A family of distinct intervals with private sites contains no nested pair: an interval contained in another could not possess a private site. The left endpoints and right endpoints therefore occur in the same strict increasing order when the intervals are listed by left endpoint. No three intervals can have a common site: if three did, the middle interval in this endpoint ordering would lie inside the union of the outer two and have no private site. Moreover, a younger interval cannot lose its overlap with its predecessor and start overlapping its successor before obtaining a site on which it is the unique active interval; otherwise its entire span would be covered by those two neighbors. The resulting scan across sites has exactly three possible states after each site: \(A\), no interval currently active; \(B\), one active interval that already has a private site; and \(D\), two active intervals where the older has acquired a private site and the younger has not. A family is valid precisely when its scan follows the transitions below and finishes in \(A\) or \(B\); these states and endpoint changes determine the interval family uniquely.

**3. Transfer enumeration.** Scan each of the \(N\) sites, weighting the start of each interval by \(z\). The allowed transitions are \(A\to A\) (nothing), \(A\to B\) (start, weight \(z\)); \(B\to A\) (old closes), \(B\to B\) (old continues, weight one; or old closes and new starts, weight \(z\)), \(B\to D\) (old continues and new starts, weight \(z\)); \(D\to B\) (older closes, younger receives its first private site), and \(D\to D\) (both continue). These are all the possibilities; no state permits three simultaneous intervals or closure of an interval lacking a private site. With rows and columns ordered \(A,B,D\), the transfer matrix is
\[
T(z)=\begin{pmatrix}1&z&0\\1&1+z&z\\0&1&1\end{pmatrix},\qquad
\Phi_N(z)=(1,0,0)T(z)^N\begin{pmatrix}1\\1\\0\end{pmatrix}.
\]
Taking the formal resolvent gives
\[
\sum_{N\ge0}\Phi_N(z)t^N=(1,0,0)(I-tT(z))^{-1}\begin{pmatrix}1\\1\\0\end{pmatrix}
=\frac{1-2t+(1-z)t^2}{(1-t)(1-(2+z)t+(1-z)t^2)}.
\]
The intermediate states do not identify interval names; names are unnecessary because each interval is uniquely specified by the site where it opens and closes. In particular, the two \(B\to B\) alternatives yield distinct families and their weights sum to \(1+z\).

**4. Coefficients and extremal faces.** Rewrite the generating function as
\[
\frac1{1-t}+\sum_{k\ge1}\frac{z^k t^k(1+t)^{k-1}}{(1-t)^{2k+1}}.
\]
Coefficient extraction yields the displayed formula for \(s_k(N)\). Every shattered \(k\)-support has \(k\) disjointly assigned private sites, so \(k\le N\). The \(N\) singleton site intervals (corresponding to adjacent-pair queries) are shattered. If \(k=N\), all sites are private to distinct intervals, forcing each interval to be a singleton; therefore the maximum support is unique. Substituting \(z=1\) gives
\[
\sum_{N\ge0}\Phi_N(1)t^N=\frac{1-2t}{(1-t)(1-3t)},
\]
whose coefficients are \((3^N+1)/2\). Finally, for \(N\ge2\) the singleton family \(\{[1,N]\}\) is inclusion-maximal: adjoining any distinct nonempty interval \(J\subseteq[1,N]\) leaves \(J\) with no private site. The family of all \(N\) singleton intervals is also inclusion-maximal, since it is already of maximum size. Their sizes differ by \(N-1=n-2\), proving nonpurity and its unbounded gap.

## Verification

The standalone `checker.py` enumerates every cut set and every subset of potential pair queries for \(N=0,1,2,3,4,5\). It compares direct realization of all binary labelings against the private-site criterion, then checks all coefficients independently using the displayed binomial formula. It also checks the polynomial transfer and coefficient formula for \(N\le30\), and the total count and top coefficient. Invoke `python checker.py` in the directory containing this document and the checker; its success marker is `CONVEX_EQUIVALENCE_INTERVAL_SHATTERING_PASS`. The all-length theorem follows from the proof, not from the finite checks.

Some initial polynomials are \(\Phi_0(z)=1\), \(\Phi_1(z)=1+z\), \(\Phi_2(z)=1+3z+z^2\), \(\Phi_3(z)=1+6z+6z^2+z^3\), and \(\Phi_4(z)=1+10z+20z^2+9z^3+z^4\).

## Relationship to prior work

Chase and Freitag's 2018 analysis supplies the learning-theoretic/model-theoretic motivation for studying VC dimension of definable concept families, but does not state a count of shattered pair-equality supports of convex finite equivalence relations [1]. Goldberg and Marmolejo-Cossío analyze query learning of convex partitions of simplices, but their point-label queries, approximations, and domains differ from the present finite pair-equivalence queries [2]. OEIS A007051 already records the *numerical sequence* \((3^N+1)/2\); no novelty is claimed for that sequence by itself [3]. OEIS A119258 has the same row sums but a distinct row-by-cardinality refinement: e.g. at \(N=3\), its row is \((1,5,7,1)\), whereas the present shattered-support coefficients are \((1,6,6,1)\) [4]. The potential contribution is the exact pair-query shattering characterization, full coefficient polynomial, and nonpure-face phenomenon for this particular concept class, not the underlying interval or integer-sequence folklore.

## Limitations

This result does not compute online/Littlestone dimension, unlabeled orbit counts, or concept classes whose equivalence blocks need not be intervals. The sequence of total face counts is pre-existing. A search for statements under interval-hypergraph irredundance and private-witness terminology found no verified theorem that implies the complete polynomial, but priority under such terminology is an unresolved literature risk. Prior results about maximum irredundant interval families may not be exhaustive enumerations; inaccessible full text cannot be declared noncovering merely from abstracts. The finite checker covers only the stated bounded cases, and external mathematical audit has not been performed.

## References

[1] H. Chase and J. Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566v1, submitted 2018-01-19, https://arxiv.org/abs/1801.06566.

[2] P. W. Goldberg and F. J. Marmolejo-Cossío, *Learning Convex Partitions and Computing Game-theoretic Equilibria from Best Response Queries*, arXiv:1807.06170v1, submitted 2018-07-17, https://arxiv.org/abs/1807.06170.

[3] OEIS A007051, https://oeis.org/A007051 (known numerical totals).

[4] OEIS A119258, https://oeis.org/A119258 (different coefficient triangle with the same total sequence).
