# Sharp Schur norm and weight rigidity after deleting one projective-plane line

## Finding

Let \(q\ge2\) be a prime power, and let \(B_q\) be the zero–one incidence matrix obtained from the point–line incidence matrix of \(\mathrm{PG}(2,q)\) by deleting exactly one **line row**, while keeping **all point columns**. Let \(\Gamma_q\) denote the complex operator-norm Schur-multiplier norm of \(B_q\). Then

\[
\Gamma_q=\max_{0\le p\le1}F_q(p),\qquad
F_q(p)=\frac{(q^2-1)\sqrt{\alpha_q(p)}+q\sqrt{\beta_q(p)}+\sqrt{\gamma_q(p)}}{\sqrt{q(q+1)}},
\]
with
\[
\alpha_q(p)=\frac{1-p}{q},\qquad
\beta_q(p)=\frac{qp}{q+1},\qquad
\gamma_q(p)=\frac{qp}{q+1}+\frac{(q+1)(1-p)}q.
\]

This maximum occurs at a **unique** \(p=p_q\in(0,1)\), determined by the unique zero of
\[
\frac{q\sqrt{q/(q+1)}}{\sqrt p}
-\frac{q^2-1}{\sqrt{q(1-p)}}
-\frac{(q+1)/q-q/(q+1)}{\sqrt{\gamma_q(p)}}=0.
\]
Among **all** norm-attaining row and column probability weights, including arbitrary non-symmetric weights, the total column weight assigned to the \(q+1\) points on the deleted line is **exactly** \(p_q\). In particular the completely uniform column weight is never optimal:
\[
0<p_q<\frac{q+1}{q^2+q+1}.
\]

As \(q\to\infty\) through prime powers,
\[
p_q=q^{-1}-2q^{-2}+6q^{-3}+O(q^{-7/2}),\qquad
\Gamma_q=\sqrt q+q^{-1}-\tfrac32q^{-3/2}+O(q^{-5/2}).
\]
The improvement over **all-uniform** row/column weights obeys the sharp law
\[
\Gamma_q-F_q\!\left(\frac{q+1}{q^2+q+1}\right)
=\tfrac12q^{-5/2}+O(q^{-7/2}).
\]
For comparison, the intact projective-plane incidence mask has Schur norm
\[
\Gamma_q^{\mathrm{full}}=\frac{q+1+(q^2+q)\sqrt q}{q^2+q+1},\qquad
\Gamma_q^{\mathrm{full}}-\Gamma_q=\tfrac12q^{-3/2}+O(q^{-5/2}).
\]
Thus deletion of a single line creates a strict norm loss and a smaller, but sharp, symmetry-breaking correction to the norming mass distribution.

## Assumptions and scope

All operator spaces and the Schur norm are over **complex Hilbert spaces**. The matrix \(B_q\) has \(q(q+1)\) rows (affine lines) and \(q^2+q+1\) columns (all projective points). Fix the deleted line as the line at infinity. The columns divide into \(q^2\) affine points and \(q+1\) ideal points, one per parallel class of affine lines. No transitivity is assumed for arbitrary non-Desarguesian planes; the theorem concerns \(\mathrm{PG}(2,q)\) over a finite field. For rectangular \(B\), write
\[
\|B\|_{\mathrm{Sch}}=\sup_{\|X\|_{\mathrm{op}}\le1}\|B\circ X\|_{\mathrm{op}}.
\]
The term *norm-attaining weights* means pairs of nonnegative row and column probability vectors attaining the trace-dual maximum, not uniqueness of each individual weight.

## Proof

**1. Trace-dual extremal principle.** By finite-dimensional operator/trace norm duality and the rank-one extreme points of the trace-class unit ball,
\[
\|B\|_{\mathrm{Sch}}=
\max_{\substack{r_i,c_j\ge0\\\sum_i r_i=\sum_jc_j=1}}
\left\|\operatorname{diag}(\sqrt r)B\operatorname{diag}(\sqrt c)\right\|_{S_1}.
\]
Indeed a rank-one trace-class element has the form \(uv^*\) for unit vectors \(u,v\); its Schur image is \(\operatorname{diag}(u)B\operatorname{diag}(\bar v)\), whose trace norm depends only on the squared coordinate moduli. This is also Lemma 2.3 of Levene [1].

**2. Symmetrization and preservation of the ideal mass.** The functional of the combined row/column weights is concave: writing the trace norm via factorization \(B=Y^*Z\) gives
\[
\left\|\operatorname{diag}(\sqrt r)B\operatorname{diag}(\sqrt c)\right\|_{S_1}
=\tfrac12\inf_{B=Y^*Z}\left(\sum_i r_i\|Y_i\|^2+\sum_jc_j\|Z_j\|^2\right),
\]
first for positive weights and then by continuity. Every summand inside the infimum is affine in the weights. The finite affine collineation group \(\mathrm{AGL}(2,q)\) preserves \(B_q\), acts transitively on all affine lines, transitively on all affine points, and transitively on the directions (ideal points). Averaging **any** maximizer over this group therefore gives another maximizer, with row weights \(1/[q(q+1)]\), affine-point weights \((1-p)/q^2\), ideal-point weights \(p/(q+1)\). Crucially, this averaging **preserves** the original total ideal-column mass \(p\). This uses the symmetrization argument of Lemma 2.5 of [1], without assuming that every individual maximizing weight is symmetric.

**3. Exact spectrum.** Put \(n=q(q+1)\), \(a=(1-p)/q^2\), and \(b=p/(q+1)\). Write \(W=n^{-1/2}B_q\operatorname{diag}(\sqrt c)\). Two distinct affine lines meet in one affine point if their directions differ, and otherwise share their single ideal point. Grouping lines into \(q+1\) parallel classes of \(q\) lines gives
\[
nWW^*=qaI_n+(b-a)(I_{q+1}\otimes J_q)+aJ_n.
\]
On vectors of sum zero *inside each class*, the eigenvalue is \(qa=\alpha_q(p)\), multiplicity \((q+1)(q-1)=q^2-1\). On vectors constant within each class whose total sum vanishes, the eigenvalue is \(qb=\beta_q(p)\), multiplicity \(q\). The global constant vector has eigenvalue \(qb+n a=\gamma_q(p)\), multiplicity one. The eigenvalues of \(WW^*\) are these divided by \(n\). Taking square roots and summing gives \(F_q(p)=\|W\|_{S_1}\), proving the global norm formula by Step 2.

**4. Unique optimum and rigidity.** Each nonconstant term of \(F_q\) is a positive multiple of the square root of a strictly positive affine function in \(p\), so \(F_q\) is strictly concave on \((0,1)\). Its derivative tends to \(+\infty\) at \(0\) (from \(\sqrt{\beta_q}\)) and to \(-\infty\) at \(1\) (from \(\sqrt{\alpha_q}\)). Hence it has a unique maximizer \(p_q\) in the interior. Differentiation yields the displayed root equation. A global optimizer with ideal-column mass \(p\), after averaging in Step 2, remains an optimizer with **the same mass**; uniqueness forces \(p=p_q\).

At completely uniform column weights \(p_u=(q+1)/(q^2+q+1)\), put \(v=q^2+q+1\) and \(\eta=(q+1)/q-q/(q+1)>0\). The sign of \(F'_q(p_u)\) is the sign of
\[
-\frac{\eta}{\sqrt{q(q+2)/v}}
+\sqrt{v/q}\left(\frac1q-\frac q{q+1}\right),
\]
which is strictly negative for every \(q\ge2\). Strict concavity then gives \(p_q<p_u\).

**5. Asymptotic coefficient and deletion loss.** Put \(t=1/q\). The critical-point equation in Step 4, evaluated at \(p=ct\) for any fixed \(c>0\), has leading sign \(c^{-1/2}-1\), so \(p_q/t\to1\). Substitute \(p=t+A t^2+B t^3\) into the equation after multiplication by \(t^{3/2}\); its expansion is
\[
t(-A/2-1)+t^2(3A^2/8-A/4-B/2+1)-2t^{5/2}+O(t^3).
\]
The coefficients through order \(t^2\) vanish exactly at \(A=-2\) and \(B=6\). Near \(p=t\), the derivative with respect to \(p\) of the normalized critical-point expression is \(-1/(2t)+O(1)\); the mean-value theorem converts its \(O(t^{5/2})\) residual into the asserted \(O(t^{7/2})\) error. Substituting in \(F_q\) and expanding gives
\[
F_q(p_q)=t^{-1/2}+t-\tfrac32t^{3/2}+2t^{5/2}+O(t^3).
\]
Comparison with \(F_q(p_u)\) yields \(\frac12t^{5/2}+O(t^{7/2})\) for the gain (the derivative and the strict concavity ensure the truncation error in the location of the optimizer is of higher order). For the full incidence matrix, the row/column transitivity and its Gram spectrum \(qI+J\) yield \(\Gamma_q^{\mathrm{full}}=[q+1+(q^2+q)\sqrt q]/v\), whose expansion minus \(F_q(p_q)\) is \(\frac12t^{3/2}+O(t^{5/2})\). This establishes the final claims. \(\square\)

## Verification

`CHECKER.py` uses NumPy and SciPy to independently build the actual finite-field incidence masks for prime orders \(2,3,5,7\), compare all singular values against the theoretical decomposition for four rational weights per order (sixteen spectral checks), and calculate the critical points numerically. It also probes the large-order expansions for \(31,101,503\). The executable is supplementary evidence; the proof above establishes all prime-power orders, including prime powers that the script does not enumerate. To reproduce from the current package, save the embedded checker file as `CHECKER.py` and run `python CHECKER.py` with NumPy and SciPy installed.

## Relationship to prior work

Levene [1] proves the weighted trace-norm variational principle and concavity/automorphism averaging, while pursuing intervals of Schur-idempotent norms through trees grafted onto highly symmetric cores. These lemmas are used directly here. Davidson and Donsig [2] study norm computations for highly symmetric Schur multipliers, including Kneser graph examples. Neither inspected treatment calculates this **one-line-punctured projective incidence mask**, its unique ideal-mass parameter, its strict nonuniformity, or the sharp asymptotic deletion cost. The intact projective-plane mask is a different, fully symmetric design: its norm and uniform optimizer do not imply the punctured theorem. This distinction is one of incidence-pattern implication, not just terminology.

## Limitations

The theorem does not assert that every maximizing row/column weight is individually group invariant. It identifies **only** the total mass on the ideal columns, which is uniquely determined for all maximizers. It does not address non-Desarguesian projective planes lacking the required affine-collineation transitivity, or arbitrary multiple-line deletions. Algebraic asymptotics are along prime powers only. Exhaustive checks are limited to the finite cases in `CHECKER.py`; independent mathematical validation has not been performed. Unindexed older graph/Schur-multiplier identities may express an equivalent result.

## References

[1] Rupert H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1, 5 November 2026, especially Lemmas 2.3 and 2.5, https://arxiv.org/html/2611.08419v1.

[2] Kenneth R. Davidson and Allan P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073, first posted 3 June 2005, https://arxiv.org/abs/math/0506073.
