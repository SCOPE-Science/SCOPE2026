# Sharp four-site local reversal between sequential and static parking on paths

## Finding

For every integer \(n\ge14\), consider the path graph \(P_n\) with vertices labelled \(1,\ldots,n\). Let \(Q_n(j)\) be the probability that vertex \(j\) belongs to the terminal random greedy maximal independent set constructed by assigning independent, continuous, uniform arrival times to all vertices and accepting an arrival if neither neighbor has already been accepted. Let \(U_n(j)\) be the probability that the same vertex belongs to a maximal independent set sampled *uniformly among all maximal independent sets*. Then, for every \(1\le j\le n\),

\[
Q_n(j)<U_n(j)\quad\Longleftrightarrow\quad j\in\{2,4,n-3,n-1\},
\]

and \(Q_n(j)>U_n(j)\) at every other vertex. All inequalities are strict. The onset \(n=14\) is sharp as an eventual classification: at \(n=13\), the central vertex \(j=7\) also satisfies \(Q_{13}(7)<U_{13}(7)\).

This demonstrates that first-order stochastic dominance of the **total** greedy occupied count over the corresponding uniform-maximal-set count, known for all paths, does not imply sitewise domination: exactly four near-endpoint sites locally favor the static model once \(n\ge14\).

## Assumptions and scope

The graph is the simple labelled path on \(n\) vertices. A random priority order is uniformly distributed over all permutations; because continuous independent arrival times induce such an order, it has the same terminal law as uniformly choosing one available vertex at each step. The static law is uniform *over maximal independent sets* and is not the law of an unrestricted uniform independent set. The theorem concerns one-point occupation probabilities; it does not assert stochastic domination for the vector of site indicators or a coupling with coordinatewise inclusion.

Let \(S_0=1,S_1=1,S_2=2\) and \(S_m=S_{m-2}+S_{m-3}\) for integers \(m\ge3\). Thus \(S_m\) counts maximal independent sets on a path of length \(m\). Put \(E_\ell(t)=\sum_{r=0}^{\ell}(-t)^r/r!\) for integers \(\ell\ge0\). The exact finite-size laws are

\[
U_n(j)=\frac{S_{\max(0,j-2)}S_{\max(0,n-j-1)}}{S_n},
\qquad
Q_n(j)=\int_0^1 E_{j-1}(t)E_{n-j}(t)\,dt.
\]

Both expressions are rational at every integer \(n,j\). An equivalent finite double sum for \(Q_n(j)\) is

\[
Q_n(j)=\sum_{r=0}^{j-1}\sum_{s=0}^{n-j}
\frac{(-1)^{r+s}}{r!s!(r+s+1)}.
\]

## Proof

**Exact formulas.** If vertex \(j\) is chosen in a maximal independent set, its two neighbors are excluded. The remaining lengths are \(\max(0,j-2)\) and \(\max(0,n-j-1)\), which can independently carry any maximal independent sets. The usual left-end decomposition gives \(S_m=S_{m-2}+S_{m-3}\) for \(m\ge3\), including the stated initial values; counting yields \(U_n(j)\).

For the greedy law let \(F_\ell(t)\) be the probability that the first site of an isolated path of \(\ell\) vertices has become accepted by time \(t\), given independent uniform priorities. Set \(F_0=0\). Conditional on that first site's priority being \(t\), it is accepted if the neighboring site's independent residual process has not accepted the neighbor before \(t\). Therefore \(F_\ell'(t)=1-F_{\ell-1}(t)\), with \(F_\ell(0)=0\), and induction gives \(1-F_\ell(t)=E_\ell(t)\). Conditional on the priority of vertex \(j\), its two arms are independent. Integrating over its priority yields the displayed formula for \(Q_n(j)\), and termwise integration gives the exact rational double sum.

**Uniform tail region.** Let \(p\) denote the unique real root greater than one of \(p^3=p+1\), and define \(R_m=S_m/p^m\). The positive identity \(p^{-2}+p^{-3}=1\) gives the convex recurrence \(R_m=p^{-2}R_{m-2}+p^{-3}R_{m-3}\). Exact-rational root brackets certify \(1324717957/10^9<p<1324717958/10^9\), and exact checks at \(m=10,11,12\) give \(95/100<R_m<97/100\). By the recurrence, the same bounds hold for all \(m\ge10\).

By symmetry it suffices to consider \(1\le j\le (n+1)/2\). When \(n\ge23\), both \(n-j-1\) and \(n\) are at least ten. Set \(B_j=S_{\max(0,j-2)}/p^{j+1}\). Then

\[
\frac{95}{97}B_j<U_n(j)<\frac{97}{95}B_j.
\]

For every \(j\ge9\), the \(B_j\) satisfy the same positive convex recurrence. The exact inequalities \(B_6<B_7\) and \(B_8<B_7\) imply \(B_j\le B_7=4/p^8\) for all \(j\ge6\). For \(0\le t\le1\), the alternating-series remainder and nonnegativity of all the \(E_\ell(t)\) give \(\lvert E_\ell(t)-e^{-t}\rvert\le t^{\ell+1}/(\ell+1)!\). In the half-path with \(j\ge6\), integrating the two product remainders therefore gives

\[
Q_n(j)\ge \frac{1-e^{-2}}2-\frac{2}{7!}
>\frac{97}{95}\frac{4}{p^8}\ge U_n(j).
\]

The strict central inequality is proved by **rational interval arithmetic**, bounding \(e^{-1}\) between its alternating sums through degrees 15 and 16 and using the displayed rational bounds for \(p\). It is checked in the standalone certificate; it is not a floating-point inference.

**Five boundary positions.** For each \(1\le j\le5\), the second factor in the exact greedy integral has error at most \(1/(n-j+2)!\) after integration, hence at most \(1/20!\) when \(n\ge23\). The infinite-arm values \(A_j=\int_0^1e^{-t}E_{j-1}(t)\,dt\) are, in order,

\[
(A_1,A_2,A_3,A_4,A_5)
=\left(1-e^{-1},\ e^{-1},\ 1-\tfrac32e^{-1},\ \tfrac76e^{-1},\ 1-\tfrac{37}{24}e^{-1}\right).
\]

Exact interval-rational checks show \(A_j-1/20!>(97/95)B_j\) for \(j\in\{1,3,5\}\), while \(A_j+1/20!<(95/97)B_j\) for \(j\in\{2,4\}\). Combined with the earlier bounds for \(U_n(j)\) and the greedy remainder, these prove the required signs at positions \(1,\ldots,5\) for all \(n\ge23\).

**Remaining finite lengths.** For each integer \(14\le n\le22\) and each \(1\le j\le n\), the standalone checker evaluates the displayed finite rational sum and the exact static fraction. Every sign is strictly as claimed. For \(n=13,j=7\), the checker verifies strict negativity, showing sharpness of the onset. These are exhaustive finite intervals, not an extrapolation from a partial experiment. Reflection symmetry completes the infinite-range proof.

## Verification

Run `python3 check.py` with Python's standard library. The program evaluates 289 exact-rational assertions, including all finite cases, independent first-arrival recurrences for lengths at most nine, independent enumeration of every maximal independent set for lengths at most ten, the plastic-root bracket, the Padovan ratio invariant, and all analytic inequality endpoints with rational interval bounds. Its actual standard output is supplied in `checker_output.txt`. The infinite range is established analytically by the positive convex recurrence and Taylor estimates just proved; numerical sampling is not substituted for the infinite proof.

## Relationship to prior work

Higuita-Diaz, López and Roldán-Correa (arXiv:2611.14718v1) prove stochastic dominance of the **total** occupied count on paths, supply the static site-probability Padovan formula, and analyze conditional static site probabilities. Their result does not give signs of the difference of the two *unconditional single-site laws*, and total-count order does not entail such signs. Shneer and van de Ven (2017, with results first circulated in 2011) supply an exact finite sequential per-site law in the equivalent random-priority/dimer model and interpret it as site throughput; the sequential site formula is not claimed as new here. The contribution is the all-length **comparative sign classification**, its four negative sites, and the exact sharp eventual onset, proved by a new uniform comparison. Previously published studies of greedy cycles, dimer parking and finite subcubic total-count order treat different claims and do not imply this sitewise classification as stated.

## Limitations

The assertion compares one-site *marginals only*, not global sampling efficiency, full joint distributions or distributions on other graph families. All finite-range assertions are checked exactly with supplied code. The two exact underlying one-site formulas and the global count-order theorem are prior results, not newly discovered. A possibly relevant earlier 2026 article on combinatorial aspects of discrete parking was not available in full text through accessible routes; it creates a residual historical-priority risk. No independent validation has been performed, and novelty searches cannot prove absolute uniqueness.

## References

1. Higuita-Diaz, R., López, L., and Roldán-Correa, A., *Stochastic Dominance in Discrete Parking Processes on Graphs*, arXiv:2611.14718v1 (10 November 2026), https://arxiv.org/html/2611.14718v1.
2. Shneer, S., and van de Ven, P. M., *Per-site occupancy in the discrete parking problem*, *Statistics & Probability Letters* **120** (2017), 141–146, https://doi.org/10.1016/j.spl.2016.09.019, authorized public copy: https://sites.math.rutgers.edu/~zeilberg/akherim/parking/shneer2017.pdf.
3. Higuita-Diaz, R., López, L., and Roldán-Correa, A., *Combinatorial aspects of a discrete parking process*, *Statistics & Probability Letters* **233** (2026), 110682, https://doi.org/10.1016/j.spl.2026.110682 (full text not accessed).
4. *Greedy maximal independent sets via local limits*, *Random Structures & Algorithms* **64** (2024), 986–1015, https://doi.org/10.1002/rsa.21200 (general asymptotic background).
