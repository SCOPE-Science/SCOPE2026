# Rank strata and sharp phase-resonance instability for complex-geometric cyclic Gabor measurements

## Finding
Fix an integer \(N\ge 2\). For \(z\in\mathbb C\), let \(g_z\in\mathbb C^N\) be the normalized geometric window \(g_z(j)=z^j/(\sum_{h=0}^{N-1}|z|^{2h})^{1/2}\) for \(0\le j<N\), with \(0^0=1\). Put \(\omega=e^{2\pi i/N}\), \((T_a f)(j)=f(j-a\bmod N)\), and \((M_b f)(j)=\omega^{bj}f(j)\). The full cyclic Gabor intensity lifting is the complex-linear map
\[
\mathcal Q_z(X)(p,q)=\operatorname{tr}\bigl(X\,(M_qT_pg_z)(M_qT_pg_z)^*\bigr),\qquad X\in\mathbb C^{N\times N},\quad p,q\in\mathbb Z/N\mathbb Z.
\]
Equip the domain with Hilbert--Schmidt norm and the target with unweighted Euclidean norm. Define the normalized cyclic ambiguity coefficients
\[
A_z(a,b)=\sum_{j=0}^{N-1}g_z(j)\overline{g_z(j-a\bmod N)}\,\omega^{bj}.
\]
**Complete spectrum and rank:** The \(N^2\) singular values of \(\mathcal Q_z\), with multiplicities, are precisely \(\sqrt N\,|A_z(a,b)|\), for \(0\le a,b<N\). Its rank has the following exhaustive description:

- If \(z=0\), then \(\operatorname{rank}\mathcal Q_z=N\).
- If \(r=|z|\ne 0,1\), then \(\operatorname{rank}\mathcal Q_z=N^2-N/2\) precisely when \(N\) is even and \(z^N\in\mathbb R\); in every other such case the rank is \(N^2\). In the deficient case the zero singular values occur exactly at \(a=N/2\) and at the \(N/2\) modulation indices with \((-1)^b=-\operatorname{sgn}(z^N)\).
- If \(|z|=1\) and \(z^N=1\), then \(\operatorname{rank}\mathcal Q_z=N\).
- If \(|z|=1\) and \(z^N\ne1\), then
\[
\operatorname{rank}\mathcal Q_z=N^2+N-\sum_{a=0}^{N-1}\gcd(a,N)-\mathbf1_{\{N\ \mathrm{even},\ z^N=-1\}},
\]
where \(\gcd(0,N)=N\).

In particular, for every nonzero parameter off the unit circle, every odd cyclic order is fully matrix-informationally complete; for even order, the exceptional nonzero parameters form exactly the rays \(\operatorname{Im}(z^N)=0\), and each point of those rays away from the circle and origin has rank defect exactly \(N/2\).

**Sharp instability at a resonant ray:** Suppose \(N\) is even, \(r>0\), \(r\ne1\), \(\eta\in\{+1,-1\}\), and \(e^{iN\phi_0}=\eta\). Set \(z(\delta)=r e^{i(\phi_0+\delta/N)}\) for real \(\delta\to0\) with \(\delta\ne0\). Put \(p=1\) if \(\eta=1\), and \(p=0\) if \(\eta=-1\), and define
\[
D_p(N,r)=\max_{0\le b<N,\ b\equiv p\ (\mathrm{mod}\ 2)}|1-r^2\omega^b|.
\]
Then the ordinary spectral condition number of the invertible lifting satisfies the exact asymptotic
\[
\boxed{\displaystyle
\lim_{\delta\to0}|\delta|\,\operatorname{cond}_2\mathcal Q_{z(\delta)}
=\frac{|r^N-\eta|\,D_p(N,r)}{r^{N/2}|r^2-1|}.}
\]
More precisely, exactly \(N/2\) singular values vanish at the resonant ray; the slope of the one indexed by \((a,b)=(N/2,b)\), \(b\equiv p\pmod2\), is
\[
\boxed{\displaystyle
\lim_{\delta\to0}\frac{\sigma_{N/2,b}(\mathcal Q_{z(\delta)})}{|\delta|}
=\frac{\sqrt N\,r^{N/2}|r^2-1|}{|r^N-\eta|\,|1-r^2\omega^b|}.}
\]
Every other singular value has a strictly positive limit. The maximum in \(D_p\) is elementary:
\[
D_p(N,r)=\begin{cases}
1+r^2,&p\equiv N/2\pmod2,\\
\sqrt{1+r^4+2r^2\cos(2\pi/N)},&p\not\equiv N/2\pmod2.
\end{cases}
\]
All statements include \(N=2\).

## Assumptions and scope
The generating vector has the indexed finite geometric form shown above, not a periodic infinite exponential; cyclic wrap-around in \(T_a\) is essential. All observations \((p,q)\in(\mathbb Z/N\mathbb Z)^2\) are included with equal unit weight. The rank concerns the linear measurement of arbitrary complex matrices, rather than claiming a converse for nonlinear vector phase retrieval from rank-deficient measurements. Where the rank is \(N^2\), the lifting is injective and hence the associated intensity measurements distinguish rank-one projectors and signals up to global phase. No assertion about full-sparkness of the Gabor atom frame is made. All asymptotics in the phase parameter fix \(N\) and \(r\ne1\); they are not uniform as \(N\to\infty\) or \(r\to1\).

## Proof
**1. Weyl diagonalization.** The operators \(\{M_bT_a/\sqrt N:0\le a,b<N\}\) form an orthonormal Hilbert--Schmidt basis. Conjugating a Weyl operator by \(M_qT_p\) multiplies it by a character of the finite phase-space group. The projector orbit therefore has a character-table expansion with coefficient \(A_z(a,b)/\sqrt N\) in the \((a,b)\)-column. Orthogonality of the \(N^2\) phase-space characters shows that distinct columns are orthogonal and have length \(\sqrt N\,|A_z(a,b)|\). This proves the stated singular-value formula and the equality between rank and the number of nonzero ambiguity coefficients. Since \(\|g_z\|=1\), Cauchy--Schwarz gives \(|A_z(a,b)|\le1\), and \(A_z(0,0)=1\); thus the largest lifting singular value is \(\sqrt N\).

**2. Geometric-series identity away from the circle.** Let \(0<r=|z|\ne1\), write \(z=r e^{i\phi}\), \(W=z^N\), \(S=\sum_{j=0}^{N-1}r^{2j}\), and \(u=r^2\omega^b\). Splitting the cyclic sum at \(j=a\) gives, for every \(0\le a,b<N\),
\[
\boxed{\displaystyle
A_z(a,b)=\frac{r^{-a}e^{ia\phi}}{S}\,
\frac{\overline W(1-W)+(1-\overline W)u^a}{1-u}.}
\]
The denominator is nonzero because \(|u|=r^2\ne1\). At \(a=0\), the numerator is \(1-r^{2N}\ne0\). If the numerator vanishes for any \(a>0\), taking moduli of its two terms yields \(r^{2a}=r^N\), because \(|1-W|=|1-\overline W|\). Since \(r\ne1\), necessarily \(N\) is even and \(a=N/2\). There \(u^a=r^N(-1)^b\). If \((-1)^b=-1\), the numerator is \(r^N(1+r^N)(e^{-iN\phi}-1)\); if \((-1)^b=1\), it is \(r^N(1-r^N)(e^{-iN\phi}+1)\). This gives all zero locations and their exact count.

**3. Unit-circle and origin boundaries.** At \(r=1\), put \(\phi=\arg z\). Directly summing the two constant-phase portions gives
\[
A_z(a,0)=\frac{e^{ia\phi}}{N}\bigl((N-a)+a e^{-iN\phi}\bigr),
\]
while for \(b\ne0\),
\[
A_z(a,b)=\frac{e^{ia\phi}}N\,(e^{-iN\phi}-1)\,
\frac{1-\omega^{ab}}{1-\omega^b}.
\]
If \(z^N=1\), the only nonzero coefficients are \((a,0)\), giving rank \(N\). Otherwise, for each \(a\), exactly \(\gcd(a,N)-1\) indices \(b\ne0\) satisfy \(\omega^{ab}=1\); additionally \(A_z(a,0)=0\) exactly when \(N\) is even, \(a=N/2\), and \(z^N=-1\). Summing the counts gives the formula. At \(z=0\), the window is the first standard basis vector; exactly the \(N\) coefficients \(A_z(0,b)\) are nonzero.

**4. The transverse singular-value slopes.** Fix the even-order resonance \(z(0)^N=\eta r^N\) and the indicated parity. At the \(N/2\) zero indices, the numerator in Step 2 has modulus \(r^N(1+r^N)2|\sin(\delta/2)|\) if \(\eta=1\), and \(r^N|1-r^N|2|\sin(\delta/2)|\) if \(\eta=-1\). Use \(S=|r^{2N}-1|/|r^2-1|\) and \(2|\sin(\delta/2)|/|\delta|\to1\) to obtain the individual slopes. The remaining finitely many ambiguity coefficients are nonzero at \(\delta=0\), so their moduli are uniformly separated from zero for sufficiently small \(\delta\). Consequently the smallest singular value comes from the largest denominator \(|1-r^2\omega^b|\) among the collapsing indices, establishing the condition-number formula. The stated closed form for \(D_p\) follows by selecting the parity-constrained root of unity closest to \(-1\).

## Verification
The standalone Python program `check_geometric_gabor.py` constructs the full rank-one projector measurement matrix, independently computes its singular values and compares them with \(\sqrt N|A_z|\). It also checks the closed geometric-series formula, the exact rank strata, and the sharp transverse condition-number limit for several resonant branches, including the smallest even order. The reported check run passed 305 assertions. These finite calculations are consistency tests; the exact all-order conclusions follow from the proof above, not from extrapolating the test range.

## Relationship to prior work
Bojarovska and Flinth (first posted March 19, 2015) prove the general nonzero-ambiguity sufficient criterion for cyclic Gabor phase retrieval and relate the projector orbit to frame bounds; that general diagonalization is used here, not claimed as new. Führ and Oussa (first posted January 21, 2022) study phase-retrievable nilpotent-group orbits and the finite Heisenberg representation, motivating explicit window selection. Li (first posted September 9, 2026) uses one special complex-geometric seed with its exponent chosen so that \(\gamma^N=2i\), obtains a summable ambiguity expression, and proves a polynomial lower margin for that fixed seed. Its fixed-seed nonvanishing and stability bounds are not new claims here. The present theorem instead supplies the *entire* complex-geometric parameter discriminant, exact ranks also on the flat-unit-circle boundary, and the individual sharp singular-value slopes at all even-order resonant rays. These parameter-wide assertions are not stated in those inspected sources; their algebraic proximity, especially to Li's geometric-series argument, is a real priority risk.

## Limitations
The result is restricted to a single explicitly parametrized cyclic-window family and full unweighted linear matrix lifting. It does not prove full spark, give an optimal window across arbitrary families, prove nonlinear phase-retrieval failure in the rank-deficient cases, or provide asymptotics uniform in dimension or radius. The analytic formulas are exact; the novelty assessment remains provisional because earlier work might contain an equivalent parameter-discriminant formulation. Independent mathematical validation has not been performed.

## References
1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, March 19, 2015; Journal of Fourier Analysis and Applications 22 (2016), 542–567. https://arxiv.org/abs/1503.05800
2. H. Führ and V. Oussa, *Phase retrieval for nilpotent groups*, arXiv:2201.08654v1, January 21, 2022; Journal of Fourier Analysis and Applications 29 (2023), article 47. https://arxiv.org/abs/2201.08654
3. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614v1, September 9, 2026, especially Theorem 3.8 and its geometric seed. https://arxiv.org/abs/2609.09614
