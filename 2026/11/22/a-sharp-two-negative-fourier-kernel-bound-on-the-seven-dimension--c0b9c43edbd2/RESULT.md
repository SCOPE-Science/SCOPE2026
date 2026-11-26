# A sharp two-negative Fourier-kernel bound on the seven-dimensional torus

## Finding

For the eight points \(x_0=0\) and \(x_j=\pi e_j\) for \(1\le j\le7\) on the seven-dimensional torus, fix the contrast
\[
c=(-1,-1,1,1,1,1,1,1)^T.
\]
Over **all continuous, real-valued, pointwise nonnegative, positive-definite** functions \(f\) on \(\mathbb T^7\), with \(f(0)=1\), the following sharp identity holds:
\[
\boxed{\inf_f c^T\bigl[f(x_i-x_j)\bigr]_{0\le i,j\le7}c=\frac{12}{7}.}
\]
In particular, the proposed universal matrix lower bound \(K_f\succeq J_8/8\) would give \(2\) in this direction, whereas the optimal attainable deficit is exactly \(-2/7\).

One extremizer is the following pointwise nonnegative trigonometric polynomial. Write \(y_j=\cos x_j\), and let \(E_r(y_2,\ldots,y_7)\) denote the elementary symmetric polynomial of degree \(r\) in those six entries. Then
\[
\boxed{
f_*(x)=\frac3{28}+\frac1{28}E_2(y_2,\ldots,y_7)
+\frac1{56}y_1E_3(y_2,\ldots,y_7).
}
\]
The lower bound is global over the infinite-dimensional function class, not merely over symmetric polynomials or finite Fourier supports.

## Assumptions and scope

The torus is \(\mathbb T^7=(\mathbb R/2\pi\mathbb Z)^7\), with its standard characters \(e^{i\langle n,x\rangle}\), indexed by \(n\in\mathbb Z^7\). The function \(f:\mathbb T^7\to\mathbb R\) is continuous, pointwise \(f(x)\ge0\), positive definite in the sense that \([f(z_i-z_j)]\) is positive semidefinite for every finite set of torus points, and normalized by \(f(0)=1\). No coordinate-permutation symmetry or finite-Fourier-support assumption is imposed on \(f\). The eight sampling points and the fixed two-negative/six-positive vector above are essential to the optimization statement.

Let \(E_r(z_1,\ldots,z_6)=\sum_{|S|=r}\prod_{j\in S}z_j\), with \(E_0=1\). The symbols \(J_8\) and \(K_f\) denote, respectively, the all-ones matrix and the eight-by-eight matrix of the kernel at differences of the specified points.

## Proof

**Step 1: Fourier-parity reduction without a finite-support assumption.** Compact-group Bochner theory gives an absolutely and uniformly convergent expansion
\[
f(x)=\sum_{n\in\mathbb Z^7}p_n e^{i\langle n,x\rangle},\qquad
p_n\ge0,\qquad \sum_n p_n=f(0)=1.
\]
Aggregate coefficients by their seven coordinate parities, writing \(P_u=\sum_{n\equiv u\pmod2}p_n\) for \(u\in\{0,1\}^7\). The weights \(P_u\) are nonnegative and total one. Put \(h=u_1\in\{0,1\}\) and \(k=u_2+\cdots+u_7\in\{0,\ldots,6\}\). For the fixed contrast, the character sum is
\[
\sum_{j=0}^7 c_je^{i\langle n,x_j\rangle}
=-1-(-1)^h+\sum_{j=2}^7(-1)^{u_j}
=5-2k-(-1)^h.
\]
Consequently the quadratic form equals
\[
Q(f)=\sum_{u\in\{0,1\}^7}P_u\bigl(5-2k-(-1)^h\bigr)^2.
\]
This equality is exact for every function in the stated class.

**Step 2: Two nonnegative sample averages.** For \(t=3,4\), let
\[
\mathcal K_k(t)=\sum_{j=\max(0,k-(6-t))}^{\min(k,t)}
(-1)^j\binom tj\binom{6-t}{k-j},\qquad
A_k=\frac{\mathcal K_k(3)}{\binom6k},\quad
B_{h,k}=(-1)^h\frac{\mathcal K_k(4)}{\binom6k}.
\]
The ratios are the averages of character signs over, respectively, three- and four-coordinate flip sets among indices \(2,\ldots,7\). Define
\[
F_{0,3}=\frac1{\binom63}\sum_{\substack{S\subseteq\{2,\ldots,7\}\\|S|=3}}
f\left(\pi\sum_{j\in S}e_j\right)\ge0,
\]
\[
F_{1,4}=\frac1{\binom64}\sum_{\substack{S\subseteq\{2,\ldots,7\}\\|S|=4}}
f\left(\pi e_1+\pi\sum_{j\in S}e_j\right)\ge0.
\]
The inequalities follow from pointwise nonnegativity; the Fourier expansion gives \(F_{0,3}=\sum_uP_u A_k\) and \(F_{1,4}=\sum_uP_u B_{h,k}\).

**Step 3: Exact fourteen-case dual certificate.** The elementary inequality
\[
7\bigl(5-2k-(-1)^h\bigr)^2-12-40A_k-60B_{h,k}\ge0
\]
holds for every \(h\in\{0,1\}\) and \(0\le k\le6\). Its fourteen exact left-hand sides, in increasing \(k\), are

| \(h\) | \(k=0\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(0\) | 0 | 36 | 0 | 4 | 96 | 260 | 416 |
| \(1\) | 260 | 80 | 20 | 0 | 4 | 80 | 340 |

There are no omitted parity sectors: \(h,k\) classify all 128 parities up to permutations of the final six coordinates. Multiplying by \(P_u\), summing, and invoking Step 2 yields the explicit stronger inequality
\[
\boxed{Q(f)\ge\frac{12}{7}+\frac{40}{7}F_{0,3}+\frac{60}{7}F_{1,4}\ge\frac{12}{7}.}
\]
The table entries are finite, rational, exhaustive consequences of the displayed binomial formula, so this is an analytic lower bound on the entire function class.

**Step 4: Construct an attainable extremizer.** Every product of cosine factors is an average of Fourier characters with nonnegative coefficients, so each of the three terms of \(f_*\) has nonnegative Fourier coefficients. Their coefficients sum to
\[
\frac3{28}+\frac1{28}\binom62+\frac1{56}\binom63=1.
\]
Thus \(f_*\) is normalized and positive definite. It remains to establish pointwise nonnegativity. Its defining polynomial is multiaffine in \(y_1,\ldots,y_7\), and therefore is a convex combination of its \(2^7\) vertex values on \([-1,1]^7\). They depend only on the sign \(y_1=(-1)^h\) and the number \(t\) of negative signs among \(y_2,\ldots,y_7\), and are exactly:

| \(h\) | \(t=0\) | \(1\) | \(2\) | \(3\) | \(4\) | \(5\) | \(6\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(0\) | 1 | \(2/7\) | 0 | 0 | \(1/7\) | \(2/7\) | \(2/7\) |
| \(1\) | \(2/7\) | \(2/7\) | \(1/7\) | 0 | 0 | \(2/7\) | 1 |

All are nonnegative, so \(f_*(x)\ge0\) on the whole torus. At the eight sample nodes the extremal kernel has unit diagonal, all off-diagonal entries meeting either of the first two nodes equal \(2/7\), and the fifteen off-diagonal pairs between the last six nodes equal zero. Its quadratic form therefore is
\[
Q(f_*)=8+\frac4{7}-\frac{48}{7}=\frac{12}{7}.
\]
Meanwhile \((\sum_jc_j)^2/8=4^2/8=2\), so the exact deficit is \(-2/7\). This attains the lower bound and completes the proof.

## Verification

The accompanying `check_certificate.py` uses only Python's standard library and exact rational arithmetic. Running `python3 check_certificate.py` verifies all fourteen dual slacks, all 128 cube vertices, Fourier-parity reconstruction at all parity points, every entry of the eight-node kernel, normalization, and the sharp deficit. Its finite checks validate the rational identities; the global theorem uses compact-group Bochner theory plus the dual inequality. No floating-point numerical optimization is required for the final proof.

## Relationship to prior work

Hinrichs and Vybíral (2011) proposed the universal bound \(K_f\succeq J_n/n\) for normalized nonnegative positive-definite functions. Vybíral (2026) supplied a counterexample on this same eight-point configuration using a **one-negative/seven-positive** sign vector with deficit \(-1/10\), and discussed a symmetric linear program for that contrast. The present result instead fixes a **two-negative/six-positive** contrast and obtains the exact optimum over *every* normalized continuous doubly-positive torus kernel, with a two-average dual certificate and an explicit extremizer. Vybíral's polynomial has \(f(\pi e_j)=9/35\) for every leaf and \(f(\pi(e_i-e_j))=0\) for distinct leaves. With the present contrast the center contributes sign \(-1\) and the sum of the seven leaf signs is \(5\). Its quadratic value is therefore \(8+2(9/35)(-1)(5)=38/7>2\), so this earlier witness does not violate the proposed bound in the stated direction. Neither its one-negative optimization nor its original polynomial implies the global sharp two-negative bound. Vybíral's Schur-product inequality concerns kernels represented as squared moduli of positive-definite functions, a narrower class that cannot contain the extremizer here.

## Limitations

The sharpness is for the specified two-negative vector, eight points and periodic torus function class; it is not asserted for arbitrary sample geometries, arbitrary contrast vectors, or nonperiodic positive-definite functions with arbitrary real Fourier frequencies. The optimizer need not be unique as a continuous function, because only finitely many parity aggregates are observed. The reduction to finitely many parity sectors is rigorous, but uniqueness outside that quotient is not claimed. Independently established mathematical priority remains subject to further literature discovery.

## References

1. A. Hinrichs and J. Vybíral, *On positive positive-definite functions and Bochner's theorem*, Journal of Complexity 27 (2011), 264–272; public preprint: https://people.fjfi.cvut.cz/vybirja2/publ/Vybiral19.pdf.
2. J. Vybíral, *An explicit counterexample to the Hinrichs--Vybiral conjecture*, arXiv:2609.21733, first publicly submitted 2026-09-18, https://arxiv.org/abs/2609.21733.
3. J. Vybíral, *A variant of Schur's product theorem and its applications*, arXiv:1909.11726, https://arxiv.org/abs/1909.11726; Advances in Mathematics 368 (2020), 107140.
4. S. Bochner, *Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse*, Mathematische Annalen 108 (1933), 378–410.
