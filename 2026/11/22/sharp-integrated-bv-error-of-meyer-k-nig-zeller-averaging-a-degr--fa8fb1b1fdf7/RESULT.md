# Sharp integrated \(BV\) error of Meyer–König–Zeller averaging: a degree-eight boundary transition

## Finding
For every integer \(n\ge1\), consider the classical Meyer–König–Zeller (Cheney–Sharma/Bernstein power-series) operator
\[
(M_nf)(x)=(1-x)^{n+1}\sum_{j=0}^{\infty}\binom{n+j}{j}x^j f\!\left(\frac{j}{n+j}\right),\qquad 0\le x<1,
\]
with \((M_nf)(1)=f(1)\). Restrict to real, right-continuous bounded-variation functions on \([0,1]\) with no endpoint jumps, and put \(V(f)=|Df|(0,1)\). The sharp integrated-error quotient is
\[
C_n=\sup_{V(f)>0}\frac{\|M_nf-f\|_{L^1(0,1)}}{V(f)}.
\]
Let \(s_0=0\), \(s_k=k/(n+k)\) for \(k\ge1\), and let \(B_{k,n}\) have the Beta distribution with parameters \((k,n+1)\). Define \(E_{k,n}(s)=\mathbb E|B_{k,n}-s|\), and
\[
K_n=(n+2)\bigl(1+\lceil\sqrt{n+1}\rceil\bigr)+1.
\]
Then the following is an **exact finite formula for every degree**:
\[
\boxed{C_n=\max_{1\le k\le K_n}\max\{E_{k,n}(s_{k-1}),E_{k,n}(s_k)\}.}
\]
Every entry is rational, computable from finite binomial sums. A sharp boundary/interior phase transition occurs at degree eight:
\[
\boxed{C_n=\frac1{n+2}\quad(1\le n\le7),\qquad C_n>\frac1{n+2}\quad(n\ge8).}
\]
For the first seven degrees the sharp norm is **not attained** by any nonconstant admissible function; it is approached by single jumps converging to the left endpoint. For each degree at least eight, an interior single jump strictly outperforms the near-left-endpoint benchmark (the theorem does not assert that the global supremum is attained).

Moreover,
\[
\boxed{\lim_{n\to\infty}\sqrt n\,C_n=\frac{2\sqrt2}{3\sqrt{3\pi}}.}
\]
For every sequence of jump locations \(t_n\in(0,1)\) whose single-jump errors satisfy \(E_n(t_n)/C_n\to1\), one has \(t_n\to1/3\). Here \(E_n(t)=\|M_n\mathbf1_{[t,1]}-\mathbf1_{[t,1]}\|_{L^1}\). Thus the worst-case jump migrates from a nonattained boundary limit at low degree to the interior, with its asymptotic location rigorously fixed at one third.

## Assumptions and scope
The input is a real right-continuous \(BV([0,1])\) function with \(f(0)=f(0+)\) and \(f(1)=f(1-)\); this canonical representative is essential because \(M_n\) samples point values. The variation is the total mass of the distributional derivative on \((0,1)\), and the output norm is the unweighted Lebesgue \(L^1(0,1)\) norm. Constants have zero variation and are reproduced. No claim is made about arbitrary point-value representatives of \(L^1\) equivalence classes.

## Proof
**1. An exact Beta law for each jump.** Any admissible \(f\) admits the measure representation
\[
f(x)=f(0)+\int_{(0,1)}\mathbf1_{[s,1]}(x)\,d(Df)(s),
\qquad |Df|(0,1)=V(f).
\]
For a jump \(h_s=\mathbf1_{[s,1]}\), \(s\in(s_{k-1},s_k]\), the only sampled nodes included in the jump are indices \(j\ge k\). Negative-binomial tail summation gives
\[
(M_nh_s)(x)=\sum_{j\ge k}\binom{n+j}{j}(1-x)^{n+1}x^j=I_x(k,n+1),
\]
where \(I_x(k,n+1)\) is the CDF of \(B_{k,n}\sim\operatorname{Beta}(k,n+1)\). Integration of the two sides of the step therefore yields exactly
\[
\begin{aligned}
E_n(s)&=\int_0^s I_x(k,n+1)\,dx+\int_s^1(1-I_x(k,n+1))\,dx\\
&=\mathbb E|B_{k,n}-s|=E_{k,n}(s).
\end{aligned}
\]
The measure representation and Minkowski's inequality give \(\|M_nf-f\|_1\le(\sup_s E_n(s))V(f)\); single jumps prove equality at the level of supremum.

**2. The exact finite candidate reduction.** For fixed \(k,n\), the function \(s\mapsto E_{k,n}(s)\) is convex. Consequently its supremum on the half-open cell \((s_{k-1},s_k]\) is the larger of its two endpoint values (the left endpoint is understood as a one-sided limit). Hence
\[
C_n=\sup_{k\ge1}\max\{E_{k,n}(s_{k-1}),E_{k,n}(s_k)\}.
\]
For \(\mu_{k,n}=k/(n+k+1)\), the Beta variance is
\[
\sigma_{k,n}^2=\frac{k(n+1)}{(n+k+1)^2(n+k+2)}.
\]
For each of the two candidate endpoints, \(|s-\mu_{k,n}|\le1/(n+k+1)\). The Cauchy–Schwarz estimate thus gives
\[
E_{k,n}(s)\le|s-\mu_{k,n}|+\sigma_{k,n}
\le\frac{1+\sqrt{n+1}}{n+k+1}.
\]
The index \(k=1\) and left limit \(s_0=0\) give \(E_{1,n}(0)=1/(n+2)\). For \(k>K_n\), the displayed upper bound is strictly smaller than \(1/(n+2)\), proving the stated finite maximum formula.

All its entries can be calculated rationally using
\[
\begin{aligned}
E_{k,n}(s)&=\mu_{k,n}-s+2\{sI_s(k,n+1)-\mu_{k,n}I_s(k+1,n+1)\},\\
I_s(a,b)&=\sum_{j=a}^{a+b-1}\binom{a+b-1}{j}s^j(1-s)^{a+b-1-j}.
\end{aligned}
\]

**3. The exact degree-eight transition.** The standalone rational checker exhausts both endpoint candidates for every \(1\le k\le K_n\) and each \(1\le n\le7\). In every case the unique maximizing *candidate* is \((k,s)=(1,0)\), with value \(1/(n+2)\). The estimate above excludes all larger indices; hence this is a finite exact certificate of the first assertion. Because \(s=0\) is excluded as an interior jump, each actual jump has strictly smaller error. Integrating the strict pointwise inequality against the variation measure proves strict inequality for every nonconstant admissible \(f\), and jumps approaching zero attain the limiting coefficient.

For the other side of the boundary it suffices to use the attained interior node \(s_3=3/(n+3)\). Direct Beta integration gives
\[
E_{3,n}(s_3)=\frac{3}{(n+3)(n+4)}
+\frac{3(9n^2+37n+36)}{(n+3)^2(n+4)}
\left(\frac{n}{n+3}\right)^{n+2}.
\]
The inequality \(E_{3,n}(s_3)>1/(n+2)\) is equivalent to
\[
\left(\frac{n}{n+3}\right)^{n+2}>
\frac{(n+3)(n^2+4n+6)}{3(n+2)(9n^2+37n+36)}.
\]
For real \(x>0\), the left side \(q(x)=(x/(x+3))^{x+2}\) increases strictly: putting \(y=3/x\), its logarithmic derivative is \(y(1+2y/3)/(1+y)-\log(1+y)\), which is positive because its derivative with respect to \(y\) is \(y(2y+1)/(3(1+y)^2)>0\) and its value at zero is zero. The right side decreases strictly, since its derivative is
\[
-\frac{2(4x^4+52x^3+245x^2+486x+342)}{3(x+2)^2(9x^2+37x+36)^2}<0.
\]
An exact rational inequality at \(n=8\), checked by the supplied program, finishes the proof for all \(n\ge8\).

**4. Sharp asymptotics and localization.** Let \(k_n/n\to r\in(0,\infty)\). Write \(B_{k_n,n}=U_n/(U_n+W_n)\) for independent Gamma variables with shapes \(k_n\) and \(n+1\). The ordinary two-variable central limit theorem and the delta method give
\[
\sqrt n\,(B_{k_n,n}-\mu_{k_n,n})\ \Longrightarrow\
N\!\left(0,\frac{r}{(1+r)^3}\right).
\]
The Beta variance formula makes absolute moments uniformly integrable after this scaling, and either endpoint differs from the mean by \(O(1/n)\). Therefore
\[
\sqrt n\,E_{k_n,n}(s_{k_n-1}),\quad
\sqrt n\,E_{k_n,n}(s_{k_n})
\longrightarrow\sqrt{\frac2\pi}\frac{\sqrt r}{(1+r)^{3/2}}.
\]
If \(k_n/n\to0\) or \(\infty\), the upper bound by mean error plus the *exact* Beta standard deviation shows the scaled candidates tend to zero. The choice \(k_n\sim n/2\) gives a positive lower bound, so every maximizing sequence has its index ratio in a compact subset of \((0,\infty)\) along subsequences. The profile \(\sqrt r/(1+r)^{3/2}\) has its unique maximum at \(r=1/2\); its value is \(2/(3\sqrt3)\). This proves the sharp limit and forces \(k_n/n\to1/2\), hence every asymptotically norming jump location tends to \(1/3\).

## Verification
Run `python checker.py` with a standard Python interpreter. The code recomputes all 326 rational candidate comparisons for degrees one through seven, checks the strict degree-eight comparison, and independently integrates negative-binomial polynomials against exact rational endpoints. The finite computation supports only the seven small degrees and the single degree-eight base case; monotonicity and asymptotics for infinitely many degrees are proved analytically above. The exact Beta-CDF, variance, and sample-node conventions are visible in the checker.

## Relationship to prior work
The classical MKZ operator and Bernstein power-series representation are established in earlier approximation literature. Kivinukk and Metsmägi (2011) prove variation-diminishing and convergence-in-variation properties of the same operator; they study the variation of \(M_nf-f\), not its sharp Lebesgue-integrated error relative to \(V(f)\). Zeng and Cheng (2011) give a sharp first absolute *pointwise* moment, including the asymptotic profile \(\sqrt{2x}(1-x)/\sqrt{\pi n}\). Thus the Gaussian profile and its maximizer should not be treated as wholly new phenomena. However, pointwise first moments are distinct from the integrated step-response norm, and do not by themselves identify the exact finite-degree boundary-to-interior transition or its nonattainment. Guo–Liu–Wang (2008) treats pointwise direct/inverse/equivalence approximation through moduli; Zeng–Zhao (2000) treats pointwise rates for bounded inputs. Earlier studies of *integrated MKZ modifications* use different operators with integral rather than point samples, and cannot be substituted without proving equivalence. Historical exact equivalents cannot be ruled out absolutely, particularly where older full text was inaccessible.

## Limitations
The operator must act on a specified right-continuous representative; arbitrary a.e. equivalence-class representatives permit altered samples. The theorem classifies the sharp values through a finite rational search, the exact degree-eight boundary of endpoint dominance, and asymptotic locations; it does not claim a closed expression for the unique maximizing finite index, or norm attainment for all degrees at least eight. The proof does not extend to Durrmeyer/integrated MKZ variants, weighted Lebesgue errors, or multidimensional versions without new arguments.

## References
1. A. Kivinukk and T. Metsmägi, *Approximation in variation by the Meyer-König and Zeller operators*, Proceedings of the Estonian Academy of Sciences 60(2) (2011), 88–97. DOI: https://doi.org/10.3176/proc.2011.2.03 . Full text: https://pdfs.semanticscholar.org/ffd6/3ab4f54c8fd26ca1da6f3b32e719f3bd8ee4.pdf .
2. X.-M. Zeng and F. Cheng, *First order absolute moment of Meyer-König and Zeller operators and their approximation for some absolutely continuous functions*, Mathematica Slovaca 61(4) (2011), 635–644. DOI: https://doi.org/10.2478/s12175-011-0033-2 . Full text: https://www.cs.uky.edu/~cheng/PUBL/Paper_FirstOrder_MKZ.pdf .
3. S. Guo, L. Liu and Z. Wang, *Pointwise Approximation by Meyer–König and Zeller Operators*, Numerical Functional Analysis and Optimization 29 (2008), 770–778; published online 17 September 2008. DOI: https://doi.org/10.1080/01630560802279223 . Abstract and publication record inspected; full text not accessible.
4. X.-M. Zeng and J.-N. Zhao, *Pointwise approximation by Meyer-König and Zeller operators*, Annales Polonici Mathematici 73 (2000), 185–196. DOI: https://doi.org/10.4064/ap-73-2-185-196 . Abstract inspected; full text access failed.
5. S. S. Guo, *On the rate of convergence of the integrated Meyer-König and Zeller operators for functions of bounded variation*, Journal of Approximation Theory 56 (1989), 245–255. DOI: https://doi.org/10.1016/0021-9045(89)90114-7 . Different integral-modification operator; only descriptive material accessed.
