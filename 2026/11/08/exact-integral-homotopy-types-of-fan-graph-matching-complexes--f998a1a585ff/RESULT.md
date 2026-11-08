# Exact integral homotopy types of fan-graph matching complexes

## Finding
For the graph \(F_n=K_1\vee P_n\), the join of one apex vertex with a path on \(n\ge2\) vertices, let \(\mathcal M(F_n)\) denote the simplicial complex whose vertices are graph edges and whose faces are pairwise vertex-disjoint edge families. There is an exact integral homotopy classification:
\[
\mathcal M(F_{3k})\simeq\bigvee^{k+1}S^{k-1}\quad(k\ge1),\qquad
\mathcal M(F_{3k+1})\simeq\bigvee^{k}S^{k}\quad(k\ge1),\qquad
\mathcal M(F_{3k+2})\simeq\bigvee^{2k+2}S^{k}\quad(k\ge0).
\]
Thus the reduced integral homology is free and supported in precisely one degree. The sphere multiplicities grow linearly with the path length and exhibit a three-residue pattern. The base cases \(n=2,3\) each consist of three connected components, and the first connected case \(n=4\) is a circle up to homotopy.

## Assumptions and scope
All graphs are finite, simple and undirected. Number the path vertices \(1,\ldots,n\); write \(p_i=\{i,i+1\}\) for its \(n-1\) path edges and \(s_i=\{0,i\}\) for the spokes from apex \(0\). All displayed homotopy equivalences concern geometric realizations. The empty augmented simplicial complex \(\{\varnothing\}\), with no nonempty faces, is denoted formally by \(S^{-1}\) for join and suspension bookkeeping: adding a cone on it contributes an isolated vertex. The ordinary wedge-of-zero-spheres convention is a set of one more point than the number of summands.

## Proof
**Path independence complexes.** Let \(I_m=\operatorname{Ind}(P_m)\) for a path with \(m\ge0\) vertices, and define \(I_{-1}=I_0=\{\varnothing\}\) when used as join factors. For \(m\ge3\), delete the second vertex of \(P_m\). Its independence-complex deletion is a cone because the first path vertex becomes isolated. Its link is \(I_{m-3}\), induced on vertices \(4,\ldots,m\). The deletion/link cofibration consequently gives \(I_m\simeq\Sigma I_{m-3}\). Together with \(I_0\simeq S^{-1}\), \(I_1\) contractible and \(I_2\simeq S^0\), this gives, for all admissible \(q\),
\[
I_{3q}\simeq S^{q-1},\qquad I_{3q+1}\simeq *,\qquad I_{3q+2}\simeq S^{q}.
\]
For the formal case \(m=-1\), use \(I_{-1}=S^{-1}\) only as the join unit.

**Spoke decomposition.** All spokes share apex \(0\), so any matching contains at most one spoke. Let \(A=\mathcal M(P_n)=I_{n-1}\) be the subcomplex consisting of matchings without spokes. For every \(1\le i\le n\), the link in \(\mathcal M(F_n)\) of the vertex associated with spoke \(s_i\) is
\[
A_i=I_{i-2}*I_{n-i-1}\subseteq A,
\]
where negative index \(-1\) denotes an empty factor. There are no faces containing two spoke vertices. Consequently \(\mathcal M(F_n)\) is obtained from \(A\) by attaching the \(n\) simplicial cones \(s_i*A_i\), all meeting one another only inside \(A\). Attaching a cone to a subcomplex is a mapping cone; if the attaching map is nullhomotopic, it splits as a wedge with the suspension of the attaching space. A contractible nonempty \(A_i\) contributes no homotopy, while \(A_i=S^{-1}\) gives one isolated vertex.

The path calculation shows that \(A_i\) is noncontractible exactly when neither integer \(i-2\) nor integer \(n-i-1\) is congruent to \(1\pmod3\). (The endpoint value \(-1\) has residue \(2\).) Counting these indices and their dimensions gives:

* For \(n=3k\), exactly \(k\) indices \(i\equiv2\pmod3\) have \(A_i\simeq S^{k-2}\), and \(A\simeq S^{k-1}\). For \(k\ge2\), any map from \(S^{k-2}\) to \(S^{k-1}\) is nullhomotopic by connectivity. Hence the \(k\) cones contribute \(k\) further \((k-1)\)-spheres, giving \(k+1\). When \(k=1\), the sole noncontractible \(A_i\) is empty, so it adds an isolated point to the two-component \(A\simeq S^0\), again yielding a wedge of two zero-spheres.
* For \(n=3k+1\), exactly \(k+1\) indices \(i\equiv1\pmod3\) have \(A_i\simeq S^{k-1}\), and \(A\simeq S^{k-1}\). Attach the cone for \(s_1\) first. Its base \(A_1=I_{3k-1}\hookrightarrow I_{3k}=A\) is a homotopy equivalence: this inclusion deletes the first path-edge vertex, equivalently the last vertex after reversing the path, and the corresponding deletion/link cofibration has link \(I_{3k-2}\), which is contractible. This first cone makes the complex contractible. All remaining attachments are consequently nullhomotopic, and the other \(k\) noncontractible links yield exactly \(k\) spheres of dimension \(k\).
* For \(n=3k+2\), \(A=I_{3k+1}\) is contractible. Exactly \(2k+2\) indices \(i\not\equiv0\pmod3\) have \(A_i\simeq S^{k-1}\). Their cones split off \(2k+2\) spheres of dimension \(k\). When \(k=0\), each base is the formal empty complex and the two spokes add two points to the existing path-edge point, giving three components.

These cofiber calculations cover every integer \(n\ge2\) and use no field-dependent argument, proving the integral homotopy types.

## Verification
A standalone Python checker enumerates matchings directly from the graph edge list and constructs mod-two simplicial boundary matrices with exact integer bit arithmetic. It independently tests all \(14\) values \(2\le n\le15\) against the formula, including disconnected and higher-dimensional cases. Run `python3 checker/verify_fan_matching.py` from the package root; the expected last line is `FAN_MATCHING_COMPLEX_EXACT_MOD2_CHECKS_OK 14`. The file `checker/verification_output.txt` records the actual replay output. Mod-two calculations are corroboration, not a replacement for the integral cofibration proof.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega prove that the matching complex of every nonempty outerplanar graph is contractible or a wedge of spheres [1, Theorem 2]. Fan graphs are a canonical maximal outerplanar family, but that result does not determine the sphere dimension or multiplicity; those follow from the explicit spoke-link calculation here. Their earlier work on polygonal *line* tilings [2] treats strings of polygons with no triple intersection and does not contain the fan's common-apex family of adjacent triangles. Standard path independence-complex computations underlie the proof, but by themselves do not settle the maps from spoke links into the path-matching subcomplex. Searches for equivalent fan-matching formulas are recorded separately in the review; absence of a search hit does not prove novelty.

## Limitations
This is a nonequivariant homotopy classification of ordinary matching complexes of the apex-joined path only. It does not assert a natural symmetry-equivariant splitting, classify general outerplanar graphs, or determine other matching constraints. The wedge description is established homotopically, not as a PL homeomorphism of the original complex. Unindexed or differently titled prior formulas remain a possibility.

## References
[1] M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1, first submitted 2024-11-07, especially Theorem 2 and its proof. https://arxiv.org/abs/2411.04601

[2] M. Bayer, M. Jelić Milutinović, J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559, first submitted 2022-11-22, especially Definitions 12 and Theorem 13. https://arxiv.org/abs/2211.12559

[3] D. N. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122, for classical path independence-complex topology. The recurrence used here is also proved directly above.
