# Sharp global convexity restoration in sparse logistic forward–backward envelopes

## Finding

For every soft Bernoulli label \(q\in(0,1)\), penalty \(\lambda>0\), and stepsize \(\gamma>0\), let
\[
 f_q(x)=\log(1+e^x)-qx,\qquad g_\lambda(x)=\lambda|x|,
\]
and define the standard forward–backward envelope on the entire real line by
\[
 E_{\gamma,q,\lambda}(x)=f_q(x)-\frac\gamma2[f_q'(x)]^2
   +(g_\lambda)_\gamma\bigl(x-\gamma f_q'(x)\bigr),
\quad
 (g_\lambda)_\gamma(y)=\min_{z\in\mathbb R}
 \left\{\lambda|z|+\frac{(z-y)^2}{2\gamma}\right\}.
\]
Set \(d=(|q-\tfrac12|-\lambda)_+\), where \(t_+=\max(t,0)\). Then the **exact** global convexity criterion is
\[
 E_{\gamma,q,\lambda}\text{ is convex on }\mathbb R
 \quad\Longleftrightarrow\quad
 0<\gamma\le \Gamma(q,\lambda)
 :=\frac{3}{\tfrac34+d^2}.
\tag{1}
\]
The threshold ranges from \(3\) to \(4\), and equals the full smooth-loss stepsize \(4\) precisely when \(\lambda\ge|q-\tfrac12|\). The unique minimizer of the composite objective is
\[
 x_* =\log\frac{p_*}{1-p_*},\qquad
 p_*=\frac12+\operatorname{sgn}(q-\tfrac12)d.
\tag{2}
\]
For every \(0<\gamma<4\), the envelope has exactly this same unique stationary point and global minimizer, even if \(\gamma>\Gamma(q,\lambda)\) makes it nonconvex. Thus the effective shrinkage \(d\) controls both the fitted probability and the loss of convex envelope geometry.

There is an explicit nonempty **convexity-restoration window**: for \(q=1/10\), \(\lambda=1/10\), \(\gamma=7/2\), the penalized envelope is globally convex because \(\Gamma=25/7\), whereas the envelope with \(\lambda=0\) is nonconvex at the same stepsize (its threshold is \(300/91\)).

As a separable weighted corollary, if \(F(x)=\sum_{i=1}^n[w_i f_{q_i}(x_i)+\lambda_i|x_i|]\), where \(w_i>0\), \(0<q_i<1\), and \(\lambda_i>0\), then its ordinary Euclidean forward–backward envelope is globally convex exactly when
\[
0<\gamma\le\min_{1\le i\le n}\frac{3}{w_i\left[\tfrac34+\bigl(|q_i-\tfrac12|-\lambda_i/w_i\bigr)_+^2\right]}.
\tag{3}
\]
The separable corollary is part of the same criterion, not a claim about coupled-feature logistic regression.

## Assumptions and scope

All assertions concern exact real arithmetic and finite \(q,\lambda,\gamma\) in the ranges above; the scalar logit uses the canonical single-feature, unit-scale logistic loss. No box constraint or data-dependent normalization is imposed. The Moreau envelope convention is the infimum with coefficient \(1/(2\gamma)\). A "convex envelope" means convexity of this smooth **forward–backward merit function**, not merely convexity of \(f_q+g_\lambda\), which already holds for every parameter choice. Equation (3) requires diagonal/separable logistic coordinates; it is not asserted for general design matrices.

## Proof

Write \(p=(1+e^{-x})^{-1}\), \(a=p(1-p)\), \(b=a(1-2p)\), \(t=p-q\), and \(y=x-\gamma t\). Then \(0<a\le1/4\), \(f_q'=t\), \(f_q''=a\), \(f_q'''=b\). The scalar Moreau envelope is exactly
\[
(g_\lambda)_\gamma(y)=
\begin{cases}y^2/(2\gamma),& |y|\le\gamma\lambda,\\
\lambda |y|-\gamma\lambda^2/2,&|y|>\gamma\lambda.
\end{cases}
\]
The resulting \(E\) is continuously differentiable. Away from the two possible proximal transition points, differentiation gives:
\[
 E''(x)=\begin{cases}
 \gamma^{-1}-a-xb,& |y|<\gamma\lambda,\\[2pt]
 a\{1-\gamma[a+(1-2p)(p-q+s\lambda)]\},
    &s y>\gamma\lambda,\quad s\in\{-1,1\}.
\end{cases}\tag{4}
\]
Since \(xb\le0\) everywhere, the middle branch satisfies
\(E''\ge\gamma^{-1}-1/4\ge0\) for \(\gamma\le4\).

By reflection \((q,x)\mapsto(1-q,-x)\), it suffices to treat \(q\le1/2\). For \(\gamma\le4\), \(y'=1-\gamma a\ge0\) and \(y(0)=\gamma(q-1/2)\le0\). Thus the positive active branch \(y>\gamma\lambda\) occurs only at \(x>0\), where \(p>1/2\) and \((1-2p)(p-q+\lambda)\le0\); its curvature in (4) is nonnegative.

For the negative active branch, put \(r=q+\lambda\). The factor that could defeat positivity is
\[
D_r(p)=p(1-p)+(1-2p)(p-r)
=-3p^2+2(1+r)p-r.
\tag{5}
\]
If \(r\ge1/2\), the negative active region lies in \(x<0\), hence \(p<1/2\le r\), and \(D_r(p)\le a\le1/4\). If \(r<1/2\), then \(D_r(p)\le a\le1/4\) outside \(p\in(r,1/2)\). On the latter interval the **exact completed square** is
\[
D_r(p)=\frac{1-r+r^2}{3}
          -3\left(p-\frac{1+r}{3}\right)^2.
\tag{6}
\]
Its unique maximum occurs at \(p_0=(1+r)/3\in(r,1/2)\), with value \((1-r+r^2)/3\). Therefore nonnegative curvature throughout every branch follows precisely from
\(\gamma\le3/(1-r+r^2)\) when \(r<1/2\), or \(\gamma\le4\) when \(r\ge1/2\). Since \(1-r+r^2=3/4+(1/2-r)^2\), these coincide with (1) for \(q\le1/2\). Continuity of \(E'\) across transition points makes this piecewise nonnegative curvature sufficient for global convexity.

The cutoff is **necessary**, not just a branchwise upper bound. For \(r<1/2\), take \(x_0=\log[p_0/(1-p_0)]<0\). As \(p_0>r=q+\lambda\), the exact inequality
\(y(x_0)=x_0-\gamma(p_0-q)<-\gamma\lambda\)
places the maximizer strictly inside the negative active branch for every \(\gamma>0\). Hence (4) at \(x_0\) is negative for \(\gamma>3/(1-r+r^2)\). When \(r\ge1/2\), \(\Gamma=4\). For every \(\gamma>4\), a neighborhood of \(x=0\) has negative curvature: if \(\lambda>|q-1/2|\) the middle branch has \(E''(0)=1/\gamma-1/4<0\), if \(\lambda<|q-1/2|\) the negative active branch has \(E''(0)=(1/4)(1-\gamma/4)<0\), and at equality the one-sided branch curvatures near zero are negative. Reflection covers \(q>1/2\). This establishes both implications in (1), including equality.

The composite objective \(f_q+\lambda|x|\) is strictly convex and coercive. Its unique subgradient zero gives (2). For \(0<\gamma<4\), define \(T_\gamma(x)=\operatorname{soft}_{\gamma\lambda}(x-\gamma f'_q(x))\), where \(\operatorname{soft}_t(y)=\operatorname{sgn}(y)(|y|-t)_+\). Direct differentiation yields
\[
E'(x)=(1-\gamma a)\frac{x-T_\gamma(x)}\gamma.
\tag{7}
\]
Here \(1-\gamma a>0\); consequently \(E'(x)=0\) if and only if \(x=T_\gamma(x)\), equivalent to \(0\in f'_q(x)+\lambda\partial|x|\). The envelope is continuous and coercive (it differs from the coercive composite objective by bounded quantities at infinity), so its unique stationary point is its global minimizer.

Finally, in the separable weighted case, the full envelope equals \(\sum_i w_i E_{\gamma w_i,q_i,\lambda_i/w_i}(x_i)\); applying (1) coordinatewise yields (3). This completes the proof.

## Verification

The accompanying standalone `verify.py` checks (4) by exact symbolic differentiation, the polynomial identity (6) and its maximizer by exact symbolic algebra, and the restoration example by rational arithmetic. It additionally checks 150 deterministic parameter tuples on a dense grid, and constructs strict negative-curvature witnesses above the predicted thresholds. The reported numerical experiments are *illustrations*, not a substitute for the all-parameter branch proof. Reproduce with `python verify.py` using Python 3 and SymPy.

## Relationship to prior work

Zhang, Gao and Udell (2026) introduce online scaling for operator splitting and study sufficient smoothness and (weak) convexity conditions for forward–backward envelopes, explicitly including \(\ell_1\)-regularized logistic regression. Their Theorem 4.6 is a sufficient general bound; it neither supplies the exact regularizer-dependent boundary (1) nor identifies the restoration window. The earlier forward–backward truncated Newton treatment of Patrinos, Stella and Bemporad (2014) gives the general envelope identity and addresses logistic sparse problems, not this sharp scalar phase diagram. The unregularized scalar logistic envelope has a previously obtained boundary \(3/(1-q+q^2)\), which is the \(\lambda\to0\) limit of (1); it does **not** imply (1) because soft thresholding changes both active branches. The genuinely new part here is the strictly positive-penalty classification and the exact coupling between shrinkage and global envelope geometry. A search of indexed mathematical records for scalar logistic, sparsity, Moreau, and forward–backward curvature formulations found no covering statement; failure to locate a statement is not a proof of historical novelty.

## Limitations

The proof is scalar, or coordinate-separable with diagonal weights. It does not give the exact threshold for logistic regression with correlated features or arbitrary Hessian/preconditioner matrices, nor does it imply algorithmic convergence for stepsizes above any given splitting scheme's admissible range. The stationarity/minimizer identity is stated only for \(0<\gamma<4\). No external independent proof audit or exhaustive literature-priority determination is asserted.

## References

1. W. Zhang, W. Gao and M. Udell, *Operator Splitting Methods with Online Scaling*, arXiv:2609.10732, first posted 2026-09-09, https://arxiv.org/abs/2609.10732; §§2, 4.1 and Appendix B.
2. P. Patrinos, L. Stella and A. Bemporad, *Forward–backward truncated Newton methods for convex composite optimization*, 2014 open version, https://optimization-online.org/wp-content/uploads/2014/02/4254.pdf; envelope identities and sparse logistic example.
3. S. Bonettini, M. Prato and S. Rebegoldi, *Convergence of Inexact Forward–Backward Algorithms Using the Forward–Backward Envelope*, SIAM Journal on Optimization, 2020, https://doi.org/10.1137/19M1254155; general FBE algorithm context (abstract examined).
