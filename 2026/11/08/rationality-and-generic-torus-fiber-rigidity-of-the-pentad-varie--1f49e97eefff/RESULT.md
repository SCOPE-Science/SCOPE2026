# Rationality and generic torus-fiber rigidity of the pentad varieties

## Finding
For every integer \(n\ge5\), the pentad variety \(\operatorname{Pen}_n\) of coordinatewise ratios of two rank-two Pluecker vectors over \(\mathbb C\) is rational. The explicit cross-ratio coordinates defined below form a transcendence basis of its function field and admit a rational inverse. On a dense open, a fiber of the Hadamard-ratio map from two Grassmannians is precisely one orbit of the simultaneous diagonal torus, rather than merely having such an orbit as an irreducible component.

In particular,
\[
\mathbb C(\operatorname{Pen}_n)
=\mathbb C\bigl(u_2,u_3,(u_j,v_j,w_j)_{j=4}^{n}\bigr)
\]
and the map is birational to \(\mathbb A^{3n-7}\). The generic fiber of the ratio map is a torsor under the split torus \((\mathbb C^*)^{n-1}\) and is geometrically irreducible.

## Assumptions and scope
Work throughout over \(\mathbb C\), with an integer \(n\ge5\). Write \(N=\binom n2-1\). Let \(\operatorname{Gr}(2,n)^\circ\) be the open subset where every Pluecker coordinate \(p_{ij}\), \(1\le i<j\le n\), is nonzero. Define
\[
\Psi_n:\operatorname{Gr}(2,n)^\circ\times\operatorname{Gr}(2,n)^\circ\to\mathbb P^N,\qquad
([p],[q])\mapsto[q_{ij}/p_{ij}]_{i<j}.
\]
Its closed image is \(\operatorname{Pen}_n\). Put \(T=(\mathbb C^*)^n/\mathbb C^*\); it acts on both Grassmannian factors by simultaneous scaling of the columns of matrix representatives. In this proof, a generic fiber means the fiber of the restriction to a suitable dense Zariski open of the source over a suitable dense Zariski open of the image; boundary and nongeneric fibers are not classified.

## Proof
**1. Normalization of any generic pair.** Represent two points by full-rank matrices with columns of the form \(\nu_i(1,x_i)^T\) and \(\mu_i(1,y_i)^T\). All minors being nonzero ensures that each labelled configuration consists of distinct points of \(\mathbb P^1\). On a dense open the independent projective changes of basis in the two row spaces can send the first three labelled points to \(0,1,2\). Apply a common diagonal column scaling to make every \(\nu_i=1\), and rescale the second matrix globally to make \(\mu_1=1\). This uses only the simultaneous torus action, separate row changes of basis, and the projective ambiguity of each Grassmannian point. It gives the normalized parameters
\[
x_1=y_1=0,\quad x_2=y_2=1,\quad x_3=y_3=2,\quad
\lambda_1=1,\quad \lambda_i=\mu_i\ (i\ge2),
\]
with all required denominators and minors nonzero. The ratio coordinates of the normalized pair are
\[
Z_{ij}=\lambda_i\lambda_j\frac{y_j-y_i}{x_j-x_i}\qquad(1\le i<j\le n).
\]
These form a dense subset of \(\operatorname{Pen}_n\); equivalently, the rational map from the parameter space \((\mathbb C^*)^{n-1}\times\mathbb A^{2n-6}\) to \(\operatorname{Pen}_n\) is dominant. The parameter count is \(3n-7\).

**2. Intrinsic cross-ratios.** On the nonzero-coordinate open of the target define
\[
u_2=\frac{z_{23}}{z_{13}},\quad
u_3=\frac{z_{23}}{z_{12}},\quad
u_j=\frac{z_{1j}z_{23}}{z_{12}z_{13}},\quad
v_j=\frac{z_{2j}z_{13}}{z_{1j}z_{23}},\quad
w_j=\frac{z_{3j}z_{12}}{z_{1j}z_{23}}\quad(4\le j\le n).
\]
Here the indices on \(u_j\) denote parameters, not column weights. These ratios are independent of the choice of homogeneous projective representative. For a normalized pair the identities are
\[
u_2=\lambda_2,\quad u_3=\lambda_3,\quad
u_j=\lambda_j\frac{y_j}{x_j},\quad
v_j=\frac{x_j(y_j-1)}{y_j(x_j-1)},\quad
w_j=\frac{x_j(y_j-2)}{y_j(x_j-2)}.
\]

**3. Exact inverse.** Set \(B_j=x_j/y_j\). Then the two latter identities become
\[
v_j=\frac{x_j-B_j}{x_j-1},\qquad
w_j=\frac{x_j-2B_j}{x_j-2}.
\]
Consequently,
\[
B_j=(1-v_j)x_j+v_j,\quad
(1-2v_j+w_j)x_j=2(w_j-v_j).
\]
On the dense open where \(1-2v_j+w_j\ne0\) and the other denominators are nonzero, recover
\[
x_j=\frac{2(w_j-v_j)}{1-2v_j+w_j},\quad
B_j=(1-v_j)x_j+v_j,\quad
y_j=\frac{x_j}{B_j},\quad
\lambda_j=u_jB_j.
\]
Also recover \(\lambda_2=u_2\), \(\lambda_3=u_3\). All these are rational functions of the displayed \(3n-7\) cross-ratios. Substitution proves both compositions are the identity on dense opens, so the cross-ratio map and normalized parametrization are birational. In particular the target has dimension \(3n-7\) and is rational. More explicitly, multiplying every projective coordinate by the same factor \(c=z_{23}/(z_{12}z_{13})\) provides the canonical representative satisfying \(c z_{12}=u_2\), \(c z_{13}=u_3\), and \(c z_{23}=u_2u_3\). Its remaining entries are exactly \(Z_{ij}\) from the reconstructed normalized parameters.

**4. Generic fibers.** Every generic source pair can be carried to the normalized chart by an element of \(T\), without changing its image under \(\Psi_n\). Two normalized pairs with the same image have identical cross-ratios; the inverse just proved forces equality of all normalized parameters and hence equality of the two normalized Grassmannian points. Thus two arbitrary generic source pairs have equal images if and only if they differ by a single simultaneous diagonal scaling. The \(T\)-action is free on \(\operatorname{Gr}(2,n)^\circ\): if \(t_it_j\) is constant for all pairs \(i<j\), then all \(t_i\) are equal, representing the identity of \(T\). Hence each generic fiber is exactly one \(T\)-orbit. The rational normalization constructs a rational section, yielding the claimed birationally trivial torus torsor; characteristic zero and generic smoothness rule out an additional nonreduced generic structure.

## Verification
The standalone file `checks/pentad_inverse.py` uses only Python's standard library. Running `python checks/pentad_inverse.py` evaluates sixteen sets of exact rational parameters of sizes \(n=5,6,8,11\). It checks full projective reconstruction, exact inversion, and invariance under arbitrary common diagonal column rescaling; the expected final line is `CERTIFICATE_OK`. These finite tests are consistency evidence only. Steps 1–4 are an algebraic proof for all stated \(n\).

## Relationship to prior work
Koefler–Ventura–Yu, *From MHV Gravity Amplitudes and Hodges map to Pentad Varieties* (arXiv:2611.00864v1, first submitted October 31, 2026), introduce \(\operatorname{Pen}_n\), construct precisely the normalized parameters and cross-ratios in Proposition 4.8, and compute a full-rank Jacobian. Their Remark 4.9 identifies the generic fiber dimension and shows a torus orbit is an irreducible component. The present contribution **starts from their parametrization** but establishes the explicit rational inverse, generic degree one, uniqueness of the fiber component, and rationality. These conclusions are not obtained solely from Jacobian rank or a dimension count. The algebraic manipulations giving the inverse are elementary but the associated global generic-identifiability statement is a separate birational conclusion.

Martin's affine slope variety (arXiv:math/0302106) is related by the source's Hadamard-product construction; its ideals and combinatorial invariants do not directly identify the generic fibers of \(\Psi_n\). Drton–Sturmfels–Sullivant's factor-analysis work (arXiv:math/0509390) supplies older pentad context. The exact overlap with all historically equivalent birational parameterizations has not been independently established.

## Limitations
The result covers the complex generic open only. It does not establish rationality of arbitrary boundary strata, describe compactified fibers, resolve singularities, or establish any non-generic fiber classification. The proof uses the 2026 paper's established definition but is otherwise direct. Historical originality is provisional: earlier algebraic-statistics parameterizations might contain equivalent reconstruction formulas. Independent review has not been performed.

## References
- J. Koefler, E. Ventura, H. Yu, *From MHV Gravity Amplitudes and Hodges map to Pentad Varieties*, arXiv:2611.00864v1 (October 31, 2026), especially Proposition 4.8, Remark 4.9, and Proposition 4.26. https://arxiv.org/html/2611.00864v1
- J. L. Martin, *The slopes determined by \(n\) points in the plane*, arXiv:math/0302106v3. https://arxiv.org/abs/math/0302106
- M. Drton, B. Sturmfels, S. Sullivant, *Algebraic Factor Analysis: Tetrads, Pentads and Beyond*, arXiv:math/0509390. https://arxiv.org/abs/math/0509390
