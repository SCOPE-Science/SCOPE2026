# A periodic shattering law for minimum independent dominating sets of paths

## Finding
Let \(P_n\) be the simple path on the ordered vertices \(1,\ldots,n\), and let \(\mathcal I_n\) consist of the characteristic functions of **all independent dominating vertex sets of minimum cardinality**. The query domain is \(\{1,\ldots,n\}\), with label one meaning membership in the selected set. Write
\[
\Phi_n(z)=\sum_{d\ge0}s_d(n)z^d,
\]
where \(s_d(n)\) counts the distinct \(d\)-vertex sets shattered by \(\mathcal I_n\). For all \(n\ge1\), the *complete* polynomial is
\[
\Phi_n(z)=
\begin{cases}
1,&n=3k,\quad k\ge1,\\
1,&n=1,\\
1+4z,&n=4,\\
1+(2k+2)z,&n=3k+2,\quad k\ge0,\\
1+(3k+1)z+(2k^2+k-2)z^2,&n=3k+1,\quad k\ge2.
\end{cases}
\]
Consequently \(\operatorname{VCdim}(\mathcal I_n)\) is \(0\) when \(n=1\) or \(3\mid n\), is \(2\) when \(n\ge7\) and \(n\equiv1\pmod3\), and is \(1\) otherwise. In addition, for every \(k\ge0\),
\[
\operatorname{Ldim}(\mathcal I_{3k+2})=\lfloor\log_2(k+2)\rfloor.
\]
In particular the online-minus-static dimension gap within this connected-path family is \(\lfloor\log_2(k+2)\rfloor-1\), which is unbounded.

## Assumptions and scope
All graphs are finite, simple, and undirected. An independent dominating set has no adjacent selected vertices and every vertex is either selected or adjacent to a selected vertex; equivalently, it is an inclusion-maximal independent set. **Minimum cardinality** is a further condition, and the present concept class is generally a proper subclass of the set of *all* maximal independent sets. We use the standard convention that a singleton concept class has VC and Littlestone dimension zero. The constant coefficient \(s_0(n)\) is one because the concept class is nonempty.

## Proof
**1. Deficiency slots and all minimum solutions.** For \(n\ge1\), the minimum cardinality is \(r=\lceil n/3\rceil\): each chosen vertex dominates at most three vertices, while placing vertices at distance three (with an endpoint adjustment) attains this bound. Label the \(r+1\) gaps of unselected vertices before, between, and after the \(r\) selected vertices. The first and last gaps have sizes in \(\{0,1\}\), the \(r-1\) interior gaps in \(\{1,2\}\). Independence and domination give precisely these possibilities, and conversely every choice of permitted gap lengths reconstructs an independent dominating set. The largest total gap length is \(2r\). Thus the number of *short* gaps, each one shorter than its permitted maximum, is exactly \(3r-n\), equal to zero, one, or two. If their ordered indices are a subset \(H\subseteq[r+1]\), the selected vertices in increasing order are
\[
x_j=3j-1-|H\cap[j]|\qquad(1\le j\le r).
\]
The correspondence is bijective: all short-slot sets \(H\) of the prescribed size, and only those, occur. For \(n=3k\) there is one concept, establishing \(\Phi_n=1\).

**2. One-short-gap case and online depth.** For \(n=3k+2\), put \(r=k+1\). There is one short gap at an arbitrary index \(p\in[r+1]\). At each \(j\in[r]\), the only potentially selected vertices are \(3j-2\) and \(3j-1\), and respectively their labels are the truth values of \(p\le j\) and \(p>j\). Each of these \(2r\) vertices is nonconstant, while all other vertices are constantly unselected. Any two vertex queries are either nested/complementary threshold conditions on the ordered index \(p\), hence cannot realize four binary patterns. This proves \(\Phi_{3k+2}(z)=1+2rz\). There are exactly \(r+1=k+2\) concepts. Any shattered complete binary tree of depth \(d\) requires at least \(2^d\) distinct concepts, proving \(\operatorname{Ldim}\le\lfloor\log_2(k+2)\rfloor\). Conversely, at each node query one of the threshold vertices \(3j-2\), choosing \(j\) to split the remaining consecutive interval of possible \(p\)-values into halves. Recursing gives a complete tree of depth \(\lfloor\log_2(k+2)\rfloor\). This proves the equality for all \(k\ge0\).

**3. Two-short-gap case: the three-state representation.** For \(n=3k+1\), put \(r=k+1\). The two short-gap indices are \(1\le p<q\le r+1\). For each time \(j\in[r]\), set \(t_j=\mathbf1_{p\le j}+\mathbf1_{q\le j}\). This is a nondecreasing sequence with values in \(\{0,1,2\}\), and the selected vertex at that time is \(3j-1-t_j\). A vertex-membership query is therefore the equality test \(t_j=a\), where the available levels are \(a\in\{0,1\}\) at \(j=1\), \(a\in\{0,1,2\}\) at \(2\le j\le r-1\), and \(a\in\{1,2\}\) at \(j=r\). Every one of the \(3r-2=n\) vertices is nonconstant when \(r\ge2\). When \(r=1\) (\(n=1\)), there is only one concept. When \(r=2\) (\(n=4\)), there are only three concepts, so no pair can be shattered and \(\Phi_4=1+4z\).

**4. Exact classification of shattered pairs.** Assume \(r\ge3\). Two distinct vertices from the same time \(j\) cannot both occur in one concept, hence cannot form a shattered pair. For two queries \((j,a)\) and \((h,b)\), with \(j<h\), all-positive realizability forces \(a\le b\). The *exact* list of pairs which realize all four label patterns is

| State pair \((a,b)\) | Condition for shattering |
|---|---|
| \((0,1)\) | Any \(j<h\), except \((j,h)=(r-1,r)\) |
| \((0,2)\) | \(h\ge j+2\) |
| \((1,1)\) | Every \(j<h\) |
| \((1,2)\) | Any \(j<h\), except \((j,h)=(1,2)\) |

For completeness, these feasibility statements can be checked directly by placing \(p<q\) at integer thresholds: \(t_j=0\iff j<p\), \(t_j=1\iff p\le j<q\), and \(t_j=2\iff q\le j\). For state pair \((0,1)\), examples for positive/positive, negative/positive, and negative/negative are respectively \((p,q)=(j+1,h+1),(1,r+1),(1,2)\). Positive/negative is supplied by \((h+1,h+2)\) when \(h<r\), or by \((j+1,j+2)\) when \(h=r\) and \(j\le r-2\); otherwise it is impossible. For \((0,2)\), four patterns are respectively witnessed by \((j+1,j+2),(j+1,r+1),(1,j+1),(1,r+1)\) when \(h-j\ge2\), and the both-positive pattern is otherwise impossible. For \((1,1)\), the positive/positive, positive/negative, negative/positive patterns are witnessed by \((1,r+1),(1,h),(j+1,r+1)\). For the negative/negative pattern choose \((h+1,h+2)\) if \(h<r\), \((1,2)\) if \(h=r,j\ge2\), and \((2,3)\) if \(h=r,j=1\) (where \(r\ge3\)). Finally for \((1,2)\), positive/positive, positive/negative, negative/negative are supplied by \((1,j+1),(1,r+1),(j+1,r+1)\), while negative/positive is supplied by \((1,2)\) if \(j\ge2\) or \((2,3)\) if \(j=1,h\ge3\); it is impossible when \((j,h)=(1,2)\). No additional states can be shattered, because \((0,0)\) and \((2,2)\) have one-way logical implications and decreasing state pairs cannot be jointly positive.

Thus the number of shattered pairs is
\[
\binom r2+\left(\binom r2-1\right)+\left(\binom r2-1\right)+\binom{r-1}2=(r-1)(2r-1)-2=2k^2+k-2.
\]

**5. No shattered triple.** If two of three queried vertices share time \(j\), no all-positive realization exists. Otherwise order the times \(j_1<j_2<j_3\). If their target states are not nondecreasing, all-positive realization is again impossible. The following table displays one impossible *binary label pattern* for each of the ten remaining nondecreasing target-state triples, in their time order:

| Target states | Impossible labels |
|---|---|
| \((0,0,0)\) | \((0,0,1)\) |
| \((0,0,1)\), \((0,0,2)\) | \((0,1,0)\) |
| \((0,1,1)\) | \((0,0,1)\) |
| \((0,1,2)\) | \((0,0,0)\) |
| \((0,2,2)\), \((1,2,2)\) | \((0,1,0)\) |
| \((1,1,1)\) | \((1,0,1)\) |
| \((1,1,2)\) | \((1,0,0)\) |
| \((2,2,2)\) | \((1,0,0)\) |

Each impossibility follows solely from \(0\le t_{j_1}\le t_{j_2}\le t_{j_3}\le2\): equal extreme target states propagate, equal middle states cannot disappear then reappear, and every monotone triple necessarily matches at least one coordinate of \((0,1,2)\). Hence no support of size three is shattered, and no larger support can be shattered by heredity. Together with the previous steps, this proves the full polynomial and all VC dimensions.

## Verification
The accompanying standalone `verify_i_path.py` uses only Python 3 standard-library modules. It directly compares independently enumerated minimum independent dominating sets with a brute-force search over every vertex subset for \(1\le n\le16\); checks the entire \(s_0,s_1,s_2,s_3\) profile by support enumeration for \(1\le n\le43\); independently calculates Littlestone dimensions by binary decision-tree recursion for \(n=3k+2\) with \(0\le k\le10\); and exhausts every two-time state pair through \(r=15\). Executing `python3 verify_i_path.py` prints `MIN_I_PATH_SHATTERING_AND_ONLINE_PASS`. These finite checks corroborate but are not substitutes for the unrestricted proof above.

## Relationship to prior work
Samanmoo, Trakultraipruk, and Ananchuen (published December 18, 2019) studied the reconfiguration graphs formed by minimum-cardinality independent dominating sets of paths and cycles; their path results distinguish the three residue classes. Brewster, Mynhardt, and Teshima (arXiv first version March 14, 2023), Section 2, supply the useful explicit gap parametrization and solution counts \(1\), \(k+2\), and \(\binom{k+2}{2}\). Those results classify solution reconfiguration and cardinality, not vertex-trace shattering polynomials or online mistake-tree depth. The present theorem adds a vertex-incidence trace classification and an exact logarithmic online dimension in the one-deficiency residue class. The general distinction between VC dimension and Littlestone dimension is standard; no novelty is claimed for that definition or for binary search on a threshold class.

## Limitations
The online dimension is determined exactly here only for the residue class \(n\equiv2\pmod3\) (and trivially for the one-concept class). There is no claimed exact online formula for \(n\equiv1\pmod3\), nor a claim about all inclusion-maximal independent sets or arbitrary trees. The earlier reconfiguration classifications are essential inputs, and alternative terminology or later work could already contain some trace consequences; an independent priority review remains outstanding.

## References
1. R. Samanmoo, N. Trakultraipruk and N. Ananchuen, “γ-Independent dominating graphs of paths and cycles,” *Maejo International Journal of Science and Technology* **13** (2019), 245–256; published December 18, 2019. https://mijst.mju.ac.th/Vol13/index.htm
2. R. C. Brewster, C. M. Mynhardt and L. E. Teshima, “The i-Graphs of Paths and Cycles,” arXiv:2303.08190v1, March 14, 2023, especially Section 2. https://arxiv.org/abs/2303.08190
