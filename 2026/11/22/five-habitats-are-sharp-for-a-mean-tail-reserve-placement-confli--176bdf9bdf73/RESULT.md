# Five habitats are sharp for a mean–tail reserve-placement conflict under spatially correlated losses

## Finding

Consider a cyclic landscape with two sites that are guaranteed to remain functional and other sites exposed to spatially correlated losses. On the five-site cycle the two possible reserve layouts are adjacent sites \(S_a=\{0,1\}\) and separated sites \(S_s=\{0,2\}\). With the periodic binary Markov/Ising landscape law of the next section and every \(0<q<1\), the separated layout uniquely maximizes the expected number of sites accessible from a reserve. Nevertheless, when \(q>1/2\), the adjacent layout uniquely maximizes the probability that **all five** sites are accessible. When \(0<q<1/2\), the separated layout wins both objectives, and at \(q=1/2\) the full-accessibility probabilities tie.

Precisely, if \(U_S\) denotes the number of functional sites reachable by a path of functional sites from at least one protected site, and \(Z_5(q)=1+(2q-1)^5\), then

\[
\mathbb E_q U_{S_s}=\frac72,
\qquad
\mathbb E_q U_{S_s}-\mathbb E_q U_{S_a}
=\frac{q(1-q)^2(4q^2-6q+3)}{Z_5(q)}>0,
\]

and

\[
\Pr_q(U_{S_a}=5)-\Pr_q(U_{S_s}=5)
=\frac{q(1-q)^2(2q-1)}{Z_5(q)}.
\]

The five-site cycle is minimal in this precise family: there is only one two-reserve placement up to symmetry on a three-site cycle, and all two-reserve layouts on a four-site cycle have the same expected accessibility, exactly \(3\).

## Assumptions and scope

For a simple cycle \(C_n\), \(n\ge3\), label its vertices \(0,\ldots,n-1\) cyclically. Before intervention, the binary site state \(\omega\in\{0,1\}^n\) has probability

\[
\Pr_q(\omega)=\frac{1}{Z_n(q)}\prod_{i=0}^{n-1}
\begin{cases}q,&\omega_i=\omega_{i+1},\\1-q,&\omega_i\ne\omega_{i+1},\end{cases}
\quad \omega_n=\omega_0,
\quad Z_n(q)=1+(2q-1)^n,
\]

for every \(q\in(0,1)\). This is the zero-field periodic two-state Markov/Ising weight, **not** an independent chain closed after generation. In particular \(q=1/2\) gives independent fair binary site states, while \(q>1/2\) has positive nearest-neighbour interaction. The normalizer is the trace of the \(n\)-th power of the stochastic symmetric transition matrix with diagonal \(q\), whose eigenvalues are \(1\) and \(2q-1\). Thus \(Z_n(q)>0\) throughout the declared domain.

A deterministic intervention selects exactly two distinct vertices \(S\) and makes their final states \(1\), regardless of their original states; it **does not condition** the pre-intervention distribution on those vertices being functional. Other states remain as drawn. Two functional sites connect if joined by a path consisting entirely of functional vertices. The union of all functional connected components containing a protected site has size \(U_S(\omega)\). Both protected sites themselves are counted, including when disconnected from one another. The two objectives are \(\mathbb E_q U_S\) and \(\Pr_q(U_S=n)\). All claims are about these two objectives for \(n=3,4,5\), not an optimization over reserve costs or ecological dynamics.

## Proof

**Step 1: exhaustive, symbolic five-site classification.** For \(n=5\), let \(j(\omega)\) count cyclic equal-neighbour pairs. An odd cycle permits only \(j\in\{1,3,5\}\). Every configuration with \(j\) agreements has unnormalized mass \(q^j(1-q)^{5-j}\). The following table gives *integer numbers* of configurations with each resulting accessibility \(U_S\); it enumerates all \(2^5=32\) binary configurations for each placement.

| Placement | Agreements \(j\) | \(U_S=2\) | \(U_S=3\) | \(U_S=4\) | \(U_S=5\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| Adjacent | 1 | 3 | 2 | 5 | 0 |
| Adjacent | 3 | 4 | 6 | 7 | 3 |
| Adjacent | 5 | 1 | 0 | 0 | 1 |
| Separated | 1 | 1 | 4 | 4 | 1 |
| Separated | 3 | 2 | 8 | 8 | 2 |
| Separated | 5 | 1 | 0 | 0 | 1 |

To reproduce each cell without trusting the table, iterate over the five binary positions and perform breadth-first search from both forced-functional sites along functional cycle edges. The included `CHECK.py` exactly implements this enumeration.

Summing \(k\) times each cell of the \(U_S=k\) column with its row weight, and dividing by \(Z_5(q)\), gives the expectation. Their difference has numerator

\[
3q(1-q)^4+q^3(1-q)^2
=q(1-q)^2(4q^2-6q+3).
\]

Because \(4q^2-6q+3=4(q-3/4)^2+3/4>0\), the expectation of the separated layout is strictly larger for all \(0<q<1\). To see its exact constant value, invert all original binary states. This involution preserves the Ising weight and, for \(S_s\), pairs configurations whose reached-site counts sum to \(7\). Hence \(\mathbb E_q U_{S_s}=7/2\).

For full accessibility, only the \(U_S=5\) table columns matter. The adjacent-minus-separated numerator is

\[
-q(1-q)^4+q^3(1-q)^2
=q(1-q)^2(2q-1).
\]

All other factors, including the normalizer, are positive, so this difference changes sign *exactly once* at \(q=1/2\). Every pair of vertices on the five-cycle is equivalent by a dihedral symmetry to one of these two choices, giving global optimality and strict uniqueness modulo cycle symmetries.

**Step 2: sharp minimum of five sites.** On the triangle, every pair of distinct vertices is in the same dihedral orbit, so conflicting strict optimal layouts do not exist. On the four-cycle, for either kind of two-vertex layout \(S\), complementing all initial states pairs each configuration \(\omega\) with \(\bar\omega\) such that \(U_S(\omega)+U_S(\bar\omega)=6\). The Ising weight is invariant under the complement operation, hence \(\mathbb E_q U_S=3\) for every \(0<q<1\) and both layout types. Therefore strict opposing expectations and tail-optimal placements cannot occur at sizes three or four; five realizes them for every \(1/2<q<1\).

## Verification

`CHECK.py` uses only the Python 3 standard library. Run `python3 CHECK.py` in the folder containing the file. It exhaustively enumerates all five-site configurations and checks all six table rows, verifies the rational identities as exact integer-polynomial coefficient identities (not sampling), checks the four-site spin-complement relation for all \(16\) configurations and each type of protected pair, checks the triangle symmetry, and verifies rational test cases.

For instance, with \(q=3/4\), the complete exact outputs are

\[
\mathbb E U_{S_s}=\frac72,\quad
\mathbb E U_{S_a}=\frac{305}{88},\quad
\Pr(U_{S_s}=5)=\frac{25}{88},\quad
\Pr(U_{S_a}=5)=\frac{27}{88}.
\]

Thus a gain of \(3/88\) in expected accessibility and a gain of \(1/44\) in full accessibility point in opposite placement directions. The finite enumeration is exhaustive for the *stated finite landscape*, not extrapolated to larger cycles.

## Relationship to prior work

Hof and Flather (1996) investigated optimal wildlife-habitat placement accounting for connectivity and spatial correlation, using different connectivity/risk formulations. Albers and colleagues (2016) optimize expected species representation under spatially correlated spreading hazards in reserve selection, illustrating the practical importance of reserve arrangement and risk dependence. Their model, objective, and disturbance law do not yield the specific two-protected-site Ising-cycle classification above. In related published mathematical records, an independent-site cyclic-refuge result found that evenly spaced refuges maximize every upper tail of reachable habitat. Here the independent case \(q=1/2\) gives equal full-accessibility tails, but positive spatial correlation \(q>1/2\) *reverses the full-accessibility choice* while preserving strict mean preference for spacing. This is a narrow model-specific counterexample to extending that independent-risk conclusion, not a challenge to its independent-case theorem.

## Limitations

The theorem uses five idealized, equally valuable habitat sites, homogeneous periodic zero-field Ising weights, two perfectly protected sites, and an intervention that does not change the other sites' original joint distribution. No alternative hazard model, empirical survival calibration, demographic dynamics, or optimization with nonzero reserve placement costs is covered. The sharp cutoff is *within cycles with exactly two protected sites and these two specified objectives*, not across all graphs. The statement's mathematical correctness is separate from independent historical-priority validation; broad random-cluster and reserve-reliability theorems might imply related special cases that were not located in accessible literature.

## References

- Hof, J. and Flather, C. H. (1996). *Accounting for connectivity and spatial correlation in the optimal placement of wildlife habitat*. Public full text: https://research.fs.usda.gov/download/treesearch/23822.pdf
- Albers, H. J., Busby, G. M., Hamaide, B., Ando, A. W., and Polasky, S. (2016). *Spatially-Correlated Risk in Nature Reserve Site Selection*. PLOS ONE **11**(1), e0146023. Published January 20, 2016. https://doi.org/10.1371/journal.pone.0146023
- Published record: *Opposing optimal reserve layouts for reachable habitat and refuge connectivity on a cyclic landscape*. Public index record: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-opposing-optimal-reserve-layouts-for-reachable-habitat-and-refug--6a11d899bd76
