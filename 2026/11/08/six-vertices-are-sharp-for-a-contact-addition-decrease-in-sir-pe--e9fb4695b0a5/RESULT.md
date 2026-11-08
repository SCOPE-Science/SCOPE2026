# Six vertices are sharp for a contact-addition decrease in SIR peak-overload risk

## Finding

Let \(G=(V,E)\) be a connected finite simple undirected unweighted graph, let \(s\in V\), and run the homogeneous continuous-time susceptible–infectious–removed (SIR) process from the single infectious vertex \(s\), with every other vertex susceptible. Each infectious--susceptible edge transmits at rate \(\beta>0\), every infectious vertex recovers at rate \(1\), and recovered vertices never become susceptible again. Write
\[
R_k(G,s;\beta)=\Pr_{G,s}\!\left(\max_{t\ge0}|I_t|\ge k\right),\qquad 2\le k\le |V|.
\]

**Theorem (sharp contact-addition boundary).** For every connected \(G\) with \(|V|\le5\), every missing edge \(e\) on its vertex set, every seed \(s\), every admissible \(k\), and every \(\beta>0\),
\[
R_k(G+e,s;\beta)\ge R_k(G,s;\beta).
\]
The vertex bound is sharp. On \(V=\{0,1,2,3,4,5\}\), take
\[
E=\{\{0,4\},\{0,5\},\{1,3\},\{2,3\},\{3,4\}\},
\quad e=\{1,2\},\quad s=1,\quad k=6,\quad\beta=50.
\]
Then
\[
R_6(G,1;50)=\frac{14289062500}{18273931533},\qquad
R_6(G+e,1;50)=\frac{1946796875000}{2491078937193},
\]
so
\[
R_6(G,1;50)-R_6(G+e,1;50)
=\frac{24352320312500}{56704429847324259}>0.
\]
This is a difference of approximately \(0.00042946063258\), not a claim that epidemic peak probability decreases at every transmission rate.

## Assumptions and scope

Graphs are finite, connected, undirected, unweighted and loopless; only one missing undirected edge is added. The initially infectious vertex stays fixed when the edge is added. Infection and recovery clocks are independent exponential clocks with the rates stated above. A *peak overload* event refers to the maximum **within a single realized trajectory**, not the peak of the mean prevalence curve. The bound is uniform over all positive transmission rates and all peak thresholds on at most five vertices. The witness uses only a single fixed transmission rate and the full-population peak threshold.

## Proof

For disjoint susceptible and infectious sets \(S,I\subseteq V\), write \(F_G(S,I)\) for the probability of ever reaching at least \(k\) simultaneous infectious vertices from that state; the remaining vertices are permanently removed. Put \(d_I(v)=|N_G(v)\cap I|\) and \(T=|I|+\beta\sum_{v\in S}d_I(v)\). First-event conditioning gives
\[
F_G(S,I)=\begin{cases}
1,&|I|\ge k,\\
0,&I=\varnothing,\\
\displaystyle\frac{\sum_{u\in I}F_G(S,I\setminus\{u\})+\beta\sum_{v\in S}d_I(v)F_G(S\setminus\{v\},I\cup\{v\})}{T},&0<|I|<k.
\end{cases}
\]
The recurrence is well-founded because \(2|S|+|I|\) decreases strictly at every event; \(T>0\) whenever the recursive branch is used. Thus all probabilities are rational functions of \(\beta\), and symbolic computations below are exact identities.

To prove the universal small-graph assertion, enumerate all labeled simple graphs with \(n=2,3,4,5\), retain connected ones, and quotient by every permutation of the vertex labels using the minimum adjacency-bitmask representative. The resulting numbers of connected isomorphism classes are \(1,2,6,21\), respectively. For every representative and every missing edge, seed and threshold, calculate \(R_k(G+e,s;\beta)-R_k(G,s;\beta)\) from the recurrence, reduce it by exact polynomial cancellation, and write its numerator and denominator as integer polynomials in \(\beta\). For every nonzero difference **both polynomials have nonnegative coefficients and are strictly positive at \(\beta=1\)**. Therefore the difference is strictly positive for all \(\beta>0\); the remaining differences vanish identically. The verifier covers **1,738** such graph--edge--seed--threshold comparisons through five vertices, including **1,475** strict symbolic inequalities and **263** identities. The maximum numerator or denominator degree encountered is \(15\). For one vertex, and for connected graphs on two vertices, no missing edge exists. The self-contained enumeration and rational recursions are implemented in `verify_peak.py`; run its four disjoint small-graph batches as instructed below.

For the six-vertex witness, the event \(\max_t|I_t|=6\) occurs exactly when all six vertices become infected before the first recovery. On any infected subset \(J\), the probability \(P_G(J)\) of that event therefore satisfies the simpler exact recurrence
\[
P_G(V)=1,\qquad P_G(J)=\frac{\beta\sum_{v\notin J}|N_G(v)\cap J|P_G(J\cup\{v\})}{|J|+\beta\sum_{v\notin J}|N_G(v)\cap J|},\quad\varnothing\ne J\subsetneq V.
\]
Using \(J=\{1\}\) and \(\beta=50\) yields the two displayed reduced fractions and their strictly positive difference. This subset-only calculation, implemented separately in `verify_peak_forward.py`, independently reproduces the rational values from the full SIR state recursion.

## Verification

Execute with Python 3 and SymPy installed:

```text
python verify_peak.py --start 0 --stop 5
python verify_peak.py --start 5 --stop 10
python verify_peak.py --start 10 --stop 15
python verify_peak.py --start 15 --stop 21
python verify_peak.py --witness
python verify_peak_forward.py
```

All commands were run against the included programs. Each symbolic batch printed `BATCH_PASS`; the summed comparison count was \(1738\). Both independent witness calculations reproduced the displayed exact rational difference. The finite computations are exhaustive only for the explicitly enumerated connected graphs of order at most five; no numerical sampling is used to justify an all-rate sign claim.

## Relationship to prior work

Van Mieghem (2014) develops exact equations for Markovian SIR and SIS on networks and studies the **maximum of mean prevalence**, not the hitting probability of a realized peak. Economou, Gómez-Corral and López-García (2015) develop a full maximum-infectives distribution in an **SIS** model and discuss SIR as a possible extension; its recovery mechanism permits reinfection and does not establish the current SIR edge-addition bound. Holme (2013) studies epidemic extinction times in a discrete-time SIR model. Holme (2017) gives exact small-graph SIR calculations for mean final size, vaccination and sentinel timing, not realized peak-overload probability under edge addition. These works motivate exact network-level comparisons without implying the present sharp six-vertex threshold. The question is also distinct from single-seed **ranking** and mean-extinction-time edge-addition questions.

## Limitations

This result concerns an idealized homogeneous finite SIR model; it does not cover heterogeneous rates, directed or weighted contacts, several initial infectives, or nonexponential infectious periods. The witness effect is small at the chosen rate, but the minimum graph order is exact. The work makes no empirical public-health prediction. The literature comparison is based on retrieved material and may miss older tables or differently named equivalent results. Independent external validation has not been performed.

## References

1. P. Van Mieghem, *Exact Markovian SIR and SIS epidemics on networks and an upper bound for the epidemic threshold*, arXiv:1402.1731, first submitted 2014-02-07, https://arxiv.org/abs/1402.1731 .
2. A. Economou, A. Gómez-Corral and M. López-García, *A stochastic SIS epidemic model with heterogeneous contacts*, Physica A 421 (2015), 78–97, https://doi.org/10.1016/j.physa.2014.10.054 ; lawful accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/90144/ .
3. P. Holme, *Extinction times of epidemic outbreaks in networks*, PLOS ONE 8 (2013), e84429, https://doi.org/10.1371/journal.pone.0084429 ; arXiv:1310.3932.
4. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, 2017, arXiv:1708.06456, https://arxiv.org/abs/1708.06456 .
