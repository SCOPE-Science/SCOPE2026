# Sharp endpoint stability and a golden-ratio phase transition for weighted \(\ell_1\)-epigraph projection

## Finding
For every integer \(n\ge1\), every \(w\in(0,\infty)^n\), and the Euclidean metric projector \(P_w\) onto
\[
K_w=\{(x,t)\in\mathbb R^n\times\mathbb R:t\ge\sum_{j=1}^n w_j|x_j|\},
\]
the exact global Lipschitz constant in the *coordinatewise maximum norm on input and output* is
\[
L(w)=\max\left\{1,\max_{\varnothing\ne I\subseteq[n]}\frac{S_I+W_I}{1+S_I},
\max_{\varnothing\ne I\subseteq[n]}\max_{i\in I}\left[1+\frac{w_i(1+W_I-2w_i)}{1+S_I}\right]\right\},
\]
where \(W_I=\sum_{j\in I}w_j\) and \(S_I=\sum_{j\in I}w_j^2\).
If \(i_1,\ldots,i_n\) are the indices sorted in nondecreasing weight order and \(I_k=\{i_1,\ldots,i_k\}\), the same constant is computed by checking **only** \(n\) scalar-row supports \(I_k\) and at most \(n(n+1)\) coordinate-row supports \(I_k\cup\{i\}\). Thus sorting plus \(O(n^2)\) real arithmetic suffices, including at ties.

The projector is nonexpansive in the coordinate maximum norm **if and only if** \(n=1\) and \(w_1=1\). In contrast, for every \(n\ge2\), among positive weights satisfying \(\prod_{i=1}^n w_i=1\), the infimum of \(L(w)\) is \(1\), and it is not attained. For equal unit weights, \(L(1,\ldots,1)=2n/(n+1)\).

There is an exact, nonmonotone **planar weight-design phase**. For \(n=2\), \(w=(r,r^{-1})\), \(r\ge1\), write
\[
A(r)=\frac{r}{r^2+r+1},\qquad
B(r)=\frac{r^2+r-1}{(r^2-r+1)(r^2+r+1)}.
\]
Then \(L(r,r^{-1})=1+\max\{A(r),B(r)\}\). The spatial-row branch \(B\) dominates for \(1<r<\varphi\) and the scalar-row branch \(A\) dominates for \(r>\varphi\), where \(\varphi=(1+\sqrt5)/2\). The unique maximum over \(r\ge1\) occurs at the unique \(r_*\in(1,\varphi)\) solving
\[
2r_*^5+3r_*^4-4r_*^3+r_*^2-4r_*-1=0,
\]
with \(r_*\approx1.203277832\) and \(L(r_*,r_*^{-1})\approx1.363352316\), greater than the balanced value \(4/3\). The coefficient returns to \(4/3\) at the unique \(r_c\in(1,\varphi)\) with \(r_c^3+r_c^2-r_c-4=0\) (\(r_c\approx1.485584\)), and decreases strictly towards \(1\) thereafter.

## Assumptions and scope
All spaces are real and finite-dimensional, all weights are strictly positive, projection is **Euclidean** in \(\mathbb R^{n+1}\), and the Lipschitz quotient uses the unweighted coordinate \(\ell_\infty\) norm. The final coordinate is \(t\), independent of \(n\) spatial coordinates. The supremum is over all distinct input pairs, not merely input directions or a restricted bounded region. The norm \(\|\cdot\|_\infty\) is the largest absolute coordinate. No fixed scalar epigraph level is assumed.

## Proof
**1. Projection and its active faces.** For an input \((y,\tau)\) inside \(K_w\), \(P_w(y,\tau)=(y,\tau)\). Otherwise strict convexity and KKT give a unique multiplier \(\lambda>0\) satisfying
\[
\lambda+\tau=\sum_{j=1}^n w_j\max\{|y_j|-\lambda w_j,0\},
\]
with output coordinates \(x_j=\operatorname{sign}(y_j)\max\{|y_j|-\lambda w_j,0\}\) and \(t=\tau+\lambda\). The left-minus-right function is strictly increasing, hence has a unique root. If every spatial output vanishes the projector is locally the apex and its derivative is zero. Otherwise, fix the nonempty strictly active set \(I\) and the signs \(s_j\), and set \(d=1+S_I\). The multiplier is affine:
\[
\lambda=\frac{\sum_{j\in I}w_js_jy_j-\tau}{d}.
\]
The Jacobian of nonzero output coordinates \((x_I,t)\) with respect to \((y_I,\tau)\) is the orthogonal hyperplane projector \(J_I=\operatorname{Id}-vv^{\mathsf T}/d\), with \(v=((s_jw_j)_{j\in I},-1)\). All spatial inactive-output derivative rows vanish. Consequently, the absolute row sum of the scalar output is exactly \((S_I+W_I)/d\), and that of each active coordinate \(i\in I\) is exactly \(1+w_i(1+W_I-2w_i)/d\), independently of signs. The interior-epigraph Jacobian is identity.

**2. Global bound and sharpness.** The projection is continuous and piecewise affine on finitely many polyhedral cells (the sign and active-set cells). The maximum of the induced \(\ell_\infty\)-operator norms of these matrices bounds every two-input quotient by segment integration. Conversely every nonempty \(I\) and sign configuration corresponds to a full-dimensional cell: set the projected active spatial outputs equal to \(5s_i\), inactive outputs zero, \(\lambda=1\), \(y_i=s_i(5+w_i)\) on \(I\), \(y_j=0\) off \(I\), and \(\tau=5W_I-1\). The active inequalities are strict, and an arbitrarily small perturbation in the sign pattern maximizing any Jacobian row realizes its induced norm locally. Thus the supremum is the displayed maximum, with no need for numerical optimization.

**3. Sorted-prefix reduction.** The scalar row's excess over \(1\) is \((W_I-1)/(1+S_I)\). If it is positive and maximal, write its value as \(\rho>0\). Adding a new index of weight \(a\) improves the ratio precisely if \(a-\rho a^2>0\); deleting an included index improves it when that expression is negative. Therefore, up to weight ties, every maximizing support is an initial segment of weights sorted from smallest to largest. For a fixed spatial row \(i\), its positive excess divided by \(w_i\) is \((1+W_I-2w_i)/(1+S_I)\). The identical exchange inequality holds for adding/deleting any \(j\ne i\), while \(i\) remains compulsory. Thus a maximizer has support \(I_k\cup\{i\}\). If a ratio never exceeds zero, the outer maximum \(1\) already controls it. This proves the quadratic-size candidate family.

**4. Rigidity and an unattained infimum.** If any weight is below \(1\), its singleton spatial row exceeds \(1\); if any is above \(1\), its singleton scalar row exceeds \(1\). Hence nonexpansivity forces all weights to equal \(1\), where the full scalar-row norm is \(2n/(n+1)>1\) for \(n\ge2\). For \(n=1\), the unique contractive choice is \(w_1=1\).

For fixed \(n\ge2\) take \(w_j(R)=R^{2j-n-1}\), \(j=1,\ldots,n\), \(R>1\). Their product is identically \(1\) and consecutive weights differ by \(R^2\). In every active set, if its largest weight is \(M\ge R\), then \(W_I\le M(1+(n-1)/R^2)\) and \(S_I\ge M^2\); the scalar-row excess is \(O_n(1/R)\). For the spatial row of that largest-weight index, \(1+W_I-2M<0\) for sufficiently large \(R\); for every other index \(w_i\le M/R^2\), its positive excess is \(O_n(R^{-2})\). If the largest active weight is at most \(1\), at most one weight equals \(1\), and the others have total at most \(n/R^2\), yielding excess \(O_n(R^{-2})\) for both row types. Thus \(L(w(R))\to1\), but the rigidity shows \(L(w)>1\) at every finite positive normalized \(w\).

**5. Planar phase diagram.** Enumerate the three nonempty active sets for weights \(r,r^{-1}\), \(r\ge1\). The positive singleton excess is \((r-1)/(r^2+1)\), and it does not exceed \(A(r)\), since their difference is \((r+1)/[(r^2+1)(r^2+r+1)]\). The full-support scalar-row excess is exactly \(A(r)\), and the full-support smaller-coordinate excess exactly \(B(r)\). The full-support larger-coordinate excess is no greater than \(B(r)\), with difference \((r-1)(r+1)/(r^2+r+1)\). All remaining singleton excesses are nonpositive. Therefore the full maximum is \(1+\max\{A(r),B(r)\}\). Direct factorization yields
\[
B(r)-A(r)=-\frac{(r-1)(r^2-r-1)}{(r^2-r+1)(r^2+r+1)}.
\]
The \(A\)-branch decreases for \(r>1\), while
\[
B'(r)=-\frac{2r^5+3r^4-4r^3+r^2-4r-1}{(r^2-r+1)^2(r^2+r+1)^2}.
\]
The numerator has strictly positive derivative on \([1,\infty)\): \(10r^4+12r^2(r-1)+2r-4>0\), and changes sign exactly once between \(1\) and \(\varphi\). Finally
\[
B(r)-\frac13=-\frac{(r-1)(r^3+r^2-r-4)}{3(r^2-r+1)(r^2+r+1)};
\]
the cubic is strictly increasing on \([1,\infty)\) and has its unique root in \((1,\varphi)\). All asserted transitions and uniqueness follow.

## Verification
The standalone `epigraph_stability_check.py` requires only Python 3 standard-library modules. Execute `python3 epigraph_stability_check.py`. It prints `PASS 13838 supplementary assertions`. These tests include exact-rational row sums, exhaustive supports against the sorted-prefix reduction through dimension seven, exact two-coordinate product-one branch checks for rational weights, and numerical KKT recovery and perturbation tests. The finite tests are supplemental; the universal proof is analytic in Steps 1–5.

## Relationship to prior work
Friedlander–Goodwin–Hoheisel (2021), arXiv:2102.06809, provide the general perspective-function epigraph projection framework and root-based formulas. Liu–Han–Wang–Chen (2015) study *differential properties of metric projectors over the epigraphs of weighted \(\ell_1\) and \(\ell_\infty\) norms*, which is directly relevant prior local calculus. The present claim is specifically the exact globally optimized **two-input coordinate maximum-norm** coefficient, its sorted-prefix reduction, the unattained geometric-mean normalized infimum, and the nonmonotone planar golden-ratio phase. These are not claimed as consequences of merely renaming earlier derivatives; independent historical-priority comparison with the inaccessible 2015 full text is warranted. Results on fixed weighted \(\ell_1\)-balls concern a different projector because the epigraph's last coordinate is free and perturbed along with the other coordinates.

## Limitations
The exact coefficient is for Euclidean metric projection measured with the *unweighted* input/output maximum norm and strictly positive finite weight vectors. It does not assert the same constant for non-Euclidean nearest points, infinite-dimensional epigraphs, or weighted error metrics. The 2015 local-differential study was identifiable from bibliographic sources but its full text was not accessible in the available retrieval paths, leaving an explicit priority uncertainty. The finding has no independent audit or independent mathematical validation.

## References
1. F. Friedlander, M. Goodwin, T. Hoheisel, *From perspective maps to epigraphical projections*, arXiv:2102.06809 (first public 2021-02-12). https://arxiv.org/abs/2102.06809
2. Y. Liu, J. Han, C. Wang, S. Chen, *Differential properties of the metric projectors over the epigraph of the weighted \(\ell_1\) and \(\ell_\infty\) norms*, Pacific Journal of Optimization **11** (2015), 737–749 (bibliography verified; full text unavailable).
3. Y. Liu and C. Wang, *Properties associated with the epigraph of the \(\ell_1\) norm function of projection onto the nonnegative orthant*, Optimization Letters (2016), DOI:10.1007/s00186-016-0540-6. https://doi.org/10.1007/s00186-016-0540-6
