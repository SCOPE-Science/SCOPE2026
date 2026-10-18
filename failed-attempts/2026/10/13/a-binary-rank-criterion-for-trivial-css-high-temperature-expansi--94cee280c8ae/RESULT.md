# A binary-rank criterion for trivial CSS high-temperature expansions
## Finding
For a star-connected finite region \(R\), let \(\mathbb S_R\) be the set of relevant star interactions in the high-temperature expansion and define the binary incidence matrix
\[
B_R\in\mathbb F_2^{R\times\mathbb S_R},\qquad (B_R)_{v,s}=1\iff v\in ds.
\]
For a subset \(T\subseteq\mathbb S_R\), write \(t\in\mathbb F_2^{\mathbb S_R}\) for its indicator vector. The coboundary parity relation is exactly
\[
B_Rt=\mathbf 1_{dT\cap R}.
\]
Hence the subsets that survive the source paper's local high-temperature selection rule \(dT\cap R=\emptyset\) are precisely the vectors in \(\ker_{\mathbb F_2}B_R\). In particular, their number is exactly
\[
2^{\dim\ker B_R}.
\]
The source's “trivial high-temperature expansion” requires that the only such subset be \(T=\emptyset\), except that \(T=\mathbb S_R\) is also permitted when \(d\mathbb S_R\cap R=\emptyset\). Therefore the condition is equivalent to
\[
\ker_{\mathbb F_2}B_R=\{0\}\quad\text{if }B_R\mathbf 1\ne0,
\qquad
\ker_{\mathbb F_2}B_R=\operatorname{span}\{\mathbf1\}\quad\text{if }B_R\mathbf1=0.
\]
Equivalently,
\[
\dim\ker B_R=\mathbf1_{\{B_R\mathbf1=0\}}.
\]
Thus the exact obstruction is excess binary nullity, rather than vertex degree by itself.

This criterion is strictly broader than the sufficient degree-two condition used in Corollary 2.7 of the source. For example,
\[
B=\begin{pmatrix}1&1&1\\1&0&0\\0&1&0\end{pmatrix}
\]
is invertible over \(\mathbb F_2\). Its first row has weight three and the associated star-qubit incidence graph is connected, yet \(\ker B=\{0\}\); therefore no nonempty star subset satisfies the local parity-cancellation condition.

For a translation-invariant CSS family in which every relevant rectangle is star-connected, if the displayed rank criterion holds for every star-connected region required by Definition 2.5, then the star part has the source's trivial high-temperature expansion. Theorem 2.6 of the source then yields its Dobrushin-Shlosman condition at every finite inverse temperature. The plaquette version follows by exchanging stars and plaquettes.

## Assumptions and scope
The statement concerns the star or plaquette high-temperature expansion used in the cited CSS thermalization paper. The region \(R\) is finite and connected in the corresponding interaction incidence graph, and \(\mathbb S_R\) is exactly the source paper's set of interactions relevant to that region. The criterion does not alter the paper's additional geometric hypotheses, such as connectedness of rectangles, nor does it by itself establish a modified logarithmic Sobolev inequality for a family that fails those hypotheses.

The matrix is over \(\mathbb F_2\). Multiple interactions with the same incidence pattern are allowed and are automatically detected as column dependencies. No assumption of bounded interaction degree is used in the equivalence.

## Proof
For any \(T\subseteq\mathbb S_R\), the product of the corresponding star operators is
\[
\prod_{s\in T}A_s=\bigotimes_{v\in dT}X_v,
\]
as in the source paper. A qubit \(v\) belongs to \(dT\) exactly when it is incident to an odd number of stars in \(T\). With \(t\) the indicator of \(T\), this parity is the \(v\)-th component of \(B_Rt\). Consequently
\[
dT\cap R=\emptyset\iff B_Rt=0.
\]
The map \(T\mapsto t\) is a bijection between subsets of \(\mathbb S_R\) and binary column vectors, so exactly \(2^{\dim\ker B_R}\) subsets obey the selection rule.

Definition 2.5 and the proof of Corollary 2.7 in the source identify a trivial expansion with the statement that the selection rule holds only for \(T=\emptyset\) and, when its full product has no support in \(R\), also for \(T=\mathbb S_R\). The latter subset corresponds to \(\mathbf1\), and
\[
d\mathbb S_R\cap R=\emptyset\iff B_R\mathbf1=0.
\]
If \(B_R\mathbf1\ne0\), triviality is therefore equivalent to \(\ker B_R=\{0\}\). If \(B_R\mathbf1=0\), then \(\mathbf1\in\ker B_R\), and triviality is equivalent to the kernel having exactly the two vectors \(0\) and \(\mathbf1\), namely \(\ker B_R=\operatorname{span}\{\mathbf1\}\). Rank-nullity gives the scalar form of the criterion.

For the displayed \(3\times3\) example, row reduction over \(\mathbb F_2\) gives rank three, so its kernel is zero although one qubit meets three interactions. This proves that the degree-two hypothesis is not necessary for the local trivial-expansion property.

Finally, when the rank criterion holds on every region required in Definition 2.5, that definition is satisfied exactly. The downstream Dobrushin-Shlosman conclusion is then an application of the source's Theorem 2.6, not a new proof of that theorem.

## Verification
The accompanying `artifacts/verify.py` implements exact Gaussian elimination over \(\mathbb F_2\), enumerates all subsets for small incidence matrices, and verifies that the enumerated solutions of \(B_Rt=0\) agree with the kernel dimension and with the two-case triviality criterion. It also verifies the rank-three example above. These finite computations corroborate the algebraic identities; the proof for arbitrary finite \(R\) is the rank-nullity argument above.

## Relationship to prior work
Stengele, Capel, Gao, Lucia, Pérez-García, Pérez-Hernández, Rouzé, and Warzel define trivial high-temperature expansion and prove that it implies a Dobrushin-Shlosman condition at every finite inverse temperature under their rectangle-connectivity hypothesis. Their Corollary 2.7 supplies the local sufficient condition that every qubit meet at most two stars (or, dually, at most two plaquettes). Its proof explicitly reduces the issue to showing that \(dT\cap R=\emptyset\) occurs only for the empty subset and possibly the full interaction set. The present result isolates that same condition as an exact binary-kernel criterion, thereby separating the algebraic obstruction from the degree-two sufficient hypothesis.

The interpretation of even-incidence subsets as a binary cycle space is classical in high-temperature expansions and coding theory. No novelty is claimed for binary incidence kernels themselves. The new point assessed here is the exact necessary-and-sufficient use of that invariant for the source paper's specific two-term CSS expansion condition, together with the immediate higher-degree admissibility test.

Focused searches for the source identifier and for equivalent formulations involving CSS high-temperature expansions, binary incidence kernels, cycle spaces, Dobrushin-Shlosman conditions, and rank criteria did not locate a published statement implying this exact criterion in the source's setting. Because the anchor is recent, unindexed equivalent observations remain a residual risk.

## Limitations
The rank criterion characterizes only the source's trivial high-temperature expansion condition. It does not show that families with larger kernel dimension fail all possible Dobrushin-Shlosman arguments, nor does it quantify mixing when the expansion has more than two terms. The local degree-three matrix is a finite incidence witness; it is not presented as a complete translation-invariant lattice model. The result also does not weaken the source's rectangle-connectivity assumptions or reprove its modified logarithmic Sobolev inequality.

## References
1. S. Stengele, Á. Capel, L. Gao, A. Lucia, D. Pérez-García, A. Pérez-Hernández, C. Rouzé, and S. Warzel, “Modified Logarithmic Sobolev Inequalities for CSS Codes,” arXiv:2510.03090v1; Communications in Mathematical Physics 407 (2026), Article 195, DOI:10.1007/s00220-026-05654-w.
2. Mathematics Subject Classification 2020, 82C10: quantum dynamics and nonequilibrium statistical mechanics (general).
