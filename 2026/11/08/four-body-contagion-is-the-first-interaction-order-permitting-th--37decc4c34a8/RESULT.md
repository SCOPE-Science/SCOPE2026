# Four-body contagion is the first interaction order permitting three finite SIS stationary modes

## Finding

Consider a completely mixed population of \(N\) individuals with spontaneous infection and simultaneous availability of interaction groups of sizes two through \(d+1\). Write \(I\in\{0,\ldots,N\}\) for the number infected. If \(0<\varepsilon<\mu/N\), \(\mu>0\), and all group-contagion coefficients are nonnegative, the unique stationary law of \(I\) has at most

\[
1+\left\lfloor\frac{d+1}{2}\right\rfloor
\]

**strict local modes**, where \(1\le d\le N-1\). In particular, pairwise and three-person contagion together have at most two strict stationary modes, whereas adding four-person contagion permits three, but never more than three. **For every \(N\ge4\), positive rates for pairwise, three-person, and four-person contagion can produce exactly three strict modes, at infected counts \(0,2,N\).** Four is the minimum population size in which this can happen.

A small exact instance with \(N=4\), recovery rate \(\mu=1\), importation rate \(\varepsilon=1/8\), and per-group transmission rates \(c_1=5/8\), \(c_2=1/16\), \(c_3=3\) has stationary infection-count probabilities

\[
(\pi_0,\pi_1,\pi_2,\pi_3,\pi_4)
=\frac1{27039}(8192,4096,4608,4416,5727).
\]

The three strict peaks are \(0,2,4\). This is a finite stationary-distribution result, not a claim about the number of stable mean-field equilibria.

## Assumptions and scope

Let \(N\ge2\) be an integer, \(1\le d\le N-1\), and \(\mu>0\). Every infected individual recovers independently at rate \(\mu\). Every susceptible individual becomes infected spontaneously at rate \(\varepsilon>0\); independently, each set of \(j\) *distinct infected* others contributes infection pressure \(c_j\ge0\) when its \((j+1)\)-person interaction is available, for \(j=1,\ldots,d\). All possible groups of each permitted size are available. The convention is \(\binom{k}{j}=0\) for \(k<j\). Rates are continuous-time Poisson rates, not per-step probabilities. Rates \(c_j\) may depend on \(N\); no thermodynamic scaling is assumed. Only the infection-count stationary law is counted, not the much larger distribution over labeled microstates.

The infected count is a birth–death chain with birth and death rates

\[
b_k=(N-k)\left(\varepsilon+\sum_{j=1}^d c_j\binom{k}{j}\right),\quad 0\le k<N,
\qquad
q_k=\mu k,\quad 1\le k\le N.
\]

A **strict local mode** is a state whose stationary mass is strictly greater than the mass at each existing nearest-neighbor state. Plateaus and non-strict ties are not counted as strict modes. The results remain valid on parameter hyperplanes where adjacent probabilities tie, as upper bounds on strict modes.

## Proof

**1. Unique stationary law and the adjacent-mass test.** Because \(\varepsilon>0\), all births below \(N\) are positive, and all deaths above zero are positive, so the chain is irreducible. The standard detailed-balance recursion gives

\[
\frac{\pi_{k+1}}{\pi_k}=
\frac{(N-k)(\varepsilon+\sum_{j=1}^d c_j\binom{k}{j})}{\mu(k+1)},
\qquad 0\le k<N.
\]

Define the real polynomial

\[
P(x)=(N-x)\left(\varepsilon+\sum_{j=1}^{d}c_j\binom{x}{j}\right)-\mu(x+1),
\qquad \binom{x}{j}=\frac{x(x-1)\cdots(x-j+1)}{j!}.
\]

It has degree at most \(d+1\), \(P(0)=N\varepsilon-\mu<0\), and \(P(N)=-\mu(N+1)<0\). For each integer \(0\le k<N\), the sign of \(P(k)\) is the sign of \(\pi_{k+1}-\pi_k\). Consequently, \(0\) is always a strict mode.

**2. Root-budget bound.** For every other strict mode \(r\in\{1,\ldots,N\}\), \(P(r-1)>0\) and either \(r=N\) or \(P(r)<0\). Thus each nonzero strict mode is the right end of a distinct positive run of the sampled polynomial signs. A positive run is bracketed by negative values, starting with \(P(0)<0\) and ending no later than \(P(N)<0\). The intermediate value theorem gives at least two *distinct* real polynomial roots for each run. Distinct runs have disjoint root brackets. Therefore, if there are \(s\) positive runs, \(2s\le\deg P\le d+1\), and there are at most \(1+s\le1+\lfloor(d+1)/2\rfloor\) strict modes. Zeros at sampled integers can eliminate a strict mode but cannot increase this bound; count connected components of \(\{x\in(0,N):P(x)>0\}\) instead if necessary.

For \(d\le2\), this bound is at most two; for \(d=3\), it is at most three.

**3. Uniform sharpness for four-person interactions.** For every integer \(N\ge4\), normalize \(\mu=1\). Set

\[
t=\frac{N-5}{(N-1)(N-2)},\quad
\varepsilon=\frac12\left(t+\frac1N\right),\quad
L=\frac2{N-1}-\varepsilon,\quad
U=\frac3{2(N-2)}-\frac{\varepsilon}{2},
\]

and take

\[
c_1=\frac{L+U}{2},\qquad c_2=\frac{U-L}{2},\qquad c_3=N+1.
\]

These are all strictly positive: \(0<\varepsilon<1/N\) and \(U-L=(\varepsilon-t)/2>0\) follow from \(t<1/N\); also \(L>0\) for \(N\ge4\). Since \(c_1>L\), the infected-count transition at \(k=1\) satisfies \(b_1>2\). Since \(c_1<U\) and \(c_2=(U-L)/2\), the inequality \(\varepsilon+2c_1+c_2<3/(N-2)\) gives \(b_2<3\). Meanwhile \(b_0=N\varepsilon<1\). For every \(3\le k<N\), \(b_k\ge(N-k)c_3\binom{k}{3}\ge N+1>k+1\). Hence the adjacent stationary ratios are strictly below one at \(k=0,2\), strictly above one at \(k=1\), and strictly above one for every \(3\le k<N\). The only strict modes are \(0,2,N\).

Finally, any distribution on \(N+1\) ordered states needs at least five states to accommodate three mutually nonadjacent strict local modes, so \(N\ge4\) is necessary. The construction attains this minimum, and all its strict inequalities persist under sufficiently small changes in the rates.

## Verification

The standalone `verify.py` uses exact rational arithmetic. It reconstructs the stationary product formula, checks detailed balance independently for labeled configuration transitions, tests the mode ceiling across 2,916 finite parameter/model combinations, tests the three-mode construction for every \(4\le N\le200\), checks the exact five-point witness and evaluates a separate four-person pair-plus-tetrahedron parameter chamber. It prints `VERIFY_OK` on success. The complete proof for arbitrary \(N\) is the preceding algebraic argument, not the finite test run. Execute with `python verify.py` (standard Python library only).

## Relationship to prior work

Kiss, Iacopini, Simon and Georgiou [1] derive the exact finite Kolmogorov rates for simplicial SIS contagion on complete structures and analyze limiting mean-field multistability through four-person groups; their equations (II.20)–(II.23) provide the baseline rates without importation. The extension here adds strictly positive importation, studies the **unique finite stochastic stationary law**, and proves a sharp *number-of-strict-peaks* ceiling together with a positive-rate witness for every population size. Its root-budget argument concerns adjacent stationary **probability masses**, not mean-field zeros. The older nodal self-infection literature [2] supplies precedent for immigration-like epidemic regularization, while the simplicial three-person literature [3] treats an approximate discrete-time epidemic transition; neither asserts the stationary four-person order threshold established above. General birth–death detailed balance [4] is standard and is not claimed as new.

## Limitations

The conclusion assumes complete mixing, independent exponential events, weak spontaneous infection \(0<\varepsilon<\mu/N\), and nonnegative group transmission rates. It does not describe a general noncomplete hypergraph, quasi-stationary laws without importation, stationary modes of individual labeled configurations, mean-field stability, or rates calibrated to empirical populations. It counts *strict* modes; equal-mass plateaus are not classified. The general degree bound need not be sharp for every higher order \(d>3\). The all-\(N\) construction is algebraic and may use strong four-person infection pressure; this demonstrates possibility rather than typicality. Independent literature priority and empirical validation remain open.

## References

[1] I. Z. Kiss, I. Iacopini, P. L. Simon, N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752v1 (first public 2023-09-22), https://arxiv.org/abs/2309.12752, especially Sections II.B–C, III.B and conclusions.

[2] P. Van Mieghem and E. Cator, *Epidemics in networks with nodal self-infection and the epidemic threshold*, Physical Review E 86, 016116 (2012), https://doi.org/10.1103/PhysRevE.86.016116.

[3] J. T. Matamalas, S. Gómez, A. Arenas, *Abrupt phase transition of epidemic spreading in simplicial complexes*, arXiv:1910.03069 (first public 2019-10-07), https://arxiv.org/abs/1910.03069.

[4] Standard finite birth–death chain detailed-balance recurrence; see, e.g., J. R. Norris, *Markov Chains*, Cambridge University Press (1997), Chapter 2.
