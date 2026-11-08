# Four vertices are sharp for shortening SIR epidemic duration by adding one contact

## Finding

In the continuous-time Markovian susceptible–infectious–recovered (SIR) epidemic on any finite, simple, undirected, unweighted contact graph, every infectious vertex recovers independently at rate one, and each infectious–susceptible edge transmits independently at rate \(\beta>0\). Initially exactly one designated vertex is infectious and all others are susceptible. Write \(T_G(s,\beta)\) for the expected time until no vertex remains infectious, including outbreaks ending after infecting only the seed.

**Sharp minimum theorem.** For every graph \(G\) with at most three vertices, every missing undirected edge \(e\), every seed \(s\), and every \(\beta>0\),
\[
T_{G+e}(s,\beta)\ge T_G(s,\beta).
\]
Four vertices suffice for a strict reverse inequality. On vertex set \(\{0,1,2,3\}\), take the four-cycle \(G\) with edge set \(\{02,03,12,13\}\), seed \(s=2\), and add its missing diagonal \(e=01\). At \(\beta=10\),
\[
T_G(2,10)=\frac{3961259}{1928619},\qquad
T_{G+01}(2,10)=\frac{1329351899}{648015984},
\]
so
\[
\boxed{T_{G+01}(2,10)-T_G(2,10)=-\frac{1631125}{648015984}<0.}
\]
At the same parameter, the expected *total number of distinct infected vertices*, including the initial seed, **increases** under the added edge by exactly
\[
\frac{8200}{586971}>0.
\]
Therefore four is the smallest network order at which adding a contact can simultaneously increase expected final epidemic size and decrease expected epidemic duration in this model. No uniqueness of four-vertex examples or transmission thresholds is claimed.

## Assumptions and scope

Vertices have states \(S,I,R\); transitions are only \(S\to I\) or \(I\to R\). Recoveries are independent exponential clocks of rate one, transmissions are independent edge-specific Poisson clocks of rate \(\beta\), with no importation, immunity loss, latent period, weights, self-loops, or simultaneous transitions. Edges are undirected and the same initial seed is retained before and after edge addition. Graphs in the lower bound may be disconnected. If recovery occurs at a common rate \(\gamma>0\), scale physical time by \(\gamma\): the counterexample is attained at transmission rate \(10\gamma\).

For a state \(z\in\{S,I,R\}^{V}\), let \(i(z)\) be the number of infectious vertices, let \(k_v(z)\) be the number of infectious neighbors of susceptible \(v\), and let \(q(z)=i(z)+\beta\sum_{v:z_v=S}k_v(z)\). For each state with an infectious vertex, denote by \(z^{v,R}\) the state after recovery at infectious \(v\), and by \(z^{v,I}\) the state after infection at susceptible \(v\). The expected additional epidemic duration \(h(z)\), and expected number \(f(z)\) of future first infections, are zero if \(i(z)=0\).

## Proof

For \(i(z)>0\), first-event conditioning gives the *exact* finite recursions
\[
 h(z)=\frac{1}{q(z)}+\frac{\sum_{v:z_v=I}h(z^{v,R})+\beta\sum_{v:z_v=S}k_v(z)h(z^{v,I})}{q(z)},
\]
\[
 f(z)=\frac{\sum_{v:z_v=I}f(z^{v,R})+\beta\sum_{v:z_v=S}k_v(z)[1+f(z^{v,I})]}{q(z)}.
\]
Every transition strictly increases the state rank \(\sum_v r(z_v)\), where \(r(S)=0,r(I)=1,r(R)=2\). Hence these are finite acyclic backward recursions, uniquely defining rational functions of \(\beta\). The total final outbreak size expectation is \(1+f(z_0)\).

For completeness, all graph–edge-addition–seed configurations on at most three vertices reduce by relabeling to the following table. Each entry is the **duration difference** \(T_{G+e}-T_G\), with \(b=\beta>0\). An isolated vertex denoted by \(2\) is included in the three-vertex initial graph. In rows with three vertices, the unlisted edges are absent.

| Initial edges | Added edge | Seed | Exact difference |
|---|---|---|---|
| \(\varnothing\) on 2 vertices | \(01\) | \(0\) | \(\frac{b}{2(b+1)}\) |
| \(\varnothing\) on 3 vertices | \(01\) | \(0\) | \(\frac{b}{2(b+1)}\) |
| \(\varnothing\) on 3 vertices | \(01\) | \(2\) | \(0\) |
| \(\{01\}\) | \(02\) | \(0\) | \(\frac{b(4b^2+13b+6)}{6(b+1)(b+2)(2b+1)}\) |
| \(\{01\}\) | \(02\) | \(1\) | \(\frac{b^2(2b+5)}{6(b+1)^2(b+2)}\) |
| \(\{01\}\) | \(02\) | \(2\) | \(\frac{b(5b^2+14b+6)}{6(b+1)^2(b+2)}\) |
| \(\{01,02\}\) | \(12\) | \(0\) | \(\frac{b^2(2b+5)}{3(b+1)^2(b+2)(2b+1)}\) |
| \(\{01,02\}\) | \(12\) | \(1\) | \(\frac{b(3b^2+8b+2)}{2(b+1)^2(b+2)(2b+1)}\) |

Every displayed denominator is positive and every numerator nonnegative for \(b>0\). These are all cases because an unlabeled graph with at most three vertices has at most three possible edges, and the only operation is insertion of one currently missing edge; the seed can lie in the old or new component. The last two rows handle inserting the third edge into a path. The two-vertex result also covers any two-vertex graph, and there is no missing edge when only one vertex is present. This proves the lower bound including disconnected cases, zeros, and arbitrarily large or small positive transmission rates.

For the four-vertex witness, apply the same finite recursion at the rational rate \(\beta=10\) to the specified edges and seed. Exact simplification yields the two displayed values of \(T\), their negative difference, and the positive difference in \(1+f\). Since the upper graph is obtained by adding just one edge to the lower graph, the example establishes sharpness. All rational identities are reproducible by `python verify.py`; an independent forward probability-flow calculation in that script confirms the witness values without using the backward expectation recurrence.

## Verification

`verify.py` (Python 3 with SymPy) enumerates **all 38 labeled** graph/missing-edge/seed triples of order two and three and verifies that the numerator and denominator of each exact difference have nonnegative polynomial coefficients and that each denominator has a positive constant term. The outcomes are 35 strictly positive differences and three identically zero differences. It also evaluates the four-vertex witness in exact rational arithmetic by two distinct methods: backward expectation recursion, and forward probability flow through every reachable finite SIR state. Both methods give the same epidemic-duration and final-size differences quoted above. This is exhaustive only for graph orders at most three; the four-vertex example is a witness, not a four-vertex census.

Run from the directory containing `verify.py`:

```bash
python verify.py
```

The assertions stop on any mismatch. The proof of the infinite parameter domain \(\beta>0\) for graphs of order at most three comes from the symbolic polynomial coefficient signs and the exact enumeration of all graph cases, not from numerical samples.

## Relationship to prior work

Sharkey, Kiss, Wilkinson and Simon (public preprint 2012) establish exact network SIR dynamics and exact pair closure on trees, and examine some special cyclic networks. Their theorem concerns moment equations, not comparison of expected absorption duration across a single added edge, and does not imply the present minimal counterexample. Holme (2013) studies epidemic extinction times versus transmission probability and network structure with **discrete-time** fixed-duration SIR simulations; this does not supply the Markovian four-vertex edge-insertion inequality or the exhaustive three-vertex bound. Holme (2017) derives exact small-network SIR calculations for influence, vaccination and sentinel detection and describes general absorption-chain methods; its reported comparisons are between initial-node objectives, not edge-inclusion monotonicity for unconditioned outbreak lifetime. The calculation method itself is not asserted to be new.

## Limitations

The four-vertex result establishes failure of edge-addition monotonicity at one positive rate and does not locate all reversal intervals, classify all graphs of order four, or establish a general stochastic ordering of outbreak times. It is not a claim about SIS dynamics, final-outbreak-size nonmonotonicity, conditional duration given a major outbreak, or interventions in empirical networks. Exact arithmetic verifies the stated mathematical model, but no independently performed research audit or historical priority certification is available. A previously published exact-duration table could conceivably contain the witness implicitly; only the source materials identified below were inspected for priority comparison.

## References

1. Sharkey, K. J., Kiss, I. Z., Wilkinson, R. R., and Simon, P. L. *Exact equations for SIR epidemics on tree graphs.* Public preprint, December 10, 2012, https://arxiv.org/abs/1212.2172 ; Bulletin of Mathematical Biology 77, 614–645 (2015), https://doi.org/10.1007/s11538-013-9923-5.
2. Holme, P. *Extinction Times of Epidemic Outbreaks in Networks.* PLOS ONE 8 (2013), e84429; published December 26, 2013, https://doi.org/10.1371/journal.pone.0084429.
3. Holme, P. *Three faces of node importance in network epidemiology: Exact results for small graphs.* Public preprint, August 22, 2017, https://arxiv.org/abs/1708.06456 ; Physical Review E 96, 062305 (2017), https://doi.org/10.1103/PhysRevE.96.062305.
