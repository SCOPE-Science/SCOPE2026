# A sharp heterogeneity threshold for disconnected mean-square stability windows in Markov-sampled quadratic SGD

## Finding

Consider constant-step stochastic gradient descent on two centered scalar quadratic losses of curvatures \(1+c\) and \(1-c\), where \(0<c<1\), with samples selected by a stationary, symmetric, anti-persistent two-state Markov chain. Even though both component losses are strongly convex, its mean-square-stable positive learning rates can form **two disjoint open intervals**. There is a sharp universal boundary: such a chain exists for the given heterogeneity \(c\) if and only if
\[
c^2>q_*:=\frac{5+2\sqrt{13}}{27}.
\]
For each fixed anti-persistence parameter, a cubic polynomial and an explicit discriminant completely classify the stable learning rates. In particular, the rational example \(c=7/10\) and chain lag-one sign correlation \(\lambda=-19/20\) is stable at steps \(h=1\) and \(h=3\), but unstable at \(h=2\) and \(h=4\). Thus, decreasing the learning rate may destroy mean-square stability even for a strongly convex objective.

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
Then stability holds **exactly** for \(h>0\) satisfying \(G_{\lambda,q}(h)>0\). It has two nonempty separated open intervals exactly when \(\mathcal P(\lambda,q)<0\). In that case the cubic has distinct positive roots \(0<r_1<r_2<r_3\), and the stable set is
\[
(0,r_1)\cup(r_2,r_3).
\]
When \(\mathcal P(\lambda,q)>0\), the stable set is the single interval from zero to the unique positive root. At the discriminant boundary \(\mathcal P=0\), use the exact strict inequality \(G>0\), which also determines whether an isolated marginally unstable step punctures an interval.

## Proof

**Step 1: exact second-moment transfer.** Define the nonnegative statewise squared multipliers
\[
A=[1-h(1+c)]^2,\qquad B=[1-h(1-c)]^2.
\]
Propagating the conditional second-moment masses yields the nonnegative \(2\times2\) transfer matrix \(M=P_\lambda^{\mathsf T}\operatorname{diag}(A,B)\) (equivalently its transposed cyclic product). Its Perron eigenvalue governs the exponential rate, because the stationary starting sign law gives a strictly positive initial moment-mass vector. Direct computation gives
\[
\det M=\lambda AB\le0,\qquad \det(I-M)=hG_{\lambda,q}(h).
\]
Since the other eigenvalue of \(M\) is nonpositive, the Perron eigenvalue is below, equal to, or above one exactly as \(\det(I-M)\) is positive, zero, or negative. This proves the exact cubic criterion for every \(h>0\), including steps where a multiplier vanishes.

**Step 2: root topology.** The leading cubic coefficient is negative and its constant coefficient is positive. Moreover, for every \(t\ge0\), all four terms in \(G_{\lambda,q}(-t)\) are nonnegative and the constant term strictly positive, because \(-1<\lambda<0\) and \(0<q<1\). Thus \(G\) has no nonpositive real zero and has at least one positive real zero. Its discriminant factors exactly as
\[
\operatorname{Disc}_h G=4\lambda(1-q)^2\mathcal P(\lambda,q).
\]
Consequently \(\mathcal P<0\) is equivalent to three distinct positive zeros, which give the asserted two stable intervals from the alternating signs of the cubic; \(\mathcal P>0\) gives exactly one real zero, necessarily positive.

**Step 3: the sharp heterogeneity boundary.** The cubic discriminant of \(\mathcal P\), regarded as a polynomial in \(\lambda\), factors as
\[
\operatorname{Disc}_\lambda\mathcal P=-256q(q-1)^3(27q^2-10q-1)^3.
\]
For \(0<q<q_*\), it is strictly negative, so \(\mathcal P(\cdot,q)\) has only one real zero. But
\[
\mathcal P(-1,q)=-4(q-1)^2(2q-1)>0,
\quad\mathcal P(0,q)=(1+q)^3>0
\]
throughout this range (because \(q_*<1/2\)). A continuous cubic with only one real zero and positive values at both endpoints cannot be negative between them. Continuity extends nonnegativity to \(q=q_*\).

For \(q_*<q<1/2\), the discriminant in \(\lambda\) is positive, so there are three simple real roots, with no roots crossing \(-1\) or \(0\) as \(q\) varies over this connected interval. At \(q=49/100\), direct exact substitution gives \(\mathcal P(-19/20,49/100)<0\) (equivalently, the rational witness below), establishing that two roots lie in \((-1,0)\) there. They therefore remain in that interval for every \(q\) between \(q_*\) and \(1/2\), and \(\mathcal P\) is negative somewhere between those two roots. For \(q=1/2\), \(\mathcal P(-19/20,1/2)=-733/64000<0\). For \(1/2<q<1\), \(\mathcal P(-1,q)<0\), so by continuity it remains negative at some \(\lambda>-1\). The threshold is therefore necessary and sufficient. At equality the polynomial has an interior double \(\lambda\)-root
\[
\lambda_* =\frac{-17+4\sqrt{13}}{3},
\]
and the learning-rate cubic has a triple positive zero at \(h_*=4/[3(1-q_*)]\), as certified by its first two derivatives.

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

Run `python verify.py` in a Python 3 environment with SymPy installed. The script reconstructs the full moment transfer, checks the two discriminant factorizations and cusp identities symbolically, and independently evaluates the rational witness and three positive-root isolating intervals. Its output is provided in `verification_output.txt`. These checks certify the specified polynomial identities; the global parameter classification additionally uses the analytic sign, continuity and root-count arguments in the proof.

## Relationship to prior work

Huo, Chen, and Xie (2022) analyze constant-stepsize linear stochastic approximation with Markovian data, principally for sufficiently small learning rates and stationary bias; their theorems do not state the global disconnected-stability classification above. Durmus and coauthors (2021) establish general random-matrix-product moment bounds for Markovian noise, rather than an exact sharp heterogeneity threshold. Mulayoff and Michaeli (2023) give exact mean-square SGD stability under independently sampled Hessians, an assumption that excludes this Markov anticorrelation mechanism.

A closer algebraic comparison is Gürbüzbalaban, Hu, Şimşekli, and Zhu (2023): their Appendix B.4.3, especially Lemma 6 and equation (61), develops a two-state Markov-stepsize scalar moment-growth expression. Because scalar curvature sampling can be reparameterized as random effective step size, that transfer framework encompasses the underlying two-state products. The distinctive result here is **not** the transfer-matrix formula; it is the complete *nonmonotone learning-rate stability-set classification* and the exact cusp threshold \(q_*\), neither stated in the inspected paper. Deriving the sharp boundary requires the two nested discriminants and a global real-root argument. This is a meaningful but specific novelty claim, not a claim of inventing Markov moment transfers.

## Limitations

The result concerns mean-square convergence of the homogeneous one-dimensional strongly convex quadratic model; it does not imply almost-sure divergence whenever mean-square stability fails, or provide an additive-noise stationary variance. The Markov chain is stationary, two-state, symmetric and anti-persistent; unequal stationary weights, momentum, higher dimensions, arbitrary Markov chains and general nonlinear losses are not covered. The algebraically related two-state random-stepsize framework in earlier literature leaves a real residual precedence risk; independent subject-specialist review has not been performed.

## References

- D. Huo, Y. Chen, Q. Xie, *Bias and Extrapolation in Markovian Linear Stochastic Approximation with Constant Stepsizes*, first posted October 3, 2022, https://arxiv.org/abs/2210.00953 (Sections 3–4, related assumptions and appendices).
- A. Durmus, E. Moulines, A. Naumov, S. Samsonov, W. Wai, *On the Stability of Random Matrix Product with Markovian Noise: Application to Linear Stochastic Approximation and TD Learning*, 2021, https://arxiv.org/abs/2102.00185 (moment bounds and Markovian products).
- R. Mulayoff, T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, first posted June 13, 2023, https://arxiv.org/abs/2306.07850 (independently sampled Hessian assumption and exact IID threshold).
- M. Gürbüzbalaban, Y. Hu, U. Şimşekli, L. Zhu, *Cyclic and Randomized Stepsizes Invoke Heavier Tails in SGD than Constant Stepsize*, first posted February 10, 2023, https://arxiv.org/abs/2302.05516 (Appendix B.4.3, Lemma 6, equation (61), two-state Markovian stepsize products).
