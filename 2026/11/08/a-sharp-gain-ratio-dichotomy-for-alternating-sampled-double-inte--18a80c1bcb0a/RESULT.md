# A sharp gain-ratio dichotomy for alternating sampled double-integrator feedback

## Finding

Fix positive proportional and derivative gains \(k_p,k_d\) and let \(r=k_p/k_d^2>0\). Consider a double-integrator plant with exact zero-order-held negative position/velocity feedback and two strictly positive sampling intervals that alternate periodically. Set \(L_r=\min\{2,2/r\}\). A constant sampled step of dimensionless length \(t=k_d h\) is exponentially stable exactly when \(0<t<L_r\).

For two such individually stable steps \(0<a,b<L_r\), the alternating two-step transition is exponentially stable if and only if
\[
S_r(a,b):=8-4(a+b)+4(1-r)ab+r^2a^2b^2>0.
\]
Equality corresponds to a Floquet multiplier \(-1\); a negative value gives a real Floquet multiplier strictly less than \(-1\). The strict two-step stability property holds for **every pair of individually stable steps** exactly when
\[
\boxed{0<r\le\tfrac12\quad\text{or}\quad r\ge2.}
\]
For every \(\tfrac12<r<2\), there exist two individually stable steps whose alternation is exponentially unstable. The optimal (not necessarily attained) value of the exact Jury margin is
\[
\inf_{0<a,b<L_r}S_r(a,b)=
\begin{cases}
0,&0<r\le\tfrac12,\\
-(2r-1)^2/r^2,&\tfrac12<r\le1,\\
-(2-r)^2/r^2,&1\le r<2,\\
8(1-2/r)^2,&r\ge2.
\end{cases}
\]
At \(r=1\), the exact individually stable choices \(a=3/4\) and \(b=7/4\) yield \(S_1(a,b)=-71/256\), providing a rational explicit instability witness.

## Assumptions and scope

For a scalar position \(x\), consider \(\ddot x(t)=u(t)\). At sampling instants \(t_j\), keep \(u(t)=-k_p x(t_j)-k_d\dot x(t_j)\) constant until the next instant. The gains \(k_p,k_d>0\) are **fixed across both phases**. All sampling intervals are positive, bounded and alternate exactly between \(h_1\) and \(h_2\). Define \(a=k_dh_1\), \(b=k_dh_2\), and the normalized state \(y=(x,\dot x/k_d)^T\); no approximation to the intersample flow is made. Exponential stability refers to the exact two-step discrete Floquet map, equivalently to the sampled trajectory and, because gaps remain bounded, the continuous-time held-feedback trajectory.

## Proof

Integrating constant acceleration exactly over a step \(h\) gives the dimensionless one-step state transition
\[
F_r(t)=\begin{pmatrix}
1-rt^2/2&t-t^2/2\\-rt&1-t
\end{pmatrix},\qquad t=k_dh.
\]
Its trace is \(T_r(t)=2-t-rt^2/2\) and its determinant is \(D_r(t)=1-t+rt^2/2\). By the strict second-order Jury test, the three positive quantities required for both eigenvalues to have modulus less than one are
\[
1-D_r(t)=t(1-rt/2),\qquad
1-T_r(t)+D_r(t)=rt^2,\qquad
1+T_r(t)+D_r(t)=4-2t.
\]
Consequently a single step is Schur stable precisely when \(0<t<L_r=\min\{2,2/r\}\).

For \(0<a,b<L_r\), write \(M=F_r(b)F_r(a)\), \(T=\operatorname{tr}(M)\), and \(D=\det(M)\). Matrix multiplication yields the exact identities
\[
D=D_r(a)D_r(b),\qquad
1-T+D=r(a+b)(a+b-ab),
\]
\[
2(1+T+D)=8-4(a+b)+4(1-r)ab+r^2a^2b^2=S_r(a,b).
\]
Individual Schur stability gives \(|D_r(a)|,|D_r(b)|<1\), hence \(1-D>0\). Moreover \(a+b-ab=\{a(2-b)+b(2-a)\}/2>0\) because each dimensionless step is less than \(2\). Hence \(1-T+D>0\), leaving only the sign of \(S_r(a,b)\). If \(S_r(a,b)=0\), the characteristic polynomial vanishes at \(-1\). If it is negative, that monic real quadratic, positive at negative infinity, has a real root below \(-1\); therefore its spectral radius exceeds one.

To optimize the sign globally, put \(L=L_r\) and \(z=ab\). Since \((L-a)(L-b)>0\),
\[
a+b<L+z/L.
\]
Because \(S_r(a,b)\) has coefficient \(-4\) on \(a+b\) at fixed \(ab=z\), it follows strictly that
\[
S_r(a,b)>S_r(L,z/L),\qquad 0<z<L^2.
\]
Every boundary pair \((L,c)\) with \(0<c<L\) is approached by interior pairs, so the infimum over the open square equals the infimum on that boundary edge (including its endpoints as limits).

When \(0<r\le1\), \(L=2\) and direct substitution gives
\[
S_r(2,c)=4c(1-2r)+4r^2c^2,\qquad 0\le c\le2.
\]
If \(r\le\tfrac12\), its minimum is \(0\) at \(c=0\). Otherwise its unique quadratic minimum occurs at \(c_*=(2r-1)/(2r^2)\in(0,2)\), and equals \(-(2r-1)^2/r^2\).

When \(r\ge1\), \(L=2/r\) and
\[
S_r(2/r,c)=4\big[c^2+(2/r-3)c+2-2/r\big],\qquad 0\le c\le2/r.
\]
For \(1\le r<2\), the minimizer \(c_*=3/2-1/r\) lies in \((0,2/r)\) and yields \(-(2-r)^2/r^2\). When \(r\ge2\), this quadratic decreases throughout \([0,2/r]\), so its minimum is the endpoint value \(8(1-2/r)^2\). The expressions agree at \(r=1\). The strict interior-to-boundary inequality proves that the zero boundary infima at \(r=1/2\) and \(r=2\) still imply strict stability for every admissible pair. For \(1/2<r<2\), a negative boundary minimum and continuity give strictly negative interior values, completing both directions.

For the rational witness \(r=1\), \(a=3/4\), \(b=7/4\), the two separate step determinants are \(17/32\), \(25/32\), while the period matrix satisfies
\[
\operatorname{tr}(M)=-1591/1024,\qquad\det(M)=425/1024,\qquad 1+\operatorname{tr}(M)+\det(M)=-71/512.
\]
These are all exact fractions; the negative final expression proves instability without relying on numerical eigenvalues.

## Verification

The standalone Python 3 and SymPy script `verify_periodic_pd.py` independently expands and factors the transition and Jury identities, checks the exact boundary candidates and rational instability witness, and compares exact-fraction Jury conditions against \(9{,}227\) rational two-step samples or witnesses. Execute `python verify_periodic_pd.py` after installing `sympy` as described in `requirements.txt`. Its recorded output is provided in `verification_output.txt`. The strict all-real-parameter conclusion is proved by the preceding inequalities, not inferred from grid testing.

## Relationship to prior work

Berberich, Wildhagen, Hertneck and Allgöwer [1] study model- and data-based stability of continuous-time systems under aperiodic sampling using robust-control and time-delay methods, including sufficient maximum-sampling-interval guarantees. Wildhagen, Berberich, Hirche and Allgöwer [2] develop improved integral-quadratic-constraint conditions for aperiodic sampling. Kotyczka and Lefèvre [3] calculate exact held-input discretizations of the double integrator but redesign controllers using symplectic integration. Sevim and Goren-Sumer [4] study nonuniformly sampled double-integrator consensus and give sufficient common-contraction criteria for arbitrary switching, rather than a sharp characterization of fixed-gain two-period products. None of the specific inspected treatments provides the displayed fixed-gain, **alternating two-period** if-and-only-if gain-ratio dichotomy or the exact Jury-margin infimum. The result does not claim that the underlying Schur/Jury tests, zero-order-hold formulas, or general time-delay methods are new.

## Limitations

The two-period analysis does not imply uniform stability under arbitrary switching among individually stable steps. The gains must remain constant across the two phases, the plant must be the ideal linear double integrator with full state feedback, and stability is asymptotic/exponential rather than a uniform transient-amplification estimate. At the two-step neutral boundary, a multiplier equals \(-1\), so strict exponential stability is absent. A publication-precedence risk remains in older sampled-data and switching-control literature, including sources whose full manuscripts were not accessible for inspection.

## References

[1] J. Berberich, S. Wildhagen, M. Hertneck, F. Allgöwer, *Data-driven analysis and control of continuous-time systems under aperiodic sampling*, first public preprint 2020-11-18, arXiv:2011.09221, https://arxiv.org/abs/2011.09221.

[2] S. Wildhagen, J. Berberich, S. Hirche, F. Allgöwer, *Improved stability conditions for systems under aperiodic sampling: model- and data-based analysis*, arXiv:2103.14353, https://arxiv.org/abs/2103.14353.

[3] P. Kotyczka, L. Lefèvre, *Discrete-Time Control Design Based on Symplectic Integration: Linear Systems*, IFAC World Congress 2020, https://ifatwww.et.uni-magdeburg.de/ifac2020/media/pdfs/1447.pdf.

[4] U. Sevim, L. Goren-Sumer, *Consensus of Double Integrator Multiagent Systems under Nonuniform Sampling and Changing Topology*, arXiv:2212.02922, https://arxiv.org/abs/2212.02922.
