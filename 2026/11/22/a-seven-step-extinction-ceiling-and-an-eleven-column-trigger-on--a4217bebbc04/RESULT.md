# A seven-step extinction ceiling and an eleven-column trigger on three-row excitable strips

## Finding

Let \(G_n=P_3\square P_n\) be the open three-row square-lattice strip, \(n\geq1\). In the synchronous three-state Greenberg–Hastings model with excitation threshold two, the maximum first time \(\tau\) at which every vertex is resting, maximized over all initial colorings, is exactly
\[
M(n)=\begin{cases}
3,&n=1,2,\\
4,&n=3,4,\\
5,&n=5,6,\\
6,&7\leq n\leq10,\\
7,&n\geq11.
\end{cases}
\]
In particular, \(F_n^7\) is the constant all-rest map for every \(n\), and the exponent seven is attained for the first time at eleven columns. Exactly \(1{,}265{,}544\) of the \(3^{33}\) initial colorings on \(G_{11}\) have \(\tau=7\). Under independent uniform initial colors on \(G_n\),
\[
\mathbb P(\tau=7)\ \geq\ 1-\left(1-\frac{1736}{3^{27}}\right)^{\lfloor n/11\rfloor},\qquad n\geq11.
\]
Consequently, the sharp seven-step delay becomes overwhelmingly likely as the strip length grows, even though no trajectory can oscillate forever.

## Assumptions and scope

Vertices are \((r,c)\) with \(r\in\{0,1,2\}\) and \(c\in\{0,\ldots,n-1\}\). An edge joins vertices of Manhattan distance one, with no wraparound and with each neighbor counted once. A configuration takes values in \(\{0,1,2\}^{3n}\): \(0\) resting, \(1\) excited, \(2\) refractory. At each simultaneous update, state \(1\) becomes \(2\), state \(2\) becomes \(0\), and state \(0\) becomes \(1\) exactly when at least two distinct neighbors were in state \(1\), otherwise staying \(0\). There is no external forcing. Define \(\tau(x)=\min\{t\geq0:F_n^t(x)=\mathbf0\}\). Once reached, \(\mathbf0\) is absorbing.

## Proof

**1. Boolean temporal reduction.** Let \(E_t(v)\) mean that vertex \(v\) is excited at time \(t\), and let \(R_0(v)\) mean that it is initially refractory. For \(t\geq1\), the only refractory vertices at time \(t\) are those excited at time \(t-1\). Thus for every vertex, with Boolean conjunctions and disjunctions,
\[
E_1(v)=\neg E_0(v)\wedge\neg R_0(v)\wedge
 \left[\sum_{u\sim v}E_0(u)\geq2\right],
\]
\[
E_{t+1}(v)=\neg E_t(v)\wedge\neg E_{t-1}(v)\wedge
 \left[\sum_{u\sim v}E_t(u)\geq2\right]\quad(t\geq1).
\]
The starting values \(E_0(v)\) and \(R_0(v)\) are mutually exclusive, yielding precisely three initial choices per vertex. If there are excited sites at the final time \(t\) at which excitation occurs, then their refractory successor persists at \(t+1\), and all states become zero at \(t+2\). Therefore \(\tau=t+2\), except that the initial all-zero configuration has \(\tau=0\); the maximum is determined by the latest possible excitation.

**2. Exact finite lemma.** For \(1\leq n\leq13\), let \(B_{n,t}\) denote the Boolean assertion that some vertex of \(G_n\) is excited at time \(t\), expressed as a function of all \(3n\) initial ternary variables. The standalone `verify_bdd.py` builds *reduced, ordered, three-branch decision diagrams* for these Boolean functions, using canonical unique-table reduction, Shannon expansion, and exact Boolean AND/OR/NOT. Its report establishes the following latest possible excited times:

| \(n\) | 1–2 | 3–4 | 5–6 | 7–10 | 11–13 |
|---|---:|---:|---:|---:|---:|
| Latest \(t\) with \(B_{n,t}\not\equiv0\) | 1 | 2 | 3 | 4 | 5 |

The diagram roots for \(B_{n,6}\) reduce to the zero terminal for *each* \(n=1,\ldots,13\). In the same computation, all asserted nonzero roots have explicit satisfying ternary assignments, which are replayed under the original update. This is an exhaustive finite calculation: at every branch all three initial colors are represented, shared nodes merely merge logically identical residual functions, and a zero root proves nonexistence. For \(n=11\), exact diagram path counting gives \(1{,}265{,}544\) assignments with \(B_{11,5}\) true. The program also compares all time-slice counts to direct brute force for \(n\leq3\). `verify_smt_optional.py` independently encodes the recurrence as finite Boolean constraints using the standard libz3 library and reproduces all thirteen sharp maximum times.

**3. Extension to all lengths.** Excitation at a vertex at time \(t\) depends only on initial states at graph distance at most \(t\), by induction on the local update. For a vertex in \(G_n\), if both horizontal endpoints lie at least six columns away, its time-six cone is identical to the cone of the middle column in \(G_{13}\). Otherwise, the cone matches one in some \(G_m\) with \(m\leq13\), where an artificial far endpoint at exactly distance six cannot influence the value at time six. Reflection handles the right endpoint. Therefore the finite zero-root checks imply \(E_6(v)=0\) for every vertex of *every* \(G_n\). There are no excited sites at time six and no new excitation at time seven; all refractory sites at six have relaxed by seven. This establishes the universal seven-step bound.

**4. Sharpness and probability.** For each \(n\leq10\), the positive diagram root at the listed final excited time gives the claimed lower bound. On eleven columns, the following initial coloring, written from left to right as three-digit column words, has an excited site at time five in the central column:

`001 010 100 000 111 000 121 000 100 010 001`.

Its successive total excited-site populations at times zero through six are \(11,12,7,4,2,1,0\); its first all-rest time is seven. For any \(n\geq11\), place this word in eleven consecutive columns and assign arbitrary states outside them. The central time-five cone cannot see outside those eleven columns, so the late excitation persists. The eleven-column diagram count above is exact and the event \(B_{11,5}\) concerns the center column only. In each disjoint eleven-column block, the probability of this local trigger is \(1{,}265{,}544/3^{33}=1736/3^{27}\). Independent blocks provide the stated lower bound and exponential convergence of the maximum-delay probability to one.

## Verification

Run `python3 verify_bdd.py` with Python 3, using no third-party packages. It checks all thirteen finite-length logical certificates, verifies the witness and sharp maxima, computes the exact eleven-column population, and cross-checks smaller instances by complete enumeration. For an independent Boolean-satisfiability implementation, `python3 verify_smt_optional.py` uses the ordinary libz3 shared library; that optional secondary check was also run successfully. The explicit Boolean recurrence and finite-cone lemma are part of the proof, not assumptions supplied by the solvers. The computations are for all initial ternary configurations of the bounded windows, not random samples.

## Relationship to prior work

The Greenberg–Hastings rule and its two-dimensional excitation/spiral behavior are classical. Durrett and Griffeath (1993) study asymptotic threshold-range effects on the plane, not this finite three-row extinction clock. Gravner, Lyu and Sivakoff (2018) treat three-color successor-contact dynamics with a single-neighbor trigger on arbitrary graphs, so their universal-cover results do not imply the two-contact, sharp finite-time theorem here. Published exact results for threshold-two wheels and open two-row ladders use different graphs and do not imply the three-row bound or its eleven-column onset. The present theorem is a finite-width causal nilpotency result; it asserts neither a corresponding bound for four-row strips nor for periodic boundary conditions.

## Limitations

The all-length statement depends on the independently checkable finite ternary decision-diagram identity for time six. No short purely hand-derived characterization of all late-excitation patterns is claimed. The probability inequality is an explicit lower bound, not an exact general-length population formula. Broader results for arbitrary finite-width strips, external forcing, other thresholds and larger state spaces remain unproved. The searched literature may omit a historical equivalent; a non-indexed priority risk remains. No independent external mathematical audit has been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, preprint submitted 22 March 1993, arXiv:patt-sol/9303002, https://arxiv.org/abs/patt-sol/9303002 ; *Experimental Mathematics* 2 (1993), 183–208, https://doi.org/10.1080/10586458.1993.10504277 .
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, preprint dated 24 October 2016, arXiv:1610.07320, https://arxiv.org/abs/1610.07320 .
3. J. M. Greenberg and S. P. Hastings, *Spatial patterns for discrete models of diffusion in excitable media*, *SIAM Journal on Applied Mathematics* 34 (1978), 515–523, https://doi.org/10.1137/0134040 .
