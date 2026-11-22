# Sharp diameter and Möbius-strip metric for optimal domination slides on cycles

## Finding
Let \(m\ge2\) and \(n=3m-2\). Let \(\mathcal D_n\) be the graph whose vertices are minimum-cardinality ordinary dominating sets of the labelled cycle \(C_n\), and whose edges are moves of one selected vertex to an unselected adjacent vertex while maintaining minimum-cardinality domination. For \(D\in V(\mathcal D_n)\), write
\[
E(D)=\bigl\{v\in\mathbb Z_n:\bigl|D\cap\{v-1,v,v+1\}\bigr|=2\bigr\}.
\]
Then \(E(D)\) is always a two-element set. Multiplication of its elements by the inverse of \(3\) modulo \(n\) is an isomorphism from \(\mathcal D_n\) to the two-token sliding graph on \(C_n\) restricted to pairs with both cyclic gaps at least \(m-1\).

Every vertex of \(\mathcal D_n\) has the same eccentricity:
\[
\boxed{\operatorname{rad}(\mathcal D_n)=\operatorname{diam}(\mathcal D_n)=\left\lfloor\frac n2\right\rfloor.}
\]
The graph is connected, has exactly \(n(m+1)/2\) vertices and \(nm\) edges, with exactly \(n\) degree-two vertices and \(n(m-1)/2\) degree-four vertices. All pairwise distances admit the explicit two-coordinate formula below, yielding linear-time distance computation from the input dominating sets and constructive optimal slides.

## Assumptions and scope
All graphs are finite, simple, and unweighted. The cycle has vertices \(\mathbb Z_n\) and edges joining consecutive residues. Domination uses *closed* neighborhoods. A minimum dominating set has \(m=\lceil n/3\rceil\) selected vertices. A legal slide replaces one vertex of the set by its neighbor on the original cycle; nonlocal replacement is not permitted. The theorem is for \(n=3m-2\ge4\), not for all cycle lengths.

For a pair \(P\subset\mathbb Z_n\) of distinct vertices, let its *standard lift* be the unique integers \(0\le a<b<n\) representing its elements. Put \(d=m-1\). The pair is admissible if \(d\le b-a\le n-d\). For admissible \(P,Q\) with standard lifts \((a,b)\) and \((c,e)\), respectively, define the lift operation \(T(u,v)=(v,u+n)\). Then the exact distance is
\[
\boxed{\operatorname{dist}_{\mathcal D_n}(D,D')=\min_{q\in\mathbb Z}\left(|a-u_q|+|b-v_q|\right),\quad (u_q,v_q)=T^q(c,e),}
\]
where \((a,b)\) and \((c,e)\) represent the transformed excess pairs. It suffices to test \(q\in\{-2,-1,0,1,2\}\). In alternative sum-and-gap coordinates \(s=a+b\), \(t=b-a\), the objective is
\[
\min_{q\in\mathbb Z}\max\bigl\{|s-s'-qn|,\ |t-\theta_q(t')|\bigr\},\qquad
\theta_q(t')=\begin{cases}t'&q\text{ even},\\ n-t'&q\text{ odd}.\end{cases}
\]
All minima are integers; either expression is evaluated with constant-many two-coordinate comparisons after one input scan.

## Proof
**1. Minimum configurations and the coverage-excess pair.** A selected vertex can dominate at most three cycle vertices, so any dominating set has at least \(m\) elements. This bound is attained by cyclic patterns with \(m\) positive clockwise gaps at most three summing to \(n\). Conversely, domination of the whole cycle is exactly the condition that all such gaps belong to \(\{1,2,3\}\). Since their total deficit from \(m\) threes is \(3m-n=2\), the gaps have either exactly one entry equal to one and all other entries three, or exactly two entries equal to two and all other entries three.

For \(D\) of size \(m\), define the coverage number \(c_D(v)=|D\cap\{v-1,v,v+1\}|\). Every \(c_D(v)\ge1\), and \(\sum_v(c_D(v)-1)=3m-n=2\). The gap classification shows that no vertex has coverage three: three selected sites in a length-three closed neighborhood would produce two adjacent unit gaps and a total gap deficit of at least four. Hence exactly two vertices have coverage two, and all others coverage one. These two vertices constitute \(E(D)\).

There are \(n\) configurations of the one-unit-gap type: the location of its unique adjacent selected pair fixes every other gap. The two-length-two-gap configurations number \(n(m-1)/2\): specify a starting selected vertex and an ordered pair of positions for the two exceptional gaps, then divide by the \(m\) choices of starting selected vertex and the two orderings of the two identical exceptional gaps. Equivalently, there are \(n\binom m2/m=n(m-1)/2\). Therefore there are \(n(m+1)/2\) minimum dominating sets.

**2. A bijective two-particle code.** Let \(A\) be the cyclic closed-neighborhood incidence operator, \((Af)(v)=f(v-1)+f(v)+f(v+1)\). The map \(A\) is injective over real vectors whenever \(3\nmid n\): if \(Af=0\), subtracting successive equations gives \(f(v+3)=f(v)\); because \(\gcd(3,n)=1\), \(f\) is constant, and hence zero. Thus \(E(D)\), which determines the complete vector \(c_D=\boldsymbol 1+\boldsymbol 1_{E(D)}\), determines \(D\) uniquely.

Since \(n=3m-2\), \(3\) has a multiplicative inverse modulo \(n\), namely \(2m-1\). Define \(\phi(D)=(2m-1)E(D)\subset\mathbb Z_n\). A single unit gap produces two neighboring covered-twice sites, whose transformed cyclic separation is \(m-1\) (equivalently \(2m-1\)). When the two exceptional gaps have length two, their intermediate covered-twice sites have a clockwise separation \(3j-1\) for some \(1\le j\le m-1\), and multiplication by the inverse of three gives separation \(j+m-1\), lying in \([m,2m-2]\). Hence every transformed pair has both cyclic gaps at least \(m-1\). The number of such unordered pairs is \(n(n-2(m-1)+1)/2=n(m+1)/2\), the number already counted for minimum dominating sets. Injectivity therefore proves surjectivity and bijectivity.

**3. Exact move correspondence.** Sliding a selected vertex from \(i\) to \(i+1\) changes its closed-neighborhood coverage vector by
\[
A(\boldsymbol 1_{i+1}-\boldsymbol 1_i)=\boldsymbol 1_{i+2}-\boldsymbol 1_{i-1}.
\]
Whenever both endpoint sets are minimum dominating, this exchanges one covered-twice site \(i-1\) for \(i+2\) (or its reverse), while retaining the other. Their images under multiplication by the inverse of three differ by one step on the transformed cycle. Conversely, if two admissible transformed pairs differ by a one-step token slide, their coverage-excess vectors differ by \(\boldsymbol 1_{i+2}-\boldsymbol 1_{i-1}\) for a unique residue \(i\). Injectivity of \(A\) implies that the corresponding dominating-set indicator vectors differ by exactly \(\boldsymbol 1_{i+1}-\boldsymbol 1_i\). Therefore the pair graph and the domination-slide graph have exactly the same edges under \(\phi\).

**4. Geodesics in the lifted strip.** Represent a particle pair by an integer lift \((a,b)\) obeying \(d\le b-a\le n-d\). The cyclic identification is precisely \((a,b)\sim T(a,b)=(b,a+n)\), where \(T^2(a,b)=(a+n,b+n)\). A legal single-site slide changes one integer coordinate by one and preserves the strip inequalities. The strip is geodesically convex in the integer \(\ell_1\) grid: the coordinatewise minimum of two feasible points is feasible, and any two coordinatewise comparable points have a monotone path of length equal to the sum of their coordinate differences. For the latter assertion, increasing either coordinate is allowed unless it would violate a boundary. If both needed increases were blocked simultaneously, the existing gap would equal both \(d\) and \(n-d\), impossible because \(d<n-d\); if only one coordinate needs increasing and its move is blocked, feasibility of the target forces the other coordinate to need increasing as well. Induction supplies the path. Joining two arbitrary points through their coordinatewise minimum gives their exact \(\ell_1\) distance.

Every cyclic particle-slide path lifts to a path in this strip, and its terminal lift is one of \(T^q(c,e)\). Hence its length is at least the displayed minimum \(\ell_1\) displacement. The strip-geodesic argument attains that minimum with valid cyclic configurations at every step. The five stated lifts suffice since for the chosen standard representatives any translation by more than two circumferences is strictly more expensive than one of the five nearest lifts. Expressing \(\ell_1\) of two coordinates as the maximum of the absolute differences of their sums and differences yields the alternative formula.

**5. Sharp eccentricities.** Put \(L=\lfloor n/2\rfloor\), and use coordinates \(s=a+b\), \(t=b-a\) with \(t\in[d,n-d]\) and \(s\equiv t\pmod2\). Under \(T^q\), the sum coordinate increases by \(qn\); the gap coordinate is \(t\) for even \(q\) and \(n-t\) for odd \(q\). Given any two states, choose an integer \(q\) making their sum-coordinate difference at most \(L\). The gap difference is at most \(n-2d=m\), which is at most \(L\) for every \(m\ge2\). The metric formula consequently bounds every distance by \(L\).

For the reverse bound from **every** state \((s,t)\), select a feasible target lift whose sum coordinate is \(s+L\); keep the gap coordinate equal to \(t\) if \(L\) is even, and otherwise change it by one in a direction staying within \([d,n-d]\). Such a choice always exists because that interval has at least two integer points. The parity of the new sum and gap agrees, so both target particle coordinates are integers. Their separation is feasible. For every integer \(q\), the absolute sum-coordinate difference between the source and any representative of that target is \(|L+qn|\ge L\). The distance formula gives a lower bound \(L\), achieved by the upper bound. Thus every eccentricity equals \(L\), proving the sharp radius and diameter.

**6. Degrees and edges.** In the transformed two-particle graph, a pair at one of the two boundary gaps has exactly two legal slides; all interior pairs have four. There are \(n\) boundary-gap pairs and \(n(m-1)/2\) interior pairs. Summing degrees gives \(2n+4n(m-1)/2=2nm\), and hence \(nm\) edges. This completes the claims.

## Verification
The accompanying `verify.py` uses only Python 3's standard library. It enumerates every size-\(m\) subset directly for \(n\in\{4,7,10,13,16,19\}\), tests domination from closed neighborhoods, builds the legal slide graph independently from the two-particle graph, checks bijectivity and exact edge correspondence, and compares every graph shortest path against the Möbius formula. It checks all eccentricities, degree distributions, and edge counts: 11,290 ordered pairs in total. Execute `python3 verify.py` from the directory containing this file and the script; the expected final line begins `ALL_VERIFY_OK`. Finite enumeration corroborates but does not replace the preceding infinite-family proof.

## Relationship to prior work
Fricke et al., *γ-Graphs of Graphs* (2011), prove connectedness of the minimum-domination slide graph of cycles of length congruent to one modulo three; that connectivity is not claimed as new. Hernández-Gómez et al. (2020) classify minimum dominating sets of paths and cycles and describe their excess-overlap positions and dihedral orbits. Rakhimol and Bhatt (2023) give the same minimum-set cardinality count and study a graph defined with different nonlocal replacement moves. Křišťan and Svoboda (arXiv:2307.10847v1, first public 2023-07-20) establish shortest dominating-set token-slide algorithms on trees and interval graphs, not this cycle-family metric or the exact all-state eccentricities.

Previously published circular bounded-gap token-sliding results already imply optimal transport **distances** for the larger general constrained-token family; that implication is explicitly acknowledged, and generic geodesic optimality is not claimed as independently new. A published self-centeredness theorem for minimum maximal matchings of cycles also gives the same numeric diameter on a **different** constrained state graph, with a stricter two-particle separation bound. Neither result identifies the overcoverage-based two-particle graph of *ordinary minimum dominating sets* or determines all eccentricities for its wider separation interval. The proposed contribution is the sharp uniform eccentricity theorem for the present reconfiguration graph, together with its explicit derived model and complete degree census.

## Limitations
Only minimum-cardinality ordinary domination on cycles with \(n\equiv1\pmod3\) is covered. The theorem is not a general complexity classification for arbitrary graphs, and the known minimum-set counts and generic optimal-transport principle are not priority claims here. The computational check is exhaustive only within the stated finite range. A mathematically equivalent theorem under different cyclic-particle terminology might exist outside the inspected sources. Independent scholarly audit has not been performed.

## References
1. G. H. Fricke et al., *γ-Graphs of Graphs*, Discussiones Mathematicae Graph Theory 31 (2011), DOI: 10.7151/dmgt.1562, https://bibliotekanauki.pl/articles/743973.pdf.
2. J. C. Hernández-Gómez et al., *Transitivity on Minimum Dominating Sets of Paths and Cycles*, Symmetry 12 (2020), 2053, https://doi.org/10.3390/sym12122053.
3. Rakhimol and K. Bhatt, *A Study on The Gamma Graph of Cycle C3K+1*, Journal of Computational Mathematica 7 (2023), https://doi.org/10.26524/cm178.
4. J. M. Křišťan and J. Svoboda, *Shortest Dominating Set Reconfiguration under Token Sliding*, arXiv:2307.10847v1, first public 2023-07-20, https://arxiv.org/abs/2307.10847.
5. *Circular bounded-gap token systems have transport-optimal sliding paths*, publicly available technical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-circular-bounded-gap-token-systems-have-transport-optimal-slidin--edbf2b8cafb9.
6. *Every minimum maximal matching of a cycle of order congruent to one modulo three has sharp eccentricity*, publicly available technical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-every-minimum-maximal-matching-of-a-cycle-of-order-3k-1-has-ecce--9e512596be10.
7. *Gap-slack isometry and exact token-sliding distances for mutually visible triples on cycles*, publicly available technical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-gap-slack-isometry-and-exact-token-sliding-distances-for-mutuall--f7b2fcae2dd0.
