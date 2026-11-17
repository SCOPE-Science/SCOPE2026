# Exact primitive-three chip-firing energy bands on complete graphs

## Finding

Let \(n\ge3\) be an integer. In parallel chip-firing on the labelled simple complete graph \(K_n\), a vertex fires precisely when it has at least \(n-1\) nonnegative integral chips, sending one chip to every other vertex; all vertices update simultaneously. Let \(H_n(z)\) count **initially periodic configurations of least period three**, weighted by their total chip number. Set \([r]_z=1+z+\cdots+z^{r-1}\) for each positive integer \(r\), and
\[
P_n(z)=\sum_{\substack{a,b,c\ge1\\a+b+c=n}}
\frac{n!}{a!b!c!}\,z^{n(n-1)-(ab+bc+ca)}
[c]_z^a[a]_z^b[b]_z^c.
\]
Then the exact generating polynomial is
\[
\boxed{H_n(z)=P_n(z)+z^{n(2n-3)}P_n(z^{-1}).}
\]
Each coefficient counts labelled states, not cycle orbits. If \(L_n=n(n-1)-\lfloor n^2/3\rfloor\), the total chip numbers supporting primitive-three periodic configurations are **exactly**
\[
\boxed{[L_n,n(n-2)]\ \cup\ [n(n-1),\ n(n-2)+\lfloor n^2/3\rfloor],}
\]
where brackets denote *integer* intervals. Each integer in either interval occurs, and no total outside the intervals occurs. In particular, the middle-stair endpoints \(n(n-2)\) and \(n(n-1)\) each support exactly
\[
\boxed{3^n-3\cdot2^n+3}
\]
primitive-three configurations. The total number of primitive-three configurations equals
\[
\boxed{2\sum_{\substack{a,b,c\ge1\\a+b+c=n}}\frac{n!}{a!b!c!}c^aa^bb^c};
\]
the number of distinct primitive-three orbits is one third of this number. The coefficients of \(H_n\) are symmetric about the total chip number \(n(2n-3)\).

At the low-energy endpoint \(L_n\) (and, by symmetry, at the upper endpoint of the high-energy band) the number of configurations is
\[
B_n=\begin{cases}
\dfrac{n!}{m!^3},&n=3m,\\[3pt]
\dfrac{3n!}{(m+1)!m!^2},&n=3m+1,\\[3pt]
\dfrac{3n!}{(m+1)!^2m!},&n=3m+2.
\end{cases}
\]

## Assumptions and scope

The graph is loopless, connected, simple, labelled, and has \(n\ge3\) vertices. Chips are nonnegative integers; there is no bound on total initial chips, but periodic configurations of nontrivial period automatically occupy a finite box. A state is *initially periodic of least period three* if the third synchronous update returns the state and neither of the first two updates does so. Periodic orbits are counted with three different temporal phases as three states. The initial chip number is not a transient-state statistic. The identity is exact for every \(n\ge3\), not an asymptotic statement.

## Proof

Write \(x_v(t)\) for chips at vertex \(v\) before update \(t\), \(f_v(t)=\mathbf1\{x_v(t)\ge n-1\}\), and \(R(t)=\sum_v f_v(t)\). The exact synchronous update is
\[
x_v(t+1)=x_v(t)+R(t)-nf_v(t).
\]
If a state returns after three steps, summing this equation yields \(n\sum_{t=0}^2 f_v(t)=\sum_{t=0}^2R(t)\), independently of \(v\). Thus every vertex fires the same number \(h\in\{0,1,2,3\}\) of times during those three steps. If \(h=0\) or \(h=3\), the state is fixed, so a primitive-three state has \(h=1\) or \(h=2\).

First consider \(h=1\). Let \(A,B,C\) be the labelled vertex sets firing at times \(0,1,2\), and let \(a=|A|\), \(b=|B|\), \(c=|C|\). Their sets partition the \(n\) vertices. The exact firing/waiting conditions for the three updates give the following independent *if-and-only-if* intervals for initial chips:
\[
\begin{array}{c|c|c}
\text{group}&\text{allowed initial chips}&\text{number of values}\\\hline
A &[n-1,\ n+c-2]&c\\
B &[b+c-1,\ n-2]&a\\
C &[c-1,\ b+c-2]&b.
\end{array}
\]
To check necessity and sufficiency directly: a vertex in \(A\) starts by firing, then has chips \(x+a-n\) and \(x+a+b-n\) at times one and two; a vertex in \(B\) starts by waiting, fires with chips \(x+a\), then waits with \(x+a+b-n\); a vertex in \(C\) waits with chips \(x\) and \(x+a\), then fires with chips \(x+a+b\). Imposing the threshold \(n-1\) at the prescribed firing time, a strict threshold inequality at waiting times, and nonnegativity yields exactly the displayed intervals. Nonempty intervals force \(a,b,c\ge1\); conversely, positive \(a,b,c\) make all three intervals nonempty. Since each vertex fires exactly once, the update equation guarantees return after three steps. Because the firing pattern is not constant in time, these states have least period three.

For a fixed ordered triple \((a,b,c)\), there are \(n!/(a!b!c!)\) choices of the labelled phase partition. The lower possible total chip count is
\[
a(n-1)+b(b+c-1)+c(c-1)=n(n-1)-(ab+bc+ca).
\]
The generating factor for independently choosing chip heights inside the intervals is \([c]_z^a[a]_z^b[b]_z^c\). Summing over positive ordered triples proves the formula for \(P_n(z)\).

For every initially primitive-three configuration, every vertex fires and waits at least once in the period. The displayed intervals show each chip count is between zero and \(2(n-1)-1=2n-3\). The transformation
\[
x_v\longmapsto 2n-3-x_v
\]
therefore gives a nonnegative state. It interchanges firing and waiting at each time, and the update equation shows that complementary configurations remain complementary at all subsequent times. It bijects the \(h=1\) and \(h=2\) period-three states, changing their total chip count \(E\) to \(n(2n-3)-E\). This proves the formula for \(H_n(z)\), as well as the coefficient symmetry. Since every primitive-three state has \(h\in\{1,2\}\), none is omitted.

For any fixed positive \((a,b,c)\), the product of the consecutive chip-height intervals has positive coefficients at every integer total between its minimum and maximum. The maximum is
\[
n(n-1)-(ab+bc+ca)+a(c-1)+b(a-1)+c(b-1)=n(n-2).
\]
Over all positive triples with sum \(n\), the minimum is obtained when \(ab+bc+ca\) is largest, namely \(\lfloor n^2/3\rfloor\), attained at the balanced triples. A balanced triple alone supplies every integer from \(L_n\) through \(n(n-2)\). The complement gives the reflected band, proving exact support, including the gap between \(n(n-2)\) and \(n(n-1)\).

At the maximum of the lower band, each ordered phase assignment contributes exactly one configuration (all its chips at their individual upper bounds). Thus the coefficient equals the number of surjections from the \(n\) labelled vertices onto the three nonempty ordered phases. Inclusion-exclusion gives \(3^n-3\cdot 2^n+3\). Complementation gives the same count at the minimum of the upper band. At \(L_n\), only balanced triples contribute and each contributes one configuration per phase assignment; their multinomial counts are precisely the stated \(B_n\). Finally, evaluate \(P_n(1)\): each ordered triple contributes \(n!c^aa^bb^c/(a!b!c!)\). Complements double this count and division by three gives orbit counts. This completes the proof.

## Verification

The standalone program `verify_exhaustive.py` independently enumerates every chip configuration in the exact confined boxes \(\{0,\ldots,2n-3\}^n\) for \(n=3,4,5,6\), applies three updates, and checks all least-period-three energy coefficients against the formula. The four box sizes are \(64,1296,32768,1000000\), respectively; all checks pass. The standalone program `verify_phase_enumeration.py` independently enumerates each of the \(3^n\) labelled firing-phase assignments for \(3\le n\le9\), derives each chip interval by inequality intersection, and compares its full polynomial with the stated multinomial polynomial; it also checks the support intervals and both endpoint identities. The programs and actual output files accompany this result. The all-\(n\) proof is the algebraic argument above; finite checks are supplementary only.

For example, the numbers of primitive-three configurations at \(n=3,4,5,6\) are \(12,144,1800,27360\), corresponding to \(4,48,600,9120\) orbits. The low-energy bands are \([3,3]\), \([7,8]\), \([12,15]\), and \([18,24]\), respectively.

## Relationship to prior work

Levine (arXiv:0811.2800, first public 17 November 2008) establishes rotation-number/activity behavior and short-period results for parallel chip-firing on complete graphs; its convention counts a loop at each vertex and fires at threshold \(n\). Adding one chip per vertex conjugates the current loopless threshold-\(n-1\) update to Levine's convention, so this change of convention does **not** establish novelty. The specific mass-refined primitive-three census, exact sharp two-band support, and endpoint multiplicities are not stated in the inspected article. Jiang (arXiv:1003.0943, first public 4 March 2010) establishes permissible period lengths on complete bipartite and multipartite graphs and general firing-count/complement lemmas, not this census. Jiang, Scully and Zhang (arXiv:1211.6786, first public 29 November 2012) classify permitted firing patterns, not chip-mass-resolved counts. Ji, Li and Wang (arXiv:2408.10508, first public 20 August 2024) exclude period three and four strictly within the middle-stair interval for general graphs, but do not give this exact count at the excluded endpoints. The current formula resolves the complete-graph endpoint populations and full mass support for primitive period three, rather than reasserting those known qualitative results.

## Limitations

This counts **initially periodic primitive-three** configurations and orbits on simple complete graphs only. It does not count transient configurations that eventually enter a three-cycle, or classify primitive periods other than three. Finite computational checks establish only the displayed finite orders, not the infinite theorem. Searches and full-text comparisons reduce but cannot exclude an unindexed earlier equivalent enumeration. Independent review or validation has not been performed.

## References

1. L. Levine, *Parallel chip-firing on the complete graph: Devil's staircase and Poincaré rotation number*, arXiv:0811.2800 (first public 2008-11-17), https://arxiv.org/abs/0811.2800.
2. T.-Y. Jiang, *On the period lengths of the parallel chip-firing game*, arXiv:1003.0943 (first public 2010-03-04), https://arxiv.org/abs/1003.0943.
3. T.-Y. Jiang, Z. Scully, and Y. X. Zhang, *Motors and impossible firing patterns in the parallel chip-firing game*, arXiv:1211.6786 (first public 2012-11-29), https://arxiv.org/abs/1211.6786.
4. D. Ji, M. Li, and D. Wang, *Non-stabilizing parallel chip-firing games*, arXiv:2408.10508 (first public 2024-08-20), https://arxiv.org/abs/2408.10508.
