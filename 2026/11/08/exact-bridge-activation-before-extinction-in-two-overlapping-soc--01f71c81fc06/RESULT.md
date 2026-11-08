# Exact bridge activation before extinction in two overlapping social hyperedges

## Finding

For a two-group continuous-time threshold contagion with all of the first group initially active, the probability that the second group first activates before extinction has an explicit finite sum of products. In addition, as the first group's internal reactivation rate \(\alpha\) diverges, the failure probability has the sharp universal leading term

\[
1-P=\frac{a!\,\delta^a}{\beta\,\alpha^{a-1}}\left(1+O(\alpha^{-1})\right).
\]

Remarkably, for fixed group size \(a\), recovery rate \(\delta\) and second-group activation rate \(\beta\), the leading constant is independent of the overlap size and the second group's critical-mass threshold, provided that the overlap reaches that threshold.

Precisely, let \(a\ge3\), \(b\ge3\), \(1\le c<\min(a,b)\), and \(1\le k\le b\) be integers. Put \(r=c-k+1\). If \(c<k\), then \(P=0\) for all positive rates. If \(c\ge k\), set

\[
\begin{aligned}
 v_i&=(a-i+1)\delta\quad(1\le i\le a),\\
 w_j&=\frac{\binom{j-1}{r-1}\binom{a-j}{c-r}}{\binom ac}
 \quad(r\le j\le a-k+1),\\
 U_j(s)&=\prod_{i=1}^{j}\frac{v_i}{v_i+s},\\
 V_j(s)&=\prod_{i=j+1}^{a}\frac{v_i}{v_i+s},
\end{aligned}
\]

where an empty product is one. Define

\[
 S=\frac{\beta}{\alpha+\beta}
   \sum_{j=r}^{a-k+1}w_j\bigl(1-U_j(\alpha+\beta)\bigr),
 \qquad
 E=\sum_{j=r}^{a-k+1}w_jU_j(\alpha+\beta)V_j(\alpha).
\]

Then \(S,E>0\), and the exact bridge-activation probability is

\[
\boxed{P=\frac{S}{S+E}}.
\]

This quantity is independent of the number \(b-c\) of initially inactive, private second-group members, when \(\beta\) and \(k\) are held fixed. For \(a=4\), \(b=3\), \(c=k=2\), \(\delta=1\), \(\alpha=3\), and \(\beta=2\), it equals \(P=720/767\).

## Assumptions and scope

There are exactly two different hyperedges \(A,B\) with \(|A|=a\), \(|B|=b\), and \(|A\cap B|=c\), on the vertex set \(A\cup B\). Each vertex has a binary active/inactive state. Initially all vertices of \(A\) are active, and all of \(B\setminus A\) are inactive. Independently, each active vertex becomes inactive at rate \(\delta>0\). If at least one vertex of \(A\) is active, the group \(A\) activates all its currently inactive vertices at Poisson rate \(\alpha>0\). If at least \(k\) vertices of \(B\) are active, group \(B\) activates all its inactive vertices simultaneously at Poisson rate \(\beta>0\). Group clocks are memoryless and independent; clock firings that cause no state change are permitted. There are no other spontaneous activations, hyperedges, or external seeds.

The event of interest is an actual \(B\)-clock firing before the all-inactive absorbing state. The first such firing necessarily activates at least one vertex, because \(B\setminus A\ne\varnothing\) is initially inactive and remains so until that firing. The two group thresholds and rates may differ. Thus this statement uses the general per-hyperedge threshold rules, not the particular uniform-threshold, single-scale choices adopted in some numerical experiments in the motivating literature.

## Proof

If \(c<k\), then before a \(B\)-event no vertex of \(B\setminus A\) can activate, and at most \(c\) members of \(B\) can be active. Hence \(B\)'s threshold never holds, and \(P=0\).

Suppose \(c\ge k\). Start an excursion immediately after all members of \(A\) have been activated. Temporarily suppress any \(A\)- or \(B\)-firing and assign independent exponential lifetimes of rate \(\delta\) to the \(a\) active members of \(A\). Let \(T_B\) be the time when the number of active overlap members first falls below \(k\), and let \(T_A\) be the time when the final member of \(A\) dies. Because \(k\ge1\), we have \(0<T_B\le T_A\) almost surely.

Let \(X\sim\mathrm{Exp}(\alpha)\) and \(Y\sim\mathrm{Exp}(\beta)\) be independent clocks. Prior to \(T_B\), both are enabled, while after \(T_B\) only the \(A\)-clock can be enabled. A \(B\)-firing before an \(A\)-firing and before \(T_B\) is a success in the current excursion, with probability

\[
\begin{aligned}
 S&=\Pr\{Y< X,\ Y<T_B\}
   =\mathbb E\int_0^{T_B}\beta e^{-(\alpha+\beta)t}\,dt\\
  &=\frac{\beta}{\alpha+\beta}
       \left(1-\mathbb E[e^{-(\alpha+\beta)T_B}]\right).
\end{aligned}
\]

The excursion instead becomes extinct before either group event precisely when there is no \(A\)-firing before \(T_A\) and no \(B\)-firing while \(B\) is eligible. Therefore its extinction probability is

\[
 E=\mathbb E\left[e^{-\alpha T_A-\beta T_B}\right].
\]

Every other excursion ends with an \(A\)-firing while at least one \(A\)-vertex is active. Such a firing restores the original all-active configuration on \(A\), and leaves \(B\setminus A\) inactive. Exponential memorylessness makes the next excursion independent with the same success and extinction probabilities. Therefore, writing \(R=1-S-E\), the renewal equation is \(P=S+RP\), and hence \(P=S/(S+E)\). Positivity of both probabilities follows from positive finite clocks and lifetimes.

It remains to evaluate the two expectations. The order of the \(a\) individual deaths is a uniform permutation, independent of the successive waiting times between deaths. Let \(J\) be the rank of the \(r=c-k+1\)-st death among the \(c\) overlap members. The number of ways for \(J=j\) is \(\binom{j-1}{r-1}\binom{a-j}{c-r}\), out of the \(\binom ac\) choices of overlap death ranks, so \(\Pr(J=j)=w_j\). The possible ranks are \(r\le j\le a-k+1\).

The successive waiting times \(D_i\) for deaths \(i=1,\ldots,a\) are independent exponentials with rates \(v_i=(a-i+1)\delta\). Conditional on \(J=j\),

\[
 T_B=D_1+\cdots+D_j,\qquad T_A=D_1+\cdots+D_a.
\]

Thus, using independence and the Laplace transform \(\mathbb E[e^{-sD_i}]=v_i/(v_i+s)\),

\[
 \mathbb E[e^{-(\alpha+\beta)T_B}\mid J=j]=U_j(\alpha+\beta),
\]

and

\[
 \mathbb E[e^{-\alpha T_A-\beta T_B}\mid J=j]
 =U_j(\alpha+\beta)V_j(\alpha).
\]

Averaging over \(J\) yields the stated finite sums. No limit or simulation is needed for this equality.

Finally fix \(a,c,k,\beta,\delta\) and let \(\alpha\to\infty\). Since \(j\ge1\) in every term and \(\sum_jw_j=1\), the displayed finite sum gives

\[
 S=\frac{\beta}{\alpha}(1+O(\alpha^{-1})).
\]

For every allowed \(j\), the product \(U_j(\alpha+\beta)V_j(\alpha)\) has all \(a\) factors with denominator asymptotic to \(\alpha\), while its numerator is

\[
 \prod_{i=1}^av_i=a!\,\delta^a.
\]

Consequently \(E=a!\,\delta^a\alpha^{-a}(1+O(\alpha^{-1}))\), uniformly over the finite set of ranks. Because \(1-P=E/(S+E)\), the asserted sharp strong-reinforcement law follows for every \(a\ge3\). The cancellation of all \(c,k\)-dependence in the leading term is exact.

## Verification

Run `python3 verify.py` using only the Python standard library. The script computes the finite formula with `fractions.Fraction`, then independently solves the absorbing-state harmonic equations for the full exact Markov chain. It performs 165 rational comparisons using a compressed active-count chain and 56 additional rational comparisons using all microstates, including tests with \(c<k\). It also prints rational large-\(\alpha\) rescalings that approach the analytically proved leading coefficient and checks the displayed concrete example. The proof above, not these finite tests, establishes the statement for arbitrary allowed sizes and all positive real rates.

## Relationship to prior work

De Arruda, Petri, Rodriguez, and Moreno introduced and investigated the simultaneous whole-hyperedge threshold-activation mechanism and demonstrated how hyperedge intersections/bridges influence metastability and intermittency. Their published Sections 'Model definition', 'Multistability', 'Methods', and 'Exact equations for the hyperblob' analyze global dynamics, approximate descriptions, and a one-hyperedge homogeneous reduction, rather than this exact two-overlap first-event probability. Their paper is the direct motivating model, not a claim of novelty for the stochastic rules.

St-Onge and collaborators studied stochastic contagion in heterogeneous hypergraphs using nodewise group infection events, approximate master equations, phase transitions, and influential seeds. Their documented Gillespie transition activates one susceptible member, not an entire eligible group at once. Their results therefore do not imply the formula here. Higham and de Kergorlay established spectral/extinction results for nodewise SIS infection rates, also using a different mechanism and a different observable. The present result isolates the event that a second whole-group clock fires before the finite absorbing state and gives a finite sum and a sharp asymptotic law. A fully general absorbing Markov-chain computation is possible in principle but does not furnish these explicit formulas or the overlap-independent leading coefficient without further analysis.

## Limitations

The result is for exactly two hyperedges, fixed heterogeneous rates/thresholds, initially fully active source group, source threshold one, no external activation, and a first successful second-group firing. It does not classify steady states, later cross-group cascades, extinction times, or transition phases on arbitrary hypergraphs. The strong-reinforcement asymptotic holds at fixed finite group sizes and fixed positive \(\beta,\delta\); it is not uniform as group sizes or those rates vary. The motivating article's supplementary material was not fully accessible during the literature comparison, and the absence of another independent equivalent in the wider literature cannot be certified.

## References

1. G. F. de Arruda, G. Petri, P. M. Rodriguez, and Y. Moreno, *Multistability, intermittency, and hybrid transitions in social contagion models on hypergraphs*, first public preprint 2021-12-08, [arXiv:2112.04273](https://arxiv.org/abs/2112.04273); *Nature Communications* **14**, 1375 (2023), [doi:10.1038/s41467-023-37118-3](https://doi.org/10.1038/s41467-023-37118-3), [full open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10011415/).
2. G. St-Onge et al., *Influential groups for seeding and sustaining nonlinear contagion in heterogeneous hypergraphs*, [arXiv:2105.07092](https://arxiv.org/abs/2105.07092), *Communications Physics* **5**, 25 (2022), [doi:10.1038/s42005-021-00788-w](https://doi.org/10.1038/s42005-021-00788-w).
3. D. J. Higham and H.-L. de Kergorlay, *Epidemics on hypergraphs: spectral thresholds for extinction*, [arXiv:2103.07319](https://arxiv.org/abs/2103.07319), *Proceedings of the Royal Society A* **477**, 20210232 (2021), [doi:10.1098/rspa.2021.0232](https://doi.org/10.1098/rspa.2021.0232).
