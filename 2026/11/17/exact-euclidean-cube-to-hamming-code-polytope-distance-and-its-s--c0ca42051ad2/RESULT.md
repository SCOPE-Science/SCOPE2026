# Exact Euclidean cube-to-Hamming-code-polytope distance and its simplex projection faces

## Finding
For every integer \(m\ge2\), set \(n=2^m-1\). Let \(C_m\subseteq\{0,1\}^n\) be the binary Hamming code whose parity-check columns are precisely the \(n\) distinct nonzero vectors in \(\mathbb F_2^m\). Write \(P_m=\operatorname{conv}_{\mathbb R}(C_m)\subseteq[0,1]^n\). With the ambient Euclidean metric,
\[
\boxed{d_H^{(2)}([0,1]^n,P_m)^2=\frac4{n+3},\qquad d_H^{(2)}([0,1]^n,P_m)=\frac2{\sqrt{n+3}}.}
\]
All \(2^n-2^{n-m}\) cube vertices outside the code are exactly the farthest points. No nonvertex cube point is farthest, and each code vertex has distance zero. Every farthest vertex has a unique nearest point in \(P_m\), lying in the relative interior of an explicitly described simplex face of dimension \((n-1)/2\).

For a noncode binary vector \(v\), there is a unique coordinate \(i\) for which \(c=v\oplus e_i\in C_m\), where \(\oplus\) denotes coordinatewise addition modulo two. Let \(T_c:[0,1]^n\to[0,1]^n\) reflect coordinate \(j\) as \(x_j\mapsto1-x_j\) if \(c_j=1\), and leave it fixed otherwise. The unique nearest point to \(v\) is \(T_c(y^{(i)})\), where
\[
y^{(i)}_i=\frac{n-1}{n+3},\qquad
 y^{(i)}_j=\frac2{n+3}\quad(j\ne i).
\]
The exposed face containing \(y^{(i)}\) in its relative interior is
\[
F_i=\operatorname{conv}\bigl(\{0\}\cup\{e_i+e_j+e_k:\ h_i+h_j+h_k=0\text{ in }\mathbb F_2^m\}\bigr),
\]
where \(h_j\) is parity-check column \(j\); the face for \(v\) is \(T_c(F_i)\). For \(m=2\), \(F_i=P_m\) is an improper face; for \(m\ge3\), the face is proper.

## Assumptions and scope
Each \(h_i\) is a distinct nonzero binary \(m\)-vector, with the indexing arbitrary. The Hamming code comprises all words \(z\) satisfying \(\sum_{j:z_j=1}h_j=0\) in \(\mathbb F_2^m\). The polytope is the **true codeword convex hull**, rather than an intersection of individual parity-check relaxations. The Hausdorff distance is the maximum of the two directed Euclidean Hausdorff distances; here \(P_m\subseteq[0,1]^n\), so only the cube-to-polytope direction is nonzero. The theorem is an exact statement for all integers \(m\ge2\), without asymptotic or generic-position assumptions.

## Proof
**1. The code and its syndrome classes.** Every nonzero codeword has weight at least three: a weight-one word would require a zero check column, and a weight-two word would require repeated check columns. Given distinct indices \(i,j\), the vector \(h_i+h_j\) is nonzero and differs from \(h_i\) and \(h_j\); hence it is a third column \(h_k\), and \(e_i+e_j+e_k\) belongs to the code. For each fixed \(i\), the other \(n-1\) indices are partitioned into exactly \((n-1)/2\) disjoint pairs \(\{j,k\}\) with \(h_j+h_k=h_i\). The syndrome map has rank \(m\), so the code has \(2^{n-m}\) words. Every nonzero syndrome occurs as exactly one check column, proving the unique correction \(v\oplus e_i\in C_m\) and the count of noncode cube vertices.

**2. A feasible projection on an explicit simplex.** For fixed \(i\), average the \((n-1)/2\) weight-three codewords containing coordinate \(i\). Their mean \(u^{(i)}\) has entry \(1\) in coordinate \(i\) and \(2/(n-1)\) elsewhere. Consequently,
\[
 y^{(i)}=\frac{n-1}{n+3}u^{(i)}+\frac4{n+3}0\in P_m.
\]
The coefficient of every codeword in this expression, and of zero, is strictly positive. The nonzero generating words are affinely independent together with zero, because each pair \(\{j,k\}\) contributes two private non-\(i\) coordinates. Their convex hull therefore is an \((n-1)/2\)-simplex, and \(y^{(i)}\) lies in its relative interior.

**3. A global supporting-hyperplane certificate.** Set \(r=e_i-y^{(i)}\). Then \((n+3)r_i=4\) and \((n+3)r_j=-2\) for every \(j\ne i\). For any binary codeword \(z\),
\[
 (n+3)\langle r,z\rangle=6z_i-2\operatorname{wt}(z)\le0.
\]
Indeed, the zero word gives equality, and a nonzero word has weight at least three; equality occurs precisely when \(z_i=1\) and \(\operatorname{wt}(z)=3\). Thus \(\langle r,z\rangle\le0\) throughout \(P_m\), and its equality face is exactly \(F_i\). Direct substitution yields \(\langle r,y^{(i)}\rangle=0\). Hence \(\langle e_i-y^{(i)},z-y^{(i)}\rangle\le0\) for all \(z\in P_m\), the necessary-and-sufficient Euclidean metric-projection inequality. Strict convexity of squared Euclidean distance gives uniqueness. Finally,
\[
 \lVert e_i-y^{(i)}\rVert_2^2=\frac{16+4(n-1)}{(n+3)^2}=\frac4{n+3}.
\]

**4. All other binary vertices.** If \(c\in C_m\), the coordinate reflection \(T_c\) is an affine Euclidean isometry preserving both the cube and \(P_m\), because modulo-two translation by a codeword permutes the code. Each noncode vertex \(v=T_c(e_i)\) therefore has the same unique projection and the same squared distance. Each code vertex lies in \(P_m\) and has distance zero.

**5. No nonvertex maximizers.** Write any cube point \(x\) as a convex combination \(\sum_a\lambda_a v^{(a)}\) of binary cube vertices, and let \(p_a\) be the unique projection of \(v^{(a)}\) to \(P_m\), with residual \(r_a=v^{(a)}-p_a\). Since \(\sum_a\lambda_a p_a\in P_m\), the variance identity gives
\[
\operatorname{dist}(x,P_m)^2\le
\sum_a\lambda_a\operatorname{dist}(v^{(a)},P_m)^2
-\frac12\sum_{a,b}\lambda_a\lambda_b\lVert r_a-r_b\rVert_2^2.
\]
If any vertex carrying positive mass belongs to the code, the first term is strictly less than \(4/(n+3)\), unless the combination is a single noncode vertex. Otherwise all support vertices are noncode. For such a vertex, its residual has one coordinate with magnitude \(4/(n+3)\) (the syndrome coordinate), and all others have magnitude \(2/(n+3)\). Its signs encode the correcting codeword \(c\). Thus **distinct noncode vertices have distinct residuals**: different syndrome coordinates change the location of the large entry; a common syndrome coordinate and different correcting codewords change a sign. Any nontrivial convex combination of distinct noncode vertices has a strictly negative variance term. Every nonvertex cube point is such a nontrivial combination, so its distance is strictly smaller than \(2/\sqrt{n+3}\). The upper bound is attained by every noncode cube vertex, completing all statements.

## Verification
The accompanying standard-library script `hamming_hull_checker.py` performs exact integer/rational tests for \(m=2,3,4\), including all codewords against each candidate supporting hyperplane and an exact count of its equality codewords. It also samples 2,000 codewords at each of \(m=5,6,7\). The independent script `hamming_numeric_projection.py` solves the nearest-point quadratic program directly in codeword convex-combination coordinates for \(m=2,3\) using NumPy and SciPy. It agrees with the exact formula within numerical precision. These finite checks test the formulas; the proof for every \(m\) is the preceding symbolic argument.

## Relationship to prior work
The standard codeword-polytope framework and codeword-translation face symmetries appear in Kashyap's *On the Convex Geometry of Binary Linear Codes* (2006). Gensheimer et al. (2019) analyze Euclidean projection onto the **single** parity-check (even/odd) polytopes relevant to LP decoding; the simultaneous Hamming codeword hull studied here is a different, generally smaller polytope. Coregliano, Jeronimo and Jones (2021) study LP hierarchies for code-size bounds, not this ambient Euclidean projection invariant. For a binary cube vertex, distance to a codeword convex hull is also the convex distance used in Talagrand-type settings; this equivalent reformulation is acknowledged, not asserted as a separate contribution. No equivalent all-length Hamming-code formula or full nearest-point/face classification was identified in the inspected sources or focused record searches. The absence of a match is not proof of historical priority.

## Limitations
The precise formula is for the standard binary Hamming code of length \(2^m-1\) in the unweighted ambient Euclidean metric, not for shortened, punctured, extended, nonlinear, or arbitrary perfect codes. The nearest **discrete codeword** is at Hamming/Euclidean distance one from every noncode cube vertex; that distinct discrete distance is not the convex-hull distance. These statements do not identify the nearest point for arbitrary nonbinary cube inputs. Independent external mathematical validation has not been performed, and historical priority remains subject to specialist scrutiny.

## References
1. F. Gensheimer, T. Dietz, K. Kraft, S. Ruzika and N. Wehn, *A Reduced-Complexity Projection Algorithm for ADMM-based LP Decoding*, arXiv:1901.03240, initially public 2019-01-10. https://arxiv.org/abs/1901.03240
2. N. Kashyap, *On the Convex Geometry of Binary Linear Codes*, presented 2006. https://ece.iisc.ac.in/~nkashyap/Papers/code_geometry.pdf
3. L. Coregliano, F. Jeronimo and C. Jones, *A Complete Linear Programming Hierarchy for Linear Codes*, arXiv:2112.09221, initially public 2021-12-16. https://arxiv.org/abs/2112.09221
