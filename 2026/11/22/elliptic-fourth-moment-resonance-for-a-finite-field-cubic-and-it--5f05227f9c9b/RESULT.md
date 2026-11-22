# Elliptic fourth-moment resonance for a finite-field cubic and its tangent line

## Finding
Let \(q\) be an odd prime power, \(F=\mathbb F_q\), and
\[
C=\{(t,t^3):t\in F\},\quad L=\{(t,0):t\in F\},\quad S=C\cup L.
\]
The line \(L\) has third-order contact with the cubic graph at its unique common point, the origin. Let \(r_S(x,y)\) count **ordered** sums of two points of \(S\), and let
\(\mathcal E(S)=\sum_{x,y\in F}r_S(x,y)^2\) be the additive energy. The exact energy, for **every** odd prime-power field, is
\[
\boxed{\mathcal E(S)=\begin{cases}
2q^3+6q^2-12q+5,&\operatorname{char}F=3,\\
q^3+13q^2-27q+14,&\operatorname{char}F\ne3,\ q\equiv2\pmod3,\\
q^3+25q^2-63q+38-4(q-1)a_q,&\operatorname{char}F\ne3,\ q\equiv1\pmod3.
\end{cases}}
\]
In the last line, \(a_q=q+1-\#E(F)\) is the ordinary elliptic Frobenius trace of the nonsingular \(j=0\) curve
\[
E:\quad v^2=(4u^3-1)/3.
\]
There is therefore a genuinely arithmetic correction in the split-cube regime, with \(|a_q|\le2\sqrt q\); when cubing is bijective, this trace disappears. In characteristic three the cubic graph is an additive subgroup and the energy instead has a different cubic leading coefficient.

More precisely, the theorem determines the **entire two-sum multiplicity function**. When \(\operatorname{char}F\ne3\), let \(\chi\) be the quadratic character with \(\chi(0)=0\), put \(c=\chi(-3)\), and let \(\nu(z)=\#\{u\in F:u^3=z\}\). Then
\[
r_S(0,0)=2q-1,\quad r_S(0,y)=2\nu(y)\quad(y\ne0),
\]
\[
r_S(x,0)=q+1+c\quad(x\ne0),
\]
and for \(x,y\ne0\), with \(z=y/x^3\),
\[
\boxed{r_S(x,y)=1+\chi\bigl((4z-1)/3\bigr)+2\nu(z)-2\mathbf1_{\{z=1\}}.}
\]
When \(\operatorname{char}F=3\), the complete law simplifies to \(r_S(0,0)=2q-1\), \(r_S(x,y)=q\) at every other point of \(S\), and \(r_S(x,y)=2\) off \(S\).

For an additive character \(\psi\) of \(F\), normalize the Fourier transform on \(F^2\) unitarily by
\[
\widehat f(\xi)=q^{-1}\sum_{v\in F^2}f(v)\psi(-\xi\cdot v).
\]
Then the exactly determined fourth Fourier moment is
\[
\sum_{\xi\in F^2}|\widehat{\mathbf1_S}(\xi)|^4=\mathcal E(S)/q^2.
\]
For \(q=p^n\) of characteristic \(p>3\), the trace in the energy is computable entirely from a single prime-field count: start with \(a_{p^0}=2\), set \(a_{p}=p+1-\#E(\mathbb F_p)\), and iterate
\[
a_{p^n}=a_p a_{p^{n-1}}-p a_{p^{n-2}}\quad(n\ge2).
\]

## Assumptions and scope
All fields have odd cardinality \(q=p^n\); no inference is made for characteristic two. The set \(S\) has exactly \(2q-1\) points. All collisions and convolutions use counting measure and ordered pairs; \(\nu(0)=1\). The affine line is specifically the tangent \(y=0\) at the origin, not an arbitrary translated line. Every division by three or by a nonzero field element occurs only in characteristic different from three.

## Proof
**1. Decompose the union convolution.** Write \(A=\mathbf1_C\), \(B=\mathbf1_L\), and \(\delta=\mathbf1_{\{(0,0)\}}\). Since \(C\cap L=\{(0,0)\}\), we have \(\mathbf1_S=A+B-\delta\), hence
\[
r_S=A*A+2A*B+B*B-2A-2B+\delta.
\]
At \((x,y)\), the mixed convolution is \((A*B)(x,y)=\nu(y)\), independently of \(x\), and \((B*B)(x,y)=q\mathbf1_{\{y=0\}}\).

**2. Evaluate the cubic self-convolution.** For \(x\ne0\) in characteristic different from three, fixing a pair of curve parameters \(t,x-t\) gives
\[
y=t^3+(x-t)^3=x^3-3xt(x-t).
\]
The quadratic equation for \(t\) has discriminant \((4y-x^3)/(3x)\). Its number of roots is
\[
(A*A)(x,y)=1+\chi((4y-x^3)/(3x)).
\]
At \(x=0\), since the cubic is odd, \((A*A)(0,0)=q\) and \((A*A)(0,y)=0\) for \(y\ne0\). Substitution into the decomposition proves the four complete fiber cases displayed above. In particular, when \(x,y\ne0\) the discriminant is \(x^2(4z-1)/3\), making its character independent of \(x\).

**3. Sum exact squares.** Let \(g=\gcd(3,q-1)\) and let \(c_z=\chi((4z-1)/3)\) for \(z\ne0\). Multiplicative-group cyclicity and a linear character sum give
\[
\sum_{z\ne0}\nu(z)=q-1,\qquad
\sum_{z\ne0}\nu(z)^2=(q-1)g,
\]
\[
\sum_{z\ne0}c_z=-\chi(-1/3)=-c,\qquad
\sum_{z\ne0}c_z^2=q-2.
\]
Put \(T_q=\sum_{u\in F}\chi((4u^3-1)/3)\). Since \(\nu\) counts cube roots,
\(\sum_{z\ne0}c_z\nu(z)=T_q-c\). Moreover \(c_1=1\) and \(\nu(1)=g\). Expanding the square, with no omitted exceptional root, yields
\[
\sum_{z\ne0}(1+c_z+2\nu(z)-2\mathbf1_{\{z=1\}})^2
=6q-11-6c+4(q-3)g+4T_q.
\]
The other convolution sectors contribute \((2q-1)^2\), \(4(q-1)g\), and \((q-1)(q+1+c)^2\). Consequently,
\[
\mathcal E(S)=q^3+11q^2-21q+10+2(q-1)(q-2)(c+2g)+4(q-1)T_q.
\]
If \(q\equiv2\pmod3\), cubing permutes \(F\), so \(g=1\) and \(T_q=0\); also \(-3\) is nonsquare, hence \(c=-1\). If \(q\equiv1\pmod3\), we have \(g=3\) and \(c=1\), because the roots of \(u^2+u+1\) belong to \(F\). The curve \(v^2=(4u^3-1)/3\) is nonsingular (its derivative is nonzero at its roots in characteristic greater than three), and its affine point count is \(q+T_q\), so \(a_q=-T_q\). The displayed two polynomial/elliptic branches follow. The trace recurrence is the standard degree-two Frobenius characteristic polynomial of this fixed elliptic curve, and Hasse's bound gives \(|a_q|\le2\sqrt q\).

**4. Characteristic three.** Now the map \(t\mapsto t^3\) is additive. Thus \(C\) and \(L\) are additive subgroups of the additive group \(F^2\), each of size \(q\), with trivial intersection and complementary direct sum \(F^2=C\oplus L\). Therefore \(A*A=qA\), \(B*B=qB\), and \(A*B=\mathbf1_{F^2}\). The decomposition gives \(r_S=2q-1\) at zero, \(r_S=q\) at nonzero points of the two axes, and \(r_S=2\) elsewhere. There are \(2(q-1)\) nonzero points of \(S\) and \((q-1)^2\) points off \(S\); summing squares proves \(2q^3+6q^2-12q+5\).

**5. Fourier moment.** Expand the fourth power of the unitary Fourier transform and use \(\sum_{\xi\in F^2}\psi(\xi\cdot w)=q^2\mathbf1_{\{w=0\}}\). Each ordered additive collision contributes \(q^{-2}\) and every noncollision contributes zero. This proves the normalized identity.

## Verification
Run `python3 verify.py` using only the Python standard library. It independently enumerates the entire union, its ordered two-sum convolution at **every** target, the total fourth moment, and the displayed formulas over the 14 prime fields of orders \(3,5,7,11,13,17,19,23,29,31,37,41,43,47\). It also constructs the extension fields of orders \(9,25,49,121\) explicitly as quadratic polynomial quotients and verifies every convolution fiber and the elliptic Frobenius trace recurrence. The observed final line is `VERIFY_OK prime_cases=14 quadratic_extension_cases=4 exact_fibers=yes max_order=121`. Finite testing corroborates the algebra but is not a substitute for the proof over arbitrary prime powers.

## Relationship to prior work
The finite-field Fourier extension programme of Biswas–Carneiro–Flock–Oliveira e Silva–Stovall–Tautges [1] provides a recent motivated setting, but their moment-curve theorem concerns different polynomial supports and sharp weighted operator norms, not the full convolution of a cubic graph plus its tangent line. Hughes–Wooley [2] analyze the curve \((t,t^3)\) in integer discrete restriction, without this finite-field arrangement. Two publicly indexed cubic-graph studies [3,4] do provide, respectively, complete two-sum fibers and the sharp weighted fourth-moment norm for the **unaugmented** cubic graph. The cubic self-convolution used in Step 2 is therefore not asserted to be new. Their stated conclusions do not include the tangent-line mixed convolution, the union's full two-sum law, or the resulting elliptic trace of its fourth moment. This distinction is about conclusions and logical implications, not wording: adding the line changes the support and introduces cross terms absent from the published self-convolution. As with all such exact calculations, an older stronger all-arrangements formula or unpublished equivalent derivation may exist.

## Limitations
The statement fixes the tangent line \(y=0\) and does not classify arbitrary lines or weighted Fourier-extension maximizers. It does not estimate higher moments. The elliptic trace is identified by an exact curve and prime-power recurrence, but a closed uniform elementary formula in the split-cube case is not claimed. No independent mathematical audit has been performed.

## References
1. C. Biswas, E. Carneiro, T. C. Flock, D. Oliveira e Silva, B. Stovall, J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields*, arXiv:2508.08377v1, first publicly posted 2025-08-11, https://arxiv.org/abs/2508.08377.
2. K. Hughes, T. D. Wooley, *Discrete restriction for \((x,x^3)\) and related topics*, arXiv:1911.12262v1, 2019-11-27, https://arxiv.org/abs/1911.12262.
3. *Complete pair-sum fibers of the cubic graph over odd residue rings*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-pair-sum-fibers-of-the-cubic-graph-over-odd-residue-rin--1bbc7ea862f6.
4. *Exact sharp finite-field cubic-graph \(L^2\) to \(L^4\) extension norm and extremizers*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-sharp-finite-field-cubic-graph-l-2-to-l-4-extension-norm-a--2db777d1e47b.
