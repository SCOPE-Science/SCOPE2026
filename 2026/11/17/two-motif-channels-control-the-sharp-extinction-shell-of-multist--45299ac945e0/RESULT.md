# Two motif channels control the sharp extinction shell of multistate excitable wheels

## Finding
For integers \(q\ge4\) and \(n\ge3\), consider the synchronous threshold-two Greenberg–Hastings map \(F_{q,n}\) on the wheel \(W_n=K_1\vee C_n\), whose hub is adjacent to all \(n\) cyclic rim vertices. Every initial state reaches the all-rest configuration. Its largest first hitting time \(\tau\) is \(q\) when \(n=3\) and \(q+1\) when \(n\ge4\). In fact, **no vertex is excited at time three or later**, so the bound holds for every rim length and every number of states \(q\ge4\).

For \(n\ge4\), write the initial rim word as \(a=(a_i)_{i\in\mathbb Z/n\mathbb Z}\), and let \(P(a)\) count centers \(i\) with
\[
(a_{i-2},a_{i-1},a_i,a_{i+1},a_{i+2})=(1,0,c,0,1),\qquad c\in\{0,q-1\},
\]
while \(Q(a)\) counts centers \(i\) with \((a_{i-1},a_i,a_{i+1})=(1,0,1)\). Occurrences count distinct centers; the indices are cyclic, including when \(n=4\). A configuration hits all-rest **for the first time at \(q+1\)** if and only if exactly one of these two mutually exclusive cases holds:

- The hub initially has color \(1\) and \(P(a)\ge1\).
- The hub initially has color \(q-1\) and \(Q(a)\ge2\).

Hence the precise labelled maximal-extinction population is \(E_q(n)=A_q(n)+B_q(n)\), where \(A_q(n)=\#\{a:P(a)\ge1\}\) and \(B_q(n)=\#\{a:Q(a)\ge2\}\). These are finite-word counts, not approximate state-space samples. For each fixed \(q\ge4\), uniformly random initial configurations satisfy
\[
\lim_{n\to\infty}\Pr(\tau=q+1)=\frac2q.
\]
In particular, the proportion of maximal-duration states has a strictly positive limit despite the growing rim.

For direct exact evaluation at arbitrary \(n\), let \(\mathcal A=\{0,1,r,*\}\), where \(r\) denotes \(q-1\) and \(*\) represents the other \(q-3\) original colors; give these symbols weights \(w(0)=w(1)=w(r)=1\), \(w(*)=q-3\). Index two \(256\)-by-\(256\) matrices by four-letter words in \(\mathcal A^4\). Their only nonzero transitions are
\[
(a,b,c,d)\longrightarrow(b,c,d,e),\quad e\in\mathcal A,
\]
with weights \(w(e)z^{p(a,b,c,d,e)}\) in \(T_P(z)\), and \(w(e)z^{s(c,d,e)}\) in \(T_Q(z)\), where \(p\) is the indicator of \((a,b,c,d,e)=(1,0,c,0,1)\) with \(c\in\{0,r\}\), and \(s\) indicates \((c,d,e)=(1,0,1)\). Then, for all \(n\ge4\),
\[
E_q(n)=2q^n-\operatorname{tr}(T_P(0)^n)
-\bigl([z^0]+[z^1]\bigr)\operatorname{tr}(T_Q(z)^n).
\]
The coefficient operators apply to the polynomial trace. The trace counts cyclically consistent labelled rim words; the formula is finite and explicit for every \(q,n\).

## Assumptions and scope
The rim is the simple cycle on \(n\ge3\) distinct vertices. All \(q^{n+1}\) initial configurations are labelled, with each vertex taking a color in \(\{0,1,\ldots,q-1\}\). A nonzero state increments by one modulo \(q\) at every update; a resting (zero) vertex changes to color one precisely when at least two **distinct graph neighbours** are currently excited (color one), and otherwise stays zero. Updates are simultaneous. There are no external stimuli, random inputs, self-loops, or repeated edges. The all-rest first hitting time \(\tau(a)\) is the least nonnegative integer \(t\) for which \(F_{q,n}^t(a)\) is all zero.

## Proof
**First update.** Denote the hub's initial color by \(h\). If \(h\ne1\), a rim vertex becomes newly excited at time one exactly for an initial triple \((1,0,1)\) centered there: since the hub is not excited, both cyclic rim neighbors must be excited. Such a vertex's two supporting neighbors are refractory at time one, and consequently no rim vertex is newly excited at time two unless the hub at time one was excited. But if the hub was newly excited at time one (possible only when \(h=0\)), each excited rim vertex at time one arose from two rim neighbors initially excited. For a rim vertex to be resting at time one and next to any such newly excited rim vertex, it would have had to be initially excited, which instead makes it refractory at time one. Therefore no rim vertex is excited at time two in the \(h=0\) case either. The same obstruction holds when \(h\ne0,1\) and the hub is not excited at time one.

**The hub channel.** If \(h=q-1\), the hub is resting at time one and becomes excited at time two precisely when at least two rim sites excited at time one. The latter are exactly the distinct occurrences counted by \(Q(a)\). All rim sites are unexcited at time two in this case, by the preceding obstruction. If \(h=0\), either the hub becomes excited at time one and is refractory at time two, or the rim initially has at most one excited vertex, in which case no rim site can become newly excited at time one and hence the hub is not newly excited at time two. If \(h\in\{1,2,\ldots,q-2\}\), the hub is refractory at time two. Thus time-two hub excitation occurs exactly in the stated \(h=q-1\), \(Q(a)\ge2\) channel.

**The rim channel.** Suppose \(h=1\). The hub is in state two at time one, and each rim vertex excited at time one was initially resting and had at least one initially excited rim neighbor (the hub provided the other contact). A rim vertex at time two can be excited only if both its cyclic rim neighbors were excited at time one. Its own color at time one must be zero, forcing its initial color to be zero or \(q-1\). Each of its two neighbors can therefore have been excited at time one only if the corresponding outer rim vertex was initially excited. This is exactly the five-site motif \(P\), with a central color \(0\) or \(q-1\). Conversely this motif indeed excites its center at time two. No other initial hub color allows time-two rim excitation, by the preceding obstruction. This proves the complete two-channel criterion.

**No third-generation excitation.** If the hub is excited at time two, there are no excited rim sites at that time, and at time three the hub is refractory, while no rim site has two excited neighbors. If rim sites are excited at time two, the hub initially had color one and hence has color three at time two (valid because \(q\ge4\)); it is not excited. Moreover, two rim sites distance two apart cannot both carry the five-site motif: the center of either would have to be initial color one as the other motif's outer support, contradicting its required color zero or \(q-1\). Thus no rim site has two excited rim neighbors at time two. The hub cannot become newly excited at time three because it is still refractory. There are no excited vertices at time three; by induction none occur afterward.

**Sharp hitting times.** Every initial excited vertex disappears into rest after \(q-1\) updates; excitations born at time one or two disappear respectively by times \(q\) and \(q+1\). All initial refractory states disappear no later than \(q-2\) updates. Thus every state rests by \(q+1\), with equality precisely for the time-two motifs. For \(n\ge5\), the initial hub color one and cyclic rim word starting \((1,0,0,0,1)\) (all other sites zero) furnish such a motif; for \(n=4\), the hub color one and rim word \((1,0,0,0)\) work with cyclic wrap. For \(n=3\) neither time-two motif can occur; a hub color one with rim word \((1,0,0)\) gives a time-one excitation and sharp time \(q\).

**Exact populations and limit.** A closed \(n\)-step walk in the four-letter de Bruijn transition graph is in one-to-one correspondence with a labelled cyclic rim word of length \(n\), and the edge weight multiplies the per-symbol multiplicities. Hence the traces of the two matrices are occurrence-generating polynomials for \(P\) and \(Q\). Subtracting words with zero \(P\) occurrences and words with at most one \(Q\) occurrence gives the displayed exact formula. To prove the limit, partition the rim into disjoint blocks of length five and look for the specific \(P\)-word \((1,0,0,0,1)\). Under product measure each block matches with fixed probability \(q^{-5}\), so \(\Pr(P=0)\to0\). In disjoint length-three blocks, the word \((1,0,1)\) has probability \(q^{-3}\), so the probability of fewer than two matches also tends to zero. The two hub colors each occur with probability \(1/q\); the limiting terminal probability is therefore \(2/q\).

## Verification
The standalone C++ program `verify_exhaustive.cpp` independently iterates the microscopic \(q\)-state update for every labelled initial state on the parameter pairs listed in `exhaustive_output.txt` (including over 1.9 million states at \(q=5,n=8\)). It compares the exact final hitting time, absence of time-three excitation, and the two predicted motif channels state-by-state. All tested cases passed. The separately constructed standard-library Python program `verify_transfer.py` computes the transfer-matrix counts directly and agrees with the exhaustive channel counts for all overlapping parameter pairs; `transfer_output.txt` records the comparison values. The all-parameter proof above is symbolic and does not infer an infinite assertion from a finite experiment.

For example the terminal counts for \(n=4,5,6,7,8\) at \(q=4\) are respectively \(10,15,71,350,1638\); for \(q=5\), they are \(10,15,89,546,3194\). The full exact formula applies at sizes much larger than the exhaustive range.

## Relationship to prior work
The 1991 threshold-range article of Fisch, Gravner and Griffeath defines the multi-state Greenberg–Hastings family and analyzes threshold and spatial-range effects on two-dimensional lattices, rather than labelled terminal-extinction shells on wheels. Gravner, Lyu and Sivakoff (2016) develop arbitrary-graph theory for the three-color, threshold-one setting; the specific model here has at least four colors and threshold two. A previously published same-wheel theorem establishes sharp extinction for the **three-state** threshold-two rule, including a five-step cutoff that becomes sharp only on rims of length at least eight. Its proof explicitly does not cover additional refractory colors or the all-size terminal-shell population. The new result differs in its \(q\)-uniform time-two motif characterization, sharp \(q+1\) clock for every rim length at least four, exact all-size motif-count formula, and limiting probability \(2/q\). No broader inspected result was found to imply these claims.

## Limitations
The claim is restricted to the deterministic, two-contact, synchronous rule on a single-hub wheel with \(q\ge4\). It does not assert the same bound or terminal population for arbitrary graph families, different thresholds, or \(q=3\). The source comparison cannot exclude all unindexed or inaccessible earlier work, and mathematical review outside the present proof and computational checks has not been performed.

## References
1. R. Fisch, J. Gravner and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39. Full text: https://www.stat.cmu.edu/~cshalizi/462/readings/fgg.pdf.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, publicly submitted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (2016), https://arxiv.org/abs/1610.07320.
4. *Sharp five-step extinction for threshold-two excitation on wheel graphs*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-five-step-extinction-for-threshold-two-excitation-on-wheel--58917bc0decb.
