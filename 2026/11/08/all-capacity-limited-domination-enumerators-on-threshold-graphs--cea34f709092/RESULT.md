# All-capacity limited-domination enumerators on threshold graphs and clique bouquets

## Finding

For a finite simple graph \(G\) and integer \(k\geq0\), let \(\mathcal L_k(G;z)=\sum_D z^{|D|}\), where the sum runs over all vertex subsets \(D\) satisfying both: every vertex outside \(D\) has a neighbor in \(D\), and every \(u\in D\) has at most \(k\) neighbors outside \(D\). The convention \(k=0\) is used to express a recursion; the original parameter ordinarily has \(k\geq1\).

**Coning theorem.** If \(H\) is any nonempty graph of order \(q\), then, for \(k\geq1\),
\[
\mathcal L_k(K_1\vee H;z)
=\mathcal L_{k-1}(H;z)
+z\sum_{t=0}^{\min(k,q)}\binom qt z^{q-t}.
\]
For every \(k\geq0\), \(\mathcal L_k(H\sqcup K_1;z)=z\mathcal L_k(H;z)\), and \(\mathcal L_0(H;z)=z^q\). Starting at \(\mathcal L_k(K_1;z)=z\), these rules compute **every coefficient at every capacity** of the limited-domination polynomial of any threshold graph, in a polynomial number of integer arithmetic operations. In particular they count its minimum sets exactly rather than merely computing their minimum cardinality.

**Clique-bouquet theorem.** Let \(r\geq2\), let \(m_1,\ldots,m_r\geq1\) be integers, write \(M=\sum_i m_i\), and let
\[
W(m_1,\ldots,m_r)=K_1\vee\left(\bigsqcup_{i=1}^r K_{m_i}\right).
\]
For every integer \(1\leq k<M\), its complete cardinality enumerator is
\[
\boxed{\mathcal L_k(W;z)=
 z\sum_{t=0}^{k}\binom Mt z^{M-t}
 +\prod_{i=1}^r\left(\sum_{t=0}^{\min(k-1,m_i-1)}\binom{m_i}{t}z^{m_i-t}\right).}
\]
Set \(T=\sum_i\min(k-1,m_i-1)\), \(a=M+1-k\), and \(b=M-T\). The exact minimum size and number of labelled minimum sets are
\[
\boxed{\gamma_k^{\mathrm L}(W)=\min\{a,b\},\qquad
 \#\operatorname{Min}_k(W)
 =\mathbf1_{a\leq b}\binom Mk
 +\mathbf1_{b\leq a}\prod_{i=1}^r\binom{m_i}{\min(k-1,m_i-1)}.}
\]
The two summands count disjoint families (with and without the common apex); both must be retained at an equality boundary.

For the uniform generalized windmill \(W_{r,m}=K_1\vee rK_m\), \(r,m\geq2\), the formula yields a sharp transition in the kind of optimizer. Write \(M=rm\) and \(h=r(m-1)+1\). At \(k=1\), the minimum size is \(M\), with exactly \(M+1\) minimum sets. For \(2\leq k\leq m\), the minimum size is \(r(m-k+1)\), with \(\binom m{k-1}^{r}\) minima. For \(m<k<h\), the minimum size is \(r\), with \(m^r\) minima. At \(k=h\), the minimum size is still \(r\), but both families occur, giving \(m^r+\binom M h\) minima. For \(h<k<M\), the minimum size is \(M+1-k\), with \(\binom Mk\) minima. Empty parameter ranges are ignored.

## Assumptions and scope

All graphs are finite, simple and undirected. A dominating set may be the full vertex set. The graph join \(K_1\vee H\) adds one vertex adjacent to every vertex of \(H\); \(\sqcup\) is disjoint union. A threshold graph is one obtained from a single vertex by successively adding isolated or universal vertices. All enumerators count vertex subsets on the given labelled vertex set, not isomorphism classes. The initial source studied \(1\leq k<\Delta(G)\); extending the definitions to nonnegative \(k\) is a bookkeeping convention, not a change in the nontrivial \(k\geq1\) theorem. The clique-bouquet statement includes one-vertex blades, while the uniform phase classification assumes \(r,m\geq2\).

## Proof

Let \(a\) be the new universal vertex of \(K_1\vee H\). Partition its limited dominating sets into disjoint cases.

If \(a\in D\), every omitted vertex of \(H\) is dominated by \(a\). If exactly \(t\) vertices are omitted, then the apex has exactly \(t\) outside neighbors and requires \(t\leq k\). Every other selected vertex has no more than \(t\) outside neighbors, hence satisfies the same capacity restriction. Thus all \(\binom qt\) choices of omissions are valid, giving the second term of the coning formula.

If \(a\notin D\), the selected subset of \(H\) must dominate \(H\) and also the apex; since \(H\) is nonempty, any dominating subset of \(H\) is nonempty. Every selected vertex acquires the additional outside neighbor \(a\), so it meets the capacity \(k\) exactly when its outside-neighbor count inside \(H\) is at most \(k-1\). This is a bijection with the sets enumerated by \(\mathcal L_{k-1}(H;z)\). The two cases establish the coning identity.

An isolated vertex must belong to every dominating set, proving the isolate recurrence. If a proper selected set were \(0\)-limited, some omitted vertex would have a selected neighbor by domination; that selected neighbor would have an outside neighbor, a contradiction. Hence the sole \(0\)-limited dominating set is the whole graph. The base at \(K_1\) and induction along the threshold creation string prove that the displayed recurrences count every valid set exactly. Keeping coefficient arrays for at most \(q+1\) sizes and all \(q+1\) capacities at stage \(q\), with binomial coefficients precomputed, takes \(O(n^3)\) integer additions/multiplications and \(O(n^2)\) coefficient storage for a creation string of length \(n\). Bit complexity depends on coefficient lengths, which are \(O(n)\) bits because each coefficient is at most \(2^n\).

For \(W\), let \(a\) now be the common apex and remove it to obtain disjoint clique blades. If the apex is selected, exactly \(t\leq k\) of the \(M\) other vertices may be omitted, giving the first summand. If the apex is omitted, every clique must contain a selected vertex to dominate its vertices, and a selected vertex in clique \(i\) has exactly \(t_i+1\) outside neighbors when \(t_i\) vertices of that clique are omitted: its \(t_i\) omitted clique neighbors and the apex. Therefore \(0\leq t_i\leq\min(k-1,m_i-1)\), independently over cliques. Choosing the omitted vertices in each clique gives the product term. No other selected sets are possible.

In the apex-selected branch the largest allowable omission count is \(k\) (as \(k<M\)), so the least size is \(a=M+1-k\) and occurs \(\binom Mk\) times. In the apex-omitted branch the largest omission count is \(T\), so the least size is \(b=M-T\) and occurs \(\prod_i\binom{m_i}{\min(k-1,m_i-1)}\) times. The branches are disjoint and their equality case must be added, proving the minimum formulas.

For equal blade size \(m\), one has \(T=r\min(k-1,m-1)\). Thus \(b=r(m-k+1)\) while \(k\leq m\), and \(b=r\) afterward; the competing value is \(a=rm+1-k\). For \(k>1\) and \(k\leq m\), \(a-b=(r-1)(k-1)>0\). For \(k>m\), equality \(a=b\) occurs precisely at \(k=h=r(m-1)+1\), with opposite inequalities on either side. Substitution gives the complete phase and multiplicity classification, including \(k=1\).

## Verification

The accompanying self-contained `verify.py` constructs graphs using independent adjacency bitsets and enumerates all vertex subsets. It compares the entire enumerator and minimum multiplicity for 1,991 heterogeneous clique-bouquet/capacity cases, independently verifies the universal-apex recurrence in 5,405 graph/capacity cases, checks 693 uniform phase cases, and compares the threshold creation-string recurrence with direct enumeration in 4,608 cases of order up to nine. Its successful final marker is `VERIFY_OK`. All arithmetic uses exact integers and no external packages. These finite tests corroborate but do not replace the unrestricted proofs above.

## Relationship to prior work

Božović, Radić, Kovijanić-Vukićević and Tepeh introduced \(k\)-limited domination and established general bounds and basic families; in particular their universal-vertex lemma already gives the scalar \(k=1\) minimum \(|V(G)|-1\). That known scalar result is not claimed as new. Tepeh subsequently established computational hardness for fixed \(k\geq2\) and studied Cartesian products; the current graph constructions are threshold creation and common-apex clique unions, not Cartesian products. Related literature on \((0,k)\)-pitchfork domination uses equivalent terminology. The new claims here are the all-capacity **all-set enumerator** for the entire threshold-graph class, and the explicit all-size bouquet enumerator with minimum-set counts and phase boundaries. General results for complete multipartite graphs do not imply the bouquet theorem, since bouquets have edges within blades and lack the complete multipartite adjacency pattern.

## Limitations

The threshold recurrence requires a valid threshold creation string; it is not a counting algorithm for arbitrary graphs. The clique-bouquet phase formula assumes the specified common-apex union of cliques. The previously established \(k=1\) universal-vertex scalar minimum is excluded from novelty claims. Relevant historical priority remains provisional; no independent mathematical audit is claimed. The numerical tests cover only the stated finite ranges.

## References

1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević and A. Tepeh, *On k-limited domination in graphs*, arXiv:2606.22422 (first public 2026-06-21); open-access article, doi:10.1007/s40314-026-03902-2.
2. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428 (first public 2026-06-21).
3. Al-Harere and Abdlhusein, *Pitchfork domination in graphs*, as cited and compared in the introduction of reference 1 (related terminology; the historical work studies other capacity constraints).
