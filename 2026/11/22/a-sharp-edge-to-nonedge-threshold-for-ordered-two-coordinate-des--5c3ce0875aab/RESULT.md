# A sharp edge-to-nonedge threshold for ordered two-coordinate descent on a three-node path

## Finding
Let \(H_c=\begin{pmatrix}1&-c&-c\\-c&1&0\\-c&0&1\end{pmatrix}\), where \(0<c<1/\sqrt2\), and minimize \(f(x)=\tfrac12 x^{\mathsf T}H_cx\) by **exactly two consecutive singleton coordinate minimizations**. The ordered coordinate pair is drawn from an arbitrary fixed law on all nine possible pairs, independently of the initial vector. Vertex \(0\) is the center and \(1,2\) are the leaves. Define the sharp worst-initial-state expected squared-energy decrement
\[
\delta(c)=\sup_{\pi}\inf_{x\ne0}\frac{\mathbb E_{(i,j)\sim\pi}\left[\|x\|_{H_c}^2-\|T_jT_ix\|_{H_c}^2\right]}{\|x\|_{H_c}^2},\qquad T_i=I-e_ie_i^{\mathsf T}H_c.
\]
The exact value is
\[
\boxed{\delta(c)=\begin{cases}
\dfrac{2(1-2c^2)}{3+2c-3c^2},&0<c\le1/\sqrt3,\\[5pt]
\dfrac{3-3c^2-\sqrt{9c^4-2c^2+1}}4,&1/\sqrt3\le c<1/\sqrt2.
\end{cases}}
\]
For \(0<c<1/\sqrt3\), draw a leaf uniformly for the first update, then update the center with probability
\[
\boxed{p_c=\frac{2(1+c)}{3+2c-3c^2}}
\]
and the *other leaf* with probability \(1-p_c\). This policy is globally optimal; every globally optimal law assigns positive mass to a nonedge leaf-to-leaf pair. For \(1/\sqrt3<c<1/\sqrt2\), always update a uniformly selected leaf first and the center second. This is globally optimal, and every globally optimal law uses only leaf-to-center ordered pairs. At \(c=1/\sqrt3\) the two displayed policies agree and the two formulas coincide. In particular, the strongest-coupling regime favors adjacent updates exclusively, whereas weaker coupling requires nonadjacent updates to attain the minimax optimum.

At \(c=1/4\), the optimal center-second probability is \(40/53\), with exact worst-state decrement \(28/53\). Always updating a leaf and then the center gives only \((45-\sqrt{233})/64\). The comparison is per *two exact coordinate solves*; it is not a runtime or asymptotic-rate claim.

## Assumptions and scope
All coordinates are real and the Hessian is the displayed \(3\times3\) symmetric positive-definite matrix (positive definite precisely when \(0<c<1/\sqrt2\)). The objective has zero linear term without loss of generality after translating to its minimizer. A draw of the ordered pair may use any distribution, including unequal marginals, repeats, and arbitrary dependence between first and second selections, but it is fixed in advance, not chosen adaptively from the initial state or observed gradients. An exact singleton update sets the current partial derivative to zero. The energy \(\|x\|_H^2=x^{\mathsf T}Hx\) equals twice the objective gap. The criterion is the least conditional expected energy reduction over all nonzero initial errors in one two-update block. It is not a claim about long-run stochastic convergence, parallel block minimization, or the number of iterations to a given tolerance.

## Proof
Write \(g=H_cx\). Because \((H_c)_{ii}=1\), a coordinate \(i\) update decreases energy by \(g_i^2\) and changes the other gradients to \(g_j-(H_c)_{ji}g_i\). Consequently the energy decrease for an ordered pair is exactly
\[
D_{ij}(g)=g_i^2+\left(g_j-(H_c)_{ji}g_i\right)^2.
\]
A repeated coordinate gives only \(g_i^2\). A leaf-to-center pair gives \(g_\ell^2+(g_0+cg_\ell)^2\); a center-to-leaf pair gives \(g_0^2+(g_\ell+cg_0)^2\); and a leaf-to-other-leaf pair gives \(g_1^2+g_2^2\).

**Weak coupling, universal upper bound.** Set \(g=(1-c,1,1)\), and \(x=H_c^{-1}g\). Each leaf-to-center or leaf-to-other-leaf pair has decrease exactly \(2\). Each center-to-leaf pair has decrease \(2-c^3(2-c)<2\), and every repeated pair has decrease strictly below \(2\). Direct inversion gives
\[
\|x\|_{H_c}^2=g^{\mathsf T}H_c^{-1}g=\frac{3+2c-3c^2}{1-2c^2}.
\]
Therefore *every* distribution has worst-state decrement at most \(\delta_0=2(1-2c^2)/(3+2c-3c^2)\).

**Weak coupling, attainment.** Put \(p=p_c\). Give each leaf-to-center ordered pair probability \(p/2\), and each of the two leaf-to-other-leaf pairs probability \((1-p)/2\). These are valid probabilities exactly when \(0<c\le1/\sqrt3\). Let \(F\) be the symmetric matrix satisfying \(x^{\mathsf T}Fx=\mathbb E[D_{ij}(H_cx)]\). In the invertible basis \(R=[e_0,e_1+e_2,e_1-e_2]\), direct multiplication gives the exact certificate
\[
R^{\mathsf T}(F-\delta_0H_c)R=\frac{2c}{3+2c-3c^2}
\left[uu^{\mathsf T}+\operatorname{diag}(0,0,(1+c)^2)\right],
\quad u=(1+c-c^2,-1-c,0)^{\mathsf T}.
\]
It is positive semidefinite for the entire stated parameter range. Hence the candidate guarantees decrement at least \(\delta_0\) for every initial vector, which matches the universal bound.

**Strong coupling.** Let \(F_B\) denote the expected-decrease matrix for a uniformly selected leaf followed by the center. In the same basis, the characteristic determinant for the center/leaf-symmetric generalized eigenmodes factors, up to a positive nonzero factor, as
\[
2t^2+(3c^2-3)t+1-2c^2.
\]
Its smaller root is
\[
t_B=\frac{3-3c^2-\sqrt{9c^4-2c^2+1}}4.
\]
The antisymmetric-leaf generalized eigenvalue is \((1+c^2)/2>t_B\); the inequality follows from \(9c^4-2c^2+1>(1-5c^2)^2\), valid for \(0<c<1/\sqrt2\), whenever its right comparison is needed. Thus \(F_B-t_BH_c\succeq0\), with equality in its symmetric worst mode.

For an explicit universal upper-bound witness, set
\[
z_c=\frac{c^2+\sqrt{9c^4-2c^2+1}-1}{2c},\qquad g=(z_c,1,1),\qquad x=H_c^{-1}g.
\]
The stationary equation of the leaf-to-center Rayleigh quotient is \(cz^2+(1-c^2)z-2c^3=0\), and \(z_c\) is its positive root. For \(1/\sqrt3\le c<1/\sqrt2\), the inequalities \(1-c\le z_c<1\) follow by evaluating this increasing-through-positive-root quadratic at \(1-c\) and at \(1\); explicitly the respective values are \(1-3c^2\le0\) and \(1+c-c^2-2c^3>0\). The latter is positive because \(2c^3<c\) in the allowed range.

For this symmetric gradient the gain from every leaf-to-center pair is \(B=1+(z_c+c)^2\). Every leaf-to-other-leaf pair has gain \(2\le B\), and every center-to-leaf pair has gain \(z_c^2+(1+cz_c)^2=B-c^2(1-z_c^2)<B\). Each repeated-pair gain is either \(1\) or \(z_c^2\), also smaller than \(B\). Since the chosen symmetric direction is the smallest generalized eigenmode of \(F_B\), its quotient is precisely \(t_B\). No arbitrary pair distribution can improve upon this witness, while the leaf-to-center law attains it. Strictness of the preceding inequalities for \(c>1/\sqrt3\) forces every optimal law to avoid all but leaf-to-center pairs.

**Sharp transition and necessity of nonedges.** At \(c=1/\sqrt3\), one has \(p_c=1\) and \(\delta_0=t_B\). For \(0<c<1/\sqrt3\), the weak-coupling witness strictly forbids hub-first and repeated choices in any optimal law. An edge-only optimal law would therefore have to use leaf-to-center pairs exclusively. By symmetry, the best such distribution is uniform over the two leaves (symmetrization cannot decrease a minimum generalized eigenvalue); its worst reduction equals \(t_B\), strictly below \(\delta_0\) because the leaf-to-center Rayleigh quotient has a strict interior minimizer at \(z_c<1-c\) when \(c<1/\sqrt3\). Hence every weak-coupling optimizer must give positive probability to nonadjacent leaf-to-leaf updates. This completes the global characterization of the optimal value and the claimed mandatory support patterns.

## Verification
Run `python verification/check.py` after installing `verification/requirements.txt`. The script constructs the nine exact two-coordinate energy matrices from the actual update operators, symbolically checks the weak-coupling positive-semidefinite certificate, the strong-coupling characteristic polynomial and the stationary equation, and tests 90 ordered-pair matrices at rational coupling values. It completed successfully. Exact identities and the analytic sign arguments establish the theorem for the continuous parameter interval; the finite tests are only supplemental checks.

## Relationship to prior work
Tu et al., *Breaking Locality Accelerates Block Gauss-Seidel* (arXiv:1701.03863; first public 2017-01-14), compare fixed and randomized simultaneous block selection and general convergence factors. Hanzely and Richtárik, *Accelerated Coordinate Descent with Arbitrary Sampling and Best Rates for Minibatches* (arXiv:1809.09354; first public 2018-09-25), design arbitrary set-valued minibatch probabilities and associated convergence bounds. Neither inspected full paper derives the exact two-**successive-singleton** ordered-pair optimum on the three-node path. The difference from simultaneous two-coordinate minimization is essential: here the first gradient affects the second and order matters.

Related published mathematical records include exact optimal sampling for *simultaneous* all-but-one-coordinate minimization on three-variable stars, optimized *single-step* sampling for general three-variable Hessians, and sharp fixed-order Gauss-Seidel horizons. These have different update maps and optimization domains; their conclusions do not imply the displayed pair-coupling threshold. A prior result on regular-graph two-step sampling also does not imply the conclusion because the three-node path is nonregular and has a positive-probability nonedge regime. General semidefinite-optimization machinery could reproduce this finite problem in principle; priority for this closed-form classification merits independent specialist checking.

## Limitations
The result applies to one two-step block, exactly three variables, equal leaf couplings and unrelaxed exact line minimization. It does not prove optimal long-horizon schedules, adaptive sampling, or cost gains after accounting for distribution design. Its explicit optimal law is fixed before the initial vector, unlike gradient-responsive policies. Publication-priority equivalence with older order-dependent quadratic design literature cannot be categorically excluded without exhaustive historical review. Independent mathematical review has not been performed.

## References
1. S. Tu, S. Venkataraman, A. C. Wilson, A. Gittens, M. I. Jordan and B. Recht, *Breaking Locality Accelerates Block Gauss-Seidel*, arXiv:1701.03863, 2017-01-14; https://arxiv.org/abs/1701.03863 ; PMLR 70 (2017), https://proceedings.mlr.press/v70/tu17a.html .
2. F. Hanzely and P. Richtárik, *Accelerated Coordinate Descent with Arbitrary Sampling and Best Rates for Minibatches*, arXiv:1809.09354, 2018-09-25; https://arxiv.org/abs/1809.09354 ; PMLR 89 (2019), https://proceedings.mlr.press/v89/hanzely19a.html .
3. P. Rodomanov and P. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587, 2019-04-09; https://arxiv.org/abs/1904.04587 .
