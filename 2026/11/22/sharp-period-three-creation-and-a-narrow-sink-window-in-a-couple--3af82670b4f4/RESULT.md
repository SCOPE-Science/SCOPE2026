# Sharp period-three creation and a narrow sink window in a coupled quadratic map

## Finding
For the map \(F_b(x,y)=(x+3y/2,\,b x(1-x))\), \(b>0\), write \(s=9b^2/4\). The complete real primitive-period-three census is: no cycles for \(0<s<24\), exactly one for \(s=24\), and exactly two for \(s>24\). At the threshold \(b=4\sqrt6/3\), the single cycle has return multipliers \(1,0\). Above it the two cycles have trace and determinant pairs
\[
 (\tau_\pm,\Delta_\pm)=(1\pm\sqrt{s-24},\ \pm(s+4)\sqrt{s-24}).
\]
Let \(s_c>24\) be the unique solution of \((s_c+4)^2(s_c-24)=1\), approximately \(24.0012753940\). The plus-sign cycle is attracting exactly for \(24<s<s_c\); at \(s=s_c\) its eigenvalues have modulus one, and for \(s>s_c\) it is unstable. The minus-sign cycle is unstable for every \(s>24\). This is an exact two-stage stability classification for the newly created real three-cycles.

## Assumptions and scope
The state space is the entire real plane, not the biological positive quadrant. The coupling is fixed at the naturally distinguished value \(a=1\) in the two-parameter model \((x,y)\mapsto(ax+3y/2,bx(1-x))\); \(b>0\). A primitive period-three cycle consists of three distinct phase points, counted modulo cyclic rotation. A sink means both eigenvalues of the three-step Jacobian lie strictly inside the unit disk. No claim is made about other periods or global basins.

## Proof
Introduce \(v=3y/2\) and \(c=3b/2\), giving the linearly conjugate map \(G_c(x,v)=(x+v,c x(1-x))\) with \(c>0\), \(s=c^2\). Put \(t=x(1-x)\), \(z=s t\). If \((X,V)=G_c^3(x,v)\), polynomial elimination in \(v\) gives, up to a nonzero scalar, the exact resultant
\[
 \operatorname{Res}_{v}(X-x,V-v)=c^2 x(x-1)\big[z^3-(s+3)(z+2)\big].
\]
For \(x=0\) and \(x=1\) the unique solution is \(v=0\), so these are the two fixed points. For any remaining resultant root, the linear subresultant has coefficient \(2c(1+z)\) in \(v\). Its solution is
\[
 v=-\frac{c t\,[z+c(2x-1)+1]}{2(1+z)}.
\]
The cubic \(H_s(z)=z^3-(s+3)(z+2)\) has \(H_s(-1)=-s-4\ne0\). Thus this expression is defined at every periodic root, and substitution in the two period-three equations verifies both equations exactly. Hence no extraneous resultant roots occur. The polynomial identities and substitution are reproduced by `verify.py`.

The discriminant of \(H_s\) is \(4(s+3)^2(s-24)\). When \(s<24\), \(H_s\) has one real root, which is positive and greater than \(s/4\) since \(H_s(0)<0\) and
\[
 H_s(s/4)=\frac{(s-24)(s+4)^2}{64}<0.
\]
But a real \(x\) requires \(t\le1/4\), hence \(z\le s/4\), so no nonfixed real three-periodic point exists. When \(s=24\), \(H_s(z)=(z-6)(z+3)^2\), producing exactly the three distinct values \(x=1/2\) and \(x=(1\pm\sqrt{3/2})/2\). These three points form one cycle, explicitly in the \(G_c\) coordinates:
\[
 (x,v)=\left(\tfrac12,-\tfrac{\sqrt6}{4}\right)
 \mapsto\left(\tfrac{2-\sqrt6}{4},\tfrac{\sqrt6}{2}\right)
 \mapsto\left(\tfrac{2+\sqrt6}{4},-\tfrac{\sqrt6}{4}\right)\mapsto\left(\tfrac12,-\tfrac{\sqrt6}{4}\right).
\]
When \(s>24\), the cubic has three distinct real roots: two negative and one positive (by the cubic's sign and its negative local maximum). Its positive root lies strictly below \(s/4\), using \(H_s(s/4)>0\). Each root produces two distinct real \(x\) values by \(x(1-x)=z/s\); there are exactly six nonfixed three-periodic points and hence two three-cycles.

At an orbit whose consecutive first coordinates are \(x_0,x_1,x_2\), the Jacobian of \(G_c\) is \(J(x)=\left(\begin{smallmatrix}1&1\\c(1-2x)&0\end{smallmatrix}\right)\). Therefore
\[
 \tau=1+c(3-2(x_0+x_1+x_2)),\qquad
 \Delta=c^3\prod_{j=0}^2(2x_j-1).
\]
Substitution of the displayed formula for \(v\), followed by polynomial reduction modulo \(H_s(sx(1-x))\), yields the exact identities
\[
 (\tau-1)^2=s-24,\qquad \Delta=(s+4)(\tau-1).
\]
Both signs occur because the involution \(x\mapsto1-x\) exchanges the six roots in pairs and reverses the sign of \(\tau-1\). At \(s=24\) the multipliers are \(1,0\). For \(s>24\), write \(d=\sqrt{s-24}>0\). On the negative branch \(1-\tau_-+\Delta_-=-(s+3)d<0\), which excludes Schur stability. For the positive branch, the Jury inequalities are \(1-\tau_++\Delta_+=(s+3)d>0\), \(1+\tau_++\Delta_+=2+(s+5)d>0\), and \(1-\Delta_+=1-(s+4)d>0\). The last holds exactly for \(24<s<s_c\), with a unique endpoint since \((s+4)\sqrt{s-24}\) increases strictly. At equality the characteristic roots have product one, nonreal conjugate roots because \(\tau_+\in(0,2)\) and \(\Delta_+=1\); they therefore lie on the unit circle. This proves the complete assertion.

## Verification
`verify.py` independently computes the polynomial resultant and linear subresultant; verifies the factorization and both trace/determinant reduction identities exactly in rational polynomial algebra; and tests sample values on either side of the creation and sink thresholds. The exact identities are the proof certificates; the numerical samples are only diagnostics.

## Relationship to prior work
Liu and Zhong (2024) introduce the two-parameter square-term map and analyze fixed-point stability plus local Neimark–Sacker, transcritical and flip bifurcations; their stated results do not provide a complete real period-three census or its sharp sink interval on \(a=1\). A broader algebraic fixed-point counting principle allows up to eight complex solutions of the third iterate, but by itself does not decide reality, boundary multiplicity or Floquet stability. The present calculation resolves these finer questions on a structurally distinguished parameter section.

## Limitations
The analysis concerns only the full-plane \(a=1\), \(b>0\) family and primitive period three. Neither global attraction nor higher-period orbit counts are established. A further independent literature and mathematical review would be useful before priority claims or publication.

## References
L. Liu and X. Zhong, *Research on Stability and Bifurcation for Two-Dimensional Two-Parameter Squared Discrete Dynamical Systems*, Mathematics 12 (2024), 2423, published August 4, 2024. https://doi.org/10.3390/math12152423.
