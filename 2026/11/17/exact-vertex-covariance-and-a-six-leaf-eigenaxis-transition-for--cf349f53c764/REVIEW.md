# Scientific review of the uniform-vertex covariance classification

## Correctness

**PASS.** The proof covers each integer \(q\ge3\). Its graph-theoretic step classifies acyclic edge-sign configurations of \(K_{2,q}\) as the union of two ternary product families, subtracting their common binary family. This produces exactly \(2\cdot3^q-2^q\) distinct vertices. Exact second-moment sums give the leaf-contrast, hub-difference and block-contrast covariance eigenvalues; permutation and hub-swap symmetries show these eigenvectors span the full zero-sum ambient space. Strict algebraic inequalities prove both the lowest eigenspace and the switch of the highest eigenspace at six leaves. The standalone standard-library checker independently reconstructs full exact-rational covariance matrices for seven graph sizes, including independent total-order enumerations for four sizes. Finite checks are supporting evidence, not the reason the all-size theorem holds.

## Originality

**PASS, with residual historical-priority risk.** Chapoton–Pilaud's complete-bipartite graphical-zonotope discussion and Carballosa–Khera–Reyes's complete-multipartite acyclic-orientation enumeration establish related encodings but do not state this Euclidean vertex covariance. Padrol–Pilaud–Poullot classify deformation cones, another invariant. Checked related results on complete-bipartite graphical-zonotope Löwner ellipsoids and complete-multipartite circumspheres determine enclosing shapes or farthest points; they do not imply a uniform distribution over the entire vertex set. Compared existing results on the same graph family's intrinsic-volume covariance, as well as vertex covariance restricted to cactus graphs: neither covers uniform-vertex covariance on \(K_{2,q}\) for \(q\ge3\), since the graph is not a cactus. Equivalence through lonesum matrices and degree-sequence moments remains a genuine search risk, not an established absence claim.

## Mathematical value

**PASS.** The exact discrete covariance spectrum is a natural, normalization-sensitive invariant of a standard infinite family of graph zonotopes. The result explains a sharp change of the principal Euclidean fluctuation axis at the smallest non-cactus complete bipartite family, with an exact all-size condition-number law growing quadratically. It is not a formal consequence of a vertex count or an enclosing ellipsoid, nor a randomly chosen parameter slice: this family is the first complete-bipartite family with multiple overlapping cycles, yet retains a tractable three-state encoding.

## Scope and limitations

The result uses equally weighted vertices of the unweighted centered zonotope and is not an intrinsic-volume covariance result. The previously known single-cycle boundary \(q=2\) is excluded from the novelty statement. The proof is exact for all \(q\ge3\); the experimental test set is finite. The literature check is extensive but cannot conclusively establish global historical priority. The review below is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
