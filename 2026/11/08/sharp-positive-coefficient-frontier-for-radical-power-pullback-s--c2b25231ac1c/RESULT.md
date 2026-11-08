# Sharp positive-coefficient frontier for radical power-pullback springs

## Finding

Let \(m\ge2\) be an integer and \(p>0\). For the power-pullback spring family defined below, the entire odd restoring-force polynomial, of degree \(4m+1\), has **strictly positive coefficients if and only if**

\[
p>p_m:=\frac{1}{\left(\frac{3(m+1)}{m+3}\right)^{1/m}-1}.
\]

All coefficients are nonnegative exactly when \(p\ge p_m\). At the sharp boundary \(p=p_m\), the linear coefficient is zero and all the other odd-power coefficients are strictly positive. Below the boundary the linear coefficient is negative. The underlying energy-polynomial coefficients are log-concave at every parameter value. The threshold has asymptotics

\[
p_m=\frac{m}{\log3}+\frac{2}{(\log3)^2}-\frac12+O(m^{-1}).
\]

The result replaces the sufficient bound \(p\ge2m\) of Pillai's Corollary 2 with an exact necessary-and-sufficient frontier for every order. The paper's independently stated sharp \(m=2\) bound is recovered.

## Assumptions and scope

For \(m\in\mathbb Z\), \(m\ge2\), and \(p\in(0,\infty)\), put

\[
a=p^m,\quad b=(p+1)^m,\quad T(w)=(w+p)^m,\quad K=mp^{m+1}(b-a),
\]

\[
A_1(w)=\frac{T(w)-a}{w},\qquad A_2(w)=\frac{b-T(w)}{1-w},\qquad P_{m,p}(w)=\frac{(w+p)^2A_1(w)A_2(w)}{K}.
\]

Both quotients are polynomials of degree \(m-1\). Write \(P_{m,p}(w)=\sum_{j=0}^{2m}d_jw^j\), with \(d_{2m+1}=0\). The normalization gives \(d_0=1\) and \(d_j>0\) for all \(0\le j\le2m\). Define \(F_{m,p}\) from the normalized energy equation \((dy/du)^2=(1-y^2)P_{m,p}(y^2)\) by \(y''+F_{m,p}(y)=0\). Differentiating the energy identity gives

\[
F_{m,p}(y)=\sum_{j=0}^{2m}(j+1)(d_j-d_{j+1})y^{2j+1}.
\]

The claim is about **every coefficient** in this precisely normalized odd force, not stability of other orbits, arbitrary initial conditions, or generic polynomial oscillators. The source proves an explicit radical central periodic orbit for all these parameters; that source result is not claimed here.

## Proof

**1. Binomial coefficients and upper tails are log-concave.** Set \(c_j=\binom mjp^{m-j}>0\) for \(0\le j\le m\). Then \(c_{j+1}/c_j=(m-j)/((j+1)p)\) strictly decreases with \(j\). The coefficient sequence of \(A_1\) is \(c_1,\ldots,c_m\), so it is log-concave. The coefficient sequence of \(A_2\) is \(b_k=\sum_{j=k+1}^m c_j\) for \(0\le k\le m-1\). Write \(r_j=c_{j+1}/c_j\). For \(0\le k\le m-1\),

\[
\frac{b_k}{c_k}=\sum_{t=1}^{m-k}\prod_{s=0}^{t-1}r_{k+s}.
\]

All ratios \(r_j\) are positive and strictly decreasing, hence \(b_k/c_k>b_{k+1}/c_{k+1}\) for \(0\le k\le m-2\). For an interior \(k\), using \(b_{k-1}=c_k+b_k\) and \(b_k-b_{k+1}=c_{k+1}\), obtain

\[
b_k^2-b_{k-1}b_{k+1}=b_kc_{k+1}-c_kb_{k+1}>0.
\]

Thus \(A_2\)'s coefficients are log-concave as well (strictly at interior indices).

**2. Convolution gives log-concavity of the energy coefficients.** The product of generating polynomials corresponds to convolution of their coefficient sequences. Convolution of nonnegative log-concave sequences without internal zeroes is log-concave (Hoggar's convolution theorem, as documented by Johnson–Goldschmidt). Both \(A_1\) and \(A_2\) have positive contiguous coefficients. Consequently their product \(Q=A_1A_2=\sum q_jw^j\) has positive log-concave coefficients. The third factor \((w+p)^2\) has positive log-concave coefficients \((p^2,2p,1)\). Therefore the full sequence \((d_j)_{0\le j\le2m}\) is positive and log-concave:

\[
d_j^2\ge d_{j-1}d_{j+1}\qquad (1\le j<2m).
\]

In addition, its *first* interior inequality is strict. For unnormalized coefficients \(e_j=Kd_j\), write \(Q=q_0+q_1w+q_2w^2+\cdots\). Then \(e_0=p^2q_0\), \(e_1=p^2q_1+2pq_0\), and \(e_2=p^2q_2+2pq_1+q_0\), so

\[
e_1^2-e_0e_2=p^4(q_1^2-q_0q_2)+2p^3q_0q_1+3p^2q_0^2>0.
\]

Here \(q_0,q_1>0\), and \(q_1^2\ge q_0q_2\). Thus \(d_1^2>d_0d_2\) for every \(m,p\), including \(m=2\).

**3. Only the linear coefficient can bind.** Positivity and log-concavity imply that \(d_{j+1}/d_j\) is nonincreasing in \(j\). Since \(d_0=1\), if \(d_1<1\) then all differences \(d_j-d_{j+1}\), including the final \(d_{2m}-d_{2m+1}=d_{2m}\), are strictly positive. If \(d_1=1\), the strict initial inequality gives \(d_2<d_1\), and log-concavity forces all later differences to be strictly positive, while \(d_0-d_1=0\). If \(d_1>1\), the linear coefficient \(d_0-d_1\) is negative. Consequently the full sign classification reduces to the comparison of \(d_1\) with one.

**4. Exact threshold.** Differentiate the three factors of \(P\) logarithmically at \(w=0\). One has \(A_1(0)=mp^{m-1}\), \(A_1'(0)/A_1(0)=(m-1)/(2p)\), \(A_2(0)=b-a\), and \(A_2'(0)/A_2(0)=1-mp^{m-1}/(b-a)\). Thus

\[
d_1=P_{m,p}'(0)=1+\frac{m+3}{2p}-\frac{mp^{m-1}}{(p+1)^m-p^m}.
\]

Since \(p>0\), rearrangement yields

\[
d_1<1\ \Longleftrightarrow\ \left(1+\frac1p\right)^m<\frac{3(m+1)}{m+3}\ \Longleftrightarrow\ p>p_m.
\]

Both equalities and reversed inequalities follow identically, completing the necessary-and-sufficient classification.

**5. Asymptotics and low order.** Expanding \(\log(3(m+1)/(m+3))=\log3-2/m+O(m^{-2})\) and the reciprocal of the exponential gives \(p_m=m/\log3+2/(\log3)^2-1/2+O(m^{-1})\). At \(m=2\), \(p_2=(5+3\sqrt5)/4\), precisely the previously known ninth-force-order boundary. Since \(3(m+1)/(m+3)\ge9/5>e^{1/2}>(1+1/(2m))^m\) for every \(m\ge2\), the new frontier always satisfies \(p_m<2m\).

## Verification

The standalone script `verify_coefficients.py` implements the displayed factors by exact rational arithmetic. For \(2\le m\le18\), it checks eleven positive rational parameter values per order, positivity and log-concavity of all factor and full coefficient sequences, the exact formula for \(d_1\), the algebraic comparison with \(3(m+1)/(m+3)\), and the force-coefficient sign regime. Its completed run returned `VERIFY_OK exact_rational_checks=8479 m_range=2..18 positive_p_samples=11`. The all-\(m\), all-real-\(p>0\) assertion is proved above; finite tests do not establish it by themselves.

## Relationship to prior work

Pillai's arXiv:2610.37730v1, Theorem 3, defines the polynomial and explicitly solves its normalized central orbit. Its Corollary 2 proves strict positivity of all force coefficients for \(p\ge2m\), explicitly calls this sufficient but not necessary, and only separately establishes the sharp \(m=2\) boundary. The result here supplies an exact condition at every integer order \(m\ge2\), together with a structural log-concavity reduction. Hoggar's convolution theorem is an established tool, not a new theorem here. The new mathematical step is recognizing that the coefficients of the particular power pullback factor into log-concave binomial tails, and that a strictly positive quadratic factor makes a single linear-stiffness comparison decisive. Literature priority outside the inspected sources is not asserted.

## Limitations

The normalized spring need not have positive linear stiffness at or below the boundary; the radical design orbit itself continues to exist for every \(p>0\). The classification concerns signs of coefficients rather than phase-space dynamics beyond the source's explicit central orbit. It does not classify alternative pullbacks or other polynomial-spring families. A specialized, separately cited but apparently unavailable 2026 preprint, *Elementary quadratures of nonsquare polynomial springs*, could contain related material; no claim of having inspected that text is made. Generic log-concavity theorems are prior mathematics.

## References

1. U. Pillai, *Nonlinear springs with orbits in radicals: a solvability criterion*, arXiv:2610.37730v1, October 27, 2026; https://arxiv.org/html/2610.37730v1 (Theorem 3, Corollary 2, and Proposition 1).
2. O. Johnson and C. Goldschmidt, *Preservation of log-concavity on summation*, ESAIM: Probability and Statistics **10** (2006), 206–215; https://doi.org/10.1051/ps:2006008 (discussion of Hoggar's convolution theorem).
