# A six-hypercube max-cut attractor and exponential mixing bottleneck on \(K_{n,n,n}\)

## Finding

For every integer \(n\ge 2\), let \(G_n=K_{n,n,n}\) be the complete tripartite graph with three labelled independent vertex sets \(A,B,C\), each of size \(n\). Each vertex carries a binary opinion. At each discrete step a uniformly chosen vertex adopts the minority opinion in its **closed** neighborhood (itself and all its adjacent vertices), keeping its current opinion only if the two closed-neighborhood counts tie. Since the closed neighborhood has \(2n+1\) vertices, there is no closed-neighborhood tie here: an updating vertex flips exactly when at least \(n\) of its \(2n\) neighbors have its current opinion.

**Theorem.** The resulting finite Markov chain has exactly one recurrent communicating class. It is the set of maximum cuts of \(G_n\), and contains exactly
\[
R_n=6(2^n-1)
\]
labelled configurations. These configurations are precisely those with two parts unanimously assigned opposite opinions and the remaining part arbitrary. Every initial configuration admits a path of at most \(2n\) single-vertex flips to this class and reaches it almost surely. The recurrent transition graph is the union of six \(n\)-dimensional hypercubes, with consecutive hypercubes meeting in one vertex along a six-cycle of overlaps; there are no other intersections. Its discrete-time stationary distribution is uniform on the \(R_n\) configurations.

The chain is irreducible and aperiodic on this class but mixes exponentially slowly. For the standard total-variation mixing time,
\[
t_{\mathrm{mix}}(1/4)>\left\lfloor\frac{3\cdot2^n}{4}\right\rfloor.
\]
More precisely, if \(F\) is any one of the six hypercube faces (containing \(2^n\) configurations), its exact stationary one-step escape probability conditioned on \(F\) is
\[
\mathbb{P}_{\pi(\cdot\mid F)}(X_1\notin F)=\frac{2}{3\cdot2^n}.
\]
Nevertheless, the stationary probability of a genuine spin flip at any step equals
\[
\frac{2^n}{3(2^n-1)},
\]
which tends to \(1/3\). Thus abundant local motion coexists with an exponentially rare change of macroscopic phase.

## Assumptions and scope

The parts \(A,B,C\) and their individual vertices are labelled. States differing by global opinion complement are counted separately. Each step selects one of all \(3n\) vertices independently and uniformly, including vertices that would not change opinion. This convention creates self-loops. The result concerns finite \(n\ge2\) and the zero-noise, closed-neighborhood minority rule; it does not apply automatically to a strict-improvement rule, to random tie breaking, or to synchronous updates. A mixing-time statement refers to the transition kernel restricted to the unique recurrent class, with its unique stationary law.

## Proof

**1. Exact update inequalities and monotone cut size.** Let \(x_A,x_B,x_C\) count opinion-one vertices in the parts. For a vertex in part \(i\), write \(S_i=x_j+x_k\) for the number of opinion-one neighbors outside its part. A current zero flips to one exactly when \(S_i\le n\), and a current one flips to zero exactly when \(S_i\ge n\). Indeed, a flip occurs when at least \(n\) of the \(2n\) neighbors match the current opinion. For any allowed flip, the cut size changes by \(\#\mathrm{same}-\#\mathrm{opposite}\ge0\), with equality exactly when the neighboring opinions are tied. In particular, the maximum-cut configurations form a closed set under the stochastic dynamics.

**2. The global maximum and all maximizers.** For the part counts \((x,y,z)\in\{0,\ldots,n\}^3\), the cut size is
\[
\mathcal C(x,y,z)=2n(x+y+z)-2(xy+xz+yz).
\]
This function is affine in each coordinate when the others are fixed. It therefore attains a global maximum at a vertex of the real box \([0,n]^3\). Among the eight corners its largest value is \(2n^2\), attained when one part has one opinion and the other two share the opposite opinion.

To classify all maximizers, note that if \(0<x<n\) at a maximizer, the coefficient of \(x\) must vanish, so \(y+z=n\). If two coordinates are interior and the third is at an endpoint, these vanishing conditions force an interior coordinate to be an endpoint, a contradiction. If all three are interior, they must equal \(n/2\), yielding cut size \(3n^2/2<2n^2\). Thus at most one part is mixed. If one part is mixed, the other two must be unanimously opposite because their counts are endpoints summing to \(n\). The three-unanimous maximizers are already included in this description.

**3. Explicit all-state reachability.** From an arbitrary configuration, consider \(S_A=x_B+x_C\). If \(S_A\ge n\), flip each opinion-one vertex in \(A\) to zero; all these flips are permitted because \(S_A\) stays constant during the operation. If \(S_A<n\), flip each opinion-zero vertex in \(A\) to one. In at most \(n\) flips, \(A\) is unanimous. If \(A\) is zero, every zero in \(B\) can now flip to one, since its external one count is \(x_C\le n\). If \(A\) is one, every one in \(B\) can flip to zero, since its external one count is \(n+x_C\ge n\). In at most another \(n\) flips, \(A\) and \(B\) are unanimously opposite, independently of the configuration of \(C\); the cut is maximal. Thus every state reaches the closed maximum-cut set by an allowed directed path of length at most \(2n\). Finiteness and positive probability of every chosen firing sequence imply almost-sure entry in that set (one may repeat the uniform positive-probability path bound on successive blocks of \(2n\) updates).

**4. Exact recurrent structure.** Fix a pair of distinct parts \((i,j)\), require part \(i\) all zero and part \(j\) all one, and allow the third part to vary arbitrarily. Denote this family by \(F_{i0,j1}\). There are six such families, each with \(2^n\) configurations. In any family, each vertex in the free part sees exactly \(n\) zeros and \(n\) ones, so its firing flips it and remains within the family. Every family is therefore a full \(n\)-dimensional hypercube of reversible transitions. If the free part is mixed, vertices in the two fixed parts cannot flip. At each endpoint where the free part becomes unanimous, the configuration also belongs to exactly one other family. The six families meet according to the cyclic sequence
\[
F_{A0,B1},\quad F_{C0,B1},\quad F_{C0,A1},\quad F_{B0,A1},\quad F_{B0,C1},\quad F_{A0,C1},
\]
with each neighboring pair intersecting in precisely one all-unanimous configuration (and no other intersections). Consequently their union is connected by reversible neutral flips. By Steps 1--3 it is the unique recurrent class. Exactly six unanimous maximum-cut configurations occur in two families each; all other configurations occur in one family. Hence its size is \(6\cdot 2^n-6\). Every allowed transition between recurrent configurations is a neutral flip, whose reverse is allowed with the same probability \(1/(3n)\). The uniform measure \(\pi\) is therefore reversible and stationary. Since some vertices are inactive in each recurrent state, the chain has self-loops and is aperiodic.

**5. Exact escape flux and mixing obstruction.** Fix \(F=F_{A0,B1}\). Its \(2^n-2\) mixed-free-part configurations have no transitions leaving \(F\). At the endpoint with \(C\) unanimously zero, exactly the \(n\) vertices of \(A\) can produce transitions leaving \(F\). At the endpoint with \(C\) unanimously one, exactly the \(n\) vertices of \(B\) can do so. The stationary directed flow out of \(F\) is therefore
\[
Q(F,F^{\mathrm c})=\frac{2n}{3nR_n}=\frac2{3R_n},
\qquad \pi(F)=\frac{2^n}{R_n}.
\]
Division gives the stated escape probability \(2/(3\cdot2^n)\).

Put \(\nu=\pi(\cdot\mid F)\). Because \(\nu\le\pi/\pi(F)\) pointwise, the same domination holds after any number of steps. A union bound over the first \(t\) opportunities to cross from \(F\) to its complement gives
\[
\mathbb P_{\nu}(X_t\notin F)\le t\,\frac{Q(F,F^{\mathrm c})}{\pi(F)}
=\frac{2t}{3\cdot2^n}.
\]
For \(n\ge2\), \(\pi(F)=2^n/[6(2^n-1)]\le2/9\). At the integer time \(t=\lfloor3\cdot2^n/4\rfloor\), therefore,
\[
\|\nu P^t-\pi\|_{\mathrm{TV}}\ge
\pi(F^{\mathrm c})-\mathbb P_\nu(X_t\notin F)
\ge \frac79-\frac12=\frac5{18}>\frac14.
\]
Total variation distance is convex under averaging of starting states, so at least one starting configuration has distance greater than \(1/4\). This proves the mixing-time lower bound.

**6. Stationary local activity.** Every face has \(n2^{n-1}\) undirected hypercube edges. Since the six faces overlap only at vertices, the recurrent transition graph has \(3n2^n\) undirected edges. Each directed flip has probability \(1/(3n)\); counting two directions per edge under uniform \(\pi\) gives
\[
\mathbb P_\pi(X_1\ne X_0)=\frac{6n2^n}{3nR_n}
=\frac{2^n}{3(2^n-1)}.
\]
This completes the proof.

## Verification

The self-contained program `verify_constructive.py` independently enumerates all labelled configurations for \(1\le n\le6\), checks the constructive path, finds all optimal cuts, verifies the six-face count and checks exactly \(2n\) outgoing directed transitions from one chosen face. It examined \(299592\) configurations in total.

The program `verify_scc.py` independently constructs the full single-site transition graph and finds terminal strongly connected components for \(1\le n\le4\). It checks that there is one recurrent component of the claimed size, that recurrent configurations coincide with maximum cuts and that every allowed recurrent flip is reversible. The exhaustive transition-graph test covers \(4680\) labelled configurations. Both programs completed with the expected PASS messages; their exact recorded standard output is included as separate text files. These finite tests support but do not replace the all-\(n\) proof.

Run using Python 3 with `python verify_constructive.py` and `python verify_scc.py`. The second program requires NetworkX (tested with version 3.6.1). No network access or external data is required.

## Relationship to prior work

Rouquier, Regnault and Thierry (2010) define precisely the fully asynchronous closed-neighborhood minority process used here and show its general monotone edge-energy identity. Their inspected analysis treats cliques, paths, cycles, trees and bipartite mechanisms; it does not give an exact recurrent-state or bottleneck classification for balanced complete tripartite graphs. The present proof uses the energy viewpoint but adds a cut maximizer classification, explicit six-hypercube recurrent geometry and an exact rare-escape flux for this dense nonbipartite family.

Papp and Wattenhofer (2019) study stabilization-time lower bounds for minority processes with strict conflict-reducing switches; their paper explicitly distinguishes those processes from the closed-neighborhood convention, which can sustain neutral stochastic motion. Their bounds do not imply the exponential **mixing within** the unique nonabsorbing recurrent class established here. General maximum-cut and local-improvement observations likewise do not determine the connected geometry and mixing obstruction of the optimal-state flip chain.

## Limitations

No matching upper bound on the mixing time, exact spectral gap or expected entrance time is proved. The six-hypercube description holds for balanced three-part graphs only; unequal part sizes or more than three parts can change the maximizing set and dynamics. Literature searches and inspected primary texts do not exclude every unindexed earlier equivalent treatment of the zero-temperature antiferromagnetic flip graph; historical priority therefore remains qualified. Independent validation has not been performed.

## References

1. J.-B. Rouquier, D. Regnault and É. Thierry, *Stochastic Minority on Graphs* (first public arXiv version 2010-11-23), arXiv:1011.5119v1. Full accessible text: https://ar5iv.labs.arxiv.org/html/1011.5119 .
2. P. A. Papp and R. Wattenhofer, *Stabilization Time in Minority Processes* (first public arXiv version 2019-07-03), arXiv:1907.02131v1; proceedings DOI 10.4230/LIPIcs.ISAAC.2019.43. The inspected published paper explicitly separates strict switching from the closed-neighborhood variant.
3. Z. Cao and X. Yang, *The Fashion Game: Network Extension of Matching Pennies*, Theoretical Computer Science 540--541 (2014), 169--181. Discusses network coordination/anti-coordination games, a different rule family without the present exact stochastic recurrent-class census.
