# Complete subsequential histogram laws for Lyapunov-irregular wandering orbits

## Finding

For the wandering rectangles in the Nakano–Soma–Yamamoto piecewise-expanding planar construction, the full family of subsequential **time-histogram laws** of the finite-time Lyapunov rate is explicit. This is stronger information than the already-known interval of accumulation values of the rate itself.

Fix an integer \(\gamma\geq2\) allowed by the construction, and put
\[
 c=\frac1{\gamma+1},\qquad d=\frac1{\gamma-1},\qquad s=\frac{\gamma-1}{\gamma+1},\qquad
 h(u)=\frac{|u-c|}{u+d}\quad(0\leq u\leq1).
\]
Choose a regular point \(x\) of a wandering rectangle \(R(0,m)\) and a tangent vector \(v=\alpha e_1+\beta e_2\) with \(\alpha\beta\ne0\). With \(a=\log\lambda_1>b=\log\lambda_2>0\), define the normalized finite-time exponent and its empirical distribution by
\[
 Z_n=\frac{2}{a-b}\left(\frac1n\log\|DF^n(x)v\|-\frac{a+b}{2}\right),
 \qquad \nu_N=\frac1N\sum_{n=1}^N\delta_{Z_n}.
\]
Here \(\lambda_1,\lambda_2\), the differentiability order, the allowed integer \(\gamma\), and \(m\) are the parameters fixed by the published construction; the theorem is **not** asserting the existence of this map for arbitrary independent parameter choices.

Let \(\ell_j=\gamma^{m+j}\), \(B_j=\sum_{i=0}^{j-1}\ell_i\) and \(N_j(\theta)=B_j+\lfloor\theta\ell_j\rfloor\), for \(\theta\in[0,1]\). Then, for every fixed \(\theta\),
\[
 \nu_{N_j(\theta)}\ \Longrightarrow\
 \mu_\theta:=\frac{d\,h_\#\operatorname{Leb}_{[0,1]}+
       \int_0^\theta\delta_{h(u)}\,du}{d+\theta}.
\]
The complete set of weak subsequential limits of \((\nu_N)\) is **exactly** \(\{\mu_\theta:0\leq\theta\leq1\}\). In particular the empirical histogram does not converge, although \(\mu_0=\mu_1\).

At completed geometric blocks the common limiting cumulative distribution function \(G\) is
\[
 G(t)=\begin{cases}
 0,&t<0,\\
 \displaystyle\frac{4\gamma t}{(\gamma^2-1)(1-t^2)},&0\leq t\leq s,\\
 1,&t\geq s.
 \end{cases}
\]
At an intra-block cutoff with \(\theta=c\), the limiting cumulative distribution function is
\[
 G_c(t)=\frac{dG(t)+t(c+d)/(1+t)}{d+c},\qquad 0\leq t\leq s,
\]
and for \(0<t<s\) one has the **strict** difference
\[
 G_c(t)-G(t)=\frac{t(s-t)}{1-t^2}>0.
\]
For example, at \(\gamma=3\) and \(t=1/4\), the two distribution functions take the distinct values \(2/5\) and \(7/15\).

## Assumptions and scope

We use the concrete one-parameter family of piecewise \(C^r\) expanding maps in [1], Section 2, with integer \(r\geq1\), integer \(\gamma>r\), and the restrictions on \(\lambda_1,\lambda_2\) and small parameters imposed in that paper. Let \(m>M\) be any permitted index and \(x\in R(0,m)'\), the full-Lebesgue-measure subset whose forward orbit avoids all branch boundaries, defined in [1], Section 3.1. Such points form a positive-Lebesgue-measure set. The theorem holds for every such \(x\) and every fixed nonzero \(v\) with both coordinate components nonzero. All norms are the standard Euclidean norm. \(h_\#\operatorname{Leb}\) is the pushforward of **probability** Lebesgue measure on \([0,1]\).

An empirical histogram of the *successive finite-time exponents*, not the orbit's physical-space empirical measure and not the distribution over random initial conditions, is being considered. Convergence is weak convergence of probability measures on \(\mathbb R\). \(\theta\) denotes a cutoff fraction inside a growing symbolic block; \(\mu_1=\mu_0\) identifies the two adjacent block-end representations.

## Proof

**1. Exact signed block-length bookkeeping.** The diagonal evolution on the wandering rectangles and coordinate interchanges at block boundaries are given by [1], (2.4), (3.1) and the derivative identity (3.2). Along successive blocks of lengths \(\ell_0,\ell_1,\ldots\), one original input component receives \(\lambda_1\) on the even blocks and \(\lambda_2\) on the odd blocks; the other receives the opposite factors. Coordinate interchanges do not change the Euclidean norm. Thus for \(0\leq t\leq\ell_j\), writing \(n=B_j+t\), we have
\[
 q_n=\sum_{i=0}^{j-1}(-1)^i\ell_i+(-1)^jt
    =\gamma^m\frac{1-(-\gamma)^j}{\gamma+1}+(-1)^jt.
\]
The norm is exactly
\[
 \|DF^n(x)v\|^2=e^{n(a+b)}\left(\alpha^2e^{(a-b)q_n}+\beta^2e^{-(a-b)q_n}\right).
\]
Any boundary convention that puts the final coordinate swap one index earlier changes only the direction of the output basis, not this norm. Since \(\alpha\beta\ne0\), the expression in parentheses is between \(e^{(a-b)|q_n|}\min(\alpha^2,\beta^2)\) and \(e^{(a-b)|q_n|}(\alpha^2+\beta^2)\). Hence, with a constant depending only on \(v,\lambda_1,\lambda_2\),
\[
 \left|Z_n-\frac{|q_n|}{n}\right|\leq\frac{C_v}{n}\quad(n\geq1).
\]
In particular, replacing \(Z_n\) by \(|q_n|/n\) does not change any weak subsequential limit of its time histograms.

**2. A universal profile on every large block.** The geometric series gives
\[
 \frac{B_j}{\ell_j}=\frac{1-\gamma^{-j}}{\gamma-1}\longrightarrow d,
 \quad \frac{q_{B_j}}{(-1)^j\ell_j}=\frac{\gamma^{-j}(-1)^j-1}{\gamma+1}\longrightarrow-c.
\]
For \(u\in[0,1]\), the ratio \(|q_{B_j+\lfloor u\ell_j\rfloor}|/(B_j+\lfloor u\ell_j\rfloor)\) therefore converges **uniformly in \(u\)** to \(h(u)=|u-c|/(u+d)\) as \(j\to\infty\). The denominator is uniformly bounded away from zero in these normalized coordinates, since \(d>0\). Together with the preceding \(O(1/n)\) estimate this also proves uniform convergence of the normalized finite-time exponents on each high-index block.

**3. Whole-block and partial-block histograms.** Let \(\psi\) be any bounded continuous test function. Uniform convergence from Step 2 and the fact that the integer mesh on each block tends to zero imply
\[
 \frac1{\ell_j}\sum_{n=B_j+1}^{B_j+\ell_j}\psi(Z_n)
   \longrightarrow\int_0^1\psi(h(u))\,du,
\]
and the same holds for sums stopped at \(\lfloor\theta\ell_j\rfloor\), with limiting integral from \(0\) to \(\theta\). Removing finitely many initial blocks loses negligible relative mass; every remaining prior block has the same limiting distribution. Since \(B_j/\ell_j\to d\), the weighted preceding-block contribution has mass \(d/(d+\theta)\), and the incomplete current block has mass \(\theta/(d+\theta)\). Division by \(N_j(\theta)/\ell_j\to d+\theta\) gives \(\mu_\theta\) as claimed.

Given an arbitrary sequence of cutoffs \(N_k\to\infty\), choose the unique \(j_k\) with \(B_{j_k}\leq N_k<B_{j_k+1}\). The fractions \(\theta_k=(N_k-B_{j_k})/\ell_{j_k}\) belong to the compact interval \([0,1]\), so every subsequence has a further subsequence with \(\theta_k\to\theta\). The same uniform block proof gives the limiting measure \(\mu_\theta\). Conversely \(N_j(\theta)\) realizes each \(\mu_\theta\). This proves the claimed **complete** cluster family. Note \(d+1=\gamma d\) and \(\mu_1=\mu_0=h_\#\operatorname{Leb}_{[0,1]}\).

**4. Closed distribution functions and nonconvergence.** The range of \(h\) is exactly \([0,s]\). For \(0\leq t\leq s\), solve \(h(u)\leq t\):
\[
 L_t:=\frac{c-td}{1+t}\leq u\leq
 U_t:=\frac{c+td}{1-t},\qquad 0\leq L_t\leq U_t\leq1.
\]
Consequently \(G(t)=U_t-L_t=4\gamma t/[(\gamma^2-1)(1-t^2)]\). More generally the entire cutoff family has explicit CDF
\[
 G_\theta(t)=\frac{dG(t)+
 \bigl[\min\{\theta,U_t\}-\max\{0,L_t\}\bigr]_+}{d+\theta}
 \quad(0\leq t\leq s),
\]
with values \(0\) and \(1\) outside \([0,s]\); here \([z]_+=\max\{z,0\}\). For \(\theta=c\), the interval \([L_t,U_t]\cap[0,c]\) has length \(c-L_t=t(c+d)/(1+t)\), yielding the stated \(G_c\). Algebra reduces its difference from \(G\) to \(t(s-t)/(1-t^2)\), which is positive for each interior \(t\). Since \(\mu_c\ne\mu_0\), no unique weak limit exists. This completes the proof.

## Verification

The accompanying standalone `check.py` verifies exact geometric signed sums, the uniform-exponent comparison for finite blocks using stable logarithmic computations, rational CDF identities and the strict mid-block separation for several admissible integers. It also directly counts time samples through a large finite \(\gamma=3\) block and checks agreement with the distinct predicted values \(2/5\) and \(7/15\). Finite tests illustrate the formulas; **the proof above establishes the infinite weak-limit classification**.

Run `python3 check.py` from the extracted files. No external dependencies are required.

## Relationship to prior work

Nakano, Soma and Yamamoto [1] construct the positive-area Lyapunov-irregular wandering rectangles and prove the **pointwise accumulation interval** for their finite-time exponent (Theorem 3.1). Their equations (2.4), (3.1) and (3.2) supply the derivative bookkeeping used in Step 1 above, which is credited rather than asserted as a new result. The new statement concerns the whole family of **empirical distributions sampled over observation times**, including its rational CDF and exact description of all subsequential probability laws. In particular, an accumulation interval alone does not determine sampling frequencies or their nonconvergence.

Jordan, Naudot and Young [2] study higher-order averages of nonconvergent Birkhoff averages. That notion differs from the weak empirical distribution of successive finite-time Lyapunov rates in this particular geometric-block model.

## Limitations

The statement is specific to the indicated Nakano–Soma–Yamamoto wandering rectangles, their permitted parameters, and directions with both nonzero components; it makes no claim about arbitrary expanding maps or coordinate-axis directions. No invariant sampling measure is posited on the wandering set, and the time histograms \(\nu_N\) should not be confused with physical-space orbit measures. The new classification is a direct analysis of known derivative formulas, not an independent construction of the maps. Equivalent deductions in literature not inspected remain a priority risk. Independent mathematical audit and publication-priority verification have not been performed.

## References

[1] Y. Nakano, T. Soma and K. Yamamoto, *Observable Lyapunov irregular sets for planar piecewise expanding maps*, arXiv:2206.09508v1 (first public version June 19, 2022), Sections 2.2–3.2, especially (2.4), (3.1), (3.2), Theorem 3.1. https://arxiv.org/abs/2206.09508

[2] T. Jordan, V. Naudot and T. Young, *Higher Order Birkhoff Averages*, arXiv:0806.3060 (2008), published in *Dynamical Systems* 24 (2009), 299–313. https://arxiv.org/abs/0806.3060
