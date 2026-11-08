# Sharp global-altruism perfection threshold on complete bipartite friendship networks

## Finding

Let \(a,b\ge1\) be integers, let the undirected friendship network be the complete bipartite graph \(K_{a,b}\), and let the friend reward \(w\ge0\) be real, with enemy penalty \(-1\). A coalition partition \(\Pi\) is *perfect* if every agent weakly prefers it to every possible partition. With global sum-based equal-treatment utility as specified below, the grand partition \(\{N\}\) is perfect **if and only if**

\[
 w\ge \Lambda(a,b),\qquad
 \Lambda(a,b)=
 \begin{cases}
 0,&a=b=1,\\
 \max\!\left\{1,\frac{2(a-1)}{b+1},\frac{2(b-1)}{a+1}\right\},&a+b\ge3.
 \end{cases}
\]

If \(w>\Lambda(a,b)\), *every* agent strictly prefers \(\{N\}\) to every distinct partition. If \(w<\Lambda(a,b)\), a two-block partition makes an agent strictly better off than \(\{N\}\). At the boundary, the grand partition is perfect and at least one nontrivial two-block split ties for at least one agent. The original friend-oriented reward \(w=a+b\) always satisfies the criterion. The contrasting families \(\Lambda(1,m)=m-1\) for \(m\ge2\) and \(\Lambda(m,m)=\max\{1,2(m-1)/(m+1)\}\) show a sharp imbalance effect.

## Assumptions and scope

Let \(N=A\sqcup B\), with \(|A|=a\) and \(|B|=b\). All cross-part pairs are mutual friends, and all distinct same-part pairs are enemies. For \(i\in N\), write \(F_i\) and \(E_i\) for its friends and enemies. For any partition \(\Pi\), the coalition containing \(i\) is \(\Pi(i)\). The underlying individual valuation and globally altruistic utility are

\[
 v_i^w(\Pi)=w\,|F_i\cap\Pi(i)|-|E_i\cap\Pi(i)|,
 \qquad U_i^w(\Pi)=\sum_{j\in F_i\cup\{i\}}v_j^w(\Pi).
\]

Thus the agent counts valuations of **all** friends, including friends in other coalitions. The weighted rule is a one-parameter cardinal extension of the sum-based equal-treatment rule of Kerkmann, Rothe, and collaborators; the standard cardinal encoding gives friend weight \(|N|=a+b\). We make no assertion for other degrees of altruism, for a fractional/mean utility, for arbitrary friendship graphs, or for a different enemy penalty normalization.

## Proof

**1. Pair-cut identity.** Fix an agent \(i\), and put \(H_i=F_i\cup\{i\}\). For distinct vertices \(u,v\), define their multiplicity
\[
 h_i(u,v)=\mathbf{1}_{\{u\in H_i\}}+\mathbf{1}_{\{v\in H_i\}}.
\]
For any partition \(\Pi\), direct expansion of the definition of \(U_i^w\) gives
\[
 U_i^w(\{N\})-U_i^w(\Pi)
 =\sum_{\substack{\{u,v\}\subset N\\\Pi(u)\ne\Pi(v)}}h_i(u,v)
 \left(w\,\mathbf{1}_{\{uv\in E(K_{a,b})\}}-\mathbf{1}_{\{uv\notin E(K_{a,b})\}}\right).
\tag{1}
\]
(The summation is over unordered pairs of *distinct* vertices; the nonedge indicator excludes self-pairs.) For a nontrivial cut \(S\subsetneq N\), define \(F_i(S)\) and \(E_i(S)\) as the sums of \(h_i(u,v)\) over, respectively, crossing friendship edges and crossing enemy pairs. Its utility gap is \(wF_i(S)-E_i(S)\). Every nontrivial cut has \(F_i(S)>0\): the graph is connected, and every crossing friendship edge is incident to a friend of \(i\), or to \(i\) itself.

If \(\Pi\) has blocks \(C_1,\ldots,C_t\), every pair separated by \(\Pi\) occurs in exactly two cuts \((C_k,N\setminus C_k)\). Hence its gap in (1) is exactly half the sum of the \(t\) cut gaps. In particular, \(\{N\}\) is perfect if and only if all two-block cuts are nonnegative for all agents; the threshold is the maximum of \(E_i(S)/F_i(S)\) over agents and nontrivial cuts. For strict inequality above the maximum, every nontrivial cut gap is strictly positive, and so is every nontrivial partition gap.

**2. Exact cut ratios for one shore.** By symmetry fix \(i\in A\), and orient a cut so its side \(S\) contains \(i\). Let \(x=|S\cap A|\), \(y=|S\cap B|\), where \(1\le x\le a\), \(0\le y\le b\), and \((x,y)\ne(a,b)\). Counting crossing pairs with their multiplicities gives
\[
 F_i(S)=(x+1)(b-y)+(a-x)y,
 \qquad E_i(S)=(a-x)+2y(b-y).
\tag{2}
\]
For fixed \(y\), the ratio \(E_i(S)/F_i(S)\) is fractional-linear in \(x\), with positive denominator, so its maximum is at \(x=1\) or \(x=a\), among feasible endpoints.

At \(x=a\), necessarily \(y<b\), and the ratio is \(2y/(a+1)\le2(b-1)/(a+1)\), with equality at \(y=b-1\). At \(x=1\), put \(p=a-1\) and \(q=2(b-y)\). Then
\[
 \frac{E_i(S)}{F_i(S)}=\frac{p+yq}{q+py}.
\tag{3}
\]
For \(y=0\) this equals \(p/(2b)\); for \(y=1\) it equals \(1\) when the cut is proper. For \(y=b\) (only feasible if \(a>1\)) it equals \(1/b\). For \(2\le y<b\), if \(q\le p\), subtraction of numerator and denominator yields \((y-1)(q-p)\le0\), so (3) is at most \(1\). If \(q>p\), use \(q+2(y-1)=2(b-1)\) and the exact identity
\[
 \bigl(q+2(y-1)\bigr)(q+py)-(p+2)(p+yq)
 =(q-p)(q+p-2)+2p(y-2)(y+1)\ge0.
\]
Because \(q\ge2\), this proves (3) is at most \(2(b-1)/(a+1)\). Thus for this shore the largest cut ratio, excluding the two-vertex degenerate case, is bounded by
\[
 \max\left\{1,\frac{a-1}{2b},\frac{2(b-1)}{a+1}\right\}.
\tag{4}
\]
The displayed \(1\) is attained by the cut containing one vertex of each shore whenever \(a+b\ge3\), and the last term by \(x=a,y=b-1\). The first term, when positive, is attained by \(x=1,y=0\).

**3. Both shores, attainment, and exact threshold.** Repeating the calculation with \(i\in B\) interchanges \(a,b\). Since
\[
 \frac{a-1}{2b}\le\frac{2(a-1)}{b+1},\qquad
 \frac{b-1}{2a}\le\frac{2(b-1)}{a+1}
\]
for all \(a,b\ge1\), the maximum over both shores is exactly the stated \(\Lambda(a,b)\), with every nonzero maximizer realized by one of the concrete two-block cuts above. When \(a=b=1\), there are no enemy pairs, all cut ratios are zero, and \(\Lambda=0\). This proves all directions and boundary statements.

Finally, for \(a+b\ge3\), both fractions inside \(\Lambda\) are at most \(a+b\), and \(1\le a+b\), so \(w=a+b\) is always sufficient. The family values follow by substitution. \(\square\)

## Verification

Run `python3 verify.py` with standard-library Python. The independent checker computes crossing pair weights directly (without using equation (2)), exhaustively checks all cuts for positive shore sizes up to eight subject to total size eleven, and enumerates all labeled set partitions for the feasible sizes up to seven against exact integer/rational utilities and threshold boundaries. It additionally checks equation (3)'s proposed upper bound over sizes through 34. In the recorded replay it passed 374,353 threshold comparisons and 85,922 agent/partition utility comparisons. Finite enumerations corroborate but do not constitute the proof for all sizes; the argument above is the infinite-size proof.

## Relationship to prior work

Kerkmann and Rothe introduced global altruistic coalition formation in 2020. Kerkmann, Cramer and Rothe's expanded study (arXiv:2301.05674, initial version January 13, 2023) defines sum-based equal-treatment global utilities and proves that components in a perfect partition must have graph diameter at most two (Proposition 17), but gives an example showing the converse fails (Example 19). Complete bipartite networks have diameter at most two, yet that necessary condition cannot decide perfectness. The present exact shore-size-dependent threshold, valid for a variable friend-to-enemy weight and including the original normalization, is not a restatement of that necessary condition.

Other altruistic *hedonic* models may ignore friends in other coalitions and consequently have different utilities; their star/cycle theorems do not automatically imply this global result. A mathematical-record and source-text search did not identify a prior equivalent exact threshold, but this is not a claim of proven uniqueness in the literature.

## Limitations

Only connected, complete bipartite mutual-friendship graphs and globally summed valuations are treated. The weight \(w\) is a cardinal generalization, not an assertion that all weights appear in the original fixed-weight encoding. The property proved is *perfectness* of the grand partition, stronger than several stability notions but not a characterization of those other notions on arbitrary partitions. Exhaustive checks are finite. Priority may be affected by unindexed work or a classification embedded in literature not fully retrievable; the earliest dated expanded public source used for cohort assignment is the January 13, 2023 arXiv preprint, while a shorter 2020 predecessor was also inspected (its exact day of initial public availability was not recovered).

## References

- A. M. Kerkmann and J. Rothe, *Altruism in Coalition Formation Games*, IJCAI 2020, pp. 347–353, DOI: 10.24963/ijcai.2020/49, https://ijcai.org/Proceedings/2020/49.
- A. M. Kerkmann, S. Cramer and J. Rothe, *Altruism in Coalition Formation Games*, arXiv:2301.05674v1 (January 13, 2023), https://arxiv.org/abs/2301.05674. In particular Section 2 and Proposition 17/Example 19 of the expanded version.
- N.-T. Nguyen, A. Rey, L. Rey, J. Rothe and L. Schend, *Altruistic Hedonic Games*, AAMAS 2016, pp. 251–259 (contrast between hedonic and global altruism).
