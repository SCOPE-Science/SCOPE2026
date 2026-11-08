# Sharp symmetric-positive-definite spectral frontier for two-coordinate discrete-potential absolute-value equations

## Finding

For the absolute-value equation (AVE) \(Ax-|x|=b\), define, for each sign vector \(z\in\{-1,1\}^2\),
\[
Z=\operatorname{diag}(z),\qquad x(z)=(A-Z)^{-1}b,\qquad F(z)=z^{\mathsf T}x(z).
\]
Suppose \(A\) is real symmetric positive definite and \(\lambda_{\min}(A)>1\). Put
\[
L_* = \frac{1+\sqrt 2}{2},\qquad c_*=\frac1{L_*}=2(\sqrt2-1).
\]

**Sharp universal frontier.** If \(\lambda_{\min}(A)\ge L_*\), then for every \(b\in\mathbb R^2\), a sign vector maximizes \(F\) if and only if its candidate \(x(z)\) solves the AVE. From every inconsistent sign vector, flipping **any nonempty subset of its strictly mismatched coordinates** increases \(F\) strictly. In two dimensions, \(\rho(|A^{-1}|)=1/\lambda_{\min}(A)\), so the same condition is \(\rho(|A^{-1}|)\le c_*\).

The frontier is optimal within this class. For **every** \(1<L<L_*\), some symmetric positive-definite \(2\times2\) matrix with \(\lambda_{\min}(A)=L\) and some right-hand side \(b\) have a unique global maximizer \(z=(1,1)\) whose candidate has a negative first coordinate. Thus the maximal universal spectral-radius guarantee is precisely \(c_*\) (inclusive). This is a guarantee about this unweighted discrete potential, not a lower bound for all possible AVE solvers.

## Assumptions and scope

All matrices and vectors are real, calculations are exact, \(|x|\) denotes componentwise absolute value, and \(\rho(|A^{-1}|)\) uses entrywise absolute value. The threshold is universal over all \(b\) and all symmetric positive-definite \(2\times2\) matrices satisfying the stated lower spectral bound; the converse is existential for each lower bound \(L\in(1,L_*)\). The AVE has a unique solution in this class since \(x\mapsto A^{-1}(|x|+b)\) is a strict Euclidean contraction when \(\lambda_{\min}(A)>1\).

A coordinate \(i\) is *mismatched* when \(z_i x_i(z)<0\). Zero coordinates are allowed and are never counted as mismatches. An AVE-consistent sign vector obeys \(z_i x_i(z)\ge0\) for both coordinates.

## Proof

**1. Exact polarity formula.** Write
\[
A=\begin{pmatrix}a&c\\c&d\end{pmatrix},\quad
D(z)=\det(A-Z)>0,\quad y(z)=(A-Z)^{-\mathsf T}z.
\]
Since \(\lambda_{\min}(A)>1\), every \(A-Z\) is positive definite. Direct inversion gives
\[
1+y_1(z)=\frac{\det A-z_2(a+c)}{D(z)},\qquad
1+y_2(z)=\frac{\det A-z_1(d+c)}{D(z)}. \tag{1}
\]
For \(\lambda_{\min}(A)=L\ge L_*\), write \(A=LI+P\) with \(P=\left(\begin{smallmatrix}u&c\\c&w\end{smallmatrix}\right)\succeq0\), so \(u,w\ge0\) and \(|c|\le\sqrt{uw}\). Then
\[
\begin{aligned}
\det A-|a+c|&\ge L(L-1)+(L-1)u+Lw-\sqrt{uw},\\
\det A-|d+c|&\ge L(L-1)+Lu+(L-1)w-\sqrt{uw}.
\end{aligned} \tag{2}
\]
The arithmetic-geometric mean inequality makes both remaining quadratic forms nonnegative when \(4L(L-1)\ge1\). Hence both differences in (2) are strictly positive. Equation (1) proves \(1+y_i(z)>0\) for every coordinate and every sign pattern, including at \(L=L_*\).

**2. Global-optimum equivalence and ascent.** For any two sign vectors \(z,w\), let \(S=\{i:z_i\ne w_i\}\). The resolvent identity, applied to \((A-Z)x(z)=b=(A-W)x(w)\), gives the exact finite-difference formula
\[
F(w)-F(z)=-2\sum_{i\in S} z_i x_i(z)\bigl(1+y_i(w)\bigr). \tag{3}
\]
If \(z\) is AVE-consistent, every term on the right is nonpositive for every \(w\), so \(z\) globally maximizes \(F\). Conversely, if \(z_i x_i(z)<0\), flipping coordinate \(i\) alone makes (3) strictly positive. Therefore a maximizer cannot be inconsistent. More generally, flipping any nonempty subset of mismatched coordinates produces a strictly positive sum. This establishes the full guarantee.

**3. Explicit sharp counterexample family.** Fix \(L=1+h\) with
\[
0<h<\frac{\sqrt2-1}{2},\quad s=\frac1{2h},\quad
 t>\frac{Lh}{1/(4h)-L},\quad
 A=LI+t\begin{pmatrix}s\\1\end{pmatrix}\begin{pmatrix}s&1\end{pmatrix}. \tag{4}
\]
This matrix is symmetric positive definite with eigenvalues \(L\) and \(L+t(s^2+1)\). Its entries are \(a=L+ts^2\), \(c=ts\), \(d=L+t\). Direct calculation yields
\[
\det A-(a+c)=Lh+t\left(L-\frac1{4h}\right)<0, \tag{5}
\]
and
\[
\det A-(d+c)=Lh+t\frac{1-h+4h^3}{4h^2}>0. \tag{6}
\]
Thus \(1+y_1(-1,1)<0\), whereas \(1+y_2(z)>0\) for all four sign vectors.

Take \(b_0=(A-I)e_2\). For \(z=(1,1)\) and \(z=(-1,1)\), the candidate is \(e_2\), and both potentials equal \(1\). Every sign vector with second sign \(-1\) has strictly smaller potential: flip that second sign from a vector with second sign \(+1\) and use (3), with \(x_2=1\) and the strict positivity from (6). Thus these are exactly the two maximizers at \(b_0\).

Now perturb to \(b_\varepsilon=(A-I)(-\varepsilon,1)^{\mathsf T}\), with \(\varepsilon>0\). At \(z=(1,1)\), the candidate is \((-\varepsilon,1)^{\mathsf T}\), which mismatches its first sign. Formula (3), when flipping just the first sign, gives
\[
F(-1,1)-F(1,1)=2\varepsilon\bigl(1+y_1(-1,1)\bigr)<0. \tag{7}
\]
The other two strict potential gaps at \(\varepsilon=0\) persist by continuity for all sufficiently small positive \(\varepsilon\). Therefore \((1,1)\) is then the **unique** global maximizer but is not AVE-consistent. This construction works for every \(L\in(1,L_*)\), proving sharpness.

**4. Spectral-radius equivalence.** The symmetric \(2\times2\) matrix \(A^{-1}\) has positive diagonal entries. Its entrywise absolute-value matrix is orthogonally similar to \(A^{-1}\) through a diagonal sign conjugation. Therefore \(\rho(|A^{-1}|)=\rho(A^{-1})=1/\lambda_{\min}(A)\), completing the stated spectral formulation.

## Verification

The standalone Python 3 script `verify_spd_dpo.py` uses exact rational arithmetic to check the flip identity on every pair of the four sign vectors, verify a rational witness, sample 250 safe positive-definite rank-one-perturbed systems, and test three additional sharp-family witnesses. It requires no nonstandard packages and exits with `VERIFY_OK` on success.

A fully rational witness is
\[
A=\begin{pmatrix}18/5&1/2\\1/2&6/5\end{pmatrix},\qquad
b=(237/500,39/200)^{\mathsf T},\quad
\lambda_{\min}(A)=11/10.
\]
Its exact potentials, in the order \( (--),(-+),(+-),(++)\), are
\[
-5351/32900,\quad 6627/6700,\quad 6753/54700,\quad 99/100.
\]
The unique maximizer is \((++)\), whose candidate is \((-1/100,1)^{\mathsf T}\). This finite example illustrates the theorem but does **not** prove the all-parameter statements; those follow from (1)--(7).

## Relationship to prior work

Chen and Xia, *Discrete Potential Optimization for Absolute Value Equations: A Sign-Flip Framework with Polynomial Complexity* (arXiv:2609.12763), introduce \(F\), establish its flip identity, and show correctness under \(\|A^{-1}\|_1<1/2\), with a scaled spectral-radius guarantee below \(1/2\). The present result concerns a narrower but natural symmetric-positive-definite two-coordinate class and proves the **exact larger** sharp unscaled spectral-radius frontier \(2(\sqrt2-1)\). The source's sufficient bound alone does not imply this new range.

The published published-finding corpus finding *The one-half threshold is sharp for discrete-potential AVE certification* (record `ba2cd47befbe`, September 2026) provides two-coordinate counterexamples for general **nonsymmetric** matrices immediately beyond the threshold \(1/2\). Its constructions do not cover the symmetric-positive-definite subclass or imply the present safe range; conversely, the current theorem makes no claim to improve the unrestricted-matrix threshold. The overview by Hladík and coauthors surveys AVE uniqueness and algorithms, including sign accord, but does not present the 2026 DPO potential's sharp symmetric spectral frontier.

## Limitations

This is an exact-arithmetic result for \(2\times2\) **symmetric positive-definite** matrices with \(\lambda_{\min}>1\). It does not classify nonsymmetric matrices, higher-dimensional positive-definite systems, other discrete potentials, finite-precision pivoting, bit complexity, or optimality of generalized Newton methods outside the stated setting. The threshold's converse concerns failure of the potential's global-maximizer correspondence, **not** failure of every sign-update method. Possible older specialized priority remains a literature risk.

## References

1. C. Chen and Y. Xia, *Discrete Potential Optimization for Absolute Value Equations: A Sign-Flip Framework with Polynomial Complexity*, arXiv:2609.12763v1 (11 September 2026), later revision v2 (21 October 2026). https://arxiv.org/abs/2609.12763
2. *The one-half threshold is sharp for discrete-potential AVE certification*, published-finding corpus public research record `ba2cd47befbe` (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-dpo-half-threshold-sharpness--ba2cd47befbe
3. M. Hladík et al., *An overview of absolute value equations: from theory to solution methods and challenges*, *Computational Optimization and Applications* 93 (2026), 435--488, publicly available online 8 August 2025. https://doi.org/10.1007/s10589-025-00717-5
4. J. Rohn, *An algorithm for solving the absolute value equation*, *Electronic Journal of Linear Algebra* 18 (2009), 589--599. https://doi.org/10.13001/1081-3810.1332
