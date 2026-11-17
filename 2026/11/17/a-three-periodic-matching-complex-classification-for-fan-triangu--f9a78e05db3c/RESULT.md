# A three-periodic matching-complex classification for fan triangulations

## Finding
Let \(P_n\) be the path on vertices \(1,\ldots,n\), and let \(F_n=K_1\vee P_n\) denote its graph join with one new apex (the *fan* graph). For every integer \(n\ge3\), its ordinary matching complex, whose vertices are graph edges and whose faces are pairwise disjoint sets of edges, has the following **integral homotopy type**:

\[
\mathcal M(F_n)\simeq
\begin{cases}
\bigvee^{q+1}S^{q-1},&n=3q,\quad q\ge1,\\
\bigvee^{q}S^{q},&n=3q+1,\quad q\ge1,\\
\bigvee^{2q+2}S^{q},&n=3q+2,\quad q\ge1.
\end{cases}
\]

In particular, all reduced integral homology is free, supported in one degree, and has precisely the displayed rank. The first cases \(n=3,4,5,6,7,8,9\) have respective types \(\bigvee^2S^0\), \(S^1\), \(\bigvee^4S^1\), \(\bigvee^3S^1\), \(\bigvee^2S^2\), \(\bigvee^6S^2\), and \(\bigvee^4S^2\).

## Assumptions and scope
Graphs are finite, simple and undirected. \(P_m\) has \(m\) vertices and \(m-1\) edges, for \(m\ge1\); \(P_0\) is the empty graph. \(F_n\) has vertices \(0,1,\ldots,n\) and edges \(\{i,i+1\}\), \(1\le i<n\), together with spokes \(\{0,i\}\), \(1\le i\le n\). Thus \(F_n\) is the canonical fan triangulation of an \((n+1)\)-gon and a maximal outerplanar graph. The theorem concerns ordinary matching complexes, not perfect-matching complexes and not line-tiling families whose triangles alternate between two rim chains. The symbol \(\bigvee^b S^d\) is the wedge of \(b\) copies of the \(d\)-sphere. At \(n=3\), \(S^0\) means a two-point space and the wedge has three connected components.

## Proof
**1. Path matching complexes.** Write \(A_m=\mathcal M(P_m)\). Since the line graph of \(P_m\) is \(P_{m-1}\), \(A_m\) is the independence complex of \(P_{m-1}\). For \(m\ge5\), delete the vertex of that independence complex corresponding to the penultimate path edge. The deletion is a cone because the final path edge becomes isolated in the remaining line graph; the link is \(A_{m-3}\). The simplicial deletion/link cofiber sequence consequently gives \(A_m\simeq\Sigma A_{m-3}\). The initial values are the formal join unit \(A_0=A_1=S^{-1}\) (the complex containing only the empty face), \(A_2\simeq *\), \(A_3\simeq S^0\), and \(A_4\simeq S^0\) (the last two are direct small-path calculations). Therefore

\[
A_m\simeq
\begin{cases}
S^{t-1},&m=3t,\ t\ge1,\\
S^{t-1},&m=3t+1,\ t\ge1,\\
*,&m=3t+2,\ t\ge0.
\end{cases}
\]

For \(m=0,1\), \(S^{-1}\) is **only a formal join unit** in the expressions below; the small \(n=3\) case is handled separately, so no invalid geometric suspension of an empty realization is used. The path recurrence follows equally from the familiar three-step independence-complex recurrence.

**2. The apex-spoke decomposition.** Let \(A=\mathcal M(P_n)\), viewed inside \(\mathcal M(F_n)\) as the matchings using no spoke. Write \(s_i=\{0,i\}\) and

\[
L_i=\mathcal M(P_{i-1})*\mathcal M(P_{n-i}).
\]

A matching can use at most one spoke. The matching complex is therefore exactly the union of \(A\) and the \(n\) distinct simplicial cones \(s_i*L_i\), all attached to \(A\) along \(L_i\); the interiors containing different spokes are disjoint. Here the join with the formal \(A_0\) or \(A_1\) leaves the other factor unchanged. The link \(L_i\) is contractible if either path factor is contractible. The path classification, together with the dimension formula for joins of spheres, gives the complete list of noncontractible links:

\[
\begin{array}{c|c|c|c}
n&\text{indices }i&\text{number}&\text{type of each }L_i\\\hline
3q&i\equiv2\pmod3&q&S^{q-2}\\
3q+1&i\equiv1\pmod3&q+1&S^{q-1}\\
3q+2&i\not\equiv0\pmod3&2q+2&S^{q-1}.
\end{array}
\]

All other links are nonempty contractible complexes for \(n\ge4\), and their cone attachments do not change the homotopy type. Multiple cone attachments along specified nullhomotopic inclusions split as a wedge of suspensions of their links, along with the original space; this is the standard cofibration/mapping-cone property, applied to the independent spoke cones.

**3. The three residue classes.** For \(n=3q+2\) with \(q\ge1\), \(A\) is contractible. All \(2q+2\) noncontractible links are \(S^{q-1}\) and their attachments are nullhomotopic, yielding \(\bigvee^{2q+2}S^q\).

For \(n=3q\) with \(q\ge2\), \(A\simeq S^{q-1}\). The \(q\) noncontractible links are \(S^{q-2}\), and every map from such a sphere to \(A\) is nullhomotopic because \(S^{q-1}\) is \((q-2)\)-connected (the disconnected-source case \(q=2\) follows from path-connectedness). Thus the result is \(S^{q-1}\vee\bigvee^q S^{q-1}\). When \(q=1\), \(F_3\) has five edges and its matching complex is a graph with five vertices, two edges and three components; it is \(\bigvee^2 S^0\).

For \(n=3q+1\), the spoke-one link is \(L_1=\mathcal M(P_{3q})\), included in \(A=\mathcal M(P_{3q+1})\). This inclusion is a homotopy equivalence: adding the endpoint rim edge \(\{1,2\}\) to the induced path on vertices \(2,\ldots,n\) attaches a cone along \(\mathcal M(P_{3q-1})\), which is contractible by step 1. Attaching the cone for spoke one therefore makes the initial space contractible. Each of the remaining \(q\) noncontractible links is \(S^{q-1}\); its inclusion into this contractible intermediate space is nullhomotopic, and each independent cone contributes one \(S^q\). This proves \(\bigvee^q S^q\), completing the classification for every \(n\ge3\).

## Verification
The accompanying standalone Python program `verify_fan.py` exhaustively enumerates the ordinary simplices of \(\mathcal M(F_n)\) for every \(3\le n\le18\), constructs every augmented mod-two simplicial boundary and computes ranks directly over \(\mathbb F_2\). For all sixteen sizes it reproduces the predicted single nonzero reduced Betti number, processing 93,822 nonempty simplices in total. Independently, a signed matching-polynomial recurrence checks the resulting Euler characteristics and the residue-class link counts for \(3\le n\le300\). Execute `python3 verify_fan.py` with ordinary Python 3. These finite tests corroborate, but do not substitute for, the all-integer homotopy proof above.

## Relationship to prior work
The outerplanar matching-complex theorem of Bayer, Jelić Milutinović and Vega, initially public on November 7, 2024, proves that every outerplanar graph has a contractible or sphere-wedge matching complex; it does **not** give the fan's exact dimensions and multiplicities. The same authors' November 2022 work gives explicit results for **alternating triangular line tilings**; those graphs differ from fan graphs for long chains. For example, the four-triangle line tiling in that paper has maximum vertex degree four, while the four-triangle fan \(F_5\) has a degree-five apex and matching-complex type \(\bigvee^4 S^1\). The path matching-complex periodicity and the deletion/link cofiber technique are standard prior tools, not claimed as new here. The new statement is the exact three-class integral homotopy formula for the full infinite fan family.

## Limitations
No equivariant action, natural basis for the integral homology, or general theorem about all maximal outerplanar graphs is claimed. The proof is fully nonequivariant and applies to fan triangulations only. The literature comparison is limited to indexed searches and the inspected primary articles; independent external novelty and correctness audits have not been performed.

## References
1. M. Bayer, M. Jelić Milutinović, and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v1 (first public November 7, 2024; the updated manuscript was also inspected). https://arxiv.org/abs/2411.04601
2. M. Bayer, M. Jelić Milutinović, and J. Vega, *General polygonal line tilings and their matching complexes*, arXiv:2211.12559 (first public November 22, 2022). https://arxiv.org/abs/2211.12559
3. D. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122 (classical path independence-complex periodicity; also reproved here).
