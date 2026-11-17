# A three-sphere and fourteen four-spheres in a scale-three torus-grid Rips complex

## Finding
Let \(T=C_7\square C_7\) be the Cartesian product of two seven-cycles with its intrinsic shortest-path metric, and use the **inclusive** Vietoris–Rips convention. Then
\[
\operatorname{VR}_{\le3}(T)\simeq S^3\vee\bigvee^{14}S^4.
\]
In particular, the only nonzero reduced integral homology groups are
\[
\widetilde H_3\cong\mathbb Z,\qquad \widetilde H_4\cong\mathbb Z^{14}.
\]
This is an integral homotopy equivalence, not merely equality of mod-two Betti numbers.

## Assumptions and scope
Represent vertices by pairs \((a,b)\in(\mathbb Z/7\mathbb Z)^2\), using representatives \(0,\ldots,6\), and put
\[
d((a,b),(c,e))=\min(|a-c|,7-|a-c|)+\min(|b-e|,7-|b-e|).
\]
A nonempty vertex subset is a simplex exactly when all pairwise distances are at most three. Label the vertex \((a,b)\) by the integer \(i=7a+b\), so a face is stored as the positive integer bitmask \(\sum_{i\in\sigma}2^i\). These indices are serialization conventions, not mathematical parameters. Homotopy is understood for the geometric realization of the finite simplicial complex.

## Proof
**Exact enumeration.** Enumerate all cliques by growing strictly increasing vertex lists, intersecting candidate sets with the neighborhood of each newly selected vertex. This enumerates each nonempty face exactly once. The resulting face vector, in dimensions zero through seven, is
\[
(49,588,2646,5488,5733,3136,896,98),
\]
with \(18{,}634\) nonempty faces. The independent certificate checker `VERIFY.py` reconstructs these faces from the metric and checks the face vector; it does not trust a saved list of faces.

**Acyclic matching.** `CERTIFICATE.json` contains \(9{,}309\) pairing events and sixteen critical-facet events, in chronological order. A pairing event `[0,f,g]` removes the face \(f\) and its unique immediate coface \(g\), which is maximal at that stage. An event `[1,m]` removes a currently maximal face \(m\) as critical. Every event is checked against the set of still-active faces; every face is removed exactly once. The critical face counts are
\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6,c_7)
=(1,0,0,1,14,0,0,0).
\]
The pairing events define an acyclic matching: in any supposed closed gradient path, consider the removal times of the lower matched faces. Each next lower face must have been removed strictly later, since, had it been removed earlier in a different pair, it would then have possessed both its matching coface and the still-present coface from the path, contradicting freeness. Thus the removal time increases strictly around a putative cycle, impossible. The intervening removal of unmatched maximal faces does not invalidate this argument. Forman's discrete Morse theorem consequently gives a CW complex with exactly the displayed critical-cell counts.

**Integral attaching degrees.** Orient simplices by their increasing vertex labels. For an oriented four-simplex \(g\) and a codimension-one face \(f\), let \([g:f]\in\{+1,-1\}\) be the ordinary integral simplicial incidence number. Define an integer \(P(f)\) for each three-simplex recursively. If \(f\) is the unique critical three-simplex, set \(P(f)=1\). If \(f\) is matched downward to a two-simplex, set \(P(f)=0\). If \(f\) is matched upward to a four-simplex \(g\), set
\[
P(f)=-[g:f]\sum_{\substack{h\subset g\\\dim h=3,\ h\ne f}}[g:h]P(h).
\]
Acyclicity makes this signed gradient-path recursion well-founded. It is exactly the elementary integral chain cancellation formula for the Morse boundary coefficient in the critical three-cell. For each of the fourteen critical four-simplices \(c\), compute
\[
D(c)=\sum_{\substack{f\subset c\\\dim f=3}}[c:f]P(f).
\]
The exact integer verifier obtains \(D(c)=0\) for all fourteen cells. The calculation uses integer coefficients, not a finite-field rank or a numerical approximation; the finite certificate and full standalone checking code are embedded with this result.

The Morse CW complex consists of a point, one three-cell attached to it, and fourteen four-cells whose attaching maps \(S^3\to S^3\) have degrees zero. Since \(\pi_3(S^3)\cong\mathbb Z\) is classified by degree, all fourteen attaching maps are nullhomotopic. The CW complex, and hence the original Rips complex, is homotopy equivalent to \(S^3\vee\bigvee^{14}S^4\), as claimed.

## Verification
With Python 3.9 or later and no third-party dependencies, place `VERIFY.py` and `CERTIFICATE.json` together and run:

```bash
python3 VERIFY.py CERTIFICATE.json
```

The checker independently regenerates the full complex, validates every chronological free-face and critical-face event, verifies exact coverage by \(9{,}309\) pairs and sixteen critical faces, and evaluates all fourteen **signed integral** critical incidence numbers. `VERIFY_OUTPUT.txt` records an actual successful replay. The certificate has SHA-256 digest `64a5c9ad74645868d56ce9bf4f56ece1c66d114a5afcee113fd85f6464745116`. All asserted computations are finite and exhaustive for this specified 49-vertex complex; no extrapolation to other torus sizes is used.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling (2025) study the same periodic Manhattan metric and inclusive Rips convention. Their Table 1 gives mod-two Betti numbers one in degree three and fourteen in degree four for this exact \(7\times7\) grid at scale three; their Section 8, Question 8.1 explicitly asks for its homotopy type. Their Theorem 7.1 addresses the distinct scales \((5,3)\) and \((7,4)\), not \((7,3)\). Sterling's 2025 thesis reproduces the corresponding partial homology table. The result here upgrades the open case from homology data to a complete integral homotopy type by an explicit discrete Morse certificate. Separate scale-two torus-grid results and results on the even-order half-diameter family do not imply this odd-order, scale-three classification.

## Limitations
This theorem concerns exactly the \(7\times7\) periodic grid at inclusive radius three. The certificate is finite and does not classify the \(6\times6\) case, larger grids, higher filtration stages, equivariant actions, or homology persistence maps. The homotopy conclusion depends on the stated discrete Morse and integral signed-path verification; an independent external mathematical audit has not been performed. A bibliographically unindexed equivalent result cannot be excluded merely by database searches.

## References
1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, and J. Sterling, *Vietoris–Rips complexes of torus grids*, first posted 2025-02-10, arXiv:2502.07134, especially Table 1, Theorem 7.1 and Question 8.1. https://arxiv.org/abs/2502.07134
2. J. Sterling, *Vietoris–Rips Complexes of Torus Grids*, Auburn University master's thesis, 2025, Table 1.1 and Chapters 3–4. https://etd.auburn.edu/handle/10415/9659
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
