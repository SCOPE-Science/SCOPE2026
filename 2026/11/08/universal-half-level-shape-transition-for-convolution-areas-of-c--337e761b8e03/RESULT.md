# Universal half-level shape transition for convolution areas of co-oriented parallelograms

## Finding

For two planar parallelograms with a common unordered pair of edge-line directions and prescribed areas \(0<A\le B\), let \(\rho=B/A\). For \(0<\theta<1\), write
\[
K+_{\theta}L=\{z\in\mathbb R^2:|K\cap(z-L)|\ge\theta M(K,L)\},
\qquad M(K,L)=\max_z|K\cap(z-L)|.
\]
The exact sharp lower envelope over all such pairs is
\[
\boxed{\min_{K,L}|K+_{\theta}L|
=A\left(\rho+1+4\theta\log\theta+(1-2\theta)H_{\rho}(\theta)\right),}
\]
where
\[
H_{\rho}(\theta)=
\begin{cases}
2\sqrt\rho,&0<\theta\le\frac12,\\
\rho+1,&\frac12\le\theta<1.
\end{cases}
\]
At the common endpoint \(\theta=1/2\), the two formulas agree.

When \(\rho>1\), the equality shapes are completely classified. Match the two edge directions, let \(r,s>0\) be the corresponding edge-length ratios (larger-area member divided by smaller-area member), and note \(rs=\rho\). For \(0<\theta<1/2\), equality holds exactly when \(r=s=\sqrt\rho\), so the shapes are homothetic. For \(1/2<\theta<1\), equality holds exactly when \(\{r,s\}=\{1,\rho\}\): one edge span is shared, and the other carries all of the area ratio. At \(\theta=1/2\), equality holds exactly when \(\{r,s\}=\{u,\rho/u\}\) with \(1\le u\le\rho\). When \(\rho=1\), all minimizing pairs have matching edge spans, hence are translates of one another.

For \(\rho>1\), the minimized volume is continuous but has a strict derivative jump at the critical level:
\[
\boxed{\left.\frac{d}{d\theta}\min|K+_{\theta}L|\right|_{\theta=1/2+}
-\left.\frac{d}{d\theta}\min|K+_{\theta}L|\right|_{\theta=1/2-}
=-2A(\sqrt\rho-1)^2.}
\]
This is a universal first-order optimal-shape transition: its level does not depend on the prescribed area ratio.

## Assumptions and scope

All bodies are full-dimensional, compact Euclidean parallelograms in \(\mathbb R^2\), with the same *two unoriented edge directions*. They need not be rectangles, centered, or translates. Area means two-dimensional Lebesgue area. The only constrained quantities are the two positive areas and the common pair of directions. The threshold obeys \(0<\theta<1\). The conclusions are invariant under invertible affine maps and translation of the bodies.

## Proof

**1. Affine reduction.** Any pair with common edge directions is the image, under one invertible linear map and individual translations, of
\[
K=[0,1]^2,\qquad L=[0,r]\times[0,s],\qquad r,s>0,\quad rs=\rho\ge1.
\]
The normalization sets the smaller area to one. Invertible linear maps multiply intersection areas, their maxima, and convolution-body areas by the same absolute determinant, so the normalized threshold is unchanged. Interchanging the two bodies preserves the convolution body. The final area is multiplied back by \(A\).

**2. The one-dimensional overlap law.** Let \(w_a(z)=|[0,1]\cap([z-a,z])|\), and put \(m_a=\min\{1,a\}\), \(d_a=|1-a|\). The maximum of \(w_a\) is \(m_a\). It is attained on an interval of length \(d_a\); on each of the two remaining ramps it varies linearly between zero and \(m_a\), over length \(m_a\). Thus the pushforward of Lebesgue measure on the positive support of \(w_a/m_a\) is the atom \(d_a\delta_1\) together with continuous density \(2m_a\) on \((0,1)\).

The two-dimensional overlap is the product \(w_r(z_1)w_s(z_2)\), with maximum \(m_rm_s\). Consequently, denoting \(m_1=m_r\), \(m_2=m_s\) and \(d_1=d_r\), \(d_2=d_s\), the convolution-body area equals
\[
V_\theta(r,s)=d_1d_2+2(1-\theta)(m_1d_2+m_2d_1)
+4(1-\theta+\theta\log\theta)m_1m_2. \tag{1}
\]
Indeed, the two mixed plateau/ramp contributions each use \(\int_{\theta}^1du=1-\theta\); the two-ramp contribution uses
\[
\int_0^1\int_0^1\mathbf1_{uv\ge\theta}\,du\,dv
=\int_\theta^1\left(1-\frac\theta u\right)du
=1-\theta+\theta\log\theta.
\]
This is a direct exact area identity, not a limit or approximation.

**3. Excluding coordinatewise crossed ratios.** If \(0<r\le1\) and \(s=\rho/r\ge1\), substituting the minima and plateaux in (1) yields
\[
V_\theta(r,\rho/r)=\frac\rho r+(\rho+1)(1-2\theta)
+r(1+4\theta\log\theta).
\]
Differentiating with respect to \(r\) gives
\[
\frac{dV_\theta}{dr}=1+4\theta\log\theta-\frac\rho{r^2}<0,
\]
because \(\rho/r^2\ge1\) and \(\theta\log\theta<0\). Every such configuration with \(r<1\) is therefore strictly worse than the boundary \(r=1\). The case \(s<1\) is symmetric. If both ratios are at least one, necessarily \(1\le r\le\rho\) and \(s=\rho/r\). There is no nontrivial case with both ratios below one because \(rs=\rho\ge1\). Hence every minimizer lies in the compact coordinatewise nested interval \(1\le r\le\rho\).

**4. The optimization and all equality cases.** On that interval, formula (1) simplifies to
\[
V_\theta(r,\rho/r)=\rho+1+4\theta\log\theta
+(1-2\theta)\left(r+\frac\rho r\right). \tag{2}
\]
The function \(r+\rho/r\) has its unique minimum \(2\sqrt\rho\) at \(r=\sqrt\rho\), and its maximum \(\rho+1\) at the two endpoints \(r=1,\rho\) (strictly smaller at interior points if \(\rho>1\)). The sign of \(1-2\theta\) changes at exactly \(\theta=1/2\). This proves both branches, sharpness, and the complete minimizer classification.

The argument also provides exact nonnegative deficits *within the nested interval*. Below the transition,
\[
V_\theta(r,\rho/r)-V_{\min}
=(1-2\theta)\frac{(r-\sqrt\rho)^2}{r}.
\]
Above the transition,
\[
V_\theta(r,\rho/r)-V_{\min}
=(2\theta-1)\frac{(r-1)(\rho-r)}{r}.
\]
At the transition every nested ratio is minimizing, while all crossed configurations are strictly worse. Restoring the determinant factor \(A\) yields the stated area and deficits.

**5. The cusp.** On either side of \(1/2\) differentiate the corresponding explicit expression. Their smooth common term \(\rho+1+4\theta\log\theta\) cancels in the derivative difference. The right derivative minus the left derivative is
\[
-2A(\rho+1)+4A\sqrt\rho=-2A(\sqrt\rho-1)^2,
\]
strictly negative when the two prescribed areas differ. This completes the proof.

## Verification

The accompanying `verify.py` reconstructs the genuine interval-intersection functions and numerically integrates their superlevel sets using a logarithmic quadrature change of variables. It compares those independently integrated areas with formula (1) for reproducible pseudorandom cases and checks the phase-minimum and exact deficit identities across parameter grids. Run `python3 verify.py` with standard Python 3. Passing finite tests supports the algebra but is not a proof for all real dimensions or parameters; the proof above establishes the universal result.

## Relationship to prior work

Martín Goñi (2026) establishes sharp **unrestricted** lower bounds for \(\theta\)-convolution-body volume and equality for oppositely oriented simplices on a specified threshold interval. Those results do not classify minimizing pairs among *co-oriented parallelograms of separately fixed areas*. Alonso-Gutiérrez, Jiménez and Villa (2013), and Alonso-Gutiérrez and Martín Goñi (2024), supply the foundational definitions, affine framework, and general estimates. Gasparyan and Ohanyan (2014) explicitly compute the covariogram of **one parallelogram against its own translate**, not the optimizing generalized two-body convolution across distinct side-length ratios. The overlap-product formula (1) is elementary and not claimed as a novel general principle. The new proposed contribution is the sharp area-constrained minimization, complete equality phase diagram, and universal derivative cusp; definitive historical priority is not established.

## Limitations

The result concerns pairs with a common pair of edge directions, not arbitrary relative rotations or unrestricted planar convex bodies. The ordinary self-covariogram and standard one-dimensional overlap formulae are established background. There is no claim of a classification beyond this affine-parallelogram subclass, of independent validation, or of exhaustive historical priority. All numerical calculations are finite corroboration, not substitutes for the analytic proof.

## References

1. J. Martín Goñi, *Improved Brunn--Minkowski inequality for \(\theta\)-convolution bodies*, arXiv:2610.37066, first public 2026-10-27. https://arxiv.org/abs/2610.37066
2. D. Alonso-Gutiérrez, C. H. Jiménez, R. Villa, *Brunn--Minkowski and Zhang inequalities for convolution bodies*, arXiv:1112.4757 (2011 preprint); *Advances in Mathematics* 238 (2013), 50–69. https://arxiv.org/abs/1112.4757
3. D. Alonso-Gutiérrez, J. Martín Goñi, *Brunn--Minkowski Inequality for \(\theta\)-Convolution Bodies via Ball's Bodies*, *Journal of Geometric Analysis* 34 (2024), article 58. https://doi.org/10.1007/s12220-023-01508-2
4. A. Gasparyan, V. Ohanyan, *Covariogram of a Parallelogram*, *Journal of Contemporary Mathematical Analysis* 49 (2014), 194–206. https://doi.org/10.3103/S1068362314040050
5. J. Haddad, *On the volume of convolution bodies in the plane*, arXiv:2405.00212 (2024 preprint). https://arxiv.org/abs/2405.00212
