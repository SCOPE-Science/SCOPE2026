# A uniform inverse-square commutativity law for regular-action restriction monoids

## Finding

Let \(G\) be any finite group of order \(n\ge1\). Let \(\mathcal R(G)\) be the inverse monoid consisting of the empty partial map and all nonempty restrictions of the left regular translations \(L_g(x)=gx\) of \(G\) to arbitrary subsets of \(G\). Write \(K(G)\) for the number of **ordered** pairs \((s,t)\in\mathcal R(G)^2\) satisfying \(st=ts\). Put
\[
\theta=(7/8)^{1/3}<1,\qquad N=n(2^n-1)+1.
\]
Then the following *simultaneous, group-independent finite bounds* hold for **every** finite group:
\[
\boxed{4^n\ \le\ K(G)\ \le\ 4^n\bigl[1+(n^2-1)\theta^n\bigr].}
\]
Moreover, if a commuting ordered pair is chosen uniformly, the probability that **both maps are partial identities** is at least
\[
\boxed{\frac{1}{1+(n^2-1)\theta^n}.}
\]
Consequently, uniformly over all finite groups with order \(n\to\infty\),
\[
\boxed{\frac{K(G)}{|\mathcal R(G)|^2}=\frac{1}{n^2}\left[1+O\!\left(n^2\theta^n\right)\right].}
\]
The implied constant is absolute. In particular, the limit is independent of whether the groups are abelian, solvable or nonabelian, despite potentially different commuting probabilities inside their groups of units. The statement does **not** assert an exact common value of \(K(G)\) at a fixed \(n\).

## Assumptions and scope

Composition of partial maps uses ordinary function composition, \((s\circ t)(x)=s(t(x))\). For \(g\in G\) and \(A\subseteq G\), put \(t_{g,A}(x)=gx\) for \(x\in A\), undefined otherwise. All \(t_{g,\varnothing}\) represent the **same** zero map. For nonempty \(A\), different \(g\) give distinct partial maps because a regular translation has no fixed agreements with a distinct translation. Thus \(|\mathcal R(G)|=n(2^n-1)+1\). Its idempotents are exactly the \(2^n\) partial identities \(t_{1,A}\), including zero; they all commute. A group of order one is permitted and the two-element monoid then has \(K(G)=4\).

## Proof

**Step 1: count with redundant translation labels.** For fixed \(g,h\in G\), let \(F_{g,h}\) be the number of ordered pairs of subsets \((A,B)\in\mathcal P(G)^2\) for which the partial maps \(t_{g,A}\) and \(t_{h,B}\) commute. Since the domain of \(t_{g,A}\circ t_{h,B}\) is
\[
D_1(A,B)=\{x\in G:x\in B,\ hx\in A\},
\]
and that of the reverse composite is
\[
D_2(A,B)=\{x\in G:x\in A,\ gx\in B\},
\]
commutation implies \(D_1=D_2\), irrespective of whether \(g\) and \(h\) commute in \(G\). If \(g=h=1\), all four Boolean choices for each \(x\) are valid, and therefore \(F_{1,1}=4^n\). If \(g,h\) do not commute, equality also forces both domains empty; this stronger condition is *not* needed for the upper bound.

**Step 2: a uniform forbidden local pattern.** If \(h\ne1\), then for any \(x\in G\), the event
\[
x\in B,\qquad x\notin A,\qquad hx\in A
\]
forces \(x\in D_1\setminus D_2\). The three membership bits are independent and equiprobable for a uniformly selected pair \((A,B)\); in particular, this event has probability \(1/8\). The left regular permutation \(x\mapsto hx\) has only cycles of length \(\ell=o(h)\ge2\). Choose a matching of consecutive directed edges on each cycle. It contains \(\lfloor\ell/2\rfloor\ge\ell/3\) edges, hence at least \(n/3\) edges across all cycles. Their vertex sets are disjoint, so their three-bit forbidden-pattern events are independent. Consequently the probability that the partial maps commute is bounded above by \((7/8)^{n/3}\), giving
\[
F_{g,h}\le4^n\theta^n\quad(h\ne1).
\]
If \(h=1\) and \(g\ne1\), reverse the roles of \((g,A)\) and \((h,B)\), obtaining exactly the same bound. Thus it applies to all \(n^2-1\) label pairs other than \((1,1)\). This is uniform in the multiplication structure of \(G\).

**Step 3: remove the shared zero.** For every pair of labels \((g,h)\), exactly \(2^{n+1}-1\) subset pairs have \(A=\varnothing\) or \(B=\varnothing\). All commute, but these raw pairs duplicate actual ordered pairs containing zero. Once they are removed, the remaining label-pairs describe the actual nonzero-map pairs *uniquely*. Adding back the \(2N-1\) ordered pairs with at least one zero gives the exact bookkeeping identity
\[
K(G)=\sum_{g,h\in G}F_{g,h}-n^2(2^{n+1}-1)+(2N-1)
=\sum_{g,h}F_{g,h}-2n(n-1)2^n+(n-1)^2.
\]
For \(n\ge1\), the correction subtracted from \(\sum F_{g,h}\) is nonnegative (it is zero at \(n=1\)). Hence
\[
K(G)\le\sum_{g,h}F_{g,h}\le4^n+(n^2-1)4^n\theta^n.
\]
The \(4^n\) ordered pairs of partial identities furnish the lower bound.

**Step 4: normalize and condition.** Since all \(4^n\) ordered partial-identity pairs commute, division by \(K(G)\) proves the conditional bound. Also
\[
\frac{4^n}{N^2}=\frac{1}{n^2}\bigl[1+O(2^{-n})\bigr]
\]
with an absolute implied constant for \(n\ge2\). Combining this with the finite sandwich and absorbing \(2^{-n}\) into \(n^2\theta^n\) yields the stated uniform asymptotic formula. No assumption about an infinite family of groups other than \(n\to\infty\) is needed.

## Verification

The standalone Python script `verify.py` performs actual partial-map composition on all elements of the restriction monoids for cyclic groups of orders \(1,2,3,4\), the nonabelian symmetric group \(S_3\), and the dihedral group of order eight, then computes the same pair counts by separately enumerating Boolean domains of pairs of group translations. The methods agree: respectively \(4,31,184,1021,21013,343897\) commuting ordered pairs. The sizes of those monoids are \(2,7,22,61,379,2041\). In every case every nonidentity label pair satisfies the proposed uniform local upper bound. The direct group-independent proof, not these finite tests, establishes all orders and all groups. To reproduce, run `python verify.py` with Python 3 and no nonstandard dependencies.

## Relationship to prior work

Derech [1] introduced and studied inverse monoids \(I(G)\) of restrictions of finite permutation groups, including their congruences and stable quasiorderings; its full public text was inspected. The present regular-action subclass is a specialization of that framework, not a new semigroup construction. Fernandes [2] studies the cyclic case and its cardinality, rank and presentations, but does not assert the present all-group commutativity asymptotic. The public mathematical note [3] gives an exact idempotent-commutant rank polynomial for every finite regular group action, and is a particularly relevant predecessor: its counted pairs have at least one *specified idempotent* rather than arbitrary pairs. The present uniform bound treats the complementary case in which both translation labels are nonidentity and identifies its group-independent exponential suppression. The established formula for elementary abelian two-groups is another special family with a sharper explicit finite census; it does not by itself imply a universal bound for all nonabelian finite groups. Eberhard [4] studies the *group* commuting probability, a distinct statistic.

## Limitations

This result gives a uniform sandwich and limiting law rather than the exact finite ordered commuting-pair count for arbitrary groups. The explicit exponential constant \(\theta=(7/8)^{1/3}\) is not claimed optimal. The regular left action is essential: nonregular faithful group actions can have distinct translations agreeing on some points, invalidating the unique-label count and the fixed-point-free matching argument. The conditional statement concerns pairs selected uniformly among **commuting** pairs, not independent uniform monoid elements. A complete historical-priority certification has not been performed. There is no independent mathematical audit.

## References

[1] V. D. Derech, *Stable Quasiorderings on Some Permutable Inverse Monoids*, Ukrainian Mathematical Journal 66 (2014), 499–513, DOI:10.1007/s11253-014-0948-1; author's public full-text upload dated 2015-07-12. https://www.researchgate.net/publication/279201486_Stable_Quasiorderings_on_Some_Permutable_Inverse_Monoids

[2] V. H. Fernandes, *On the cyclic inverse monoid on a finite set*, arXiv:2211.02155v1 (first posted 2022-11-03). https://arxiv.org/html/2211.02155v1

[3] *Idempotent-commutant rank polynomials recover the element orders of finite regular groups*, published mathematical note (2026), full `RESULT.md` inspected. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-idempotent-commutant-rank-polynomials-recover-the-element-orders--d8e52ca92e37

[4] S. Eberhard, *Commuting probabilities of finite groups*, Bulletin of the London Mathematical Society 47 (2015), 796–808, first posted 2015-07-28; paper concerns commuting in groups, not their inverse monoids of restrictions. https://doi.org/10.1112/blms/bdv050
