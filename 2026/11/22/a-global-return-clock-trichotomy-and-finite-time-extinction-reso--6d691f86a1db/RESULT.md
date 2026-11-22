# A global return-clock trichotomy and finite-time extinction resonance in a mixed-trace border-collision map

## Finding
For \(b>0\), \(r>0\), and \(d>r^2/4\), consider the continuous, positively homogeneous plane map
\[
F(x,y)=\begin{cases}(y-bx,0),&x\le0,\\(y+rx,-dx),&x>0.\end{cases}
\]
The left Jacobian has negative trace and zero determinant; the right Jacobian has positive trace and a nonreal conjugate eigenvalue pair. Define
\[
\rho=\sqrt d,\quad \theta=\arccos\!\left(\frac{r}{2\rho}\right)\in(0,\pi/2),\quad k=\left\lceil\frac{\pi}{\theta}\right\rceil,
\]
and the nonnegative and positive quantities
\[
A=-\rho^{k-1}\frac{\sin(k\theta)}{\sin\theta}\ge0,
\qquad B=\rho^k\frac{\sin((k-1)\theta)}{\sin\theta}>0.
\]
**Every** real initial state reaches either the origin or the positive horizontal ray in at most \(k+2\) steps. On that ray the complete first-return or extinction rule is
\[
\boxed{
\begin{array}{c|c|c}
\text{condition}&\text{first return/extinction time}&\text{return on }(u,0),\ u>0\\\hline
bA<B&k+1&(b(B-bA)u,0)\\
bA=B&k&(0,0)\\
bA>B&k&((bA-B)u,0).
\end{array}}
\]
The middle row is possible for some positive \(b\) **if and only if** \(\pi/\theta\notin\mathbb N\). It then occurs at the unique value \(b_*=B/A\), and yields **global exact finite-time extinction**:
\[
F^{2k+2}\equiv(0,0).
\]
Away from the extinction surface, put \(M=b(B-bA)\) and \(h=k+1\) in the first row, or \(M=bA-B\) and \(h=k\) in the last row. Then precisely:

- \(0<M<1\): the origin is globally exponentially attracting.
- \(M=1\): every trajectory is eventually either the zero orbit or a primitive period-\(h\) orbit. In fact each point of the positive horizontal ray starts such a period-\(h\) orbit.
- \(M>1\): every trajectory is either eventually zero or tends to infinity in norm.

These are statements about all initial points in \(\mathbb R^2\), not merely the subset of orbits obeying one prescribed symbolic word.

The exact integer-coefficient example \(r=1,d=3\) has \(k=3\), \(A=2\), \(B=3\), so its positive-ray return multiplier is \(b(3-2b)\) over \(0<b<3/2\) (period four), the whole plane is annihilated in finitely many steps at \(b=3/2\), and its multiplier is \(2b-3\) over \(b>3/2\) (period three). Three distinct neutral parameters occur at \(b=1/2,1,2\); an open interval \(1/2<b<1\) gives escape between two intervals of exponential attraction, and the finite-time extinction resonance separates the two return-clock lengths.

## Assumptions and scope
The parameters satisfy \(b,r,d>0\), \(4d>r^2\) and are fixed in any one iteration experiment. The switching line \(x=0\) uses the left formula, consistent with the right formula there; all real initial data are allowed. The right matrix has eigenvalues \(\rho e^{\pm i\theta}\) with \(0<\theta<\pi/2\). In the notation of the standard border-collision normal form, \(\mu=\delta_L=0\), \(\tau_L=-b\), \(\tau_R=r\), \(\delta_R=d\). The return time counts applications of the original planar map, not an accelerated induced-map clock. A trajectory "eventually zero" reaches \((0,0)\) at a finite integer time. The bound \(2k+2\) is a sufficient uniform annihilation bound, not asserted to be the minimal one for every parameter.

## Proof
**Step 1: Finite exit from the right focus branch.** While an orbit remains in \(x>0\), its first components satisfy
\[
x_{j+2}=rx_{j+1}-dx_j.
\]
For an arbitrary initial point with \(x_0>0\), there are \(C>0\) and \(\phi\in(0,\pi)\) for which its *prospective* right-branch first coordinates are
\[
x_j=C\rho^j\sin(\phi+j\theta).
\]
This follows by solving the second-order recurrence and writing its nonzero initial sine-cosine combination in amplitude-phase form; \(x_0>0\) fixes \(\phi\in(0,\pi)\). Let \(j\ge1\) be the first integer with \(\phi+j\theta\ge\pi\). Because \(\theta<\pi/2\), the sine cannot skip the nonpositive half-cycle at this first crossing; hence \(x_j\le0\), while every preceding first coordinate is positive. Moreover \(j\le k=\lceil\pi/\theta\rceil\). The state at that first exit satisfies \(y_j=-dx_{j-1}<0\), including when \(x_j=0\).

**Step 2: Uniform reduction to the positive axis.** At the exit from Step 1, the next, left, iterate is \((y_j-bx_j,0)\). If its first coordinate is positive, the positive ray has been reached. If it is negative, one more left iterate sends it to \((b|y_j-bx_j|,0)\), positive. If it vanishes, the state is the origin. This takes at most \(j+2\le k+2\) iterations. Initial points already in \(x\le0\) need at most two steps by the same left-branch sign rule: their first image is \((y-bx,0)\) and a negative value is made positive in the next step. This proves the uniform reduction claim, including all switching-line states.

**Step 3: Exact ray return.** From \((u,0)\) with \(u>0\), the right-branch recurrence has \(x_0=u\), \(x_1=ru\), hence
\[
x_j=u\rho^j\frac{\sin((j+1)\theta)}{\sin\theta}.
\]
Since \((k-1)\theta<\pi\le k\theta<\pi+\theta\), the coordinates \(x_0,\ldots,x_{k-2}\) are strictly positive but \(x_{k-1}\le0\). The accompanying second coordinate is \(y_{k-1}=-d x_{k-2}\). Therefore the state at the first right-to-left crossing is exactly
\[
F^{k-1}(u,0)=(-Au,-Bu).
\]
One left step gives \(F^k(u,0)=((bA-B)u,0)\). If this equals zero, ray extinction takes exactly \(k\) steps. If it is positive, this is the first return to the positive ray at time \(k\). If it is negative, one further left step yields \((b(B-bA)u,0)\), the first positive-ray return at time \(k+1\). All intermediate states have negative second coordinate throughout the right block, and the first nonpositive state also has negative second coordinate, so none lies on the positive horizontal ray before the stated return. Consequently a return with multiplier one has **least period** \(k\) or \(k+1\), rather than merely a period dividing that integer.

**Step 4: Existence and uniqueness of the extinction resonance.** The formula for \(A\) and the angular inequalities imply \(A=0\) exactly when \(k\theta=\pi\), equivalently \(\pi/\theta\in\mathbb N\). Otherwise \(A>0\). Since \(B>0\), the equation \(bA=B\) then has the single positive solution \(b=B/A\). At this gain every positive-ray state reaches zero in \(k\) steps; combining with Step 2 gives \(F^{2k+2}\equiv0\). Conversely, if \(bA\ne B\), the positive-ray state \((u,0)\) has multiplier \(M>0\) at every successive return and thus can never reach zero. Uniform finite-time annihilation is impossible; indeed that one state is never annihilated.

**Step 5: Complete global trichotomy.** For \(bA\ne B\), Step 3 gives for every \(u>0\)
\[
F^{jh}(u,0)=(M^ju,0),\qquad j\in\mathbb Z_{\ge0}.
\]
At the finitely many intermediate phases, the states are positive scalar multiples of a fixed nonzero list of vectors. If \(M<1\), all these phase norms vanish geometrically, and the bounded number of steps in Step 2, together with continuity and piecewise linear homogeneity, yields a **uniform global exponential estimate** \(\|F^n(z)\|\le C\sigma^n\|z\|\) for some \(C<\infty\), \(0<\sigma<1\) depending on the fixed parameters. If \(M=1\), each positive-ray state is periodic of least period \(h\), so every trajectory eventually reaches zero or such a cycle. If \(M>1\), all phase norms tend to infinity for every orbit that reaches the positive ray. These alternatives exhaust the full plane by Step 2.

Finally, when \(r=1,d=3\), the recurrence gives \((x_0,x_1,x_2)=(u,u,-2u)\), followed by \(y_2=-3u\); thus \(k=3\), \(A=2\), \(B=3\), and the exact example follows by substituting into the return formulas. In particular \(b(3-2b)=1\) holds precisely at \(b=1/2,1\), while \(2b-3=1\) holds at \(b=2\).

## Verification
The standalone script `check_focus_return.py` uses exact rational arithmetic to check the closed-form first-return law and uniform positive-ray reduction on full-plane grids for the integer-coefficient example, including exact finite extinction at its singular gain. It also draws reproducible random focus parameters and validates the trigonometric return formulas numerically with explicit tolerances. Running `python3 check_focus_return.py` prints `MIXED_TRACE_RETURN_VERIFY_OK`. The computations are finite regression checks; Steps 1–5 independently establish the theorem for every real parameter and initial condition.

## Relationship to prior work
Simpson's 2024 preprint [1] gives the zero-determinant border-collision normal form and studies forced parameter slices. Section 4.1 explicitly sets aside the exact unforced \(\mu=0\) case and notes the difficulty of deciding its origin stability. Neither the arbitrary-initial-condition finite reduction, the mixed-sign return multiplier, nor the global extinction/periodic/escape trichotomy is stated there.

Simpson's earlier homogeneous-map stability study [2] develops general angular-measure criteria and sufficient asymptotic-stability conditions, but its detailed noninvertible planar calculations in §6 explicitly exclude the case of a zero piece determinant by assuming \(\delta_L>0\) and \(\delta_R<0\). Its general framework does not give the stated exact induced-map clock, annihilation resonance or phase portrait. Simpson's 2026 return-map study [3] uses a nonzero forcing term \(\mu=1\), and thus its affine return intervals and Farey classification do not imply this homogeneous one-ray return formula.

A previous homogeneous max-plus classification [4] has vanishing left trace, rather than the strictly negative left trace used here. A separate five-step nilpotence result [5] assumes **both** traces are negative and uses a different two-step cancellation. Neither is a parameter specialization covering the present positive-right-focus / negative-left-trace quadrant. These full claims were compared by equations and implications, not merely their titles. General contraction of a scalar ray return is elementary; novelty is only claimed for the complete, parameter-explicit global dynamics of this mixed-trace normal-form subfamily. Equivalent results outside the inspected sources remain possible.

## Limitations
The theorem assumes \(b,r,d>0\), \(d>r^2/4\), \(\mu=\delta_L=0\) and exact piecewise linearity. It does not classify the right-node region \(d\le r^2/4\), signed determinants, nonzero forcing, smooth perturbations or stochastic switching. The global finite-extinction exponent \(2k+2\) is sufficient, not claimed universally minimal. At neutral multiplier one, the continuum of nonzero periodic orbits is not an isolated asymptotically stable cycle. The historical novelty comparison is finite and does not prove publication priority.

## References
1. D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1, first public 8 August 2024; later *SIAM Journal on Applied Dynamical Systems* 24 (2025), 2205–2245, DOI 10.1137/24M1683548. https://arxiv.org/abs/2408.04790
2. D. J. W. Simpson, *The stability of fixed points on switching manifolds of piecewise-smooth continuous maps*, arXiv:1612.02932v1, first public 9 December 2016; later *Journal of Dynamics and Differential Equations* 32 (2020), 1527–1552. https://arxiv.org/html/1612.02932v1
3. D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901v1, public 8 June 2026; later *Qualitative Theory of Dynamical Systems* 25 (2026), article 160. https://link.springer.com/article/10.1007/s12346-026-01576-z
4. *Sharp extinction and persistence at the homogeneous max-plus border collision*, mathematical result publicly recorded 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-extinction-and-persistence-at-the-homogeneous-max-plus-bor--a2b1d9a86864
5. *Sharp five-step extinction resonance in the zero-determinant border-collision map*, mathematical result publicly recorded 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-five-step-extinction-resonance-in-the-zero-determinant-bor--a76c8cea2c0d
