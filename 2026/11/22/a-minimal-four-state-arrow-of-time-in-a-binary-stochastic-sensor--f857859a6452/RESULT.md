# A minimal four-state arrow of time in a binary stochastic sensor

## Finding

A stationary binary readout of an irreducible continuous-time Markov chain with at most three microstates is reversible as a **complete process**, even when the hidden chain violates detailed balance. Four microstates are sharp. In the clockwise ring with positive rates \(1\to2\to3\to4\to1\) equal to \(a,b,c,d\), respectively, a binary sensor that labels \(\{1,3\}\) by 1 and \(\{2,4\}\) by 0 yields a time-irreversible stationary process **if and only if** \((a-c)(b-d)\ne0\). Every other nonconstant binary coloring of this ring yields a time-reversible process.

For equal-time-step samples, let \(p_h(w)\) be the stationary probability of the four-symbol word \(w\), observed at times \(0,h,2h,3h\). Then

\[
p_h(1100)-p_h(0011)=\frac{abcd(a-c)(b-d)}{abc+abd+acd+bcd}\,h^3+O(h^4),\qquad h\downarrow0.
\]

Thus four binary snapshots detect the temporal direction at arbitrarily small sampling intervals whenever both opposite rate contrasts are nonzero. A physically reversible-edge version (strictly positive transitions in both directions around the ring) also has a nonzero binary time-arrow witness, for all sufficiently small counterclockwise rates, with finite positive entropy production.

## Assumptions and scope

A finite-state continuous-time Markov chain has its usual row-generator \(Q\), exponential holding times and stationarity under its unique invariant distribution \(\pi\). A binary sensor is a deterministic map from microstates to \(\{0,1\}\), observed continuously or at finitely many deterministic times. Reversibility means equality in law of \((Y_{t_1},\ldots,Y_{t_k})\) and \((Y_{-t_1},\ldots,Y_{-t_k})\) for every finite collection of times in stationarity; it is not a claim about reversibility of microscopic rates. The upper-bound part covers every irreducible generator with \(1\le n\le3\) and every binary coloring, with no condition of microscopic detailed balance. The four-state classification is only for the specified one-way ring, not for every four-state topology. Rates are all strictly positive, and endpoints where they vanish are excluded.

For the one-way ring, in the ordered state basis \((1,2,3,4)\),

\[
Q=\begin{pmatrix}-a&a&0&0\\0&-b&b&0\\0&0&-c&c\\d&0&0&-d\end{pmatrix},\qquad
\pi=\frac{(bcd,acd,abd,abc)}{Z},\quad Z=abc+abd+acd+bcd.
\]

The sensor projectors are \(M_1=\operatorname{diag}(1,0,1,0)\) and \(M_0=I-M_1\).

## Proof

**1. Lower bound on the hidden state count.** On at most three states, any nonconstant binary partition has a singleton class. Whenever the chain enters that microstate, the strong Markov property restarts the future, and every exit returns to the other color. Its successive singleton dwell times are independent exponentials. The intervals in the complementary color are independent first-return excursions, identically distributed from cycle to cycle, and are independent of the singleton holding times. Thus the binary process is the stationary version of an alternating renewal process with independent sojourn lengths in its two colors. Its Palm law of alternating renewal intervals is invariant under reversing interval order, and equilibrium residual-life sampling gives the same stationarity correction in either direction. Consequently the full stationary binary path law is reversible. Constant colorings are trivial. This conclusion is unaffected by internal irreversible cycles within the complementary class.

**2. Four-state coloring classification.** The nonconstant binary partitions of the directed ring, up to exchanging colors and rotating or reflecting their geometric descriptions, are singleton versus triple, adjacent pair versus adjacent pair, and opposite pair versus opposite pair. Singleton partitions are handled by step 1, regardless of ring size. For adjacent pairs, every sojourn of one color traverses two successive exponential clocks, then enters the other color at a fixed microstate. The two color-sojourn distributions repeat independently each cycle, hence the observed process is alternating renewal and reversible. For opposite pairs, successive 1-runs alternate between exponential laws with rates \(a\) and \(c\), and successive 0-runs alternate between rates \(b\) and \(d\). At an entry into color 1, the hidden entry state is 1 or 3 with equal Palm probability: each of the four ring edges carries the same stationary traffic \(J=abcd/Z\).

Denote by \(U\) the length of the 1-run begun at a typical entry into color 1, by \(V_+\) the immediately succeeding 0-run, and by \(V_-\) the immediately preceding 0-run. Conditioning on the two equally frequent hidden phases and using independence of the exponential clocks gives

\[
\mathbb E[UV_+]-\mathbb E[UV_-]
=\frac12\left(\frac1a-\frac1c\right)\left(\frac1b-\frac1d\right).
\]

Under time reversal, past and future 0-runs exchange places; hence nonzero difference proves time irreversibility whenever both opposite rate contrasts are nonzero. Conversely, if \(a=c\), all 1-run lengths are independent identically distributed and the 0-run lengths form an independent alternating sequence of exponential laws with rates \(b,d\), its initial phase being a fair coin. Reversing a bi-infinite sequence exchanges the two phases, which have equal law. Replacing \(a=c\) by \(b=d\) gives the same argument with colors swapped. Thus the sensor is reversible exactly when \(a=c\) or \(b=d\), proving necessity and sufficiency without assuming that its binary dynamics are Markovian.

**3. Explicit four-snapshot witness.** Define the diagonal projectors \(M_0,M_1\) as above, and write \({\bf1}\) for the column of ones. The exact stationary probability of a sampled word \(w=(w_0,w_1,w_2,w_3)\) is

\[
p_h(w)=\pi M_{w_0}e^{hQ}M_{w_1}e^{hQ}M_{w_2}e^{hQ}M_{w_3}{\bf1}.
\]

Insert \(e^{hQ}=I+hQ+h^2Q^2/2+h^3Q^3/6+O(h^4)\). Direct multiplication shows that the coefficients of degrees zero, one and two cancel in \(p_h(1100)-p_h(0011)\), whereas the degree-three coefficient is \(abcd(a-c)(b-d)/Z\). This proves the displayed expansion and supplies an explicit four-snapshot witness whenever the two rate contrasts differ from zero. For **equally spaced observations**, four consecutive symbols are the smallest window length capable of showing time-reversal asymmetry in any stationary binary series: one-, two-, and three-consecutive-symbol word frequencies are necessarily reversal symmetric by stationarity and two-symbol counting (a known general observation). This does **not** rule out a three-time test with unequal gaps. For every sufficiently small positive \(h\), the coefficient above forces a nonzero four-symbol witness.

**4. Positive reverse edges.** Keep each clockwise rate \(a,b,c,d\) and add a common counterclockwise rate \(\varepsilon>0\) at every site. The stationary distribution and each fixed-lag four-word probability depend continuously on the rates by irreducibility of finite generators. Select positive rates with \((a-c)(b-d)\ne0\), then fix a sufficiently small \(h>0\) with a nonzero one-way witness. Continuity makes that witness persist for all sufficiently small positive \(\varepsilon\). All edges are now bidirectional and the entropy production is finite. For \(\varepsilon^4\ne abcd\), the cycle affinity \(\log(abcd/\varepsilon^4)\) is nonzero; a four-edge unicyclic network then has a nonzero stationary circulation and strictly positive entropy production. This establishes physical robustness without asserting that the simple rate-equality criterion remains exact at arbitrary reverse rates.

## Verification

The included `checker.py` evaluates the stationary matrix-product coefficient **symbolically for arbitrary positive \(a,b,c,d\)** using SymPy, checking exact cancellation through quadratic order and the exact cubic factor. It compares 20 independent numerical rate choices using the matrix exponential, checks 15 reversible parameter instances at five finite lags, tests 288 variable-gap reversed four-word probabilities for nonreversible three-state rings under binary readouts, and verifies a strictly positive reverse-rate example with \(\varepsilon=0.025\). It executes with Python, SymPy, NumPy and SciPy; command: `python checker.py`. These diagnostics verify algebra and representative finite-lag evaluations, but do not substitute for the regenerative and time-reversal proofs above.

## Relationship to prior work

Ghosal and Bisker's 2026 review of experimental stochastic irreversibility and coarse-graining motivates the specific question of whether a one-bit observable can carry an arrow of time. Biddle (2026) reconstructs entropy production from a sufficiently resolved **state sequence**, rather than from this deterministic binary projection. Lucente et al. (2022), Section V, explicitly establish that a singleton-class binary coarse-graining is a two-state renewal/semi-Markov observation with zero trajectory entropy-production rate; this is credited as the crucial known obstruction behind the three-state lower bound. Arola-Fernandez and Lacasa (2023), Section III, prove the general impossibility of detecting irreversibility from binary words of fewer than four symbols; this observation-count limit is not claimed as new. Martínez et al. (2019) develop entropy inference from semi-Markov waiting times; the Hartich–Godec (2024) comment cautions against interpreting certain waiting-time entropy measures as actual broken detailed balance without examining coarse-graining and kinetic hysteresis.

The assessed increment is the **complete binary-coloring and rate-contrast classification for the minimal directed four-state cycle**, together with the closed Palm two-run witness, explicit four-snapshot coefficient, and bidirectional robustness. Earlier work supplies general inference methods and no-go mechanisms; none of the inspected material presents or logically supplies this specific rate criterion and coefficient as a stated result. These parts remain publication-priority claims, not externally certified uniqueness.

## Limitations

The exact iff criterion is restricted to a one-way four-state ring and its stated alternating binary partition. Although the nonzero witness persists for sufficiently small bidirectional perturbations, an exact global phase diagram for arbitrary reverse rates is not established. Detecting a binary time arrow is not the same as reconstructing microscopic entropy production or all hidden rates. In finite data, the equally spaced four-symbol witness is cubic in short sampling intervals and can be difficult to estimate; no finite-sample power bound is claimed. The four-symbol minimality applies only to equally spaced consecutive observations: unequal three-time gaps may already detect a nonreversible binary process. Earlier coarse-grained stochastic thermodynamics literature is broad, and an equivalent unstated corollary or unindexed account cannot be excluded. No independent mathematical audit has been performed.

## References

1. A. Ghosal and G. Bisker, “Identification and quantification of irreversibility in stochastic systems,” *Physical Chemistry Chemical Physics* **28** (2026), 9840–9866, first public 2026-04-08, DOI: 10.1039/D5CP04712A. Full open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13067933/
2. J. W. Biddle, “A method for calculating entropy production without knowing transition rates or dwell times,” arXiv:2605.27635, first submitted 2026-05-26. https://arxiv.org/abs/2605.27635
3. D. Lucente, A. Baldassarri, A. Puglisi, A. Vulpiani and M. Viale, “Inference of time irreversibility from incomplete information: Linear systems and its pitfalls,” *Physical Review Research* **4** (2022), 043103, DOI: 10.1103/PhysRevResearch.4.043103. https://arxiv.org/abs/2205.08961
4. L. Arola-Fernandez and L. Lacasa, “Irreversibility of symbolic time series: a cautionary tale,” arXiv:2303.11868, first submitted 2023-03-21. https://arxiv.org/abs/2303.11868
5. I. A. Martínez, G. Bisker, J. M. Horowitz and J. M. R. Parrondo, “Inferring broken detailed balance in the absence of observable currents,” *Nature Communications* **10** (2019), 3542, DOI: 10.1038/s41467-019-11051-w.
6. D. Hartich and A. Godec, “Comment on ‘Inferring broken detailed balance in the absence of observable currents’,” *Nature Communications* **15** (2024), 8678, DOI: 10.1038/s41467-024-52602-0.
