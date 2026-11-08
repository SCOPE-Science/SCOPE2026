# The five-state positivity barrier and sharp recovery for Richardson-extrapolated backward Euler on directed cycles

## Finding
Let \(n\ge2\) be an integer, let \(P_n\) be the cyclic permutation matrix on \(n\) states, and let \(Q_n=P_n-I_n\) be the unit-rate directed-cycle Markov generator. For every real \(h\ge0\), apply the ordinary **unmodified** two-level, second-order Richardson extrapolation of backward Euler:
\[
T_n(h)=2(I_n-hQ_n/2)^{-2}-(I_n-hQ_n)^{-1}.
\]
The one-step matrix is row- and column-sum one for every \(n\) and \(h\), but entrywise nonnegativity has the following exact classification.

1. For \(2\le n\le4\), every entry of \(T_n(h)\) is strictly positive for every \(h>0\). At \(h=0\), \(T_n(0)=I_n\).
2. For every \(n\ge5\), the entry in cyclic displacement four satisfies
\[
[T_n(h)]_{i,i+4\pmod n}=-\frac38h^4+O(h^5),\qquad h\downarrow0.
\]
Consequently \(T_n(h)\) has a negative entry for every sufficiently small positive \(h\). For every fixed finite \(n\ge5\), however, \(T_n(h)\) is strictly positive entrywise for all sufficiently large \(h\), and \(T_n(h)\to n^{-1}{\bf1}{\bf1}^{\mathsf T}\).
3. On the *first failing size*, \(n=5\), there is exactly one positive positivity-recovery threshold \(h_*\). It is the unique positive zero of
\[
\begin{aligned}
p(h)={}&25h^8+300h^7+1300h^6+2850h^5+3450h^4\\
&+2240h^3+560h^2-160h-96.
\end{aligned}
\]
It obeys \(0.297835687<h_*<0.297835689\). The matrix \(T_5(h)\) is not entrywise nonnegative on \(0<h<h_*\), is entrywise nonnegative (with a zero cyclic displacement-four entry) at \(h=h_*\), and is strictly positive for \(h>h_*\).

This is a dimension-specific result for *directed cycles*, not a universal minimum dimension for all finite Markov generators.

## Assumptions and scope
All statements are in exact real arithmetic. Here \(P_n e_i=e_{i-1\pmod n}\), or the transpose convention equivalently, and cyclic displacement means the coefficient of \(P_n^j\). The generator \(Q_n\) has off-diagonal transition rate one and zero row and column sums, so its exact exponential \(e^{hQ_n}\) is stochastic and nonnegative for every \(h\ge0\). We consider only the standard Richardson combination of one backward Euler macro-step and two backward Euler half-steps; no clipping, projection, modified weights or adaptive step selection is performed. For nonnegative initial probability vectors, the numerical result is a probability vector for every initial distribution precisely when \(T_n(h)\) is entrywise nonnegative.

## Proof
Set
\[
 a=\frac{h}{h+2},\qquad b=\frac{h}{h+1}.
\]
For \(h>0\), both numbers belong to \((0,1)\). Since \(P_n^n=I_n\), the exact geometric-resolvent identity gives
\[
(I_n-hQ_n)^{-1}=\frac{1}{h+1}\sum_{j=0}^{n-1}\frac{b^j}{1-b^n}P_n^j.
\]
Squaring the half-step inverse, or summing \(\sum_{m\equiv j\ ({\rm mod}\ n)}(m+1)a^m\), yields
\[
(I_n-hQ_n/2)^{-2}=\frac{4}{(h+2)^2}\sum_{j=0}^{n-1}\frac{a^j[(j+1)+(n-j-1)a^n]}{(1-a^n)^2}P_n^j.
\]
Hence \(T_n(h)=\sum_{j=0}^{n-1}c_{n,j}(h)P_n^j\), where the **exact** rational coefficient is
\[
c_{n,j}(h)=\frac{8a^j[(j+1)+(n-j-1)a^n]}{(h+2)^2(1-a^n)^2}-\frac{b^j}{(h+1)(1-b^n)}.
\tag{1}
\]
Every coefficient has strictly positive denominator. More explicitly, put \(A=h+2\), \(B=h+1\), and
\[
D_n(h)=(A^n-h^n)^2(B^n-h^n)>0.
\]
For \(0\le j<n\), define
\[
\begin{aligned}
U_{n,j}(h)={}&8(j+1)A^{2n-j-2}(B^n-h^n)\\
&+8(n-j-1)h^n A^{n-j-2}(B^n-h^n)\\
&-B^{n-j-1}(A^n-h^n)^2,
\end{aligned}
\tag{2}
\]
where the second summand is **omitted** when \(j=n-1\), so no negative powers occur. Direct simplification of (1) gives
\[
 c_{n,j}(h)=\frac{h^j U_{n,j}(h)}{D_n(h)}.
\tag{3}
\]
For each \(n\in\{2,3,4\}\) and each \(0\le j<n\), elementary integer-polynomial expansion of (2) has only nonnegative coefficients and at least one positive coefficient. The same is true for \(n=5\) and \(j=0,1,2,3\). The complete expansion checks are reconstructible without a symbolic-algebra package using the included `verify.py` (integer list polynomials, exact multiplication, and no numerical approximation); equation (2) is itself the general certificate. Thus all listed entries are strictly positive when \(h>0\).

For \(n=5\), \(j=4\), the only exceptional numerator factorizes *exactly* as
\[
U_{5,4}(h)=4p(h),
\]
with \(p\) stated in the finding. Its coefficient sequence, read from low to high degree, is
\[
(-96,-160,560,2240,3450,2850,1300,300,25).
\]
There is exactly one sign change (read either way), so Descartes' rule of signs allows at most one positive root, counting multiplicity. As \(p(0)=-96<0\) and \(p(h)\to+\infty\) with \(h\), the intermediate value theorem provides exactly one such root. Exact rational endpoint evaluation proves the displayed interval; all other entries are positive. This completes the five-state classification, including equality at the threshold.

To prove the all-\(n\) small-step obstruction, write the method's power series at the origin:
\[
T_n(h)=\sum_{m=0}^{\infty}\left(\frac{2(m+1)}{2^m}-1\right)h^mQ_n^m
\]
for sufficiently small \(h\). Since \(Q_n=P_n-I_n\), for \(n\ge5\) a term \(P_n^4\) cannot occur in \(Q_n^m\) with \(m<4\); it occurs with coefficient one in \(Q_n^4\). Its order-four coefficient is \(2\cdot5/16-1=-3/8\). Higher-order terms are \(O(h^5)\) for each fixed \(n\), proving the negative entry. This proves the sharp dimension split at four versus five within the directed-cycle family.

Finally, \(P_n\) is unitarily diagonalized by the discrete Fourier matrix. Its eigenvalues are the \(n\)-th roots of unity. Thus the eigenvalues of \(Q_n\) are \(\omega-1\), with a single zero eigenvalue and all others in the strict left half-plane. The Richardson stability function
\[
r(z)=2(1-z/2)^{-2}-(1-z)^{-1}
\]
satisfies \(r(0)=1\) and \(r(hz)\to0\) as \(h\to\infty\) for every nonzero \(z\) with negative real part. Fourier diagonalization gives
\[
T_n(h)\longrightarrow\frac1n{\bf1}{\bf1}^{\mathsf T},
\]
entrywise. Because \(n\) is finite and the limit has strictly positive entries, all entries are positive for sufficiently large \(h\). Both resolvent factors fix \({\bf1}\) on the left and right, yielding row and column sums one for all \(h\), including \(h=0\). All assertions follow.

## Verification
Execute `python3 verify.py` in the same directory as this document. It requires only Python's standard library, performs integer-polynomial expansion of (2) and checks its coefficient signs for all \(2\le n\le5\), verifies the exceptional polynomial and Descartes sign-change count, brackets the root using exact rational arithmetic, and independently compares (1) against exact Gaussian-elimination matrix inverses on \(2\le n\le8\) over six rational step sizes. It also tests finite small/large-step examples. The supplied `verify-output.txt` records **1,476 exact-arithmetic assertions** passing. Finite tests do **not** prove the all-dimension negative coefficient or eventual positivity; those are proved by the power series and spectral argument above. The code and output are both included, and the code can be replayed without downloads.

## Relationship to prior work
Classical Richardson extrapolation combines a coarse backward Euler step and two half-steps with a negative weight. Constantinescu and Sandu derive Euler-based extrapolation tableaux and their order and stability properties; those constructions are not new here. Blanes, Iserles and Macnamara motivate high-order positivity-preserving integrators for graph-Laplacian ODEs and construct exponential, splitting and Magnus alternatives, not the present extrapolated-resolvent cycle coefficients. Hadjimichael, Ketcheson and Lóczi give circulant-entry positivity analysis for centered spatial advection discretizations coupled to \(\theta\)-methods; their generators and one-step map differ. A separate published scalar Richardson positivity result identifies failure past a large positive scalar decay step, but a negative scalar amplification eigenvalue neither supplies nor rules out entrywise nonnegativity of the directed-cycle update; in particular the exact five-state *small-step* obstruction and large-step recovery are not its corollaries. The contribution is the dimension-four/five boundary, exact five-cycle recovery root, and eventual recovery in every finite directed-cycle size for this specific extrapolation scheme.

## Limitations
There is no general all-generator Markov positivity characterization here, nor an exact recovery threshold for every \(n\ge6\). A finite directed cycle and unmodified two-level \(r=2\) extrapolation are essential to the stated exact classification. Although the entries eventually become positive, a large step can still be inaccurate as an approximation of the true transient. Structural order, mass preservation and numerical stability alone do not imply positivity. The literature search cannot exclude every obscure equivalent rational-function calculation; specialist precedence is a residual risk. Independent verification is not claimed.

## References
1. Sergio Blanes, Arieh Iserles, Shev Macnamara, *Positivity-preserving methods for population models* (first arXiv version, 16 February 2021), arXiv:2102.08242. Revised as *Positivity-preserving methods for ordinary differential equations*, https://arxiv.org/abs/2102.08242.
2. Emil M. Constantinescu and Adrian Sandu, *Achieving Very High Order for Implicit Explicit Time Stepping: Extrapolation Methods*, technical report TR-08-13 (18 July 2008), and Argonne technical report ANL/MCS-TM-306 (April 2009), https://web.cels.anl.gov/~emconsta/Repository/Papers/TM-306.pdf.
3. Yiannis Hadjimichael, David I. Ketcheson, Lajos Lóczi, *Positivity preservation of implicit discretizations of the advection equation*, arXiv:2105.07403 (16 May 2021), https://arxiv.org/abs/2105.07403.
4. *Richardson acceleration creates a sharp positivity barrier for backward Euler*, published-finding corpus, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-richardson-acceleration-creates-a-sharp-positivity-barrier-for-b--c9c2b9f6d7e1.
