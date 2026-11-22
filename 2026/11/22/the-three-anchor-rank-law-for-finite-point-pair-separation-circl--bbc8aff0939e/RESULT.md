# The three-anchor rank law for finite point-pair separation circles

## Finding

Consider finite circles with *unoriented point-pair separation* as their only relation. In this natural Fraïssé class, the one-point-extension rank of every finite circle and every marked induced substructure is explicit. In addition, the rank distribution over **all** marked subsets has a closed formula.

For every integer \(n\ge3\), write \(\mathcal S_n\) for a circle of \(n\) distinct points in the strict quaternary language \(S\). The relation \(S(a,b,c,d)\) holds exactly when the two pairs \(\{a,c\}\) and \(\{b,d\}\) alternate around the circle; it is false on repeated coordinates. There is no chosen orientation or starting point. Ranks below refer to the finite-structure rank introduced in [1], with prime extensions taken in the class of all such finite separation structures.

**Exact rank of a marked substructure.** Let \(F\subseteq\mathcal S_n\) contain \(m\ge3\) marked points. In either cyclic orientation, let \(g_1,\ldots,g_m\) count the *unmarked* points in successive gaps of the marked circle. Then
\[
\operatorname{rk}_{\mathcal S_n}(F)=\min_{1\le i\le m}\left\lfloor\log_2(g_i+1)\right\rfloor.
\]
In particular, \(\operatorname{rk}_{\mathcal S_n}(F)\ge k\) if and only if all marked gaps contain at least \(2^k-1\) unmarked points, for each integer \(k\ge0\).

**Rank of the entire circle.** For \(n\ge3\),
\[
\operatorname{rk}(\mathcal S_n)=3+\left\lfloor\log_2\left\lfloor\frac n3\right\rfloor\right\rfloor.
\]
For \(0\le n\le2\), the rank is \(n\). Thus the least circle achieving rank \(h\ge3\) has precisely \(3\cdot 2^{h-3}\) vertices.

**Exact finite rank census.** Let \(n\ge m\ge3\) and \(k\ge0\) be integers. The number \(H_{n,m}(k)\) of \(m\)-point subsets \(F\) of the labelled \(n\)-point circle with \(\operatorname{rk}_{\mathcal S_n}(F)\ge k\) is
\[
H_{n,m}(k)=
\begin{cases}
\displaystyle\frac nm\binom{n-m2^k+m-1}{m-1},&n\ge m2^k,\\[4pt]
0,&n<m2^k.
\end{cases}
\]
The number of subsets of **exact** rank \(k\) is \(H_{n,m}(k)-H_{n,m}(k+1)\). Moreover the largest rank among \(m\)-point subsets is
\[
\max_{|F|=m}\operatorname{rk}_{\mathcal S_n}(F)=\left\lfloor\log_2\left\lfloor\frac nm\right\rfloor\right\rfloor,
\]
attained by nearly equally spaced marked points.

## Assumptions and scope

Let \(\mathcal F\) be the hereditary class of finite structures obtained by restricting unoriented cyclic pair-separation to finite point sets, including the empty structure and circles on fewer than four points, where \(S\) is empty. This class is Fraïssé: finite circular orders can be amalgamated by simultaneously inserting points of the two extensions in the gaps of the common finite subcircle (with a compatible choice of reversal). The first three points have only the empty atomic diagram. On four or more named points, the alternating-quartet relation determines the unoriented circular order.

For every finite \(X\in\mathcal F\) and marked induced substructure \(F\subseteq X\), define \(r_X(F)\ge0\). Recursively, \(r_X(F)\ge j+1\) exactly when *each* abstract one-point extension \(E\supset F\) in \(\mathcal F\), considered over the individually named elements of \(F\), has a realization \(F\cup\{x\}\subseteq X\) with \(r_X(F\cup\{x\})\ge j\). Define \(\operatorname{rk}(X)=r_X(\varnothing)\). All these ranks are finite nonnegative integers for finite \(X\), because successive successful realizations strictly increase the size of the marked set. Isomorphism over \(F\), not merely isomorphism of unmarked extensions, is essential.

The binomial formula counts marked *subsets* of a fixed labelled circle; it does not count isomorphism classes of marked circles or coloured and oriented variants. For the formula, \(g_i\) is always the number of unmarked points strictly between consecutive marked points, so \(\sum_i g_i=n-m\).

## Proof

**1. One-point extension types.** For \(|F|=0,1,2\), every abstract extension over the named base has the same \(S\)-diagram: there are not yet four distinct entries to evaluate. For \(m=3\), adjoining a fourth point creates one of three distinct alternating-pairing patterns, according to the cyclic gap of insertion. For \(m\ge4\), the separation data on marked quartets recover the cyclic order of \(F\) up to reversal. The alternation statements containing three marked points and the new point distinguish every insertion gap and depend only on that gap. Indeed, fixing three anchors partitions a circle into three arcs; the new point's position relative to them is recovered from the three possible pair separations. Varying the triple refines this to the consecutive gap in the full marked order. Thus the abstract prime extensions over a named \(m\)-point base, \(m\ge3\), correspond **bijectively** to the \(m\) cyclic gaps.

**2. Gap threshold.** Prove by induction on \(k\ge0\) the equivalence
\[
r_{\mathcal S_n}(F)\ge k\quad\Longleftrightarrow\quad g_i\ge 2^k-1\text{ for every }i,
\]
for every \(n\ge m\ge3\) and every marked \(F\). For \(k=0\), the right side is automatic, matching the rank definition. Assume the equivalence for \(k\). At level \(k+1\), every possible insertion-gap type must have some realizing unmarked point whose addition leaves rank at least \(k\). Inserting a point into a gap of size \(g\) creates two new nonnegative gaps of sizes \(a,b\) with \(a+b=g-1\); all other gaps remain unchanged. By induction, such a split has rank at least \(k\) if and only if
\[
a,b\ge2^k-1\qquad\text{and every unsplit gap is at least }2^k-1.
\]
A split satisfying the two inequalities exists exactly when \(g\ge2(2^k-1)+1=2^{k+1}-1\). Since the challenger may choose *any* old gap, all gaps must meet this larger threshold. Conversely, if all do, each challenged gap can be split with the required lower bounds, so every extension type has a valid response. This proves the equivalence. Taking the largest possible \(k\) yields the logarithmic minimum-gap formula, including zero gaps and the terminal full-set case.

**3. Empty-base rank.** Since there is just one prime-extension type until three points have been selected, the first three rounds may be chosen to produce **any** three distinct points of \(\mathcal S_n\). Formally, for \(n\ge3\), repeated application of the one-type successor definition shows
\[
r_{\mathcal S_n}(\varnothing)=3+\max_{|F|=3}r_{\mathcal S_n}(F).
\]
For a triple of marked points the nonnegative gaps total \(n-3\), so the maximum possible minimum gap is \(\lfloor n/3\rfloor-1\), achieved by splitting \(n-3\) as evenly as possible into three parts. Step 2 gives \(\max_{|F|=3}r_{\mathcal S_n}(F)=\lfloor\log_2\lfloor n/3\rfloor\rfloor\). With \(n=0,1,2\), the unique successive extension is realizable exactly until the universe is exhausted, giving ranks \(0,1,2\). Solving \(r_{\mathcal S_n}(\varnothing)\ge h\) for \(h\ge3\) yields the sharp least order \(3\cdot2^{h-3}\).

**4. Marked-subset census.** Fix \(n\ge m\ge3\), \(k\ge0\), and abbreviate \(d=2^k-1\). A qualifying set has all \(m\) gaps at least \(d\). Choose a marked starting vertex in \(n\) ways and list its \(m\) subsequent unmarked gap sizes clockwise. On subtracting \(d\) from each gap, the remaining weak composition has total
\[
(n-m)-m(2^k-1)=n-m2^k.
\]
For a nonnegative total, stars and bars gives exactly \(\binom{n-m2^k+m-1}{m-1}\) ordered vectors. Each qualifying unrooted marked subset has exactly \(m\) possible choices of marked starting point; orientation is fixed merely for this counting argument, not named in the structure. Dividing by \(m\) proves \(H_{n,m}(k)\). If the total is negative no such subset exists. Subtracting successive tails yields exact-rank counts. Finally, maximizing the least gap is achieved by a balanced weak composition, giving \(\lfloor(n-m)/m\rfloor=\lfloor n/m\rfloor-1\) and the final maximum-rank formula. Every asserted equality is attained by the described choices.

## Verification

Run `python3 separation_rank_verify.py` with Python 3 and no third-party modules. The checker constructs each possible abstract one-point extension by its complete alternating-quartet truth fingerprint on the individually marked base, computes the finite minimax rank recursively without using the gap formula, and compares the result with the theorem on **all** marked subsets of all circles of sizes zero through eleven. It also independently enumerates all marked subsets for sizes three through sixteen to verify the complete rank-tail binomial formula for levels zero through four. The observed output concludes `ALL_CHECKS_OK game_n_max=11 count_n_max=16`. In particular the exact game-rank sequence on circles of sizes zero through eleven is \((0,1,2,3,3,3,4,4,4,4,4,4)\). This finite verification corroborates, but does not replace, the preceding proof for all finite orders.

## Relationship to prior work

López-Callejas and Navarro-Castillo [1], Definition 2.3, introduce the precise rank recursion used here and compute its finite-linear-order analogue in Section 6. The dyadic interval-splitting mechanism is already present in that work. Their inspected treatment concerns **linear orders** and contains neither the quaternary, reversal-invariant separation signature nor the three-anchor circle rank law and the exact distribution over all marked subsets. Thus the present result is an application and structural extension of the framework, not an independent invention of the rank or dyadic splitting method.

Assari, Hosseinzadeh and Macpherson [2] discuss circular separation relations among homogeneous relational structures, but their inspected discussion concerns representation and model-theoretic homogeneity rather than finite extension-game rank spectra. A previously indexed scientific result [3] classifies the **quantifier-rank-five first-order theories** of the finite quaternary separation circles; another [4] gives first-order quantifier-rank thresholds for the **oriented ternary cyclic-order** language. Neither statement computes the rank of the game in [1], the relative ranks of marked substructures, or their binomial distribution; agreement under five-move Ehrenfeucht–Fraïssé games is not equivalent to the one-point-extension rank recursion. The literature comparison is substantive but does not establish exhaustive historical priority.

## Limitations

The results are for finite uncoloured **unoriented point-pair separation** structures, with one strict quaternary relation, no named constants, and the specific prime-extension rank of [1]. They make no claim about infinite ordinal ranks, countably infinite limits, coloured circles, closed or oriented extensions, unrestricted first-order Ehrenfeucht–Fraïssé ranks, or other geometric invariants. The present derivation reuses a well-known binary gap-splitting idea; its claimed scope is the exact quaternary circular classification and marked-subset census. Related sources beyond those inspected might contain equivalent specializations, so historical priority remains provisional. Independent scientific validation has not been performed.

## References

1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461, first public 15 April 2026. Full text: https://arxiv.org/html/2604.14461 ; submission history: https://arxiv.org/abs/2604.14461 .
2. S. Assari, A. Hosseinzadeh and H. D. Macpherson, *Set-homogeneous hypergraphs*, Journal of the London Mathematical Society (2023), DOI: 10.1112/jlms.12796, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.12796 .
3. *Fifteen rank-five theories of finite circular point-pair separation structures*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-fifteen-rank-five-theories-of-finite-circular-point-pair-separat--160af653c332 .
4. *Sharp quantifier-rank cutoff and three-variable completeness for finite cyclic orders*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-quantifier-rank-cutoff-and-three-variable-completeness-for--5fa0dcc54b96 .
