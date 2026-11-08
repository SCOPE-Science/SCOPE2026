# Two-player coalitional stability is exactly efficiency in biclique max-\(q\)-cut games

## Finding

For every \(a,b\ge1\) and \(q\ge2\), consider the unweighted max-\(q\)-cut game on the complete bipartite graph \(K_{a,b}\). Each vertex chooses one of the same \(q\) labeled colors, and earns one point from each differently colored neighbor. The complete pure Nash equilibrium classification consists of two disjoint families:

1. **Proper profiles:** no color occurs on both sides of the biclique. These are socially optimal, unrestricted strong equilibria.
2. **Uniform mixed-support profiles:** possible exactly when \(q\mid a\) and \(q\mid b\), and comprising profiles with each color occurring \(a/q\) times on the left and \(b/q\) times on the right. These are Nash equilibria but fail stability against a coalition of two.

At a uniform profile, two players in opposite parts can strictly improve together if and only if their original colors differ. Their **unique** jointly beneficial reassignment is to exchange their colors; each gains precisely one utility unit. The number of profitable unordered pairs is exactly \(ab(1-1/q)\). Thus for this entire family

\[
\text{2-strong equilibria}=\text{strong equilibria}=\text{socially optimal profiles}=\text{proper colorings}.
\]

The worst-Nash price of anarchy is

\[
\operatorname{PoA}(K_{a,b},q)=
\begin{cases}
q/(q-1),&q\mid a\text{ and }q\mid b,\\
1,&\text{otherwise}.
\end{cases}
\]

The smallest host supporting an inefficient Nash equilibrium has \(2q\) vertices, namely \(K_{q,q}\).

Let \(S(n,r)\) be the Stirling number of the second kind, with labeled vertices and labeled colors. The exact number of proper (equivalently, 2-strong or strong) profiles is

\[
D_{a,b,q}=
\sum_{r=1}^{\min(a,q-1)}\sum_{s=1}^{\min(b,q-r)}
\binom qr\binom{q-r}s\,r!S(a,r)\,s!S(b,s).
\]

The number of pure Nash profiles is

\[
N_{a,b,q}=D_{a,b,q}+\mathbf{1}_{q\mid a,\,q\mid b}
\frac{a!b!}{((a/q)!)^{q}((b/q)!)^{q}}.
\]

For example, \(K_{3,3}\) with three colors has \(42\) strong profiles and another \(36\) inefficient Nash profiles, giving \(78\) Nash profiles in total.

## Assumptions and scope

The host is an undirected, unweighted and loopless complete bipartite graph \(K_{a,b}\), where both parts are nonempty and all vertices are individually labeled. Every vertex has the same strategy set \(\{1,\ldots,q\}\), with \(q\ge2\). Every player earns the number of differently colored neighbors. A profitable deviation must strictly increase the utility of **every** participating player; a \(2\)-strong equilibrium resists coalitions of at most two, and a strong equilibrium resists coalitions of arbitrary size. Social welfare is the sum of all utilities, so every bichromatic edge is counted twice. The count formulas distinguish labeled strategy profiles; permuting color names generally changes the profile.

Write \(x_i\) for the count of vertices in the first part colored \(i\), and \(y_i\) for the count in the second part colored \(i\), with \(\sum_i x_i=a\) and \(\sum_i y_i=b\). A first-part vertex of color \(i\) has utility \(b-y_i\); a second-part vertex has utility \(a-x_i\). Therefore

\[
W(x,y)=2\left(ab-\sum_{i=1}^{q}x_iy_i\right),
\]

and the unconstrained social optimum is \(2ab\), realized by using one color on the first part and a different color on the second.

## Proof

**Step 1: classify every unilateral equilibrium.** A first-part vertex is a best responder precisely when its chosen color attains the smallest count among \(y_1,\ldots,y_q\). Analogously a second-part vertex is a best responder when its chosen color minimizes the coordinates of \(x\). Suppose a pure Nash profile omits some color on the first part. The minimum of the \(x_i\) is then zero, so every second-part vertex must use an omitted first-part color. The color supports are disjoint, giving family (i). The same conclusion applies if any color is omitted on the second part. If neither part omits a color, all \(q\) colors are used on both sides. Since every first-part color is then a best response, all \(y_i\) must equal \(b/q\); similarly all \(x_i\) equal \(a/q\). This requires \(q\mid a,b\) and gives family (ii). Conversely, a proper profile makes every vertex achieve its full possible degree; a uniform profile makes every available color yield the same utility. Both are Nash equilibria. They are disjoint since the second family has every color on both sides.

**Step 2: identify all profitable pairs in the uniform family.** Put \(m=a/q\) and \(n=b/q\). Initially, a first-part vertex has utility \(b-n\), and a second-part vertex has utility \(a-m\). Two vertices on the same side cannot both strictly improve, because their simultaneous recolorings do not alter any opposite-side color counts; each already receives a best-response utility. Consider a left vertex of color \(i\) and a right vertex of color \(j\), and let them change to colors \(i'\neq i\) and \(j'\neq j\). For the left vertex, the right counts after the joint move are \(y'_c=n-\mathbf{1}_{c=j}+\mathbf{1}_{c=j'}\). A strict gain means \(y'_{i'}<n\); necessarily \(i'=j\) and \(j'\neq j\). Symmetrically, the right vertex strictly gains only when \(j'=i\) and \(i'\neq i\). Therefore both gain if and only if \(i\neq j\), and then the sole improving recoloring exchanges \(i\) and \(j\); each gains exactly one. Among the \(ab\) cross-part vertex pairs, precisely \(\sum_i x_iy_i=ab/q\) share a color. Consequently \(ab-ab/q=ab(1-1/q)\) unordered cross-part pairs admit a strict joint improvement. The uniform profiles are never \(2\)-strong.

**Step 3: strong stability and welfare.** Every vertex in a proper profile receives its full degree, so no player can strictly improve under any change of colors, even in a coalition. Thus every proper profile is a strong equilibrium, and Step 2 excludes all other Nash profiles from the \(2\)-strong set. Since a strong equilibrium is also Nash, all three asserted sets coincide. Proper profiles achieve welfare \(2ab\); every uniform profile has \(\sum_i x_iy_i=ab/q\) and welfare \(2ab(1-1/q)\). Division yields the price-of-anarchy formula. A uniform profile requires each nonempty side to contain at least \(q\) vertices, so its first possible size is \(2q\), attained by \(K_{q,q}\).

**Step 4: count labeled colorings.** To count proper profiles using exactly \(r\) colors on the first side and \(s\) different colors on the second side, choose the two disjoint labeled color subsets in \(\binom qr\binom{q-r}s\) ways. A surjection from \(a\) labeled vertices onto \(r\) selected colors has \(r!S(a,r)\) possibilities, and similarly the right part has \(s!S(b,s)\). Summing the products over every \(1\le r\le\min(a,q-1)\) and \(1\le s\le\min(b,q-r)\) gives \(D_{a,b,q}\). The uniform profiles exist precisely when \(q\) divides both part sizes; independently on each side, the multinomial number of assignments with exactly equal color multiplicities is \(a!/((a/q)!)^q\) and \(b!/((b/q)!)^q\). Add this disjoint family to get \(N_{a,b,q}\). No unlabeled-vertex or unlabeled-color quotient is taken.

## Verification

The accompanying standalone Python 3 program `verify_maxcut_biclique.py` enumerates all complete labeled color profiles for every \(q\in\{2,3,4\}\), \(1\le a,b\le4\) and \(a+b\le7\). Across \(45\) model instances it tests \(58{,}547\) profiles. It computes utilities independently from the neighbor colors, checks every player's possible unilateral recoloring, and at every Nash profile checks all color-reassignment possibilities for every coalition of two. It compares the Nash classification with actual best responses, confirms exact counts via an independent inclusion-exclusion formula for surjections, verifies welfare and tests the unique-profitable-swap assertion pair by pair. Execution returns:

`VERIFIED: instances=45 profiles=58547; Nash, 2-strong, counts, blocking pairs`

These finite checks corroborate the complete proof in Steps 1–4; they do not prove the universal statements by themselves. The mathematical argument uses only the stated assumptions and exact integer counting.

## Relationship to prior work

Carosi, Fioravanti, Gualà and Monaco (2018) study coalitional stability for the max-\(k\)-cut game, proving general results on 5-strong equilibria and special conditions guaranteeing strong equilibria; the full preprint's principal results, relevant appendices and graph-family conditions were examined. They do not supply this all-parameter biclique converse (2-strong implies welfare-optimal), uniform Nash classification, profitable-pair uniqueness or labeled equilibrium formula. Gourvès and Monnot (2010) develop general bounds on strong stability; Garuglieri and collaborators (2020, 2024) study coalition resistance of globally optimal colorings. None of these implications reverses from two-agent resistance to welfare-optimality on a biclique.

Gogoi (2026) constructs a connected unweighted graph whose socially optimal max-\(k\)-cut coloring nevertheless admits a coalitional improvement. That counterexample is **not** complete bipartite and hence does not contradict the present biclique theorem. Its general necessary conditions for profitable coalitions also do not classify biclique Nash equilibria. The distinction is substantive: the family studied here is exactly one where two-player coalition resistance and optimal welfare coincide, whereas no such equivalence holds for general networks. Separate graph-coloring work on majority-\(C\) colorings concerns a different, nonstrategic property, not payoffs or coalition deviations.

## Limitations

The theorem assumes a complete, unweighted, undirected bipartite interaction graph; it makes no claim for arbitrary bipartite graphs, weighted bicliques, asymmetric color availability, price-of-stability for other payoff specifications, or mixed-strategy equilibria. Its original-literature comparison does not exclude unpublished, unindexed or differently named equivalent results; publication priority cannot be certified by finite searches. The finite computational verifier exhausts only the explicitly stated bounded instances. No independent external audit is claimed.

## References

- R. Carosi, S. Fioravanti, L. Gualà and G. Monaco, *Coalition Resilient Outcomes in Max \(k\)-Cut Games*, arXiv:1810.09278 (first public version 2018-10-22), https://arxiv.org/abs/1810.09278.
- L. Gourvès and J. Monnot, *The Max \(k\)-Cut Game and its Strong Equilibria*, TAMC 2010, DOI:10.1007/978-3-642-13562-0_22.
- A. Garuglieri, D. Madeo, C. Mocenni, G. Palma and S. Rinaldi, *Optimal Coloring Strategies for the Max \(k\)-Cut Game*, Mathematics 12(4), 604 (2024), DOI:10.3390/math12040604; related 2020 preprint arXiv:2006.05464.
- D. Madeo, C. Mocenni, G. Palma and S. Rinaldi, *A Game Theory Proof of Optimal Colorings Resilience to Strong Deviations*, Mathematics 10(15), 2781 (2022), DOI:10.3390/math10152781.
- H. Gogoi, *Social Optimality Does Not Imply Coalitional Stability in Unweighted Max-\(k\)-Cut Games*, arXiv:2610.04948 (2026-10-04), https://arxiv.org/abs/2610.04948.
