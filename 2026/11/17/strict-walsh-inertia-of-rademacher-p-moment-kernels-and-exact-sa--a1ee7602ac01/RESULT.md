# Strict Walsh inertia of Rademacher \(p\)-moment kernels and exact sampling rigidity

## Finding
Let \(n\ge2\) be an integer and \(0<p<2\). On the antipodal Boolean group
\[
G_n=\{-1,1\}^n/\{\pm\mathbf1\},\qquad |G_n|=2^{n-1},
\]
consider the symmetric absolute-moment matrix
\[
K_{n,p}([x],[y])=\left|\sum_{i=1}^{n}x_i y_i\right|^p.
\]
For every \(0\le k\le\lfloor n/2\rfloor\), the even Walsh characters \(\chi_S([x])=\prod_{i\in S}x_i\), with \(|S|=2k\), are eigenvectors with eigenvalue
\[
\lambda_{2k}(n,p)=\frac12\sum_{a=0}^{2k}\sum_{b=0}^{n-2k}(-1)^a\binom{2k}{a}\binom{n-2k}{b}|n-2a-2b|^p.
\]
Each eigenvalue has multiplicity \(\binom n{2k}\), including coincident eigenvalues counted by characters. The constant level is positive, and every nonconstant level has the **strict** sign rule
\[
\lambda_0(n,p)>0,\qquad \operatorname{sgn}\lambda_{2k}(n,p)=(-1)^{k+1}\quad(k\ge1).
\]
In particular, \(K_{n,p}\) is nonsingular, and its exact positive, negative, and zero inertia is
\[
\left(1+\sum_{\substack{k\ge1\ \mathrm{odd}\\2k\le n}}\binom n{2k},\ \sum_{\substack{k\ge2\ \mathrm{even}\\2k\le n}}\binom n{2k},\ 0\right).
\]
The sign pattern does not depend on \(p\) within the open interval \((0,2)\). For comparison, at \(p=2\) the eigenvalues are \(n2^{n-1}\) for the constant character, \(2^n\) for degree two, and zero for all even degrees at least four. Hence the rank at the quadratic endpoint is \(1+\binom n2\).

There is a sharp exact-discretization consequence. Let real weights \(w_x\) be assigned to finitely many sign vectors \(x\in\{-1,1\}^n\), with repetitions combined. If
\[
\sum_x w_x\left|\sum_{i=1}^n a_i x_i\right|^p
=2^{-n}\sum_{\epsilon\in\{-1,1\}^n}\left|\sum_{i=1}^n a_i\epsilon_i\right|^p
\quad\text{for every }a\in\mathbb R^n,
\]
then the sum of the weights of the two signs in each antipodal pair is exactly \(2^{1-n}\). This remains true without assuming nonnegativity of the weights. Consequently at least \(2^{n-1}\) distinct antipodal pairs must be sampled; this is attained by selecting one sign from each pair with equal weight.

## Assumptions and scope
The coefficient field is real, the sign space is uniformly distributed, and sample nodes in the exactness statement are constrained to original sign outcomes. No statement is made about complex coefficient vectors, arbitrary external nodes, or approximate quadrature. The power satisfies \(0<p<2\), with the endpoint \(p=2\) treated separately. The primary classification is MSC2020 \(46B09\), probabilistic methods in Banach-space theory.

## Proof
**1. Antipodal Walsh diagonalization.** The quotient \(G_n\) is an elementary abelian two-group. Exactly the Walsh characters indexed by even subsets \(S\subseteq\{1,\ldots,n\}\) descend to \(G_n\); they form an orthogonal basis of all real functions on \(G_n\). The kernel depends only on the group product, so convolution sends each character to a scalar multiple of itself. For a subset of size \(2k\), counting negative coordinates inside and outside \(S\) yields the finite binomial formula in the finding. The multiplicity is \(\binom n{2k}\).

**2. A positive fractional-cosine representation.** For \(0<p<2\) there exists a constant \(c_p>0\) such that for all real \(s\),
\[
|s|^p=c_p\int_0^\infty\frac{1-\cos(ts)}{t^{1+p}}\,dt.
\]
Fix an even subset \(S\) of size \(2k\ge2\), and put \(m=n-2k\). Independence of the fair signs gives
\[
2^{-n}\sum_{\epsilon}\chi_S(\epsilon)\cos\left(t\sum_i\epsilon_i\right)
=(-1)^k(\sin t)^{2k}(\cos t)^m.
\]
The weighted character sum of the constant function vanishes. Passing from the full sign cube to antipodal classes therefore gives
\[
\lambda_{2k}(n,p)=2^{n-1}c_p(-1)^{k+1}I_{k,m}(p),\qquad
I_{k,m}(p)=\int_0^\infty\frac{(\sin t)^{2k}(\cos t)^m}{t^{1+p}}\,dt.
\]
Absolute convergence follows from the bound \((\sin t)^{2k}=O(t^{2k})\) at zero and from the integrable weight at infinity. Because \(2k\ge2>p\), the integral is well-defined.

**3. The crucial strict-sign lemma.** For every integer \(k\ge1\), every integer \(m\ge0\), and every \(0<p<2\), the integral \(I_{k,m}(p)\) is strictly positive. If \(m\) is even, the integrand is nonnegative and positive on a set of positive measure. If \(m\) is odd, put \(F(u)=(\sin u)^{2k}(\cos u)^m\). Then \(F(u+\pi)=-F(u)\), \(F(\pi-u)=-F(u)\), and \(F(u)>0\) when \(0<u<\pi/2\). For \(j\ge0\), define
\[
h_j(u)=(u+2j\pi)^{-1-p}-(u+(2j+1)\pi)^{-1-p}\quad(0<u<\pi).
\]
Since \(t\mapsto t^{-1-p}\) is strictly decreasing and strictly convex, \(h_j(u)>0\) and is strictly decreasing. Pairing consecutive intervals of length \(\pi\), and then pairing \(u\) with \(\pi-u\), gives
\[
\begin{aligned}
\int_{2j\pi}^{(2j+2)\pi}\frac{F(t)}{t^{1+p}}\,dt
&=\int_0^\pi F(u)h_j(u)\,du\\
&=\int_0^{\pi/2}F(u)[h_j(u)-h_j(\pi-u)]\,du>0.
\end{aligned}
\]
This holds also for \(j=0\), because the singularity at zero is integrable after multiplication by \(F\). Summing the positive paired integrals proves the lemma. Therefore each \(\lambda_{2k}\) has the asserted strict sign. The constant eigenvalue is the row sum of a nonnegative matrix with positive diagonal; hence \(\lambda_0>0\). Orthogonality of the Walsh basis gives the exact inertia and nonsingularity.

**4. Exact sampling rigidity.** Let \(\omega_{[x]}=w_x+w_{-x}\), interpreting missing sign outcomes as zero weights. Evaluate the claimed quadrature identity at \(a=y\) for each representative \(y\in G_n\). The resulting linear system is
\[
K_{n,p}\,\omega=K_{n,p}\,(2^{1-n}\mathbf1).
\]
Invertibility forces \(\omega=2^{1-n}\mathbf1\). This proves uniqueness of antipodal class weights and the sharp number of distinct sign classes. No positivity hypothesis is required.

**5. Quadratic endpoint.** Expanding the square,
\[
\left(\sum_i\epsilon_i\right)^2=n+2\sum_{i<j}\epsilon_i\epsilon_j,
\]
shows directly that the degree-zero and degree-two eigenvalues of the antipodal convolution matrix are \(n2^{n-1}\) and \(2^n\), and that every higher even degree vanishes. The rank formula follows.

## Verification
The calculation of the finite binomial spectrum has been checked against direct Walsh eigenvector multiplication on every antipodal sign cube of dimensions \(2\) through \(6\), for the powers \(1\) and \(3/2\). The standalone pure-Python script `check_rademacher_inertia.py` additionally checks integral-level sign predictions on finite dimensions for representative powers, uses exact integer arithmetic at powers \(1\) and \(2\), and reports `RADEMACHER_ABSOLUTE_POWER_DIAGNOSTICS_OK 587`. The all-dimensions assertion follows from the integral sign lemma, not finite diagnostics. For a compact hand check, at \(n=4\) the three eigenvalues are \(4^p+4\cdot2^p\), \(4^p\), and \(4^p-4\cdot2^p\), with multiplicities \(1,6,1\) and signs \(+,+,-\) when \(0<p<2\).

## Relationship to prior work
Dai and Kosov (2026), arXiv:2611.05930v1, study approximate \(L^p\)-norm discretization and supply near-linear sampling bounds at fixed relative error. Their Theorem 1.3 and Corollary 1.6 concern approximate sampling of marginal moments, whereas the result here treats **exact** cubature on one specific natural subspace and determines the full signed spectrum of its sampling kernel. The combinatorial Walsh/Krawtchouk diagonalization is classical; Feinsilver and Schott (2018) give a general Krawtchouk transform calculus but not the strict sign law for this absolute-power kernel. Earlier work on the Blaschke–Lévy / \(L^p\) cosine transform, including Koldobsky (1996), may imply injectivity and representing-measure uniqueness in broader settings; the uniqueness-of-weights consequence is therefore not represented as a standalone priority claim. The specific all-dimensions **positive/negative inertia** and sign calculation is the new structural assertion assessed here.

## Limitations
The theorem is not a lower bound for approximate discretization and does not restrict quadratures supported at nodes outside the Boolean sign cube. It does not assert a uniform spectral gap as the power approaches \(2\) or the dimension grows. Earlier equivalent formulations of the Walsh sign property in Krawtchouk or cosine-transform literature may affect publication priority. Some relevant earlier cosine-transform material was available only at the abstract level and merits subsequent independent inspection.

## References
1. F. Dai and E. Kosov, *Empirical approximation of \(L^p\) norms for \(p\in(1,2)\)*, arXiv:2611.05930v1, first publicly submitted 4 November 2026. https://arxiv.org/html/2611.05930v1
2. P. Feinsilver and R. Schott, *Krawtchouk transforms and convolutions*, Bulletin of Mathematical Sciences (2018), DOI:10.1007/s13373-018-0132-2. https://link.springer.com/article/10.1007/s13373-018-0132-2
3. A. Koldobsky, *Inverse formula for the Blaschke–Lévy representation with applications to zonoids and sections of star bodies*, arXiv:math/9605212 (1996). https://arxiv.org/abs/math/9605212
