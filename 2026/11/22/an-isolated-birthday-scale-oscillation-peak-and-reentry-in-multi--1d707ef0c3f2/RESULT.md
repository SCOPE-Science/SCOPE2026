# An isolated birthday-scale oscillation peak and reentry in multicolor plurality

## Finding

Under deterministic synchronous plurality on every complete bipartite graph \(K_{m,n}\), a vertex adopts the unique most frequent color among its neighbors, if one exists, and otherwise retains its own color. For every alphabet of \(q\ge2\) colors and shore sizes \(m,n\ge1\), every configuration enters a fixed point or primitive two-cycle within two updates; the entire first-entry-time/period census below is exact. For independent uniform initial colors, the probability of eventual oscillation is
\[
\mathbb P(\mathrm{period}=2)=\left(1-\frac1q\right)\frac{U_{m,q}}{q^m}\frac{U_{n,q}}{q^n},
\]
where \(U_{r,q}\) counts length-\(r\) words with a unique most frequent color.

The oscillation probability exhibits a nonmonotone palette-size hierarchy. Let \(m\to\infty\), \(n/m\to\rho\in(0,\infty)\). At the birthday scale \(q/m^2\to c\in(0,\infty)\),
\[
\mathbb P(\mathrm{period}=2)\longrightarrow H_\rho(c)=\frac{\rho^2}{4c^2}\exp\!\left(-\frac{1+\rho^2}{2c}\right).
\]
This profile has the unique maximum at \(c=(1+\rho^2)/4\), with value \(4e^{-2}\rho^2/(1+\rho^2)^2\); the balanced case \(\rho=1\) attains the largest possible *birthday-scale* peak \(e^{-2}\), at \(q\sim m^2/2\). Oscillation vanishes when \(q\gg m^2\), and also when \(m^{3/2}\ll q\ll m^2\). In contrast, at each fixed \(q\ge2\) the oscillation probability tends to \(1-1/q\). Thus descending from exceptionally large palettes to fixed palettes produces a birthday-scale oscillation peak, a suppression valley, and renewed oscillation.

## Assumptions and scope

The graph is the simple open-neighborhood complete bipartite graph \(K_{m,n}\); all vertices update simultaneously. The alphabet is a set of \(q\) labelled colors. A neighborhood has a *unique winner* if exactly one color achieves its maximum occurrence (including the zero-count colors in the comparison); if the maximum ties, the vertex remains its current color, whether or not that color participates in the tie. There is no random tie-break at update time. The initial colors are independent and uniform only for probabilistic statements; the exact deterministic census includes every labelled configuration.

Write \(U_m=U_{m,q}\), \(U_n=U_{n,q}\), \(B_m=q^m-U_m\), and \(B_n=q^n-U_n\). The unique-winner count is explicitly
\[
U_{r,q}=q\,r!\,[z^r]\sum_{h=1}^{r}\frac{z^h}{h!}\left(\sum_{j=0}^{h-1}\frac{z^j}{j!}\right)^{q-1}.
\]
First periodic-entry time \(t\) is the least nonnegative time for which the state at time \(t\) belongs to its eventual periodic orbit. The least period is \(p\). The full census is:

| \((t,p)\) | Number of labelled configurations |
|---|---|
| \((0,1)\) | \(B_mB_n+q\) |
| \((0,2)\) | \(q(q-1)\) |
| \((1,1)\) | \(U_mU_n/q-q+q(B_m+B_n)\) |
| \((1,2)\) | \((q-1)U_mU_n/q-q(q-1)\) |
| \((2,1)\) | \((U_m-q)B_n+(U_n-q)B_m\) |

All remaining classes are empty. The displayed five integers sum to \(q^{m+n}\). In particular \(F^4=F^2\) for the update map \(F\). A state with different monochromatic shores exhibits a genuine two-cycle from time zero, showing that period two is possible.

## Proof

**Dynamics and exact census.** Let \(A\) and \(B\) be the words on the two shores, and let \(w(A)\), \(w(B)\) be their unique winning colors when they exist. Because each vertex on one shore sees the same opposing word, a unique winner on that opposing shore overwrites *every* vertex on its own shore. If neither word has a unique winner, the state is fixed. If both winners exist, after one step the shores are monochromatic in colors \(w(B)\) and \(w(A)\). The resulting state is fixed if the winners agree and otherwise alternates between the two monochromatic shores forever. If exactly one winner exists, the first step makes the opposing shore monochromatic, leaving the other shore unchanged; the second step makes both shores monochromatic in the winner's color. No other recurrence is possible.

The \(q\) monochromatic uniform configurations and \(q(q-1)\) opposite-monochrome configurations account for the initial fixed and two-periodic states among configurations having two winners. Among words with unique winners, color symmetry gives exactly \(U_r/q\) words per winner color. Thus two winners agree on \(U_mU_n/q\) pairs, and disagree on \((q-1)U_mU_n/q\) pairs. Of these, respectively \(q\) and \(q(q-1)\) are already periodic at update zero. If exactly one winner exists, there are \(U_mB_n+U_nB_m\) configurations; exactly \(qB_n+qB_m\) of these already have a monochromatic winning shore and become fixed at update one, and the remainder become fixed at update two. Both ties account for \(B_mB_n\) additional initial fixed points. Collecting yields the table. A unique-winner word count is obtained by designating the winning color, choosing its occupancy \(h\), then restricting the \(q-1\) other color occupancies to at most \(h-1\), yielding the stated exponential-generating coefficient.

**Critical birthday limit.** For a uniform word of length \(r\) over \(q\) colors, let \(C\) count pairs of positions sharing a color. For \(q\asymp r^2\), its factorial moments converge to those of a Poisson variable with mean \(\lambda=r(r-1)/(2q)\to\lambda_\infty\); this can be seen directly by separating disjoint-index pair selections from overlapping connected collision diagrams, which have vanishing expected counts. The probability of a triple is at most \(\binom r3/q^2\to0\). With no triple, exactly one pair collision is precisely the event of a unique winning color; two or more distinct doubletons cause a tie for maximum. Consequently \(U_{r,q}/q^r\to\lambda_\infty e^{-\lambda_\infty}\). This also follows without a general Poisson approximation by using the exact one-pair probability
\[
\binom r2\frac{q(q-1)_{r-2}}{q^r}
\]
and the triple bound, where \((q-1)_{r-2}\) is a falling factorial. Applying the formula separately on the two shores yields limiting single-winner probabilities \(a=(2c)^{-1}e^{-1/(2c)}\) and \(b=(\rho^2/(2c))e^{-\rho^2/(2c)}\). Conditional on the winners existing, their colors are independent and uniform, so their probability of disagreement is exactly \(1-1/q\to1\); multiplication gives \(H_\rho(c)\). Differentiating its logarithm shows its unique critical point, a maximum, occurs at \(c=(1+\rho^2)/4\); the inequality \(4\rho^2/(1+\rho^2)^2\le1\) has equality precisely at \(\rho=1\).

**Suppression and reentry.** When \(q\gg r^2\), the union bound gives \(\mathbb P(C>0)\le\binom r2/q\to0\), so a unique plurality is absent with high probability. If \(r^{3/2}\ll q\ll r^2\), then \(\mathbb EC=\binom r2/q\to\infty\) and \(\operatorname{Var}(C)=\binom r2(1/q)(1-1/q)\); pair-collision indicators are pairwise independent, even for pairs sharing one position. Chebyshev implies \(C\ge2\) with probability tending to one, whereas the triple bound still tends to zero, so the maximum frequency is two attained by at least two colors and \(U_{r,q}/q^r\to0\). The assertions for two shores follow because \(n/m\) stays bounded above and below. For a fixed palette \(q\ge2\), the probability that two prescribed color counts coincide is \(O_q(r^{-1/2})\): condition on the number of samples using either of those two colors (which is binomial with a positive linear mean), then use the central-binomial bound for their equal split. A union bound over the finite \(\binom q2\) color pairs shows \(U_{r,q}/q^r\to1\), hence the final fixed-palette oscillation limit.

**Limiting first-entry classes.** At the birthday scale let \(a=(2c)^{-1}e^{-1/(2c)}\) and \(b=(\rho^2/(2c))e^{-\rho^2/(2c)}\). Dividing the exact five entries by \(q^{m+n}\), the limits of \((t,p)=(0,1),(1,2),(2,1)\) respectively are \((1-a)(1-b)\), \(ab\), and \(a(1-b)+b(1-a)\). The other two classes have limiting probability zero. The three values sum to one.

## Verification

The included `check_plurality.py` independently enumerates the entire state space for every balanced pair of shore sizes \(1,2,3\) and each of \(2,3,4,5\) colors, and compares the observed first-entry/least-period distribution with the displayed formulas. The independent `check_unbalanced.py` enumerates 27 combinations of \(2,3,4\) colors and unequal or equal shores of sizes \(1,2,3\), independently evaluating the update map and exact populations. The separate `check_occupancy.py` checks the strict-plurality coefficient formula by an exact integer occupancy recurrence against brute force for all alphabets \(2\) through \(6\) and word lengths \(1\) through \(6\), and compares single-collision probabilities with the birthday limit for larger input sizes. Reproducible commands: `python3 check_plurality.py`, `python3 check_unbalanced.py`, `python3 check_occupancy.py`. Their outputs were checked against the included logs. The infinite-size claims follow from the analytic proof, not from these finite enumerations.

## Relationship to prior work

Binary-majority dynamics and its period-two phenomena are classical (Goles–Olivos; Tamuz–Tessler), but two opinions do not yield the growing-palette collision transition. Existing multicolor-majority studies commonly use different tie rules or random graphs (Chellig–Fountoulakis), while later research distinguishes several nonbinary majority rule variants (2025 deterministic three-opinion review). The two-shore swap reduction is elementary but by itself does not imply the exact labelled five-class first-entry census or the nonmonotone birthday-scale oscillation law, including the optimal balanced peak and fixed-palette reentry. The accessible research record checked for equivalent identities and stronger covering results revealed no such direct implication. Historical priority is not independently established.

## Limitations

The state-transition rule *retains the incumbent on every nonunique neighborhood plurality*; other tie-breaking policies can change all conclusions. The birthday-scale asymptotic assumes a positive finite shore-size ratio. The low-palette reentry statement treats each fixed integer \(q\), not the entire intermediate range between constant palettes and the sparse-collision valley. Neither a uniform relaxation-time theorem on arbitrary graphs nor an exact global maximizer over all palette values is asserted. The finite scripts corroborate definitions and formulas but do not certify the infinite proof; independent external validation has not been performed.

## References

- O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, first arXiv public version 2013-07-15, https://arxiv.org/abs/1307.4035 .
- N. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of Deterministic Majority Process*, first arXiv version 2015-08-14, https://arxiv.org/abs/1508.03519 .
- C. Chellig and N. Fountoulakis, *Majority dynamics on random graphs: the multiple states case*, first arXiv version 2023-11-15, https://arxiv.org/abs/2311.09078 .
- *Three Majority-Based Deterministic Dynamics for Three Opinions*, AppliedMath 2025, 5(4), 147, https://doi.org/10.3390/appliedmath5040147 .
