# Total and paired domination in commuting graphs of dihedral groups

## Finding

Let \(D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) with \(n\ge3\), and let \(\mathcal C(D_{2n})\) be the commuting graph on the noncentral elements. If \(n\) is odd, \(\mathcal C(D_{2n})\) has isolated reflection vertices, so it has neither a total dominating set nor a paired dominating set. If \(n\) is even, then \[\mathcal C(D_{2n})\cong K_{n-2}\sqcup \frac n2 K_2,\] and consequently \[\gamma_t(\mathcal C(D_{2n}))=\gamma_{\mathrm{pr}}(\mathcal C(D_{2n}))=n+2.\]

The parity of the rotation order therefore gives a sharp existence dichotomy for these strengthened domination parameters.

## Assumptions and scope

Let
\[
D_{2n}=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle,
\qquad n\ge3.
\]
The commuting graph \(\mathcal C(D_{2n})\) has vertex set
\[
D_{2n}\setminus Z(D_{2n})
\]
and distinct vertices are adjacent exactly when they commute.

A total dominating set \(S\) requires every vertex, including every vertex of \(S\), to have a neighbor in \(S\). A paired dominating set is a dominating set whose induced subgraph has a perfect matching.

## Proof

Every rotation commutes with every other rotation. A reflection \(sr^i\) commutes with a rotation \(r^a\) exactly when
\[
sr^i r^a=r^a sr^i,
\]
which is equivalent to
\[
r^a=r^{-a}.
\]
Thus a reflection commutes only with central rotations.

Two reflections \(sr^i\) and \(sr^j\) commute exactly when
\[
r^{j-i}=r^{i-j},
\]
equivalently
\[
2(j-i)\equiv0\pmod n.
\tag{1}
\]

If \(n\) is odd, then
\[
Z(D_{2n})=\{1\}.
\]
Equation (1) shows that distinct reflections do not commute. Each reflection is therefore isolated in the commuting graph, because it also commutes with no noncentral rotation. A graph with an isolated vertex has no total dominating set and no paired dominating set.

Now suppose \(n\) is even. Then
\[
Z(D_{2n})=\{1,r^{n/2}\}.
\]
The noncentral rotations form a clique of order \(n-2\). No reflection is adjacent to any of these rotations.

For the reflections, (1) gives
\[
sr^i\sim sr^j
\iff
j-i\equiv n/2\pmod n
\]
for distinct reflections. Hence the reflection vertices form exactly \(n/2\) disjoint edges. Therefore
\[
\mathcal C(D_{2n})
\cong
K_{n-2}\sqcup \frac n2 K_2.
\tag{2}
\]

Total domination is additive over connected components when each component has no isolated vertex. The clique \(K_{n-2}\) has total domination number \(2\), and every \(K_2\) component requires both of its vertices. Thus
\[
\gamma_t(\mathcal C(D_{2n}))
=
2+\frac n2\cdot2
=
n+2.
\]

The same lower bound applies to paired domination, because every paired dominating set is total dominating. Equality is attained by choosing two vertices of the clique and all reflection vertices. The two selected clique vertices form one matching edge, and each reflection component supplies its own matching edge. Therefore
\[
\gamma_{\mathrm{pr}}(\mathcal C(D_{2n}))
=
n+2.
\]

## Verification

The standalone checker constructs the dihedral group from its multiplication law, computes the center, builds the commuting graph on the noncentral elements, identifies connected components, and exhaustively determines total and paired domination minima for
\[
3\le n\le10.
\]

Exact output:

```text
VERIFY_OK
n=3 vertices=5 center=1 components=[1, 1, 1, 2] gamma_t=None gamma_pr=None
n=4 vertices=6 center=2 components=[2, 2, 2] gamma_t=6 gamma_pr=6
n=5 vertices=9 center=1 components=[1, 1, 1, 1, 1, 4] gamma_t=None gamma_pr=None
n=6 vertices=10 center=2 components=[2, 2, 2, 4] gamma_t=8 gamma_pr=8
n=7 vertices=13 center=1 components=[1, 1, 1, 1, 1, 1, 1, 6] gamma_t=None gamma_pr=None
n=8 vertices=14 center=2 components=[2, 2, 2, 2, 6] gamma_t=10 gamma_pr=10
n=9 vertices=17 center=1 components=[1, 1, 1, 1, 1, 1, 1, 1, 1, 8] gamma_t=None gamma_pr=None
n=10 vertices=18 center=2 components=[2, 2, 2, 2, 2, 8] gamma_t=12 gamma_pr=12
```

The computation is corroborative only. The theorem for all \(n\ge3\) follows from the explicit commutation equations above.

## Relationship to prior work

Vahidi and Talebi studied commuting graphs of dihedral and generalized quaternion groups and computed clique and independence parameters. Their accessible full text records the standard noncentral commuting-graph convention and the parity-dependent structure used for comparison.

Ali, Salman, and Huang later studied the commuting graph of the dihedral group in detail, including distance, detour distance, metric dimension, and the resolving polynomial. Their publication supplies the archive-era algebra classification used here.

Targeted searches for the exact graph together with “total domination,” “paired domination,” and “domination number” did not locate the existence dichotomy or the value \(n+2\). The result is not implied by the published clique or metric-dimension formulas: total domination must treat every disconnected component, and paired domination additionally requires a perfect matching inside the selected set.

## Limitations

The theorem uses the standard commuting graph on noncentral elements. Definitions that include central elements produce a different graph and different domination behavior.

No claim is made for generalized quaternion, semidihedral, or generalized dihedral groups.

The value for even \(n\) is a consequence of the exact component decomposition (2); the odd case is an existence obstruction rather than a finite numerical value.

## References

1. F. Ali, M. Salman, and S. Huang, “On the Commuting Graph of Dihedral Group,” *Communications in Algebra* 44 (2016), 2389–2401. DOI: 10.1080/00927872.2015.1053488.
2. J. Vahidi and A. A. Talebi, “The Commuting Graphs on Groups \(D_{2n}\) and \(Q_n\),” *Journal of Mathematics and Computer Science* 1 (2010), 123–127. DOI: 10.22436/jmcs.001.02.07.
3. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206.
