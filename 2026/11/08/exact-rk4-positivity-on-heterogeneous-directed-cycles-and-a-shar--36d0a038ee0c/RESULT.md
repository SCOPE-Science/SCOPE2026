# Exact RK4 positivity on heterogeneous directed cycles and a sharp CFL gain

## Finding

On a directed one-way cycle with arbitrary positive, vertex-dependent rates, the classical four-stage, fourth-order Runge--Kutta endpoint is entrywise nonnegative on exactly one closed interval of timesteps. The endpoint is determined only by adjacent-rate cubics and sums of four consecutive rates; two-jump entries never constrain positivity. The exact classification yields a four-maximal-rate plateau criterion for strict improvement over forward Euler, a sharp universal gain factor, and a sharp phase change for a single rate defect.

Let \(n\ge5\), with indices modulo \(n\), and let \(r_i>0\). Use the row generator
\[
Q_{ii}=-r_i,\qquad Q_{i,i+1}=r_i,\qquad Q_{ij}=0\quad\text{otherwise},
\]
and the RK4 transition polynomial
\[
T(h)=I+hQ+\frac{h^2Q^2}{2}+\frac{h^3Q^3}{6}+\frac{h^4Q^4}{24},\qquad h\ge0.
\]
For \(a,b>0\), define
\[
F_{a,b}(h)=1-\frac{a+b}{2}h+\frac{a^2+ab+b^2}{6}h^2
-\frac{a^3+a^2b+ab^2+b^3}{24}h^3,
\]
and let \(\vartheta(a,b)\) be its unique positive zero. Set
\[
W=\max_{i\in\mathbb Z/n\mathbb Z}\sum_{j=0}^3r_{i+j},\qquad
h_*=\min\left\{\min_i\vartheta(r_i,r_{i+1}),\frac4W\right\}.
\]
**The sharp positivity theorem** is
\[
\boxed{T(h)\ge0\ \text{entrywise}\quad\Longleftrightarrow\quad 0\le h\le h_* .}
\]
There is no positivity reentry after \(h_*\). Every diagonal entry and every entry at forward distance two or four is strictly positive for all \(h>0\). Only entries at forward distance one or three can turn negative.

With \(M=\max_i r_i\), the forward-Euler positivity step is \(h_{\rm FE}=1/M\). The sharp structural criterion is
\[
\boxed{h_*>h_{\rm FE}\quad\Longleftrightarrow\quad
\text{no four consecutive vertices all have rate }M.}
\]
Let \(\alpha\) be the unique positive root of
\[
1-\frac z2+\frac{z^2}{6}-\frac{z^3}{24}=0,
\qquad\alpha=2.7852935634052818\ldots .
\]
For every finite cycle with positive rates, \(1\le Mh_*<\alpha\), and the upper constant is the sharp supremum over admissible rates and sizes. The left equality occurs precisely when a four-rate maximum plateau exists.

For a single high-rate defect \(r_0=R\ge1\), \(r_1=\cdots=r_{n-1}=1\), define \(R_c\) as the unique root on \([1,\infty)\) of
\[
3R^3-9R^2-15R-43=0,\qquad R_c=4.70845296658594\ldots .
\]
Then
\[
\boxed{h_*(R)=
\begin{cases}
4/(R+3),&1\le R\le R_c,\\
\vartheta(R,1),&R\ge R_c,
\end{cases}}
\]
with equality of branches at \(R_c\), and \(\lim_{R\to\infty}R h_*(R)=\alpha\). Hence the controlling negativity switches from a three-jump to a one-jump entry at the exact defect contrast \(R_c\).

## Assumptions and scope

The cycle has at least five states, every rate is strictly positive and finite, and the update is the *unmodified* classical RK4 stability polynomial for the autonomous linear equation with generator \(Q\). Probabilities are row vectors evolved by multiplication on the right. The theorem concerns componentwise positivity for every nonnegative initial row vector; because \(Q\mathbf1=0\), stochastic row sums are preserved for all steps. It asserts no analogous sharp classification for cycles with fewer than five states, multistage positivity, time-varying generators, nonlinear systems, or numerical floating-point arithmetic.

## Proof

**1. Exact walk expansion.** For a starting state \(i\), a length-\(j\) term in \(Q^j\) contains a sequence of diagonal stays and forward jumps. If exactly \(k\) jumps occur, the destination is \(i+k\) and \(j=k+\ell\). Since \(j\le4<n\), no path wraps around and returns to its starting state. Diagonal stays can be distributed among the \(k+1\) visited vertices. Consequently, writing \(h_\ell\) for the complete homogeneous symmetric polynomial of degree \(\ell\),
\[
(Q^{k+\ell})_{i,i+k}=(-1)^\ell
\left(\prod_{u=0}^{k-1}r_{i+u}\right)
 h_\ell(r_i,\ldots,r_{i+k}),\qquad 1\le k\le4,
\]
whenever \(k+\ell\le4\). For \(k=0\), \((Q^j)_{ii}=(-r_i)^j\) up to order four. All entries at other forward distances are zero.

Let \(a=r_i\), \(b=r_{i+1}\); for the two-jump entry let \(c=r_{i+2}\). Direct substitution gives the five possible types:
\[
\begin{aligned}
T_{ii}(h)&=1-hr_i+\tfrac12h^2r_i^2-\tfrac16h^3r_i^3+\tfrac1{24}h^4r_i^4,\\
T_{i,i+1}(h)&=haF_{a,b}(h),\\
T_{i,i+2}(h)&=h^2ab\left[\tfrac12-\tfrac{a+b+c}{6}h
+\tfrac{a^2+b^2+c^2+ab+ac+bc}{24}h^2\right],\\
T_{i,i+3}(h)&=\frac{h^3r_ir_{i+1}r_{i+2}}{24}
\left[4-h\sum_{j=0}^3r_{i+j}\right],\\
T_{i,i+4}(h)&=\frac{h^4r_ir_{i+1}r_{i+2}r_{i+3}}{24}.
\end{aligned}
\]

**2. The only two obstructions.** The diagonal polynomial is strictly positive for \(h>0\): it is the fourth Taylor truncation of \(e^{-z}\), which exceeds \(e^{-z}\) for \(z>0\) by the positive fifth-order Taylor remainder. The distance-four entry is strictly positive for \(h>0\). For distance two, put \(s=a+b+c\) and \(H_2=(s^2+a^2+b^2+c^2)/2\). The bracket's quadratic discriminant is
\[
\frac{s^2}{36}-\frac{H_2}{12}
=-\frac{s^2+3(a^2+b^2+c^2)}{72}<0,
\]
and its leading coefficient is positive, so it is strictly positive for all real \(h\). The distance-three entry changes sign once at the explicit step \(4/(r_i+r_{i+1}+r_{i+2}+r_{i+3})\).

For distance one, the derivative of \(F_{a,b}\) is
\[
F'_{a,b}(h)=-\frac{a+b}{2}+\frac{a^2+ab+b^2}{3}h
-\frac{a^3+a^2b+ab^2+b^3}{8}h^2.
\]
It is everywhere strictly negative because its quadratic discriminant has the sign of
\[
4(a^2+ab+b^2)^2-9(a+b)(a^3+a^2b+ab^2+b^3)
=-[5a^4+10a^3b+6a^2b^2+10ab^3+5b^4]<0.
\]
As \(F_{a,b}(0)=1\) and \(F_{a,b}(h)\to-\infty\), there is exactly one positive root \(\vartheta(a,b)\), and the one-jump entry is nonnegative exactly up to it. Intersecting these necessary and sufficient entrywise conditions proves the sharp formula, including nonreentry.

**3. Forward-Euler improvement and the four-plateau criterion.** Substituting \(h=2/(a+b)\) gives the exact identity
\[
F_{a,b}\left(\frac2{a+b}\right)=\frac13>0,
\]
so \(\vartheta(a,b)>2/(a+b)\ge1/M\). Also \(W\le4M\), with equality exactly when four consecutive rates are all \(M\). Thus \(4/W\ge1/M\), with equality exactly in this plateau case, proving both the forward-Euler inequality and its sharp strictness criterion.

**4. The universally optimal gain constant.** Let \(i\) have \(r_i=M\). If \(T(h)\) is nonnegative, then its stochastic row sum one forces \(T_{ii}(h)\le1\). Set \(z=Mh\) and \(G(z)=1-z/2+z^2/6-z^3/24\). Since
\[
T_{ii}(h)=1-zG(z),
\]
this gives \(G(z)\ge0\). The derivative \(G'(z)=-1/2+z/3-z^2/8\) is negative for all real \(z\) (negative discriminant, negative leading coefficient), so \(G\) has a unique positive root \(\alpha\), and \(z\le\alpha\). Equality is impossible: the same row would have diagonal one and a strictly positive distance-four entry. Hence \(Mh_*<\alpha\). Sharpness follows from part 5.

**5. One-defect phase transition and sharpness.** For \(R\ge1\) and all remaining rates one, \(W=R+3\). The only two types of one-jump pairs are \((R,1)\) and \((1,1)\), and \(\vartheta(1,1)>1\ge4/(R+3)\). Thus \(h_*(R)=\min\{4/(R+3),\vartheta(R,1)\}\). Exact substitution gives
\[
F_{R,1}\left(\frac4{R+3}\right)
=-\frac{3R^3-9R^2-15R-43}{3(R+3)^3}.
\]
The cubic in the numerator decreases then increases on \([1,\infty)\), is negative at one and positive at five, and has a unique root \(R_c\) in that domain. As \(F_{R,1}\) is strictly decreasing, the sign gives the asserted phase classification. For fixed \(z\),
\[
F_{R,1}(z/R)\longrightarrow G(z)
\qquad(R\to\infty),
\]
and uniqueness of the positive roots gives \(R\vartheta(R,1)\to\alpha\). For \(R>R_c\), \(h_*(R)=\vartheta(R,1)\); thus \(Rh_*(R)\to\alpha\) and the universal gain constant cannot be improved.

## Verification

The supplied standalone \(\texttt{verify.py}\) uses only Python 3's standard library. Its direct exact-rational matrix-power replay compares the five closed entry formulas against the independently assembled RK4 matrix: 14,200 exact entry comparisons and 1,800 exact stochastic-row comparisons across cycle lengths five through ten. A separate 1,200-case floating-point two-sided boundary stress check finds positivity below the formula's threshold and a negative entry just above it. Six exact single-defect phase identities and numerical isolation of \(R_c\) and \(\alpha\) also pass. Run \(\texttt{python3 verify.py}\). These experiments do not establish the universal statements: the signed-polynomial proofs above do.

## Relationship to prior work

Gottlieb, Shu and Tadmor (2001) develop high-order SSP linear time-stepping and establish the forward-Euler-scale positivity/stability baseline, rather than a sharp heterogeneous directed-cycle endpoint classification. Horváth (2005) treats RK positivity step-size conditions on classes of positive IVPs and invariant cones. Horváth, Song and Terlaky (2015) give general polynomial-root sufficient bounds for Taylor-type invariance-preserving discretizations, but do not identify the five entry classes, an exact local-rate formula, absence of positivity reentry, a four-rate plateau criterion, or the sharp universal gain for directed cycles. Blanes, Iserles and Macnamara (2021) motivate positivity for nonsymmetric graph generators and study positivity-preserving integrators, not this RK4 classification. Generic finite-matrix testing and polynomial root algorithms should not be mistaken for a closed parametric classification across every cycle length and all positive rate vectors.

## Limitations

The theorem is restricted to positive one-way cycle rates, \(n\ge5\), and a single linear RK4 endpoint, not positivity of intermediate RK stages. The upper gain factor is a supremum approached by unbounded rate contrast, never attained when all rates remain positive. Numerical tests cover finite samples and are supplementary to the analytic proof. This result does not settle publication priority against all uncatalogued specialist literature; the literature comparison is necessarily bounded.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review **43** (2001), 89–112, first published electronically 2001-02-02. https://doi.org/10.1137/S003614450036757X ; full text https://drum.lib.umd.edu/bitstreams/faa96f40-0fbb-4af0-84a3-5e3b80c908df/download
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356. https://doi.org/10.1016/j.apnum.2004.08.026
3. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, Discrete and Continuous Dynamical Systems **35** (2015), 2997–3019. https://doi.org/10.3934/dcds.2015.35.2997 ; full text https://optimization-online.org/wp-content/uploads/2016/07/5534.pdf
4. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models*, 2021. https://arxiv.org/abs/2102.08242
