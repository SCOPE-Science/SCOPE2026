# Exact original-time capture statistics and critical scaling in a max-plus negative-feedback oscillator

## Finding
Fix real parameters \(B>0\) and \(m>1\). The max-plus negative-feedback map is
\[
F_{m,B}(X,Y)=\bigl(Y,\,B-\max\{0,mX\}\bigr).
\]
Set \(d=(1-m)B<0\) and \(c=B/(m+1)\). Let \(\mathcal C\) be the attracting four-cycle through \((B,B)\), with points \((B,B),(B,d),(d,d),(d,B)\). For independent, uniformly distributed initial coordinates \((X,Y)\in(0,B)^2\), define the **first original-iteration capture time**
\[
N=\min\{n\ge0:F_{m,B}^{n}(X,Y)\in\mathcal C\}.
\]
Write \(r=1/m\). Then \(N\) is finite almost surely and, for every integer \(j\ge2\),
\[
\boxed{\Pr(N=2j-1)=(1-r)r^{j-2}(1-r^{j-2}),\qquad
\Pr(N=2j)=(1-r)r^{j-2}(1-r^{j-1}).}
\]
There is no mass at earlier times. In particular,
\[
\boxed{\mathbb E N=\frac{4m-1}{m-1},\qquad
\Pr(N\ \text{is odd})=\frac1{m+1}.}
\]
The physical-clock parity imbalance becomes maximal as \(m\to\infty\) and vanishes as \(m\downarrow1\). The sharp weak-limit law at the neutral boundary is
\[
\boxed{\lim_{m\downarrow1}\Pr\!\left(\frac{(m-1)N}{2}\le t\right)=(1-e^{-t})^2\quad(t\ge0).}
\]
Thus the rescaled capture time approaches the maximum of two independent unit exponential variables, not a single exponential; its limiting mean is \(3/2\). At exactly \(m=1\), every starting point in \((0,B)^2\) except the center belongs to a primitive four-cycle and no such interior point ever reaches the distinguished boundary four-cycle. The finite-capture regime therefore ends sharply at \(m=1\).

The same scalar reduction gives complete global deterministic capture geometry for \(m>1\): besides the fixed point \((c,c)\), the only periodic orbits are \(\mathcal C\) and the four-cycle through \((c,B)\). Every point having neither coordinate equal to \(c\) enters \(\mathcal C\) in finitely many steps; a point with exactly one coordinate equal to \(c\) instead enters the mixed four-cycle. This global orbit classification is included to identify precisely what the random capture law measures, but is not by itself the claimed new quantitative contribution.

## Assumptions and scope
All random variables refer to independent Lebesgue-uniform initial coordinates on the *open* square \((0,B)^2\). Time \(N\) counts **individual applications** of \(F_{m,B}\), not four-step Poincaré returns or applications of its scalar second iterate. Parameter \(m\) is strictly greater than one for the probability formulas, with a separate statement at \(m=1\). The event of starting with either coordinate exactly at \(c\) has zero planar probability; the complete deterministic description handles it explicitly. The results are exact for every real \(B>0\), \(m>1\), and every integer \(j\ge2\).

## Proof
**1. Exact decoupling.** Define \(h(u)=B-\max\{0,mu\}\). Direct composition gives
\[
F_{m,B}^{2k}(X,Y)=(h^k(X),h^k(Y)),\qquad
F_{m,B}^{2k+1}(X,Y)=(h^k(Y),h^{k+1}(X))
\]
for all integers \(k\ge0\). The scalar two-cycle is \(D=\{B,d\}\) because \(h(B)=d\) and \(h(d)=B\). For \(u>0\), the affine active branch is \(h(u)=B-mu\), centered at its unique positive fixed point \(c\). If a scalar trajectory beginning at \(u>0\) never enters the nonpositive half-line, then its deviations are \(h^k(u)-c=(-m)^k(u-c)\), which are unbounded in alternating sign unless \(u=c\). Such a trajectory cannot remain positive. If the initial point is nonpositive then its next image is \(B\), and if \(u\ge B\), either it is already \(B\) or it next enters the nonpositive half-line. It follows that each real scalar point other than \(c\) enters \(D\) in finitely many steps. A periodic planar point under \(F^{2k}=(h^k,h^k)\) must therefore have coordinates in \(D\cup\{c\}\); the four points in \(D^2\) form \(\mathcal C\), the four points with exactly one \(c\) form the second four-cycle, and \((c,c)\) is fixed. This proves the stated exhaustive orbit and basin classification.

**2. First scalar reset from a uniform position.** For \(u\in(0,B)\), let
\[
T(u)=\min\{t\ge1:h^t(u)\le0\}.
\]
For \(u\ne c\) this is finite. The points surviving \(n\) scalar steps with positive states form an open interval
\[
I_n=c+(-1/m)^n\bigl((0,B)-c\bigr),\qquad n\ge0.
\]
Indeed, before the first nonpositive iterate, \(h(u)=B-mu\) maps the positive continuation interval \((0,B/m)\) bijectively onto \((0,B)\), with inverse contraction of ratio \(-1/m\) centered at \(c\). Hence \(|I_n|=B/m^n\) and
\[
\Pr(T>n)=m^{-n},\qquad
\Pr(T=t)=(1-r)r^{t-1},\quad t\ge1.
\]
At the first nonpositive scalar value, one more application of \(h\) produces \(B\), while no earlier state lies in \(D\). Consequently the scalar first-hitting time
\[
q(u)=\min\{k\ge0:h^k(u)\in D\}
\]
satisfies \(q=T+1\) for Lebesgue-almost every \(u\in(0,B)\), and \(\Pr(q=j)=(1-r)r^{j-2}\) for \(j\ge2\), with \(\Pr(q\le j)=1-r^{j-1}\).

**3. Restore the original two-coordinate clock.** Let \(q_X,q_Y\) be the independent scalar first-hitting times. From the even/odd iterate formula, the first time at which *both* coordinates have entered the invariant scalar pair is exactly
\[
N=2\max\{q_X,q_Y\}-{\bf1}_{\{q_X>q_Y\}}.
\]
The subtraction by one is essential: when the original \(X\) scalar path is slower than the \(Y\) path, the first captured plane state occurs at an odd iterate. Thus for \(j\ge2\),
\[
\Pr(N\le2j)=(1-r^{j-1})^2,\qquad
\Pr(N\le2j-1)=(1-r^{j-1})(1-r^{j-2}).
\]
Subtract successive cumulative probabilities to obtain both boxed mass formulas. Independence also gives
\[
\Pr(q_X>q_Y)=\sum_{j\ge2}(1-r)r^{j-2}(1-r^{j-2})=\frac r{1+r},
\]
which is the probability that \(N\) is odd. Moreover,
\[
\mathbb E\max(q_X,q_Y)=2+\sum_{k\ge0}\bigl(2r^{k+1}-r^{2k+2}\bigr)
=2+\frac{2r}{1-r}-\frac{r^2}{1-r^2}.
\]
Using the formula for \(N\) and the strict-order probability yields
\[
\mathbb EN=2\mathbb E\max(q_X,q_Y)-\frac r{1+r}
=\frac{4-r}{1-r}=\frac{4m-1}{m-1}.
\]

**4. Critical scaling, with boundaries.** As \(m\downarrow1\), we have \(\log m\sim m-1\). For integer \(k\) of order \(t/(m-1)\), the even-time cumulative probability is \((1-m^{-(k-1)})^2\), so choosing the integer floor consistent with \((m-1)N/2\le t\) gives \((1-e^{-t})^2\) at every \(t>0\). The odd/even one-step ambiguity disappears under multiplication by \(m-1\). At \(t=0\) the probability is zero since \(N\ge4\). Uniform geometric tails also justify the limiting mean \(\lim_{m\downarrow1}(m-1)\mathbb EN/2=3/2\). At \(m=1\), \(h(u)=B-u\) on \((0,B)\), whence \(F^2(X,Y)=(B-X,B-Y)\) and \(F^4\) is the identity. The only interior fixed point is \((B/2,B/2)\), while all other interior points have least period four. None reaches the four boundary points of \(\mathcal C\). This proves the sharp singular transition.

## Verification
Run the self-contained standard-library checker `python3 checker.py` from this package. It tests 69,310 exact-rational identities, continuation intervals, scalar and original-time capture indices on a deterministic rational grid at five parameters and two forcing scales, together with finite-step cumulative-probability identities. Its numerical scope is explicitly finite; the four analytic proof steps establish the universally quantified theorem. A direct proof of the first-capture distribution does not rely on simulated trajectories, asymptotic regression, or independence incorrectly attributed to successive observations along one trajectory.

## Relationship to prior work
Ohmori and Yamazaki's 2023 negative-feedback study [1] identifies this exact max-plus model, the attracting and repelling four-cycles, and a piecewise-linear Poincaré section return map; its qualitative orbit pictures do not give the probability law for a planar-uniform initialization in **unaccelerated** time, its exact odd/even split, or the maximum-of-two-exponentials critical limit. Yamazaki and Ohmori's 2023 follow-up [2] explains the phase-lock relationship to tropically discretized limit cycles. Their 2024 generalized model [3] includes the present family as the parameter line with vanishing first-row feedback, and studies branches, limit-cycle state counts, and instability, not this square-initialization capture distribution. Earlier Gibo–Ito work [4] introduced ultradiscrete negative-feedback oscillators; the bibliographic abstract was accessible but its complete article was not available for comparison.

There is also a precise **affine-conjugate representation** \(G_m(u,v)=(1+v,-\max\{0,mu\})\), obtained by scaling \(X\) by \(B\) and replacing \(Y/B\) by \(v+1\). A previously derived geometric residence law for a *one-dimensional section* of that zero-determinant border-collision form concerns section-conditioned return counts, not planar-uniform initial conditions, unaccelerated capture, or the parity-dependent law here. This reduction and its prior section-level consequences are credited rather than treated as new. General first-return geometry for zero-determinant border collisions is discussed by Simpson [5,6].

## Limitations
The distribution requires independent uniform coordinates on \((0,B)^2\); it does not apply unchanged to a correlated prior or an invariant measure. The boundary at \(m=1\) is singular and the supercritical formula is not asserted there. This is a theorem about the exact max-plus model, not stability under smoothing or noise. The source's cyclic-orbit existence results and older section-specific geometric residence calculations are not claimed as discoveries. Further equivalences in unindexed or inaccessible literature remain possible; independent mathematical validation has not been performed.

## References
[1] S. Ohmori and Y. Yamazaki, *Dynamical properties of discrete negative feedback models*, arXiv:2305.05908, first public 2023-05-10. https://arxiv.org/abs/2305.05908

[2] Y. Yamazaki and S. Ohmori, *Emergence of ultradiscrete states due to phase lock caused by saddle-node bifurcation in discrete limit cycles*, arXiv:2306.00733 (2023). https://arxiv.org/abs/2306.00733

[3] S. Ohmori and Y. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230 (2024). https://arxiv.org/abs/2402.06230

[4] S. Gibo and H. Ito, *Discrete and ultradiscrete models for biological rhythms comprising a simple negative feedback loop*, J. Theor. Biol. 378 (2015), 89–95, DOI 10.1016/j.jtbi.2015.04.024.

[5] D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790 (2024). https://arxiv.org/abs/2408.04790

[6] D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901 (2026). https://arxiv.org/abs/2606.08901
