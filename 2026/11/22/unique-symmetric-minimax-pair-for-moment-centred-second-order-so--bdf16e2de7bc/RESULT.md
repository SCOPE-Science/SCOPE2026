# Unique symmetric minimax pair for moment-centred second-order Sobolev evaluation

## Finding

Let
\[
\mathcal H=\left\{f\in H^2(0,1;\mathbb R):\int_0^1 f(u)\,du=\int_0^1 u f(u)\,du=0\right\},
\qquad \|f\|_{\mathcal H}^2=\int_0^1|f''(u)|^2\,du.
\]
For two distinct observation points \(0\le x<y\le1\), put
\[
\Lambda(x,y)=\sup_{f\in\mathcal H\setminus\{0\}}
\frac{|f(x)|^2+|f(y)|^2}{\int_0^1|f''(u)|^2\,du}.
\]
There is exactly one minimizing **unordered** pair, namely
\[
\{x_*,y_*\}=\left\{\frac12-d_*,\frac12+d_*\right\},
\quad d_*=0.30080451499127222856\ldots,
\]
where \(d_*\) is the unique root in \((0.3008,0.301)\) of
\[
1344d^6-3920d^4+4480d^3-1236d^2+21=0.
\]
At this pair the two point-evaluation Riesz representers are orthogonal and have equal squared norm, and the exact sharp value is
\[
\boxed{\min_{0\le x<y\le1}\Lambda(x,y)=
\frac{3-120d_*^2+320d_*^3-80d_*^4}{480}
=0.00040982270636359294785\ldots.}
\]
The corresponding operator norm is \(0.02024407830363222409\ldots\). Every nonzero function whose second derivative belongs to the two-dimensional span of the two optimal Riesz kernels attains the sharp fixed-pair inequality, and these are all equality functions.

## Assumptions and scope

All functions and coefficients are **real**. The two integral constraints select the \(L^2(0,1)\)-orthogonal complement of affine functions, making the second-derivative seminorm a Hilbert norm. Evaluation is of a function itself, not of its derivative. Points may be at endpoints; the theorem optimizes the *largest* squared simultaneous observation norm, with equal unit weights on both observations. The only constraints on the two positions are their distinctness and membership in \([0,1]\).

## Proof

**1. Riesz representers and an exact Gram reduction.** For \(g=f''\in L^2(0,1)\), the fundamental theorem of calculus gives
\[
f(x)=a+bx+\int_0^1(x-u)_+g(u)\,du.
\]
Define \(h_0(u)=(1-u)^2/2\) and \(h_1(u)=1/3-u/2+u^3/6\). Solving the two moment constraints for \(a,b\) yields
\[
f(x)=\int_0^1 K_x(u)g(u)\,du,\quad
K_x(u)=(x-u)_++(6x-4)h_0(u)+(6-12x)h_1(u).
\]
Every \(g\in L^2\) determines precisely one \(f\in\mathcal H\), so this representation is surjective. Set \(G(x,y)=\int_0^1K_x(u)K_y(u)\,du\). The Hilbert-space singular-value identity gives
\[
\Lambda(x,y)=\lambda_{\max}\begin{pmatrix}G(x,x)&G(x,y)\\G(x,y)&G(y,y)\end{pmatrix}.
\]
Writing \(t=x(1-x)\), direct polynomial integration gives
\[
g_0(x):=G(x,x)=\frac{21t^3+28t^2-11t+1}{105}.
\]
For \(0\le x\le y\le1\), the complete off-diagonal polynomial is
\[
\begin{aligned}
420G(x,y)=-(&42x^5y-21x^5-105x^4y+70x^4\\
&+42xy^5-105xy^4+210xy^2-156xy\\
&+22x-21y^5+70y^4-70y^3+22y-4).
\end{aligned}
\]
These formulas result from integrating the product of the stated kernels separately over \([0,x]\), \([x,y]\), and \([y,1]\); `check.py` independently repeats this symbolic integration.

**2. Symmetric/antisymmetric Rayleigh lower bounds.** Write \(c=(x+y)/2\), \(d=(y-x)/2\), and \(h=c-1/2\). Let
\[
A(c,d)=\tfrac12\|K_x+K_y\|_2^2,\qquad
B(c,d)=\tfrac12\|K_x-K_y\|_2^2.
\]
Testing the Gram matrix against \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\) gives \(\Lambda(x,y)\ge\max\{A(c,d),B(c,d)\}\). At the centred pair \(c=1/2\), the diagonal Gram entries coincide, so equality holds and
\[
A_0(d)=\frac{3-120d^2+320d^3-80d^4}{480},\qquad
B_0(d)=\frac{d^2(99-560d+840d^2-336d^4)}{840}.
\]
Exact expansion of the Gram polynomials gives
\[
\begin{aligned}
A(c,d)-A_0(d)&=-\frac{h^2}{840}\left[1680d^4-1680d^2+111
+(3360d^2-700)h^2+336h^4\right],\\
B(c,d)-B_0(d)&=\frac{d^2(2h)^2}{8}(6-8d^2-4h^2).
\end{aligned}
\]
The second difference is strictly positive for every feasible off-centre pair with \(d>0\), since \(d\le1/2\), \(|h|\le1/2-d\) and the final factor is positive.

**3. A rational confinement certificate.** Put \(U=41/100000\). At the centred half-gap \(d_0=188/625=0.3008\), exact rational evaluation gives \(A_0(d_0)<U\) and \(B_0(d_0)<U\); hence a global optimizer must have \(\Lambda\le U\). Each observation separately has squared evaluation norm at most \(\Lambda\), so \(g_0(x),g_0(y)\le U\).

The identity
\[
g_0'(x)=-\frac{2x-1}{105}(63x^4-126x^3+7x^2+56x-11)
\]
and the factorization of the quartic derivative
\[
14(2x-1)(3x-4)(3x+1)
\]
show that \(g_0\) decreases and then increases on \([0,1/2]\), with exactly one interior minimum, and is reflected about \(1/2\). Exact rational evaluation gives \(g_0(39/200)>U\) and \(g_0(9/40)>U\). Therefore any observation satisfying \(g_0\le U\) lies in
\[
I_L=[39/200,9/40]=[0.195,0.225]\quad\text{or}\quad
I_R=[31/40,161/200]=[0.775,0.805].
\]
Both sites cannot lie in the same interval. Indeed, on either interval \(g_0\ge1/3000\): on \(I_L\), set \(r=x(1-x)-1/6\) so \(|r|<1/100\), and use
\[
105g_0(x)=1/24+r/12+(77/2)r^2+21r^3
\ge1/24-1/1200-21/10^6>105/3000.
\]
Reflection gives the other interval. Furthermore
\[
\|\partial_xK_x\|_2^2=13/35-x+2x^3-x^4<1/5
\]
on both intervals (by reflection and monotonicity). For \(x,y\) in the same interval, \(|x-y|\le3/100\) therefore
\[
A(c,d)=g_0(x)+g_0(y)-\tfrac12\|K_x-K_y\|_2^2
\ge\frac2{3000}-\frac9{100000}>U,
\]
a contradiction. Thus exactly one site lies in each interval and
\[
\frac{11}{40}\le d\le\frac{61}{200},\qquad |h|\le\frac3{200}.
\]

**4. Global symmetrization and the unique collision of spectral modes.** On this confined rectangle, the bracket in the expression for \(A-A_0\) is negative: its \(h=0\) part \(1680d^4-1680d^2+111\) decreases in \(d\) and is less than \(-6\) at \(d=11/40\); the coefficient \(3360d^2-700\) is negative; and \(336h^4\le336(3/200)^4<6\). Consequently \(A(c,d)\ge A_0(d)\), strictly unless \(h=0\). The earlier identity gives \(B(c,d)\ge B_0(d)\), also strictly unless \(h=0\).

On the confined interval, \(B_0\) is strictly decreasing: its derivative is
\[
B_0'(d)=-\frac d{140}(336d^4-560d^2+280d-33),
\]
and the quartic in parentheses is positive there (its second derivative is negative and its two endpoint values are positive). Moreover, \(A_0\) is strictly increasing for \(d\ge0.3008\), since
\[
A_0'(d)=-\frac d6(4d^2-12d+3)>0.
\]
The difference satisfies
\[
A_0(d)-B_0(d)=\frac{1344d^6-3920d^4+4480d^3-1236d^2+21}{3360}.
\]
Its sign is negative at \(0.3008\) and positive at \(0.301\); the stated monotonicities give exactly one crossing \(d_*\) in that interval. If \(d<d_*\), then \(B_0(d)>B_0(d_*)\); if \(d>d_*\), then \(A_0(d)>A_0(d_*)\). For any off-centre pair, one of the Rayleigh inequalities is strict. The global minimum is therefore unique, centred, and occurs at \(d_*\).

**5. Equality functions.** At the optimal pair \(G(x_*,x_*)=G(y_*,y_*)=A_0(d_*)\) and \(G(x_*,y_*)=0\) because \(A_0(d_*)=B_0(d_*)\). Thus the two Riesz kernels form an orthogonal, equal-norm pair. Equality in the Hilbert-space norm inequality holds exactly when \(f''\) is a nonzero linear combination of these two kernels; the two moment constraints then uniquely determine \(f\). This proves the claimed full equality classification.

## Verification

`check.py` uses exact SymPy polynomial integration to reconstruct the kernel and all Gram identities. It asserts the rational confinement inequalities and spectral crossing signs, calculates the algebraic root to high precision, and compares 1,830 distinct rational-grid configurations as additional *finite* corroboration. Run `python3 check.py` with Python 3 and SymPy installed. The polynomial bounds and calculus argument above—not the finite grid or numerical root—prove global optimality and uniqueness.

## Relationship to prior work

The archived paper by Estévez develops equivalent trace norms and quasi-optimal linear spline extensions for first- and second-order Sobolev classes on arbitrary node sequences. It does not give this exact two-point operator norm, equal-moment normalization or free-node global minimax location. Davydov–Schaback study approximation rates and optimal stencil construction for Sobolev functionals; their error/rate optimization differs from minimizing a simultaneous value-evaluation operator norm. Their framework motivates considering point observations and Sobolev energy but does not imply the present algebraic two-point design. Standard finite Gram-matrix spectral methods alone do not solve the unrestricted node-placement problem: the essential new step is a global rational confinement followed by two positive centring deficits and spectral-mode equalization.

## Limitations

The result concerns exactly two **equal-weight** evaluations on a fixed interval, second-derivative energy, and the two specified moment constraints. The minimizing arrangement need not remain optimal with unequal weights, different moment complements, more nodes, alternative boundary conditions, or different Sobolev orders. The location is specified by a unique real algebraic root rather than radicals. An unindexed historical equivalent or an unstated corollary of other exact sampling-design work remains a priority risk; no independent audit has been performed.

## References

1. D. Estévez, *Explicit traces of functions on Sobolev spaces and quasi-optimal linear interpolators*, arXiv:1211.1498, publicly submitted 2012-11-07, https://arxiv.org/abs/1211.1498.
2. O. Davydov and R. Schaback, *Optimal Stencils in Sobolev Spaces*, arXiv:1611.04750, publicly submitted 2016-11-15, https://arxiv.org/abs/1611.04750.
