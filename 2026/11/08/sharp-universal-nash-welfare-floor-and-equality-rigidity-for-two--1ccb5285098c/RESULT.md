# Sharp universal Nash welfare floor and equality rigidity for two-agent EFX allocations

## Finding

Every complete two-agent EFX allocation of finitely many strictly positive goods with identical additive valuations retains at least \(2\sqrt{2}/3\) of the unrestricted optimal Nash social welfare. This factor is sharp. Equality holds exactly when the larger bundle has two equal-valued goods and the smaller bundle can be split into two equal-valued subbundles, as specified below.

## Assumptions and scope

Let \(G\) be a finite nonempty family of indivisible goods; each good \(g\in G\) has value \(v(g)>0\), common to two agents. Assume at least two goods so an unrestricted allocation with positive Nash welfare exists. An allocation partitions \(G\) into \(A\) and \(B\), and is **EFX** when for both ordered pairs of agents and for every good of the envied bundle, deleting that good eliminates envy. With \(a=v(A)\), \(b=v(B)\), its Nash social welfare is \(\operatorname{NSW}(A,B)=\sqrt{ab}\). Write \(P^\star=\max_{S\subseteq G}v(S)(v(G)-v(S))>0\) and \(\operatorname{NSW}^\star=\sqrt{P^\star}\).

## Proof

Exchange names so \(0\le a\le b\). Since valuations are common, the agent holding value \(b\) never envies the other. EFX is therefore precisely \(b-v(g)\le a\) for **every** good \(g\in B\).

**Case 1: the larger bundle contains one good.** Write its value \(b\). The entire complement totals \(a\le b\). Every bipartition keeps that unique good in one side, of value at least \(b\); the other side has value at most \(a\). Since the product \(x(T-x)\) decreases for \(x\ge T/2\), no bipartition improves on \(ab\). Hence \(P^\star=ab\), giving ratio one.

**Case 2: the larger bundle contains at least two goods.** Let \(s=\min_{g\in B}v(g)\). Since the goods are positive and there are at least two, \(s\le b/2\). EFX gives \(b-a\le s\), so \(a\ge b/2\). Put \(T=a+b\). This forces \(T/3\le a\le T/2\), hence \(ab=a(T-a)\ge 2T^2/9\). Independently, every allocation obeys \(P^\star\le T^2/4\). Therefore

\[\frac{\operatorname{NSW}(A,B)}{\operatorname{NSW}^\star}=\sqrt{\frac{ab}{P^\star}}\ge\sqrt{\frac{2T^2/9}{T^2/4}}=\frac{2\sqrt{2}}{3}.\]

For equality, both inequalities must be equalities. The first requires \(a=T/3\) and \(b=2T/3\), as \(a(T-a)\) is strictly increasing for \(a\le T/2\). EFX then gives \(s\ge b-a=b/2\); combined with \(s\le b/2\), this forces \(s=b/2\) and exactly two goods in \(B\), each of value \(u=b/2\). Thus \(a=u\). The other equality is \(P^\star=T^2/4\), requiring an exactly balanced division of total \(T=3u\). Since the two goods of size \(u\) cannot occur together in one half of value \(3u/2\), and goods in \(A\) total only \(u\), every equal split uses exactly one of these goods and a subbundle of \(A\) valued \(u/2\). Conversely, any such split makes the optimum exactly \(T^2/4\); the original \((B,A)\) is EFX because removing either \(u\)-good from \(B\) leaves \(u=a\). This proves the equality classification.

Choosing goods of values \((2,2,1,1)\), allocate \((2,2)\) versus \((1,1)\): the EFX product is \(4\cdot2=8\) and optimal product is \(3\cdot3=9\). The ratio is exactly \(2\sqrt{2}/3\). Because a positive lower bundle of value \(u\) must have a nonempty split into two positive halves, equality requires at least four goods.

## Verification

A standalone Python verifier exhaustively enumerates 456 unordered positive-integer item-value profiles, for 2 through 6 goods and values from 1 through 5. It independently recomputes unrestricted Nash-optimal subset products, enumerates 2,939 EFX allocations, checks the \(8/9\) squared-ratio inequality and verifies the necessary equal-case structure in its four equality cases. It separately tests the sharp four-good instance. Run `python3 verifier.py`. Finite enumeration is supplemental and is not used as a proof of the universal inequality.

## Relationship to prior work

Feng–Hu–Li (2026) prove a general worst-case EF1 welfare gap for identical agents; their result permits broader numbers of agents and addresses EF1, which is weaker than EFX. Yang and coauthors (2026) study guarantees for **arbitrary EF1** allocations of identical additive valuations, including a small-item regime. The accessible descriptions do not state the sharp **universal EFX** ratio or necessary-and-sufficient equality classification here; possible additional unpublished or uninspected coverage remains a priority risk. Feldman–Mauras–Ponitka (2024) prove existence of allocations satisfying simultaneous EFX/NSW performance, a different existential quantifier from the statement about **every** EFX allocation here. Amanatidis and coauthors (2021) discuss when an optimal-NSW allocation is EFX; that implication does not constrain Nash welfare of all other EFX allocations. The known full text and summaries are compared by implications, not by name alone.

## Limitations

The analysis requires strictly positive common item values, two agents, complete allocations and conventional unweighted geometric-mean Nash social welfare. It makes no claim for heterogeneous valuations, more agents or arbitrary partial allocations. Unindexed equivalent priority results or details of not-fully-accessible sources remain a risk. No independent scientific audit is claimed.

## References

- Y. Feng, W. Hu, S. Li, *New Convex Programming Technique for Nash Social Welfare and Scheduling*, arXiv:2604.24120, first submitted 2026-04-27; ICALP 2026, DOI:10.4230/LIPIcs.ICALP.2026.90. https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.90/LIPIcs.ICALP.2026.90.html
- Z.-S. Yang et al., *EF1-Constrained Nash Social Welfare with Identical Additive Valuations: Complexity, Guarantees, and Experiments*, arXiv:2609.03846, first submitted 2026-09-03. https://arxiv.org/abs/2609.03846
- M. Feldman, S. Mauras, T. Ponitka, *On Optimal Tradeoffs between EFX and Nash Welfare*, AAAI 2024. https://doi.org/10.1609/aaai.v38i9.28826
- G. Amanatidis et al., *Maximum Nash Welfare and Other Stories About EFX*, Theoretical Computer Science 863 (2021), 69–85. https://doi.org/10.1016/j.tcs.2021.02.020
