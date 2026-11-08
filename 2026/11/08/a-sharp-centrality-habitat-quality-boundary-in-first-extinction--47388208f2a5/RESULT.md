# A sharp centrality–habitat-quality boundary in first extinction of competing colonizers

## Finding

Let two ecologically symmetric species, \(A\) and \(B\), compete for three sites forming the path \(L-C-R\). Initially each species occupies one site and the third site is vacant. Every occupied site becomes vacant at rate \(1\) if it is an endpoint and at rate \(\mu>0\) if it is the center. Each occupied site sends propagules independently to each adjacent vacant site at rate \(c>0\). A propagule arriving at an occupied site has no effect. There is no immigration or spontaneous colonization. Let success mean that species \(B\) becomes globally extinct *before* species \(A\), so that \(A\) is the last species present, although it too eventually becomes extinct.

Up to endpoint reflection, exactly three initial allocations are possible:

- \(C\): \(A\) occupies the center and \(B\) an endpoint;
- \(E\): \(A\) occupies an endpoint and \(B\) the center;
- \(S\): the two species occupy opposite endpoints.

Their exact success probabilities are

\[
P_C=\frac{(c+2)(\mu+2)}{2(\mu+1)(c+\mu+2)},\qquad
P_E=1-P_C,\qquad P_S=\frac12.
\]

Consequently, for \(0<\mu\le 1\), the strict ranking is \(P_C>P_S>P_E\) for every \(c>0\). For \(\mu>1\), define the positive threshold \(c_*(\mu)=(\mu-1)(\mu+2)\). Then

\[
\begin{array}{ll}
0<c<c_*(\mu): &P_E>P_S>P_C,\\
c=c_*(\mu): &P_E=P_S=P_C=\frac12,\\
c>c_*(\mu): &P_C>P_S>P_E.
\end{array}
\]

Thus there is exactly one central-versus-peripheral winner switch as colonization varies whenever the center has larger mortality than the endpoints. Equivalently, at fixed \(c>0\) the center is favored precisely when \(\mu<\bigl(\sqrt{9+4c}-1\bigr)/2\), with equality a three-way tie.

## Assumptions and scope

This is a continuous-time Markov chain on \(\{0,A,B\}^3\), with an empty site written \(0\). Each directed occupied-to-vacant edge causes a birth at rate \(c\), and site-specific mortality is independent of species identity. When the center is empty between opposite species, its two incoming colonization clocks each have rate \(c\). Rate units are normalized so that endpoint mortality is \(1\). Both initial species are represented by exactly one occupied patch, and the initial third patch is empty. All statements quantify over every real \(c>0\) and \(\mu>0\).

Once a species disappears it can never return. From every nonempty configuration there is a positive probability of enough death events, with no successful births, to reach the completely empty state in a fixed time interval. Because the state space is finite, extinction of both species occurs almost surely. Independent exponential clocks exclude simultaneous final species deaths almost surely. The first-species-extinction event is therefore well-defined with total probability one.

## Proof

By interchangeability of the two species, swapping their labels exchanges success and failure. Endpoint reflection gives \(P_E=1-P_C\). For the separated-endpoints allocation, swapping the species and reflecting the path leave the unlabeled geometry unchanged, so \(P_S=1-P_S\), hence \(P_S=1/2\).

Write \(x=P_C\). Starting from the representative configuration \((B,A,0)\), let \(u\) be the probability of \(A\)'s success after the only possible successful colonization of the vacant right endpoint, which leads to \((B,A,A)\). First-event conditioning gives

\[
(\mu+1+c)x=1+cu.
\tag{1}
\]

Indeed, death of the central \(A\) at rate \(\mu\) is a failure, death of the endpoint \(B\) at rate \(1\) is a success, and birth into the other endpoint at rate \(c\) leads to \(u\). From \((B,A,A)\), the last \(B\) dies at rate \(1\) (success), the right-hand \(A\) dies at rate \(1\) (returning to \(x\)), or the central \(A\) dies at rate \(\mu\). In the last case the species occupy opposite endpoints, giving success probability \(1/2\). Therefore

\[
(\mu+2)u=1+x+\frac{\mu}{2}.
\tag{2}
\]

These are exhaustive possible state changes before the first species extinction. Eliminating \(u\) yields

\[
\begin{aligned}
[(\mu+1+c)(\mu+2)-c]x
&=(\mu+2)\left(1+\frac{c}{2}\right),\\
(\mu+1)(c+\mu+2)x
&=\frac{(\mu+2)(c+2)}{2},
\end{aligned}
\]

proving the claimed exact formula. In particular,

\[
P_C-\frac12
=\frac{c-(\mu-1)(\mu+2)}{2(\mu+1)(c+\mu+2)}.
\tag{3}
\]

The denominator is strictly positive on the entire stated domain. If \(\mu\le1\), its numerator is positive for every \(c>0\). If \(\mu>1\), its numerator has exactly one zero in \(c>0\), at \(c_*(\mu)=(\mu-1)(\mu+2)\), and changes sign from negative to positive there. Since \(P_E=1-P_C\) and \(P_S=1/2\), equation (3) establishes the complete strict orderings and all tie cases.

Two further exact sensitivity identities are

\[
\frac{\partial P_C}{\partial c}=
\frac{\mu(\mu+2)}{2(\mu+1)(c+\mu+2)^2}>0,
\qquad
\frac{\partial P_C}{\partial\mu}=
-\frac{(c+2)(c+\mu^2+4\mu+4)}{2(\mu+1)^2(c+\mu+2)^2}<0.
\]

Thus the location switch is not an artifact of multiple branches or disconnected parameter regimes.

## Verification

The accompanying `checker.py` independently constructs the full set of \(12\) states in which both types are present, generates all death and occupied-to-empty colonization rates directly from the graph, and solves the absorbing first-extinction equations with exact rational Gaussian elimination. The full-state solver makes no use of the two-equation reduction in the proof. It verifies all three formulas and the predicted phase-sign conditions at \(81\) rational parameter pairs, plus three exact boundary examples. Run it with `python3 checker.py` using only the Python standard library.

For example, at \(\mu=2\) the threshold is \(c_*=4\). At \(c=1\), the respective values \((P_C,P_S,P_E)=(2/5,1/2,3/5)\) favor an endpoint for species \(A\); at \(c=4\) all three values are \(1/2\); and at \(c=6\), they are \((8/15,1/2,7/15)\), favoring the center. These finite checks corroborate, but do not substitute for, the all-parameter proof from equations (1)–(3).

## Relationship to prior work

The neutral multitype contact process was studied by Neuhauser [1], and spatial competition and coexistence on infinite lattices are treated by Chan, Durrett and Lanchier [2], Valesin [3], and Mountford, Barrios Pantoja and Valesin [4]. The model here uses the same occupied-site competition rule but a finite three-site landscape and site-dependent, species-independent mortality. The proved event is the *order of first global type extinction*, not infinite-time coexistence on an infinite lattice or a stationary distribution. None of the inspected theorem statements from these sources specifies the above three-placement first-extinction probabilities or the curve \(c=(\mu-1)(\mu+2)\). This is a comparison of mathematical implications and model assumptions, not a claim of exhaustive historical priority.

## Limitations

The exact classification is for three sites, two exchangeable colonizers with equal per-edge birth rates, single initial seeds, local independent exponential deaths, and mutually exclusive patch occupation. It says nothing about equilibrium community diversity, longer graphs, demographic memory, coexistence with immigration, competition where offspring can displace occupied competitors, or populations in which multiple individuals occupy a patch. Both types ultimately disappear from this closed finite system. The threshold predicts the probability of winning the transient first-extinction race, not long-run coexistence or a field intervention effect. Priority remains subject to independent literature review, especially older finite-state ecological competition studies not available in full text.

## References

1. C. Neuhauser, *Ergodic theorems for the multitype contact process*, Probability Theory and Related Fields 91 (1992), 467–506. DOI: https://doi.org/10.1007/BF01192067.
2. B. Chan, R. Durrett, N. Lanchier, *Coexistence for a multitype contact process with seasons*, Annals of Applied Probability 19 (2009), 1921–1943. First accessible preprint dated 2009-10-21: https://arxiv.org/abs/0910.4014; DOI: https://doi.org/10.1214/09-AAP599.
3. D. Valesin, *Multitype Contact Process on \(\mathbb Z\): Extinction and Interface*, Electronic Journal of Probability 15 (2010), 2220–2260. First preprint dated 2010-04-12: https://arxiv.org/abs/1004.1958.
4. T. Mountford, P. L. Barrios Pantoja, D. Valesin, *The asymmetric multitype contact process*, Stochastic Processes and their Applications 129 (2019), 2783–2820. First preprint dated 2018-03-05: https://arxiv.org/abs/1803.01533.
