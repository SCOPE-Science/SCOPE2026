# The terminal-excitation motif law for Greenberg–Hastings dynamics on fan graphs

## Finding
For each integer \(n\ge1\), let \(G_n=K_1\vee P_n\) be the fan graph with one hub and a path of \(n\) labelled rim vertices. Under synchronous three-state Greenberg–Hastings dynamics with activation threshold two, every state first reaches complete rest by update five. Define \(N_5(n)\) to be the number of labelled initial configurations whose *first* all-rest update is exactly five, with \(N_5(0)=0\) as a generating-function convention. Then
\[
\boxed{\sum_{n\ge0}N_5(n)z^n=\frac{4z^9(1-2z)}{(1-3z)(1-3z+2z^4-4z^5)^2}.}
\]
In particular, \(N_5(n)=0\) for \(1\le n\le8\), whereas \(N_5(n)>0\) for every \(n\ge9\). Thus the sharp worst-case extinction clock equals five for all \(n\ge9\). The initial values \(N_5(9),\ldots,N_5(15)\) are \(4,28,144,648,2684,10564,40088\). Under uniform independent initial colours, the probability of first reaching rest at update five converges to \(1/3\):
\[
\lim_{n\to\infty}\frac{N_5(n)}{3^{n+1}}=\frac13.
\]
The exact criterion is that the hub is initially excited and the initial path word contains *at least two*, possibly overlapping, occurrences of either motif `10001` or `10201`. Motifs may overlap only in their common endpoint `1`.

## Assumptions and scope
The hub is \(h\), and the ordered rim vertices \(v_1,\ldots,v_n\) have the path edges \(v_iv_{i+1}\) and hub spokes \(hv_i\). There are no loops or cyclic wrap-around rim edges. Each state belongs to \(\{0,1,2\}\), denoting resting, excited, and refractory. At each synchronous update, state \(1\) changes to \(2\), state \(2\) changes to \(0\), and state \(0\) changes to \(1\) precisely when at least two *distinct graph neighbours* are in state \(1\); otherwise it remains \(0\). No external excitation is supplied. If \(s\) is an initial configuration, its extinction time is \(\tau(s)=\min\{t\ge0:F_n^t(s)=\mathbf 0\}\). All counting is of labelled colourings of the specified fan, without identifying rotations, reflections, or colour permutations.

## Proof
**Step 1: local rim-exclusion lemma.** Write \(H_t\) for the hub colour at time \(t\) and \(R_t\) for the set of rim sites excited at time \(t\). If \(H_{t-1}\ne1\) and \(t\ge1\), then \(R_{t+1}=\varnothing\). To see this, a rim site excited at time \(t\) must have had both of its path neighbours excited at time \(t-1\), because the hub supplied no excited neighbour. Therefore all its path neighbours are refractory, not resting, at time \(t\). A site that is resting at time \(t\) consequently has *no* excited path neighbour at that time; it cannot receive two excited neighbours even if the hub is excited. This proves the lemma for interior vertices and, a fortiori, endpoints.

**Step 2: the five-update bound.** If \(H_0\ne1\), the lemma yields \(R_2=\varnothing\); hence \(R_3=\varnothing\), since a rim site at time two has no excited path neighbour, and no newly excited site can be created solely by the hub. The rim has fully recovered by update four. The hub cannot be excited after update two and has recovered by update four as well. Thus \(\tau\le4\) in this case. If \(H_0=1\), then \(H_1=2\) and \(H_2=0\). Applying the lemma at times two and three gives \(R_3=R_4=\varnothing\). The hub can fire at update three, but not again at update four or later; it has recovered by update five. All rim states are resting by update four. Hence \(F_n^5(s)=\mathbf0\) for every initial state \(s\).

**Step 3: exact criterion for a fifth update.** Suppose \(H_0=1\). At time one, a rim site is excited exactly when it was initially resting and had at least one initially excited path neighbour. At time two the hub is refractory, so a rim site can be excited precisely when it is resting at time one and *both* its path neighbours are excited at time one. These conditions are equivalent to the five consecutive initial rim colours, centred on that site, being `10001` or `10201`: both adjacent sites are initially resting, both sites at distance two are initially excited, and the centre is initially resting or refractory. This equivalence holds also at the boundary because a rim endpoint has only one path neighbour and cannot be excited at time two. Thus the number of excited rim sites at update two is exactly the number of occurrences of these motifs in the initial rim word. Since \(H_2=0\), the hub fires at time three if and only if at least two such occurrences exist. There are then excited hub, refractory hub and resting hub states at times three, four and five respectively; no rim excitation survives past time two. Conversely, without that time-three firing, all vertices are resting by update four. This proves the asserted if-and-only-if condition for \(\tau=5\).

**Step 4: the rational counting function.** Let \(c(w)\) be the number of occurrences of the two motifs in a ternary word \(w\), and put
\[
P(z,u)=\sum_{n\ge0}\sum_{w\in\{0,1,2\}^{n}}z^nu^{c(w)}.
\]
Expand \(u^{c(w)}=(1+(u-1))^{c(w)}\) by marking any subset of the motif occurrences. Two distinct marked occurrences can overlap only in the terminal/initial symbol `1`; the corresponding starting positions differ by exactly four. Each connected cluster of \(k\ge1\) overlapping marked occurrences has length \(4k+1\), has \(2^k\) possibilities for the central symbols, and has weight \((u-1)^k\). Its generating series is therefore
\[
C(z,u)=\frac{2(u-1)z^5}{1-2(u-1)z^4}.
\]
A marked word decomposes uniquely into isolated unmarked letters (total weight \(3z\)) and these clusters, so
\[
P(z,u)=\frac1{1-3z-C(z,u)}=\frac{1-2(u-1)z^4}{1-3z-2(u-1)z^4+4(u-1)z^5}.
\]
Write \(Q(z)=1-3z+2z^4-4z^5\). Words with at least two occurrences have generating series
\[
\begin{aligned}
\sum_{n\ge0}N_5(n)z^n&=P(z,1)-P(z,0)-\left.\partial_uP(z,u)\right|_{u=0}\\
&=\frac1{1-3z}-\frac{1+2z^4}{Q(z)}-\frac{2z^5}{Q(z)^2}\\
&=\frac{4z^9(1-2z)}{(1-3z)Q(z)^2}.
\end{aligned}
\]
There cannot be two occurrences unless the rim has at least nine vertices, because their starting positions differ by at least four; for every \(n\ge9\), the initial rim prefix `100010001` followed by resting sites supplies two occurrences. This proves the sharp onset.

**Step 5: limiting fifth-round probability.** Conditional on initial hub colour one, split the rim into \(\lfloor n/5\rfloor\) disjoint blocks of five. Each block independently equals one of the two motifs with probability \(2/3^5\). The probability that fewer than two such blocks occur tends to zero by the elementary binomial distribution. Thus the conditional probability of at least two motifs in the full rim tends to one. Since initial hub colour one has probability \(1/3\), the unconditional fifth-round extinction probability tends to \(1/3\), as claimed.

## Verification
The accompanying standalone Python 3 program `verify_fan.py` implements the dynamical update independently from the motif test. It exhaustively enumerates every initial colouring for \(1\le n\le10\) (\(265716\) configurations in total), checking extinction by time five and the exact motif criterion state by state. It separately checks \(13122\) seven-site local windows with all allowable hub histories, and matches a finite-state suffix automaton for motif counting against the rational-generating-function recurrence for \(0\le n\le65\). Run `python3 verify_fan.py`; its recorded output is `verify_fan_output.txt`. Exhaustion at finite lengths serves as a check, not a substitute for the all-size argument above.

## Relationship to prior work
Fisch, Gravner and Griffeath (1991), and Durrett and Griffeath (1993), develop the Greenberg–Hastings excitation framework mainly for lattice settings. The published *Sharp five-step extinction for threshold-two excitation on wheel graphs* (2026) proves the five-step bound for cyclic-rim fans (wheels), including a smaller sharp onset at rim size eight, but does **not** give an all-size exact terminal-shell generating function for open-rim fans. Its elementary rim-exclusion lemma also works in the open-rim setting and is not claimed as new. The contribution here is the motif characterization, the rational fifth-round shell census, its sharp onset at rim size nine, and the limiting one-third terminal probability. The Goulden–Jackson method is a known word-enumeration technique; its use here does not constitute a claim of a new enumerative method. Other work on excitable complete bipartite graphs, sunlets, and prisms uses different graph geometries and does not imply this precise fan motif law.

## Limitations
The result is specific to synchronous, deterministic, three-state, threshold-two excitation on the labelled open fan \(K_1\vee P_n\). It does not assert an exact census of the first-rest times zero through four, nor a corresponding formula for wheels, other thresholds, or larger refractory alphabets. The novelty comparison was limited to available primary literature, one directly relevant published full result, and indexed searches; an unindexed earlier equivalent remains possible. No independent mathematical audit is asserted.

## References
- R. Fisch, J. Gravner, D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing **1** (1991), 23–39. Full text: https://www.stat.cmu.edu/~cshalizi/462/readings/fgg.pdf.
- R. Durrett, D. Griffeath, *Asymptotic behavior of excitable cellular automata*, arXiv:patt-sol/9303002, first submitted 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
- *Sharp five-step extinction for threshold-two excitation on wheel graphs*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-five-step-extinction-for-threshold-two-excitation-on-wheel--58917bc0decb.
- J. Noonan, D. Zeilberger, *The Goulden–Jackson cluster method: extensions, applications and implementations*, Journal of Difference Equations and Applications **5** (1999), 355–377. https://doi.org/10.1080/10236199908808197.
