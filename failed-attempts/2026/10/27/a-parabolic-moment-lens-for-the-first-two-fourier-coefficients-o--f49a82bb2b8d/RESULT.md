# A parabolic moment lens for the first two Fourier coefficients of circular indicator sets

## Finding

For a Lebesgue-measurable set \(E\) on the unit circle, write
\[
a=\frac{|E|}{2\pi},\qquad c_k(E)=\frac{1}{2\pi}\int_E e^{-ik\theta}\,d\theta\quad(k=1,2).
\]
Here \(0<a<1\), and angles are understood modulo \(2\pi\). Put
\[
M_a=\frac{\sin(\pi a)}{\pi},\quad
\gamma_+(a)=\frac{\pi}{2}\tan\frac{\pi a}{2},\quad
\gamma_-(a)=\frac{\pi}{2}\cot\frac{\pi a}{2}.
\]
**Complex Fourier constraints.** Every such \(E\) satisfies the simultaneous sharp disk inequalities
\[
|c_1(E)|\le M_a,\qquad
\boxed{\left|c_2(E)+\gamma_+(a)c_1(E)^2\right|
\le M_a-\gamma_+(a)|c_1(E)|^2},
\]
\[
\boxed{\left|c_2(E)-\gamma_-(a)c_1(E)^2\right|
\le M_a-\gamma_-(a)|c_1(E)|^2}.
\]
Each disk inequality is sharp **at every prescribed** \(|c_1(E)|=r\in[0,M_a]\); all equality sets are classified below.

**Exact real-moment body.** Define \(m=\Re c_1(E)\) and \(q=\Re c_2(E)\). As \(E\) varies over all measurable sets of a fixed measure fraction \(a\), the set of attainable pairs is *exactly* the closed parabolic lens
\[
\boxed{ |m|\le M_a,\quad -M_a+\pi\cot\frac{\pi a}{2}\,m^2
\le q\le
M_a-\pi\tan\frac{\pi a}{2}\,m^2. }
\]
No reflection symmetry is assumed on \(E\). At every \(m\) in this interval, the upper and lower equality sets are unique up to null sets; their shapes are respectively an outer two-arc configuration and an inner two-arc configuration. The two boundary curves meet only at \(|m|=M_a\), where both configurations reduce to a single arc. The area of the real-moment lens is \(\frac83 M_a^2\).

## Assumptions and scope

Only Lebesgue measurability and \(0<|E|<2\pi\) are assumed. Endpoints of arcs are immaterial, and equality always means equality modulo sets of measure zero. Set \(t=\pi a\), \(s=\sin(t/2)\), \(c=\cos(t/2)\), so \(M_a=2sc/\pi\). For any \(m\in[-M_a,M_a]\), define the angles
\[
\begin{aligned}
&u_+=\arccos\!\left(-\frac{\pi m}{2c}\right)-\frac{\pi-t}{2},
&&v_+=u_++\pi-t,\\
&u_-=\arccos\!\left(\frac{\pi m}{2s}\right)-\frac t2,
&&v_-=u_-+t.
\end{aligned}
\]
These are uniquely defined with \(0\le u_\pm\le v_\pm\le\pi\). Working with the representative \(\theta\in[-\pi,\pi]\), put
\[
E_+(a,m)=\{\theta:|\theta|\le u_+\ \text{or}\ |\theta|\ge v_+\},
\]
\[
E_-(a,m)=\{\theta:u_-\le|\theta|\le v_-\}.
\]
All assertions about the first two complex coefficients use the standard negative-exponent Fourier convention given above. A rigid rotation of a set by \(\varphi\) multiplies \(c_k\) by \(e^{-ik\varphi}\).

## Proof

**1. The attainable first cosine moment.** Replacing \(E\) by the average of its reflections does not change the mass or any cosine moment. Since \(\cos\theta\) decreases strictly as \(|\theta|\) increases from \(0\) to \(\pi\), the elementary rearrangement argument says that its integral over a set of length \(2t\) is between the values for the arcs \(|\theta|\le t\) and \(|\theta|\ge\pi-t\). This gives \(|m|\le\sin(t)/\pi=M_a\). The two explicit sets above have precisely the prescribed mass \(a\), and direct integration gives \(\Re c_1(E_\pm)=m\):
\[
\frac{\sin u_+-\sin v_+}{\pi}=m,
\qquad \frac{\sin v_--\sin u_-}{\pi}=m.
\]

**2. Explicit moment values.** Put \(z_+=(u_++v_+)/2\), \(z_-=(u_-+v_-)/2\). The formulas for the first moments imply
\[
\cos z_+=-\frac{\pi m}{2c},\qquad
\cos z_-=\frac{\pi m}{2s}.
\]
Integrating \(\cos(2\theta)\) over the two configurations yields
\[
\begin{aligned}
\Re c_2(E_+)&=\frac{\sin(2u_+)-\sin(2v_+)}{2\pi}
=-\frac{\sin t}{\pi}\cos(2z_+)
=M_a-\pi\tan(t/2)m^2,\\
\Re c_2(E_-)&=\frac{\sin(2v_-)-\sin(2u_-)}{2\pi}
=\frac{\sin t}{\pi}\cos(2z_-)
=-M_a+\pi\cot(t/2)m^2.
\end{aligned}
\]

**3. The exact nonnegative deficit certificates.** For either \(\varepsilon\in\{+,-\}\), set
\[
G_\varepsilon(\theta)
=2(\cos\theta-\cos u_\varepsilon)(\cos\theta-\cos v_\varepsilon).
\]
The identity
\[
G_\varepsilon(\theta)=\cos(2\theta)
-2(\cos u_\varepsilon+\cos v_\varepsilon)\cos\theta
+1+2\cos u_\varepsilon\cos v_\varepsilon
\]
shows that for sets of the same mass and first cosine moment, their difference in second cosine moments equals their difference in integrated \(G_\varepsilon\). By construction, \(G_+\) is positive on \(E_+\) and negative outside, whereas \(G_-\) is negative on \(E_-\) and positive outside. Hence, for every \(E\) of mass \(a\) and first cosine moment \(m\),
\[
\boxed{\Re c_2(E_+)-\Re c_2(E)
=\frac1{2\pi}\int_{E\triangle E_+}|G_+(\theta)|\,d\theta,}
\]
\[
\boxed{\Re c_2(E)-\Re c_2(E_-)
=\frac1{2\pi}\int_{E\triangle E_-}|G_-(\theta)|\,d\theta.}
\]
This proves both parabola bounds, all equality cases and an exact stability certificate. The zero sets of each \(G_\varepsilon\) are finite, so a zero deficit forces equality of sets modulo null sets, even if one angle is an endpoint.

**4. No gaps in the lens.** Fix \(a,m\) and any \(q\) between the two attained boundary values. A convex mixture of the two indicator functions \(\mathbf1_{E_-}\) and \(\mathbf1_{E_+}\) is a density \(f\in[0,1]\) with exactly the required integrals of \(1,\cos\theta,\cos2\theta\). It can be replaced by an indicator preserving these three integrals: the family of bounded densities \(0\le f\le1\) with the three fixed moments is weak-* compact and convex, hence has an extreme point. Such an extreme point is indicator-valued, because otherwise on a positive-measure set it lies in \([\delta,1-\delta]\) for some \(\delta>0\); divide that set into four positive-measure pieces. Their three-component moment vectors are linearly dependent, so a small nonzero signed perturbation supported on those pieces preserves all three moments and the bounds \([0,1]\), contradicting extremality. This proves exact attainment of every point in the lens. Integrating the difference of its two parabolas over \([-M_a,M_a]\) gives the claimed area.

**5. The complex disk inequalities.** Apply the just-proved real inequalities after every rotation \(\varphi\). They hold with \(m_\varphi=\Re(e^{i\varphi}c_1)\), \(q_\varphi=\Re(e^{2i\varphi}c_2)\). Using
\[
2m_\varphi^2=|c_1|^2+\Re(e^{2i\varphi}c_1^2)
\]
turns the upper bound into
\[
\Re\{e^{2i\varphi}(c_2+\gamma_+c_1^2)\}
\le M_a-\gamma_+|c_1|^2.
\]
Taking the maximum over \(\varphi\) gives the first disk. The lower real inequality similarly gives
\[
\Re\{e^{2i\varphi}(c_2-\gamma_-c_1^2)\}
\ge -M_a+\gamma_-|c_1|^2
\]
and thus the second disk. The right-hand sides are positive because \(|c_1|\le M_a\) and \(\gamma_+M_a=\sin^2(t/2)\), \(\gamma_-M_a=\cos^2(t/2)\).

**6. Equality in the complex disks.** Equality in either modulus inequality supplies an angle \(\varphi\) at which the corresponding real inequality is equal. The unique equality characterization in step 3 makes \(E\) a rotation of \(E_+(a,m_\varphi)\), respectively \(E_-(a,m_\varphi)\). These sets are reflection symmetric, so their first Fourier coefficients have magnitude \(|m_\varphi|\). Consequently, for any specified \(r=|c_1|\in[0,M_a]\), all equality sets are precisely the rotations of \(E_+(a,r)\) for the plus disk and the rotations of \(E_-(a,r)\) for the minus disk. Direct substitution of step 2 proves that each such rotation indeed attains equality. This also proves the asserted sharpness at every admissible first-coefficient magnitude.

## Verification

The standalone standard-library script `check_moment_lens.py` evaluates the exact trigonometric extremizer formulas and dual-polynomial identities, including both endpoint values of \(m\). It independently integrates Fourier coefficients of 4,320 randomized unions of equal subarcs and checks the two complex disk inequalities and parabolic bounds. Execution returned `PASS 41864 assertions`. These finite calculations check algebra, signs and normalization; they are not substitutes for the analytical argument for arbitrary measurable sets or the weak-* purification step.

## Relationship to prior work

The starting point is the use of Fourier coefficients to describe circular arcs and measurable windows. Huang [1] reconstructs the mass of an arc from a measure's Fourier coefficients using a Wiener-type series. Courtney [2] proves uniqueness of a union of at most \(n\) arcs from the first \(n\) coefficients of its indicator. Chalendar–Garcia–Ross–Timotin [3] optimize Hardy-space dual functionals for a *fixed* characteristic-function symbol, including arcs and general measurable sets. In contrast, the result here varies all indicators of prescribed measure, determines the complete *joint* real first/second Fourier-coefficient region, proves sharp nonlinear complex-coefficient bounds, and gives unique extremizers with exact deficits. Reconstruction or Hardy distance of a fixed set does not by itself state or imply these parabolic formulas. General non-atomic moment convexity and elementary rearrangement are used as standard tools and are not claimed as new.

## Limitations

The pair of complex disks is proved necessary and separately sharp, not claimed to be a sufficient characterization of the full four-real-dimensional feasible complex-coefficient body at fixed \(a\). The explicit exact feasible region concerns the two **real cosine** coefficients, without imposing or specifying the sine coefficients. The result is restricted to Fourier modes one and two, and to \(0<a<1\); no general higher-mode body is asserted. Potential exact equivalent formulas in older specialized moment-space literature remain a priority risk; no independent priority audit is claimed.

## References

[1] Huichi Huang, *A Wiener-type theorem for arcs in the unit cirle*, arXiv:2407.19424, first submitted 2024-07-28, https://arxiv.org/abs/2407.19424 (original spelling of paper title retained).

[2] Dennis Courtney, *Unions of arcs from Fourier partial sums*, arXiv:1002.0639, first submitted 2010-02-03, https://arxiv.org/abs/1002.0639.

[3] Isabelle Chalendar, Stephan Ramon Garcia, William T. Ross, Dan Timotin, *An extremal problem for characteristic functions*, arXiv:1307.2646, first submitted 2013-07-10, https://arxiv.org/abs/1307.2646.
