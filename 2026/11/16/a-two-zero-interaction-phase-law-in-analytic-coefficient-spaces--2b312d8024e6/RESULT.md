# A two-zero interaction phase law in analytic coefficient spaces

## Finding

For every real \(1<p<\infty\), let \(q=p/(p-1)\) and let \(\ell_A^p\) consist of analytic series \(f(z)=\sum_{n=0}^{\infty}a_nz^n\) on the unit disk with \(\|f\|_p^p=\sum_{n\ge0}|a_n|^p\). For finite nonzero zero constraints, define the **excess coefficient energy**
\[
C_p(W)=\min\{\|f\|_p^p-1:f\in\ell_A^p,\ f(0)=1,\ f(w)=0\ (w\in W)\}.
\]
A zero of multiplicity two at \(r\) means both \(f(r)=0\) and \(f'(r)=0\); denote its energy by \(C_p^{\rm jet}(r)\). For every \(0<r<1\), put \(C_p^{\rm one}(r)=C_p(\{r\})\) and \(C_p^{\rm opp}(r)=C_p(\{-r,r\})\). Then
\[
C_p^{\rm one}(r)=(r^{-q}-1)^{p-1},\qquad C_p^{\rm opp}(r)=(r^{-2q}-1)^{p-1},\qquad
\frac{C_p^{\rm opp}(r)}{C_p^{\rm one}(r)}=(1+r^{-q})^{p-1}.
\]
Compare the cost of two zeros to twice the cost of one (the **interaction deficit**). For \(p\ge2\), antipodal zeros strictly exceed twice the one-zero energy at every interior radius. For \(1<p<2\), the sign switches *exactly once*, at the explicit radius
\[
r_*(p)=\bigl(2^{q-1}-1\bigr)^{-1/q}:
\quad C_p^{\rm opp}(r)\begin{cases}>2C_p^{\rm one}(r),&0<r<r_*(p),\\=2C_p^{\rm one}(r),&r=r_*(p),\\<2C_p^{\rm one}(r),&r_*(p)<r<1.\end{cases}
\]
The critical radius tends to \(1/2\) as \(p\downarrow1\), and \(1-r_*(p)\sim(\log2)(2-p)\) as \(p\uparrow2\).

A colliding pair obeys a second, independently quantified version of this phase contrast. Define \(s=r^q\), let \(N_s\) have the geometric law \(\Pr(N_s=n)=(1-s)s^{n-1}\) for \(n\ge1\), and set
\[
F_q(s)=\min_{t\in\mathbb R}\mathbb E|1+tN_s|^q,\qquad
M_q=\min_{b\in\mathbb R}\int_0^\infty e^{-x}|1+bx|^q\,dx.
\]
Then the exact (not truncated) double-zero energy and its boundary ratio are
\[
C_p^{\rm jet}(r)=\left(\frac{s}{1-s}F_q(s)\right)^{1-p},\quad
\frac{C_p^{\rm jet}(r)}{C_p^{\rm one}(r)}=F_q(s)^{1-p},\quad
\lim_{r\uparrow1}\frac{C_p^{\rm jet}(r)}{C_p^{\rm one}(r)}=M_q^{1-p}.
\]
The function \(F_q:(0,1)\to(0,1)\) is **continuous and strictly increasing**. For \(p\ge2\), the double zero costs strictly more than twice the one-zero energy for every \(0<r<1\). For \(1<p<2\), there is **exactly one** jet transition radius \(r_{\rm jet}(p)\in(0,1)\), uniquely characterized by \(F_q(r_{\rm jet}(p)^q)=2^{1-q}\): below it the double-zero energy is strictly greater than twice the one-zero energy, at it equal, and above it strictly less. At \(p=2\), the two different placements have **identical energy at every radius**:
\[
C_2^{\rm jet}(r)=C_2^{\rm opp}(r)=r^{-4}-1.
\]
Moreover \(C_p^{\rm jet}(r)\sim C_p^{\rm opp}(r)\sim r^{-2p}\) as \(r\downarrow0\). If \(W_\theta=\{re^{i\theta},re^{-i\theta}\}\) with \(\theta\ne0\), then
\[
\lim_{\theta\to0} C_p(W_\theta)=C_p^{\rm jet}(r).
\]
Thus the cooperative regime for \(1<p<2\) persists for genuinely **distinct**, sufficiently close zero pairs at radii near the boundary. The sharp jet radius is given implicitly rather than by elementary functions.

## Assumptions and scope

All statements concern finite zero constraints and coefficient \(\ell^p\) norm, with strictly \(1<p<\infty\) and \(0<r<1\). The squared-norm analogy is only at \(p=2\); for general \(p\) it is important to subtract the fixed constant-term contribution \(1\) from the \(p\)-th power of the norm. The comparison with twice the one-zero energy is a benchmark for nonadditivity of distinct or repeated constraints, not an assertion that the two separate extremizing functions can be added. Rotation of a single zero does not affect its cost. All minima exist, and the normalized minimizer is unique, by reflexivity and strict convexity.

## Proof

**1. One zero and its antipode.** For a single zero, write \(f=1+\sum_{n\ge1}a_nz^n\) and impose \(\sum_{n\ge1}a_nr^n=-1\). Hölder's inequality has sharp equality, so the minimal coefficient energy equals
\[
\left(\sum_{n\ge1}r^{nq}\right)^{1-p}=
\left(\frac{r^q}{1-r^q}\right)^{1-p}.
\]
For \(f(\pm r)=0\), addition and subtraction of the constraints give \(\sum_{m\ge1}a_{2m}r^{2m}=-1\) and \(\sum_{m\ge0}a_{2m+1}r^{2m+1}=0\). The minimizing odd coefficients vanish, and another sharp Hölder application gives the second displayed cost. Their ratio has derivative strictly negative with respect to \(r\), from infinity at \(r\downarrow0\) to \(2^{p-1}\) at \(r\uparrow1\). Comparing the last limit with \(2\) gives the complete phase classification; solving equality yields \(r_*(p)\). Its endpoint asymptotics follow by taking logarithms and using \(q-2\sim2-p\) as \(p\uparrow2\).

**2. Double-zero dual problem and an extremal witness.** For \(f(r)=f'(r)=0\), the coefficient constraints become \(\sum a_nr^n=-1\) and \(\sum n a_nr^n=0\), summing over \(n\ge1\). Let
\[
Q(t)=\sum_{n\ge1}r^{nq}|1+tn|^q.
\]
The function \(Q\) is strictly convex and coercive on the real line, and has a unique minimizer \(t_*\), characterized by
\[
\sum_{n\ge1}n r^{nq}(1+t_*n)|1+t_*n|^{q-2}=0.
\]
Here the product is interpreted as zero when its factor vanishes. The coefficient vector
\[
a_n=-\frac{r^{n(q-1)}(1+t_*n)|1+t_*n|^{q-2}}{Q(t_*)}
\]
satisfies both constraints: the derivative constraint follows from stationarity and the value constraint follows from decomposing \(1=(1+t_*n)-t_*n\). Its coefficient energy is exactly \(Q(t_*)^{1-p}\). Conversely Hölder applied to the linear combination of the two constraints implies \(\sum|a_n|^p\ge Q(t_*)^{1-p}\) for every admissible vector. This proves the exact formula, including optimality and attainment. Complex coefficients cannot improve the minimum because real-part projection preserves the two real constraints and does not increase the norm.

Writing \(Q(t)=[s/(1-s)]\,\mathbb E|1+tN_s|^q\) proves the geometric-probability representation and the ratio against a single zero.

**3. Small radii.** The trial value \(t=-1\) gives \(F_q(s)\le s+O_q(s^2)\). Let \(t_s\) minimize \(F_q(s)\). Since the term for \(N_s=1\) is \((1-s)|1+t_s|^q\), this upper bound forces \(t_s\to-1\). The term for \(N_s=2\) then gives \(F_q(s)\ge (1-s)s|1+2t_s|^q=s(1+o(1))\). Thus \(F_q(s)\sim s\), and both two-zero energies are asymptotic to \(r^{-2p}\). In particular, the double-zero-to-single ratio tends to infinity as \(r\downarrow0\).

**4. Strict increase and uniqueness of the jet crossover.** Set \(Y_s=(1-s)N_s\), whose mean equals one, and write \(g_s(b)=\mathbb E|1+bY_s|^q\). For fixed \(u\ge0\), with \(m=\lfloor u/(1-s)\rfloor\), the geometric memoryless property gives the **exact stop-loss transform**
\[
\mathbb E(Y_s-u)_+=s^m\bigl(1-u+m(1-s)\bigr).
\]
Within each interval on which \(m\) is fixed, its derivative in \(s\) is
\[
m s^{m-1}\bigl((m+1)(1-s)-u\bigr)\ge0.
\]
At the moving integer thresholds the stop-loss transform is continuous, so for every \(u\ge0\) it is nondecreasing with \(s\), and it is strictly increasing for every fixed \(u>1-s_1\) as \(s\) moves from \(s_1\) to a larger value. For every \(b\ne0\), the function \(y\mapsto|1+by|^q\) is strictly convex and has positive second derivative almost everywhere on \(y>0\). The integral representation of convex expectations by the stop-loss transform (or integration twice by parts, with moment truncation) therefore gives \(g_{s_2}(b)>g_{s_1}(b)\) for \(s_2>s_1\). The minimizer \(b_s\) of \(g_s\) is nonzero, since \(g_s'(0)=q>0\). Using \(b_{s_2}\) as a trial coefficient at \(s_1\) proves
\[
F_q(s_1)\le g_{s_1}(b_{s_2})<g_{s_2}(b_{s_2})=F_q(s_2).
\]
Continuity follows from convergence of the geometric moments on compact subintervals and coercivity, so \(F_q\) is continuous and strictly increasing. In particular, if its endpoint limit exceeds the interaction threshold, there can be **only one** crossover.

**5. The critical exponent and the boundary.** The exact quadratic minimum for \(N_s\) is
\[
F_2(s)=1-\frac{(\mathbb EN_s)^2}{\mathbb EN_s^2}=\frac{s}{1+s}.
\]
For \(1<q<2\), the monotonicity of probability \(L^u\)-norms implies
\[
F_q(s)\le F_2(s)^{q/2}<2^{-q/2}<2^{1-q}.
\]
Since the exponent \(1-p\) is negative, this proves \(C_p^{\rm jet}(r)>2C_p^{\rm one}(r)\) for \(p>2\). For \(q=2\) the equality in the quadratic formula yields the explicit common double-zero and antipodal cost.

For \(q>2\), the reverse comparison gives
\[
F_q(s)\ge F_2(s)^{q/2}.
\]
As \(s\uparrow1\) the right-hand side tends to \(2^{-q/2}>2^{1-q}\), so sufficiently close to the boundary \(F_q(s)>2^{1-q}\) and consequently \(C_p^{\rm jet}(r)<2C_p^{\rm one}(r)\). The small-radius asymptotic gives the opposite strict inequality there. Strict monotonicity and continuity from Step 4 now imply the unique transition \(r_{\rm jet}(p)\) and the asserted complete sign classification.

For the exact boundary constant, put \(Y_s=(1-s)N_s\). Its law converges weakly to a mean-one exponential random variable, and all fixed positive moments converge. Writing \(t=b(1-s)\) changes the objective to \(\mathbb E|1+bY_s|^q\). A minimizing \(b_s\) is bounded uniformly as \(s\uparrow1\): by Minkowski, \(\|1+b_sY_s\|_q\ge|b_s|\|Y_s\|_q-1\), while the minimum is at most one and \(\|Y_s\|_q\) stays bounded away from zero. The objectives converge uniformly for \(b\) on compact sets by moment convergence and uniform integrability. Therefore their minima tend to \(M_q\), proving the boundary formula. At \(q=2\), \(M_2=1/2\); at \(q<2\) the bound above gives \(M_q<2^{1-q}\), whereas at \(q>2\) the reverse bound gives \(M_q>2^{1-q}\). The signs of the limiting interaction ratios follow.

**6. Confluence of distinct zeros.** With \(\theta\ne0\) small, the constraints \(f(re^{i\theta})=f(re^{-i\theta})=0\) are equivalent to
\[
\sum_{n\ge1}a_n r^n\cos(n\theta)=-1,\qquad
\sum_{n\ge1}a_n r^n\frac{\sin(n\theta)}{\sin\theta}=0.
\]
Call the two real coefficient vectors \(A_\theta,B_\theta\). They converge in \(\ell^q\), respectively to \(A_0=(r^n)_{n\ge1}\) and \(B_0=(nr^n)_{n\ge1}\): dominated convergence applies since \(|\sin(n\theta)/\sin\theta|\le n\) for small nonzero real \(\theta\). Put \(D_\theta=\min_{t\in\mathbb R}\|A_\theta+tB_\theta\|_q\). The two limiting vectors are linearly independent, as are the perturbed vectors for sufficiently small \(|\theta|\) (their first two coordinates already distinguish them). By the same stationarity and Hölder argument as in Step 2, now with \(A_\theta,B_\theta\) in place of \((r^n),(nr^n)\), the minimum coefficient energy is \((D_\theta^q)^{1-p}=D_\theta^{-p}\). In particular, at a minimizing \(t\), the vector with entries \(-|w_n|^{q-2}w_n/D_\theta^q\), \(w=A_\theta+tB_\theta\), satisfies both constraints. The minimizing multipliers satisfy \(|t|\|B_\theta\|_q\le 2\|A_\theta\|_q\) and are uniformly bounded near zero. The norm objectives therefore converge uniformly on an interval containing their minimizers, giving \(D_\theta\to D_0>0\). Taking the power \(-p\) proves the confluence law and openness of the strict cooperative and repulsive regimes for sufficiently close distinct pairs.

## Verification

A standalone `CHECK.py` computes exact finite-dimensional dual norms and truncation approximations, checks the analytic \(p=2\) identity, verifies the antipodal phase threshold on both sides of the critical radius, and compares small- and large-radius dual ratios for exponents on either side of two. These checks are finite consistency tests, not substitutes for the preceding infinite-series and weak-convergence arguments. Every displayed infinite identity is justified by Hölder duality, geometric-series summation, or dominated/uniform-integrability convergence as appropriate.

## Relationship to prior work

Abakumov, Chalendar and Poltoratski (arXiv:2611.02159, first public November 1, 2026), especially Theorem 3.1 and Section 4, prove a general sharp moment-duality criterion and regular-polygon zero-set criteria. The exact one-zero and antipodal calculations and the explicit antipodal transition are elementary consequences of sharp Hölder duality and are presented here as benchmarks. The distinct result is the all-radius repeated-zero phase classification: strict monotonicity of the normalized geometric affine-loss minimum gives a unique coalescent threshold, the exponential boundary problem gives the limiting ratio, and continuity transfers strict signs to genuinely distinct nearby zeros. Neither abstract finite-zero duality nor a new infinite zero-set criterion is claimed.

Cheng, Mashreghi and Ross (arXiv:1802.04646, 2018/2019), especially Sections 1, 6 and 7, construct the general finite-zero extremal framework and allow repeated zeros; again this structural existence is prior art. Cheng, Ross and Seco (arXiv:2104.08014, 2021/2022) investigate zeros of optimal polynomial approximants and a distinct optimal-approximant radius, not the present two-prescribed-zero energy comparison. The present formulas are elementary consequences of duality plus a separate quantitative analysis; claiming independent origin of the dual method would be inaccurate.

## Limitations

This is a finite-constraint interaction theorem, not a characterization of infinite zero sets, and the unique **coalescent** transition radius when \(1<p<2\) is implicit rather than in an elementary closed form. The boundary constant \(M_q\) is given by a one-dimensional variational integral, not a closed elementary evaluation except in the Hilbert case. The exact antipodal threshold is a comparatively direct use of existing moment-duality machinery; its possible appearance in an earlier worked example remains an originality risk. Numerical verification cannot prove universal inequalities. Publication priority requires independent literature review.

## References

1. E. Abakumov, I. Chalendar, A. Poltoratski, *Zero sets in spaces of analytic functions with p-summable Taylor coefficients*, arXiv:2611.02159v1 (submitted November 1, 2026), https://arxiv.org/abs/2611.02159 .
2. R. Cheng, J. Mashreghi, W. T. Ross, *Inner functions and zero sets for \(\ell_A^p\)*, arXiv:1802.04646 (2018), Trans. Amer. Math. Soc. 372 (2019), 2045–2072, https://arxiv.org/abs/1802.04646 .
3. R. Cheng, W. T. Ross, D. Seco, *Zeros of optimal polynomial approximants in \(\ell_A^p\)*, arXiv:2104.08014 (2021), Advances in Mathematics (2022), https://arxiv.org/abs/2104.08014 .
