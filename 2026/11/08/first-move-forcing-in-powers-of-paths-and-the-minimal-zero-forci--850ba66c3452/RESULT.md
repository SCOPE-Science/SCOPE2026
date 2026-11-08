# First-move forcing in powers of paths and the minimal zero-forcing spectrum of path squares

## Finding

**Theorem.** For integers \(n\ge 2\) and \(1\le k<n\), give the power \(P_n^k\) vertex labels \(1,\ldots,n\) and adjacency when \(0<|i-j|\le k\). Under the *ordinary* zero-forcing color-change rule, an initial blue set \(S\) forces the entire graph if and only if either \(S\) is already the entire vertex set or some initially blue vertex has exactly one initially white neighbor. In particular, for each oriented edge \((v,w)\) set
\[
T(v,w)=\{v\}\cup(N(v)\setminus\{w\}).
\]
The inclusion-minimal zero-forcing sets are exactly the inclusion-minimal members of \(\{T(v,w):vw\in E(P_n^k)\}\). Every zero-forcing set contains at least one of these triggers. This gives at most \(2|E(P_n^k)|\) inclusion-minimal sets and a bounded-size local description for every power of a path.

For the square \(P_n^2\), \(n\ge3\), let \(M_n(z)\) count inclusion-minimal zero-forcing sets by their size. Then
\[
M_n(z)=\begin{cases}
3z^2,&n=3,\\
4z^2,&n=4,\\
4z^2+z^3,&n=5,\\
4z^2+2z^3,&n=6,7,\\
4z^2+2z^3+3(n-7)z^4,&n\ge8.
\end{cases}
\]
For \(n\ge8\) the labelled minimal sets have three possible sizes, exactly \(4\) of size two, exactly \(2\) of size three, and exactly \(3(n-7)\) of size four. There are \(3n-15\) in total, with maximum inclusion-minimal size \(4\). The previously known minimum zero-forcing size \(2\) is **not** asserted as new.

## Assumptions and scope

All graphs are finite and simple. An ordinary zero-forcing process colors a white neighbor \(w\) blue only when its blue neighbor \(v\) has precisely one white neighbor, namely \(w\). A forcing set is inclusion-minimal if none of its proper subsets forces all vertices. Initial legal moves are tested *before* any recoloring. Every index bound below is inclusive; an index interval with lower bound greater than upper bound contributes no sets.

## Proof

**1. Propagation from any first move.** Fix \(1\le k<n\). Suppose an initially legal force \(v\to w\) occurs. Immediately afterward all of \(N[v]\) is blue: every neighbor other than \(w\) was initially blue, and \(v\) itself was blue. Hence the entire interval
\[
[a,b]=[\max(1,v-k),\min(n,v+k)]
\]
is blue. If \(b<n\), necessarily \(b=v+k\). The blue vertex \(u=b-k+1\) has as its only neighbor outside \([a,b]\) the vertex \(b+1\): its leftmost possible neighbor is \(b-2k+1=v-k+1\ge a\), and its rightmost is \(b+1\). Thus \(u\) forces \(b+1\). Replacing \(b\) by \(b+1\) and iterating makes \([a,n]\) blue. If \(a>1\), necessarily \(a=v-k\). At the left end the blue vertex \(u=a+k-1\) has exactly one outside neighbor, namely \(a-1\): the remaining possible neighbors are contained in \([a,n]\), because every remaining neighbor of \(u\) lies between \(a\) and \(\min(n,a+2k-1)\), and this entire interval is blue after the preceding rightward propagation. Iterating leftward colors all of \([1,n]\). Preexisting additional blue vertices can only help, never invalidate this chosen force sequence (if the target was already recolored, omit that force). Therefore one legal initial move suffices.

Conversely, a proper blue set with no initially legal move cannot take any first step, hence is not forcing. A move \(v\to w\) is initially legal precisely when \(T(v,w)\subseteq S\) and \(w\notin S\). If \(S\) contains \(T(v,w)\) but also \(w\), then \(N[v]\) is already blue, and the interval-spreading argument above applies without a first step. Indeed, the same spread can begin from any entirely blue closed neighborhood. Consequently \(S\) forces if it contains a trigger; moreover the all-blue set contains a trigger since every vertex has a neighbor. For an inclusion-minimal forcing set, choosing a first move shows it equals a minimal trigger. Conversely, inclusion-minimal triggers force and are inclusion-minimal among all forcing sets. Every trigger has at least one vertex and there are at most twice as many oriented edges as edges.

**2. Complete minimal-trigger classification in the square.** Let \(k=2\). For \(n=3\), the square is \(K_3\), and its three minimal sets are the two-element subsets. For \(n\ge4\), the inclusion-minimal triggers of size two are exactly
\[
\{1,2\},\quad\{1,3\},\quad\{n-2,n\},\quad\{n-1,n\}.
\]
This follows by listing triggers centered at the two endpoints (each has exactly two neighbors); all other vertices have at least three neighbors and thus yield triggers of size at least three. These four pairs are distinct for \(n\ge4\).

For \(n\ge5\), triggers at vertices \(2\) and \(n-1\) have three vertices. After deleting those that contain one of the four minimal pairs, precisely
\[
\{2,3,4\},\qquad \{n-3,n-2,n-1\}
\]
remain. They coincide when \(n=5\) and are distinct for \(n\ge6\). All other three-element candidates are impossible because their center has at least four neighbors (with the only small boundary already handled). None of the displayed triples contains a minimal pair.

For \(n\ge6\), the only remaining candidates are four-element triggers whose centers have degree four, that is, centers \(v\in\{3,\ldots,n-2\}\). Their neighbor set is \(\{v-2,v-1,v+1,v+2\}\), so omitting one neighbor produces one of four patterns. Triggers containing a listed minimal pair or triple are redundant. The surviving patterns are **exactly** the following three pairwise disjoint labelled families:
\[
\begin{array}{ll}
\{j,j+1,j+2,j+3\},&3\le j\le n-5,\\
\{j,j+2,j+3,j+4\},&2\le j\le n-6,\\
\{j,j+1,j+2,j+4\},&3\le j\le n-5.
\end{array}
\]
To check exhaustion directly, for each center \(v\) omit respectively \(v-2,v-1,v+1,v+2\). The resulting relative patterns are \(\{v-1,v,v+1,v+2\}\), \(\{v-2,v,v+1,v+2\}\), \(\{v-2,v-1,v,v+2\}\), and \(\{v-2,v-1,v,v+1\}\). The first and last are consecutive four-sets; they survive precisely when their smallest label is at least \(3\) and greatest at most \(n-2\). The second survives precisely for \(4\le v\le n-4\); the third precisely for \(5\le v\le n-3\). These are the three ranges displayed. At each excluded boundary, one of the previously displayed pair or triple triggers lies inside the four-set. No retained four-set contains a smaller trigger, and distinct families have different internal gap patterns. Thus all retained candidates are minimal, and there are no further ones.

Each of the three four-set families has \(\max(n-7,0)\) members. Together with four distinct pairs and one or two triples, this proves the polynomial with all small-order cases included. The known equality \(Z(P_n^2)=2\) is consistent with, but much weaker than, this complete labelled enumeration. \(\square\)

## Verification

The standalone `verify_pathpower.py` builds each power-of-path adjacency matrix from distances between labels and independently runs the ordinary iterative color-change rule. Across \(55\) pairs of parameters with \(1\le k\le5\) and \(k+1\le n\le14\), it tests \(163716\) starting masks against the first-move theorem. For squares \(3\le n\le18\) it tests \(524280\) starting masks, independently generates all ordered-edge triggers, computes their inclusion-minimal antichain, and checks every coefficient of the claimed polynomial. Output from actual execution:

```
VERIFY_OK first_move_cases=55 first_move_subsets=163716 square_orders=3..18 square_full_subsets=524280 square_minimal_sets=288 exact_polynomial=PASS all_minimal_triggers=PASS standard_zero_forcing=PASS
```

The unrestricted proof is mathematical; exhaustive tests over finitely many orders do not establish the theorem for all orders.

## Relationship to prior work

Nazari and Karimi Radpoor (2012), Theorem 3.5, already give \(Z(P_n^k)=k\) and an endpoint construction. This settles the scalar minimum but does not enumerate every inclusion-minimal starting set or characterize all forcing configurations. Brimkov and Carlson (first posted 2022-04-04) study inclusion-minimal zero-forcing sets, upper zero forcing number, and polynomial versus exponential counts, but their primary full-text analysis does not give either stated path-power theorem or this exact path-square polynomial. Boyer et al. (2018) derive zero-forcing polynomials for several graph families, including ordinary paths; their families do not include the nontrivial powers of paths. A later paper of Johnson, Vick, Flórez, and Narayan on *failed skew zero forcing* of path powers concerns a different rule in which uncolored vertices may force and does not supply an ordinary minimal-set spectrum. Its full open-access primary PDF, including the path-power section and closing open problems, was inspected; it develops failed *skew* zero-forcing numbers, not ordinary minimal-set cardinality distributions.

## Limitations

The complete closed cardinality polynomial is proved only for squares \(P_n^2\), not for every larger power. For general powers, the theorem supplies an exact finite trigger characterization of all configurations, but not a simplified generating polynomial. The result is reviewed on correctness, coverage, and mathematical value by a single non-independent review; no independent mathematical audit or new-publication priority claim is made. Possible unindexed equivalent classifications remain a limitation.

## References

1. B. Brimkov and J. Carlson, *Minimal Zero Forcing Sets*, arXiv:2204.01810 (initial public preprint 2022-04-04), https://arxiv.org/abs/2204.01810.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910, https://arxiv.org/abs/1801.08910.
3. A. M. Nazari and M. Karimi Radpoor, *Minimum Rank of Graphs Powers Family*, Open Journal of Discrete Mathematics (2012), DOI:10.4236/ojdm.2012.22012, especially Theorem 3.5.
4. A. Johnson, A. Vick, R. Flórez, and D. A. Narayan, *Failed Skew Zero Forcing Numbers of Path Powers and Circulant Graphs*, 2025, DOI:10.3390/appliedmath5020032 (rule differs from ordinary zero forcing).
