# Exact oscillation basins for threshold-two cyclic dynamics on complete split graphs

## Finding
For every pair of integers \(a,b\ge1\), let \(G_{a,b}=K_a\vee\overline K_b\) be the simple graph comprising a clique of \(a\) labelled vertices adjacent to each of \(b\) labelled independent vertices. Under synchronous three-colour threshold-two cyclic dynamics, each vertex of colour \(c\in\{0,1,2\}\) advances to \(c+1\pmod 3\) if at least two *distinct open neighbours* currently have colour \(c+1\); otherwise its colour is unchanged. Let \(F_{a,b}\) be the update map.

**Theorem.** The identity \(F_{a,b}^{7}=F_{a,b}^{4}\) holds for all \(a,b\ge1\). Thus every configuration enters a fixed point or a primitive three-cycle within four updates; four is sharp (already at \((a,b)=(2,5)\)). Define entire formal power series
\[
U(z)=e^z-1-z,\qquad V(w)=e^w-1-w.
\]
The exact number \(N_3(a,b)\) of *labelled initial configurations eventually attracted to primitive three-cycles*, including transient configurations, is
\[
\boxed{N_3(a,b)=a!b!\,[z^a w^b]\,\Phi(z,w)},
\]
where
\[
\boxed{\begin{aligned}
\Phi(z,w)={}&U(z)^3e^{3w}
+3U(z)^2e^{2w}\bigl[V(w)+z(V(w)+w)\bigr]\\
&+3V(w)^3(z+z^2)+z^3(V(w)+w)^3.
\end{aligned}}
\]
Consequently the fixed-point attraction basin contains exactly \(3^{a+b}-N_3(a,b)\) labelled initial states.

Primitive three-cycles exist precisely in the following parameter regimes: \(a\ge5,\ b\ge1\); or \(a=4,\ b\ge2\); or \(a=3,\ b\ge3\); or \(a\in\{1,2\},\ b\ge6\). All other sizes have only eventual fixed points.

For each fixed \(a\), as \(b\to\infty\), the three-cycle basin probability tends to \(p_a\), with
\[
p_1=1,\quad p_2=\frac23,\quad p_3=p_4=\frac29,
\qquad p_a=1-\frac{3(a^2+a+1)}{3^a}\quad(a\ge5).
\]
In particular, the limiting oscillatory fraction drops sharply at clique sizes three and four and then increases again. The error is uniformly bounded by \(3[(2/3)^b+(b/3)(2/3)^{b-1}]\), independently of \(a\).

## Assumptions and scope
The graph has no loops or multiple edges, every vertex is labelled, all updates occur simultaneously, and colours are interpreted modulo three. The threshold counts different neighbours, never multiple encounters with one neighbour. The probability refers to independent uniform initial colours, not to stochastic time evolution. \(N_3\) counts attraction basins, not only states already on cycles. The restrictions \(a,b\ge1\) are essential to the statement's graph-family definition.

## Proof
**Step 1: a fixed-size exact quotient.** Partition the initial clique vertices into their three original colour classes, of sizes \(m_0,m_1,m_2\), and the initial independent vertices similarly, of sizes \(n_0,n_1,n_2\). Each original class remains monochromatic at all later times: vertices belonging to one class have identical open neighbourhoods except for one another, but while their current colours coincide, the number of *successor-coloured* clique neighbours is identical for each. Their current colour cannot itself be the successor colour. Thus the current colours of all six original classes can be tracked by six tags \(t_i\in\{0,1,2\}\).

Replace each initial class size by its clip \(\min(2,m_i)\) or \(\min(2,n_i)\). Clipping loses no information necessary for any update: for every finite multiset of nonnegative integers, its sum is at least two if and only if the sum of its separately clipped values is at least two. For tags \(t=(t_0,\ldots,t_5)\), compute the clipped current clique and independent colour counts \(A_c,B_c\) by summing clipped masses attached to classes of tag \(c\), with clipping at two after addition. Tag \(t_i=c\) advances precisely if \(A_{c+1}+B_{c+1}\ge2\) for \(i<3\) or if \(A_{c+1}\ge2\) for \(i\ge3\). Although an actual initial class may contain arbitrarily many vertices, this *tag* transition is exactly the original vertex transition for every such population vector.

**Step 2: complete finite certificate.** There are exactly \(3^6=729\) possible clipped six-tuples, including impossible tuples for a particular \((a,b)\), which is harmless because proving an identity on a superset suffices. For each tuple, initialize tags \((0,1,2,0,1,2)\), apply the explicit transition seven times, and compare the tags at times four and seven for every class whose clipped size is positive. Exhaustive application yields equality in all 729 cases. The executable `finite_certificate.py` contains this complete finite loop, explicit update rule, and assertions, with no precomputed truth table or unverified external solver. It also finds clipped vectors requiring first periodic entry at time four, and verifies that no other eventual period occurs. Since the reduction is exact for all nonnegative initial class sizes, this finite enumeration proves \(F_{a,b}^{7}=F_{a,b}^{4}\) for *every* \(a,b\ge1\), not merely for tested graph sizes.

Sharpness has an independently checkable explicit example. On \(G_{2,5}\), give the clique the ordered colours \((1,2)\), and the independent vertices \((0,0,1,1,2)\). The successive complete vertex colour words are `1200112`, `2000112`, `0100112`, `1100112`, `1111112`, after which the word is fixed. Its first periodic entry is at time four.

**Step 3: exact basin count by labelled exponential generating functions.** For a single original-colour class, the exponential generating functions for sizes clipped to zero, one, and two are respectively \(1\), \(z\), and \(U(z)\) in the clique and \(1\), \(w\), and \(V(w)\) in the independent set. The factor \(a!b!\) restores labels. In the same 729-case loop, mark a clipped tuple as oscillatory exactly when at times four and five at least one positive-size original class has different tags. The identity already proved ensures that this is equivalent to eventual *primitive* period three. Exactly 122 clipped tuples are marked. Summing the associated products of six size-generating functions gives a polynomial of 31 distinct monomials in \(z,U(z),w,V(w)\); its expansion is *identically* \(\Phi\) as displayed in the theorem. `finite_certificate.py` independently expands the claimed four-summand form as a formal polynomial in those four symbols and verifies all 31 integer coefficients against the 729-case count. Coefficient extraction is valid for every \(a,b\) because it is merely the disjoint enumeration of all initial colour populations.

**Step 4: existence and limiting law.** All coefficients of the four-summand form are nonnegative. The minimum positive clique/independent degrees in its summands give exactly the four existence regimes listed above, with no cancellation. For fixed \(a\), the probability that each of the three initial independent-set colour classes has size at least two tends to one; a union bound shows the failure probability is at most \(3[(2/3)^b+(b/3)(2/3)^{b-1}]\). Conditional on this event, the three-class clipped independent vector is \((2,2,2)\), so the clique-size exponential generating function for eventual oscillation is the coefficient of \(V(w)^3\) in the formal four-variable polynomial:
\[
H(z)=U(z)^3+3U(z)^2(1+z)+3(z+z^2)+z^3
=e^{3z}-3(1+2z+z^2)e^z+2+9z+9z^2+3z^3.
\]
Therefore \(p_a=a![z^a]H(z)/3^a\), giving the displayed values, including the stated expression for \(a\ge5\). The same union bound controls the unconditional error.

## Verification
The two standalone scripts rely only on Python 3's standard library. Running `python3 finite_certificate.py` enumerates all 729 symbolic clipped cases and verifies the universal identity, the maximum-entry certificate, and the exact 31-monomial polynomial identity. Running `python3 full_state_check.py` independently enumerates every individually labelled initial state for every \(a,b\ge1\) with \(a+b\le10\) (752,877 states over 45 graph sizes), checks eventual periods and first-entry times by direct vertex updates, and compares the exact oscillatory basin count to coefficient extraction of \(\Phi\). The resulting captured outputs are in `finite_certificate.out` and `full_state_check.out`. This second finite experiment corroborates but does not replace the exact clipping lemma and all-729-case proof.

For a small check, \(N_3(3,3)=36\), \(N_3(4,2)=18\), and \(N_3(5,1)=90\). All remaining initial states in each case eventually fix.

## Relationship to prior work
The successor-contact rule is a specialization of the cyclic cellular automaton investigated by Durrett and Griffeath [1], which analyzes periodic structures in spatial lattice dynamics; the finite split-graph basin enumerator is not a specialization of their reported lattice spiral cutoffs. Goles and Matamala [2,3] established graph-wide bounds and examples for cyclic automata, but full texts of those particularly relevant older works could not be inspected, so an unrecognized equivalent specialized calculation remains a priority risk. Epperlein and Siegmund [4] prove graph-theoretic periodicity and phase-locking statements for related threshold/refraction networks; the inspected theorem concerns a different update mechanism and does not supply the labelled split-graph basin count.

The star case \(a=1\) and the case \(a=2\), which is also a complete tripartite cone with part sizes \((1,1,b)\), overlap previously studied special graph families; those are not asserted to be independent discoveries. The principal new scope is \(a\ge3\), particularly the uniform four-term attraction-basin generating function and fixed-clique-size limiting oscillation law, which are not implied by those special cases. No proof of global historical uniqueness is claimed.

## Limitations
The correctness proof uses a small exhaustive symbolic-state certificate rather than a hand-written case-by-case classification of all 729 signatures; scripts are included and independently cross-checked. The theorem concerns three colours, threshold exactly two, synchronous updates and the complete split graph only. The exact numbers of *distinct temporal cycles* of each length are not determined, only their labelled attraction-basin populations. Full-text comparison with the 1995 and 1997 finite-graph papers remains incomplete; subsequent human priority review may identify overlap. Independent mathematical validation has not been performed.

## References
[1] R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, Experimental Mathematics 2 (1993), 183–208. Public preprint dated 1993-03-22, https://arxiv.org/abs/patt-sol/9303002; accessible full PDF https://sites.math.duke.edu/~rtd/reprints/paper79.pdf.

[2] M. Matamala and E. Goles, *Cyclic Automata Networks on Finite Graphs*, LATIN 1995, Lecture Notes in Computer Science 911, 398–410. https://doi.org/10.1007/3-540-59175-3_105 (abstract available; full text not inspected).

[3] E. Goles and M. Matamala, *Dynamic Behavior of Cyclic Automata Networks*, Discrete Applied Mathematics 77 (1997), 161–184. https://doi.org/10.1016/S0166-218X(97)84104-2 (abstract available; full text not inspected).

[4] J. Epperlein and S. Siegmund, *Phase-locked trajectories for dynamical systems on graphs*, Discrete and Continuous Dynamical Systems B 18 (2013), 1827–1844. https://doi.org/10.3934/dcdsb.2013.18.1827; accessible text https://www.researchgate.net/publication/259299835_Phase-locked_trajectories_for_dynamical_systems_on_graphs.
