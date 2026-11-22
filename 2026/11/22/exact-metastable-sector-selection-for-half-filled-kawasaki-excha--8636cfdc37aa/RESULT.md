# Exact metastable-sector selection for half-filled Kawasaki exchange on the Petersen graph

## Finding
For the zero-field ferromagnetic Ising model on the Petersen graph, fix five positive and five negative spins. At each edge whose endpoint spins differ, exchange them at rate one when the change in Ising energy is nonpositive; reject energy-increasing exchanges. Thus energy-neutral exchanges remain active. Among the \(\binom{10}{5}=252\) equally likely initial spin configurations, the probability of eventually entering an energy-minimizing ground state is exactly
\[
\Pr(\text{ever reaches a ground state})=\frac{8}{63}.
\]
The complementary probability of entering a closed, dynamically active, excited-energy class is exactly \(55/63\). The chain has precisely thirteen closed communicating classes: twelve isolated ground states of energy \(-5\) and one irreducible class of 120 configurations of energy \(-1\). The other 120 configurations are transient. All ground configurations consist of one positive-spin five-cycle; all energy-\(-1\) configurations induce a five-vertex tree. The expected first entrance time into *any* closed class, from the uniform half-filled ensemble, is \(5/42\) in rate-one edge-clock time units. These values hold for the stated dynamics only.

## Assumptions and scope
Let \(P\) be the Petersen graph represented as \(KG(5,2)\): its ten vertices are the unordered two-element subsets of \(\{0,1,2,3,4\}\), and two vertices are adjacent when disjoint. It has fifteen edges. A spin configuration is described by its five-element set \(S\subseteq V(P)\) of positive spins. With coupling \(J=1\) and zero field, define
\[
H(S)=-\sum_{\{u,v\}\in E(P)}\sigma_u\sigma_v,
\qquad \sigma_v=\begin{cases}+1&v\in S,\\-1&v\notin S.\end{cases}
\]
Every disagreeing edge independently attempts to swap its endpoints with rate one. The move takes place if and only if \(\Delta H\le0\), including \(\Delta H=0\). Agreement-edge attempts, if included, have no effect. There are no exchanges between nonadjacent vertices, no spin flips, no temperature-dependent upward moves, and no additional fields. The initial law is uniform over all 252 half-filled labelled configurations. A closed communicating class is meant in the Markov-chain sense; the excited class is *not* a set of static frozen configurations.

## Proof
Put \(e(S)=|E(P[S])|\), the number of occupied–occupied edges. Cubic regularity and \(|S|=5\) give \(|\partial S|=15-2e(S)\), hence
\[
H(S)=-15+2|\partial S|=15-4e(S).
\]
Exchanging unlike spins along an edge can therefore occur precisely when \(e(S)\) does not decrease. Enumerate all five-element subsets using the explicit ten vertices and fifteen edges above; this is a complete finite proof, reproducible by `verify_kneser.py`. The independently constructed outer-pentagon/inner-pentagram presentation in `verify_spoked.py` reproduces the same counts and transitions without relying on the first graph construction.

The *complete* microstate transition census is below. The three right columns count the outgoing allowed exchanges from **each** configuration on the indicated row, classified by the target energy. Omitted target energies have count zero.

| Current energy | Number of configurations | Target \(-5\) | Target \(-1\) | Target \(3\) | Target \(7\) |
|:--|--:|--:|--:|--:|--:|
| \(-5\) | 12 | 0 | 0 | 0 | 0 |
| \(-1\) | 120 | 0 | 4 | 0 | 0 |
| \(3\) | 60 | 1 | 4 | 0 | 0 |
| \(7\) | 60 | 0 | 2 | 4 | 5 |

An exhaustive breadth-first search along energy-preserving exchanges proves that the 120 configurations of energy \(-1\) form one connected class, and that the 60 configurations of energy \(7\) form one energy-preserving connected class. The twelve energy-\(-5\) states have no allowed exits. Every energy-\(3\) state makes one transition to energy \(-5\) and four to energy \(-1\), so its ground-reaching probability is \(1/5\). An energy-\(7\) state has six strictly downward choices: two to energy \(-1\) and four to energy \(3\). Its five energy-neutral choices do not alter these downward hazard rates, which are the same at every energy-\(7\) state. Thus its first downward transition goes to energy \(3\) with probability \(4/6\), and its eventual ground-reaching probability is \((4/6)(1/5)=2/15\). The class probabilities, by starting energy, are therefore \(1,0,1/5,2/15\) in ascending-energy order. Averaging over the exact multiplicities gives
\[
\frac{12+60/5+60(2/15)}{252}=\frac{8}{63},\qquad 1-\frac{8}{63}=\frac{55}{63}.
\]
Since every energy-\(3\) state leaves at total rate five, its expected terminal-class entrance time is \(1/5\); every energy-\(7\) state first jumps to a lower energy level at rate six, and then with probability \(2/3\) spends an additional mean \(1/5\) at energy \(3\). Hence the uniform initial mean entrance time is
\[
\frac{60}{252}\cdot\frac15+\frac{60}{252}\left(\frac16+\frac23\cdot\frac15\right)=\frac5{42}.
\]
The induced subgraph for each energy-\(-5\) state has exactly five edges on five vertices and (by the Petersen graph's girth five) must be a five-cycle. The two exact programs verify this directly, rather than inferring it solely from the energy count. The 120 energy-\(-1\) subsets have four internal edges and are connected (their induced graph is a tree); this is also checked by exhaustive enumeration. Their repeated energy-neutral exchanges explain why their long-time fate is active metastability rather than literal immobilization.

## Verification
Run `python3 verify_kneser.py` and `python3 verify_spoked.py` from the directory containing these two included standalone scripts. Both use the Python standard library only. One builds the Petersen graph from disjoint two-subsets and enumerates all half-filled masks, accepted moves and neutral components. The second builds the graph from its distinct outer-ring/inner-star/spoke description, counts all 252 energies and accepted edges and independently constructs every equal-energy component. Both reconstruct the fractions from exact integer rates and rational arithmetic. Successful execution prints `PASS` lines. No random simulation, rounding or limiting extrapolation is needed. The combinatorial census is finite and exhaustive.

## Relationship to prior work
Constrained zero-temperature Kawasaki dynamics and blocked-state statistics on one-dimensional Ising chains are studied by De Smedt, Godrèche and Luck (2002), including exact terminal-energy distributions and a kinetic-adsorption representation. Krząkała (2004) analyzes glassy relaxation and metastability for Kawasaki dynamics on two-dimensional ferromagnets. These papers establish the physical context, but their geometries and their analyzed distributions do not include the half-filled ten-site Petersen graph. In contrast with strictly energy-decreasing constrained exchange, the present dynamics explicitly **allows neutral swaps**, making a 120-configuration excited recurrent class essential. The classical Petersen graph's five-cycle structure and ten-site vertex set are existing combinatorial facts, not new claims. General fixed-magnetization mixing results at positive temperature do not determine this explicit zero-temperature local-exchange absorption fraction.

## Limitations
This is an exact result for one fixed ten-vertex graph at fixed magnetization, with adjacent-edge exchange clocks at equal rate and energy-neutral moves accepted. It does not apply to all-to-all Kawasaki updates, unequal edge rates, positive temperature, field disorder, nonconserved Glauber flips or other graphs. At any positive temperature the excited class ceases to be strictly closed; the theorem makes no quantitative assertion about its escape times. The comparison to currently located published literature is not a proof of worldwide historical priority. Independent scientific audit has not been performed.

## References
1. G. De Smedt, C. Godrèche and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, first posted 26 February 2002, https://arxiv.org/abs/cond-mat/0202465 (especially section 4).
2. F. Krząkała, *Glassy properties of the Kawasaki dynamics of two-dimensional ferromagnets*, first posted 14 September 2004, https://arxiv.org/abs/cond-mat/0409348.
3. *Petersen graph*, standard Kneser and pentagon/pentagram descriptions, https://mathworld.wolfram.com/PetersenGraph.html.
