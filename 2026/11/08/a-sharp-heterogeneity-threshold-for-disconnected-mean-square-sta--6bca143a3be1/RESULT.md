# A sharp heterogeneity threshold for disconnected mean-square stability windows in Markov-sampled quadratic SGD

## Finding

Consider constant-step stochastic gradient descent on two centered scalar quadratic losses of curvatures \(1+c\) and \(1-c\), where \(0<c<1\), with samples selected by a stationary, symmetric, anti-persistent two-state Markov chain. Reentrant mean-square stability for the same model at one fixed curvature ratio was already established in [5]. The additional result here is the **sharp boundary over all curvature contrasts**: for the given \(c\), there exists such a chain whose stable learning rates have two components separated by a positive-length instability gap if and only if
\[
c^2>q_*:=\frac{5+2\sqrt{13}}{27}.
\]
The same strict boundary applies if the gap is allowed to consist of a single marginal step. A cubic polynomial and its discriminant classify the stable set for each anti-persistence parameter, including which multiple-root boundaries are punctures rather than a collapse of the larger-step interval. The rational example \(c=7/10\), with chain lag-one sign correlation \(\lambda=-19/20\), illustrates the phenomenon: it is stable at steps \(h=1\) and \(h=3\), but unstable at \(h=2\) and \(h=4\).

## Assumptions and scope

The individual losses are \(f_\pm(x)=\tfrac12(1\pm c)x^2\), with \(0<c<1\); their average is \(f(x)=\tfrac12x^2\). Independently of \(X_0\ne0\), the sign process \((S_k)_{k\ge0}\) starts at its stationary fair law on \(\{-1,+1\}\) and follows the irreducible transition matrix
\[
P_\lambda=\tfrac12\begin{pmatrix}1+\lambda&1-\lambda\\1-\lambda&1+\lambda\end{pmatrix},\qquad -1<\lambda<0.
\]
The update is \(X_{k+1}=[1-h(1+cS_k)]X_k\), for a constant \(h>0\). Mean-square exponential stability means \(\mathbb E[X_n^2]\to0\) exponentially for every finite deterministic nonzero \(X_0\); the opposite case means it fails to vanish. The chain must be temporally correlated: the independent case is outside the stated anti-persistence range. Write \(q=c^2\).

Define
\[
G_{\lambda,q}(h)=\lambda(1-q)^2h^3-4\lambda(1-q)h^2
+[\lambda(5-3q)-(1+q)]h+2(1-\lambda)
\]
and
\[
\begin{aligned}
\mathcal P(\lambda,q)={}&(27q^3-18q^2-q)\lambda^3\\
&+(27q^3-57q^2+21q+1)\lambda^2\\
&+(9q^3-56q^2+41q-2)\lambda+(1+q)^3.
\end{aligned}
\]
Then stability holds **exactly** for \(h>0\) satisfying \(G_{\lambda,q}(h)>0\). The stable set has two components with a positive-length gap exactly when \(\mathcal P(\lambda,q)<0\). In that case the cubic has distinct positive roots \(0<r_1<r_2<r_3\), and the stable set is
\[
(0,r_1)\cup(r_2,r_3).
\]
When \(\mathcal P(\lambda,q)>0\), the stable set is the single interval from zero to the unique positive root. When \(\mathcal P=0\) and there are a double root \(d\) and a distinct simple root \(s\), the stable set is \((0,d)\cup(d,s)\) if \(d<s\) and \((0,s)\) if \(s<d\). This order can be read off from \(s+2d=4/(1-q)\). For a triple root \(r\) the stable set is \((0,r)\). Multiple roots themselves are never mean-square stable.

## Proof

**Step 1: exact second-moment transfer.** Define the nonnegative statewise squared multipliers
\[
A=[1-h(1+c)]^2,\qquad B=[1-h(1-c)]^2.
\]
Propagating the conditional second-moment masses yields the nonnegative \(2\times2\) transfer matrix \(M=P_\lambda^{\mathsf T}\operatorname{diag}(A,B)\) (equivalently its transposed cyclic product). Its Perron eigenvalue governs the exponential rate, because the stationary starting sign law gives a strictly positive initial moment-mass vector. Direct computation gives
\[
\det M=\lambda AB\le0,\qquad \det(I-M)=hG_{\lambda,q}(h).
\]
Since the other eigenvalue of \(M\) is nonpositive, the Perron eigenvalue is below, equal to, or above one exactly as \(\det(I-M)\) is positive, zero, or negative. If the Perron eigenvalue is at least one, projecting the positive initial moment vector onto a nonzero nonnegative left Perron eigenvector gives a nonvanishing lower bound for the sum of the moments. If it is less than one, the matrix powers decay exponentially. This proves the exact cubic criterion for every \(h>0\), including steps where a multiplier vanishes.

**Step 2: root topology.** The leading cubic coefficient is negative and its constant coefficient is positive. Moreover, for every \(t\ge0\), all four terms in \(G_{\lambda,q}(-t)\) are nonnegative and the constant term strictly positive, because \(-1<\lambda<0\) and \(0<q<1\). Thus \(G\) has no nonpositive real zero and has at least one positive real zero. Its discriminant factors exactly as
\[
\operatorname{Disc}_h G=4\lambda(1-q)^2\mathcal P(\lambda,q).
\]
Consequently \(\mathcal P<0\) is equivalent to three distinct positive zeros, which give the asserted two stable intervals from the alternating signs of the cubic; \(\mathcal P>0\) gives exactly one real zero, necessarily positive. For \(\mathcal P=0\) a real cubic has either a triple real root or one double real root and one distinct simple real root, all positive here. In the latter case, writing \(G(h)=\lambda(1-q)^2(h-s)(h-d)^2\) gives strict positivity exactly for \(0<h<s\) with \(h\ne d\); the coefficient of \(h^2\) gives the root sum. An explicit puncture occurs for \(q=(97+5\sqrt{745})/512\) and \(\lambda=-(1+q)/(5/16+3q)\), which lie in the admissible ranges. With \(z=(1-q)h\), the equations \(G=G_h=0\) at \(z=5/4\) reduce to that value of \(\lambda\) and \(256q^2-97q-9=0\). The remaining root has \(z=4-2(5/4)=3/2>5/4\) by the root sum.

**Step 3: the sharp heterogeneity boundary.** The cubic discriminant of \(\mathcal P\), regarded as a polynomial in \(\lambda\), factors as
\[
\operatorname{Disc}_\lambda\mathcal P=-256q(q-1)^3(27q^2-10q-1)^3.
\]
For \(0<q<q_*\), it is strictly negative, so \(\mathcal P(\cdot,q)\) has only one real zero and it is simple. The leading coefficient is nonzero for \(0<q\le 1/2\), since \(27q^2\le (27/2)q<18q+1\). But
\[
\mathcal P(-1,q)=-4(q-1)^2(2q-1)>0,
\quad\mathcal P(0,q)=(1+q)^3>0
\]
throughout this range (because \(q_*<1/2\)). A cubic with only one simple real zero and positive values at both endpoints cannot vanish between them. Continuity extends nonnegativity to \(q=q_*\).

For \(q_*<q<1/2\), the discriminant in \(\lambda\) is positive, so there are three simple real roots, with no roots crossing \(-1\) or \(0\) as \(q\) varies over this connected interval. At \(q=49/100\), direct exact substitution gives \(\mathcal P(-19/20,49/100)<0\) (equivalently, the rational witness below), establishing that two roots lie in \((-1,0)\) there. They therefore remain in that interval for every \(q\) between \(q_*\) and \(1/2\), and \(\mathcal P\) is negative somewhere between those two roots. For \(q=1/2\), \(\mathcal P(-19/20,1/2)=-733/64000<0\). For \(1/2<q<1\), \(\mathcal P(-1,q)<0\), so by continuity it remains negative at some \(\lambda>-1\). The threshold is therefore necessary and sufficient. At equality the polynomial has an interior double \(\lambda\)-root
\[
\lambda_* =\frac{-17+4\sqrt{13}}{3},
\]
and the learning-rate cubic has a triple positive zero at \(h_*=4/[3(1-q_*)]\), as certified by substituting into \(G,G_h,G_{hh}\). The zero of \(\mathcal P(\cdot,q_*)\) at \(\lambda_*\) is the only interior zero: nonnegativity forces every interior zero to have even multiplicity, and the polynomial is cubic. So there is no puncture or positive-length gap at or below the threshold. Above it there is always a positive-length gap for some admissible chain by the proof that \(\mathcal P<0\) somewhere.

**Step 4: exact rational witness.** At \(q=49/100\), \(\lambda=-19/20\),
\[
G(h)=-\frac3{200000}(16473h^3-129200h^2+322900h-260000).
\]
At learning rates \(h=1,2,3,4\), the corresponding values of \(\det(I-M)\) are, in order,
\[
\frac{149481}{200000},\quad-\frac{147}{6250},\quad
\frac{83961}{200000},\quad-\frac{3501}{3125}.
\]
The sign alternation guarantees three distinct positive roots in \((1,2),(2,3),(3,4)\), hence exactly two stability windows. Sharper rational isolating intervals are \((189/100,190/100)\), \((226/100,227/100)\), and \((369/100,370/100)\). This also demonstrates the effect without any nonconvex component loss.

## Verification

Run `python check_boundary.py` in a Python 3 environment with SymPy installed. The supplemental certificate checks the nested discriminant, endpoint signs, triple root and the puncture example; it also checks the transform of [5]'s determinant and the four rational witness values. The original companion `verify.py` checks both discriminant factorizations, the cusp, and three positive-root isolating intervals for the rational example; its output is in `verification_output.txt`. These checks certify polynomial identities and finite witnesses. The global parameter classification additionally uses the analytic sign, continuity and root-count arguments in the proof.

## Relationship to prior work

Huo, Chen, and Xie (2022) analyze constant-stepsize linear stochastic approximation with Markovian data, principally for sufficiently small learning rates and stationary bias; their theorems do not state the global disconnected-stability classification above. Durmus and coauthors (2021) establish general random-matrix-product moment bounds for Markovian noise, rather than an exact sharp heterogeneity threshold. Mulayoff and Michaeli (2023) give exact mean-square SGD stability under independently sampled Hessians, an assumption that excludes this Markov anticorrelation mechanism.

A close algebraic antecedent is Gürbüzbalaban, Hu, Şimşekli, and Zhu (2023): Appendix B.4.3, Lemma 6, equation (61), and Corollary 4 give regenerative moment conditions for two-state Markov stepsizes. At the scalar-product level, curvature sampling can be written as Markov effective stepsizes \(h(1\pm c)\). The formula can serve as another starting point for a stability calculation; it does not give the sharp all-contrast domain.

The closest theorem is [5], which uses curvatures 1 and 6 and gives the same determinant/cubic method, the exact persistence threshold at that contrast, and the larger-step collision there. Its stay probability \(p\) and step \(\eta\) identify with \(\lambda=2p-1\) and \(h=7\eta/2\); the contrast is \(q=(5/7)^2\). Under this substitution \(hG_{\lambda,q}(h)=\eta C_p(\eta)\) with \(C_p\) from [5]. Thus the phenomenon and the fixed-contrast classification are not new. The additional statement is the sharp existence threshold across variable \(q\), the joint phase criterion on the anti-persistent domain, and the general distinction between a puncture and the collapse already seen at ratio six. The ratio-six analysis, even together with the geometric criterion, does not determine the real-root topology as \(q\) varies: the second discriminant and endpoint signs give that extra step.

## Limitations

The result concerns mean-square convergence of the homogeneous one-dimensional strongly convex quadratic model; it does not imply almost-sure divergence whenever mean-square stability fails, or provide an additive-noise stationary variance. The Markov chain is stationary, two-state, symmetric and anti-persistent; unequal stationary weights, momentum, higher dimensions, arbitrary Markov chains and general nonlinear losses are not covered. The algebraically related two-state random-stepsize framework in earlier literature leaves a real residual precedence risk; independent subject-specialist review has not been performed.

## References

- D. Huo, Y. Chen, Q. Xie, *Bias and Extrapolation in Markovian Linear Stochastic Approximation with Constant Stepsizes*, first posted October 3, 2022, https://arxiv.org/abs/2210.00953 (Sections 3–4, related assumptions and appendices).
- A. Durmus, E. Moulines, A. Naumov, S. Samsonov, W. Wai, *On the Stability of Random Matrix Product with Markovian Noise: Application to Linear Stochastic Approximation and TD Learning*, 2021, https://arxiv.org/abs/2102.00185 (moment bounds and Markovian products).
- R. Mulayoff, T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, first posted June 13, 2023, https://arxiv.org/abs/2306.07850 (independently sampled Hessian assumption and exact IID threshold).
- M. Gürbüzbalaban, Y. Hu, U. Şimşekli, L. Zhu, *Cyclic and Randomized Stepsizes Invoke Heavier Tails in SGD than Constant Stepsize*, first posted February 10, 2023, https://arxiv.org/abs/2302.05516 (Appendix B.4.3, Lemma 6, equation (61), two-state Markovian stepsize products).
- [5] *A reentrant mean-square stability window for Markov-sampled quadratic descent*, Resultary, October 12, 2026, https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-a-reentrant-mean-square-stability-window-for-markov-sampled-quad--2e4ff5de9e1e/RESULT.md .
