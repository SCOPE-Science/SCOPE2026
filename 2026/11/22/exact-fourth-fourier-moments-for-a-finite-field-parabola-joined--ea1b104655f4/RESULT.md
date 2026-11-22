# Exact fourth Fourier moments for a finite-field parabola joined to an affine line

## Finding

Let \(q\) be an arbitrary odd prime power, \(\mathbb F_q\) its field, \(P=\{(x,x^2):x\in\mathbb F_q\}\), and \(L\) any affine line in \(\mathbb F_q^2\). Write \(S=P\cup L\), \(\chi\) for the quadratic character of \(\mathbb F_q\) extended by \(\chi(0)=0\), and \(\varepsilon=\chi(-1)\). The ordered additive energy is
\[
E(S)=\#\{(s_1,s_2,s_3,s_4)\in S^4:s_1+s_2=s_3+s_4\}.
\]
If \(L\) is nonvertical, express it as \(y=mx+c\) and put \(\Delta=m^2+4c\). For every \(q\ge3\), the complete classification is
\[
\begin{array}{c|l}
\text{line type}&E(P\cup L)\\\hline
\text{vertical}&q^3+12q^2-23q+11\\
\chi(\Delta)=-1& q^3+16q^2-(9+2\varepsilon)q\\
\Delta=0& q^3+(16+2\varepsilon)q^2-(35+6\varepsilon)q+19+4\varepsilon\\
\chi(\Delta)=1&q^3+16q^2-(73+2\varepsilon)q+90+8\varepsilon
\end{array}
\]
The second, third, and fourth cases mean a line meeting the parabola in respectively zero, one (tangent), or two field points. Vertical lines meet the parabola once but have a different fourth moment from tangent lines.

In particular, if \(\psi\) is any nontrivial additive character and
\[
\widehat{\mathbf1_S}(\xi)=q^{-1}\sum_{s\in S}\psi(-\xi\cdot s),
\]
then the exact unitary-normalized fourth Fourier moment is
\[
\sum_{\xi\in\mathbb F_q^2}|\widehat{\mathbf1_S}(\xi)|^4=q^{-2}E(S).
\]
Equivalently, for the extension map \(\mathcal E_Sf(\xi)=|S|^{-1}\sum_{s\in S}f(s)\psi(\xi\cdot s)\) with counting measure on the output,
\[
\|\mathcal E_S\|_{\ell^\infty(S)\to\ell^4(\mathbb F_q^2)}^4
=\frac{q^2E(S)}{|S|^4},
\]
where \(|S|=2q-1,2q,2q-1,2q-2\) in the four respective cases. This operator-norm reduction is standard; the contribution here is the complete energy evaluation.

## Assumptions and scope

All sums and convolutions use the additive group \(G=(\mathbb F_q^2,+)\). Write \((f*g)(z)=\sum_{w\in G}f(w)g(z-w)\). The quadratic character takes values \(0,\pm1\). There are no primality restrictions beyond odd characteristic, and no genericity assumptions on the position of the line. An affine bijection \(z\mapsto Az+b\) preserves additive energy because equality of two two-term sums is equivalent after applying the map.

## Proof

**1. Reduction to horizontal and vertical normal forms.** For \(L:y=mx+c\), the affine shear
\[
(x,y)\longmapsto (x-m/2,\ y-mx+m^2/4)
\]
fixes the standard shape of \(P\) and takes \(L\) to \(y=\Delta/4\). Multiplication of coordinates by \((r,r^2)\) (with \(r\ne0\)) preserves \(P\), so every nonzero square height reduces to \(1\), while the nonsquare case depends only on its quadratic character. For a vertical line \(x=a\), the parabolic affine translation \((x,y)\mapsto(x-a,y-2ax+a^2)\) reduces it to \(x=0\).

**2. Twofold representation formula for a horizontal line.** Let \(B_c=\{(u,c):u\in\mathbb F_q\}\), \(R_c=\{r\in\mathbb F_q:r^2=c\}\), and \(h=|R_c|\). Define
\[
\begin{aligned}
N_c(u,v)&=3+\chi(2v-u^2)+2\chi(v-c),\\
C_c(u,v)&=\sum_{r\in R_c}\mathbf1_{\{v=c+(u-r)^2\}},\\
D_c(u,v)&=\mathbf1_{\{v=2c\}}\left(q-2h+\sum_{r,s\in R_c}\mathbf1_{\{u=r+s\}}\right).
\end{aligned}
\]
Since \(\mathbf1_{P\cup B_c}=\mathbf1_P+\mathbf1_{B_c}-\sum_{r\in R_c}\mathbf1_{(r,c)}\), direct convolution gives the exact representation function
\[
\mathbf1_{P\cup B_c}*\mathbf1_{P\cup B_c}=N_c-2C_c+D_c.
\]
Indeed \(\mathbf1_P*\mathbf1_P(u,v)=1+\chi(2v-u^2)\), \(\mathbf1_P*\mathbf1_{B_c}(u,v)=1+\chi(v-c)\), and \(\mathbf1_{B_c}*\mathbf1_{B_c}(u,v)=q\mathbf1_{\{v=2c\}}\). The two intersection-removal terms and their self-convolution are exactly \(-2C_c\) and the remaining part of \(D_c\).

Put \(\langle F,H\rangle=\sum_{u,v}F(u,v)H(u,v)\), and \(\|F\|_2^2=\langle F,F\rangle\). The energy is
\[
E=\|N\|_2^2+2\langle N,D\rangle-4\langle N,C\rangle+\|D\|_2^2-4\langle D,C\rangle+4\|C\|_2^2.
\]
For the horizontal representatives, the six quantities on the right are exactly
\[
\begin{array}{c|c|c|c}
&\chi(c)=-1&c=0&c=1\\\hline
\|N\|_2^2&14q^2-9q&14q^2-5q&14q^2-q\\
\langle N,D\rangle&q(q-\varepsilon)&(q-2)(3q+\varepsilon(q-1))+3&(q-4)(5q-\varepsilon)+22\\
\langle N,C\rangle&0&6q-3&12q-6\\
\|D\|_2^2&q^3&q^3-4q^2+6q-3&q^3-8q^2+24q-26\\
\langle D,C\rangle&0&q-1&4q-10\\
\|C\|_2^2&0&q&2q+2
\end{array}
\]
Here is a reconstruction of the nontrivial entries. For \(a\ne0\), the standard quadratic-character identity is
\[
\sum_{t\in\mathbb F_q}\chi(at^2+b)=
\begin{cases}\chi(a)(q-1),&b=0,\\-\chi(a),&b\ne0.\end{cases}
\]
It follows by counting the pairs solving \(z^2=at^2+b\) (or by the bijection \((z-t,z+t)\) when \(a\) is a square), and remains true after multiplication by a nonsquare. Expanding the squares in \(N_c\), using that \(\sum_{u,v}\chi(2v-u^2)\chi(v-c)=q\chi(c)\), yields
\[
\|N_c\|_2^2=14q^2-5q+4q\chi(c).
\]
When \(c\) is nonsquare, \(R_c\) is empty, \(C_c=0\) and \(D_c=q\mathbf1_{v=2c}\); the \(N,D\) entry follows from \(\sum_u N_c(u,2c)=q-\varepsilon\). At \(c=0\), \(R_c=\{0\}\) and \(C_c=\mathbf1_{v=u^2}\); summing \(N_c\) on that curve gives \(6q-3\), and \(D_c\) has weights \(q-1\) at \((0,0)\) and \(q-2\) at all other points on \(v=0\). At \(c=1\), \(R_c=\{-1,1\}\); \(C_c\) consists of two parabolas meeting only at \(u=0\). Each contributes \(6q-3\) to \(\langle N,C\rangle\). The weights in \(D_c\) are \(q-2\) at \(u=0\), \(q-3\) at \(u=\pm2\), and \(q-4\) otherwise, with the three positions distinct even in characteristic \(3\). At \(v=2\), \(\sum_u N_1(u,2)=5q-\varepsilon\), while \(N_1(0,2)+N_1(2,2)+N_1(-2,2)=16\) with \(u=0\) counted twice in the correction, giving the displayed \(22\) total correction. The remaining three columns follow by squaring these stated weights and taking their intersections with the two curves. Substitution yields the three formulas.

**3. Vertical line.** For \(B=\{(0,v):v\in\mathbb F_q\}\), the intersection with \(P\) is \(\{(0,0)\}\). Set
\[
N(u,v)=3+\chi(2v-u^2),\qquad C(u,v)=\mathbf1_{\{v=u^2\}},\qquad D(u,v)=\mathbf1_{\{u=0\}}(q-2+\mathbf1_{\{v=0\}}).
\]
Again \(\mathbf1_{P\cup B}*\mathbf1_{P\cup B}=N-2C+D\). Direct character sums and the indicated one-point intersections give, in the same order as the preceding energy expansion,
\[
(\|N\|_2^2,\langle N,D\rangle,\langle N,C\rangle,\|D\|_2^2,\langle D,C\rangle,\|C\|_2^2)
=(10q^2-q,\ 3q(q-2)+3,\ 4q-1,\ q^3-4q^2+6q-3,\ q-1,\ q).
\]
The vertical formula follows immediately. These computations hold verbatim over all odd prime-power fields.

**4. Fourier and extension statements.** Character orthogonality gives \(\sum_{\xi\in G}|q^{-1}\sum_{s\in S}\psi(-\xi\cdot s)|^4=q^{-2}E(S)\). The extension norm from \(\ell^\infty(S)\) equals the \(\ell^4(G)\) norm of the extension of the constant-one function: expanding the fourth power produces a sum over additive quadruples; taking absolute values bounds each summand by \(\|f\|_\infty^4\), and constant input attains equality. Its fourth power is \(q^2E(S)/|S|^4\).

## Verification

The separate dependency-free \`checker.py\` computes exact finite-field arithmetic, explicitly constructs each support and its twofold sum multiplicities, and compares the resulting ordered energy with the displayed polynomial. It tests every affine line over \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\), and representative lines over \(\mathbb F_{11}\), \(\mathbb F_{13}\), \(\mathbb F_{17}\), \(\mathbb F_{19}\), \(\mathbb F_{25}\), and \(\mathbb F_{49}\); all 236 configurations pass. The general theorem follows from the character-sum proof, not from finite enumeration.

## Relationship to prior work

Iosevich, Li, and Yu (arXiv:2609.25404, originally public September 21, 2026), Section 8.2, formulate the general fourth-Fourier-moment/additive-energy identity; their Theorem 9.1 identifies the sharp constant-input \(\ell^\infty\)-to-\(\ell^4\) extension principle, and their later examples calculate complete paraboloids under affine-transitive symmetry. Those general identities are not claimed as new here. The present support \(P\cup L\) is a mixed, generally nontransitive set; its four specific polynomial evaluations and the arithmetic separation between line configurations do not follow from a parabola-only energy value or from a generic energy inequality. González-Riquelme and Oliveira e Silva (arXiv:2405.16647) study sharp extension from complete quadratic surfaces, while Lewko (arXiv:2606.22882) and Iosevich–Koh–Lewko (arXiv:1712.05549) study restriction estimates and additive-energy bounds for paraboloids. None of their inspected statements evaluates the mixed-support energy in the four cases above.

## Limitations

The result covers only the union with one entire affine line over fields of odd characteristic. It does not evaluate mixed supports from multiple lines or higher-degree curves, characterize \(L^2\to L^4\) extremizers, or imply sharp Fourier-algebra \(\ell^\infty\)-projection norms. The formulas evaluate the constant-input Fourier fourth moment and the \(\ell^\infty\to\ell^4\) extension norm, not an \(\ell^2\to\ell^4\) extension norm. Exhaustive tests cover only the finite instances listed; bibliographic completeness cannot be established by database searches.

## References

1. A. Iosevich, Z. Li and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404, first public 2026-09-21; updated full-text title *Spectral synthesis, Fourier extension, and arithmetic in \(\mathbb Z_N^d\)*. https://arxiv.org/html/2609.25404v2
2. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647. https://arxiv.org/abs/2405.16647
3. M. Lewko, *A bilinear approach to the finite field restriction problem, II*, arXiv:2606.22882. https://arxiv.org/abs/2606.22882
4. A. Iosevich, D. Koh and M. Lewko, *Finite field restriction estimates for the paraboloid in high even dimensions*, arXiv:1712.05549. https://arxiv.org/abs/1712.05549
