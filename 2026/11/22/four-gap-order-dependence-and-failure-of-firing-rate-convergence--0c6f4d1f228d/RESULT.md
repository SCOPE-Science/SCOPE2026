# Four-gap order dependence and failure of firing-rate convergence despite fixed clock marginals

## Finding

There is a uniformly discrete, relatively dense time scale whose opportunity density and complete empirical one-gap distribution converge with bounded counting errors, but whose structure-preserving integrate-and-fire neuron has **no asymptotic firing rate**. The failure occurs on an exact, nonempty reset-to-threshold interval, and only four clock gaps per periodic motif are needed for the underlying gap-order dependence; at most three gaps per periodic motif can never distinguish two orders of the same gap multiset by their asymptotic firing rates.

More precisely, choose any infinite word \(b=(b_k)_{k\geq0}\) in \(\{A,B\}\) and let

\[
P_A=\{0,2,5,9\},\qquad P_B=\{0,2,6,9\},\qquad
\mathbb T_b=\bigcup_{k\geq0}\bigl(14k+P_{b_k}\bigr).
\]

Write \(N_B(m)=\#\{0\leq k<m:b_k=B\}\). Starting with a reset/spike at \(t_0=0\), let the subsequent firing times satisfy the forward-projection law

\[
t_{j+1}=\min\{u\in\mathbb T_b:u\geq t_j+c\},\qquad c>0,
\]

and let \(S_c(x)=\#\{j\geq0: t_j<x\}\). For every integer \(m\geq1\) and all \(0<c\leq5\), **exactly**

\[
S_c(14m)=
\begin{cases}
4m,&0<c\leq2,\\
3m,&2<c\leq3,\\
3m-N_B(m),&3<c\leq4,\\
2m,&4<c\leq5.
\end{cases}
\]

Each block of four consecutive opportunity gaps is a permutation of \((2,3,4,5)\). Thus the opportunity density is exactly \(2/7\), and the empirical frequencies of all four individual gap lengths are exactly \(1/4\), with \(O(1)\) discrepancy at arbitrary truncations. The maximum gap (graininess) is \(5\).

If \(b\) consists of alternating constant-letter runs of lengths \(L_j=2^{2^j}\), \(j=1,2,\ldots\), beginning with an \(A\)-run, then for each \(3<c\leq4\)

\[
\liminf_{x\to\infty}\frac{S_c(x)}x=\frac17,
\qquad
\limsup_{x\to\infty}\frac{S_c(x)}x=\frac3{14},
\]

and the set of all subsequential limits is the full interval \([1/7,3/14]\). Outside this interval of threshold values, but within \(0<c\leq5\), the firing-rate limit exists for every \(b\), with respective values \(2/7\), \(3/14\), and \(1/7\) in the three remaining ranges above.

For the two pure periodic clocks \(AAAA\ldots\) and \(BBBB\ldots\), the input densities and one-gap distributions are identical, yet their firing rates for \(3<c\leq4\) are \(3/14\) and \(1/7\), respectively. The smallest length of a periodic gap motif capable of exhibiting such an order effect, **among two periodic clocks with the same unordered gap list and the same reset time \(c\)**, is four.

## Assumptions and scope

The temporal domain is the closed, unbounded, discrete subset \(\mathbb T_b\subset[0,\infty)\). No stationarity, ergodicity, or existence of letter frequencies is assumed. The law starts at an actual spike/reset time \(0\in\mathbb T_b\), and an opportunity at exact delay \(c\) is eligible; this weak inequality matters at \(c=2,3,4,5\).

For a concrete physiological normalization of the structure-preserving leaky integrate-and-fire model, take membrane time constant \(\tau_m=1\), reset potential \(V_r=0\), asymptotic potential \(V_\infty=1\), and threshold \(V_{th}=1-e^{-c}\). Then \(V_\infty>V_{th}>V_r\), the continuous reset-to-threshold travel time is exactly \(c\), and the on-time-scale firing model of Kaymakçalan–Selçuk yields the displayed forward projection. Thus the counting assertion is about genuine threshold/reset trajectories, not a discretized Euler approximation.

The minimal-four assertion concerns **periodic clocks with a specified finite number of strictly positive successive gaps per period**, considered up to reordering the same gap multiset. It does not claim that every four-gap ordering differs, nor that arbitrary nonperiodic clocks with only three distinct gap *values* have convergent firing rates.

## Proof

**Step 1 (event statistics).** In an \(A\)-cell, the four gaps (including the transition to the next cell origin) are \((2,3,4,5)\). In a \(B\)-cell, they are \((2,4,3,5)\). Hence there are precisely four opportunities per half-open cell \([14k,14(k+1))\) and one occurrence of each gap length in its complete four-gap list. At the end of \(m\) cells there are exactly \(4m\) opportunities and exactly \(m\) gaps of each of the four lengths; all arbitrary-time remainders are bounded by four events/gaps. Therefore \(\#(\mathbb T_b\cap[0,x))/x\to4/14=2/7\), the one-gap empirical distribution tends to \((1/4,1/4,1/4,1/4)\), and the maximum gap is \(5\).

**Step 2 (exact cell transitions).** Every cell origin \(14k\) is a firing time, by induction from \(t_0=0\). Indeed, the earliest-next-opportunity rule gives the following exhaustive within-cell lists, written relative to the origin, *including the next boundary at \(14\)*:

| Range for \(c\) | \(A\)-cell fired offsets | \(B\)-cell fired offsets |
|---|---|---|
| \(0<c\le2\) | \(0,2,5,9,14\) | \(0,2,6,9,14\) |
| \(2<c\le3\) | \(0,5,9,14\) | \(0,6,9,14\) |
| \(3<c\le4\) | \(0,5,9,14\) | \(0,6,14\) |
| \(4<c\le5\) | \(0,5,14\) | \(0,6,14\) |

Each entry is at least \(c\) after the preceding fired offset, and each omitted opportunity lies strictly less than \(c\) after that preceding fired offset. The final offset is \(14\) for both letters and every displayed range, so concatenation introduces no phase uncertainty. Counting all fired offsets less than the right endpoint of each cell proves the exact formula for \(S_c(14m)\). Counts over a final incomplete cell differ by at most four; replacing \(14m\) by arbitrary \(x\to\infty\) changes the count/time quotient by \(o(1)\).

**Step 3 (nonconvergence and the full limit interval).** Choose \(b\) by alternating blocks of letters with lengths \(L_j=2^{2^j}\). The ratio of any previous combined run length to the current one tends to zero; at ends of successive \(A\)- and \(B\)-runs, \(N_B(m)/m\) tends along subsequences to \(0\) and \(1\), respectively. Its full liminf and limsup are therefore \(0\) and \(1\). Moreover consecutive Cesàro averages differ by at most \(1/(m+1)\), hence every intermediate value in \([0,1]\) is a subsequential limit: between arbitrarily late averages near the two extremes, the bounded increments force intermediate crossings. For \(3<c\le4\), the exact count formula yields \(S_c(14m)/(14m)=(3-N_B(m)/m)/14\); bounded remainders give the stated full interval of firing-rate limit points. The remaining threshold bands follow from the constant counts in Step 2.

**Step 4 (why four is the first possible periodic gap-order obstruction).** Fix \(c>0\). On any finite increasing set of eligible event times, choosing the earliest point and then always the earliest point at least \(c\) later maximizes the number chosen. This follows inductively by replacing the first choice of any competing \(c\)-separated subset with the earlier first available event; the replacement cannot spoil any later spacing constraint.

For any periodic clock with period \(P>0\) and \(r\) opportunities in each half-open period, its finite-state phase map has an eventually periodic phase itinerary, so its greedy firing density exists. Cyclic rotation of the ordered \(r\) gaps amounts to translating the periodic event set; the maximal separated subset counts in long finite windows differ by at most \(O(r)\), hence the asymptotic greedy rates agree. Reversing the ordered gaps reflects the event set. In a window \([0,nP]\) whose endpoints are event times, the reflection \(t\mapsto nP-t\) bijects eligible events and preserves the sizes of separated subsets. The maximum count, therefore the greedy count, is exactly the same under reversal in each such window, and the rates agree. For \(r\le3\), every permutation of \(r\) elements is a cyclic rotation or a cyclic rotation followed by reversal (the dihedral group on three positions is the full symmetric group). Consequently all orderings of an unordered list of at most three periodic gaps have the same firing density for every \(c>0\). The explicit \(A\)- and \(B\)-periodic clocks above both have four gaps and have distinct densities in \(3<c\le4\), proving sharpness.

## Verification

A standalone Python 3 program `verify.py` checks the forward-projection law in exact rational arithmetic on every binary clock word of lengths \(1\) through \(8\), at all four transition boundaries and their interiors, and compares with the complete formula. It also checks individual gap multisets and finite-window reversal invariance of maximal separated subsets for samples of three-gap periodic motifs. These are finite consistency tests; the proof above, not the enumeration, establishes the infinite statements.

## Relationship to prior work

Kaymakçalan and Selçuk (2026) prove that the constant-input, structure-preserving leaky integrate-and-fire model on an arbitrary closed time scale has spike recursion \(t_{n+1}=\Pi_{\mathbb T}^+(t_n+c)\), and derive a firing rate for homogeneous lattice clocks. Their Sections 5–8 do not classify the existence of rates under merely bounded gaps or under fixed first-order gap statistics. The present result uses their recursion but adds an explicit sharp order-obstruction, a uniform gap-histogram counterexample, and an exact nonconvergence interval.

The literature on nonparalyzable dead-time detection, such as Peterson (2021), studies stochastic event sources, numerical interval distributions and history-dependent event filtering. The deterministic, fully explicit fixed-gap-histogram construction here addresses a different infinite-time assertion. The elementary earliest-event greedy exchange principle is standard and is used as a proof tool, not claimed as a new algorithm.

## Limitations

The result is an exact, constructed boundary phenomenon, not a claim of typical behavior for randomly generated or uniquely ergodic opportunity clocks. It concerns a single neuron with constant input, deterministic admissible times, and a first spike fixed at \(0\); it does not characterize all initial phases or all thresholds \(c>5\). First-order gap frequencies alone do not ensure convergence here, but the theorem does not rule out stronger sufficient hypotheses involving longer patterns, stationarity, or unique ergodicity. The claimed minimality is restricted to rearrangements of the same periodic gap multiset; it is not an optimality claim over all possible clock statistics or random processes. Independent mathematical validation has not been performed.

## References

1. B. Kaymakçalan and B. İ. Selçuk, *Structure-Preserving Leaky Integrate-and-Fire Dynamics on Arbitrary Time Scales*, arXiv:2611.17219v1, first public 12 November 2026. https://arxiv.org/html/2611.17219v1
2. A. J. Peterson, *A numerical method for computing interval distributions for an inhomogeneous Poisson point process modified by random dead times*, Biological Cybernetics **115** (2021), 177–190. https://doi.org/10.1007/s00422-021-00868-8
