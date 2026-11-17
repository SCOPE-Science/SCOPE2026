# A resonance hole in sharp relaxation for complete-graph refractory automata

## Finding

Fix integers \(q\ge3\), \(r\ge1\), and \(n\ge1\). On the labelled loopless complete graph \(K_n\), use \(q\) local states: rest \(0\), firing \(1\), and ordered refractory stages \(2,\ldots,q-1\). At each synchronous update, a resting vertex fires if and only if **exactly** \(r\) other vertices are firing; a firing vertex advances to stage \(2\); each later refractory stage advances by one; stage \(q-1\) becomes rest. Let \(\tau(x)\) be the first time the trajectory of a labelled configuration is periodic.

Every recurrent configuration is either all rest or a primitive \(q\)-cycle in which every local state has exactly \(r\) vertices. Thus nontrivial recurrence is possible **if and only if** \(n=qr\), and then the number of primitive \(q\)-cycles is
\[
\frac{(qr)!}{q(r!)^q}.
\]

The sharp maximum first-entry time, including the exceptional periodic resonance, is
\[
\boxed{T_{q,r}(n)=\min\left(2q-2,\ q-1+\left\lfloor\frac{n-1}{r}\right\rfloor\right)-\mathbf1_{\{n=qr\}}.}
\]
The single missing top-relaxation layer at \(n=qr\) is a genuine resonance hole: for all \(n>(q-1)r\) other than \(qr\), some configurations require \(2q-2\) updates; at \(n=qr\) none do, and the maximum is exactly \(2q-3\).

Here is an exact exponential generating function for the *entire* first-entry census. Put
\[
E=e^z,\qquad h=\frac{z^r}{r!},
\]
let \(N_{n,t}\) count all labelled configurations with \(\tau=t\), and set \(\mathcal G_{q,r}(z,u)=\sum_{n\ge0}\sum_{t\ge0}N_{n,t}z^nu^t/n!\), with the empty vertex set counted as one all-rest state. Then
\[
\boxed{\begin{aligned}
\mathcal G_{q,r}(z,u)={}&E+h^q
+\sum_{s=2}^{q-1}u^{q-s}(E-1)E^{q-s}\\
&+u^{q-1}(E-1-h)E^{q-1}\\
&+\sum_{j=1}^{q-1}h^jE^{q-j-1}
 \bigl[u^{j+q-2}+u^{j+q-1}(E-1-h)\bigr].
\end{aligned}}
\]
For \(n\ge1\), \(N_{n,t}=n![z^nu^t]\mathcal G_{q,r}(z,u)\). At \(n=qr\), the coefficient of \(u^0\) contains the one all-rest fixed point plus the \((qr)!/(r!)^q\) initially primitive \(q\)-periodic configurations. All other states eventually become all rest.

When \(n>(q-1)r\) and \(n\ne qr\), the number of configurations attaining the sharp \(2q-2\) bound equals
\[
\frac{n!}{(r!)^{q-1}(n-(q-1)r)!}.
\]
At the resonance \(n=qr\), the exact population attaining the lowered maximum \(2q-3\) is
\[
\frac{(qr)!}{(r!)^{q-2}(2r)!}\left(2^{2r}-1-\binom{2r}{r}\right).
\]
For fixed \(q,r\), a uniformly random initial state has \(\tau=q-1\) with probability \(1-O_{q,r}(n^r((q-1)/q)^n)\) as \(n\to\infty\): typical decay is recovery-limited, while extremely long delays form explicitly countable rare layers.

## Assumptions and scope

Vertices are individually labelled. The graph has all edges between distinct vertices and no self-loops. All sites update synchronously, based solely on the previous row. Only firing vertices in state \(1\) count toward the **exactly** \(r\) condition. All refractory transitions are compulsory. The result concerns finite graphs and the specified exact-birth rule, not at-least-threshold Greenberg–Hastings dynamics, ordinary square-lattice Brian's Brain, stochastic contact processes, or asynchronous updates.

For nonempty \(K_n\), the all-rest configuration is fixed. By the original definition, \(\tau=0\) for a configuration already in a recurrent orbit, whether fixed or a primitive cycle. No spatial symmetry quotient is taken.

## Proof

**1. Occupancy map.** Write \(a_i\) for the number of vertices presently in local state \(i\), with \(\sum_{i=0}^{q-1}a_i=n\). Every resting vertex has precisely \(a_1\) firing neighbors, because the graph is complete and resting vertices are not themselves firing. Thus if \(a_1=r\), every rest vertex fires and the global update is the simultaneous cyclic permutation \(0\mapsto1\mapsto\cdots\mapsto q-1\mapsto0\) of all vertices. If \(a_1\ne r\), no new firing vertex appears in this update. Thereafter the firing population is zero, so no future birth occurs (since \(r\ge1\)); the remaining refractory stages empty into rest in at most \(q-1\) updates.

**2. The mismatch clock and all periodic points.** Define the cyclic inspection order of initial occupancies by
\[
\sigma=(1,0,q-1,q-2,\ldots,2).
\]
While births continue, the firing population at successive times is \(a_{\sigma_0},a_{\sigma_1},\ldots,a_{\sigma_{q-1}}\). If all these entries equal \(r\), each update rotates every local state, and the configuration has least period exactly \(q\), since each labelled vertex moves to a different local state at every earlier time. All entries then equal \(r\), forcing \(n=qr\). Otherwise let \(j\in\{0,\ldots,q-1\}\) be the first index with \(a_{\sigma_j}\ne r\). At time \(j\) the global rotation stops and compulsory decay begins. If \(j\ge1\), local state \(2\) has exactly \(r\) vertices (it holds the preceding firing class). Therefore the time to reach all rest is
\[
\tau=j+q-1\quad\text{if }a_{\sigma_j}>0,
\qquad
\tau=j+q-2\quad\text{if }a_{\sigma_j}=0.
\]
If \(j=0\) and \(a_1>0\), then \(\tau=q-1\). If \(j=0\) and \(a_1=0\), let \(s\) be the smallest occupied refractory class \(2\le s\le q-1\), if one exists. Then \(\tau=q-s\); if none exists, all vertices are already resting and \(\tau=0\). This is exhaustive and necessary-and-sufficient, with no assumption about the counts in the uninspected classes.

**3. Sharp upper bound.** For a mismatch at \(j\ge1\) with positive firing population, the preceding \(j\) classes each have \(r\) vertices, and the mismatched class has at least one; thus \(jr+1\le n\) and \(\tau\le q-1+\min(q-1,\lfloor(n-1)/r\rfloor)\). For a zero-population mismatch at \(j\ge1\), \(jr\le n\) and \(\tau=j+q-2\), which satisfies the same bound. The \(j=0\) cases do too. When \(n=qr\), the only way to pass \(q-1\) matching classes is to have the final class also equal \(r\), which is periodic rather than maximally transient; hence one must subtract a unit from the general bound.

For sharpness when \(n>(q-1)r\) and \(n\ne qr\), place \(r\) vertices in each of the first \(q-1\) classes of \(\sigma\), and put the remaining positive, non-\(r\) population in the final class. When \(n\le(q-1)r\), put \(j=\lfloor(n-1)/r\rfloor\) consecutive inspected populations equal to \(r\), and distribute the remainder to give a positive non-\(r\) mismatch when possible; when the remainder is exactly \(r\), one additional matched class and then a zero mismatch attain the same time. The case \(n<r\) is attained by \(a_1=n\), and \(n=r\) by \(a_1=r\) and all remaining vertices zero. At \(n=qr\), fix the first \(q-2\) inspected populations at \(r\), the next at \(2r\), and the last at zero: the resulting mismatch yields exactly \(2q-3\) updates. These constructions prove the formula for every positive \(n,q,r\).

**4. All labelled first-entry populations.** By the exponential formula, a color class with arbitrary occupancy contributes \(E=e^z\), an empty class contributes \(1\), a positive class contributes \(E-1\), a class with exactly \(r\) vertices contributes \(h=z^r/r!\), and a positive class different from \(r\) contributes \(E-1-h\). The all-rest state contributes \(E\), and the immediate primitive cycles contribute \(h^q\). If \(j=0\) with no initially firing vertices, choosing the earliest occupied refractory stage \(s\) contributes \((E-1)E^{q-s}\) at entry time \(q-s\). If \(j=0\) with a positive non-\(r\) firing class, the contribution is \((E-1-h)E^{q-1}\) at time \(q-1\). For each \(j\ge1\), the first \(j\) inspected classes contribute \(h^j\); the mismatch contributes either \(1\) or \(E-1-h\); the remaining \(q-j-1\) classes contribute \(E^{q-j-1}\). Attaching the proven entry-time exponents gives the displayed generating function. Every occupancy vector belongs to exactly one term, so no terms overlap.

**5. Extremizer counts and typical time.** At the full maximum \(2q-2\), the first \(q-1\) inspected classes must all have size \(r\) and the final class the unique positive non-\(r\) remainder, giving the multinomial count. When \(n=qr\), the maximal mismatch index is \(q-2\), with \(q-2\) classes of size \(r\), a positive next class of size \(c\ne r\), and the last class of size \(2r-c\); summing \(1\le c\le2r\), \(c\ne r\), gives \(2^{2r}-1-\binom{2r}r\). Finally, a uniform random labelled configuration has a binomial firing population \(\mathrm{Bin}(n,1/q)\). Except when that population equals zero or \(r\), the entry time is precisely \(q-1\). Both exceptional probabilities are \(O_{q,r}(n^r((q-1)/q)^n)\).

## Verification

The accompanying stand-alone integer-only programs are `check_census.py` and `check_direct.py`. Run with `python check_census.py` and `python check_direct.py` from a directory containing these files. The first compares the exponential generating function with direct multinomial enumeration of occupancy vectors for 340 parameter triples \(3\le q\le7\), \(1\le r\le4\), \(1\le n\le17\), checking conservation of the full \(q^n\) state population and the sharp maximum time. The second independently executes the labelled cellular automaton until recurrence for 1,834,800 initial states across 112 finite systems, checking both the exact first-entry time and primitive period.

For \(q=4\), \(r=2\), the maximal entry times at \(n=5,6,7,8,9,10\) are respectively \(5,5,6,5,6,6\): the isolated drop at the eight-vertex periodic resonance is observed directly. At \(n=8\), the number of immediately primitive four-periodic configurations is \(2520\), and exactly \(3780\) configurations attain the exceptional largest transient time five.

The finite checks verify calculations and implementations, not the theorem at infinitely many parameter values; the exhaustive combinatorial proof above supplies that step.

## Relationship to prior work

Brian Silverman's original three-state exactly-two firing rule is described in the 1996 *Exploring Emergence* material of Resnick and Silverman, and precisely in Evans's 2002 exposition. Those references concern the rule and its square-lattice behavior, not complete-graph transient distributions. The general Generations family allows successive refractory stages. The present result specifically treats an exact-count birth condition on loopless complete graphs.

A superficially related mathematical literature treats the Greenberg–Hastings *at-least-threshold* excitable system on complete bipartite, split, and multipartite graphs. That is not the same update: above the birth threshold, the present automaton **stops** producing newborn firing sites, which is the mechanism behind the isolated \(n=qr\) resonance hole. In contrast, the previously studied cyclic successor-contact complete-graph automata advance any occupied color when a successor threshold is met, with no unique resting class and no mandatory refractory pipeline. Thus their orbit and relaxation enumerators do not imply the stated theorem.

## Limitations

The full pre-2000 original *Exploring Emergence* page is not presently accessible; its dated bibliographic record supplies the historical model date but does not establish a priority-negative statement about every possible result. Evans's 2002 full page and contemporary full rule descriptions were inspected. Indexed research searches and relevant existing complete-graph, biclique, and cyclic-automaton result statements did not reveal the exact-count complete-graph result, but unpublished, unindexed, or inaccessible earlier work could overlap. The theorem does not concern stochastic excitation, general sparse graphs, inhomogeneous thresholds, or non-synchronous schedules.

## References

1. M. Resnick and B. Silverman, *Exploring Emergence: The Brain Rules*, MIT Media Laboratory, 1996-02-04. Bibliographic record and archived original link: https://www.playfulinvention.com/emergence/mutants.html (original currently inaccessible).
2. M. S. Evans, *Brian's Brain*, 2002-01-28. https://www.msevans.com/automata/briansbrain.html (full exposition inspected).
3. *Brian's Brain — Cellular Automata Lab*, complete model and Generations definition. https://openworldlab.org/fun/cellular-automata/brians-brain (full text inspected).
4. *OCA: Brian's Brain*, LifeWiki model account. https://conwaylife.com/wiki/OCA:Brian%27s_Brain (full access restricted).
