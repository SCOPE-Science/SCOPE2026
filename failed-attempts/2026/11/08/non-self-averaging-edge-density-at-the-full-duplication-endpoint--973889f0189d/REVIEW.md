# Independent mathematical audit

## correctness

PASS

A birth adds d_U+ξ edges. For two-stars, old neighbors contribute Σ_(w~U)d_w, linking the parent contributes ξd_U, and the new vertex contributes choose(d_U+ξ,2). Using Σd=2E and Σd²=2S+2E recovers all three conditional recurrences and their stated polynomial solutions with the singleton initial values. (E_n−EE_n)/(n(n+1)) is bounded and has constant conditional expectation because centered increments multiply the previous centered count by (n+2)/n. This gives almost-sure and L² convergence of F_n and its limiting moments; the complement couples the same parent sequence with flipped coins, including deterministic endpoints. An independent check encodes the graph by a binary split tree with one coin per internal vertex: conditional on the tree, Var(E_n)=r(1−r) times Σ_v (a_v b_v)^2, with child leaf counts a_v,b_v. For an ordered root split the first subtree size is uniform on 1,…,n−1 by the unit-seeded Pólya urn, and the within-subtree choices are uniform conditional on the sizes. Thus H_1=0 and (n−1)H_n=Σ_{a=1}^{n−1}[(a(n−a))²+H_a+H_(n−a)] for the expectation of the sum. Substitution or the power-sum identity Σ a²(n−a)²=(n⁵−n)/30 gives H_n=n(n−1)(n²+n+3)/18. A bounded replay of this recurrence in scaled integers J_n=18H_n checked orders 2–64 (J_2 through J_5 are 18,90,276,660). The limit proof is not based on that bounded check.

## originality

FAIL

Féray–Rivera-Lopez already analyze the identical recursive cograph process, not merely a related duplication process. Their Theorem 1.11 proves a.s. graphon convergence, Proposition 1.13 gives the full split law, and Proposition 1.14 identifies exact finite marginals as graphon sampling. The displayed scalar variances are not quoted verbatim in the examined source, but both are mechanical second-moment corollaries of these exact statements, demonstrated below. The materially stronger same-process source is absent from the frozen prior-work discussion.

## value

FAIL

Non-self-averaging and an exact variance are natural statistics, but the actual new-claim remainder is only a routine second-moment readout of an exact same-model graphon and sampling law. The alternative scalar martingale and star recurrence are sound, yet do not create a distinct unsupported-in-prior-work invariant or extend the model, distribution or parameter range. Within the stated standard no substantive remainder warrants repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
