# A sharp all-grid positivity frontier for uniform natural cubic interpolation

## Finding

Let \(S_n:\mathbb R^{n+1}\to C[0,n]\) be the ordinary natural cubic interpolant at the equally spaced knots \(0,1,\ldots,n\), for an arbitrary integer \(n\ge1\). Write \(S_n y=\sum_{i=0}^n y_i\ell_{n,i}\) for its cardinal representation. Then
\[
\sup_{n\ge1}\max_{0\le x\le n}\sum_{i=0}^n|\ell_{n,i}(x)|=\frac{1+3\sqrt3}{4}.
\]
Each finite-grid norm is strictly smaller than this supremum, and centered half-cell evaluations on growing grids approach it.

Consequently, for every real \(0<m\le M\), all such splines with data \(m\le y_i\le M\) are nonnegative at every point on every finite uniform grid **if and only if**
\[
\frac M m\le\frac{7+4\sqrt3}{3}.
\]
The necessity has universal-quantifier meaning: for every ratio exceeding this constant, there exist a finite grid and strictly positive data in \([m,M]\) whose ordinary natural cubic spline becomes negative. At equality, all finite-grid interpolants are in fact strictly positive.

## Assumptions and scope

Unit knot spacing is without loss of generality by an affine rescaling. The interpolant is \(C^2\), cubic on each cell, interpolates the supplied values, and has \(S_n''(0)=S_n''(n)=0\). No shape-adjustment or nonlinear slope limiter is applied. The norm is the map from the maximum absolute *nodal* value to the maximum continuous interpolant value. The positivity frontier concerns strictly positive nodal values with one global minimum and maximum, not monotone data, a nonuniform mesh, or positivity of derivatives.

## Proof

Let \(\vartheta=\operatorname{arcosh}2\), \(r=e^{-\vartheta}=2-\sqrt3\), and \(c=(\sqrt3-1)/2\). At the cell \(x=j+t\), \(0\le j<n\), \(0\le t\le1\), set \(k=n-1-j\) and
\[
 a=t(1-t)(2-t),\qquad b=t(1-t)(1+t).
\]
The nodal second derivatives \(m_i=S_n''(i)\) satisfy \(m_0=m_n=0\) and
\[
 m_{i-1}+4m_i+m_{i+1}=6(y_{i-1}-2y_i+y_{i+1}),\qquad 1\le i<n.
\]
The cell formula is
\[
 S_n(j+t)=(1-t)y_j+ty_{j+1}-\frac{am_j+bm_{j+1}}6.
\]
The inverse of the interior tridiagonal matrix has signed entries
\[
 G_{uv}=(-1)^{u+v}\frac{\sinh(\min(u,v)\vartheta)\sinh((n-\max(u,v))\vartheta)}{\sinh\vartheta\sinh(n\vartheta)},\qquad1\le u,v<n.
\]
Here and below an empty inverse is understood when \(n=1\). Substitution and a second difference in the data index show that the two central cardinal coefficients are positive; the other coefficients alternate in sign outward on each side. The positive multiplicative factors for the left and right tails involve respectively
\[
 a\sinh((k+1)\vartheta)-b\sinh(k\vartheta)>0,\qquad
 b\sinh((j+1)\vartheta)-a\sinh(j\vartheta)>0.
\]
Indeed \(a,b\ge0\), \(b/a\le2\), \(a/b\le2\) in the cell interior and \(\sinh((q+1)\vartheta)/\sinh(q\vartheta)>e^{\vartheta}>2\) for positive integers \(q\); the zero-index cases follow immediately. The checker independently reconstructs all signs via the matrix formula.

Summing precisely the negative cardinal weights on both tails yields the **exact** negative mass \(N(j,t,k)=N_L+N_R\), with
\[
 N_L=\frac{(\cosh(j\vartheta)-1)[a\sinh((k+1)\vartheta)-b\sinh(k\vartheta)]}{\sinh(n\vartheta)},
\]
\[
 N_R=\frac{(\cosh(k\vartheta)-1)[b\sinh((j+1)\vartheta)-a\sinh(j\vartheta)]}{\sinh(n\vartheta)}.
\]
Both formulae remain valid at endpoint cells. Writing \(N=aC_a+bC_b\), the coefficients are
\[
 C_a=\frac{(\cosh(j\vartheta)-1)\sinh((k+1)\vartheta)-(\cosh(k\vartheta)-1)\sinh(j\vartheta)}{\sinh((j+k+1)\vartheta)},
\]
\[
 C_b=\frac{(\cosh(k\vartheta)-1)\sinh((j+1)\vartheta)-(\cosh(j\vartheta)-1)\sinh(k\vartheta)}{\sinh((j+k+1)\vartheta)}.
\]
These two formulas are interchanged by swapping \(j,k\). We now establish the decisive all-boundary inequality
\[
 2C_a+C_b\le3c,\qquad C_a+2C_b\le3c.
\]
Set \(X=r^j\) and \(Y=r^k\), each in \((0,1]\). Replace hyperbolic functions by
\(\cosh(q\vartheta)=(r^{-q}+r^q)/2\) and \(\sinh(q\vartheta)=(r^{-q}-r^q)/2\).
A direct simplification gives a bidegree-\((2,2)\) polynomial
\[
 P(X,Y)=(3c-2C_a-C_b)(1-r^2X^2Y^2).
\]
In the tensor-product quadratic Bernstein basis \(\binom2iX^i(1-X)^{2-i}\binom2lY^l(1-Y)^{2-l}\), its coefficients (rows indexed by \(i=0,1,2\)) are exactly
\[
\begin{pmatrix}
0&\sqrt3-\frac32&\frac{9-5\sqrt3}2\\
\frac{\sqrt3}2&\frac{3(\sqrt3-1)}2&\frac{3(\sqrt3-1)}2\\
\frac{3-\sqrt3}2&\frac{3(\sqrt3-1)}2&27-15\sqrt3
\end{pmatrix}.
\]
Every entry is nonnegative, and all but the upper-left entry are positive. Thus \(P(X,Y)\ge0\) on the entire closed unit square, strictly positive for finite \(j,k\). Since \(1-r^2X^2Y^2>0\), the first bound follows; the second is its reflected counterpart.

Finally
\[
\begin{aligned}
N&=t(1-t)[(2-t)C_a+(1+t)C_b]\\
&=t(1-t)[(1-t)(2C_a+C_b)+t(C_a+2C_b)]\\
&\le3ct(1-t)\le\frac{3c}{4}.
\end{aligned}
\]
Because the spline reproduces constants, its cardinal weights sum to one, so their total absolute mass is \(1+2N\). This proves the upper norm bound. For \(j,k\to\infty\), the exact formulas give \(C_a,C_b\to c\); taking \(t=1/2\) proves sharpness. The Bernstein polynomial is strictly positive for every finite pair, proving nonattainment.

Given \(m\le y_i\le M\), the smallest interpolated value at each point is \(m-(M-m)N\): assign \(M\) to negative cardinal weights and \(m\) to the others. Thus \(m-(M-m)3c/4\ge0\) on every finite grid if and only if the ratio obeys \(M/m\le1+4/(3c)=(7+4\sqrt3)/3\). If the ratio is larger, choose \(j=k\) large enough that the exact negative mass at the midpoint exceeds \(m/(M-m)\), and use that same sign-extremizing data to obtain a negative interpolant. This also establishes sharpness and strict positivity at the limiting contrast on every finite grid.

## Verification

Run `python verify.py` using Python 3 and SymPy. The script symbolically checks the nine exact Bernstein coefficients, the sharp constants, and the identity between the closed negative-mass formulas and independently inverted tridiagonal natural-spline matrices at 315 rational test configurations. The unrestricted-grid statement is proved by the Bernstein argument above, not by these finite tests. No machine-assisted infinite proof certification is claimed.

## Relationship to prior work

Beatson and Chacko (1990/1992) studied numerical norms of eight spline methods, including natural cubics; their Table 3 explicitly gives natural-spline norm values approaching \(1.549038\), and their footnote attributes the **infinite cardinal** constant \((1+3\sqrt3)/4\) to earlier work cited as Powell. That infinite-lattice constant is **not claimed as new**. The claim here is the *sharp uniform all-finite-natural-grid inequality*, including natural endpoint effects, its strict finite-grid deficit, a finite-boundary positivity contrast valid for all lengths, and constructive failure beyond the contrast. The finite-grid bound does not follow solely from the numeric table; the explicit Bernstein certificate handles both finite boundaries. Bogdanov and Volkov (2019) discuss shape preservation and positivity conditions for classical cubic splines, but the inspected local criteria do not give this sharp universal ratio or the same all-length certificate. Aràndiga, Baeza, and Yáñez (2021) study monotonicity via nonlinear Hermite constructions rather than this unmodified natural interpolant.

## Limitations

No assertion is made for nonuniform grids, clamped/not-a-knot splines, smoothing or approximation accuracy. The supremal norm and positivity threshold are sharp over all finite grid lengths, but equality in the norm is not attained at a finite grid. Earlier infinite-grid norm results are explicit prior coverage and historical uniqueness of the all-finite-grid bound has not been independently established. Replaying the computation does not constitute an independent audit.

## References

1. R. K. Beatson and E. Chacko, *Which Cubic Spline Should One Use?* University of Canterbury report (1990); SIAM J. Sci. Stat. Comput. 13 (1992), 1009–1024. https://ir.canterbury.ac.nz/server/api/core/bitstreams/76c796a1-5524-4a10-8394-a0e93ecc05e5/content ; DOI: 10.1137/0913059.
2. V. V. Bogdanov and Yu. S. Volkov, *Shape-preservation conditions for cubic spline interpolation*, Mat. Tr. 22 (2019), 19–67. https://www.mathnet.ru/eng/mt347 ; DOI: 10.33048/mattrudy.2019.22.102.
3. F. Aràndiga, A. Baeza and D. F. Yáñez, *Monotone cubic spline interpolation for functions with a strong gradient*, arXiv:2102.11564, first submitted 2021-02-23. https://arxiv.org/abs/2102.11564.
4. V. T. Shevaldin and O. Y. Shevaldina, *Lebesgue Constant of Local Cubic Splines with Equally Spaced Nodes*, Numerical Analysis and Applications 10 (2017), 362–367. DOI: 10.1134/S1995423917040085.
