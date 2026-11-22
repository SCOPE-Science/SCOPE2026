# Sharp latitude-drift contrast between spherical trapezoidal and Richardson-extrapolated flows

## Finding
For the rigid-axis flow \(p'(t)=\omega e_3\times p(t)\) on the unit sphere, the exact height \(c=e_3\cdot p(t)\) is invariant. Two spherical second-order integrators nonetheless have different sharp, third-order **height** errors. With \(T>0\), \(h=T/N\), \(c=e_3\cdot p_0\), and \(s^2=1-c^2\),
\[
\lim_{N\to\infty}\frac{e_3\cdot p_N^{\mathrm{STVDRK2}}-c}{h^3}=\frac{T\omega^4}{8}c(1-c^2)(1-2c^2),
\qquad
\lim_{N\to\infty}\frac{e_3\cdot p_N^{\mathrm{SRKRE}[1,2]}-c}{h^3}=-\frac{T\omega^4}{8}c^3(1-c^2).
\]
The Richardson-extrapolated scheme drifts toward the equator at leading order for every \(0<|c|<1\). The maximal normalized absolute drift is exactly \(3\sqrt{15}/500\), attained at \(|c|=\sqrt{3/5}\). By contrast, STVDRK2's third-order coefficient changes sign at \(|c|=1/\sqrt2\). At that exceptional latitude, it satisfies
\[
\lim_{N\to\infty}\frac{e_3\cdot p_N^{\mathrm{STVDRK2}}-c}{h^5}=\frac{T\omega^6c}{64}\ne0.
\]

## Assumptions and scope
Let \(e_3=(0,0,1)^\mathsf T\), \(\omega\in\mathbb R\setminus\{0\}\), and \(p_0\in\mathbb S^2\). Set \(c=e_3\cdot p_0\), \(s=\sqrt{1-c^2}\), and take \(T>0\) fixed while \(N\to\infty\) through integers and \(h=T/N\). The formulas concern \(0<|c|<1\); for \(c=0\) and \(|c|=1\), both numerical heights are exactly constant. The methods use the intrinsic spherical exponential \(E_h(p)=\exp_p(h\omega e_3\times p)\):
\[
\begin{aligned}
\mathrm{STVDRK2}(p,h)&=\mathrm{SLERP}\bigl(p,E_h(E_h(p)),\tfrac12\bigr),\\
\mathrm{SRKRE}[1,2](p,h)&=\mathrm{SLERP}\bigl(E_h(p),E_{h/2}(E_{h/2}(p)),2\bigr).
\end{aligned}
\]
The geodesic branch is well defined for all sufficiently small \(h\). This is not a claim of higher global position order.

## Proof
The methods commute with rotations about \(e_3\). Therefore their one-step height maps depend only on the input height \(c\), and we may choose \(p=(s,0,c)\) when \(0<|c|<1\). Put \(t=\omega h\). For any SFE stage of length \(\tau\),
\[
E_\tau(p)=\cos(\tau\omega s)p+\frac{\sin(\tau\omega s)}s(e_3\times p).
\]
For STVDRK2, write \(a=st\), \(u=\sqrt{s^2\cos^2a+\sin^2a}\), and \(b=tu\). Two stages give \(e_3\cdot q_2=c\cos a\cos b\) and \(p\cdot q_2=\cos a\cos b-(s/u)\sin a\sin b\). Since the spherical geodesic midpoint is \((p+q_2)/\|p+q_2\|\), the **exact** height multiplier is
\[
\frac{c_+}{c}=\frac{1+\cos a\cos b}{\sqrt{2\left(1+\cos a\cos b-(s/u)\sin a\sin b\right)}}.
\]
Taylor expansion at \(t=0\), uniform for \(c\) in compact subsets of \((-1,1)\setminus\{0\}\), yields
\[
\frac{c_+}{c}=1+\frac{s^2(2s^2-1)}8t^4+\frac{s^4(2-s^2)}{24}t^6+O(t^8).
\]
For SRKRE\([1,2]\), set \(a=st/2\), \(u=\sqrt{s^2\cos^2a+\sin^2a}\), and \(b=tu/2\). The coarse and two-half-step endpoints \(q_c,q_f\) obey
\[
\frac{e_3\cdot q_c}c=\cos(2a),\qquad\frac{e_3\cdot q_f}c=\cos a\cos b,\qquad q_c\cdot q_f=\cos a\cos b+\frac{s}{u}\sin a\sin b.
\]
For unit endpoints the exact doubled geodesic extrapolation identity is \(\mathrm{SLERP}(q_c,q_f,2)=2(q_c\cdot q_f)q_f-q_c\). Thus
\[
\frac{c_+}c=2\left(\cos a\cos b+\frac{s}{u}\sin a\sin b\right)\cos a\cos b-\cos(2a)
=1-\frac{s^2(1-s^2)}8t^4+\frac{s^4(1-s^2)}{24}t^6+O(t^8).
\]
For either method, \(c_{n+1}=c_n+h^4A(c_n)+h^6B(c_n)+O(h^8)\), with smooth coefficients near fixed \(c\). Over \(N=T/h\) steps, \(c_n-c=O(h^3)\), and telescoping gives \(c_N-c=Th^3A(c)+O(h^5)\). At \(c^2=1/2\), the STVDRK2 coefficient \(A(c)\) vanishes, so \(c_n-c=O(h^5)\) and \(c_N-c=Th^5B(c)+O(h^7)\), with \(B(c)=\omega^6c/64\). This proves all three limits. Maximizing \(|c|^3(1-c^2)/8\) over \(|c|\le1\) gives the unique nonzero maximizers \(c^2=3/5\) and value \(3\sqrt{15}/500\).

## Verification
Run `python verify.py` with SymPy and mpmath. It independently expands both exact one-step height formulas to sixth order, asserts every displayed coefficient symbolically, and checks convergence to the global constants for four signed and unsigned latitudes at two resolutions. The script completed with all assertions satisfied. Taylor expansions are algebraic support for an analytic proof; the numerical sequence checks alone are not used to infer an infinite-limit assertion.

## Relationship to prior work
The spherical forward Euler and STVDRK2 methods were developed by Leung, Chau, and Lee (2024). Lee and Leung (2026), Sect. 3.2, introduced SRKRE\([1,2]\) as the intrinsic Richardson extrapolation of spherical forward Euler. These references establish their algorithms, geometric constraint preservation, and state convergence orders. The present theorem instead derives an exact coefficient and sign boundary for the **additional rigid-rotation height first integral**, including exceptional fifth-order height accuracy of STVDRK2. The literature's global position-order claims neither imply the coefficient nor the direction of invariant drift. The older paper discusses rigid-axis rotation in a general stability context, without deriving these latitude-height asymptotics.

## Limitations
The result is for one rigid-axis rotation on \(\mathbb S^2\) with fixed \(T\), not all sphere vector fields. The asymptotic sign statements require sufficiently small positive \(h\); they do not establish monotone drift for arbitrary steps. Exact unit-norm preservation is not the same as conservation of latitude. Only the height observable has third- or fifth-order accuracy; global position errors may remain second order. No independent mathematical audit has been performed.

## References
- Y. K. Lee and S. Leung, *High-Order Spherical Runge-Kutta Schemes Based on Spherical Linear Extrapolation*, J. Sci. Comput. 107, 103 (2026), published 14 May 2026. https://link.springer.com/article/10.1007/s10915-026-03318-4
- S. Leung, W. M. Chau, and Y. K. Lee, *SLERP-TVDRK (STVDRK) Methods for Ordinary Differential Equations on Spheres*, J. Sci. Comput. 101, 63 (2024). https://link.springer.com/article/10.1007/s10915-024-02702-2
