# Arithmetic Fourier-zero lattices and Wiener cyclicity for two separated intervals

## Finding: local vanishing at real Fourier zeros

Let \(a,b,d>0\), let \(f\) be the indicator of \([0,a]\cup[a+d,a+d+b]\), and set \(\widehat f(\xi)=\int f(x)e^{-2\pi i x\xi}\,dx\). The three real-zero families below are due to Łaba (2001, Lemma 3.1, after scaling); they are used here to determine **the local order and strength of vanishing**, not claimed as new zero sets.

At a nonzero real zero \(\xi_0\), write \(u=e^{-2\pi i a\xi_0}\) and \(v=e^{-2\pi i(a+d)\xi_0}\). The leading derivative satisfies
\[
\begin{array}{c|l}
\text{family containing }\xi_0&\xi_0\widehat f'(\xi_0)\\ \hline
Z_0 & a+bv\\
Z_+ & a+b+d-du\\
Z_- & a+d-(b+d)u
\end{array}
\]
and the formulas agree wherever families overlap. If \(a\ne b\), they give the uniform bound \(|\xi_0\widehat f'(\xi_0)|\ge |a-b|\) over **all** real zeros, including lattice overlaps. Equality is possible, for instance at \(\xi_0=1\) when \((a,b,d)=(1,2,1/2)\), so the bound is sharp over the family. If \(a=b\), every real zero is also simple except at
\[
\xi_0\in Z_0\cap Z_-:\qquad a\xi_0\in\mathbb Z,\quad 2(a+d)\xi_0\in 2\mathbb Z+1.
\]
These and only these zeros are double, with
\[
\widehat f(\xi_0+t)=\frac{2\pi i a(a+d)}{\xi_0}t^2+O(t^3).
\]
Thus the intensity near a simple null is \(|\widehat f'(\xi_0)|^2 t^2+O(t^3)\), whereas at a double null it is \(4\pi^2a^2(a+d)^2t^4/\xi_0^2+O(t^5)\). The local order distinguishes nulls with linear amplitude recovery from those with only quadratic recovery; membership in several zero families is not by itself evidence of a higher-order null.

## Known zero locations and cyclicity consequences

In the present variables, Łaba's families with the origin excluded are
\[
\begin{aligned}
Z_0&=\{\xi\ne0:a\xi,b\xi\in\mathbb Z\},\\
Z_+&=\{\xi\ne0:(a+b)\xi,d\xi\in\mathbb Z\},\\
Z_-&=\{\xi\ne0:(a-b)\xi\in\mathbb Z,\ 2(d+b)\xi\in 2\mathbb Z+1\}.
\end{aligned}
\]
To translate Lemma 3.1, let \(L=a+b\), \(\lambda=L\xi\), \(r=a/L\), and let \(A=(a+d)/L\) denote the normalized second left endpoint. The lemma's \(Z_2,Z_3\) become \(Z_0,Z_+\), respectively. Its \(Z_1\) requires \(\lambda(2r-1)\in\mathbb Z\), \(\lambda A\in\mathbb Z+1/2\), equivalent to the row \(Z_-\) since \((a+d)\xi-(b+d)\xi=(a-b)\xi\). If needed, reflect the intervals to exchange the lengths so that \(r\le1/2\). Reflection and translation preserve the real zero locations and their orders. The origin is adjoined in Łaba's convention but is not a transform zero: \(\widehat f(0)=a+b\).

The cyclicity criterion is a consequence of this known classification and Wiener's theorem. For \(a\ne b\), the first two nonemptiness conditions are \(a/b\in\mathbb Q\) and \(d/(a+b)\in\mathbb Q\), respectively. For the third, write \(\rho=2(d+b)/(a-b)\). If \(\rho=P/Q\) in lowest terms with \(Q>0\), a nonzero integer multiple of \(\rho\) is an odd integer iff \(P\) is odd, as witnessed by the multiple \(Q\). Irrational \(\rho\) cannot give an odd integer. If \(a=b\) the third family is always nonempty. Therefore the closed linear span of all translates equals \(L^1(\mathbb R)\) precisely when \(a\ne b\), both of the first two ratios are irrational, and \(\rho\) is irrational or has even reduced numerator. The noncyclic set is the union of the corresponding countably many proper planes in the positive octant, hence null and meagre, and it is dense by the plane family with \(a/b\) rational. The cyclic set is full measure and dense residual. The transform is nonzero entire, so its real zeros are null; the \(L^2\) Wiener criterion gives \(L^2\) cyclicity for every parameter triple.

## Proof of the local law

At nonzero frequency put \(N(\xi)=2\pi i\xi\widehat f(\xi)\). Direct integration gives the analytic numerator
\[
N(\xi)=1-e^{-2\pi i a\xi}+e^{-2\pi i(a+d)\xi}-e^{-2\pi i(a+d+b)\xi}.
\]
At a real zero use \(u,v\) as above and \(w=e^{-2\pi i(a+d+b)\xi_0}\). Differentiation and \(N(\xi_0)=0\) give
\[
\xi_0\widehat f'(\xi_0)=a u-(a+d)v+(a+d+b)w.
\]
In \(Z_0\) one has \(u=1,v=w\); in \(Z_+\), \(v=u,w=1\); in \(Z_-\), \(v=-1,w=-u\). These substitutions prove the table. The reverse triangle inequality gives \(|a-b|\) as a lower bound in the first and third rows and \(a+b\) in the second row. When \(a=b\), the first row can vanish only for \(v=-1\), and the third only for \(u=1\); either condition puts the zero in \(Z_0\cap Z_-\). At an overlap with \(a=b\), the three endpoint phases are \((u,v,w)=(1,-1,-1)\). The second derivative of the numerator there is
\[
N''(\xi_0)=(-2\pi i)^2[-a^2-(a+d)^2+(2a+d)^2]=-8\pi^2 a(a+d).
\]
It is nonzero. Dividing its Taylor coefficient by \(2\pi i\xi_0\) proves the exact quadratic term for \(\widehat f\). Squaring the absolute values of the local expansions proves the intensity laws.

In particular double zeros exist for equal lengths iff \(2(a+d)/a\) is rational with odd numerator in lowest terms. Indeed, if this ratio is \(P/Q\) in lowest terms, \(a\xi_0\) must be an odd multiple of \(Q\). For example, \(a=b=1\), \(d=1/2\) has double zeros at all odd integers, whereas \(a=b=1\), \(d=1\) has only simple zeros.

## Verification and limits

Run `python verify_multiplicity.py` with SymPy installed to reproduce finite exact rational parameter-frequency checks. The script reduces the signed endpoint polynomial and its first two frequency derivatives modulo a cyclotomic polynomial, compares their orders and the derivative coefficients with the displayed formulas, and tests cases belonging exclusively to each family. It checks 2,592 cases including 402 simple and 24 double zeros. The statements about arbitrary real parameters follow from the analytic proof, not from these finite checks.

The analysis is for continuous real frequencies and two disjoint unweighted intervals with a positive gap. The bound on the normalized slope applies at exact zeros; it is not a uniform lower bound on the Fourier amplitude away from the zero set. No classification of nonreal zeros, more intervals, weighted windows or discrete translates is asserted.

## Relationship to prior work

Łaba gives the three-family real zero classification in normalized interval coordinates. The cyclicity criteria and measure/category conclusions above are included for context and follow from that classification and classical Tauberian results. The focus is the explicit local Taylor law, including the uniform nonzero slope bound for unequal lengths and the quadratic coefficient at equal-length double overlaps. Xia and Xu study recovery from the full Fourier magnitude up to symmetries, not the local Taylor law at every real null in their two-interval uniqueness theorem. This comparison does not establish exhaustive historical priority.

## References

1. I. Łaba, *Fuglede’s conjecture for a union of two intervals*, Proc. Amer. Math. Soc. 129 (2001), 2965–2972, Lemma 3.1, https://arxiv.org/abs/math/0002067.
2. N. Wiener, *Tauberian theorems*, Annals of Mathematics 33 (1932), 1–100.
3. Y. Xia and Z. Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, Theorem 1.2.
