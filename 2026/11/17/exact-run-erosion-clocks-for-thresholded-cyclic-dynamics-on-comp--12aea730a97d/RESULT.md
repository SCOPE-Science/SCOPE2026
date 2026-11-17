# Exact run-erosion clocks for thresholded cyclic dynamics on complete graphs

## Finding

**Theorem (all colors, all integer contact thresholds).** Fix integers \(q\ge3\), \(\theta\ge1\), and \(n\ge2\). Let \(F\) be the synchronous cyclic successor-contact update on the loopless labelled complete graph \(K_n\): a vertex of color \(c\in\mathbb Z/q\mathbb Z\) advances to \(c+1\) exactly when at least \(\theta\) other vertices have color \(c+1\). For an initial configuration \(x\), let \(m_i\) be its number of vertices of color \(i\), and put \(A=\{i:m_i\ge\theta\}\).

If \(A\) is the complete color circle, \(x\) is already on a primitive temporal \(q\)-cycle. Otherwise, every orbit freezes. Decompose the proper active set \(A\) into maximal nonempty directed consecutive color runs \(R\). If the run \(R\) has length \(\ell(R)\) and its immediately preceding inactive color is \(j(R)\), the **exact first periodic-entry time** is
\[
\boxed{\tau(x)=\max_{R}\bigl(\ell(R)-1+\mathbf1_{m_{j(R)}>0}\bigr),}
\]
where the maximum over no runs is zero. Thus every eventual primitive period is \(1\) or \(q\); there are no delayed nontrivial cycles. The sharp largest first-entry time among all \(n\)-vertex configurations is
\[
\boxed{T_{q,\theta}(n)=\begin{cases}
\min(q-2,n-1),&\theta=1,\\
\min\bigl(q-1,\lfloor(n-1)/\theta\rfloor\bigr),&\theta\ge2.
\end{cases}}
\]
In particular, threshold two or higher creates a new possible relaxation layer at \(q-1\), in contrast to the \(q-2\) maximum at threshold one.

**Complete labelled-state census.** Define the formal exponential series
\[
Z(z)=1,\quad L_\theta(z)=\sum_{j=1}^{\theta-1}\frac{z^j}{j!},\quad H_\theta(z)=e^z-\sum_{j=0}^{\theta-1}\frac{z^j}{j!}.
\]
For each cyclic word \(s\in\{0,S,A\}^q\), use product weight \(W_s(z)=\prod_i w_{s_i}(z)\) with \(w_0=Z\), \(w_S=L_\theta\), and \(w_A=H_\theta\). For \(s\ne A^q\), define \(d(s)\) by the displayed run formula, treating \(A\) as active and a preceding \(S\) (but not \(0\)) as a positive deficient population. Then the number \(N_n(t,p)\) of labelled initial configurations with first-entry time \(t\) and eventual least period \(p\) is exactly
\[
\begin{aligned}
N_n(t,1)&=n![z^n]\sum_{\substack{s\in\{0,S,A\}^q\\s\ne A^q,\ d(s)=t}}W_s(z),\\
N_n(0,q)&=n![z^n]H_\theta(z)^q,
\end{aligned}
\]
with all other \(N_n(t,p)=0\). In particular, there are \(N_n(0,q)/q\) primitive \(q\)-orbits, and these exist precisely when \(n\ge q\theta\).

For \(\theta\ge2\), the exact number attaining the full \(q-1\) update delay is
\[
\boxed{N_n(q-1,1)=q\,n![z^n]L_\theta(z)H_\theta(z)^{q-1}.}
\]
For fixed \(q\ge3\) and \(\theta\ge2\), with independent uniform initial vertex colors and \(n\to\infty\),
\[
\boxed{\Pr(\tau=q-1\mid\text{initial state not period-}q)=1-O_{q,\theta}(n^{1-\theta}).}
\]

## Assumptions and scope

The graph is finite, simple, loopless and complete, with labelled vertices. All colors update simultaneously, and each vertex counts distinct neighbors (not itself). The threshold \(\theta\) may exceed vertex degree, in which case no color is active. Colors form a cyclic, directed palette \(\mathbb Z/q\mathbb Z\). First-entry time \(\tau\) is the least number of full synchronous updates before an actual periodic configuration is first reached; period means vertex-level temporal period, not period of the histogram of populations. Combinatorial exponential generating functions count labelled vertex assignments, so no quotient by color rotations is taken.

## Proof

Write \(m_i(t)\) for the color populations and \(a_i(t)=\mathbf1_{m_i(t)\ge\theta}\). All vertices currently in color \(i\) move together if and only if \(a_{i+1}(t)=1\). Hence the exact simultaneous population recurrence is
\[
m_i(t+1)=m_i(t)(1-a_{i+1}(t))+m_{i-1}(t)a_i(t).\tag{1}
\]
If \(a_i(t)=0\), (1) is at most \(m_i(t)<\theta\). Consequently, a color never becomes active after it is inactive: \(A(t+1)\subseteq A(t)\). If every color is active initially, all vertices advance at every step, preserving activity and shifting the histogram by one; each labelled vertex changes color at every step, so the least period is exactly \(q\).

Suppose the initial active set is proper. In a nonempty maximal active run \(i,i+1,\ldots,i+\ell-1\), its predecessor \(j=i-1\) and successor \(i+\ell\) are inactive. Formula (1) shows that an active color with an active successor retains activity at the next step exactly when its predecessor is active: its new population is the predecessor's old population. The rightmost active color, whose successor is inactive, keeps its own population and possibly receives additional population, so it remains active. Therefore in each update the leftmost member of every run of length at least two becomes inactive, all other members stay active, and singleton runs remain active. Inactive colors never reactivate. After exactly \(\ell-1\) steps, this run has only its rightmost active color.

The same recurrence proves a stronger packet statement: the old population \(m_j\) of the inactive color immediately preceding the run passes through the vacated left boundary one color per update, while the other vacated positions are zero after that packet leaves. At time \(\ell-1\), the only possibly nonzero site immediately preceding the surviving rightmost active color is the packet of size \(m_j<\theta\). If it is zero, that run's entire sector has stopped by then. If it is positive, it makes exactly one further move into the surviving active color, and this is the final move in that sector. Distinct runs cannot interact, because their intervening inactive colors cannot acquire new vertices, by (1). Thus the run contributes exactly \(\ell-1+\mathbf1_{m_j>0}\) steps, and the global first-entry time is the maximum of these contributions. Every proper-active orbit therefore freezes and has eventual period one.

For \(\theta=1\), every inactive color is empty, so a proper active run has clock \(\ell-1\), with \(\ell\le\min(q-1,n)\). The upper bound \(\min(q-2,n-1)\) is realized by a single run with that maximal length. For \(\theta\ge2\), a run of length \(\ell\) with positive preceding inactive packet needs at least \(\ell\theta+1\) vertices, while a zero-packet run needs at least \(\ell\theta\) and takes one fewer update. This yields \(T_{q,\theta}(n)\le\min(q-1,\lfloor(n-1)/\theta\rfloor)\). Equality is attained by putting one vertex into the inactive predecessor and at least \(\theta\) vertices into each of \(\ell=\min(q-1,\lfloor(n-1)/\theta\rfloor)\) consecutive colors, placing any leftover vertices into one of those active colors. If \(\ell=0\), all states are fixed.

The three categories zero, positive but below threshold, and active have respective labelled exponential weights \(1,L_\theta,H_\theta\). Their products count all occupancy compositions with the corresponding exact threshold signature; the clock was proved to depend only on that signature. Coefficient extraction therefore gives every \(N_n(t,p)\). For the maximum \(q-1\) delay, necessarily one color is positive but below threshold and the other \(q-1\) colors are active; conversely every such configuration has that delay. Choosing the deficient color gives the coefficient \(q n![z^n]L_\theta H_\theta^{q-1}\).

For the asymptotic assertion, failure of immediate \(q\)-periodicity means that at least one of the \(q\) occupancy counts is at most \(\theta-1\). Inclusion-exclusion, with fixed \(q\) and \(\theta\), gives
\[
\Pr(\text{not period-}q)=\frac{q\binom n{\theta-1}(q-1)^{n-\theta+1}}{q^n}\left(1+O_{q,\theta}(1/n)\right).
\]
The sole-deficiency cases with a positive deficient occupancy are exactly the maximum-delay configurations. Among the other nonperiodic states, the zero-deficiency cases contribute at most \(q(q-1)^n\), and the states with at least two deficient colors contribute at most \(O_{q,\theta}(n^{2\theta-2}(q-2)^n)\). Dividing by the preceding leading term gives an error \(O_{q,\theta}(n^{1-\theta})\). This completes the proof.

## Verification

The standalone `verify_states.py` directly simulates labelled vertex states and detects first repetition, independently of the population recursion. It checks all \(1{,}376{,}046\) configurations for \(3\le q\le6\), \(1\le\theta\le3\), and \(2\le n\le7\), including exact least periods and sharp maximum delays. The separate `verify_counts.py` performs two independent all-parameter finite censuses, one over occupancy compositions and another using labelled binomial convolution on the three-category signatures, for \(3\le q\le7\), \(1\le\theta\le4\), and \(2\le n\le14\). It checks 260 parameter triples and their total \(3{,}573{,}166{,}925{,}868\) weighted initial configurations. Reproduction: `python3 verify_states.py` and `python3 verify_counts.py`, with Python standard library only. Finite checks corroborate the general proof; they do not establish the infinite-parameter conclusion by exhaustion.

## Relationship to prior work

Fisch, Gravner, and Griffeath [1] introduced the general cyclic contact-threshold dynamics and primarily analyze spatially extended planar media, wave fronts, and threshold/range scaling, rather than complete-graph exact entrance clocks. The previously published three-color complete-graph exact census [2] covers arbitrary threshold but restricts to three colors. Separate four-color threshold-two and arbitrary-color threshold-one classifications are natural comparators with strictly narrower parameter coverage. Their individual claims do not establish the present simultaneous arbitrary-color/arbitrary-threshold run-erosion law, the associated finite-signature clock formula, or its sharp high-threshold asymptotic statement. The theorem is for complete graphs, not an assertion about a general finite graph or a planar lattice.

## Limitations

The use of loopless complete adjacency and fully synchronous updates is essential. The theorem does not assert the same transient behavior under asynchronous scans, on multipartite graphs, or under other local thresholds. The asymptotic law fixes both palette size and threshold before increasing vertex count. Historical priority is assessed from accessible comparisons; not all relevant archival papers can be ruled out. No external independent mathematical audit has been conducted.

## References

[1] R. Fisch, J. Gravner, and D. Griffeath, *Threshold-range scaling of excitable cellular automata*, Statistics and Computing 1 (1991), 23–39; freely accessible manuscript https://www.math.ucdavis.edu/~gravner/papers/fgg.pdf ; dated public arXiv record https://arxiv.org/abs/patt-sol/9304001 (1993-04-02).

[2] *Complete-graph cyclic dominance: exact orbit census and an arithmetic critical window*, published-finding corpus research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-graph-cyclic-dominance-exact-orbit-census-and-an-arithm--01f472caead4 .
