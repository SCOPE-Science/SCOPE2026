# Sharp one-to-three-mode transition for a weighted equiangular Poisson extension

## Finding

For \(0<r<1\) define the circular Poisson kernel
\[
P_r(t)=\frac{1-r^2}{1+r^2-2r\cos t}.
\]
For every real \(w>1\), let
\[
U_{r,w}(t)=wP_r(t)+P_r(t-2\pi/3)+P_r(t+2\pi/3),\qquad t\in\mathbb R/(2\pi\mathbb Z).
\]
Define
\[
F(r)=\frac{9r^2(1+r^2+r^4)}{(1-r^2)^3}.
\]
Then the number of *strict local maxima* of \(U_{r,w}\) on the circle is exactly
\[
\begin{cases}
1,&w-1\ge F(r),\\
3,&0<w-1<F(r).
\end{cases}
\]
At equality, the sole strict local maximum is at \(t=0\); there are in addition exactly two stationary points \(t=\pm\arccos(-r/2)\) of order two for the derivative (stationary shoulders, not extrema). For \(w-1<F(r)\), all three local maxima are nondegenerate, as are all three minima. When \(w-1>F(r)\), the sole maximum and the sole minimum are nondegenerate.

Equivalently, for each \(w>1\) there is one and only one critical radius \(r_*(w)\in(0,1)\), characterized by \(F(r_*)=w-1\); increasing \(r\) across it creates exactly one symmetric pair of additional maxima via two simultaneous nondegenerate folds. If \(x_-(r)<x_+(r)\) are the two noncentral cosine coordinates when \(r>r_*\), then
\[
x_\pm(r)=-\frac r2\pm
\sqrt{\frac{(1-r_*^2)(1+2r_*^2)}{2r_*(1+r_*^2+r_*^4)}}\sqrt{r-r_*}
+O(r-r_*),\quad r\downarrow r_*.
\]
Here \(x_-\) corresponds to a lateral maximum and \(x_+\) to an adjacent minimum at positive angle. For the ordinary four-observation empirical sample with locations \(0,0,\pm 2\pi/3\) (\(w=2\)), \(r_*^2\) is the unique root in \((0,1)\) of
\[
10q^3+6q^2+12q-1=0,
\]
so \(r_*\approx0.28236911011380844\).

## Assumptions and scope

All locations and angles are understood modulo \(2\pi\). The parameter \(r\) is a *concentration radius*: the Poisson kernel approaches a constant as \(r\downarrow0\) and an atomic mass as \(r\uparrow1\). The weight condition \(w>1\) means the atom at angle zero has larger mass than either of the two symmetric atoms. Multiplying \(U\) by \(1/[2\pi(w+2)]\) yields a probability density without altering critical points or modes. All statements concern \(0<r<1\), not the singular endpoint \(r=1\). A *mode* means a strict local maximum of the smooth real-valued function on the whole circle.

## Proof

The absolutely convergent Fourier expansion \(P_r(t)=\sum_{n\in\mathbb Z}r^{|n|}e^{int}\) gives the exact three-root identity
\[
P_r(t)+P_r(t-2\pi/3)+P_r(t+2\pi/3)=3P_{r^3}(3t).
\]
Consequently \(U_{r,w}=(w-1)P_r(t)+3P_{r^3}(3t)\). Set \(x=\cos t\), \(D_1=1+r^2-2rx\), and \(D_3=1+r^6-2r^3(4x^3-3x)\). Direct differentiation, using \(\sin(3t)=(4x^2-1)\sin t\), yields
\[
U'_{r,w}(t)=-\frac{2r(1-r^2)\sin t}{D_1^2}
\left[(w-1)+9r^2(1+r^2+r^4)(4x^2-1)\frac{D_1^2}{D_3^2}\right].
\]
For \(0<t<\pi\), the derivative is strictly negative whenever \(|x|\ge1/2\). In the remaining interval, let
\[
Q_r(x)=1-r^2+r^4+2r(1+r^2)x+4r^2x^2.
\]
The factorization \(D_3=D_1Q_r(x)\) follows by expansion (or by multiplying the two shifted Poisson denominators). In particular \(Q_r(x)>0\) for \(-1\le x\le1\). Define
\[
H_r(x)=\frac{9r^2(1+r^2+r^4)(1-4x^2)}{Q_r(x)^2},\qquad -\frac12\le x\le\frac12.
\]
On the middle sector the sign of the derivative is minus the sign of \((w-1)-H_r(x)\). The exact derivative identity
\[
H'_r(x)=
-\frac{36r^2(1+r^2+r^4)(r+2x)(1+2rx)(1+r^2-2rx)}{Q_r(x)^3}
\]
shows strict increase on \((-1/2,-r/2)\) and strict decrease on \((-r/2,1/2)\). Both endpoint values are zero and
\[
Q_r(-r/2)=(1-r^2)^2,\quad H_r(-r/2)=F(r).
\]
Thus \(H_r(x)=w-1\) has two distinct interior solutions if and only if \(0<w-1<F(r)\), one double solution at equality, and none if \(w-1>F(r)\). The sign pattern of \(U'\) as \(t\) goes from \(0\) to \(\pi\) is \(-,+,-\) in the two-root regime and is negative elsewhere. Since \(U\) is even, this proves the complete mode count, nondegeneracy away from the threshold, and the shoulder classification at equality. The stationary point at \(\pi\) is always a strict minimum, while \(0\) is a strict maximum.

Finally,
\[
F'(r)=\frac{18r(1+2r^2)^2}{(1-r^2)^4}>0,
\]
with \(F(0+)=0\) and \(F(1-)=+\infty\), proving uniqueness of \(r_*(w)\). At \(x=-r/2\),
\[
H''_r(-r/2)=-\frac{72r^2(1+r^2+r^4)(1+2r^2)}{(1-r^2)^5}<0.
\]
Taylor expansion of \(H_r(x)-(w-1)\) around the moving maximizer \(x=-r/2\), at \(r=r_*\), gives the displayed square-root separation with coefficient squared \(2F'(r_*)/[-H''_{r_*}(-r_*/2)]\). Substituting \(w=2\) and \(q=r^2\) yields the stated cubic and its unique root.

## Verification

A standalone SymPy script `check.py` verifies, by exact symbolic reduction, the denominator factorization, derivative identity, global maximum formula, threshold derivative, second derivative, fold coefficient, and the \(w=2\) cubic. It additionally performs exact rational interval root counts for several test radii; these illustrative checks are not substituted for the global sign proof. Run `python check.py` with Python 3 and SymPy installed. The script reports twelve passing exact assertions.

## Relationship to prior work

The circular Poisson/wrapped-Cauchy density and its Fourier-series interpretation are developed by Chaubey (2018). Zhang and Chen (2020) give general directional density-estimator derivative and mode-consistency results, while Baringhaus and Grübel (2023) study representations and convolution composition of wrapped-Cauchy distributions. None of the inspected corresponding analyses derives the present *weighted three-equiangular finite-sample mode count, exact all-weight threshold, stationary-fold location, or square-root splitting*. Real-line Poisson mixture mode results concern a different, nonperiodic geometry and do not imply these circle thresholds. This is a best-knowledge comparison, not a claim of certified historical uniqueness.

## Limitations

The classification assumes exactly three angular sites at separation \(2\pi/3\), equal satellite weights, and a heavier central atom \(w>1\). It does not classify unequal satellite weights, other site geometries, negative masses, or smoothing kernels other than the wrapped Cauchy/Poisson family. General-mode algorithms and unindexed older exact identities might cover equivalent special cases; independent historical and mathematical assessment remains outstanding. The fold law is asymptotic as \(r\downarrow r_*\) with fixed \(w\), not uniform in unbounded \(w\).

## References

1. Y. P. Chaubey, *Smooth Kernel Estimation of a Circular Density Function: A Connection to Orthogonal Polynomials on the Unit Circle*, Journal of Probability and Statistics (2018), DOI: 10.1155/2018/5372803, https://onlinelibrary.wiley.com/doi/10.1155/2018/5372803 (first public 2018-04-01).
2. Y. Zhang and Y.-C. Chen, *Kernel Smoothing, Mean Shift, and Their Learning Theory with Directional Data*, arXiv:2010.13523 (2020), https://arxiv.org/abs/2010.13523.
3. L. Baringhaus and R. Grübel, *Discrete mixture representations of spherical distributions*, Statistical Papers (first online 2023), DOI: 10.1007/s00362-023-01393-5, https://link.springer.com/article/10.1007/s00362-023-01393-5.
