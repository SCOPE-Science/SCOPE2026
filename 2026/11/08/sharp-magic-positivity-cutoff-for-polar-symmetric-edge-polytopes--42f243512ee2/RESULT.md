# Sharp magic-positivity cutoff for polar symmetric-edge polytopes of \(K_{3,q}\)

## Finding
Let \(q\ge1\) be an integer, let \(G=K_{3,q}\), and define the symmetric edge polytope \(\mathcal P_G=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G)\}\) in the zero-coordinate-sum lattice. Write \(P_q=\mathcal P_G^{\vee}\) for its polar with respect to the dual lattice, and \(L_q(t)=|tP_q\cap M|\) for the Ehrhart polynomial. Its degree is \(d=q+2\). Define the magic coefficients by the unique expansion
\[
L_q(t)=\sum_{i=0}^{d}a_i(q)t^i(t+1)^{d-i}.
\]
**Theorem.** All \(a_i(q)>0\) if and only if \(1\le q\le6\). For every integer \(q\ge7\), at least one magic coefficient is strictly negative. In particular, the ordinary nonnegative convention for magic positivity gives the same cutoff: every coefficient is positive below the cutoff and a coefficient is negative above it.

## Assumptions and scope
The graph is the simple connected complete bipartite graph with left part of size exactly three and right part of arbitrary positive size. The ambient lattice for the polar identifies graph potentials modulo simultaneous integer translation; one left potential is set to zero. The variable \(t\) is a nonnegative integer when counting lattice points and an indeterminate when considering the Ehrhart polynomial. Bernoulli numbers use \(B_1=-1/2\); \(S_m(N)=\sum_{j=1}^N j^m\) for integers \(N\ge0\), with its canonical Faulhaber-polynomial extension. No statement is made about bipartite left-part sizes other than three, or about positivity of coefficients in the monomial basis.

## Proof
### The exact lattice-point count
The polar inequalities are \(|f(u)-f(v)|\le t\) along graph edges, with integer potentials \(f\) modulo a common translation. Fix the first of the three left values to zero and call the remaining two left values \(x,y\in\mathbb Z\). The spread of the three left potentials is \(r=\max(0,x,y)-\min(0,x,y)\). Every right potential must lie in the intersection of the three integer intervals centered at the left values with radius \(t\). Hence it has \(2t+1-r\) choices when \(r\le2t\) and zero choices otherwise. The \(q\) right potentials are independent.

The number of integer pairs \((x,y)\) having spread at most \(r\) is \(1+3r(r+1)\) for integer \(r\ge0\): split into the nonnegative quadrant, the nonpositive quadrant and the two mixed-sign wedges, with overlap counted once. Consequently, precisely \(6r\) pairs have spread exactly \(r\ge1\), and one pair has spread zero. This proves, for every \(t\in\mathbb Z_{\ge0}\),
\[
\boxed{L_q(t)=(2t+1)^q+6\sum_{r=1}^{2t}r(2t+1-r)^q}
=(2t+1)^q+6\bigl((2t+1)S_q(2t)-S_{q+1}(2t)\bigr).
\]
The rightmost expression is a polynomial of degree \(q+2\), and agreement on all nonnegative integers identifies it with the Ehrhart polynomial.

### The first two magic coefficients
Put \(L_q(t)=\sum_{j=0}^d c_jt^j\) and \(c_0=1\). The magic change of basis is the finite identity
\[
a_i(q)=\sum_{j=0}^i(-1)^{i-j}\binom{d-j}{i-j}c_j.
\]
For every \(q\ge3\), the Faulhaber derivatives give \(S_m'(0)=B_m\) and \(S_m''(0)=mB_{m-1}\) for \(m\ge3\). (Here differentiation is with respect to the upper-limit variable, before substitution of \(2t\).) Applying the identities to the preceding count yields
\[
\boxed{a_1(q)=q-2+12(B_q-B_{q+1}),}\qquad
\boxed{a_2(q)=\frac{q^2-5q+2}{2}+12qB_{q-1}-24qB_q+12(q+1)B_{q+1}.}
\]
These identities use the Bernoulli convention above and are asserted only for \(q\ge3\).

### An elementary Bernoulli lower bound
For every even integer \(r\ge14\), we claim \(|B_r|\ge r/12\). Euler's even-Bernoulli formula implies
\[
\frac{|B_{r+4}|}{|B_r|}=
\frac{(r+1)(r+2)(r+3)(r+4)}{(2\pi)^4}\frac{\zeta(r+4)}{\zeta(r)}.
\]
For \(r\ge14\), \(1<\zeta(r)<2\) and \(\pi<4\), so the ratio is strictly greater than \((r+1)(r+2)(r+3)(r+4)/8192\). At \(r=14\), this lower bound is \(73440/8192>8\), and it increases with \(r\), whereas \((r+4)/r<2\) throughout this range. Thus \(|B_{r+4}|/(r+4)>|B_r|/r\) for every even \(r\ge14\). The two base cases are \(B_{14}=7/6=14/12\) and \(B_{16}=-3617/510\), whose absolute value exceeds \(16/12\). Induction in the two even residue classes proves the claim.

A second estimate is needed when \(q\equiv3\pmod4\) and \(q\ge15\). Euler's same formula, together with \(\zeta(q-1)<2\) and \(\pi^2<10\), gives
\[
\frac{|B_{q+1}|}{B_{q-1}}
=\frac{q(q+1)}{4\pi^2}\frac{\zeta(q+1)}{\zeta(q-1)}
>\frac{q(q+1)}{80}\ge3.
\]
In this congruence class, both \(B_{q-1}>0\) and \(B_{q+1}<0\).

### Uniform exclusion of all sufficiently large parameters
Separate the integers \(q\ge13\) by residue modulo four:

* If \(q\equiv0\pmod4\), then \(q\ge16\), \(B_q<0\), and \(B_{q+1}=0\). Thus \(a_1(q)=q-2-12|B_q|\le-2<0\).
* If \(q\equiv1\pmod4\), then \(q\ge13\), \(B_q=0\), and \(B_{q+1}>0\). Hence \(a_1(q)=q-2-12B_{q+1}\le-3<0\).
* If \(q\equiv2\pmod4\), then \(q\ge14\), \(B_{q-1}=B_{q+1}=0\), and \(B_q>0\). Consequently \(a_2(q)\le(q^2-5q+2)/2-2q^2<0\).
* If \(q\equiv3\pmod4\), then \(q\ge15\), \(B_q=0\), \(B_{q-1}>0\), and \(B_{q+1}<0\). The preceding ratio estimate gives \(B_{q-1}<|B_{q+1}|/3\); hence
\[
a_2(q)<\frac{q^2-5q+2}{2}-(8q+12)|B_{q+1}|
\le\frac{q^2-5q+2}{2}-\frac{(8q+12)(q+1)}{12}
=-\frac{q(q+25)}6<0.
\]
Thus no integer \(q\ge13\) has all magic coefficients nonnegative.

### Remaining dimensions, with exact rational certificates
The following are the complete magic vectors, listed in increasing index, for \(1\le q\le6\):

| \(q\) | \((a_0,\dots,a_{q+2})\) |
|---:|---|
|1|\((1,3,3,1)\)|
|2|\((1,2,2,2,1)\)|
|3|\((1,7/5,12/5,12/5,7/5,1)\)|
|4|\((1,8/5,11/5,16/5,11/5,8/5,1)\)|
|5|\((1,19/7,5/7,33/7,33/7,5/7,19/7,1)\)|
|6|\((1,30/7,4/7,18/7,74/7,18/7,4/7,30/7,1)\)|

Every entry is strictly positive. For \(7\le q\le12\), respectively, the negative witnesses \((q,i,a_i(q))\) are \((7,3,-142/15)\), \((8,3,-272/15)\), \((9,4,-1242/11)\), \((10,4,-2235/11)\), \((11,5,-601467/455)\), and \((12,3,-5952/13)\). These rational entries follow from the exact lattice-count polynomial by the stated magic-basis formula; they can also be reproduced with the accompanying checker. Together with the four infinite residue classes, this exhausts every integer \(q\ge1\) and proves the theorem.

## Verification
Run `python3 verify.py` in a directory containing the companion file. The self-contained program uses only the Python standard library, exact integer sums, rational interpolation and rational Bernoulli numbers. It checks the Ehrhart identity by direct graph-potential enumeration, recalculates magic vectors, verifies the finite cutoff cases and independently matches the two Bernoulli coefficient identities. Expected output begins with `EXACT_CHECKS_OK 410` and prints the first twelve complete coefficient vectors. These 410 finite exact checks test the certificates; the all-parameter proof is the analytic argument above. Every claimed uniform inequality has been separately verified algebraically.

## Relationship to prior work
Konoike's 2025 work and associated FPSAC poster tabulate finite complete-bipartite polar examples, including positivity at \(K_{3,6}\) and failure at \(K_{3,7}\). This supplies the natural sharp-threshold question but not a no-return theorem for every larger right part. Ohsugi and Tsuchiya (arXiv:2610.06419, submitted October 5, 2026; primary 52B20) prove magic positivity for polar duals of pseudo-symmetric simplicial reflexive polytopes, and for polar duals associated with cycles, not the present all-parameter complete-bipartite classification. The present theorem is consistent with their positive subclasses because the nonpositive examples here are outside those assumptions. The related two-left-vertex \(K_{2,q}\) threshold has a distinct bound and does not imply this result. Search comparisons and source inspections are documented in the accompanying review; absence of a search match is not a priority certificate.

## Limitations
The statement is specific to the polar of \(K_{3,q}\); it neither classifies general \(K_{p,q}\) nor addresses Ehrhart positivity in the ordinary monomial basis. The computation is not a replacement for the universal Bernoulli proof. Historical priority and the proof itself have not undergone independent mathematical audit. The early 2025 finite table already records cases on both sides of the boundary; the contribution is the infinite no-return classification and its exact obstruction.

## References
1. H. Ohsugi and A. Tsuchiya, *Magic positivity for polar duals of pseudo-symmetric smooth Fano polytopes*, arXiv:2610.06419, first submitted 2026-10-05, https://arxiv.org/abs/2610.06419 .
2. M. Konoike, *A New Class of Magic Positive Ehrhart Polynomials of Reflexive Polytopes*, Séminaire Lotharingien de Combinatoire 93B (2025), Article 148; first preprint arXiv:2409.16648 (2024-09-25), https://emis.muni.cz/journals/SLC/wpapers/FPSAC2025/148.html .
3. M. Konoike, *A new class of magic positive Ehrhart polynomials of reflexive polytopes*, FPSAC 2025 conference poster with complete-bipartite sign table, https://www.math.sci.hokudai.ac.jp/sympo/fpsac2025/public/posters/87.pdf .
4. Classical Euler formula for even Bernoulli numbers \(|B_{2m}|=2(2m)!\zeta(2m)/(2\pi)^{2m}\), under the standard \(B_1=-1/2\) convention.
