# Five symmetry orbits and the complete minimum zero-forcing time spectrum of cyclic prisms

## Finding
For each integer \(n\ge5\), let \(P_n=C_n\square K_2\), the cyclic prism on vertices \(u_i,v_i\) with subscripts in \(\mathbb Z/n\mathbb Z\), with cycle edges \(u_i u_{i+1}\), \(v_i v_{i+1}\), and rungs \(u_i v_i\). Under **standard** zero forcing with all permitted forces applied synchronously, \(Z(P_n)=4\). Every minimum zero-forcing set belongs to exactly one of the following five orbits under rim rotations, reflections and exchange of the two rings:

| Class | Representative four-set | Labelled sets | Synchronous propagation time |
| --- | --- | ---: | --- |
| A | \(\{u_0,u_1,v_0,v_1\}\) | \(n\) | \(\lfloor(n-1)/2\rfloor\) |
| B | \(\{u_0,u_1,u_2,u_3\}\) | \(2n\) | \(\lfloor(n+1)/2\rfloor\) |
| C | \(\{u_0,u_1,u_2,v_0\}\) | \(4n\) | \(\lfloor(n+1)/2\rfloor\) |
| D | \(\{u_0,u_1,v_0,v_{n-1}\}\) | \(2n\) | \(\lfloor n/2\rfloor\) |
| E | \(\{u_0,u_1,u_3,v_1\}\) | \(4n\) | \(\lfloor(n+3)/2\rfloor\) |

Consequently the number of minimum zero-forcing sets is exactly \(13n\). If \(F_n(z)=\sum_{|S|=4,\ S\text{ zero forcing}}z^{\operatorname{pt}(P_n,S)}\), then
\[
F_n(z)=\begin{cases}
nz^{m-1}+8nz^m+4nz^{m+1}, & n=2m,\\
3nz^m+6nz^{m+1}+4nz^{m+2}, & n=2m+1.
\end{cases}
\]
Both parities have three consecutive attainable propagation times. In particular the number of fastest minimum sets is \(n\) for even \(n\), and \(3n\) for odd \(n\).

## Assumptions and scope
Graphs are finite, undirected and simple. An initial blue set \(S\) forces a white vertex \(w\) in one round whenever an already-blue vertex has \(w\) as **its only white neighbor**; all simultaneously available forces occur each round. The propagation time \(\operatorname{pt}(P_n,S)\) is the least number of rounds needed to color all vertices blue, and is undefined for an unsuccessful set. The claim concerns all integers \(n\ge5\) and every four-vertex starting set. It does not assert the full zero-forcing polynomial (which counts larger successful starting sets), a result for positive-semidefinite forcing, or the exceptional triangular and square prisms.

## Proof
**1. Initial-force classification and minimum size.** Every vertex has degree three. A successful starting set smaller than four must contain a blue vertex with two blue neighbors to make its first force. Up to the symmetry group there are exactly two three-vertex patterns that enable an initial force: \(R=\{u_{n-1},u_0,u_1\}\), which initially forces \(v_0\), and \(M=\{u_{n-1},u_0,v_0\}\), which initially forces \(u_1\). For \(n\ge5\), in either three-set the new vertex has two white neighbors and all other blue vertices have at least two white neighbors. Thus the process stops after one round. Since every successful three-set would need one of these patterns, none exists; fewer than three cannot start. The four-set in class A succeeds by expanding two blue fronts on each ring, so \(Z(P_n)=4\). This also recovers, but does not newly claim, the known zero-forcing number in [1, Theorem 3.8].

**2. Exhaustive classification of four-sets.** Every successful four-set has a possible first force; deleting one of its four vertices leaves a forced-vertex wedge of type \(R\) or \(M\). Fix such a wedge. Inspection of the three neighbors of the newly forced vertex, and the other initially blue vertices, shows the only positions of a fourth vertex for which forcing continues past the initial round are
\[
\{u_2,u_{n-2},v_1,v_{n-1}\}.
\]
For the \(R\) wedge, the four completions belong respectively to classes B, B, C, C. For \(M\), they belong respectively to E, C, D, A. When the fourth vertex is elsewhere, exactly the one initial force can occur and the process then stops; all four completions in the list have a successful forcing trajectory as established below. This gives an exhaustive list of at most five orbits, and the arrival-time construction establishes that all are realized. Note that the geometric checks remain valid at \(n=5\), when boundary indices are close but distinct.

The graphs' cycle edges and rungs are distinguished by how many four-cycles contain them: for \(n\ge5\), a rim edge is in one four-cycle and a rung is in two. Thus the automorphisms are precisely the dihedral symmetries of the two aligned rims and the global ring exchange. Counting distinct translates and reflections of the five representatives gives orbit sizes, respectively, \(n,2n,4n,2n,4n\). The orbits do not overlap: this can be checked directly by the rung/rim incidence patterns of their induced four-vertex subgraphs, including their cyclic gaps. Summing gives \(13n\).

**3. Explicit arrival-time certificate.** Write \(T_i\), respectively \(B_i\), for the first round in which \(u_i\), respectively \(v_i\), is blue. An entry not listed in the following table is zero. All index ranges are integral, empty ranges are omitted:

| Class | Nonzero top-ring times \(T_i\) | Nonzero bottom-ring times \(B_i\) |
| --- | --- | --- |
| A | \(T_i=\min(i-1,n-i)\), \(2\le i\le n-1\) | \(B_i=T_i\), \(2\le i\le n-1\) |
| B | \(T_i=\min(i-1,n+2-i)\), \(4\le i\le n-1\) | \(B_0=B_3=2\), \(B_1=B_2=1\); \(B_i=T_i\) for \(4\le i\le n-1\) |
| C | \(T_{n-1}=1\); \(T_i=\min(i,n+1-i)\), \(3\le i\le n-2\) | \(B_i=\min(i,n+1-i)\), \(1\le i\le n-1\) |
| D | \(T_i=\min(i,n-i)\), \(2\le i\le n-1\) | \(B_i=\min(i,n-i)\), \(1\le i\le n-2\) |
| E | \(T_2=1\); \(T_i=\min(i,n+3-i)\), \(4\le i\le n-1\) | \(B_0=B_3=3\), \(B_2=2\); \(B_i=T_i\) for \(4\le i\le n-1\) |

For each row, let \(X_t\) denote vertices whose displayed arrival time is at most \(t\). The initial \(X_0\) is the representative four-set. Using \(N(u_i)=\{u_{i-1},u_{i+1},v_i\}\) and \(N(v_i)=\{v_{i-1},v_{i+1},u_i\}\), direct substitution of each piecewise minimum gives, for every \(t\ge0\),
\[
X_{t+1}\setminus X_t
=\bigl\{w\notin X_t:\ \exists x\in X_t\text{ with }N(x)\setminus X_t=\{w\}\bigr\}.
\]
For clarity, the only special initial delays not captured by the two advancing cycle fronts are the bottom-row values \((2,1,1,2)\) in B, the initial top vertex \(u_{n-1}\) in C, and the delays \(T_2=1\), \((B_0,B_2,B_3)=(3,2,3)\) in E. All remaining positive arrival times are minima of the arrival times from the clockwise and counterclockwise fronts; at the collision index both fronts give the same final round. The displayed identity can be verified on each interior interval by changing the index by one, and at the listed endpoints by the explicit special values. This supplies both a legal forcing witness and the exclusion of earlier forces. No vertex remains uncolored beyond the largest listed time.

Taking the maximum over the \(2n\) arrival times for each row gives the five propagation-time values in the finding. Multiplying by the orbit sizes, and collecting like powers separately for even and odd \(n\), yields \(F_n(z)\). The proof covers every \(n\ge5\) and does not extrapolate from a finite sample.

## Verification
The standalone Python program `verify_prism_python.py` enumerates every four-element starting set for \(5\le n\le18\), computes synchronous rounds independently of the formula, checks the five group orbits, and matches the exact histogram. The standalone C++17 program `verify_prism_cpp.cpp` independently enumerates all four-sets for \(5\le n\le25\) using bit-mask forcing and compares the same histogram. Its separately implemented arrival-time verifier independently checks all five displayed schedules for every \(5\le n\le300\). Both programs report their exact success markers when run; see `VERIFICATION.md`. These checks corroborate, but do not replace, the all-order case distinction in the proof.

## Relationship to prior work
AIM Minimum Rank–Special Graphs Work Group [1, Theorem 3.8] established \(Z(C_s\square P_t)=\min(s,2t)\), giving \(Z(P_n)=4\) for \(n\ge5\); its Theorem 3.9 treats Möbius ladders. Neither supplies minimum-set orbits or propagation-time multiplicities. Chilakamarri and collaborators [2] developed iteration indices; Hogben and collaborators [3] studied propagation time on general graphs and explicitly discussed a small prism. Boyer and collaborators [4] developed zero-forcing-set counting polynomials for other graph families, without the present minimum-set time enumerator. Thus the claimed contribution is precisely the prism five-orbit enumeration and exact weighted time distribution, not the established zero-forcing number or a general theorem for all cubic graphs.

## Limitations
The novelty assessment is based on inspected primary publications, indexed searches and comparative mathematical literature, not a proof of global historical priority. Unindexed or inaccessible calculations could duplicate this result. The symmetry classification is for the standard minimum-size forcing sets only. It does not classify larger initial sets or asynchronous forcing schedules. The exceptional prisms \(n=3,4\) have different classifications. Independent external validation is not claimed.

## References
[1] AIM Minimum Rank–Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* **428** (2008), 1628–1648, DOI: 10.1016/j.laa.2007.10.009; first publicly available online 2007-11-26, as printed on the publisher-formatted first page. OA: https://draganstevanovic.wordpress.com/wp-content/uploads/2012/09/published-version2.pdf.

[2] S. Chilakamarri, N. Dean, C. X. Kang, E. Yi, “Iteration index of a zero forcing set in a graph,” first arXiv submission 2011-05-08, https://arxiv.org/abs/1105.1492.

[3] L. Hogben, M. Huynh, N. Kingsley, S. Meyer, S. Walker, M. Young, “Propagation time for zero forcing on a graph,” first arXiv submission 2014-10-15, https://arxiv.org/abs/1410.4191.

[4] C. Boyer and collaborators, “The zero forcing polynomial of a graph,” first arXiv submission 2018-01-26, https://arxiv.org/abs/1801.08910; used for comparison, not archive-period anchoring.
