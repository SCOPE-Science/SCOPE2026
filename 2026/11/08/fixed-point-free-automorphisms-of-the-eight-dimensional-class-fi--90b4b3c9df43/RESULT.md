# Fixed-point-free automorphisms of the eight-dimensional class-five Leibniz algebra

## Finding

Let \(F=\mathbb F_q\) have characteristic \(p>3\). Define the eight-dimensional right Leibniz algebra \(A(F)\) by the multiplication table below. A linear automorphism \(\varphi\) is *fixed-point-free* if \(\ker(\varphi-\operatorname{id})=0\). Put \(n=q-1\), \(g=\gcd(n,3)\), and \(\varepsilon=1\) if \(4\mid n\), or \(0\) otherwise. Then

\[
\boxed{\#\{\varphi\in\operatorname{Aut}_F(A(F)):\ker(\varphi-\operatorname{id})=0\}
=q^5\bigl(n^2-(6+g)n+4+6g+2\varepsilon\bigr).}
\]

In particular the number is zero for \(q=5\), positive for every prime power \(q\ge7\) of characteristic greater than three, and its proportion among automorphisms tends to one as \(q\) grows. The leading finite-field correction depends on whether \(3\mid(q-1)\), and the constant term additionally detects whether \(4\mid(q-1)\). This is an exact count for the one specified algebra, not a result for all Leibniz algebras.

## Assumptions and scope

The basis is \(e_1,\ldots,e_8\). All products not specified here vanish, and the nonzero products are

\[
\begin{aligned}
[e_1,e_2]&=-e_3,& [e_2,e_1]&=e_3,& [e_2,e_2]&=e_4,\\
[e_2,e_3]&=e_5,&[e_4,e_1]&=e_5,&[e_4,e_2]&=e_6,\\
[e_4,e_3]&=e_7,&[e_5,e_2]&=e_7,&[e_6,e_1]&=2e_7,\\
[e_6,e_2]&=e_7,&[e_5,e_3]&=3e_8,&[e_6,e_3]&=e_8,\\
[e_7,e_1]&=3e_8,&[e_7,e_2]&=e_8.
\end{aligned}
\]

These are the structure constants of the minimal class-five example in Atajonov--Khudoyberdiyev--Yusupov, arXiv:2610.40348, equation (5.11). The right Leibniz identity follows by verifying \([R_1,R_2]=R_3\), \([R_1,R_3]=[R_2,R_3]=0\), and \(R_i=0\) for \(i\ge4\), with \(R_i(x)=[x,e_i]\); these are integral polynomial identities and remain valid over \(F\). The result requires \(p>3\); it makes no assertion in characteristics two or three.

## Proof

**Step 1: automorphism normal form, including a necessary sign.** Every automorphism has unique parameters \(a,b\in F^\times\) and \(u,v,w,m,h\in F\), with the following images. Write \(\varphi_j=\varphi(e_j)\):

\[
\begin{aligned}
\varphi_1={}&ae_1+au e_3+m e_8,\\
\varphi_2={}&\frac{a-b}{3}e_1+be_2+v e_3-ub e_4+w e_5+\frac{u^2b}{2}e_6
 +\left(-uw-\frac{u^3b}{6}\right)e_7+h e_8,\\
\varphi_3={}&ab e_3,\\
\varphi_4={}&b^2e_4+b\left(v+\frac{u(b-a)}3\right)e_5-ub^2e_6
 +\left(\frac{au^2b}{3}-ubv+bw+\frac{u^2b^2}{6}\right)e_7\\
&+\left(-\frac{au^3b}{6}-auw+\frac{u^2bv}{2}+3vw\right)e_8,\\
\varphi_5={}&ab^2e_5-uab^2e_7+\left(3abw+\frac{ab^2u^2}{2}\right)e_8,\\
\varphi_6={}&\frac{ab^2-b^3}{3}e_5+b^3e_6+(2b^2v-uab^2)e_7\\
&+\left(-2abuv+abw+\frac{ab^2u^2}{6}+\frac{a^2bu^2}{3}+3bv^2\right)e_8,\\
\varphi_7={}&ab^3e_7+(3ab^2v-ua^2b^2)e_8,\\
\varphi_8={}&a^2b^3e_8.
\end{aligned}
\]

For completeness, let \(U=\varphi(e_1)\) and \(V=\varphi(e_2)\). These determine the entire map because \(e_3=[e_2,e_1]\), \(e_4=[e_2,e_2]\), \(e_5=[e_2,e_3]\), \(e_6=[e_4,e_2]\), \(e_7=[e_5,e_2]\), and \(e_8=[e_6,e_3]\). The \(e_4,e_5,e_7,e_8\) coefficients of \([U,U]=0\), together with invertibility on \(A/A^2\), force \(U_2=U_4=U_6=0\), \(U_1V_2\ne0\), and \(U_1U_7+U_3U_5=0\). The \(e_5,e_7\) coefficients of \([U,V]+[V,U]=0\) give

\[
 U_1V_4+U_3V_2=0,\qquad 2U_1V_6+U_3V_4+U_5V_2=0.
\]

The \(e_8\) coefficient of \([[V,U],U]=0\) then forces \(2U_1^2V_6=U_3^2V_2\), whence \(U_5=U_7=0\). The vanishing \(e_8\)-coefficient of \([V,U]\) gives

\[
 V_7=-\frac{U_3(3V_5+V_6)}{3U_1}.
\]

Writing \(a=U_1\), \(b=V_2\), \(u=U_3/a\), \(v=V_3\), \(w=V_5\), \(m=U_8\), \(h=V_8\), this is exactly \(V_7=-uw-u^3b/6\). Finally the \(e_7\)-coefficient of \([\varphi(e_5),V]=[\varphi(e_6),V]\) forces \(a=3V_1+b\). Recursive evaluation of the six generating products yields the displayed columns. These deductions only divide by \(2,3,6,a,b\), so apply to every field of characteristic greater than three.

Conversely, direct substitution of the displayed columns into the fourteen nonzero products and fifty zero products gives \([\varphi_i,\varphi_j]=\varphi([e_i,e_j])\) for all ordered basis pairs. Their block-triangular determinant is \(a^6b^{15}\ne0\). Hence they are precisely the automorphisms, with \(q^5(q-1)^2\) choices. A symbolic check of all 64 products and a standalone finite-field implementation are described below.

**Sign clarification.** The \(e_7\)-coefficient of \(\varphi(e_2)\) in the displayed equation (6.2) of arXiv:2610.40348v1 contains \(+u^3b/6\); the defining identity \([\varphi(e_2),\varphi(e_1)]=\varphi(e_3)\) forces the minus sign used here. The remaining column formulas, with this correction, satisfy all 64 defining identities. The present counting argument uses the independently checked form, not the inconsistent sign.

**Step 2: eigenvalues and fixed points.** With basis blocks \((e_1,e_2),e_3,e_4,(e_5,e_6),e_7,e_8\), the automorphism matrix is block lower triangular, with diagonal entries

\[
 a,\quad b,\quad ab,\quad b^2,\quad ab^2,\quad b^3,\quad ab^3,\quad a^2b^3.
\]

Therefore \(\varphi-I\) is invertible exactly when none of these eight scalars is one. The five parameters \(u,v,w,m,h\) do not influence this condition.

**Step 3: count admissible \((a,b)\).** Write \(n=q-1\), which is even. Values of \(b\) with \(b^2=1\) or \(b^3=1\) are forbidden, a union containing \(1+g\) elements, where \(g=\gcd(n,3)\). For each remaining \(b\), the four scalars \(1,b^{-1},b^{-2},b^{-3}\) are distinct forbidden values of \(a\). The remaining condition \(a^2b^3\ne1\) forbids two additional, distinct values precisely when \(b\) is a square; otherwise it forbids none. Indeed these quadratic roots cannot collide with the four displayed values unless \(b^j=1\) for \(j\in\{1,3\}\), already excluded.

There are \(n/2\) squares in \(F^\times\). Every cube root of unity is a square because \(n\) is even, while \(-1\) is a square precisely when \(4\mid n\). Consequently the number of allowed square values of \(b\) is \(n/2-g-\varepsilon\). The number of valid pairs is thus

\[
\begin{aligned}
N_n&=(n-1-g)(n-4)-2(n/2-g-\varepsilon)\\
&=n^2-(6+g)n+4+6g+2\varepsilon.
\end{aligned}
\]

Each admissible pair has exactly \(q^5\) lifts, proving the formula. For \(q=5\), \(n=4\) and \(N_n=0\); for \(q=7\), \(N_n=4\). For all even \(n\ge8\), the counting expression is positive: at least one admissible \(b\) remains and the forbidden \(a\)-set has at most six elements. This proves the stated existence boundary.

## Verification

The included standalone `verify.py` uses only Python's standard library. It constructs the matrices of the corrected normal form, independently multiplies elements using all fourteen defining products, tests the 64 ordered basis products and the rank of \(\varphi-I\), and checks the closed formula against exhaustive pairs in cyclic multiplicative groups of various even orders. This verifies samples, not the unrestricted theorem. A separate exact symbolic calculation over the rational function field verified all 64 product identities (its result is reported, and the included finite-field checker is the standalone reproducible artifact). Execute: `python3 verify.py`.

## Relationship to prior work

Atajonov, Khudoyberdiyev and Yusupov, arXiv:2610.40348v1 (29 October 2026), introduce this class-five right Leibniz algebra in (5.11), prove rigidity of local derivations and automorphisms over \(\mathbb C\), and derive its complex automorphism parameters in Proposition 6.4. That source does **not** count finite-field fixed-point-free automorphisms. Its matrix-parameter approach and diagonal weights are prior work. The present contribution is the finite-field fixed-point-free count, its arithmetic dependence on \(q-1\), and the exact smallest-field obstruction; the sign needed to use the normal form is verified directly.

General fixed-point-free automorphism theorems for Lie algebras (for example the 1989 result of Jianguo) do not enumerate automorphisms of this non-Lie right Leibniz algebra. A published exact count for the three-dimensional Heisenberg Lie algebra over finite fields concerns a different algebra with a different automorphism group. Neither result implies the eight-weight torus exclusion formula here.

## Limitations

This theorem concerns exactly \(A(F)\) with these structure constants over finite fields of characteristic greater than three. It does not assert rigidity of local automorphisms over finite fields, the existence of an automorphism all of whose nonidentity powers are fixed-point-free, or any formula in characteristics two or three. The correction to a source coefficient is stated transparently. Although the available sources and similarity searches revealed no identical count, complete historical priority has not been independently established.

## References

1. K. Atajonov, A. Khudoyberdiyev, B. Yusupov, *Local Derivations and Local Automorphisms of Arbitrary Finite-Dimensional Nilpotent Lie and Leibniz Algebras*, arXiv:2610.40348v1 (29 October 2026), especially (5.11) and Proposition 6.4. https://arxiv.org/html/2610.40348v1
2. Jianguo Z., *Fixed-point-free automorphisms of Lie algebras*, Acta Mathematica Sinica 5 (1989), 95–96. https://doi.org/10.1007/BF02107627
3. AMS, Mathematics Subject Classification 2020, class 17A32 (Leibniz algebras). https://mathscinet.ams.org/msc/msc2020.html
