# Universal logarithmic variation amplification for fixed-order Floater–Hormann interpolation

## Finding
Fix an integer \(d\ge1\). For \(n\ge2d\), let \(R_{n,d}\) be the ordinary Floater–Hormann rational interpolant of blending degree \(d\) at the integer nodes \(0,1,\ldots,n\), acting on real nodal data. For \(1\le j\le n\), let \(s^{(j)}_i=\mathbf1_{\{i\ge j\}}\), and put
\[
\beta_i=\sum_{k=\max(0,i-n+d)}^{\min(d,i)}\binom dk,
\quad w_i=(-1)^i\beta_i,
\quad L_j=\sum_{i=0}^{j-1}w_i.
\]
There is a constant \(C_d<\infty\), depending only on \(d\), such that **uniformly for every \(n\ge2d\) and every \(1\le j\le n\)**,
\[
\left|\operatorname{Var}_{[0,n]}(R_{n,d}s^{(j)})
-\frac{2|L_j|}{\pi2^d}\log\bigl(j(n-j+1)\bigr)\right|\le C_d.
\]
Furthermore, \(|L_j|\le2^{d-1}\) for all \(j\), with equality whenever \(d\le j\le n-d+1\). Consequently the sharp real bounded-variation seminorm satisfies
\[
\boxed{\ \sup_{\operatorname{Var}(f)>0}
\frac{\operatorname{Var}(R_{n,d}f)}{\operatorname{Var}(f)}
=\frac2\pi\log n+O_d(1),\quad n\to\infty.\ }
\]
The supremum at every finite \(n\) is attained by some one-jump input, and any sequence of central jumps \(j=\lfloor n/2\rfloor\), with fixed \(d\) and sufficiently large \(n\), achieves the leading coefficient. Thus the coefficient \(2/\pi\) is independent of each **fixed** positive polynomial-reproduction degree; the bounded remainder is not claimed uniform as \(d\to\infty\).

## Assumptions and scope
The nodes are equally spaced and are written as integers by affine rescaling. Data are real. The operator is the rational interpolant
\[
R_{n,d}y(x)=\frac{\sum_{i=0}^n w_i y_i/(x-i)}{D_{n,d}(x)},
\qquad D_{n,d}(x)=\sum_{i=0}^n\frac{w_i}{x-i},
\]
with continuous removable values at the nodes. For a real function \(f\) of finite Jordan variation on \([0,n]\), \(R_{n,d}f\) means interpolation of the samples \(f(0),\ldots,f(n)\). Write \(V_d(y)=\sum_{i=0}^{n-1}|y_{i+1}-y_i|\). The precise finite-grid seminorm is taken over real data as \(\sup_{V_d(y)>0}\operatorname{Var}(R_{n,d}y)/V_d(y)\), which equals the function-space supremum in the finding. The asymptotic lets \(n\to\infty\) with \(d\) fixed. The theorem does not cover \(d=0\), changing \(d\) with \(n\), arbitrary nonuniform nodes, or complex-valued data.

## Proof
**1. Exact jump reduction.** Constant data are reproduced. Every real vector has the decomposition
\[
y_i=y_0+\sum_{j=1}^n (y_j-y_{j-1})s_i^{(j)}.
\]
By linearity and the triangle inequality for variation,
\[
\operatorname{Var}(R_{n,d}y)\le V_d(y)\max_{1\le j\le n}\operatorname{Var}(R_{n,d}s^{(j)}).
\]
The reverse inequality is attained by the data of a maximizing single jump. It is also attained in the BV function formulation by a step at a non-nodal point strictly between \(j-1\) and \(j\). Thus the exact finite-grid seminorm is precisely the maximum of the jump-response variations.

**2. Prefix arithmetic.** The stated \(\beta_i\) are the equispaced Floater–Hormann weights. Their symmetry \(\beta_{n-i}=\beta_i\) and binomial construction give
\[\sum_{i=0}^n w_i=0.\]
Indeed, expand \(\sum_i w_i=\sum_{k=0}^d\binom dk\sum_{i=k}^{n-d+k}(-1)^i\). If the inner interval has even length, each inner sum vanishes; if it has odd length, the inner sum equals \((-1)^k\), whose binomially weighted total is \((1-1)^d=0\) for \(d\ge1\).
For \(1\le j\le d\), reversing a finite double sum gives the explicit formula
\[
L_j=(-1)^{j-1}
\sum_{\substack{0\le k\le j-1\\k\equiv j-1\pmod2}}
\binom dk.
\]
The sum is bounded by the full parity half-sum \(2^{d-1}\), with equality at \(j=d\). On the interior plateau \(\beta_i=2^d\), the recurrence \(L_{j+1}=L_j+(-1)^j2^d\) shows \(L_j=(-1)^{j-1}2^{d-1}\) for \(d\le j\le n-d+1\). Reflection and the zero total sum handle the right boundary. In particular \(\max_j|L_j|=2^{d-1}\). Also, as \(i\) traverses the interior, the suffix sums \(Q_i=\sum_{k=i}^n w_k=-L_i\) alternate with constant magnitude \(2^{d-1}\); at most \(2d\) boundary indices have other bounded magnitudes.

**3. Uniform inverse-denominator control.** If \(x=m+t\), with integer \(0\le m<n\) and \(0<t<1\), the established Floater–Hormann denominator inequality for the degree-\(d\) equispaced weights reads
\[
|D_{n,d}(m+t)|\,t(1-t)\ge1.
\]
It is the unit-mesh form of the inequality proved in Bos–De Marchi–Hormann–Klein (2012), Section 2, from the positive local polynomial-blending denominator. Independently, \(\beta_i\le2^d\) and the square-reciprocal series bound imply
\[
|D_{n,d}'(m+t)|\le C_d\bigl(t^{-2}+(1-t)^{-2}\bigr).
\]
Writing \(g_{n,d}=1/D_{n,d}\) away from the nodes and extending continuously with value zero at each node gives
\[
|g_{n,d}(m+t)|\le t(1-t),\qquad |g_{n,d}'(m+t)|\le C_d.
\]
The derivatives extend continuously through the nodes. The classical alternating cotangent partial-fraction formula identifies the infinite constant-weight denominator as \(D_\infty(x)=2^d\pi/\sin(\pi x)\). Therefore put \(g_\infty(x)=\sin(\pi x)/(2^d\pi)\). For fixed \(d\), only the first and last \(d\) weights differ from \(2^d\), while the omitted exterior alternating tails have first-term bounds. Consequently, off bounded-width boundary neighborhoods,
\[
|D_{n,d}-D_\infty|+|D_{n,d}'-D_\infty'|
\le C_d\left(\frac1{1+x}+\frac1{1+n-x}\right)=C_d E_n(x).
\]
Here poles at integral nodes are understood only off the nodes. The identity \(g-g_\infty=gg_\infty(D_\infty-D)\), together with \(|g|+|g_\infty|\le C_d t(1-t)\) and the derivative bounds, cancels the apparent poles and yields the **global** estimate
\[
|g_{n,d}(x)-g_\infty(x)|+|g_{n,d}'(x)-g_\infty'(x)|\le C_d E_n(x).
\tag{1}
\]
On each fixed-width boundary neighborhood the same estimate follows directly from boundedness of both inverses and their derivatives, because \(E_n\) is bounded below there by a positive constant depending only on \(d\). These estimates hold also at nodes by continuity. No asymptotic uniformity in \(d\) is used.

**4. Alternating-tail lemma for a jump.** Define \(N_j(x)=\sum_{i=j}^n w_i/(x-i)\) for \(x<j\). Summation by parts, using \(Q_i=-L_i\) and \(Q_{n+1}=0\), gives
\[
N_j(x)=\frac{L_j}{j-x}
+\sum_{i=j+1}^n Q_i\left(\frac1{x-i}-\frac1{x-i+1}\right).
\]
For \(j-x\ge1\), the successive reciprocal differences are positive and decrease in absolute value, at scale \((i-x)^{-2}\). The \(Q_i\) form a bounded alternating sequence except at finitely many boundary indices (depending only on \(d\)); the alternating-series estimate plus these finitely many terms, and the same argument after differentiation, show
\[
\left|N_j(x)-\frac{L_j}{j-x}\right|\le\frac{C_d}{(j-x)^2},\quad
\left|N_j'(x)-\frac{L_j}{(j-x)^2}\right|\le\frac{C_d}{(j-x)^3}.
\tag{2}
\]
For \(x\ge j\), the analogous reverse summation by parts for the complementary numerator \(C_j(x)=\sum_{i=0}^{j-1}w_i/(x-i)\) gives
\[
\left|C_j(x)-\frac{L_j}{x-j+1}\right|\le\frac{C_d}{(x-j+1)^2},\quad
\left|C_j'(x)+\frac{L_j}{(x-j+1)^2}\right|\le\frac{C_d}{(x-j+1)^3}.
\tag{3}
\]
The bounds are uniform in \(n,j\) for each fixed \(d\).

**5. Variation outside the jump cell.** For \(x\in[0,j-1]\), the response is \(N_j(x)g_{n,d}(x)\). For \(x\in[j,n]\), it is \(1-C_j(x)g_{n,d}(x)\). Combining (1)–(3) with \(g_\infty'(x)=\cos(\pi x)/2^d\) yields respectively
\[
\left|(R_{n,d}s^{(j)})'(x)-\frac{L_j\cos(\pi x)}{2^d(j-x)}\right|
\le C_d\left(\frac1{(j-x)^2}+\frac{E_n(x)}{j-x}\right),
\]
\[
\left|(R_{n,d}s^{(j)})'(x)+\frac{L_j\cos(\pi x)}{2^d(x-j+1)}\right|
\le C_d\left(\frac1{(x-j+1)^2}+\frac{E_n(x)}{x-j+1}\right).
\]
Each right side has an integral bounded uniformly in \(n,j\): the squared-distance terms are integrable, and \(E_n\) has uniformly bounded integral and the other denominators are at least one. On the single crossing cell \((j-1,j)\), the response derivative has total integral \(O_d(1)\): on its left half the numerator \(N_j\) and its derivative are uniformly bounded, and on its right half the complementary numerator \(C_j\) and its derivative are uniformly bounded. Indeed each is a finite initial cluster followed by a decreasing alternating reciprocal tail. The previously established bounds on \(g\) and \(g'\) finish this local estimate. Thus
\[
\operatorname{Var}(R_{n,d}s^{(j)})=
\frac{|L_j|}{2^d}\left(
\int_1^{j}\frac{|\cos(\pi u)|}{u}\,du+
\int_1^{n-j+1}\frac{|\cos(\pi u)|}{u}\,du
\right)+O_d(1).
\tag{4}
\]

**6. Extract the sharp coefficient.** The periodic function \(|\cos(\pi u)|\) has mean \(2/\pi\) and its mean-zero part has a bounded primitive. Integration by parts therefore gives \(\int_1^s |\cos(\pi u)|u^{-1}du=(2/\pi)\log s+O(1)\), uniformly for \(s\ge1\). Substituting into (4) proves the stated uniform jump profile. Its upper bound follows from \(|L_j|\le2^{d-1}\) and \(j(n-j+1)\le(n+1)^2/4\). A central jump has \(|L_j|=2^{d-1}\) and \(j(n-j+1)\asymp n^2\) for sufficiently large \(n\) at fixed \(d\), giving the matching lower bound \((2/\pi)\log n-O_d(1)\). The exact jump reduction completes the proof.

## Verification
The accompanying `verify_fh_bv.py` checks the binomial weights, zero alternating sum, prefix bounds, exact rational denominator inequality on a finite test grid, and high-order Gauss quadrature of all jump-response variations for several sizes and blending degrees. It prints `ALL_FIXED_ORDER_FH_BV_CHECKS_PASS` when those finite checks pass. The package's analytical argument, rather than any finite calculation, proves the statement for all \(n\) and every fixed \(d\). To reproduce, run `python verify_fh_bv.py` in an environment with Python 3, NumPy and SciPy.

## Relationship to prior work
Floater and Hormann (2007) introduced the pole-free rational family and its barycentric weights. Bos, De Marchi, Hormann and Klein (2012) studied its supremum-norm Lebesgue constants, including logarithmic bounds; their lower-denominator estimate is explicitly used here. Berrut, Floater and Klein (2011) proved derivative approximation rates under smoothness assumptions. None of those statements, as inspected, calculates the BV-to-BV operator seminorm on discontinuous input or the degree-dependent jump profile in (4). A known result for Berrut's different \(d=0\) weights also has logarithmic BV growth with coefficient \(2/\pi\), but does not logically imply the all-fixed-positive-degree theorem, whose endpoint coefficients, polynomial reproduction and extremal jump locations differ.

## Limitations
The claim determines a sharp **leading logarithmic coefficient** and a uniform-in-jump-position asymptotic with an unspecified degree-dependent bounded remainder, not exact finite-\(n\) variation values. An optimal single jump exists at each finite size, but its finite-grid position is not classified. The results are for real signals, equally spaced nodes and each fixed \(d\ge1\); no uniform estimate is asserted when \(d\) increases with \(n\), for nonuniform meshes or for higher-dimensional interpolation. Historical-priority uncertainty remains possible for unindexed work using equivalent BV or derivative-integral terminology.

## References
1. M. S. Floater and K. Hormann, *Barycentric rational interpolation with no poles and high rates of approximation*, Numerische Mathematik **107** (2007), 315–331. https://doi.org/10.1007/s00211-007-0093-y ; full author copy: https://www.inf.usi.ch/hormann/papers/Floater.2007.BRI.pdf . Public online date verified as 2007-06-28.
2. L. Bos, S. De Marchi, K. Hormann and G. Klein, *On the Lebesgue constant of barycentric rational interpolation at equidistant nodes*, Numerische Mathematik **121** (2012), 461–471. https://doi.org/10.1007/s00211-011-0442-8 ; author manuscript: https://www.math.unipd.it/~demarchi/papers/lebesgue.pdf .
3. J.-P. Berrut, M. S. Floater and G. Klein, *Convergence rates of derivatives of a family of barycentric rational interpolants*, Applied Numerical Mathematics **61** (2011), 989–1000. https://doi.org/10.1016/j.apnum.2011.05.001 ; author copy: https://fredi.hepvs.ch/documents/301839/files/bary_derivs.pdf .
4. K. Hormann, G. Klein and S. De Marchi, *Barycentric rational interpolation at quasi-equidistant nodes*, Dolomites Research Notes on Approximation **5** (2012), 1–6. https://doi.org/10.14658/PUPJ-DRNA-2012-1-1 .
