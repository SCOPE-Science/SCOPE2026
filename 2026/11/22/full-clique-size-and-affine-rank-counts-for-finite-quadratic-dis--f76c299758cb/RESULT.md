# Full clique-size and affine-rank counts for finite quadratic distance graphs

## Finding

Let \(q\) be an odd prime power of characteristic \(p\), \(d\ge1\), \(a\in\mathbb F_q^\times\), and \(r\ge2\). In the graph on \(\mathbb F_q^d\) joining distinct \(x,y\) precisely when \(Q(x-y)=a\), with \(Q(x)=\sum_{i=1}^d x_i^2\), let \(T_r\) be the number of **ordered** \(r\)-cliques, and \(D_r\) the number whose vertices are affinely dependent. The formulas below give both numbers uniformly for every parameter; in particular, \(T_r/r!\) is the count of unlabeled \(r\)-cliques, including nonmaximum cliques.

Write \(\chi\) for the quadratic character, and \(\mathcal O(n,\delta)\) for the size of the full orthogonal group of a nondegenerate \(n\)-dimensional symmetric form with determinant square class \(\delta\). For \(n=0\), set \(\mathcal O(0,1)=1\). These explicit numbers are
\[
\mathcal O(2s+1,\delta)=2q^{s^2}\prod_{j=1}^{s}(q^{2j}-1),
\]
\[
\mathcal O(2s,\delta)=2q^{s(s-1)}(q^s-\chi((-1)^s\delta))\prod_{j=1}^{s-1}(q^{2j}-1)\quad(s\ge1).
\]
The determinant argument to \(\mathcal O\) is specified only up to nonzero squares.

**Case \(p\nmid r\).** Put \(k=r-1\), \(\Delta=(a/2)^k r\). If \(d<k\), or if \(d=k\) and \(\chi(\Delta)=-1\), then \(T_r=D_r=0\). Otherwise
\[
T_r=q^d\frac{\mathcal O(d,1)}{\mathcal O(d-k,\Delta^{-1})},\qquad D_r=0.
\]
When \(d=k\), the denominator means \(\mathcal O(0,1)\), conditional on the square-class criterion.

**Case \(p\mid r\).** Put \(h=r-2\), \(\Delta=(a/2)^h(r-1)\) as an element of \(\mathbb F_q^\times\), and \(m=d-h\). If \(d<h\), or if \(m=0\) and \(\chi(\Delta)=-1\), then \(T_r=D_r=0\). Otherwise put
\[
E=q^d\frac{\mathcal O(d,1)}{\mathcal O(m,\Delta^{-1})}.
\]
Define \(Z_0=1\), \(Z_m=q^{m-1}\) when \(m\ge1\) is odd, and when \(m\ge2\) is even define
\[
Z_m=q^{m-1}+(q-1)q^{m/2-1}\chi((-1)^{m/2}\Delta^{-1}).
\]
Then
\[
\boxed{T_r=E Z_m,\qquad D_r=E.}
\]
Thus, whenever \(T_r>0\), the proportion of ordered \(r\)-cliques that are affinely dependent is **exactly** \(1/Z_m\), a uniform finite-field phase transition at characteristic-divisible clique sizes. Both formulas imply \(T_r=0\) for all \(r>d+2\).

For example, over \(\mathbb F_3^3\), with \(r=3\), side \(a=2\) gives \(T_3=1620\), \(D_3=324\), while side \(a=1\) gives \(T_3=D_3=162\). In particular the same dimension and clique size can have different affine-rank histograms. The full clique polynomial is \(1+q^d t+\sum_{r=2}^{d+2}T_r t^r/r!\).

## Assumptions and scope

All fields are finite of **odd** characteristic, including proper extension fields. The quadratic form is the standard sum of coordinate squares; the prescribed squared side length \(a\) is nonzero. Labeled means **ordered** distinct vertices; a clique of size \(r\) corresponds to \(r!\) ordered configurations. Negative/zero singular-dimension cases must be resolved before evaluating an orthogonal group. The displayed formulas count raw configurations, not isometry orbits.

## Proof

Translate the first vertex to the origin; this contributes \(q^d\). With \(k=r-1\), the remaining vectors \(v_1,\ldots,v_k\) must have common squared norm \(a\), pairwise bilinear product \(a/2\), and hence Gram matrix
\[
G=\frac a2(I_k+J_k),\qquad \det G=(a/2)^k r.
\]
If \(p\nmid r\), \(G\) is nondegenerate. Every such ordered frame defines an isometric embedded nondegenerate \(k\)-space \(U\). Its orthogonal complement has dimension \(d-k\) and determinant square class \(\Delta^{-1}\), since the ambient determinant is \(1\). The classification of nondegenerate quadratic spaces over finite fields of odd order gives existence for all positive complement dimensions, and for zero-dimensional complement exactly when \(\chi(\Delta)=1\). By Witt extension, the full orthogonal group is transitive on these frames and its stabilizer is precisely the orthogonal group of the complement. This yields the first formula, including that all frames are linearly independent.

If \(p\mid r\), the Gram matrix has one-dimensional radical spanned by the coefficient vector \((1,\ldots,1)\). Its first \(h=k-1\) basis vectors yield a nonsingular Gram matrix \(G_0=(a/2)(I_h+J_h)\), of determinant \(\Delta=(a/2)^h(h+1)=(a/2)^h(r-1)\). The same Witt-orbit argument counts their embedded frames by \(E/q^d\). Let \(U\) be their nondegenerate orthogonal complement. The remaining point must satisfy
\[
v_k=-\sum_{i=1}^{h}v_i+t,\qquad t\in U,\quad Q(t)=0.
\]
Indeed, the prescribed inner products determine the projection to their span, and the remaining squared norm forces isotropy. The number of such \(t\) is the standard finite-field zero count \(Z_m\) for a nondegenerate form in dimension \(m\) with determinant \(\Delta^{-1}\); an additive-character or quadratic Gauss-sum calculation gives precisely the listed odd/even formulas. The full frame is linearly dependent if and only if \(t=0\), giving exactly one dependent completion per embedded \(G_0\)-frame. For \(m=0\), this conclusion also applies. Translation supplies the common factor \(q^d\). No cases beyond these two characteristic divisibility regimes are possible.

The orthogonal-group orders follow by the standard split/nonsplit finite classical group formulas. All arguments apply unchanged when \(q\) is a proper prime power.

## Verification

`CHECK.py` constructs the original distance graph, enumerates ordered cliques and affine dependence independently of the orbit formula, and compares with that formula for \(102\) prime-field tests over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\) and \(16\) additional extension-field tests over \(\mathbb F_9\). The executed checker printed `EQUILATERAL_COUNT_OK 102` and `EXTENSION_FIELD_F9_OK 16`. These are finite cross-checks, not a substitute for the proof above. The finite-field classification, Witt transitivity, and isotropic-zero formulas are used as standard general results with complete hypotheses stated above.

## Relationship to prior work

Swanepoel (first public 2026-11-10) gives sharp **existence** criteria, affine dependence constraints, and length restrictions for equilateral sets over fields. Lorenz and Zimmermann (preprint 2023) count **maximum** cliques in quadratic-form representation graphs and characterize maximum configurations. The present explicit complete count treats every size (including smaller-than-maximum cliques) and separates independent from dependent frames. The orbit-stabilizer method itself is classical and is not asserted to be novel. An equivalent nonmaximum-clique enumerator in other work remains a residual originality risk.

## Limitations

No claim is made for characteristic two, degenerate ambient quadratic forms, arbitrary nonstandard distance matrices, orbit counts under smaller symmetry groups, or higher induced subgraph statistics. The work does not reprove standard orthogonal-group order or Gauss-sum zero-count theorems. The count is unconditionally exact subject to those classical theorems; it does not establish that an identical expression has never appeared in unindexed literature.

## References

- Konrad J. Swanepoel, *Equilateral simplices over general fields*, arXiv:2611.14845, initially submitted 2026-11-10. https://arxiv.org/abs/2611.14845
- Nico Lorenz and Marc Christian Zimmermann, *Cliques in representation graphs of quadratic forms*, preprint 2023, later journal publication in 2026. https://doi.org/10.1007/s00454-026-00763-8
- Standard background: Witt's extension theorem and orders of finite orthogonal groups; quadratic Gauss-sum formula for zeros of nondegenerate quadratic forms over odd finite fields.
