# The complete inclusion-minimal zero-forcing spectrum of an extremal edge–isolate/path join

## Finding

For every integer \(m\ge4\), form the simple undirected graph
\[
G_m=(K_2\sqcup K_1)\vee P_m.
\]
Name the three vertices of the first factor \(x,y,z\), with \(xy\) its only edge, and name the path vertices \(v_1,\ldots,v_m\) in order. The join adds all edges between the two factors. Let \(\mathcal M_m\) denote the family of inclusion-minimal ordinary zero-forcing sets. Its cardinality polynomial is
\[
M_m(t)=\sum_{S\in\mathcal M_m}t^{|S|}
=8t^4+(4m-15)t^5+2t^{m+1}.
\]

The disjoint structural classification is as follows, with arbitrary choices from \(\{x,y,z\}\) understood as *labelled* choices:

1. Any two core vertices, together with either endpoint path pair \(\{v_1,v_2\}\) or \(\{v_{m-1},v_m\}\): exactly \(6\) sets of size \(4\).
2. Any two core vertices, together with a consecutive interior path triple \(\{v_i,v_{i+1},v_{i+2}\}\) with \(2\le i\le m-3\): exactly \(3(m-4)\) sets of size \(5\).
3. All three core vertices, together with one path endpoint: exactly \(2\) sets of size \(4\).
4. All three core vertices, together with a consecutive interior path pair \(\{v_i,v_{i+1}\}\) with \(2\le i\le m-2\): exactly \(m-3\) sets of size \(5\).
5. Precisely one core vertex, either \(x\) or \(y\), together with all path vertices: exactly \(2\) sets of size \(m+1\).

The total number is \(4m-5\). For \(m\ge6\), the size spectrum is exactly \(\{4,5,m+1\}\), with the \(m-5\) missing intermediate sizes \(6,\ldots,m\). At \(m=4\), the last two polynomial terms both contribute at size five.

## Assumptions and scope

The graph is finite, simple, undirected, and has exactly the specified core and path edges. The ordinary zero-forcing rule is: a blue vertex with exactly one white neighbour can turn that neighbour blue. A set of initially blue vertices is zero forcing if repeated applications can blue every vertex. It is *inclusion-minimal* if no proper subset is zero forcing. This is not a classification of all zero-forcing sets, of positive semidefinite forcing, or of arbitrary joins.

Write \(A=\{x,y,z\}\), \(B=\{v_1,\ldots,v_m\}\), and \(a=|S\cap A|\). Because zero forcing is monotone in the initial blue set, inclusion minimality is equivalent to the failure of zero forcing after removing any single vertex from \(S\).

## Proof

**Step 1: Initial forcing, split by \(a\).** If \(a=0\), no blue path vertex has fewer than three white core neighbours, so no initial force is possible. If \(a=1\), every blue path vertex has two white core neighbours, so no path vertex can force initially. The core vertex \(x\) or \(y\), when blue, has the other endpoint of the core edge plus all white path vertices as white neighbours. It can start if and only if *every* path vertex is initially blue; it then forces its core-edge partner, after which a blue path vertex forces \(z\). If \(z\) alone is blue in the core, it can at most force a unique missing path vertex; even after this, the two core-edge endpoints remain white, so propagation stalls. Thus the sole possibilities when \(a=1\) are the two sets of family 5.

Let \(a=2\). There is a unique white core vertex. A blue path vertex can force that vertex at once exactly when both its path neighbours (whenever present) are blue. When at least two path vertices are white, no core vertex has exactly one white path neighbour; even a blue core-edge endpoint has no better opportunity. Therefore a zero-forcing set with at least two initially white path vertices must contain a blue path vertex whose existing path neighbours are all blue. Such a local configuration is equivalent to containing an endpoint-adjacent blue pair or an interior blue triple. If there are at most one white path vertex, since \(m\ge4\) the two endpoint pairs are vertex-disjoint, hence at least one of them is entirely blue; the same necessary condition holds. Conversely, given the endpoint pair or interior triple, a path vertex immediately forces the last white core vertex. With the whole core now blue, that adjacent pair allows propagation along the path in both directions. This proves the complete zero-forcing criterion for \(a=2\): exactly those whose path part contains an endpoint-adjacent pair or an interior consecutive triple.

Let \(a=3\). When a path endpoint is initially blue, or when any two adjacent path vertices are initially blue, the path propagates while the three core vertices are already blue. Conversely, if the initially blue path vertices omit both endpoints and contain no adjacent pair, then at least two path vertices are white (as \(m\ge4\)), so none of the blue core vertices can start, and each blue path vertex has two white path neighbours. Consequently \(S\) forces precisely when its path part contains an endpoint or an adjacent pair.

**Step 2: Extract the inclusion-minimal subsets in each case.** In the \(a=1\) case, family 5 is inclusion-minimal: deleting any path vertex prevents the core-edge endpoint from forcing its white partner, and deleting the sole blue core vertex leaves all core vertices white.

In the \(a=2\) case, the inclusion-minimal path patterns satisfying the criterion are exactly the endpoint-adjacent pairs and interior consecutive triples. In a triple no endpoint is present; no proper subset contains a local all-blue path-neighbourhood. Removing one initially blue core vertex changes to \(a=1\), but the selected path pattern has at most three vertices, strictly fewer than \(m\), and hence cannot force in the \(a=1\) criterion. Every such configuration is thus inclusion-minimal, and any strictly larger path part contains one as a proper forcing subset.

In the \(a=3\) case, the inclusion-minimal path patterns are exactly a singleton endpoint or an adjacent pair not containing a path endpoint. Removing one core vertex leaves \(a=2\), but neither singleton-endpoint nor interior pair contains a path vertex with all its path neighbours initially blue. These sets are therefore inclusion-minimal; supersets are not.

**Step 3: Enumerate.** Families 1 and 3 contribute \(6+2=8\) sets of size four; families 2 and 4 contribute \(3(m-4)+(m-3)=4m-15\) sets of size five; family 5 contributes two sets of size \(m+1\). The five patterns are disjoint by core membership and path configuration. Adding coefficients completes the theorem.

## Verification

The included standalone `verify.py` independently builds the graph adjacency masks, simulates the ordinary zero-forcing rule for each starting subset, verifies the four-case structural criterion, and compares *all inclusion-minimal sets* to the explicit five-family generator. It exhausts every initial subset for each \(4\le m\le14\), then checks the forcing criterion on deterministic pseudorandom samples at \(m\in\{20,35,60,100\}\). Run `python3 verify.py`. The final line must be `VERIFY_OK`. Those finite tests corroborate, rather than establish, the all-\(m\) theorem.

## Relationship to prior work

McKay, Ray and Valliere, *Maximizing the discrepancy between zero forcing parameters relative to graph order* (arXiv:2609.35522; first public version 2026-09-28), Proposition 3.3, introduced exactly this join family for its extreme inclusion-minimal sizes, proving \(Z(G_m)=4\) and \(\overline Z(G_m)=m+1\). These facts and this graph family are **not claimed as new**. Their relevant proof exhibits an extremal minimum set and an extremal maximum minimal set but does not enumerate *all* minimal zero-forcing sets or rule out intermediate cardinalities. The present classification and its linear counting polynomial are not consequences of the two endpoints alone.

Brimkov and Carlson, *Minimal Zero Forcing Sets* (arXiv:2204.01810, Section 3, Proposition 15), analyze a different join \((2K_2)\vee P_{n-4}\) and show its extreme minimum/maximum sizes. Their general fort-transversal characterization does not supply the labelled count for the present family. Published work on the reconfiguration graph of \(K_s\vee P_n\) likewise has a complete-clique core and is not the present edge-plus-isolate join.

## Limitations

The claim is specific to ordinary zero forcing and this labelled infinite family. The numeric extremal forcing parameters and extremal graph family are previously known. The additional claim is the *full* inclusion-minimal classification and polynomial. An independent mathematical audit and exhaustive historical-priority determination have not been performed. Search failure is not proof of novelty; comparison with some related published records was limited to their abstracts or summaries. No general classification of arbitrary graph joins or all zero-forcing sets follows.

## References

1. A. McKay, A. Ray and J. Valliere, *Maximizing the discrepancy between zero forcing parameters relative to graph order*, arXiv:2609.35522v1, https://arxiv.org/abs/2609.35522 (first posted 2026-09-28), especially Section 3.1, Proposition 3.3.
2. B. Brimkov and J. Carlson, *Minimal Zero Forcing Sets*, arXiv:2204.01810, https://arxiv.org/abs/2204.01810 (first posted 2022-04-04), especially Section 3, Proposition 15.
3. J. Grood and collaborators, *Well-forced graphs*, arXiv:2312.14298, https://arxiv.org/abs/2312.14298 (background on minimal zero-forcing sets and well-forcedness).
