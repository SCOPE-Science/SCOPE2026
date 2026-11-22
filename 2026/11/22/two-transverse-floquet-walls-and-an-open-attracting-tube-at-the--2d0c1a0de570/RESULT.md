# Two transverse Floquet walls and an open attracting tube at the Euler–Chen axis flip

## Finding

Consider the forward-Euler Chen map
\[
F_{a,b,c,h}(x,y,z)=\bigl(x+ha(y-x),\ y+h((c-a)x-xz+cy),\ z+h(xy-bz)\bigr).
\]
For every \(a>2c>0\), there is \(h_0(a,c)>0\) such that the conclusions below hold for each \(0<h<h_0\) at the **axial flip resonance** \(b=2/h\).

The entire axis \(x=y=0\) is invariant, and every \(A>0\) gives a primitive period-two cycle \((0,0,A)\leftrightarrow(0,0,-A)\). Put
\[
M_0=\begin{pmatrix}1-ha&ha\\h(c-a)&1+hc\end{pmatrix},\quad
m=\det M_0=1+h(c-a)+h^2a(a-2c),\quad
T=\operatorname{tr}(M_0^2),
\]
and define two strictly ordered positive amplitudes
\[
A_+=\frac{\sqrt{1-T+m^2}}{h^2a},\qquad
A_-=\frac{\sqrt{1+T+m^2}}{h^2a},\qquad 0<A_+<A_-.
\]
The two-step Floquet multipliers are exactly \(1\) and the roots of
\[
\lambda^2-T\lambda+\bigl(m^2-h^4a^2A^2\bigr)=0.
\]
Thus for \(0<A<A_+\) both transverse multipliers lie strictly inside the unit circle; for \(A_+<A<A_-\) exactly one lies outside; for \(A>A_-\) both lie outside. At \(A=A_+\) a transverse multiplier equals \(+1\), and at \(A=A_-\) one equals \(-1\). These are exact, exhaustive transverse classifications of the axial cycles, not a census of off-axis cycles.

For every \(0<A<A_+\), an open three-dimensional neighborhood of \((0,0,A)\) has trajectories converging geometrically, at even and odd times, to **some** axial period-two cycle. The limiting amplitude depends on the initial condition and need not equal \(A\).

The two thresholds separate scales as \(h\downarrow0\):
\[
A_+\sim\frac{2\sqrt{a(a-2c)}}{ah},\qquad
A_-\sim\frac2{ah^2},\qquad\frac{A_-}{A_+}\sim\frac1{h\sqrt{a(a-2c)}}.
\]
For the rational benchmark \((a,c,h,b)=(3,1,1/10,20)\),
\[
A_+=11,\qquad A_-=\frac{\sqrt{32689}}3.
\]
Consequently, an entire positive-volume neighborhood is attracted toward a continuum of primitive period-two oscillations despite the single real equilibrium of the corresponding continuous Chen flow.

## Assumptions and scope

The state space is \(\mathbb R^3\). All parameters are real with \(a>2c>0\), \(h>0\), \(b=2/h\), and \(h\) sufficiently small for the transverse origin block \(M_0\) to be Schur stable with \(0<T<2\). Such an \(h_0\) exists and depends only on \(a,c\). The map is the explicit Euler discretization of the standard Chen vector field, not an exact time-\(h\) flow. A cycle of amplitude \(A\) is the unordered pair of its two axis points. “Transverse” refers to the \((x,y)\)-subspace, and a transverse mode with modulus greater than one is called expanding. The unavoidable longitudinal Floquet multiplier is \(+1\). All attracting statements are local to the period-two axis family, not global attractor claims.

## Proof

**1. Axis resonance and linearization.** At \(x=y=0\), one iteration sends \(z\mapsto(1-hb)z=-z\). Hence all nonzero axis points have least period two. The Jacobian along the axis is block diagonal, with transverse block
\[
M(z)=\begin{pmatrix}1-ha&ha\\h(c-a-z)&1+hc\end{pmatrix}=M_0-hzE_{21}
\]
and axial entry \(-1\). Thus the transverse two-step return is \(P(A)=M(-A)M(A)\), while the axial two-step derivative is \(+1\).

**2. Floquet invariants and the exact walls.** Using \(E_{21}^2=0\) and the fact that a matrix commutator has trace zero,
\[
\operatorname{tr}P(A)=\operatorname{tr}(M_0^2)=T.
\]
Because \(\det M(z)=m+h^2az\), multiplicativity gives
\[
\det P(A)=m^2-h^4a^2A^2=:D(A).
\]
The displayed quadratic is therefore the **complete** transverse characteristic polynomial. Put \(\tau=c-a<0\), \(\Delta=a(a-2c)>0\). As \(h\to0^+\), \(M_0=I+hB\), where \(\operatorname{tr}B=\tau<0\) and \(\det B=\Delta>0\). The strict quadratic Schur inequalities are
\[
1-m=-h\tau-h^2\Delta>0,\quad
1-\operatorname{tr}M_0+m=h^2\Delta>0,\quad
1+\operatorname{tr}M_0+m=4+2h\tau+h^2\Delta>0
\]
for sufficiently small positive \(h\). Hence \(M_0\) and \(P(0)=M_0^2\) are strictly Schur stable, while \(T\to2\) from below; after reducing \(h_0\), \(0<T<2\). At \(A=0\), therefore, \(1-T+D(0)>0\) and \(1+T+D(0)>0\). For every \(A\ge0\), \(1-D(A)>0\), while the first two expressions decrease strictly with \(A^2\). Their unique positive zeros are \(A_+\) and \(A_-\), in that order because \(T>0\). The degree-two Schur criterion
\[
1-T+D>0,\qquad 1+T+D>0,\qquad 1-D>0
\]
proves strict attraction below \(A_+\). At the first wall \(\lambda=1\) is simple and the other transverse root is \(T-1\in(-1,1)\). Between the walls, continuity and the signs of the characteristic polynomial at \(\pm1\) give exactly one multiplier outside and one inside. At the second wall \(\lambda=-1\) is simple and the other is \(T+1>1\); beyond it the two real roots lie respectively below \(-1\) and above \(+1\). No unproved genericity statement is needed.

**3. Open attraction to the family.** Fix \(A\in(0,A_+)\). In even time write \(U_k=(x_{2k},y_{2k})\) and \(Z_k=z_{2k}\). Direct composition gives
\[
U_{k+1}=P(Z_k)U_k+O(\|U_k\|^3),\qquad
Z_{k+1}=Z_k+h\bigl(x_{2k+1}y_{2k+1}-x_{2k}y_{2k}\bigr)=Z_k+O(\|U_k\|^2),
\]
uniformly for \(Z_k\) in a compact interval around \(A\). Since the spectral radius of \(P(A)\) is less than one, a suitable equivalent vector norm has induced norm \(\|P(A)\|_*<1\). Continuity and a sufficiently small neighborhood make \(\|U_{k+1}\|_*\le q\|U_k\|_*\) with \(q<1\). The quadratic drift is then summable, \(\sum_k|Z_{k+1}-Z_k|\le C\|U_0\|_*^2/(1-q^2)\), so shrinking the initial neighborhood keeps all \(Z_k\) in the chosen interval. It follows that \(Z_k\to Z_\infty\) and \(U_k\to0\) exponentially. The odd iterates converge to \((0,0,-Z_\infty)\). All initial points in this neighborhood are included, proving openness, without incorrectly claiming attraction to a particular individual cycle.

**4. Distinct singular scales.** The identity \(1-T+m^2=\det(I-M_0^2)=\det(I-M_0)\det(I+M_0)\) yields
\[
A_+^2=\frac{a(a-2c)\bigl(4+2h(c-a)+h^2a(a-2c)\bigr)}{h^2a^2}.
\]
Moreover \(1+T+m^2\to4\), giving the two stated asymptotics and their ratio. For \((a,c,h)=(3,1,1/10)\), direct rational substitution gives \(m=83/100\), \(T=79/50\) and
\[
D(A)=\frac{6889-9A^2}{10000},\quad
1-T+D(A)=\frac{9(121-A^2)}{10000},\quad
1+T+D(A)=\frac{32689-9A^2}{10000}.
\]
These establish the exact benchmark without numerical root finding.

## Verification

The accompanying `verify.py` uses exact symbolic polynomial arithmetic to reconstruct the Euler map, its axis two-cycle, the two-step Jacobian, the transverse characteristic polynomial, the two Schur walls, their rational benchmark, and the quadratic order of axial drift. It also checks representative amplitude regimes numerically as supplementary diagnostics. Run `python verify.py` with Python 3 and SymPy installed. The general proof is the preceding algebra and contraction argument; floating-point samples are neither the proof nor an exhaustive orbit search.

## Relationship to prior work

Rana, Uddin, Santra and Mahapatra (2023) study fixed-point stability, Neimark–Sacker bifurcation, period-doubling near equilibria and numerical chaotic behavior of a forward-Euler Chen map. Their displayed analysis does not supply an axial period-two continuum, its amplitude-dependent transverse characteristic polynomial, two distinct stability walls, or the open-family attraction result. Rana and Uddin (2022) analyze the related but different discrete Lü system, whose middle equation omits the \((c-a)x\) term; its fixed-point results do not imply the present Chen-specific thresholds. Standard Floquet/Schur theory and standard normal-attraction principles are used as known methods, not claimed as new.

## Limitations

Only the axial period-two family is classified; other periodic orbits, their basins, and global bounded dynamics are not. The continuum exists on the Euler-step resonance surface \(hb=2\), so it need not persist as such away from resonance. The open-set attraction is toward a **member of the family**, with nonconstant limiting amplitude. At the two exact walls, no nonlinear bifurcation classification is asserted. Large axial amplitudes may lie outside a physically meaningful modeling region. The originating article's accessible HTML text suppresses some displayed equations; the explicitly written map here is independently defined by the standard Chen equations and the stated forward-Euler rule. Novelty is assessed relative to inspected sources, not independently certified or guaranteed against unindexed equivalent work.

## References

1. S. M. S. Rana, M. J. Uddin, P. K. Santra and G. S. Mahapatra, *Chaotic Dynamics and Control of a Discrete-Time Chen System*, Mathematical Problems in Engineering (2023), article 7795246; first published 2023-05-22. DOI: https://doi.org/10.1155/2023/7795246.
2. S. M. S. Rana and M. J. Uddin, *Dynamics of a Discrete-Time Chaotic Lü System*, Pan-American Journal of Mathematics 1 (2022), article 7, DOI: https://doi.org/10.28919/cpr-pajm/1-7.
3. T. Lü and X. Zhang, *Darboux Polynomials and Algebraic Integrability of the Chen System*, International Journal of Bifurcation and Chaos 17 (2007), 2739–2748, DOI: https://doi.org/10.1142/S0218127407018725 (standard Chen vector-field normalization).
