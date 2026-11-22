# A unique antipodal two-cycle with a nilpotent superattraction sheet in a three-dimensional sine map

## Finding
For the real-parameter map
\[
F_{p,q,r}(x,y,z)=(y,\sin z,\;px+qy-r\sin z),
\]
write \(A=p+q-r\) and \(B=q-p+r\). Whenever \(|A|\leq1\) and \(1<B<\pi\), the map has **exactly one** real primitive period-two orbit. It is
\[
P_+=(v,-v,Bv),\qquad P_-=(-v,v,-Bv),
\]
where \(v\in(0,1]\) is the unique positive solution of \(v=\sin(Bv)\). Equality \(v=1\) occurs exactly at \(B=\pi/2\). For \(|A|\le1\), \(0<B\le1\), there is no primitive period-two orbit.

On the entire parameter sheet \(B=\pi/2\), \(|A|\le1\), the orbit is exactly \((1,-1,\pi/2)\leftrightarrow(-1,1,-\pi/2)\), and its return Jacobian is nilpotent: \(\bigl(D(F^2)(P_\pm)\bigr)^3=0\). Consequently the two-cycle is locally superattracting, even when \(p\ne0\) and the one-step Jacobian is nonzero.

Fix any real \(p\ne0\) and \(|A|\le1\). Vary \(B\) near \(\pi/2\) by setting \(q=(A+B)/2\) and \(r=p+(B-A)/2\). The two-cycle persists and its two-step spectral radius has the **fractional-power onset**
\[
\rho\bigl(D F^2(P_\pm)\bigr)
=|p|^{2/3}|B-\pi/2|^{2/3}\left(1+O_{p,A}(|B-\pi/2|^{1/3})\right).
\]
In particular it stays attracting on a neighborhood of the nilpotent sheet, with contraction becoming superattraction on the sheet.

## Assumptions and scope
All states are real triples and all three coefficients \(p,q,r\) are real. The count refers to distinct real primitive orbits of least period exactly two, not fixed points or cycles of higher period. The global census requires \(|A|\le1\) and \(0<B<\pi\); no census is asserted outside this domain. The transverse spectral asymptotic holds for each **fixed nonzero** \(p\) and fixed \(A\) as \(B\to\pi/2\), with the indicated coupling of \(q,r\). It is not uniform as \(p\to0\).

## Proof
**Reduction to one scalar equation.** Let a period-dividing-two state be \((x,y,z_0)\), with its next state \((y,x,z_1)\), since \(F^2(x,y,z_0)=(x,y,z_0)\) implies \(x=\sin z_0\) and \(y=\sin z_1\). The third-coordinate recurrence gives
\[
z_0=qx+(p-r)y,\qquad z_1=(p-r)x+qy.
\]
Set \(u=(x+y)/2\), \(v=(x-y)/2\), so that \(z_0=Au+Bv\), \(z_1=Au-Bv\). Adding and subtracting the two sine equations yields the *necessary and sufficient* pair
\[
u=\sin(Au)\cos(Bv),\qquad v=\cos(Au)\sin(Bv).
\]
Conversely these equations reconstruct a genuine period-dividing-two point by the displayed formulas, so no periodic points are lost.

When \(|A|\le1\), \(|u|\le|\sin(Au)|\le |Au|\le|u|\). If \(u\ne0\), the strict inequality \(|\sin t|<|t|\) for nonzero real \(t\), or the \(A=0\) case, contradicts this chain. Hence \(u=0\), leaving exactly
\[
v=\sin(Bv),\quad z_0=Bv,\quad z_1=-Bv.
\]
For \(0<B\le1\), the strict sine inequality excludes nonzero roots. For \(1<B<\pi\), any positive root has \(v\le1\). Moreover \(Bv\in(0,\pi)\), and \(\sin t/t\) decreases strictly from \(1\) to \(\sin B/B\le1/B\) on \((0,B]\); thus there is precisely one positive root of \(\sin(Bv)/v=1\). Its negative is the other point on the same primitive orbit. Finally \(v=1\) iff \(\sin B=1\) in \(1<B<\pi\), exactly when \(B=\pi/2\). This proves the census and the explicit sheet.

**Nilpotent return and local attraction.** The Jacobian at \(z\) is
\[
J(z)=\begin{pmatrix}0&1&0\\0&0&\cos z\\p&q&-r\cos z\end{pmatrix}.
\]
The two cycle phases have equal derivatives because cosine is even. At \(B=\pi/2\), their third coordinates equal \(\pm\pi/2\), so the common derivative is \(J_0=\begin{psmallmatrix}0&1&0\\0&0&0\\p&q&0\end{psmallmatrix}\) with \(J_0^3=0\). The two-step derivative is \(J_0^2\) and its cube is zero. Thus the sixth iterate near either phase has vanishing derivative at its fixed point; by differentiability this iterate is a contraction in a sufficiently small neighborhood. The orbit is locally attracting, and all its linear multipliers vanish.

**Two-thirds-power spectral law.** Near \(B_0=\pi/2\), the implicit equation \(g(v,B)=v-\sin(Bv)=0\) has \(\partial_vg(1,B_0)=1\). The implicit function theorem yields a smooth root \(v(B)\) with \(v(B_0)=1\) and \(v'(B_0)=0\). Hence \(t(B)=\cos(Bv(B))=-(B-B_0)+O((B-B_0)^2)\). The characteristic polynomial of the phase Jacobian is
\[
\det(\lambda I-J)=\lambda^3+rt\lambda^2-qt\lambda-pt.
\]
At fixed \(p\ne0\) and \(A\), the three roots satisfy \(|\lambda_j|=|pt|^{1/3}(1+O_{p,A}(|t|^{1/3}))\): divide the polynomial by \(pt\), rescale \(\lambda=|pt|^{1/3}\zeta\), and use simple-root perturbation of \(\zeta^3=\operatorname{sgn}(pt)\). Since both phase Jacobians are equal, the return Jacobian is \(J^2\); its spectral radius equals \((\max_j|\lambda_j|)^2\). Substituting \(t(B)\) proves the formula. Its limit zero also proves persistence of attraction for sufficiently small nonzero detuning.

## Verification
The accompanying `check.py` numerically recomputes the cyclic images, Jacobian characteristic polynomial, nilpotency and near-sheet spectral scaling for 224 parameter/spectral cases (Python, NumPy). Its successful execution is supplementary only. The argument above proves the infinite-parameter statements without trusting numerical root counts or sampled eigenvalues. Reproduce with `python check.py` in an environment with NumPy installed.

## Relationship to prior work
Rajagopal et al. (2023) give the five-parameter map \((y,\sin z,\alpha+\beta x+\gamma y-\delta\sin z+\mu z)\), which contains this map exactly at \(\alpha=\mu=0\), \(\beta=p\), \(\gamma=q\), \(\delta=r\). Their analysis emphasizes numerical bifurcations, Lyapunov exponents and synchronization; it does not give an exact global primitive-two-cycle census or nilpotent sheet. Mammeri (2017) had already published the fixed-sine-coefficient slice \(r=1\), including numerical periodic windows and fixed-point analysis, but not the current period-two census or nilpotent-sheet result. An earlier 2016 Mammeri paper discusses related fixed-sine-coefficient maps; no claim of originality for that slice as a model is made. Almatroud et al. (2024) explicitly publish the three-parameter map analyzed here and discuss fixed-point stability, numerical dynamics and control, but do not give the period-two equations, completeness classification or fractional spectral law. The earlier 2023 publication is accordingly the earliest verified public source for this exact map as a parameter subfamily. Classical sine-intersection monotonicity and eigenvalue perturbation are standard ingredients, not claimed as independent discoveries. Database comparisons found different sine-memory, quadratic, and coupled-map cycle results but no statement implying this combined exact result.

## Limitations
No global basin geometry, higher-period classification, entropy or chaos characterization is asserted. The one-parameter spectral asymptotic is pointwise in fixed nonzero \(p\) and \(A\), not uniform near \(p=0\). Earlier unindexed accounts of the same reduction or general higher-dimensional nilpotent periodic-orbit spectral laws may affect publication priority. The printed scalar recurrence of Almatroud et al. and its separately printed three-dimensional map are not asserted here to be dynamically equivalent; the present theorem concerns the literal three-dimensional equations.

## References
1. K. Rajagopal, S. Kanagaraj, C. Volos and A. Karthikeyan, *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry **15** (2023), 780. https://doi.org/10.3390/sym15040780 (public 2023-03-23).
2. M. Mammeri, *Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps*, Bull. Math. Anal. Appl. **9** (2017), 1–8. https://emis.muni.cz/journals/BMAA/repository/docs/BMAA9-1-1.pdf (public 2017-01-12).
3. O. A. Almatroud et al., *Multistability, Chaos, and Synchronization in Novel Symmetric Difference Equation*, Symmetry **16** (2024), 1093. https://doi.org/10.3390/sym16081093 (public 2024-08-22).
