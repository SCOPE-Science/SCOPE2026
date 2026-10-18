# An invertible four-dimensional counterexample to the dyadic numerical-radius conjecture

## Finding
Paul and Bag conjectured in 2012 (Conjecture 2.7) that every **nonnilpotent** bounded operator \(A\) on a complex Hilbert space satisfies
\[
w(A)\le D(A):=\sum_{n=0}^{\infty}\frac{\|A^{2^n}\|^{1/2^n}}{2^{n+1}}.
\]
This assertion fails for an explicit **invertible** \(4\times4\) matrix. Write
\[
S=\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\0&0&0&0\end{pmatrix},
\qquad \varepsilon=\frac1{10000},\qquad T=S+\varepsilon I_4.
\]
Then \(\det T=\varepsilon^4>0\), while the strict, fully rationally certified separation is
\[
D(T)<\frac{31503}{40000}<\frac45<w(T).
\]
Moreover the set of all matrices violating this proposed bound is open in the operator norm. Thus merely excluding nilpotent matrices cannot rescue the conjecture.

## Assumptions and scope
The Hilbert space is \(\mathbb C^4\) with its standard inner product and induced operator norm. The numerical radius is \(w(A)=\sup_{\|x\|_2=1}|\langle Ax,x\rangle|\). The series defining \(D(A)\) is meaningful for every bounded operator on any complex Hilbert space: by submultiplicativity,
\[
0\le \|A^{2^n}\|^{1/2^n}\le\|A\|,
\]
so the series converges absolutely. There is no assumption of normality, positivity, or self-adjointness.

## Proof
**1. Upper bound on the dyadic series.** For any bounded \(A\), submultiplicativity and the fact that \(2^n\) is divisible by \(4\) for \(n\ge2\) give
\[
\|A^2\|^{1/2}\le\|A\|,\qquad
\|A^{2^n}\|^{1/2^n}\le\|A^4\|^{1/4}\quad(n\ge2).
\]
The first two dyadic weights add to \(3/4\), and all remaining weights add to \(1/4\). Consequently
\[
D(A)\le\frac34\|A\|+\frac14\|A^4\|^{1/4}.
\]
For \(T=S+\varepsilon I_4\), \(S^4=0\) and \(\|S^j\|=1\) for \(j=0,1,2,3\). The binomial expansion therefore yields
\[
\|T\|\le1+\varepsilon,\qquad
\|T^4\|\le4\varepsilon+6\varepsilon^2+4\varepsilon^3+\varepsilon^4.
\]
Since \(0<\varepsilon=10^{-4}<1/11\), the last expression is less than \(5\varepsilon=1/2000\), which is strictly less than \((3/20)^4=81/160000\). Hence \(\|T^4\|^{1/4}<3/20\), and
\[
D(T)<\frac34\left(1+\frac1{10000}\right)+\frac14\cdot\frac3{20}
=\frac{31503}{40000}<\frac45.
\]
This bounds the full infinite series, not merely a finite truncation.

**2. Lower bound on the numerical radius.** Let \(v\in\mathbb R^4\) have entries \(v_j=\sqrt{2/5}\sin(j\pi/5)\) for \(1\le j\le4\). The sine identity for the four-vertex path gives \(\|v\|_2=1\) and
\[
\langle Sv,v\rangle=\cos(\pi/5)=\frac{1+\sqrt5}{4}.
\]
As \(\varepsilon>0\),
\[
w(T)\ge|\langle Tv,v\rangle|
=\frac{1+\sqrt5}{4}+\varepsilon>\frac45,
\]
where the strict final inequality follows from \(\sqrt5>11/5\). Combining this with Step 1 establishes the counterexample.

**3. Robustness under perturbations.** Fix a bounded operator-norm ball \(\|A\|\le M\). For each \(n\), the function \(A\mapsto 2^{-n-1}\|A^{2^n}\|^{1/2^n}\) is continuous and bounded by \(M2^{-n-1}\). The Weierstrass test implies that \(D\) is locally uniformly convergent and continuous. The numerical radius is norm-continuous since \(|w(A)-w(B)|\le\|A-B\|\). Consequently \(w-D\) is continuous, and the strict violation at \(T\) persists on a nonempty open operator-norm neighborhood of \(T\). Since \(T\) is invertible and invertibility is open, that neighborhood can be restricted to consist only of invertible counterexamples.

## Verification
The included standalone `verify.py` uses rational arithmetic and explicitly checks the power identity \(S^4=0\), the fourth-power binomial expansion, the strict bound \(4\varepsilon+6\varepsilon^2+4\varepsilon^3+\varepsilon^4<(3/20)^4\), and the exact rational upper bound \(31503/40000<4/5\). Run it with `python3 verify.py`; it requires only the Python standard library. The irrational lower bound follows analytically from \(\sqrt5>11/5\), also checked as the rational squared inequality \(5>(11/5)^2\). The script is a finite certificate for the displayed inequalities, not a replacement for the operator-theoretic proof and not an independent mathematical audit.

## Relationship to prior work
The precise claim being refuted is Paul and Bag, *A Conjecture on Upper Bound of the Numerical Radius of a Bounded Linear Operator* (2012), Conjecture 2.7, page 1543. Crucially, their Example 2.5 on the **same page** already exhibits the nilpotent four-step shift \(S\) with \(w(S)=\cos(\pi/5)>3/4=D(S)\). Their conjecture specifically excludes such nilpotent operators. The present assertion therefore makes no novelty claim about \(S\), its numerical radius, or the nilpotent inequality violation. It shows that the exclusion does not suffice: a concrete nonnilpotent, indeed invertible, perturbation still violates the proposed estimate, and the inequality has an open set of invertible counterexamples. This is an elementary but consequential continuity obstruction to the stated conjecture.

Kittaneh's earlier upper bound \(w(A)\le(\|A\|+\|A^2\|^{1/2})/2\), discussed in Paul and Bag's introduction, is a different, valid inequality: it does not assert an upper bound by \(D(A)\). Yamazaki's iterative Aluthge-transform estimate, cited by Paul and Bag, also uses different operator quantities. Those results are not contradicted.

## Limitations
The theorem refutes Conjecture 2.7 in its literal formulation; it does not characterize the maximal natural class of operators on which the dyadic upper bound remains true. It also does not provide a sharp quantitative measure of the largest possible violation. The original article's nilpotent example is a close antecedent, and the deduction from that example to invertible counterexamples is short. An equivalent earlier published counterexample not captured by the inspected literature remains possible.

## References
1. K. Paul and S. Bag, *A Conjecture on Upper Bound of the Numerical Radius of a Bounded Linear Operator*, International Journal of Mathematical Analysis **6** (2012), no. 31, 1539–1544, especially Example 2.5 and Conjecture 2.7, page 1543. https://m-hikari.com/ijma/ijma-2012/ijma-29-32-2012/paulIJMA29-32-2012.pdf
2. F. Kittaneh, *A numerical radius inequality and an estimate for the numerical radius of the Frobenius companion matrix*, Studia Mathematica **158** (2003), 11–17, as cited and quoted in [1].
3. T. Yamazaki, *On upper and lower bounds of the numerical radius and an equality condition*, Studia Mathematica **178** (2007), 83–89, as cited in [1].
