# A sharp non-log-concave mixing frontier on a four-state reversible path

## Finding

Fix the path on four states and a prescribed stationary distribution
\[\pi=\frac{(1,t,t,1)}{2(1+t)},\qquad t>0.\]
Among **all** reversible, nonnegative, stochastic nearest-neighbor transition matrices (holding allowed), the minimum second-largest eigenvalue modulus is
\[
\mu_*(t)=
\begin{cases}
1-\dfrac{2t}{t+3+2\sqrt2},&0<t\leq1,\\[4pt]
\dfrac1{\sqrt{1+t}},&t\geq1.
\end{cases}
\]
The optimal chain is unique, including against choices that break left-right reflection symmetry. In the unnormalized edge-flow coordinates defined below, its three weights are \((a_*,b_*,a_*)\), where
\[
(a_*,b_*)=
\begin{cases}
\left(\dfrac{t(2+\sqrt2)}{t+3+2\sqrt2},\dfrac{t(t+1+\sqrt2)}{t+3+2\sqrt2}\right),&0<t\leq1,\\[7pt]
\left(\dfrac{t}{1+t},\dfrac t2\right),&t\geq1.
\end{cases}
\]
The formulas agree at \(t=1\). For \(0<t<1\), both interior holding probabilities vanish; for \(t>1\), they equal \((t-1)/(2(t+1))\). The optimal SLEM is continuous but has unequal one-sided derivatives \(-1/4\) and \(-1/(4\sqrt2)\) at \(t=1\). The non-log-concave branch \(0<t<1\), its exact optimizer and unrestricted uniqueness are the central contribution; the \(t\geq1\) branch recovers an existing harmonic-flow result in this special family.

## Assumptions and scope

Let \(M=\operatorname{diag}(1,t,t,1)\), and let \(L(a,b,c)\) denote the weighted combinatorial path Laplacian with successive edge flows \(a,b,c\). Define \(P=I-M^{-1}L(a,b,c)\). Then \(P\) is reversible with stationary law \(\pi\), and its entries are
\[
P=\begin{pmatrix}
1-a&a&0&0\\
a/t&1-(a+b)/t&b/t&0\\
0&b/t&1-(b+c)/t&c/t\\
0&0&c&1-c
\end{pmatrix}.
\]
The *entire* feasible set is given by \(a,b,c\geq0\), \(a,c\leq1\), \(a+b\leq t\), and \(b+c\leq t\). The actual stationary edge fluxes are \(a/[2(1+t)]\), \(b/[2(1+t)]\), \(c/[2(1+t)]\). Let \(\mu(P)\) denote the largest absolute eigenvalue of \(P\) except for the designated stationary eigenvalue \(1\), counting any additional unit eigenvalue if the chain is reducible. This is the customary SLEM for reversible finite chains. All displayed optima have strictly positive edge flows and SLEM below one.

## Proof

**1. Exact certificate for \(0<t\leq1\).** Put \(r=1+\sqrt2\), \(d=r^2+t=t+3+2\sqrt2\) and \(q=(r,1,-1,-r)^\mathsf T\). This vector is \(M\)-orthogonal to the constant vector. The generalized Rayleigh principle for \(Lq=\lambda Mq\) gives, for the smallest positive generalized eigenvalue \(\gamma\),
\[
\gamma\leq \frac{q^\mathsf T Lq}{q^\mathsf T Mq}
=\frac{2(a+c)+4b}{2(r^2+t)}
=\frac{a+c+2b}{r^2+t}
\leq\frac{2t}{r^2+t}=:\gamma_*.
\]
The last inequality is the sum of the two interior stochasticity constraints. Therefore \(\mu(P)\geq1-\gamma\geq1-\gamma_*\).

Set \(a=c=x=t(2+\sqrt2)/d\) and \(b=y=t(t+1+\sqrt2)/d\). Both are positive, \(x+y=t\), and \(x<1\). Direct substitution verifies \(L(x,y,x)q=\gamma_* Mq\). To check that \(\gamma_*\) is the smallest positive eigenvalue and that a negative eigenvalue of \(P\) does not defeat the bound, use reflection parity. The even sector has generalized Laplacian eigenvalues \(0\) and \(e=x(1+1/t)\). The odd sector has the two roots \(\lambda_-<\lambda_+\) of
\[
\lambda^2-\left(x+\frac{x+2y}{t}\right)\lambda+\frac{2xy}{t}=0.
\]
The polynomial evaluated at \(e\) is \(-2xy/t^2<0\), so \(\lambda_-<e<\lambda_+\). The positive odd eigenvector \(q\) has \(\lambda_-=\gamma_*\), and
\[
\lambda_-+\lambda_+=x+\frac{x+2y}{t}=2+x\left(1-\frac1t\right)\leq2.
\]
Thus the largest absolute nonstationary eigenvalue of \(P\) is \(1-\lambda_-=1-\gamma_*\); the lower bound is sharp.

For uniqueness, suppose any feasible \((a,b,c)\) attains this bound. Both Rayleigh inequalities must then be equalities. In particular, \(a+b=c+b=t\), so \(a=c\), and equality of the Rayleigh quotient forces \(q\) to be a generalized eigenvector of eigenvalue \(\gamma_*\). Its first coordinate gives \(a(r-1)=\gamma_*r\), yielding precisely \(a=x\); the other two constraints give \(b=y\). This proves global uniqueness without assuming symmetry.

**2. Exact certificate for \(t\geq1\).** Set \(S=M^{1/2}PM^{-1/2}\), and let \(\Pi\) be the orthogonal projector onto the stationary vector proportional to \((1,\sqrt t,\sqrt t,1)\). Then \(\mu(P)=\|S-\Pi\|_2\). With \(v=(1,0,0,-1)^\mathsf T/\sqrt2\), one has \(\Pi v=0\) and
\[
\begin{aligned}
\mu(P)^2&\geq\|(S-\Pi)v\|_2^2\\
&=\frac12\left[(1-a)^2+\frac{a^2}{t}+(1-c)^2+\frac{c^2}{t}\right]\\
&=\frac1{1+t}+\frac{1+1/t}{2}\left[\left(a-\frac{t}{t+1}\right)^2+\left(c-\frac{t}{t+1}\right)^2\right].
\end{aligned}
\]
In particular \(\mu(P)\geq1/\sqrt{1+t}\), with equality requiring \(a=c=t/(1+t)\). For \(t\geq1\), these outer weights together with \(b=t/2\) are feasible. In the odd reflection sector, the symmetrized transition is
\[
K=\begin{pmatrix}
1-a&a/\sqrt t\\[2pt]
a/\sqrt t&1-(a+2b)/t
\end{pmatrix}.
\]
At the proposed weights \(K^2=I_2/(1+t)\); the remaining nonstationary even eigenvalue is zero. This attains the bound.

Finally, if equality holds, the squared-norm lower bound forces the two outer weights. With \(a=c=t/(1+t)\), equality in the operator-norm bound applied to the first odd basis vector forces that vector to be an eigenvector of \(K^2\). Since \(K_{12}>0\), the off-diagonal identity \((K^2)_{12}=K_{12}\operatorname{tr}K\) gives \(\operatorname{tr}K=0\), hence \(b=t/2\). Uniqueness follows. At \(t=1\), both descriptions coincide.

**3. Sharp interface.** The lower branch differentiates to \(-2(3+2\sqrt2)/(t+3+2\sqrt2)^2\), with left derivative \(-1/4\) at one; the upper branch differentiates to \(-1/[2(1+t)^{3/2}]\), with right derivative \(-1/(4\sqrt2)\). The optimal chain remains continuous, but both the interior holding probability and the SLEM slope change regime at one.

## Verification

The standalone file `verify.py` tests the exact vector-eigenvalue identity, parity characteristic polynomial, spectral matrix-square identity, boundary matching, and stochasticity relations symbolically using SymPy. It additionally checks the exact candidate eigenvalues and 1,800 reproducible random feasible (including asymmetric) chains across twelve mass ratios using NumPy. Run `python verify.py` with SymPy and NumPy installed. The analytic variational and operator-norm inequalities above prove the continuum statement; sampled computations are only supplementary.

At \(t=1/2\), the unique optimal edge flows are approximately \((0.2697521434,0.2302478566,0.2697521434)\), with SLEM \(0.8419828529\). At \(t=2\), they are \((2/3,1,2/3)\), with SLEM \(1/\sqrt3\).

## Relationship to prior work

The 2004 and 2006 Boyd–Diaconis collaboration establishes convex fastest-mixing formulations and the uniform-stationary path optimum; the 2007 symmetry analysis develops general reductions. The later prescribed-stationary-flow treatment by Jafarizadeh (2020), §VI.B and Appendix B, states the harmonic rule \(q_i=\pi_i\pi_{i+1}/(\pi_i+\pi_{i+1})\) for log-concave stationary masses. Within this family the condition requires \(t\geq1\). The new result supplies the complete non-log-concave \(0<t<1\) optimizer, its active interior stochasticity constraints, uniqueness against asymmetric chains, and the sharp interface with that previously covered harmonic regime. Cihan–Akar's degree-proportional stationary laws address a different constrained family (the four-path degree profile corresponds to \(t=2\)); their results do not give the low-mass branch.

## Limitations

This classification covers four-state paths with reflected two-level stationary masses only. It does not prove a general formula for arbitrary non-log-concave stationary distributions or for longer paths. The references and indexed comparison are evidence for publication priority, not an exhaustive literature or independent mathematical audit. The 2018 path article was accessible only in abstract, and unindexed earlier work may contain equivalent special cases.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://doi.org/10.1137/S0036144503423264
2. S. Boyd, P. Diaconis, J. Sun, L. Xiao, *Fastest Mixing Markov Chain on a Path*, American Mathematical Monthly 113 (2006), 70–74. https://web.stanford.edu/~boyd/papers/pdf/fmmc_path.pdf
3. S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955 (public version of September 6, 2007). https://arxiv.org/abs/0709.0955
4. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks 6 (2020), 88–104. https://doi.org/10.1109/TSIPN.2020.2964211
5. O. Cihan, M. Akar, *Fastest Random Walk on a Path*, International Journal of Systems Science 50 (2019), 1–7. https://doi.org/10.1080/00207721.2018.1543470
