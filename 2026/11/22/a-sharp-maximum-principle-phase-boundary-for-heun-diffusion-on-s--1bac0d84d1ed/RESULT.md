# A sharp maximum-principle phase boundary for Heun diffusion on scaled fractional-regularized multipartite graphs

## Finding

Fix an unweighted connected complete multipartite graph \(G=K_{n_1,\ldots,n_q}\) with \(q\ge2\) nonempty parts and \(N=\sum_{r=1}^q n_r\ge2\). Form its *scaled regularized fractional graph Laplacian* \(\widehat L_{\alpha,\beta}\) using a spectral exponent \(0<\alpha<1\) and amplification \(\beta\ge1\): an existing inter-part edge retains conductance one, while each absent within-part edge receives \(\beta\) times the corresponding conductance in the spectral fractional graph. For the linear heat equation \(\dot u=-\widehat L_{\alpha,\beta}u\), apply one completed explicit trapezoidal (Heun, SSPRK(2,2)) step,
\[
P_h=I-h\widehat L_{\alpha,\beta}+\frac{h^2}{2}\widehat L_{\alpha,\beta}^{\,2}.
\]
Put, for each part,
\[
a_r=1-\frac{n_r}{N},\qquad
c_\alpha(a)=\frac{a^\alpha-a}{1-a},\qquad
w_r=\beta N^{\alpha-1}c_\alpha(a_r),\qquad
e_r=a_r+(1-a_r)w_r.
\]
Weights \(w_r\) are used only for parts with \(n_r\ge2\); a singleton has no internal edges. Define
\[
\boxed{\quad
h_*(\alpha,\beta;G)=\frac1N\min\left\{2,\ \min_{r:\,n_r\ge2,\,w_r>1}\frac{2(e_r-a_r)}{e_r^2-a_r}\right\},\quad}
\]
with the minimum of an empty set omitted. **Theorem.** For every such graph, exponent, and amplification, \(P_h\) preserves the nonnegative cone (equivalently the scalar maximum principle for all initial vectors) **if and only if** \(0\le h\le h_*\). It is always symmetric and mass-preserving, with strictly positive diagonal entries for every finite \(h\ge0\). Every forbidden step has an explicit negative off-diagonal entry, and positivity never returns at a larger step.

When at least one part has size two or greater, let \(m=\min\{n_r:n_r\ge2\}\) and \(a_*=1-m/N\). The unique *amplification transition* is
\[
\boxed{\beta_*=\frac{N^{1-\alpha}}{c_\alpha(a_*)}>1.}
\]
For \(1\le\beta\le\beta_*\), the sharp positivity horizon is the universal \(h_*=2/N\), and it equals the spectral stability horizon of Heun. For \(\beta>\beta_*\), one or more within-part couplings exceed the preserved original conductance; then \(h_*<2/N\) and, more strongly,
\[
\boxed{\quad h_*<\frac{2}{\lambda_{\max}(\widehat L_{\alpha,\beta})}.\quad}
\]
Thus a nonempty interval of *spectrally stable yet positivity-violating* steps appears immediately after the amplification transition. If every part is singleton (the complete graph), set \(\beta_*=+\infty\); then \(h_*=2/N\) for every \(\beta\).

## Assumptions and scope

The unnormalized graph Laplacian is \(L_G=\operatorname{diag}(A_G\mathbf1)-A_G\), and \(L_G^\alpha\) denotes its real symmetric spectral power, assigning zero to the zero eigenvalue. The scaled regularized graph retains every original edge of conductance one and assigns conductance \(\beta[-(L_G^\alpha)_{ij}]\) to each nonedge \(i\ne j\). This is the exact construction of Filippo and Mazza, Definition 4.1, with amplification \(\beta\ge1\), not the graph operator \(\beta L_G^\alpha\) and not a normalized graph Laplacian. Positivity concerns the *completed endpoint map*, not the internal Heun stage, which may be negative. All statements are exact-arithmetic and hold for all real admissible parameters and all finite part-size profiles. Spectral stability means contraction on every nonconstant Laplacian eigenmode; the scalar stability interval of Heun on the nonnegative real axis is \([0,2]\).

## Proof

**1. Compute the fractional nonedge conductances.** Let \(J\) be the full all-ones matrix, \(J_r\) the all-ones matrix of part \(r\) extended by zeros, and \(I_r\) the coordinate identity in that part. The mutually orthogonal projectors
\[
E_0=\frac JN,\quad E_c=\sum_r\frac{J_r}{n_r}-\frac JN,\quad E_r=I_r-\frac{J_r}{n_r}
\]
resolve the identity; \(E_r=0\) for singletons. A direct edge-Laplacian calculation gives
\[
L_G=NE_c+\sum_r(N-n_r)E_r,\qquad
L_G^\alpha=N^\alpha E_c+\sum_r(N-n_r)^\alpha E_r.
\]
For two distinct vertices in part \(r\), the second identity yields
\[
-(L_G^\alpha)_{ij}=N^{\alpha-1}\frac{a_r^\alpha-a_r}{1-a_r}>0.
\]
The within-part conductance in the scaled regularized graph is therefore exactly \(w_r\).

**2. The regularized graph and its Heun step.** Since every inter-part conductance is one and every part has homogeneous internal conductance \(w_r\), the same projectors diagonalize its Laplacian:
\[
\widehat L_{\alpha,\beta}=NE_c+N\sum_r e_rE_r.
\]
Writing \(t=Nh\) and \(R(z)=1-z+z^2/2\), its Heun propagator is
\[
P_h=E_0+R(t)E_c+\sum_rR(te_r)E_r.
\]
This directly gives \(P_h\mathbf1=\mathbf1\). Also \(R(z)=\tfrac12(1+(z-1)^2)>0\) for every real \(z\). All eigenvalues of \(P_h\) are positive, so each diagonal entry is strictly positive.

**3. Exhaust every off-diagonal sign.** For vertices in different parts, the projector formula gives
\[
(P_h)_{ij}=\frac{1-R(t)}N=\frac tN\left(1-\frac t2\right).
\]
Because there are at least two parts, these entries are nonnegative exactly for \(0\le t\le2\) and strictly negative for \(t>2\). For distinct vertices in the same nonsingleton part \(r\), the exact entry is
\[
(P_h)_{ij}=\frac{t}{N(1-a_r)}\left[(e_r-a_r)-\frac t2(e_r^2-a_r)\right].
\]
For \(0<t\le2\), the bracket is affine in \(t\). At zero it is \(e_r-a_r=(1-a_r)w_r>0\); at \(t=2\) it equals \(e_r(1-e_r)\). If \(w_r\le1\), equivalently \(e_r\le1\), both endpoints are nonnegative and hence the entire interval is allowed. If \(w_r>1\), equivalently \(e_r>1\), the bracket has a unique positive zero at \(t_r=2(e_r-a_r)/(e_r^2-a_r)<2\) and is negative for every \(t>t_r\). The minimum of all these exact constraints is precisely \(Nh_*\); it is necessary and sufficient because there are no remaining matrix entries. It also proves the absence of positivity re-entry.

**4. Sharp amplification phase and spectral mismatch.** The function \(c_\alpha(a)\) increases strictly on \((0,1)\). Indeed,
\[
c_\alpha'(a)=\frac{\alpha a^{\alpha-1}+(1-\alpha)a^\alpha-1}{(1-a)^2}>0,
\]
by strict weighted arithmetic–geometric mean for \(0<a<1\), \(0<\alpha<1\). The maximum \(w_r\) thus occurs in the *smallest nonsingleton part* and crosses one exactly at the displayed \(\beta_*\). Moreover \(0<c_\alpha(a)<1\) and \(N^{\alpha-1}<1\), proving \(\beta_*>1\). When all \(w_r\le1\), every \(e_r\le1\), so \(\lambda_{\max}=N\) and both Heun spectral stability and entrywise positivity end at \(2/N\). Above \(\beta_*\), choose a part attaining \(e_{\max}=\max_r e_r>1\). Its positivity zero is strictly below the spectral endpoint since
\[
\frac{2(e_{\max}-a_r)}{N(e_{\max}^2-a_r)}
<\frac{2}{Ne_{\max}}
=\frac2{\lambda_{\max}(\widehat L_{\alpha,\beta})},
\]
where the strict inequality reduces to \(a_r(e_{\max}-1)>0\). The overall positivity limit is no larger than this part's limit. This proves every asserted strict boundary.

## Verification

The accompanying standalone `VERIFY.py` constructs the full weighted graph Laplacian independently of the projector formulas, computes \(P_h\) by exact rational matrix products, verifies every off-diagonal entry formula, row sums, positive diagonals and both sides of the claimed sharp cutoff on **2,162 graph-and-weight combinations**, including all integer multipartitions of orders two through eight and a rational menu of zero, subunit, unit and superunit internal conductances. In addition, the optional NumPy section independently diagonalizes original graph Laplacians, constructs their fractional spectral powers, and checks the claimed regularized nonedge weights and spectra on **24 fractional graph/exponent/amplification cases**. Output from the local replay was `EXACT_RATIONAL_CASES 2162`, `FRACTIONAL_SPECTRAL_CASES 24`, and `VERIFY_OK`. These are finite regression checks; the displayed projector and sign arguments prove the full quantified claim.

For a concrete spectral-stability gap, take \(G=K_{2,2}\), \(\alpha=1/2\), \(\beta=6\). Then \(w_r=3(\sqrt2-1)>1\), \(\beta_*=2(1+\sqrt2)\approx4.828427\), and the sharp positivity horizon is \(h_*\approx0.410189\), strictly below the spectral ceiling \(\approx0.445903\). An interior edge of either size-two part witnesses the negative transition in this interval.

## Relationship to prior work

Bianchi, Donatelli, Durastante and Mazza previously developed the compatible graph regularization framework (arXiv:2101.00425, first public 2021); Filippo and Mazza subsequently make its scaled fractional definition explicit and establish spectral and diffusion properties, but do not determine a sharp completed explicit Runge–Kutta maximum-principle cutoff as a function of its amplification parameter. Known complete-multipartite graph projector formulas are used rather than claimed. The published *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs* gives the \(2/N\) Heun cutoff for **unweighted** complete multipartite graphs; this is a covered boundary case, not the present novelty. The published *Independent sharp positivity thresholds for fourth-order diffusion on block-homogeneous complete networks* concerns the different fourth-order **implicit Gauss** stability function on a larger weighted network class, not the second-order Heun stability polynomial or the fractional-power scaling transition. The published *A sharp positivity transition for fractional graph heat on complete multipartite networks* concerns the **exact exponential semigroup** of the unregularized fractional power, not Heun discretization of the scaled regularized operator. A universal scalar-filter positivity criterion for unweighted complete multipartite Laplacians does not by itself provide the weighted amplified Heun boundary or its spectral mismatch. The new assertion is the full sharp amplification/timestep phase diagram for the named source's weighted nonlocal regularization.

## Limitations

The result is restricted to finite complete multipartite starting graphs, spectral exponents strictly between zero and one, the scaled regularization of Definition 4.1, and the completed second-order Heun endpoint. It does not claim a stagewise maximum principle, arbitrary graph topology, nonlinear diffusion, or analogous formulas for other integrators. Although relevant full texts and published records were compared, exhaustive historical priority is not certified, and no independent mathematical audit is represented.

## References

1. A. Filippo and M. Mazza, *Spectral and computational aspects of a regularized fractional Laplacian for non-local diffusion on graphs*, arXiv:2606.10480v1, first posted 2026-06-09, especially Section 4.1 and Definition 4.1; full publisher open-access article: https://doi.org/10.1515/jnma-2026-0007.
2. *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs*, mathematical research record (2026), full `RESULT.md` examined.
3. *Independent sharp positivity thresholds for fourth-order diffusion on block-homogeneous complete networks*, mathematical research record (2026), full `RESULT.md` examined.
4. *An exact positivity criterion on complete multipartite diffusion graphs*, mathematical research record (2026), full `RESULT.md` examined.
5. *A sharp positivity transition for fractional graph heat on complete multipartite networks*, mathematical research record (2026), full `RESULT.md` examined.
6. D. Bianchi, M. Donatelli, F. Durastante and M. Mazza, *Compatibility, embedding and regularization of non-local random walks on graphs*, arXiv:2101.00425, first posted 2021-01-02; J. Math. Anal. Appl. 511 (2022), article 126020.
7. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242 (2021), general numerical time-integration positivity context.
