# Sharp existence boundary for antiphase two-cycles in planar Ricker competition

## Finding
For the positive two-species Ricker map
\[
T(x,y)=\left(rxe^{-x-\alpha y},\;sye^{-\beta x-y}\right),
\]
there is a strictly antiphase primitive two-cycle if and only if
\[
X>2,\qquad Y>2,\qquad
\alpha\beta<\left(1-\frac2X\right)\left(1-\frac2Y\right),
\]
provided \(\alpha\beta\ne1\) and \((X,Y)\) is the positive coexistence equilibrium. "Antiphase" means that one species is larger at the first point while the other is smaller, and both inequalities reverse at the second point. Equality does not produce an antiphase two-cycle.

In the regime \(X,Y>2\), the product threshold equals the zero of the equilibrium's \(-1\) characteristic factor:
\[
\det(I+DT(X,Y))=XY\left[\left(1-\frac2X\right)\left(1-\frac2Y\right)-\alpha\beta\right].
\]
Moreover, along any family with \(X,Y\) held fixed and \(\alpha\beta\) increasing to this threshold, the amplitudes of every antiphase two-cycle vanish. This is an existence statement, not a claim of uniqueness, stability, or global attraction.

## Assumptions and scope
All parameters \(r,s,\alpha,\beta\) are positive real numbers. Assume \(\alpha\beta\ne1\) and a positive fixed point \((X,Y)\) exists. Then \((X,Y)\) is uniquely specified by
\[
X+\alpha Y=\log r,\qquad \beta X+Y=\log s.
\]
The domain is the strictly positive quadrant and the dynamics is discrete-time; a primitive two-cycle has two distinct strictly positive points. The antiphase condition requires strict opposite directions of variation in its two coordinates. The statement excludes the singular coefficient matrix \(\alpha\beta=1\) and says nothing about in-phase cycles or higher periods.

## Proof
**Midpoint reduction.** Write the two cycle points as \((x_0,y_0)\) and \((x_1,y_1)\). Sum the logarithmic ratio of the first component over one full cycle; it gives
\[
x_0+x_1+\alpha(y_0+y_1)=2\log r.
\]
The same calculation in the second component gives
\[
\beta(x_0+x_1)+y_0+y_1=2\log s.
\]
As \(1-\alpha\beta\ne0\), the midpoint is exactly \((X,Y)\). Orient any antiphase cycle so that the first point is \((X+u,Y-w)\) and the second \((X-u,Y+w)\), where \(0<u<X\), \(0<w<Y\). Define for \(0<t<L\)
\[
U_L(t)=t-2\operatorname{arctanh}(t/L).
\]
The two forward cycle equations, with the equilibrium identities substituted, are **equivalent** to
\[
U_X(u)=\alpha w,\qquad U_Y(w)=\beta u.\tag{1}
\]
Indeed \(\log((X-u)/(X+u))=-2\operatorname{arctanh}(u/X)\) and \(\log((Y+w)/(Y-w))=2\operatorname{arctanh}(w/Y)\). The reverse transition follows by reversing these logarithmic ratios and replacing the centered displacements by their negatives. Thus every solution of (1) in the positive open amplitude rectangle gives a genuine antiphase cycle.

**Shape lemma.** Direct differentiation yields
\[
U_L'(t)=1-\frac{2L}{L^2-t^2},\qquad
U_L''(t)=-\frac{4Lt}{(L^2-t^2)^2}<0\quad(0<t<L).
\]
When \(L\le2\), \(U_L(t)<0\) for all \(t>0\). When \(L>2\), let \(c_L=1-2/L>0\). Strict concavity, \(U_L'(0)=c_L\), and \(U_L(t)\to-\infty\) as \(t\uparrow L\) imply that there is a unique \(s_L\in(0,L)\) with \(U_L(s_L)=0\). On \((0,s_L)\),
\[
0<\frac{U_L(t)}t<c_L,
\]
and \(U_L\) is positive; on \((s_L,L)\) it is negative.

**Necessity.** In (1), both right-hand sides are strictly positive, so the shape lemma forces \(X,Y>2\), \(0<u<s_X\), \(0<w<s_Y\). Multiplying the two amplitude ratios gives
\[
\alpha\beta=\frac{U_X(u)}u\frac{U_Y(w)}w
<\left(1-\frac2X\right)\left(1-\frac2Y\right).
\]
This rules out antiphase cycles at and above the threshold, including the equality case.

**Sufficiency.** Assume the three strict inequalities. Set \(c_X=1-2/X\) and \(c_Y=1-2/Y\), and on \((0,s_X)\) put \(w(t)=U_X(t)/\alpha\). For small positive \(t\), \(w(t)>0\), \(w(t)<s_Y\), and
\[
H(t)=U_Y(w(t))-\beta t,
\qquad \lim_{t\downarrow0}\frac{H(t)}t
=\frac{c_Xc_Y}{\alpha}-\beta>0.
\]
If \(w(t)\) reaches \(s_Y\) before \(t=s_X\), let \(t_*\) be its first such contact; then \(H(t_*)=-\beta t_*<0\). If it never reaches \(s_Y\), take \(t_*=s_X\), where \(w(t_*)=0\), hence likewise \(H(t_*)=-\beta s_X<0\). In both cases \(H\) is continuous on the intervening closed segment and positive near zero, so it has a root \(u\in(0,t_*)\). With \(w=w(u)\), both amplitudes are strictly positive and satisfy (1), constructing a genuine primitive antiphase two-cycle. This establishes the converse.

**Sharp disappearance.** If \(X,Y\) are fixed and positive antiphase cycles occur for a sequence of products \(\alpha_j\beta_j\uparrow c_Xc_Y\), then (1) gives
\[
\alpha_j\beta_j=\frac{U_X(u_j)}{u_j}\frac{U_Y(w_j)}{w_j}.
\]
Both ratio factors are positive and strictly below their respective \(c\)-values, and each extends continuously to its strict maximum only at amplitude zero. Their product approaching \(c_Xc_Y\) forces \(u_j,w_j\to0\). The Jacobian formula at the equilibrium is obtained by differentiation of the map and yields the displayed spectral identity. This completes the proof.

## Verification
The accompanying `verify_antiphase_ricker.py` reconstructs three positive antiphase two-cycles numerically and checks both map transitions, with maximum residual below \(5\times10^{-14}\). It also evaluates four scenarios that are excluded by the analytic threshold. The finite tests verify examples, **not** the universal quantifiers; the strict concavity and intermediate-value argument provide the proof for all admissible parameters.

## Relationship to prior work
The 2026 study by Goldar, Hassan, Pati, Mohsen, and Izadi investigates exactly this exponential Ricker competition system, its local flip/Neimark–Sacker bifurcations and examples of period-two solutions. Its Section 5 gives periodicity equations and a Jacobian test but not the sharp necessary-and-sufficient global-in-amplitude antiphase existence threshold above. Kulakov, Neverova, and Frisman (2022) investigate in-phase and out-of-phase cycles and describe bifurcations numerically, without an inspected claim supplying this exact criterion. General local flip tests do not suffice for existence over the full amplitude rectangle; the present proof adds a global concavity-and-intermediate-value argument. Earlier global-stability results address other parameter ranges; a complete comparison with every older source remains a residual priority risk.

## Limitations
No assertion is made about number, attraction, or hyperbolicity of antiphase cycles, in-phase cycles, more general periodic orbits, or global attractors. The limit at the threshold fixes \(X,Y\) while the couplings vary. The singular case \(\alpha\beta=1\) is outside the hypotheses. A portion of older relevant literature was accessible only as web excerpts, which limits definitive historical-priority assessment. No independent scientific audit has been performed.

## References
1. S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen, and M. Izadi, *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, *Discrete Dynamics in Nature and Society* (2026), article 7255117. First public version dated 2026-09-16. DOI: 10.1155/ddns/7255117. Full HTML: https://onlinelibrary.wiley.com/doi/10.1155/ddns/7255117.
2. A. Kulakov, G. Neverova, and E. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, *Mathematics* 10 (2022), 1076. DOI: 10.3390/math10071076.
3. *New global stability results for the planar Ricker model* (2026), DOI: 10.1080/10236198.2026.2636481 (abstract-level comparison only).
