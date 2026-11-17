# Sharp logarithmic bounded-variation growth of Chebyshev-root Hermite–Fejér interpolation

## Finding

Let \(H_n\) denote ordinary Hermite–Fejér polynomial interpolation at the \(n\) distinct zeros of the first-kind Chebyshev polynomial \(T_n\): it matches \(n\) sampled values and has derivative zero at all \(n\) nodes, with degree at most \(2n-1\). For real bounded-variation functions on \([-1,1]\), put
\[
K_n=\sup_{\operatorname{Var}(f)>0}\frac{\operatorname{Var}(H_nf)}{\operatorname{Var}(f)}.
\]
For every integer \(n\ge2\), \(K_n\) is attained by a one-jump function. As \(n\to\infty\),
\[
\boxed{K_n=\frac4{\pi^2}\log n+O(1).}
\]
Moreover the one-jump function changing value between the two central groups of interpolation nodes already has variation amplification \(4\log n/\pi^2+O(1)\). This is an asymptotically sharp leading coefficient, *not* an exact formula for any fixed \(n\). Although every \(H_n\) is a positive unital operator with \(\|H_n\|_{L^\infty\to L^\infty}=1\), its bounded-variation seminorm is not uniformly bounded in \(n\).

## Assumptions and scope

For an integer \(n\ge2\), write \(\theta_k=(k-1/2)\pi/n\), \(x_k=\cos\theta_k\), \(1\le k\le n\), so \(x_1>\cdots>x_n\). For any real \(f\) defined on \([-1,1]\), the polynomial \(H_nf\) is uniquely determined by
\[
(H_nf)(x_k)=f(x_k),\qquad (H_nf)'(x_k)=0\quad(1\le k\le n).
\]
The variation seminorm is \(\operatorname{Var}_{[-1,1]}(g)=\sup_{-1=t_0<\cdots<t_r=1}\sum_{i=1}^r|g(t_i)-g(t_{i-1})|\). The supremum defining \(K_n\) ranges over real functions of finite, nonzero variation; no differentiability or continuity is required. Sampling bounded-variation functions at the nodes is well-defined because point values are part of the specified data. Logarithms are natural.

Let \(h_k\) be the fundamental Hermite–Fejér polynomial satisfying the above derivative conditions and \(h_k(x_j)=\mathbf1_{j=k}\). Standard Chebyshev identities give the exact representation, with removable singularities at nodes,
\[
h_k(x)=\frac{T_n(x)^2(1-x x_k)}{n^2(x-x_k)^2},\qquad H_nf=\sum_{k=1}^nf(x_k)h_k.
\]
Indeed, \(T'_n(x_k)^2=n^2/(1-x_k^2)\) and \(T''_n(x_k)/T'_n(x_k)=x_k/(1-x_k^2)\). Hence \(h_k\ge0\), and uniqueness for the constant data yields \(\sum h_k=1\). The case \(n=1\) has zero output variation and is excluded from the logarithmic theorem.

## Proof

**1. Reduction to steps and exact oscillation count.** For each \(1\le m<n\), define \(F_m=\sum_{k=1}^m h_k\). At the ordered nodes, \(F_m(x_k)=1\) when \(k\le m\), zero otherwise, and \(F'_m(x_k)=0\) for every \(k\). For any sampled data \(y_k=f(x_k)\), write
\[
H_nf=y_n+\sum_{m=1}^{n-1}(y_m-y_{m+1})F_m.
\]
Thus \(\operatorname{Var}(H_nf)\le\max_m\operatorname{Var}(F_m)\sum_m|y_m-y_{m+1}|\le\max_m\operatorname{Var}(F_m)\operatorname{Var}(f)\). Conversely, a unit step between \(x_m\) and \(x_{m+1}\) has unit input variation and produces \(F_m\). The same sampled values and unit variation can be achieved by a continuous monotone piecewise-linear ramp confined to this gap. Therefore
\[
K_n=\max_{1\le m<n}\operatorname{Var}(F_m).
\]
Moreover \(0<F_m(x)<1\) whenever \(x\in(-1,1)\) is not a node: both \(F_m\) and \(1-F_m\) are sums of strictly positive \(h_k\) there. Hence each of the \(n-2\) open intervals between consecutive nodes with *equal* step labels contains an interior extremum of \(F_m\). Together with the \(n\) distinct nodal zeros of \(F'_m\), these supply \(2n-2\) distinct zeros. As \(\deg F'_m\le2n-2\), this exhausts its zeros. Consequently each equal-label gap has exactly one interior extremum, the central label-changing gap is monotone, and the two exterior intervals are monotone. Writing \(B_j\) for the maximum of \(1-F_m\) on \([x_{j+1},x_j]\) when \(j<m\), and the maximum of \(F_m\) there when \(j>m\), gives
\[
\operatorname{Var}(F_m)=1+2\sum_{j<m}B_j+2\sum_{j>m}B_j+E_m,
\]
where \(0\le E_m\le2\) is the sum of the two endpoint departures from the nearest nodal value. This formula includes all intervals and has no uncounted critical points.

**2. Exact angular kernel.** Put \(x=\cos\theta\). Using \(\cos\theta-\cos\phi=-2\sin((\theta+\phi)/2)\sin((\theta-\phi)/2)\) and \(1-\cos\theta\cos\phi=\sin^2((\theta-\phi)/2)+\sin^2((\theta+\phi)/2)\), we obtain for \(\theta\ne\theta_k\)
\[
h_k(\cos\theta)=\frac{\cos^2(n\theta)}{4n^2}\left[\csc^2\frac{\theta-\theta_k}{2}+\csc^2\frac{\theta+\theta_k}{2}\right].
\]
The first term is the direct angular interaction; the second is its endpoint-reflected interaction. We use \(0\le\frac14\csc^2(t/2)-t^{-2}\le C\) uniformly for \(0<t\le\pi\), with an absolute constant \(C\), and \(\frac14\csc^2(t/2)\le(\pi^2/4)\min\{t,2\pi-t\}^{-2}\) for \(0<t<2\pi\).

**3. Uniform upper bound.** Consider a zero-label gap \(j>m\), so \(\theta\in[\theta_j,\theta_{j+1}]\). Since \(\theta-\theta_k\ge(j-k)\pi/n\) for \(k\le m\), the direct part of \(F_m\) is bounded by
\[
\frac1{\pi^2}\sum_{k=1}^m\frac1{(j-k)^2}+\frac{Cm}{n^2}.
\]
For the reflected part, \(\theta+\theta_k\ge(j+k-1)\pi/n\) and \(2\pi-\theta-\theta_k\ge(2n-j-k)\pi/n\). Thus it is at most
\[
\frac14\sum_{k=1}^m\left(\frac1{(j+k-1)^2}+\frac1{(2n-j-k)^2}\right).
\]
Summing over zero-label gaps \(j=m+1,\ldots,n-1\), the two reflected double sums are individually at most one: for the first, bound each denominator by \(j\) and use \(m\sum_{j>m}j^{-2}\le1\); for the second, put \(a=n-j\), \(b=n-k\), bound \((a+b)^{-2}\le b^{-2}\), and use \((n-m-1)\sum_{b\ge n-m}b^{-2}\le1\) whenever the range is nonempty. The direct sum is bounded by
\[
\frac1{\pi^2}\sum_{d=1}^{n-m-1}\sum_{r=d}^{\infty}r^{-2}=\frac1{\pi^2}\log(n-m)+O(1),
\]
where \(d=j-m\), and the summed uniform error is \(O(1)\). Therefore \(\sum_{j>m}B_j\le\pi^{-2}\log(n-m)+O(1)\), with the constant uniform in \(m,n\).

Reflecting \(x\mapsto-x\) interchanges the nodes and complements the step, so the identical argument shows \(\sum_{j<m}B_j\le\pi^{-2}\log m+O(1)\). Hence
\[
\operatorname{Var}(F_m)\le\frac2{\pi^2}\bigl[\log m+\log(n-m)\bigr]+O(1)\le\frac4{\pi^2}\log n+O(1),
\]
uniformly for \(1\le m<n\). This proves the asserted upper bound for \(K_n\).

**4. Matching lower bound from one central step.** Take \(m=\lfloor n/2\rfloor\). For zero-label gaps indexed by \(j=m+d\), \(1\le d\le\lfloor n/4\rfloor\), evaluate at \(\theta=j\pi/n\). These are gap midpoints where \(\cos^2(n\theta)=1\). Since \(\frac14\csc^2(t/2)\ge t^{-2}\) for \(0<t\le\pi\), the exact kernel gives
\[
B_j\ge F_m(\cos(j\pi/n))\ge\frac1{\pi^2}\sum_{r=0}^{m-1}\frac1{(d+r+1/2)^2}\ge\frac1{\pi^2}\left[\frac1{d+1/2}-\frac1{d+m+1/2}\right].
\]
The last inequality compares a decreasing sum with its integral. Summing the displayed bound over \(1\le d\le\lfloor n/4\rfloor\) yields \(\sum_{j>m}B_j\ge\pi^{-2}\log n+O(1)\): the first reciprocal sum is harmonic, while the second is uniformly bounded. By reflection the one-label gaps contribute another \(\pi^{-2}\log n+O(1)\). The exact variation formula from step 1 therefore gives
\[
\operatorname{Var}(F_{\lfloor n/2\rfloor})\ge\frac4{\pi^2}\log n+O(1).
\]
Together with step 3 this proves both the sharp leading coefficient and central-step asymptotic attainment.

## Verification

The accompanying `checker.py` independently reconstructs the fundamental cardinal polynomials in small degrees, checks nonnegativity and the partition of unity numerically for several degrees, and numerically maximizes the interior step-response oscillations for \(n=2,3,4,6,8,12,18,30\). It reports `ALL_FINITE_HERMITE_FEJER_CHECKS_PASS`. These finite tests do not prove the all-degree asymptotic; that proof is the exact zero-count plus angular-kernel estimates above. Run using `python3 checker.py` with Python, NumPy, SciPy and SymPy.

## Relationship to prior work

The Hermite–Fejér operator, its positivity, and uniform approximation of continuous data at first-kind Chebyshev zeros are classical (Fejér 1916). The 1990 paper of Al-Jarrah and Rababah and the 1983 work of Bojanic and Cheng concern pointwise approximation-rate estimates for bounded-variation inputs; they do not state the global output-variation seminorm or its sharp asymptotic coefficient. The later work of Xiang and He studies approximation in uniform norms, derivative data, and smooth-function error rates, not this output-BV stability. Smith's 2002 study concerns the Lebesgue function for *extended* nodes, a different operator and norm. These are comparisons of mathematical implications, not claims of exhaustive priority. See the accompanying review for access limitations and priority risks.

## Limitations

The theorem is asymptotic, with an unspecified uniform additive \(O(1)\); it does not give the exact finite-degree \(K_n\), nor prove that the central step maximizes \(K_n\) for each finite \(n\). Its setting is first-kind Chebyshev zeros on \([-1,1]\), zero imposed nodal derivatives, real BV input, and output total variation on the same whole interval. It does not cover endpoint-extended node sets, second-kind Chebyshev nodes, Jacobi families with other parameters, or joint value-and-derivative interpolation. Historical priority remains subject to unindexed older literature.

## References

1. L. Fejér, “Über Interpolation,” Nachrichten der Gesellschaft der Wissenschaften zu Göttingen (1916), pp. 66–91 (original historical source, year established; full text not inspected).
2. R. Al-Jarrah and A. Rababah, “On the rate of convergence of Hermite-Fejér polynomials to functions of bounded variation on the zeros of certain Jacobi polynomials,” Revista Colombiana de Matemáticas **24** (1990), pp. 51–64, https://revistas.unal.edu.co/index.php/recolma/article/download/33206/33203/123112 (primary full text inspected).
3. R. Bojanic and F. H. Cheng, “Estimates for the rate of approximation of functions of bounded variation by Hermite-Fejér polynomials,” CMS Conference Proceedings **3** (1983), pp. 5–17 (cited and described by Ref. 2; independent full text not obtained).
4. W. Gautschi, “Interpolation before and after Lagrange,” Rendiconti del Seminario Matematico della Università e Politecnico di Torino **70** (2012), pp. 347–368, https://seminariomatematico.polito.it/rendiconti/70-4/347.pdf (historical survey).
5. S. Xiang and G. He, “On the Convergence Rate of Hermite-Fejér Interpolation,” in *Spectral and High Order Methods for Partial Differential Equations* (2020), pp. 623–635, https://doi.org/10.1007/978-3-030-39647-3_50 (full open-access HTML inspected).
6. S. J. Smith, “The Lebesgue function for Hermite-Fejér interpolation on the extended Chebyshev nodes,” Bulletin of the Australian Mathematical Society **66** (2002), pp. 151–162, https://doi.org/10.1017/S0004972700020773 (abstract examined; full text not inspected).
