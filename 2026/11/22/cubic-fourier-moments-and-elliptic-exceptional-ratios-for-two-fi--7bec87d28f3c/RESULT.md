# Cubic Fourier moments and elliptic exceptional ratios for two finite-field hyperbola shells

## Finding

Let \(F=\mathbb F_q\) have odd order and let \(H_u=\{(x,u/x):x\in F^\times\}\). Define \(N_q\) as the number of \(\lambda\in F^\times\setminus\{1\}\) for which the origin is missing from \(3(H_1\cup H_\lambda)\). Summands may repeat. Then \(N_q=0\) unless \(q\equiv2\pmod3\). In that congruence class,
\[
N_q=\begin{cases}
(q-5)/4,&\operatorname{char}F=5,\\
(q-5+2\chi(-15)-t_E)/4,&\operatorname{char}F\ne5,
\end{cases}
\qquad E: y^2=(1-4x)x(x-4).
\]
Here \(\chi\) is the quadratic character extended by zero. In the second case \(E\) denotes the smooth elliptic completion and \(t_E=q+1-\#E(F)\). An exceptional ratio exists precisely for \(q\equiv2\pmod3\) and \(q>5\). In that regime \(N_q=q/4+O(\sqrt q)\). For \(\mathbb F_{11}\) the two exceptional ratios are \(7,8\).

## Proof

**Reduction to a character sieve.** Put \(S=H_1\cup H_\lambda\), and let \(a=\chi(-3)\), \(b=\chi(1-4\lambda)\), \(c=\chi(\lambda(\lambda-4))\). The background two-shell pair-count formula [1, Finding and Proof §§2–3] gives for \(AB=s\ne0\)
\[
(\mathbf1_S*\mathbf1_S)(A,B)=4+\chi(s(s-4))+\chi(s(s-4\lambda))+2\chi((s+1-\lambda)^2-4s).
\]
This is its split planar specialization \(Q(x,y)=xy\). Evaluating at \(s=1,\lambda\) gives \(4+a+b+2c\) and \(4+a+c+2b\), respectively. Summing over the centrally symmetric set \(S\) yields
\[
(\mathbf1_S^{*3})(0)=(q-1)(8+2a+3b+3c).
\]
Equivalently this is \(q^{-2}\sum_{\xi\in F^2}\widehat{\mathbf1_S}(\xi)^3\), with both convolution and Fourier transform unnormalized and the latter taken with respect to any fixed nontrivial additive character. The bracket vanishes exactly when \(a=b=c=-1\). For context, the pair count in [1] is positive on both axes (two at nonzero axis vectors and \(2(q-1)\) at zero). Subtract a point of \(H_1\) matching any nonzero coordinate of a target to leave an axis vector. Hence the origin is the only possible missing vector. Neither this support reduction nor the preceding cubic evaluation of the pair count is claimed here as independent of that general pair-count result.

In characteristic three \(a=0\). Otherwise \(a=-1\) precisely when \(q\equiv2\pmod3\), by the discriminant of \(X^2+X+1\) and the criterion for primitive cube roots in \(F\). Assume henceforth \(q\equiv2\pmod3\).

**Exceptional-ratio count.** Write \(A(x)=1-4x\), \(B(x)=x(x-4)\), \(P(x)=A(x)B(x)\), and \(T=\sum_{x\in F}\chi(P(x))\). Over \(F\) the sums of \(\chi(A)\) and \(\chi(B)\) are respectively \(0,-1\): the former is a bijective affine change, and the latter follows by counting the \(q-1\) pairs with \((x-2-y)(x-2+y)=4\). Removing \(0,1\) leaves the two sums equal to zero because the removed values for \(\chi(A)\) are \(1,-1\) and for \(\chi(B)\) are \(0,-1\). The sum of \(\chi(P)\) on this domain is \(T-1\). Thus
\[
\frac14\sum_{x\notin\{0,1\}}(1-\chi(A(x)))(1-\chi(B(x)))=(q-3+T)/4.
\]
Away from zeros this counts exactly the simultaneous nonsquares. In characteristic other than five the two remaining zeros \(4,1/4\) are distinct; at each the other character is \(\chi(-15)\) (the factor \(1/16\) at \(1/4\) is a square). Subtract their total contribution \((1-\chi(-15))/2\). The cubic is squarefree, with one point at infinity, so \(T=\#E(F)-q-1=-t_E\). This gives the stated trace formula. In characteristic five the two zeros coalesce and \(P=x(x-4)^2\), hence \(T=-1\). The one doubly vanishing factor pair contributes \(1/4\) spuriously, giving \((q-5)/4\); no smooth elliptic count is used in this case.

**Existence.** In the smooth case the Hasse bound implies \(4N_q\ge q-7-2\sqrt q>0\) for \(q\ge17\). The only smaller smooth odd field in this congruence class is \(\mathbb F_{11}\), where the simultaneous nonsquares occur at \(7,8\). In characteristic five the only applicable orders are odd powers of five, and \((q-5)/4>0\) exactly when \(q>5\). The same Hasse bound proves the stated asymptotic.

## Reproducibility and scope

The accompanying `artifacts/verify_two_shell_threefold.py` uses direct ordered pair counts in small prime and extension fields, checks the cubic-origin reduction and computes the census and trace by finite enumeration. These checks supplement, but do not replace, the algebraic sieve and Hasse bound. The claim concerns two different nonzero shell levels over odd fields only; it does not give triple multiplicities away from the origin.

## Relationship to prior work

The new question here is how many shell ratios obstruct return, not the general two-shell quadratic convolution or its immediately derived three-step test. The general pair formula in [1] supplies the test, but its fourth-moment calculation sums different quartic character polynomials, not the simultaneous nonsquare indicator as the radius varies. The correction terms at the vanishing characters and the fixed elliptic trace in the census come from that separate sieve. The association-scheme intersection numbers in [2] are related background for quadratic distance walks. Single-shell covering [3] gives no census over a second radius. The elliptic traces in [4] concern unions of scalar projection images, not the distribution of missing origins of vector threefold sums. Historical priority for the census is qualified by the scope of the available comparisons.

1. *Exact two-shell Fourier energy and a three-valued elliptic-trace cancellation*, Resultary record `deadda507c3b`, Finding and Proof §§2–4 (2026-11-22), https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-two-shell-fourier-energy-and-a-three-valued-elliptic-trace--deadda507c3b.
2. C. Brittenham and J. Pakianathan, *Random walks and the “Euclidean” association scheme in finite vector spaces*, DOI:10.4153/S0008414X24000518.
3. *Sharp three-sum covering of the split modular hyperbola over finite fields*, Resultary record `02aca6c7a46d` (2026-11-01), https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-sharp-three-sum-covering-of-the-split-modular-hyperbola-over-fin--02aca6c7a46d.
4. P. Stănică, E. Mulder, and M. Hittmeir, *Multi-target hyperbolic sieves and elliptic trace obstructions*, arXiv:2606.13018v1, especially Theorem 3.13.
