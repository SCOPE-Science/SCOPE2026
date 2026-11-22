# Two-state carry laws at the first two dependence thresholds of lacunary Riesz products

## Finding

Let \(p\geq4\) be an integer, let \(q\geq p-1\) be an integer, and let \(n\geq1\). For arbitrary amplitudes \(0<\lambda_j\leq1\) define the finite nonnegative Riesz product on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\):
\[
R_{q,n}(t)=\prod_{j=0}^{n-1}\bigl(1+\lambda_j\cos(q^j t)\bigr),\qquad
M_{q,n}=\int_{\mathbb T} R_{q,n}(t)^p\,\frac{dt}{2\pi}.
\]
Write \(a_k(\lambda)\) for the coefficient of \(e^{ikt}\) in \((1+\lambda\cos t)^p\), set \(a_k(\lambda)=0\) for \(k>p\), and put
\[
T_q(\lambda)=
\begin{pmatrix}
 a_0(\lambda)&2a_q(\lambda)\\
 a_1(\lambda)&a_{q-1}(\lambda)+a_{q+1}(\lambda)
\end{pmatrix}.
\]
Then the exact finite-length identity, valid for every such parameter and every \(n\), is
\[
\boxed{M_{q,n}=(1,0)\,T_q(\lambda_0)\cdots T_q(\lambda_{n-1})\binom10.}
\]
In particular, with the same amplitudes, for every \(n\geq2\),
\[
\boxed{M_{p-1,n}>M_{p,n}>M_{q,n}
=\prod_{j=0}^{n-1}a_0(\lambda_j)\quad(q\geq p+1).}
\]
Thus the first two integer bases below exact independence have an irreducible two-state positive carry interaction; beyond them all \(p\)-th moments factor exactly, at every finite length.

For a fixed amplitude \(\lambda_j=\lambda\in(0,1]\), put \(A=a_0(\lambda)\), \(B_q=a_{q-1}(\lambda)+a_{q+1}(\lambda)\) and
\[
\Lambda_q^{\pm}(\lambda)=\frac{A+B_q\pm\sqrt{(A-B_q)^2+8a_q(\lambda)a_1(\lambda)}}{2}.
\]
For \(q\in\{p-1,p\}\), the exact recurrence and sharp exponential rate are
\[
\begin{aligned}
&M_{q,0}=1,\quad M_{q,1}=A,\\
&M_{q,n+2}=(A+B_q)M_{q,n+1}-(AB_q-2a_q a_1)M_{q,n},\\
&\lim_{n\to\infty}M_{q,n}^{1/n}=\Lambda_q^+(\lambda),\qquad
\Lambda_{p-1}^+(\lambda)>\Lambda_p^+(\lambda)>A.
\end{aligned}
\]
The exact small-amplitude onset is
\[
\Lambda_{p-1}^+(\lambda)-a_0(\lambda)
=\frac{p^2}{2^{p-1}}\lambda^p+o(\lambda^p),\qquad
\Lambda_p^+(\lambda)-a_0(\lambda)
=\frac{p}{2^p}\lambda^{p+1}+o(\lambda^{p+1}).
\]
For the first fourth-moment example \(p=4\), \(\lambda=1\), the three rates (bases three, four, and any base at least five) are respectively
\[
\boxed{\frac{99+9\sqrt{65}}{32},\qquad
\frac{39+\sqrt{1073}}{16},\qquad\frac{35}{8}.}
\]

## Assumptions and scope

All integrals use normalized Haar measure on the circle. The Fourier coefficients are real, symmetric, and strictly positive for indices \(0\leq k\leq p\) when \(0<\lambda\leq1\). An explicit formula, with the standard binomial convention for parity-incompatible indices, is
\[
a_k(\lambda)=\sum_{\substack{k\leq r\leq p\\r\equiv k\pmod2}}
{p\choose r}{r\choose(r-k)/2}\left(\frac{\lambda}{2}\right)^r.
\]
No irrational frequencies, arbitrary phases, or exponents outside the integers \(p\geq4\) are asserted. The product has integral one for all \(q\geq3\), since its first-power frequencies have unique balanced-digit representations; it is therefore a finite Riesz probability density.

## Proof

**1. Exact carry states.** Expanding the \(p\)-th power gives
\[
M_{q,n}=\sum_{\substack{d_0,\ldots,d_{n-1}\in[-p,p]\cap\mathbb Z\\
\sum_j d_jq^j=0}}\prod_{j=0}^{n-1}a_{|d_j|}(\lambda_j).
\]
For every admissible digit string there is a unique sequence of integer carries starting and ending at zero,
\[
c_0=c_n=0,\qquad d_j=qc_{j+1}-c_j.
\]
This follows by successive reductions modulo \(q\), and conversely telescoping gives \(\sum_j d_jq^j=q^nc_n-c_0=0\). Whenever \(q\geq p-1\) and \(p\geq4\), the inequality \(p+1<2q\) shows inductively that integer carries reachable from zero satisfy \(|c_j|\leq1\). Therefore the exact sum is a weighted closed-walk count on states \(-1,0,+1\), with a one-step edge \(c\to c'\) weighted by \(a_{|qc'-c|}(\lambda_j)\).

**2. Symmetry reduction.** The two nonzero states are mirror images. Starting at zero, their accumulated weights remain equal. Folding them into a single combined state gives exactly the displayed \(2\times2\) matrix: \(0\to0\) carries \(a_0\); \(0\to\{\pm1\}\) carries \(2a_q\); \(\{\pm1\}\to0\) carries \(a_1\); and \(\{\pm1\}\to\{\pm1\}\) carries \(a_{q-1}+a_{q+1}\). Matrix multiplication in digit order proves the boxed finite-length formula. For \(q\geq p+1\), \(a_q=0\); from initial carry zero no nonzero state can be reached, and factorization follows.

**3. Strict ordering.** Directly from the binomial formula,
\[
a_p=\left(\frac\lambda2\right)^p,\quad
a_{p-1}=p\left(\frac\lambda2\right)^{p-1},\quad
a_{p-2}={p\choose2}\left(\frac\lambda2\right)^{p-2}
+p\left(\frac\lambda2\right)^p.
\]
Consequently \(a_{p-2}+a_p>a_{p-1}>a_p>0\) for \(p\geq4\), \(0<\lambda\leq1\). In the order of the folded states, \(T_{p-1}(\lambda)\) dominates \(T_p(\lambda)\) entrywise, and \(T_p(\lambda)\) dominates each \(T_q(\lambda)\), \(q\geq p+1\), on reachable entries. Since a length-two return via the nonzero state has strictly positive weight \(2a_q(\lambda_0)a_1(\lambda_1)\), the moment inequalities are strict for \(n\geq2\), even if amplitudes vary with \(j\).

**4. Rates.** For constant \(\lambda\), Cayley–Hamilton gives the stated second-order recurrence. For the two resonant bases, every matrix entry is strictly positive, so the Perron eigenvalue is \(\Lambda_q^+\), strictly dominates the other eigenvalue, and its spectral projection has a positive \((0,0)\)-entry. This proves the exact root limit. Entrywise domination gives strict ordering of the Perron eigenvalues. As \(\lambda\downarrow0\), \(a_0=1+O(\lambda^2)\), \(a_1=p\lambda/2+O(\lambda^3)\), \(a_{p-1}=p(\lambda/2)^{p-1}\), and \(a_p=(\lambda/2)^p\); expanding the larger root gives the stated onset constants. With \(p=4\), the five coefficients are \(35/8,7/2,7/4,1/2,1/16\). Substitution yields the three displayed exact rates.

## Verification

Run `python3 verify_riesz_moments.py`. The standalone checker independently computes the zero Fourier coefficient by finite Laurent convolution with exact rational arithmetic, compares it with the matrix rule for integer orders four through eight at and above the first two resonance bases, tests nonconstant rational amplitudes, verifies strict inequalities through order ten, and checks the explicit fourth-moment coefficients. The recorded run passed 220 exact assertions. This finite replay is not the proof for arbitrarily large \(p\) or \(n\); the carry and Perron arguments above establish those universal statements.

## Relationship to prior work

Bonami, Latała, Nayar and Tkocz (2018), Lemma 7, prove qualitative unbounded growth of the dependent-to-independent norm ratio at the geometric base equal to an even moment order. Their Lemma 11 and the discussion preceding it provide exact factorization in the independent range. Neither assertion specifies the inhomogeneous two-state carry rule, the strict finite-length ordering between the two adjacent resonance bases, the sharp Perron rates, or the amplitude-onset exponents proved here. The recurrence is obtained by an elementary carry argument and may be subsumed by a more general published finite-state transfer formalism not identified in the consulted literature. Fraser (2024), Section 3.1, treats Fourier spectra and dimensions of Riesz measures rather than these finite-density moment recurrences.

## Limitations

The exact matrix reduction is asserted only for \(p\geq4\) and \(q\geq p-1\), with nonnegative real amplitudes and unshifted cosine factors. Smaller bases can require additional carries; arbitrary phase shifts generally require retaining separate signed states. The proof does not establish a new optimal bound for arbitrary linear combinations of finite Riesz products, nor a classification of all Riesz moment transfer operators. Publication priority is best-knowledge only: classical transfer-matrix literature may contain equivalent formulations. Independent review has not been performed.

## References

1. A. Bonami, R. Latała, P. Nayar, T. Tkocz, *Bounds on moments of weighted sums of finite Riesz products*, arXiv:1805.10918 (first posted 2018-05-28), especially Lemmas 7 and 11; https://arxiv.org/abs/1805.10918.
2. J. M. Fraser, *The Fourier spectrum and sumset type problems*, Mathematische Annalen (2024), Section 3.1; https://doi.org/10.1007/s00208-024-02843-7.
3. F. R. Keogh, *Riesz products*, Proc. London Math. Soc. (3) 14A (1965), 174–182 (historical background).
