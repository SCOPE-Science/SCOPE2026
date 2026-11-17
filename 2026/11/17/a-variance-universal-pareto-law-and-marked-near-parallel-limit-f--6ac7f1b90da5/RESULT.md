# A variance-universal Pareto law and marked near-parallel limit for random-line triangles

## Finding
Take three independent random planar lines with independent normal angles \(\Theta_i\) sampled from a continuous probability density \(g\) on \([0,\pi]\), and signed offsets \(H_i\) drawn independently from the same nonconstant distribution supported in \([-B,B]\). The angle and offset samples are independent. Write \(v=\operatorname{Var}(H_i)>0\). Almost surely the three pairwise intersections are well defined; let \(T\) be the area of their convex hull (which may be zero for an atomic offset law). Then
\[
\boxed{\lim_{t\to\infty}t\,\Pr\{T>t\}=6v\int_0^\pi g(\theta)^2\,d\theta.}
\]
Thus the large-area law depends on the offsets only through their variance, even if the offset distribution has atoms. Every positive area moment exists precisely below order one. Among all such angular densities, the coefficient has the sharp minimum \(6v/\pi\), with equality only for uniform angular sampling.

A *marked* version identifies the rare configurations. On \(\{T>t\}\), let \(\{I_t,J_t\}\) denote the uniquely closest pair of line directions in projective angular distance (ties have probability zero), and let \(K_t\) be the remaining index. Define
\[
\delta_t=|\Theta_{I_t}-\Theta_{J_t}|,\quad
D_t=H_{I_t}-H_{J_t},\quad
W_t=\frac{2t\,\delta_t}{D_t^2}.
\]
For definiteness define \(W_t=0\) when \(D_t=0\). As \(t\to\infty\), conditional on \(T>t\), the unordered pair \(\{I_t,J_t\}\) becomes uniform on the three index pairs; its common angular location \(\Theta_{I_t}\) has limiting density \(g^2/\int g^2\); the pair of offsets has limiting joint law weighted by \((H_i-H_j)^2/(2v)\); the unused line retains its original independent angular and offset laws; and the limiting value of \(W_t\) is independent \(\operatorname{Uniform}(0,1)\). The signed small angular displacement has an independent fair sign. These claims hold jointly in the sense of weak convergence for bounded continuous test functions. In particular, \(T/t\), conditioned on \(T>t\), tends in law to \(1/W\) with \(W\sim\operatorname{Uniform}(0,1)\).

## Assumptions and scope
For \(i=1,2,3\), put \(n(\theta)=(\cos\theta,\sin\theta)\) and \(L_i=\{x\in\mathbb R^2:n(\Theta_i)\cdot x=H_i\}\). All six sampling variables are independent except for sharing their respective common laws. The density \(g:[0,\pi]\to[0,\infty)\) is continuous and integrates to one; it need not be symmetric or strictly positive. The offset distribution may be discrete or continuous but is supported on a fixed bounded interval, and its variance is strictly positive. Angles are unoriented normal directions on the half-open projective fundamental domain; the signed offsets follow that fixed convention. If all lines happen to be concurrent, their convex hull has zero area; the theorem does not exclude that event. The tail parameter \(t\) has units of Euclidean area and tends to infinity with all sampling laws fixed. The pair index is formed by minimizing \(|\sin(\Theta_i-\Theta_j)|\); its almost-sure uniqueness is sufficient. On the conditional event the near-parallel pair is asymptotically away from the projective seam, so the ordinary angular difference is the correct displacement in the marked limit.

The limiting offset-pair law is characterized without densities: for bounded measurable \(\phi\),
\[
\mathbb E_*[\phi(H_i,H_j)]
=\frac{\mathbb E[\phi(H_i,H_j)(H_i-H_j)^2]}{2v}.
\]
The two offset marks need not remain independent under this size bias. All other independence statements above refer to the limiting marked law, not exact finite-threshold independence.

## Proof
**1. Exact area formula.** Define
\[
a=\sin(\Theta_2-\Theta_3),\quad
b=\sin(\Theta_3-\Theta_1),\quad
c=\sin(\Theta_1-\Theta_2).
\]
Cramer's rule for the three pairwise line intersections and the determinant formula for triangle area give the exact identity
\[
T=\frac{(H_1a+H_2b+H_3c)^2}{2|abc|}.
\tag{1}
\]
All denominators are nonzero almost surely because \(g\) is continuous.

**2. Exceedances require near-parallel directions.** The three numbers \(x=|a|\), \(y=|b|\), \(z=|c|\) satisfy the triangle inequalities by the sine addition identity and \(|\sin(s+t)|\le|\sin s|+|\sin t|\). Hence \((x+y+z)^2\le4(xy+yz+zx)\). Since \(|H_i|\le B\), (1) implies
\[
T\le2B^2\left(\frac1x+\frac1y+\frac1z\right).
\tag{2}
\]
Consequently \(T>t\) requires at least one of the three pairwise sines to have magnitude below \(6B^2/t\). By boundedness of \(g\), the probability of two distinct such pair-collisions is \(O(t^{-2})\). If two directions differ by nearly \(\pi\), the event requires one angle near zero and the other near \(\pi\), likewise of probability \(O(t^{-2})\). Thus to first order only one ordinary-angle collision contributes.

**3. Blow-up of one collision.** Consider \(\Theta_2=\Theta_1+z/t\) with \(z\ne0\), while \(\Theta_3\) stays a fixed positive angle away from \(\Theta_1\) and their projective seam. Formula (1) yields, for fixed offsets,
\[
\frac{T}{t}\longrightarrow\frac{(H_1-H_2)^2}{2|z|}.
\tag{3}
\]
The convergence is uniform on compact subsets away from \(z=0\) and the third-direction collision. The envelope (2) constrains the scaled collision variable to a bounded interval on the relevant single-collision region. A second direction within \(\epsilon\) of the selected pair contributes at most \(O(\epsilon/t)\); by first removing that region and then letting \(\epsilon\downarrow0\), dominated convergence applies to the entire first-order probability flux. For fixed \(H_1,H_2\), the limiting admissible \(z\)-interval is
\[
-\frac{(H_1-H_2)^2}{2}<z<\frac{(H_1-H_2)^2}{2}.
\]
The two signed halves have combined length \((H_1-H_2)^2\). Therefore the pair \(\{1,2\}\) contributes
\[
\lim_{t\to\infty}t\Pr(T>t,\text{pair }\{1,2\}\text{ dominates})
=\mathbb E(H_1-H_2)^2\int_0^\pi g(\theta)^2\,d\theta
=2v\int_0^\pi g^2.
\]
Summing the three symmetric pairs proves the tail formula.

**4. Marked convergence.** Insert any bounded continuous test function of the pair identity, the near-collision angle, both pair offsets, the unused line, the displacement sign, and \(W_t\) into the preceding flux calculation. After the change of variable \(\delta=|z|/t\), the limiting measure for one pair is proportional to
\[
g(\theta)^2\,d\theta\;
\Pr_H(dh_1)\Pr_H(dh_2)\,(h_1-h_2)^2\;
\Pr_g(d\theta_3)\Pr_H(dh_3)\;\frac12\sum_{s=\pm1}\delta_s\;dw,
\qquad 0<w<1.
\]
The substitution \(w=2|z|/(h_1-h_2)^2\) converts the permitted signed \(z\)-interval to the unit interval. Normalizing by the coefficient in Step 3 gives precisely the independent factors and size bias stated in the finding. Formula (3) gives the Pareto area mark. Atoms at \(h_1=h_2\) receive zero limiting mass, so the finite-threshold definition at equal offsets is immaterial.

**5. Moment threshold and sharp angular optimum.** The positive finite coefficient implies \(\Pr(T>t)\asymp t^{-1}\); the tail-integral identity \(\mathbb E[T^p]=p\int_0^\infty t^{p-1}\Pr(T>t)dt\) proves finiteness precisely for \(0<p<1\). Cauchy–Schwarz gives \(\int_0^\pi g^2\ge1/\pi\), with equality only if \(g\equiv1/\pi\). This proves the sharp minimizer.

## Verification
A standalone Python checker `verify.py` reconstructs the exact area separately from the triangle's three pairwise vertices, tests the collision asymptotic \(\delta T\to (H_1-H_2)^2/2\), and simulates independent uniform and anisotropic directions with both continuous uniform and two-point atomic bounded offsets, and the theoretical \(1/t\) coefficient. It tests the normalized angular optimum and a near-collision uniform-mark mean. The checker successfully returned `THREE_RANDOM_LINE_AREA_CHECKS_OK`. Finite simulation is corroboration only; the proof above establishes the infinite-threshold assertions.

## Relationship to prior work
Finch's 2011 paper studies three circle tangents, conditioned on the circle being their incircle, and derives the distribution of a side rather than the present arbitrary-offset and arbitrary-direction full-area law. A later public note on uniformly sampled circumscribing tangents determines a more detailed second-order area-tail expansion for that special conditioned circle model; the appearance of a \(1/t\) tail in tangency models is **not** claimed as new. Another public note treats the curvature–width dependence of fixed-sample random tangent polygons, including nonuniform angle densities, but its offsets are deterministic support-function values tied to the normal angles and its result is conditioned on bounded support-halfplane intersection. Neither note states the variance-only coefficient, squared-density angular optimum, or full marked disintegration for three independent signed-offset lines.

Beermann–Redenbach–Thäle study small cells of Poisson-line tessellations, a different sampling object and opposite size regime. Fodor–Hug–Ziebarth study large-sample circumscribed random halfspace approximations with outer truncation and \(n\to\infty\) mean/variance asymptotics, not the large-area tail of a fixed three-line triangle. Daley–Ebert–Swift study triangles formed from independently directed sides after setting one side to unit length; their publisher abstract does not give the independent bounded-offset three-line law. The latter full text was not accessible, and therefore constitutes a genuine historical-priority limitation rather than a demonstrated noncoverage result.

## Limitations
The model requires exactly three independent lines, continuous bounded angular density, an offset law independent of angle and bounded in a fixed interval, and positive offset variance. The result is first-order in the large-area threshold; no finite-threshold error constant or statement for unbounded offsets, dependent angles, or a Poisson-line cell is claimed. The marked convergence claimed is weak convergence, not total variation. Prior studies of random tangents already establish related \(1/t\) tails in specialized sampling models. Historical priority remains provisional, notably against older inaccessible full texts; independent mathematical validation has not been performed.

## References
1. S. R. Finch, *Three Random Tangents to a Circle*, arXiv:1101.3931v1, first publicly posted 2011-01-20, https://arxiv.org/abs/1101.3931.
2. M. Beermann, C. Redenbach and C. Thäle, *Asymptotic shape of small cells*, arXiv:1211.5488, first publicly posted 2012-11-23, https://arxiv.org/abs/1211.5488.
3. F. Fodor, D. Hug and I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105, first publicly posted 2014-09-29, https://arxiv.org/abs/1409.8105.
4. D. J. Daley, S. Ebert and R. J. Swift, *Size distributions in random triangles*, Journal of Applied Probability 51 (2014), 283–295, DOI:10.1239/jap/1417528481.
5. *A sharp logarithmic second correction for random tangent-triangle area tails*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-logarithmic-second-correction-for-random-tangent-triangl--a518cd59e8fe.
6. *Curvature–width Pareto law for bounded random tangent polygons*, publicly available mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-curvature-width-pareto-law-for-bounded-random-tangent-polygons--df3f4bf5ad69.
