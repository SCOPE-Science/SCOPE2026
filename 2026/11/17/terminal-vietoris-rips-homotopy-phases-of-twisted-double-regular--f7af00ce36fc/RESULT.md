# Terminal Vietoris–Rips homotopy phases of twisted double regular polygons

## Finding
For any integer \(n\ge3\), radius \(R>0\), height \(h>0\), and relative twist \(0\le t\le\tfrac12\), place two regular \(n\)-gons in parallel planes, rotating the upper one through \(2\pi t/n\). Equip their \(2n\) vertices \(P=P(n,R,h,t)\) with ambient Euclidean distance. Let \(b\) be the largest intervertex distance and \(a<b\) the next-largest **distinct** intervertex distance. Write \(K=\operatorname{VR}_{\le a}(P)\), the last Rips complex before the full simplex.

Define the two standard homotopy types
\[
\mathcal C_n\simeq\begin{cases}
S^{2n/3-1}\vee S^{2n/3-1},&n\equiv0\pmod3,\\
S^{(2n-2)/3},&n\equiv1\pmod3,\\
S^{(2n-4)/3},&n\equiv2\pmod3;
\end{cases}
\]
and, for even \(n\),
\[
\mathcal M_n\simeq\begin{cases}
S^{n/2-1},&n\equiv0\pmod4,\\
\bigvee^3 S^{n/2-1},&n\equiv2\pmod4.
\end{cases}
\]
The labels \(\mathcal C_n\) and \(\mathcal M_n\) stand for the homotopy types of the independence complexes of \(C_{2n}\) and of the Möbius ladder \(M_{2n}\), respectively. The homotopy type of \(K\) is **exactly** as follows:

* If \(n\) is odd and \(t=0\), then \(K\simeq\mathcal C_n\). If \(n\) is odd and \(0<t\le\tfrac12\), then \(K\simeq S^{n-1}\).
* If \(n\) is even, put \(h_*(t)=2R\sin(\pi t/n)\). If \(0\le t<\tfrac12\) and \(h\ne h_*(t)\), then \(K\simeq S^{n-1}\). If \(0<t<\tfrac12\) and \(h=h_*(t)\), then \(K\simeq S^{n/2-1}\).
* If \(n\) is even and \(t=\tfrac12\), then \(K\simeq S^{n-1}\) for \(h<h_*(t)\), \(K\simeq\mathcal M_n\) for \(h=h_*(t)\), and \(K\simeq\mathcal C_n\) for \(h>h_*(t)\).

The exact diameter is
\[
b^2=\begin{cases}
h^2+4R^2\cos^2\!\left(\frac{\pi(1/2-t)}n\right),&n\text{ odd},\\
\max\!\left\{4R^2,\ h^2+4R^2\cos^2\!\left(\frac{\pi t}n\right)\right\},&n\text{ even}.
\end{cases}
\]
The last noncontractible filtration stage occupies the entire nonempty interval \(a\le r<b\); at \(r=b\) the complex becomes a full simplex. No earlier stages or persistent homology maps are asserted.

## Assumptions and scope
Let \(j\in\mathbb Z/n\mathbb Z\). The two layers are
\[
L_j=(R\cos(2\pi j/n),R\sin(2\pi j/n),0),\quad
U_j=(R\cos(2\pi(j+t)/n),R\sin(2\pi(j+t)/n),h).
\]
The twist range \(0\le t\le\tfrac12\) represents all relative twists up to relabeling and reflection. All distances are Euclidean and the Rips convention is inclusive: a face has all pairwise distances at most the parameter. The forbidden graph \(F\) joins precisely pairs at distance \(b\). Denote by \(qK_2\) a disjoint union of \(q\) edges and by \(qC_4\) a disjoint union of \(q\) four-cycles.

## Proof
**1. Distance maxima.** Pairwise squared distances inside either layer are
\[
d^2(L_i,L_j)=4R^2\sin^2\!\left(\frac{\pi(i-j)}n\right),
\]
with the analogous expression for the upper layer. Cross-layer squared distances are
\[
d^2(L_i,U_j)=h^2+4R^2\sin^2\!\left(\frac{\pi(i-j-t)}n\right).
\]
When \(n\) is odd, each layer's maximum occurs at either of the two cyclic offsets \((n-1)/2\) and \((n+1)/2\), giving squared length \(4R^2\cos^2(\pi/(2n))\). A cross-layer pair always has larger maximum because \(h>0\) and its best angular separation is at least as close to \(\pi\). When \(t=0\), each vertex has two cross-layer farthest neighbors; for \(0<t\le\tfrac12\), exactly one. The formula for \(b^2\) follows.

When \(n\) is even, the in-layer maximum is \(4R^2\), achieved at exactly one antipodal neighbor for each vertex. The cross-layer maximum is \(h^2+4R^2\cos^2(\pi t/n)\). For \(0\le t<\tfrac12\), each vertex has exactly one cross-layer farthest neighbor; for \(t=\tfrac12\), exactly two. The maxima coincide precisely at \(h=2R\sin(\pi t/n)\), which can occur for \(h>0\) only when \(t>0\). This proves the exact diameter formula and identifies all its attaining pairs.

**2. Four forbidden-graph patterns.** At \(a\le r<b\), every pair except a diameter pair is allowed. Since a Rips complex is flag, \(K\) is *simplicially identical* to \(\operatorname{Ind}(F)\), where \(F\) joins diameter pairs. The just-identified maximizing offsets give the exhaustive cases:

* A unique farthest partner for each of the \(2n\) vertices gives \(F=nK_2\).
* The two cross-layer farthest offsets at odd \(n,t=0\), or even \(n,t=\tfrac12\) with cross-layer dominance, give one connected alternating cycle \(F=C_{2n}\). Indeed, two consecutive alternating steps move the layer index by one modulo \(n\).
* If \(n\) is even, \(0<t<\tfrac12\), and the within- and between-layer maxima tie, the union of the intralayer antipodal matching and the unique cross-layer matching is \(F=(n/2)C_4\). Its squares are disjoint on the four vertices \(L_j,L_{j+n/2},U_j,U_{j+n/2}\), up to the harmless index shift on one layer.
* If \(n\) is even, \(t=\tfrac12\), and the maxima tie, adding the intralayer antipodal matching to the alternating \(2n\)-cycle adds **exactly** its antipodal chords. Thus \(F=M_{2n}\), the standard Möbius ladder. To see the chord distance explicitly, enumerate the alternating cycle as \(L_j,U_{j+n/2},L_{j+1},U_{j+n/2+1},\ldots\). Then matching opposite in-layer vertices are separated by \(n\) steps on the \(2n\)-cycle.

These cases include every equality boundary; no numerical generic-position hypothesis has been made.

**3. Homotopy types.** The independence complex of \(K_2\) is \(S^0\). Independence complexes turn disjoint graph unions into simplicial joins, hence \(\operatorname{Ind}(nK_2)\cong(S^0)^{*n}\cong S^{n-1}\). Also, \(\operatorname{Ind}(C_4)\simeq S^0\), so \(\operatorname{Ind}((n/2)C_4)\simeq S^{n/2-1}\). The classical independence-complex homotopy classification of cycles, due to Kozlov, gives \(\operatorname{Ind}(C_{2n})\simeq\mathcal C_n\). The published Möbius-ladder independence-complex theorem of Agarwal and Basak gives \(\operatorname{Ind}(M_{2n})\simeq\mathcal M_n\) for even \(n\). Substituting these four graph types yields all the listed homotopy cases. At \(r=b\), every pair is present and the Rips complex is the full simplex. This completes the proof.

## Verification
The standalone \(`verify_twisted_prism.py`\) reconstructs all Euclidean point pairs for \(672\) choices of \(3\le n\le30\), twist and height, including exact critical-height parameter choices, and compares the maximizing-pair graph with the independently predicted edge set. It checks graph connected-component sizes and degrees for all four patterns. Separately, it constructs every independent face and reduces augmented mod-two simplicial boundary matrices for \(54\) cases with \(3\le n\le8\). All checked ranks agree with the all-parameter homotopy formula (see \(`verify_output.txt`\)). The exact proof above, not these finite tests, establishes the theorem for all admissible real parameters and integers.

## Relationship to prior work
Saleh, Titz Mite, and Witzel classify Rips complexes of the vertex sets of Platonic solids and explicitly identify other polyhedral families as natural extensions; their theorem does not treat variable-twist double polygons. The established cycle independence-complex classification and the 2026 Möbius-ladder independence-complex classification are invoked, not reproved or presented as new. The fixed-height uniform antiprism and a particular rectangular-box special case have independently been analyzed before. Neither covers the full two-parameter twist-height phase diagram or the generic and simultaneous-diameter transitions. Graph-metric Rips complexes of prism *graphs* are a different problem from Euclidean chord-distance Rips complexes of the point sets considered here.

## Limitations
The theorem classifies only the last filtration stage before contractibility, not all earlier Rips stages, their inclusion maps, or persistence barcodes. The quoted Möbius-ladder and cycle homotopy theorems are external established ingredients. Finite checks do not certify all real parameters. Equivalent unpublished or unindexed classifications cannot be excluded by the literature searches alone.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public February 28, 2023), https://arxiv.org/abs/2302.14388 . Primary MSC2020 55N31.
2. A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601v1 (first public August 31, 2026), https://arxiv.org/abs/2608.30601 . Its independence-complex theorem supplies the even Möbius-ladder case.
3. D. N. Kozlov, *Complexes of Directed Trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122, doi:10.1006/jcta.1999.2984 . Classical cycle independence-complex homotopy types.
4. M. Adamaszek, H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669 (2015), https://arxiv.org/abs/1503.03669 . Background on Rips complexes of circular point sets.
