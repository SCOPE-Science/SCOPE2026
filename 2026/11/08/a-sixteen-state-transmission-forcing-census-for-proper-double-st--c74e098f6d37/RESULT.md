# A sixteen-state transmission-forcing census for proper double stars

## Finding

Let \(D_{a,b}\), for integers \(a,b\ge2\), be the tree with adjacent hubs \(x,y\), with \(a\) leaves adjacent only to \(x\) and \(b\) leaves adjacent only to \(y\). For transmission proportion \(0<\alpha\le1\) and threshold \(0<\beta\le1\), define the all-seed polynomial

\[
\mathcal T_{a,b;\alpha,\beta}(z)=\sum_{S\subseteq V(D_{a,b}):\ S\text{ successfully transmits}}z^{|S|}.
\]

**Theorem (complete finite-kernel formula).** For each \((p,q,h,g)\in\{0,1\}^4\), define \(E_{p,q,h,g}(a,b;\alpha,\beta)\in\{0,1\}\) using the following *four-vertex kernel*, which requires at most three synchronous rounds:

* Start with adjacent hubs \(x,y\), and include one white leaf at \(x\) if \(p=1\), and one white leaf at \(y\) if \(q=1\). Set the initial hub weights to \(h\) and \(g\); a hub with initial weight one is filled, and one with weight zero is white.
* In **round one only**, inject an extra \((a-p)\alpha\) into the white hub \(x\) and \((b-q)\alpha\) into the white hub \(y\), reflecting all initially filled ordinary leaves. Simultaneously, a filled hub with exactly one white kernel neighbour contributes \(\alpha\) times its current weight to that neighbour. Sum the contributions before thresholding at \(\beta\).
* In rounds two and three apply only the latter hub/leaf unique-white-neighbour transmission rule, never reusing a directed force; weights of already filled vertices remain unchanged. Let \(E_{p,q,h,g}=1\) if all present kernel vertices are filled by the end of round three, and \(0\) otherwise.

Then, for every \(a,b\ge2\) and every \(0<\alpha,\beta\le1\),

\[
\boxed{\mathcal T_{a,b;\alpha,\beta}(z)=
\sum_{p,q,h,g\in\{0,1\}}\binom ap\binom bq
E_{p,q,h,g}(a,b;\alpha,\beta)\ z^{a+b-p-q+h+g}.}
\]

This is an **exact parameter-dependent polynomial**, with at most sixteen explicitly specified terms, whose evaluation cost is bounded independently of \(a+b\). Every successful seed set on \(D_{a,b}\) fills the graph within three rounds; no successful set omits two leaves adjacent to the same hub. In particular, for \(\beta\le\alpha\), the kernel simplifies to the explicit polynomial

\[
\boxed{\mathcal T_{a,b;\alpha,\beta}(z)=z^{a+b-2}(z+a)(z+b)(1+z)^2.}
\]

The invariant is not generally upward closed even on proper double stars: on \(D_{2,2}\), with \(\alpha=4/5\) and \(\beta=1\), the three leaves consisting of both \(x\)-leaves and one \(y\)-leaf form a successful initial set, but adding hub \(y\) makes it unsuccessful.

## Assumptions and scope

The graph is finite, simple and undirected. A filled vertex sends \(\alpha\) times its current weight to its unique white neighbour, if one exists; each source acts at most once and newly filled vertices act only in later synchronous rounds. The recipient's weight is the sum of all concurrent contributions, and it fills if it reaches at least \(\beta\). Filled weights are retained. In the kernel, a nonpresent leaf is **absent**, not a filled graph vertex; the round-one injections are made only into initially white hubs and are made exactly once. These conventions match the weighted transmission-zero-forcing process of [1]. The main formula applies to positive parameters and \(a,b\ge2\), with threshold equalities included.

## Proof

**Leaf deficit bound.** Suppose two leaves of the same hub are initially unfilled. Each of those leaves has only the hub as neighbour. Until one fills, the hub has at least two unfilled neighbours and hence cannot contribute to either; there is no other possible source for them. Thus neither can ever fill. Therefore any successful seed set omits at most one leaf at each hub.

**Reduction.** Fix a successful seed set \(S\). Let \(p\in\{0,1\}\) and \(q\in\{0,1\}\) indicate the number of missing leaves at the two hubs, and let \(h,g\in\{0,1\}\) indicate their initial membership in \(S\). The \(a-p\) initially filled leaves adjacent to \(x\) each have only one possible white target, namely \(x\) itself if it is initially white. They therefore all send exactly \(\alpha\) in the first round when \(h=0\), and never contribute at a later round. The same argument applies to the \(b-q\) initially filled leaves at \(y\). These contributions are precisely the first-round injections stated in the theorem. The only other possible white vertices are the two hubs and the at most two omitted leaves. Their induced graph, their initial weights, and their possible directed forces are represented exactly by the prescribed kernel; simultaneous thresholds and weights are preserved. Induction on rounds proves equality of the original and kernel states on all initially white vertices.

**Three-round cutoff.** Every hub that fills must do so by round two: at round one it can receive contributions from its original leaves and any initially filled opposite hub; if neither hub newly fills at round one, no fresh source becomes available. If just one hub newly fills, then the only possible new hub contribution is from that hub in round two (a unique-white-neighbour force). Thus there can be no newly filled hub after round two. An originally white leaf can only be filled by its hub, and once its hub is filled, it is the hub's unique remaining white neighbour if any such forcing is possible. It therefore fills no later than the next round, at most round three. This proves the cutoff and the exact decision procedure.

**Enumeration.** For each four-bit pattern, there are exactly \(\binom ap\binom bq\) choices of the omitted named leaves, and each has \(a+b-p-q+h+g\) initially filled vertices. These cases partition all potentially successful seed sets, yielding the sixteen-term formula. When \(\beta\le\alpha\), every four-bit pattern succeeds: each unseeded hub has at least one seeded leaf and fills at the first step, while every omitted leaf fills as soon as its hub has no other white neighbour. Summing all sixteen choices gives \(z^{a+b-2}(z+a)(z+b)(1+z)^2\).

**Nonmonotonic witness.** In \(D_{2,2}\), seed both leaves of \(x\) and exactly one leaf of \(y\). In round one the hub weights are \(8/5\) at \(x\) and \(4/5\) at \(y\); only \(x\) fills. In round two \(x\) sends \((4/5)(8/5)=32/25\) to \(y\), which fills with weight \(52/25\); in round three \(y\) fills its remaining leaf using weight \((4/5)(52/25)>1\). If instead \(y\) is seeded initially, the white hub \(x\) receives \(8/5\) and fills after the first round; hub \(y\) could not force at round one because \(x\) and one of its own leaves were white. After \(x\) fills, \(y\)'s only white neighbour is its leaf and it sends just \(4/5<1\), so this larger seed set fails.

## Verification

The standalone `verify.py` implements both an ordinary-vertex, exact-rational simulator and the independent four-vertex quotient with first-round injections. For every \(2\le a,b\le5\), it checks all \(2^{a+b+2}\) labelled seed sets at each of 36 rational parameter pairs against every coefficient of the sixteen-state formula, totaling 576 graph/parameter comparisons. It also verifies the explicit nonmonotonic witness. Run `python3 verify.py` from the enclosing directory. Exhaustive finite tests corroborate but do not replace the all-parameter proof.

## Relationship to prior work

Berliner and collaborators [1] introduced transmission zero forcing, defined the weighted process, and determined complete graphs, complete bipartite graphs, paths and cycles, with general bounds. The present family consists of proper diameter-three trees and is not one of those solved families. Prior work on ordinary zero forcing and fractional forts of double stars [2] concerns different processes and does not determine the weighted sixteen-state census. In the \(\beta\le\alpha\) regime the formula reduces to ordinary zero forcing, which is not asserted as independently new. The novel contribution is the complete all-seed parameter-dependent quotient formula, the universal three-round cutoff for successful sets, and the sharp tree witness of upward-closure failure.

## Limitations

The finite-kernel formula is algorithmic rather than an expanded list of piecewise inequalities for all sixteen configurations. It determines each coefficient exactly using at most three synchronous rounds, with no computation depending on the number of leaves. The theorem excludes zero transmission parameters and makes no claim about general caterpillars or larger tree diameters. Full historical priority and independent mathematical validation remain outstanding.

## References

1. A. H. Berliner et al., *Transmission Zero Forcing*, arXiv:2606.22246v2, first publicly submitted 2026-06-20, https://arxiv.org/abs/2606.22246 .
2. *Fort hypergraph and fractional zero forcing of double stars*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-fort-hypergraph-and-fractional-zero-forcing-of-double-stars--6179dfc83bcc .
