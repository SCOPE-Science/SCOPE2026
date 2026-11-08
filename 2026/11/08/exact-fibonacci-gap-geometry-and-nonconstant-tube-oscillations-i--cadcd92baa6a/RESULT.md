# Exact Fibonacci gap geometry and nonconstant tube oscillations in a Lorenz alpha-limit set

## Finding

For the explicit expanding Lorenz map of Cholewa and Oprocha (2021, Section 3), let \(K\) be the Cantor set identified there as the backward alpha-limit set of a distinguished two-cycle. Its bounded complementary intervals, within its convex hull, have **exactly** the following lengths, with multiplicity:

\[
\kappa\quad\text{once},\qquad
\delta\,\beta^{-m}\quad\text{with multiplicity }2F_{m+1}\quad(m=0,1,2,\ldots),
\]

where \(F_1=F_2=1\) are Fibonacci numbers and

\[
\beta=2\sqrt{\frac23},\qquad
\delta=\frac{15-6\sqrt6}{49}>0,\qquad
\kappa=\frac{10\sqrt6-24}{49}>0.
\]

Consequently, the geometric zeta function of these intervals is

\[
\boxed{\displaystyle
\zeta_K(s)=\kappa^s+\frac{2\delta^s}{1-\beta^{-s}-\beta^{-2s}}
}\qquad(\Re s>D),
\]

with meromorphic extension given by the same expression, and the exact Hausdorff and box dimensions are

\[
\boxed{\displaystyle D=\frac{\log\varphi}{\log\beta}=0.981234651356489\ldots},\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

The complex poles consist of two simple arithmetic progressions, \(D+2\pi i k/\log\beta\) and \(-D+(2k+1)\pi i/\log\beta\), where \(k\in\mathbb Z\).

Let \(a=\min K\), \(b=\max K\), and \(V(\varepsilon)\) be the Lebesgue measure of the \(\varepsilon\)-neighborhood of \(K\) *within* \([a,b]\). Put

\[
\theta(\varepsilon)=\left\{\log_\beta\frac{\delta}{2\varepsilon}\right\}\in[0,1),
\]

where braces denote the fractional part. Then

\[
\boxed{\displaystyle V(\varepsilon)
=(2\varepsilon)^{1-D}\,P(\theta(\varepsilon))+O(\varepsilon)}
\quad(\varepsilon\downarrow0),
\]

with the explicit continuous, nonconstant, one-periodic profile (endpoint values identified)

\[
\boxed{\displaystyle
P(t)=\frac{2\delta^D}{\sqrt5}\left[
\varphi^{3-t}+\frac{\varphi^2}{\beta-\varphi}\,\beta^{(1-D)t}
\right],\quad 0\le t\le1.}
\]

In particular, \(K\) is *not Minkowski measurable*. Both its lower and upper \(D\)-dimensional Minkowski contents are finite and strictly positive, but they are unequal. These results concern the explicit Lorenz alpha-limit set, not an arbitrary Lorenz map.

## Assumptions and scope

The source map is given by \(f(x)=(g(2x-1)+1)/2\) on \([0,1]\), where

\[
\begin{aligned}
&\beta_1=6/5,\quad\beta_2=2\sqrt{2/3},\quad\beta_3=5/(2\sqrt6),\\
&\alpha_1=2(132-25\sqrt6)/245,\quad
\alpha_2=2(32-3\sqrt6)/49,\\
&p=(\alpha_2-\alpha_1)/(\beta_1-\beta_2),\quad
q=(1-\alpha_2)/(\beta_2-\beta_3),
\end{aligned}
\]

and \(g\) is the following piecewise affine map (the convention at its discontinuity is immaterial to the set below):

\[
 g(u)=\begin{cases}
 \beta_1u+\alpha_1,&-1\le u<p,\\
 \beta_2u+\alpha_2,&p\le u<q,\\
 \beta_3u+1,&q\le u<0,\\
 \beta_3u-1,&0\le u\le-q,\\
 \beta_2u-\alpha_2,&-q<u\le-p,\\
 \beta_1u-\alpha_1,&-p<u\le1.
 \end{cases}
\]

Use the explicit orbit endpoints

\[
\begin{aligned}
p_1&=(43-10\sqrt6)/98,&p_2&=(73-10\sqrt6)/98,\\
p_3&=(73+10\sqrt6)/98,&p_4&=(25+22\sqrt6)/98,\\
q_1&=(55+10\sqrt6)/98,&q_2&=(25+10\sqrt6)/98,\\
q_3&=(25-10\sqrt6)/98,&q_4&=(73-22\sqrt6)/98.
\end{aligned}
\]

Define four pairwise disjoint closed intervals

\[
I_0=[q_3,p_1],\quad I_1=[q_4,p_2],\quad
I_2=[q_2,p_4],\quad I_3=[q_1,p_3],\quad
Q=\bigcup_{j=0}^3I_j,
\]

and the forward survivor \(K=\bigcap_{n\ge0}f^{-n}(Q)\). Cholewa and Oprocha prove that \(K=\alpha_f(z_0)\) for the explicitly given two-cycle point \(z_0=(509-146\sqrt6)/490\), and give its symbolic description as the shift avoiding \(000\) and \(111\). Here the metric is ordinary Euclidean distance on the original \([0,1]\), not a symbolic metric. The convex hull is \([q_3,p_3]\).

## Proof

**1. Exact affine core and first holes.** Direct substitution into the six defining branches of \(g\) shows that each \(I_j\) lies entirely in a branch on which \(f\) has slope \(\beta\), and

\[
f(I_0)=I_1,\quad f(I_1)=[q_2,p_3],\quad
f(I_2)=[q_3,p_2],\quad f(I_3)=I_2.
\]

The permitted core transitions, in the order \(0,1,2,3\), are therefore exactly

\[
A=\begin{pmatrix}
0&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&0
\end{pmatrix}.
\]

Within the convex hull, the three gaps between the four initial intervals have lengths

\[
q_4-p_1=q_1-p_4=\delta,\qquad q_2-p_2=\kappa.
\]

The image of \(I_1\) spans \(I_2\) and \(I_3\), leaving the gap \((p_4,q_1)\); its inverse under the affine branch is one new gap of length \(\delta/\beta\) within \(I_1\). Likewise, \(I_2\) has one new inverse gap of length \(\delta/\beta\), corresponding to \((p_1,q_4)\). The other two core intervals have no first-generation internal gap.

**2. All gap generations.** Set \(v=(0,1,1,0)^\mathsf T\). After \(m\) transition-prefix steps, the number of newly generated inverse holes is \(\mathbf 1^\mathsf T A^m v\), each of length \(\delta\beta^{-(m+1)}\). Symmetry between the pair \(I_0,I_3\) and the pair \(I_1,I_2\) reduces the counting recurrence to Fibonacci's recurrence; directly,

\[
\mathbf 1^\mathsf T A^m v=2F_{m+2}\qquad(m\ge0).
\]

Together with the two initial gaps of length \(\delta\), this gives precisely \(2F_{m+1}\) holes of length \(\delta\beta^{-m}\) for every \(m\ge0\), and the single gap \(\kappa\). No other gaps exist: every retained interval is replaced by its full collection of allowed inverse branches, with diameters shrinking uniformly by \(\beta^{-1}<1\).

**3. Length sum, zeta function, and dimension.** A direct algebraic check gives

\[
\kappa+\frac{2\delta}{1-\beta^{-1}-\beta^{-2}}=p_3-q_3.
\]

Thus the complementary gaps exhaust the convex-hull length, and \(K\) has zero Lebesgue measure. The Fibonacci series identity

\[
\sum_{m\ge0}F_{m+1}z^m=\frac1{1-z-z^2}
\]

gives \(\zeta_K\) as stated. The abscissa of absolute convergence is \(D=\log\varphi/\log\beta\), since \(\beta>\varphi>1\). Equivalently, the graph-directed similarities all have ratio \(\beta^{-1}\), are strongly separated in the intervals above, and have adjacency Perron eigenvalue \(\varphi\). The graph-directed dimension theorem, or the same separated-cylinder covering and mass-distribution argument, yields \(\dim_H K=\dim_B K=D\). The denominator's zeros give precisely the displayed simple complex poles.

**4. Exact tube count.** The portion of \(K_\varepsilon\) within \([q_3,p_3]\) covers a fraction \(\min\{2\varepsilon,\ell\}\) of each complementary gap of length \(\ell\). Consequently the identity

\[
V(\varepsilon)=\min\{\kappa,2\varepsilon\}
+2\sum_{m=0}^{\infty}F_{m+1}\min\{\delta\beta^{-m},2\varepsilon\}
\]

holds for every \(\varepsilon>0\). For \(0<2\varepsilon<\delta\), put \(N=\lfloor\log_\beta(\delta/(2\varepsilon))\rfloor\). Separating \(m\le N\) and \(m>N\), using \(\sum_{m=0}^N F_{m+1}=F_{N+3}-1\), and writing \(\psi=(1-\sqrt5)/2\), Binet's formula gives the **exact** expression

\[
\begin{aligned}
V(\varepsilon)={}&2\varepsilon+4\varepsilon(F_{N+3}-1)\\
&+\frac{2\delta}{\sqrt5}\left[
\frac{\varphi(\varphi/\beta)^{N+1}}{1-\varphi/\beta}
-\frac{\psi(\psi/\beta)^{N+1}}{1-\psi/\beta}
\right].
\end{aligned}
\]

Now \(N=\log_\beta(\delta/(2\varepsilon))-\theta(\varepsilon)\) and \(\varphi=\beta^D\). Separating the \(\varphi\)-terms produces the stated \(P(\theta)\), and the remaining terms are \(O(\varepsilon)\) uniformly in \(\theta\). The function \(P\) has equal endpoint values \(P(0)=P(1)\), but is nonconstant because it is a positive sum of exponentials with distinct nonzero exponents, \(-\log\varphi\) and \(\log(\beta/\varphi)\). Thus different sequences of \(\varepsilon\downarrow0\) yield different positive values of \(V(\varepsilon)/(2\varepsilon)^{1-D}\), proving failure of Minkowski measurability. The two exterior \(\varepsilon\)-neighborhoods outside the convex hull contribute only \(2\varepsilon\), so the conclusion also holds for the ordinary full-line tubular neighborhood.

## Verification

Run `python CHECK.py` after installing the dependencies in `requirements.txt`. The checker independently substitutes the actual six-piece formula, tests all four exact core-image identities, verifies the two exact initial gap lengths and gap-length sum, checks the Fibonacci transition identity through sixteen generations, reduces the rational generating function symbolically, and tests the exact tube sum against the analytical periodic profile at three fractional phases. It prints `EXACT_LORENZ_BRANCHES_OK`, `EXACT_FIBONACCI_GAPS_OK`, and `TUBE_ASYMPTOTIC_SPOTCHECK_OK` when successful. Exact branch, gap and matrix assertions are symbolic; numerical tube tests are corroborating checks, not substitutes for the general proof.

## Relationship to prior work

Cholewa and Oprocha (2021) construct the Lorenz map and prove that the specified alpha-limit is a Cantor set conjugate to a finite-type shift, with topological entropy \(\log\varphi\). Those claims are prior work. The dimension formula alone follows routinely from that entropy and the constant slope on the four invariant branches, and is **not claimed as a new general dimension principle**. The new object-specific metric claim is the **complete Euclidean gap multiplicity spectrum**, the resulting *exact* geometric zeta function with its actual length constants, and the *nonconstant explicit* tube-amplitude profile for this alpha-limit set. General fractal-string theory already supplies a framework for geometric zeta functions and log-periodic tube oscillations, and the Fibonacci denominator is itself classical. These general results do not specify the two gap scales and the precise tube profile of this six-piece Lorenz-map construction; that identification is proved here.

## Limitations

The claim is for the particular parameter values and the particular alpha-limit Cantor set above; no variation in map parameters is established. It is a metric refinement of a previously known symbolic construction, not a discovery of its invariant set, entropy, or its abstract Fibonacci recurrence. The general theory of lattice fractal strings and related Fibonacci strings remains prior art. Searches and inspected sources cannot rule out unindexed or differently formulated equivalent calculations. No independent mathematical audit has been performed.

## References

1. Ł. Cholewa and P. Oprocha, *On α-Limit Sets in Lorenz Maps*, Entropy **23** (2021), article 1153, DOI: 10.3390/e23091153. Complete open-access text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8469790/ ; see especially Sections 3–4.
2. Ł. Cholewa and P. Oprocha, *Renormalization in Lorenz Maps—Completely Invariant Sets and Periodic Orbits*, arXiv:2104.00110 (first submitted 2021-03-31; revised 2024). See its distinction between invariant sets and renormalization in expanding Lorenz maps.
3. M. L. Lapidus, E. P. J. Pearse, and S. Winter, *Pointwise Tube Formulas for Fractal Sprays and Self-Similar Tilings with Arbitrary Generators*, arXiv:1006.3807 (2010). General tube-formula framework.
4. M. L. Lapidus, G. Radunović, and D. Žubrinić, *Fractal Tube Formulas for Compact Sets and Relative Fractal Drums*, arXiv:1604.08014 (2016). General complex-dimension framework.
