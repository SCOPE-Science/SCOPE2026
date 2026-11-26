# Additive energy of a finite-field cubic graph and its tangent line

## Finding

Let \(F=\mathbb F_q\), where \(q\) is odd. Set \(C=\{(t,t^3):t\in F\}\), \(L=\{(t,0):t\in F\}\), and \(S=C\cup L\). The line \(L\) has third-order contact with \(C\) at their only intersection. Let \(r_S(w)=\#\{(s_1,s_2)\in S^2:s_1+s_2=w\}\) count ordered pairs, and put \(\mathcal E(S)=\sum_w r_S(w)^2\). Then
\[
\mathcal E(S)=\begin{cases}
2q^3+6q^2-12q+5,&\operatorname{char}F=3,\\
q^3+13q^2-27q+14,&\operatorname{char}F\ne3,\ q\equiv2\pmod3,\\
q^3+25q^2-63q+38-4(q-1)a_q,&\operatorname{char}F\ne3,\ q\equiv1\pmod3,
\end{cases}
\]
where \(a_q=q+1-\#E(F)\) is the Frobenius trace of the smooth projective elliptic curve \(E:v^2=(4u^3-1)/3\) in the third branch. In particular, \(|a_q|\le2\sqrt q\). For \(q=p^n\), \(p>3\), the trace of this fixed curve is determined by \(a_{p^0}=2\), the prime-field trace \(a_p\), and \(a_{p^n}=a_pa_{p^{n-1}}-pa_{p^{n-2}}\) for \(n\ge2\).

For any **nontrivial** additive character \(\psi:F\to\mathbb C^\times\), the unitary transform \(\widehat f(\xi)=q^{-1}\sum_{w\in F^2} f(w)\psi(-\xi\cdot w)\) gives
\[
\sum_{\xi\in F^2}|\widehat{\mathbf1_S}(\xi)|^4=q^{-2}\mathcal E(S).
\]
This is the standard energy-to-Fourier conversion, not a new transform identity.

## Assumptions and scope

The line is the specified tangent through the origin; arbitrary affine lines are not covered. Convolution uses counting measure. The description applies to odd prime powers, including quadratic and higher extensions; all field divisions by \(3\) occur only when \(\operatorname{char}F\ne3\). The nontriviality condition is needed for the Fourier-moment identity, not for the energy calculation.

## Proof

Write \(A=\mathbf1_C\), \(B=\mathbf1_L\), \(\delta=\mathbf1_{\{(0,0)\}}\), and \(\nu(y)=\#\{u:u^3=y\}\). Using \(\mathbf1_S=A+B-\delta\) gives
\[
r_S=A*A+2A*B+B*B-2A-2B+\delta,
\qquad (A*B)(x,y)=\nu(y),\qquad (B*B)(x,y)=q\mathbf1_{\{y=0\}}.
\]

In characteristic three, cubing is additive and \(F^2=C\oplus L\) as additive groups. Thus \(A*A=qA\), \(B*B=qB\), and \(A*B=\mathbf1_{F^2}\). The multiplicities are \(2q-1\) at zero, \(q\) on the \(2(q-1)\) nonzero points of \(S\), and \(2\) on the \((q-1)^2\) other points. This gives the first branch.

In the remaining characteristics let \(\chi\) be the quadratic character extended by \(\chi(0)=0\), and write \(c=\chi(-3)\). For \(x\ne0\), solving \(y=t^3+(x-t)^3\) is a quadratic discriminant calculation with discriminant \((4y-x^3)/(3x)\). At \(x=0\), the cubic self-convolution is \(q\) for \(y=0\) and zero otherwise. Substitution gives the auxiliary full multiplicity law:
\[
\begin{aligned}
r_S(0,0)&=2q-1, & r_S(0,y)&=2\nu(y)\quad (y\ne0),\\
r_S(x,0)&=q+1+c\quad (x\ne0), &
r_S(x,y)&=1+c_z+2\nu(z)-2\mathbf1_{\{z=1\}}\quad (xy\ne0),
\end{aligned}
\]
where \(z=y/x^3\) and \(c_z=\chi((4z-1)/3)\).

Put \(g=\gcd(3,q-1)\) and \(T_q=\sum_{u\in F}\chi((4u^3-1)/3)\). Over \(z\ne0\) the sums of \(\nu,\nu^2,c_z,c_z^2,c_z\nu\) are, respectively, \(q-1,(q-1)g,-c,q-2,T_q-c\). The first two follow from cyclicity of \(F^\times\), the next two from the linear character argument, and the last by grouping nonzero cubes and removing the contribution \(c\) from \(u=0\). At \(z=1\), \(c_1=1\) and \(\nu(1)=g\). Consequently,
\[
\sum_{z\ne0}(1+c_z+2\nu(z)-2\mathbf1_{\{z=1\}})^2
=6q-11-6c+4(q-3)g+4T_q.
\]
Multiply this by \(q-1\) and add the axis and origin contributions \(4(q-1)g\), \((q-1)(q+1+c)^2\), and \((2q-1)^2\). The total is
\[
q^3+11q^2-21q+10+2(q-1)(q-2)(c+2g)+4(q-1)T_q.
\]
The discriminant \(-3\) of \(U^2+U+1\) is a square precisely when there are primitive cube roots of unity in \(F\). For \(q\equiv2\pmod3\), this gives \(c=-1,g=1\), and bijective cubing makes \(T_q=0\). For \(q\equiv1\pmod3\), take \(c=1,g=3\). The polynomial \((4u^3-1)/3\) has distinct roots; adding the single point at infinity to the affine point count \(q+T_q\) gives \(a_q=-T_q\). The two branches follow, as do the Hasse bound and the trace recurrence by the elliptic Frobenius characteristic polynomial.

Finally, for \(\psi\) nontrivial, the sum over \(\xi\in F^2\) of \(\psi(\xi\cdot w)\) is \(q^2\) at \(w=0\) and zero otherwise: for \(w\ne0\) the linear map onto \(F\) is surjective, and a nontrivial character sums to zero. In the fourth-moment expansion the surviving ordered tuples are exactly the additive collisions, with weight \(q^{-2}\). The trivial character would instead give \(|S|^4/q^2\).

## Verification

The accompanying `verify.py` can enumerate each convolution fiber and the energy by exact arithmetic in fourteen prime fields and four quadratic extensions; it also checks the quadratic-extension trace relation where the elliptic curve is defined. It checks the energy numerically by exact enumeration, not a separate transform calculation. The Fourier identity and general field ranges follow from the proof, not those finite checks.

## Relationship to prior work and limitations

The planar cubic's self-convolution is prior input. The complete union multiplicities follow directly from it and the elementary line and mixed terms; they are included for the calculation, not asserted to be a separate novelty. Biswas–Carneiro–Flock–Oliveira e Silva–Stovall–Tautges (arXiv:2508.08377) treat the full finite-field moment curve. Hughes–Wooley (arXiv:1911.12262) treat the integer cubic restriction problem. Resultary records `2026/11/8/SCOPE-complete-pair-sum-fibers-of-the-cubic-graph-over-odd-residue-rin--1bbc7ea862f6` and `2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b` give the graph fibers in odd residue rings and sharp finite-field cubic graph extension, respectively. The three-dimensional tangent union in `2026/11/22/SCOPE-two-sum-spectral-strata-of-a-finite-field-twisted-cubic-and-its--13e9a7104876` is a different set with a different energy. The parabola-line and conic-tangent calculations `2026/11/22/SCOPE-exact-fourth-fourier-moments-for-a-finite-field-parabola-joined--ea1b104655f4` and `2026/11/22/SCOPE-sharp-two-sum-fourier-convolution-coverage-for-a-conic-and-its-t--f947e0197ff6` do not cover the planar cubic. Other graph energies are already known to involve elliptic traces, e.g. `2026/11/8/SCOPE-elliptic-frobenius-traces-in-the-additive-energy-of-the-inverse--32ae2e4d9598`.

The distinctive evaluation here is the all-odd-field energy of this tangent arrangement, in particular the mixed-collision contribution \(-4(q-1)a_q\) in the split-cube regime and its disappearance in the bijective regime. No historical priority is inferred from a shared catalogue date, and broader prior arrangement identities cannot be ruled out. No assertion is made about higher moments, extremizers, or an elementary trace formula.
