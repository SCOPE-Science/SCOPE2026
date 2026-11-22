# Independent secure domination on cycles: a complete two-and-seven tiling census

## Finding

For each labelled simple cycle \(C_n\), \(n\ge4\), let \(P_n(z)=\sum_S z^{|S|}\), where the sum ranges over **independent secure dominating sets** \(S\). Here "independent" applies to the initial set; a defending swap is required to preserve domination but is **not** required to preserve independence.

The complete cardinality polynomial is

\[
\boxed{P_n(z)=n[x^n]\log\!\left(\frac{1}{1-zx^2-z^3x^7}\right)}\qquad(n\ge4).
\]

Equivalently, with \(a,b\) ranging over nonnegative integers,

\[
\boxed{P_n(z)=\sum_{\substack{2a+7b=n\\a+b>0}}\frac{n}{a+b}\binom{a+b}{b}z^{a+3b}.}
\]

The cyclic-gap characterization underlying the result is exact: if consecutive selected vertices are separated clockwise by distances two or three, then every distance-three gap must be followed by at least two distance-two gaps (cyclically), and conversely these conditions suffice. These cyclic configurations are canonically tiled by length-two blocks with one selected vertex and length-seven blocks with three selected vertices. The complete polynomial includes the exceptional absence \(P_5(z)=0\) and the two alternating sets on every even cycle. For the triangle, which lies outside the main assertion, \(P_3(z)=3z\).

Let \(p_n=P_n(1)\). Then \(p_n\sim\lambda^n\), where \(\lambda\approx1.1907127070818\) is the unique positive root of \(\lambda^7-\lambda^5-1=0\). Ordinary independent dominating sets have total number \(q_n\sim\mu^n\), with \(\mu\approx1.32471795724475\) satisfying \(\mu^3-\mu-1=0\). Consequently \(p_n/q_n\sim(\lambda/\mu)^n\): independence plus one-step defense becomes exponentially rare even within the independent dominating family.

## Assumptions and scope

The vertices of \(C_n\) are labelled \(0,1,\dots,n-1\), and edges join residues differing by one modulo \(n\). A set \(S\) dominates if every vertex is in \(S\) or has a neighbor in \(S\). It is secure dominating if, for every \(u\notin S\), there exists an adjacent \(v\in S\) for which \((S\setminus\{v\})\cup\{u\}\) dominates. It is independent secure dominating if it is both independent and secure dominating. No independence condition is imposed on the replacement set. The theorem concerns distinct labelled vertex subsets, not rooted cyclic words, witnesses, or orbits under rotation.

## Proof

**1. Allowed gaps.** Fix \(n\ge6\) and let \(S\) be independent dominating. In cyclic order, consecutive members of \(S\) are separated by either two or three edges: distance one violates independence; distance at least four leaves an intermediate vertex without a selected neighbor. Denote such distances by *short* (two) and *long* (three). Conversely every cyclic gap sequence of short/long distances defines an independent dominating set.

**2. Local defense criterion.** Consider a long gap with selected endpoints \(v\) and \(w=v+3\) (cyclic indices). The unselected vertex \(v+1\) is adjacent to just the selected endpoint \(v\). Moving the guard from \(v\) to \(v+1\) loses coverage of \(v-1\), unless the preceding selected vertex is \(v-2\), that is, the gap preceding \(v\) is short. Similarly \(v+2\) can be defended exactly when the gap following \(w\) is short. In each successful case all other vertices retain a selected neighbor. For a short gap with endpoints \(v,v+2\), its unique interior vertex \(v+1\) can be defended by moving \(v\) right if and only if the preceding gap is short, or by moving \(v+2\) left if and only if the following gap is short. These are the only candidate defenders. For \(n\ge6\) no exceptional wraparound edge alters these checks.

Therefore every long gap must have two short neighbors and every short gap must have at least one short neighbor. This is equivalent to requiring that between any two long gaps in cyclic gap order there occur at least two short gaps. When there is only one long gap, the condition applies around the complete cyclic return to that same gap.

**3. Canonical block decomposition.** Associate every long gap with the next two short gaps. The separation condition makes these triples pairwise disjoint. They are length-seven blocks (three selected starting points, cyclic vertex extent seven). Every remaining short gap is a length-two block (one selected starting point, vertex extent two). The original gap word and hence \(S\) can be recovered uniquely, so this is a bijection with labelled circular tilings by such blocks. If there are \(a\) short blocks and \(b\) long blocks, circumference is \(2a+7b\) and number selected is \(a+3b\).

**4. Exact labelled enumeration.** There are \(\binom{a+b}{b}\) ordered block-type words of length \(a+b\). Assigning the origin of one block to a labelled vertex gives \(n\) choices. Every labelled tiling has exactly \(a+b\) choices of distinguished block origin. Therefore the number of labelled tilings with these block counts is \(\frac{n}{a+b}\binom{a+b}{b}\). Summing yields the asserted polynomial; the marked-cycle identity \(-\log(1-u-v)=\sum_{r\ge1}(u+v)^r/r\) gives the coefficient-extraction form with \(u=zx^2\) and \(v=z^3x^7\).

**5. Small cycles.** On \(C_4\), the only independent dominating sets are the two alternating pairs, and each is secure; the formula gives \(2z^2\). On \(C_5\), each independent dominating pair has gap word (short,long), violating the two-short separation condition; the formula gives zero. For \(C_3\), exactly the three singleton sets qualify, handled separately. The local proof for \(n\ge6\) and these direct base cases cover all simple cycles.

**6. Exponential comparison.** At \(z=1\), the ordinary generating function derived by applying \(x\partial_x\) to the logarithm has denominator \(1-x^2-x^7\). It has a unique dominant positive real simple zero \(\rho\): by the triangle inequality, any zero of modulus \(\rho\) requires both phase exponents two and seven to agree with phase one, which, because the exponents are coprime, forces the positive real zero. The local form of the logarithmic derivative is \((1-x/\rho)^{-1}+O(1)\) at that zero, giving \(p_n\sim\rho^{-n}\). The same argument for all independent dominating sets, whose cyclic gap distances are unrestricted two/three, gives \(q_n=n[x^n]\log(1/(1-x^2-x^3))\sim\sigma^{-n}\). Setting \(\lambda=1/\rho\) and \(\mu=1/\sigma\) yields the stated roots and ratio.

## Verification

The included standalone C++17 program `verify_cycle.cpp` tests all \(2^n\) vertex subsets of every labelled cycle with \(4\le n\le22\). It independently evaluates initial independence, domination, every admissible neighbor-replacement security test, the cyclic-gap characterization, and the binomial coefficient formula. The command `c++ -std=c++17 -O3 -Wall -Wextra verify_cycle.cpp -o verify_cycle && ./verify_cycle` returned `CYCLE_INDEPENDENT_SECURE_VERIFY_OK` for all such \(n\). For example, the total counts at circumferences \(14,18,21,22\) are respectively \(9,29,28,57\). These finite checks are corroborative, not a replacement for the infinite argument above.

## Relationship to prior work

J. Pavan Kumar and P. Venkata Subba Reddy, *Algorithmic Aspects of Some Variants of Domination in Graphs*, first public preprint 31 January 2020, introduce the independent secure domination invariant and give the minimum cardinality of such a set in cycles apart from the triangle/pentagon exceptions (their Proposition 4). Their scalar minimum result is **prior work**, not a novelty claim here. The result proved here instead determines every valid labelled configuration, every size coefficient, a canonical block bijection and an exponential enumeration gap relative to ordinary independent domination. Independent Roman domination uses three-valued labels and a different feasibility condition, so its weight enumerators do not by definition provide these secure-replacement coefficients.

## Limitations

The theorem concerns simple cycles and standard one-guard secure domination under an initially independent set, not multiple simultaneous repairs, a requirement of independence after each repair, graph powers, or general graphs. A known minimum-cardinality result is not reasserted as new. The novelty comparison is based on inspectable primary literature and indexed mathematical searches; unindexed related enumerations could exist. No independent external audit has been performed.

## References

1. J. Pavan Kumar and P. Venkata Subba Reddy, *Algorithmic Aspects of Some Variants of Domination in Graphs*, arXiv:2002.00002 (first public 2020-01-31); journal DOI: 10.2478/auom-2020-0039. https://arxiv.org/abs/2002.00002
2. Z. Duan, H. Jiang, X. Liu, P. Wu and Z. Shao, *Independent Roman Domination: The Complexity and Linear-Time Algorithm for Trees*, *Symmetry* 14 (2022), 404. https://doi.org/10.3390/sym14020404
