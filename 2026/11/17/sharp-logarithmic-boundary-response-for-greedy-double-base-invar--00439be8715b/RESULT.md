# Sharp logarithmic boundary response for greedy double-base invariant measures

## Finding
For each fixed real \(B>1\), the physical invariant probability of the greedy double-base map has a non-Lipschitz but sharply quantified response when its zero-digit base approaches the full-branch boundary. Define \(M=1/(B-1)\), \(q_\varepsilon=B/(B-1)-\varepsilon\), and \(\mu_\varepsilon\) as in the following section. Put
\[
C_B=\frac{(B-1)^2}{B^2\log B}>0.
\]
Then, in the dual space of continuous functions on \([0,M]\),
\[
\boxed{\frac{\mu_\varepsilon-\mu_0}{\varepsilon\log(1/\varepsilon)}\ \xrightarrow[\varepsilon\downarrow0]{\mathrm{weak}^*}\ C_B(\mu_0-\delta_M).}
\]
The same leading coefficient determines the **sharp total-variation response**:
\[
\boxed{\|h_\varepsilon-h_0\|_{L^1([0,M])}=2C_B\varepsilon\log(1/\varepsilon)+o(\varepsilon\log(1/\varepsilon)).}
\]
Thus the total-variation distance between the two probabilities, defined as one half of that norm, is asymptotic to \(C_B\varepsilon\log(1/\varepsilon)\). For the coordinate observable, the sharp one-sided law is
\[
\int x\,d\mu_\varepsilon=\frac M2-\frac{B-1}{2B^2\log B}\varepsilon\log(1/\varepsilon)+o(\varepsilon\log(1/\varepsilon)).
\]
These statements apply to every fixed \(B>1\), without arithmetic restrictions on \(B\).

## Assumptions and scope
Fix \(B>1\) once and for all; all error constants may depend on \(B\), and none is asserted uniformly as \(B\downarrow1\) or \(B\to\infty\). For \(0\le\varepsilon<B/(B-1)-1\), put \(q_\varepsilon=B/(B-1)-\varepsilon>1\). On the compact interval \(I=[0,M]\), where \(M=(B-1)^-1\), define
\[
G_\varepsilon(x)=\begin{cases}q_\varepsilon x,&0\le x<1/B,\\Bx-1,&1/B\le x\le M.\end{cases}
\]
The source's existence, exactness, and step-density theorem supplies a unique absolutely continuous invariant probability \(\mu_\varepsilon\) with density \(h_\varepsilon\). Uniqueness here is *within absolutely continuous invariant probabilities*: endpoint atomic invariant measures need not be unique. At \(\varepsilon=0\), both branches are full, so \(\mu_0(dx)=dx/M\). All limits are from \(\varepsilon>0\) toward zero; pointwise values of the map at branch boundaries do not change the absolutely continuous law.

For a finite signed measure \(\eta\), \(\|\eta\|_{\mathrm{TV,norm}}\) means the total mass of its variation measure, not half of it. We use this norm to avoid ambiguity in the distinction between \(L^1\) norm and probability total-variation distance.

## Proof
**Step 1. The exact invariant step series.** Set \(r_\varepsilon=q_\varepsilon/B=M-\varepsilon/B\), \(x_0=r_\varepsilon\), \(x_n=G_\varepsilon^n(r_\varepsilon)\), and \(d_n=\mathbf 1_{[1/B,M]}(x_n)\). Define \(w_0=1\) and
\[
w_{n+1}=\frac{w_n}{q_\varepsilon}\quad(d_n=0),\qquad w_{n+1}=\frac{w_n}{B}\quad(d_n=1).
\]
The source's Parry-type formula gives the non-normalized finite measure
\[
\nu_\varepsilon(dx)=f_\varepsilon(x)\,dx,\quad
f_\varepsilon(x)=\sum_{n\ge0}w_n\mathbf1_{[0,x_n]}(x),\quad
Z_\varepsilon=\nu_\varepsilon(I)=\sum_{n\ge0}w_nx_n,\quad
\mu_\varepsilon=\nu_\varepsilon/Z_\varepsilon.
\]
The series converges absolutely since \(w_n\le\min(B,q_\varepsilon)^{-n}\) and \(0\le x_n\le M\). For clarity, it is also possible to check its invariance directly: the Frobenius–Perron image of the weighted \(n\)-th step is \(w_{n+1}\mathbf1_{[0,x_{n+1}]}+\mathbf1_{\{d_n=1\}}w_nq_\varepsilon^{-1}\mathbf1_{[0,r_\varepsilon]}\). The telescoping digit identity \(r_\varepsilon=\sum_{d_n=1}w_{n+1}\) yields \(\sum_{d_n=1}w_n/q_\varepsilon=Br_\varepsilon/q_\varepsilon=1\), proving \(P_\varepsilon f_\varepsilon=f_\varepsilon\). At the boundary \(x_n=M\), \(w_n=B^{-n}\), hence
\[
\nu_0(dx)=\frac B{B-1}\,dx,\qquad Z_0=\frac B{(B-1)^2},\qquad\mu_0(dx)=\frac {dx}{M}.
\]

**Step 2. An exactly quantifiable long critical prefix.** For sufficiently small \(\varepsilon>0\), let \(L=L_\varepsilon\) be the first \(n\ge0\) for which \(x_n<1/B\). Until this first exit the orbit uses only the right branch, so for all \(0\le n\le L\),
\[
x_n=M-\varepsilon B^{n-1},\qquad w_n=B^{-n}.
\]
The inequalities \(x_{L-1}\ge1/B\) and \(x_L<1/B\) imply
\[
\frac MB<\varepsilon B^{L-1}\le M.
\]
Consequently
\[
L=\frac{\log(1/\varepsilon)}{\log B}+O_B(1),\qquad B^{-L}=\Theta_B(\varepsilon).
\]
For every index \(n\le L\), the weighted mass missing from the boundary interval relative to the unperturbed step is **exactly**
\[
\int_{x_n}^M B^{-n}dx=B^{-n}(M-x_n)=\frac\varepsilon B.
\]

**Step 3. Decomposition and weak limit.** Put
\[
D_\varepsilon(dx)=\sum_{n=0}^L B^{-n}\mathbf1_{(x_n,M]}(x)\,dx,\qquad m_\varepsilon=D_\varepsilon(I)=\frac{(L+1)\varepsilon}B.
\]
Separate the first \(L+1\) terms from the infinite step series to obtain
\[
\nu_\varepsilon-\nu_0=-D_\varepsilon+R_\varepsilon,\qquad
\|R_\varepsilon\|_{\mathrm{TV,norm}}=O_B(\varepsilon).
\]
Indeed, after the first left visit, \(\sum_{n>L}w_n\le B^{-L}\sum_{j\ge1}\sigma^{-j}=O_B(\varepsilon)\), with \(\sigma>1\) a uniform lower bound for \(q_\varepsilon\) and \(B\); the unperturbed geometric tail has the same order. The missing-mass scale satisfies
\[
\frac{m_\varepsilon}{\varepsilon\log(1/\varepsilon)}\longrightarrow\frac1{B\log B}.
\]
For any fixed \(\delta>0\), the number of prefix indices with \(M-x_n>\delta\) is at most a constant depending on \(B,\delta\), because \(M-x_n=\varepsilon B^{n-1}\) and \(L=\log_B(1/\varepsilon)+O_B(1)\). Each such index contributes exactly \(\varepsilon/B\) mass. It follows that
\[
\frac{D_\varepsilon}{m_\varepsilon}\ \xrightarrow{\mathrm{weak}^*}\ \delta_M.
\]
Since \(Z_\varepsilon=Z_0-m_\varepsilon+O_B(\varepsilon)\), normalization gives
\[
\mu_\varepsilon-\mu_0
=\frac{m_\varepsilon}{Z_0}\mu_0-\frac1{Z_0}D_\varepsilon+O_{\mathrm{TV,norm}}(\varepsilon+m_\varepsilon^2).
\]
The preceding two limits and \(1/(B Z_0\log B)=(B-1)^2/(B^2\log B)=C_B\) prove the asserted signed weak-* limit.

**Step 4. Sharp \(L^1\) size.** Taking the variation norm of the same decomposition gives the upper bound
\[
\limsup_{\varepsilon\downarrow0}\frac{\|\mu_\varepsilon-\mu_0\|_{\mathrm{TV,norm}}}{\varepsilon\log(1/\varepsilon)}\le2C_B.
\]
The variation norm of signed finite measures on a compact interval is lower semicontinuous for weak-* convergence, by its dual characterization as a supremum over continuous functions of sup-norm at most one. The limiting signed measure is \(C_B(\mu_0-\delta_M)\); because \(\mu_0\) has no atom at \(M\), this has variation norm exactly \(2C_B\). Thus the matching lower bound holds, proving the sharp \(L^1\) equivalence. Applying the weak limit to the continuous function \(x\mapsto x\) gives the displayed mean expansion, since \(\int x\,d\mu_0=M/2\), whereas \(\int x\,d\delta_M=M\). Its nonzero coefficient excludes any finite one-sided derivative against this observable.

## Verification
The standalone script `verify.py` computes the invariant series directly, numerically integrates the normalized step density exactly on each finite partition cell using high-precision decimal arithmetic, and checks the prefix identities and leading mean and \(L^1\) ratios for four fixed bases and three perturbation scales. Execute `python verify.py` using Python 3.10 or later; no additional packages are required. The code uses a truncated invariant series. Its finite checks corroborate but do not replace the analytical bounds on the omitted tail, the weak limit, or the infinite-parameter quantifiers.

## Relationship to prior work
Huang, Komorni and Zou (2026), Theorems 1.1–1.3, prove existence, exactness and the invariant step density for greedy double-base dynamics. The present result **assumes and explicitly credits that density formula**; its new target is the sharp parameter-response limit, including the signed endpoint concentration and the exact total-variation coefficient. Keller, Howard and Klages (2008) prove general logarithmic-modulus stability bounds for expanding maps and discuss sharpness in different piecewise-linear families; a modulus bound does not determine this family's signed limiting measure or leading coefficient. A separate 2026 treatment, *Exactly two Markov loci for greedy double-base digit dynamics*, classifies first-order Markov digit laws, rather than response of physical invariant measures to approach to the full-branch line. Those results are compatible and do not state the present sharp asymptotic. Earlier general invariant-density representations could potentially yield a specialization, so novelty is assessed only against the specifically inspected claims, not guaranteed against all literature.

## Limitations
All asymptotics fix \(B>1\). There is no asserted uniformity in a simultaneous limit of the two bases, nor a response theorem away from the one-sided full-branch boundary. The signed weak limit is not total-variation convergence of the rescaled signed measures: it has an atom and each approximating signed measure is absolutely continuous. A general first-order logarithmic stability bound was previously known; novelty is the exact signed-measure limit and sharp constant for the specified family. This is a mathematical result, not an independent external certification or an empirically tested model.

## References
1. W. Huang, V. Komorni and Y. Zou, *Invariant measure for double base expansions*, arXiv:2605.08641 (first posted 2026-05-09), https://arxiv.org/abs/2605.08641. Relevant: Theorems 1.1–1.3 and the definition of the greedy map.
2. G. Keller, P. J. Howard and R. Klages, *Continuity properties of transport coefficients in simple maps*, arXiv:0801.2413 (first posted 2008-01-16), https://arxiv.org/abs/0801.2413. Relevant: Lemma 1 and Remark 1, concerning logarithmic continuity of stationary densities.
3. P. Góra, *Invariant densities for generalized beta maps*, *Ergodic Theory Dynam. Systems* (2007). Relevant general density-formula context; only the accessible abstract was compared.
4. *Exactly two Markov loci for greedy double-base digit dynamics* (public research record, 2026-10-26). Relevant: digit-process Markov classification, not parameter-response asymptotics.
