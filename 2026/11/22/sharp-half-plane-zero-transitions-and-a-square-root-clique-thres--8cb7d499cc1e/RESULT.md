# Sharp half-plane zero transitions and a square-root clique threshold for cyclic hard-core gases

## Finding

Consider the hard-core lattice gas with **common vertex fugacity** \(z\) on the graph \(G_{n,h}=K_h\vee C_n\): a clique on \(h\) vertices, a cycle on \(n\) vertices, and all edges between them. Throughout \(n\ge3\) and \(h\) is a positive integer. Introduce the real-parameter polynomial \(P_{n,u}(z)=I(C_n;z)+uz\) for \(u>0\); it agrees with the partition polynomial of \(G_{n,h}\) when \(u=h\).

Put \(d=\lfloor n/2\rfloor\), \(a_{n,k}=4\cos^2((2k-1)\pi/(2n))\) for \(1\le k\le d\), and
\[
\Theta_n(y)=\sum_{k=1}^d\arctan(a_{n,k}y),\qquad
H_n(y)=\frac{\prod_{k=1}^d\sqrt{1+a_{n,k}^2y^2}}{y}\quad(y>0).
\]
For every nonnegative integer \(j\) satisfying \(4j+3<d\), there is a unique \(y_{n,j}>0\) with \(\Theta_n(y_{n,j})=(4j+3)\pi/2\). Define \(u_{n,j}=H_n(y_{n,j})\). For every \(u>0\), **including values coinciding with thresholds**, the number of zeros of \(P_{n,u}\) in the open right half-plane, with algebraic multiplicity, is exactly
\[
N_{\mathrm R}(n,u)=2\#\{j:4j+3<d,\ u>u_{n,j}\},
\]
and the number on the imaginary axis is exactly \(2\#\{j:4j+3<d,\ u=u_{n,j}\}\). Every boundary zero is simple and equals \(\pm i y_{n,j}\). The threshold values need not be assumed distinct. No conjugate pair ever returns from the right to the left as \(u\) increases.

Consequently **every clique size is strictly left-half-plane stable for \(3\le n\le7\)**. For \(n\ge8\), set \(u_n^*=\min_{4j+3<d}u_{n,j}\): the polynomial is strictly left-half-plane stable precisely when \(0<u<u_n^*\); equality places at least one conjugate pair on the axis, while larger \(u\) creates right-half-plane zeros. At the sharp smallest-cycle boundary,
\[
u_8^*=72+56\sqrt2,\]
so \(K_{151}\vee C_8\) is strictly stable but \(K_{152}\vee C_8\) is not. For the large-cycle family the optimal clique-activity threshold satisfies the **sharp square-root law**
\[
\boxed{\lim_{n\to\infty}\frac{u_n^*}{\sqrt n}=\sqrt{3e}.}
\]
In particular, for fixed positive integer \(h\), the independence polynomial of \(K_h\vee C_n\) is strictly stable for all sufficiently large \(n\), whereas a clique size of order \(\sqrt n\) is the sharp scale on which nonstable roots first become possible.

## Assumptions and scope

\(I(G;z)=\sum_{S\subseteq V(G)\,\mathrm{independent}}z^{|S|}\) counts independent sets in a finite simple graph. The graph join has every edge between its two factors. "Strictly stable" means that every complex zero has \(\operatorname{Re}z<0\); imaginary-axis zeros are not strictly stable. The real parameter \(u\) is a polynomial interpolation; the graph has \(h=u\) clique vertices only when \(u\) is a positive integer. All zero counts include multiplicities. The large-cycle asymptotic is for \(n\to\infty\) through integers \(n\ge8\). No assertion of real-rootedness for the joined graph is made.

## Proof

**1. Exact partition polynomial.** An independent set uses either only cycle vertices, or exactly one clique vertex and no cycle vertex. Hence \(I(G_{n,h};z)=I(C_n;z)+hz\). The independent-set coefficients on the cycle are
\[
I(C_n;z)=\sum_{k=0}^{d}\frac{n}{n-k}\binom{n-k}{k}z^k.
\]
The usual two-state transfer relation gives \(I(C_n;z)=\lambda_+(z)^n+\lambda_-(z)^n\), where \(\lambda_\pm=(1\pm\sqrt{1+4z})/2\). For \(z=-1/(4\cos^2\alpha)\) with \(0<\alpha<\pi/2\), this equals \(2\cos(n\alpha)/(2\cos\alpha)^n\). Thus all \(d\) zeros are \(-1/a_{n,k}\), and normalization at the origin gives
\[
I(C_n;z)=\prod_{k=1}^{d}(1+a_{n,k}z).
\]
Every factor parameter is strictly positive.

**2. Imaginary-axis crossings.** For \(y>0\), write \(I(C_n;iy)=M(y)e^{i\Theta_n(y)}\), where \(M(y)=\prod_k\sqrt{1+a_{n,k}^2y^2}\). Each phase summand increases from zero to \(\pi/2\); hence \(\Theta_n\) increases strictly from zero to \(d\pi/2\). The equation \(P_{n,u}(iy)=0\) means \(I(C_n;iy)=-iuy\). Matching phase and modulus yields precisely \(\Theta_n(y)=(4j+3)\pi/2\) and \(u=M(y)/y\), with \(4j+3<d\). Conversely these equations provide zeros; conjugation supplies their partners. No zero occurs at \(z=0\), as \(P_{n,u}(0)=1\).

**3. Every crossing is transverse and left-to-right.** Let \(F(z)=I(C_n;z)\). At a boundary zero \(z=iy\), put
\[
A=\sum_k\frac{a_{n,k}}{1+a_{n,k}^2y^2}>0,\qquad
B=\sum_k\frac{a_{n,k}^2}{1+a_{n,k}^2y^2}>0.
\]
Since \(F(iy)=-iuy\) and \(F'(iy)/F(iy)=A-iyB\),
\[
\partial_z P_{n,u}(iy)=u(1-y^2B)-iuyA\ne0.
\]
Implicit differentiation of \(P_{n,u}(z(u))=0\) then gives
\[
\operatorname{Re}\frac{dz}{du}=
\frac{y^2A}{u((1-y^2B)^2+y^2A^2)}>0.
\]
Thus each boundary conjugate pair is simple and enters the right half-plane, never leaving as \(u\) grows. At \(u=0\), all \(d\) zeros are strictly negative real. Continuity of polynomial roots on bounded parameter intervals, with nonzero fixed leading coefficient for \(d\ge2\), makes the displayed crossing list exhaustive. When \(d=1\) the positive linear polynomial is trivially strictly stable. This proves both zero counts, including simultaneous boundary events.

**4. Finite boundary.** \(4j+3<d\) has a solution exactly when \(d\ge4\), equivalent to \(n\ge8\). For \(n=8\),
\[
P_{8,u}(z)=1+(8+u)z+20z^2+16z^3+2z^4.
\]
The real part at \(z=iy\) is \(1-20y^2+2y^4\), whose two positive squared-frequency roots are \(5\pm\tfrac72\sqrt2\). Only the larger has \(u=-\operatorname{Im}F(iy)/y=16y^2-8>0\), giving \(72+56\sqrt2\). The adjacent integer graph cases follow.

**5. Sharp large-cycle asymptotic.** From the coefficients in Step 1,
\[
\sum_k a_{n,k}=n,\qquad \sum_k a_{n,k}^2=3n\quad(n\ge3),
\]
and \(0<a_{n,k}\le4\). The continuous envelope \(H_n(y)=M(y)/y\) has exactly one global minimum \(y_n>0\), since the stationarity equation
\[
\sum_k\frac{a_{n,k}^2 y_n^2}{1+a_{n,k}^2y_n^2}=1
\]
has a strictly increasing left-hand side running from zero to \(d\) for \(d\ge2\). Uniform boundedness of the \(a_{n,k}\) gives \(y_n^2=(3n)^{-1}+O(n^{-2})\). Consequently
\[
\log H_n(y_n)=\tfrac12\sum_k\log(1+a_{n,k}^2y_n^2)-\log y_n
=\tfrac12+\tfrac12\log(3n)+O(n^{-1}),
\]
so \(H_n(y_n)=\sqrt{3en}(1+O(n^{-1}))\). Any crossing threshold is at least this minimum. On the other hand \(\Theta_n(y_n)=ny_n+O(ny_n^3)=\sqrt{n/3}+O(n^{-1/2})\), and \(\Theta_n'(y)=n+O(ny^2)\) on a fixed multiple of the \(n^{-1/2}\) scale. For sufficiently large \(n\), the nearest permitted phase \((4j+3)\pi/2\), spaced by \(2\pi\), is within \(\pi\) of \(\Theta_n(y_n)\), so its unique frequency lies within \(O(n^{-1})\) of \(y_n\). Taylor's theorem applied to \(\log H_n\), whose second derivative is \(O(n)\) there and whose first derivative vanishes at \(y_n\), gives \(H_n(y_{n,j})=H_n(y_n)(1+O(n^{-1}))\). Taking the minimum over crossings proves \(u_n^*=\sqrt{3en}(1+O(n^{-1}))\) and the asserted limit.

## Verification

The independent standard-library program `verify_cycle_clique.py` enumerates all independent sets of \(C_n\) for \(3\le n\le12\), checks its polynomial against the coefficient formula, independently constructs exact rational Routh arrays for a grid of graph-size/positive-integer-clique samples, and compares the resulting exact right-half-plane counts to numerical phase thresholds. It also checks the exact boundary at \(n=8\), moment identities for the cycle root parameters, and four illustrative large-cycle scales. Run `python3 verify_cycle_clique.py` in the extracted directory. These finite checks support but do not prove the all-size statements; all infinite statements follow from Steps 1--5.

## Relationship to prior work

Scott and Sokal [1] identify the hard-core gas partition function with the independence polynomial and study general zero-free regions. Chudnovsky and Seymour [2] prove real negative roots for every claw-free graph, including the cycle before a universal clique is joined; this by itself says nothing about the new right-half-plane roots because the join can create induced claws. Brown and Cameron [3, Corollary 2.2] prove qualitative eventual right-half-plane roots when a sufficiently large clique is joined to any graph of independence number at least four. Their result covers the **existence** of nonstable roots for \(n\ge8\) and large clique, but not a sharp finite-parameter half-plane count or the \(\sqrt n\)-scale threshold and constant. Their Proposition 3.1 treats stars with a different polynomial and their other graph constructions likewise do not yield these claims.

The publicly available *Exact independence-root phase diagram for clique coronas with independent leaves* [4] has an explicit threshold theorem for the factor \((1+z)^k+rz\). That special polynomial has all equal negative roots, whereas the cycle factor has distinct negative roots \(-1/a_{n,k}\); its trigonometric thresholds do not supply the distinct cycle constants or the stated all-cycle census. The closest separate wheel-gas enumeration with an independently fixed hub fugacity concerns \(I(C_n;z)+t\), a **constant perturbation**, with negative-real root collisions; its statement does not imply a half-plane census for the **linear perturbation** \(I(C_n;z)+uz\). Jerrum and Patel [5] study degree-bounded classes and general zero-free neighborhoods of the positive real axis; their results do not provide the present unbounded-hub half-plane threshold.

## Limitations

This is a mathematical result for complex partition-function zeros, not a real positive-fugacity thermodynamic phase transition. The threshold \(u_n^*\) is specified by finite scalar implicit equations, not an elementary radical formula at arbitrary \(n\). Thresholds for different mode indices are not asserted to be distinct or ordered. The \(O(n^{-1})\) relative bound is an asymptotic analytical estimate, not a uniform finite-size error certificate. The self-review are not independent scientific validation; historical priority beyond the inspected works and indexed research results remains uncertain.

## References

1. A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, first posted 2003-09-15, arXiv:cond-mat/0309352; https://arxiv.org/html/cond-mat/0309352v2.
2. M. Chudnovsky and P. Seymour, *The roots of the independence polynomial of a clawfree graph*, J. Combin. Theory Ser. B 97 (2007), 350–357, DOI:10.1016/j.jctb.2006.06.001.
3. J. I. Brown and B. Cameron, *On the Stability of Independence Polynomials*, Electron. J. Combin. 25 (2018), P1.46, DOI:10.37236/7280, https://arxiv.org/abs/1802.02478.
4. *Exact independence-root phase diagram for clique coronas with independent leaves*, public online mathematical record, 2026-10-18, https://github.com/published-finding corpus/2026.
5. M. Jerrum and V. Patel, *Zero-free regions for the independence polynomial on restricted graph classes*, J. London Math. Soc. 113 (2026), e70458, DOI:10.1112/jlms.70458.
