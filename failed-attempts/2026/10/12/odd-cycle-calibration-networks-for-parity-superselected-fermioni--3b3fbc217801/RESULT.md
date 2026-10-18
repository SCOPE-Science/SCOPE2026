# Odd-cycle calibration networks for parity-superselected fermionic Lindbladian learning
## Finding
Consider the internal-marker calibration mechanism for parity-superselected fermionic Lindbladian learning. Let \(V\) be a finite set of internal marker cores and let \(G=(V,E)\) record the marker pairs for which the source paper's termwise-separation condition holds and a pair response is measured. For marker \(i\), write \(b_i\) for its dynamical correction, and for a measured pair \(ij\in E\), write \(s_{ij}\) for the normalized short-time pair response. Proposition 5.8 of the source gives
\[
s_{ij}=b_i+b_j.
\]
Let \(B_G\) be the unsigned edge-vertex incidence matrix: the row for edge \(ij\) has a \(1\) in columns \(i\) and \(j\) and zeros elsewhere. Then
\[
s=B_Gb,
\qquad
Q_G:=B_G^{\mathsf T}B_G=D_G+A_G,
\]
where \(Q_G\) is the signless Laplacian of \(G\).

The marker corrections are uniquely identifiable from the measured pair responses if and only if every connected component of \(G\) is non-bipartite, equivalently every component contains an odd cycle. In that case
\[
b=Q_G^{-1}B_G^{\mathsf T}s.
\]
For noisy pair data \(\widetilde s=s+e\), the least-squares estimator
\[
\widehat b=Q_G^{-1}B_G^{\mathsf T}\widetilde s
\]
satisfies
\[
\|\widehat b-b\|_2
\le
\frac{\|e\|_2}{\sqrt{\lambda_{\min}(Q_G)}}.
\]
Hence if every measured pair has absolute error at most \(\eta\),
\[
\|\widehat b-b\|_2
\le
\frac{\sqrt{|E|}}{\sqrt{\lambda_{\min}(Q_G)}}\,\eta.
\]

This gives a complete sparse-access criterion for the calibration layer. With completely unknown marker corrections and pair responses only, at least as many measured pairs as markers are necessary. Equality \(|E|=|V|\) is possible exactly when every connected component is an odd unicyclic graph. Therefore the source's three-marker triangle is simultaneously marker-minimal and edge-minimal, but pairwise separation of every pair in a larger marker set is unnecessary: any measurement graph whose components contain odd cycles is sufficient.

For the connected odd cycle \(C_q\), where \(q\ge3\) is odd,
\[
\lambda_{\min}(Q_{C_q})
=4\sin^2\!\left(\frac{\pi}{2q}\right),
\]
so edgewise error at most \(\eta\) gives the explicit bound
\[
\|\widehat b-b\|_2
\le
\frac{\sqrt q}{2\sin(\pi/(2q))}\,\eta.
\]
The triangle \(C_3\) recovers the three equations and inversion used in the source paper.

## Assumptions and scope
The underlying dynamics are those of the source paper: a time-independent parity-covariant local fermionic Lindbladian with internal Majorana markers. The only source-specific input used here is the proved pair-calibration identity \(s_{ij}=b_i+b_j\), which requires the two marker cores associated with a measured edge to be termwise separated. To apply the recovered \(b_i\) to a target odd probe through the source's correction theorem, marker \(i\) must also be termwise separated from that target.

The graph \(G\) describes available valid pair measurements; it is not the physical interaction graph. A non-edge imposes no calibration equation and need not be a termwise-separated pair. The result does not assert that every abstract calibration graph can be embedded in every physical geometry. It gives the exact algebraic condition that the available valid pair measurements must satisfy.

No assumption of independent measurement noise is needed for the deterministic stability inequality. The error vector \(e\) may be arbitrary. The componentwise error hypothesis \(|e_{ij}|\le\eta\) is used only to bound \(\|e\|_2\le\sqrt{|E|}\eta\).

## Proof
For each measured edge \(ij\), the source identity is \(s_{ij}=b_i+b_j\). Stacking these equations gives \(s=B_Gb\).

To determine when \(B_G\) has full column rank, first consider one connected component. A vector \(x\) lies in \(\ker B_G\) exactly when
\[
x_i+x_j=0
\]
for every edge \(ij\). Along a path, the values therefore alternate between \(t\) and \(-t\). If the component is bipartite, assigning \(t\) to one color class and \(-t\) to the other gives a nonzero kernel vector. Conversely, if the component contains an odd cycle, alternating signs around that cycle forces \(t=-t\), hence \(t=0\); connectedness then forces every coordinate in the component to vanish. Applying the argument componentwise proves that \(B_G\) has full column rank exactly when every component is non-bipartite.

Since
\[
Q_G=B_G^{\mathsf T}B_G,
\]
full column rank is equivalent to positive definiteness of \(Q_G\). Multiplying \(s=B_Gb\) by \(B_G^{\mathsf T}\) therefore gives
\[
b=Q_G^{-1}B_G^{\mathsf T}s.
\]
This is the standard signless-Laplacian normal equation.

For noisy data, the least-squares error is
\[
\widehat b-b=B_G^{\dagger}e,
\]
where \(B_G^{\dagger}\) is the left pseudoinverse. Its operator norm is
\[
\|B_G^{\dagger}\|_2
=\frac{1}{\sigma_{\min}(B_G)}
=\frac{1}{\sqrt{\lambda_{\min}(Q_G)}}.
\]
This proves the stated stability inequality.

For the edge-count statement, a non-bipartite connected component with \(v\) vertices contains a cycle and hence has at least \(v\) edges. Summing over components gives \(|E|\ge|V|\). Equality holds exactly when every component is unicyclic; identifiability further forces its unique cycle to be odd. With fewer than three marker vertices no simple non-bipartite graph exists, so the source's triangle is marker-minimal. Its three edges also meet the lower bound \(|E|\ge|V|\).

Finally, for \(C_q\),
\[
Q_{C_q}=2I+A(C_q).
\]
The adjacency eigenvalues are \(2\cos(2\pi k/q)\). For odd \(q\), the smallest signless-Laplacian eigenvalue is therefore
\[
2-2\cos\!\left(\frac{\pi}{q}\right)
=4\sin^2\!\left(\frac{\pi}{2q}\right),
\]
which gives the displayed cycle stability bound.

## Verification
The proof above is analytic and applies to every finite calibration graph. A standalone standard-library checker in `artifacts/verify.py` corroborates exact recovery on odd cycles of lengths \(3,5,7,9\), exhibits the alternating kernel on an even cycle, and checks the closed form for the least signless-Laplacian eigenvalue of the tested odd cycles. It returns `VERIFY_OK` when run from the packaged path. These finite checks are not used as a proof of the general statement.

## Relationship to prior work
Möbus, Stilck França, and Rouzé introduce internal markers for parity-superselected local fermionic Lindbladian learning and calibrate three separated markers from all three pair responses. Their abstract and main-results discussion explicitly describe a three-marker calibration mechanism, and their Proposition 5.8 supplies the pair identity used here. The present result keeps that physical identity but treats the available valid pair measurements as an arbitrary graph, yielding an if-and-only-if identifiability condition, a sparse odd-cycle replacement, an edge-minimality statement, and a quantitative conditioning bound.

The matrix \(Q_G=D_G+A_G\) and its connection to bipartiteness belong to the classical theory of signless graph Laplacians. The new point here is not a new graph-spectral theorem: it is the exact reduction of the recent fermionic marker-calibration problem to that structure and the resulting access and stability consequences for this learning protocol.

## Limitations
This is a calibration-layer theorem. It does not, by itself, replace every geometric-access assumption in the source's full learning theorem, nor does it establish the same sample-complexity constants for an arbitrary marker network. Any full protocol using a new marker graph must still realize the required even preparations and measurements, target-marker separation, locality conditions, and block-frame access.

The result assumes exact validity of the source pair identity on the selected edges. If a physical system only approximately satisfies termwise separation, the resulting model bias must be added to the error vector and bounded separately. No claim of optimal marker-network conditioning is made beyond the exact identifiability and edge-count statements.

## References
1. T. Möbus, D. Stilck França, and C. Rouzé, “Learning Local Fermionic Lindbladians under Parity Superselection,” arXiv:2610.00448v1, first submitted 2026-09-30.
2. D. Cvetković, P. Rowlinson, and S. Simić, “Signless Laplacians of finite graphs,” Linear Algebra and its Applications 423 (2007), 155–171, DOI:10.1016/j.laa.2007.01.009.
