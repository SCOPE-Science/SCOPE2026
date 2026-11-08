# Global critical prey clearance and a sign-changing logarithmic correction in a fear-modulated discrete Leslie–Gower map

## Finding
Consider the modified discrete Leslie–Gower model with fear-modulated prey reproduction:
\[
 x_{n+1}=x_n\exp\!\left(\frac{R}{1+k y_n}-d-a x_n-b y_n\right),\qquad
 y_{n+1}=y_n\exp\!\left(h-\frac{y_n}{m+x_n}\right).
\]
At the critical prey-invasion threshold \(R=(d+b h m)(1+k h m)\), a concrete nonempty open parameter region has a globally attracting predator-only equilibrium with a sharp nonhyperbolic prey-clearance law and a *finite* first logarithmic correction. Every strictly positive initial population satisfies
\[
\frac1{x_n}= Cn+A\log n+K(x_0,y_0)+o(1),\qquad
 y_n-hm=h x_n+C x_n^2+O(x_n^3),
\]
where \(K\) is finite and the explicit \(C>0\), \(A\) may have either sign. Thus \(nx_n\to 1/C\), \(n(y_n-hm)\to h/C\), and the first asymptotic approach of \(n x_n\) to \(1/C\) reverses direction as parameters change. The correction coefficient is not generally universal in sign.

## Assumptions and scope
All parameters \(R,d,a,b,k,h,m\) are strictly positive, and both initial populations are strictly positive. Set
\[
 Y=hm,\quad D=1+kY,\quad \Delta=R-d,\quad L=b+\frac{Rk}{D^2},\quad
 C=a+hL,\quad S=\frac{Rk^2h^2}{D^3},\quad
 A=\frac C2+L-\frac S C.
\]
Assume
\[
 R=(d+bY)D,\qquad 0<h<1,\qquad 0<\Delta<1,\qquad
 a>\frac{\Delta}{m(e^{1-h}-1)}.
\]
The theorem holds for *all* \(x_0>0\), \(y_0>0\), regardless of their size, within this specified parameter region. The reference equilibrium is \((0,Y)\). No assertion is made about parameter choices failing these sufficient conditions.

In particular, take
\[
 h=m=\frac12,\quad k=1,\quad b=d=\frac1{100},\quad R=\frac1{64},\quad
 a\in\left\{\frac3{100},\frac1{10}\right\}.
\]
In both cases the assumptions hold, \(L=1/50\), \(S=1/500\), \(C=a+1/100\), while
\[
 A(3/100)=-\frac1{100},\qquad A(1/10)=\frac5{88}.
\]
There is a unique zero of \(A\) between them,
\[
 a_*=\frac{2\sqrt{11}-3}{100}.
\]
This is a sign reversal of the first logarithmic correction at fixed values of the other six parameters.

## Proof
**1. A global prey bound.** For every \(x,y>0\), since \(y\mapsto R/(1+ky)-d-by\) decreases,
\[
 x_{n+1}\le f_\Delta(x_n):=x_ne^{\Delta-a x_n}.
\]
The maximum of this scalar map over \(x>0\) is \(e^{\Delta-1}/a<1/a\), so \(0<x_n<1/a\) from generation one onward. On \([0,1/a]\), \(f_\Delta\) is increasing. Comparison with the scalar recurrence \(u_{n+1}=f_\Delta(u_n)\), initialized with \(u_1=x_1\), gives \(x_n\le u_n\) for \(n\ge1\). When \(0<\Delta<1\), every positive such scalar orbit converges monotonically to \(\Delta/a\). Hence \(\limsup x_n\le\Delta/a\).

**2. Bringing the predator under its global carrying cap.** For any \(x\ge0\), maximizing \(y\mapsto y e^{h-y/(m+x)}\) over \(y>0\) gives
\[
 y_{n+1}\le(m+x_n)e^{h-1}.
\]
By the strict condition on \(a\), one can choose \(\eta>0\) so small that \((m+\Delta/a+\eta)e^{h-1}<m\). As \(x_n\le\Delta/a+\eta\) eventually, \(0<y_n<m\) eventually. On the interval \([0,m]\), the function \(f_m(y)=y e^{h-y/m}\) is increasing and maps this interval into itself. Since \(m+x_n\ge m\), the original predator update dominates \(f_m(y_n)\). Iteration of the scalar comparison from some \(0<y_N<m\) yields \(\liminf y_n\ge hm=Y\).

**3. Global extinction at equality.** For \(\epsilon>0\), eventually \(y_n\ge Y-\epsilon\). Defining \(Q(y)=R/(1+ky)-d-by\), with \(Q(Y)=0\), we obtain
\[
 x_{n+1}\le x_ne^{Q(Y-\epsilon)-a x_n}.
\]
For sufficiently small \(\epsilon\), its scalar right-hand map has exponent \(0<Q(Y-\epsilon)<1\) and is increasing on \([0,1/a]\). The same scalar comparison gives \(\limsup x_n\le Q(Y-\epsilon)/a\). Sending \(\epsilon\downarrow0\) forces \(x_n\to0\). Conversely, for every sufficiently small \(\delta>0\), eventually \(x_n\le\delta\) and \(y_n<m\). The predator recurrence is bounded above by \(y e^{h-y/(m+\delta)}\), increasing on \([0,m]\) and preserving it when \(h(m+\delta)<m\). Its positive scalar attractor is \(h(m+\delta)\); therefore \(\limsup y_n\le h(m+\delta)\). Sending \(\delta\downarrow0\) yields \(y_n\to Y\).

**4. Quantitative slaving near the boundary.** At \((0,Y)\) the Jacobian is
\[
 \begin{pmatrix}1&0\\ h^2&1-h\end{pmatrix},
\]
so there is one neutral and one strictly contracting eigenvalue. The positive half of the local center manifold has a smooth graph
\[
 y=Y+h x+q x^2+O(x^3).
\]
Substitution into the predator recurrence and the graph invariance identity gives \(q=C\): on the proposed graph the predator update is \(Y+h x+(1-h)q x^2+O(x^3)\), whereas the graph evaluated after the prey update equals \(Y+h x+(q-hC)x^2+O(x^3)\). Equality forces \(q=C\). Local stable-foliation contraction transfers this expansion to every eventually small positive orbit, with an error \(O(x_n^3)\). Equivalently, writing \(w_n=y_n-Y-hx_n-Cx_n^2\), Taylor expansion yields a recurrence \(w_{n+1}=(1-h+o(1))w_n+O(x_n^3)\); because \(x_{n+1}/x_n\to1\), geometric convolution gives \(w_n=O(x_n^3)\). Here the possible purely fast invariant curve is the boundary \(x=0\), excluded by positive initial prey.

**5. Cubic prey map and reciprocal summation.** The Taylor expansion along this asymptotic graph is
\[
 x_{n+1}=x_n-Cx_n^2+B x_n^3+O(x_n^4),\qquad B=\frac{C^2}{2}-LC+S.
\]
The \(O(x_n^3)\) graph error only affects order \(x_n^4\) and higher. Because \(C>0\), the recurrence implies \(x_n\sim (Cn)^{-1}\). With \(U_n=1/x_n\), direct expansion gives
\[
 U_{n+1}=U_n+C+\frac{C^2-B}{U_n}+O(U_n^{-2}).
\]
First summation gives \(U_n=Cn+O(\log n)\). Thus
\[
 U_{n+1}-U_n-C-\frac{A}{n}=O\!\left(\frac{\log n}{n^2}\right),
 \qquad A=\frac{C^2-B}{C}=\frac C2+L-\frac S C.
\]
The residual series is absolutely summable, and \(\sum_{j=1}^{n}j^{-1}-\log n\) converges, proving the existence of a *finite* orbit-dependent constant \(K\) and the stated \(o(1)\) remainder. The predator asymptotic follows from Step 4. Finally, the explicit rational family gives \(A=(a+1/100)/2+1/50-1/[500(a+1/100)]\), proving both signs and the unique zero stated above. \(\square\)

## Verification
Run `python verify.py` with Python, SymPy and mpmath installed. The script checks the center-graph invariance and cubic Taylor coefficients in exact rational arithmetic, both exact signs, the zero of the logarithmic coefficient, the sufficient global-domain inequality, and two illustrative finite-horizon orbits. Numerical orbits are diagnostics, not a proof of the limits. The complete global and asymptotic statements follow from the comparison and reciprocal-summation proof above.

## Relationship to prior work
Lin, Chen, Li and Chen (2022) introduce this exact modified discrete Leslie–Gower fear map and study its equilibria, global attractivity under sufficient conditions, flip bifurcations and transcritical bifurcations. The present theorem deliberately works at the *equality* prey-invasion threshold and establishes a global rate, the entire logarithmic correction including its finite remainder, and an explicit sign reversal. Their treatment of transcriticality does not itself establish these quantified assertions in the source sections inspected. Chen, He and Chen (2021) study a related fear-mediated discrete prey–predator model, but its predator recurrence differs from the Leslie–Gower response above. Generic center-manifold and parabolic iteration principles underpin the local asymptotic proof; no novelty is claimed for those general methods.

## Limitations
The global proof is conditional on \(0<h<1\), \(0<R-d<1\) and the strict crowding inequality stated above. It covers neither predator oscillations outside that region nor noisy finite populations. The \(K\) term depends on the initial populations and is not supplied in elementary closed form. The source publisher's HTML full text was not fully retrievable during this assessment, so an unlocated corresponding asymptotic formula in its appendices or elsewhere remains a publication-priority risk; the novelty assessment is consequently best-knowledge, not proof of priority. The independent audit has not been performed.

## References
1. S. Lin, F. Chen, Z. Li and L. Chen, *Complex Dynamic Behaviors of a Modified Discrete Leslie–Gower Predator–Prey System with Fear Effect on Prey Species*, **Axioms** 11 (2022), 520, first public date 2022-10-01, https://doi.org/10.3390/axioms11100520.
2. J. Chen, X. He and F. Chen, *The Influence of Fear Effect to a Discrete-Time Predator-Prey System with Predator Has Other Food Resource*, **Mathematics** 9 (2021), 865, https://doi.org/10.3390/math9080865.
