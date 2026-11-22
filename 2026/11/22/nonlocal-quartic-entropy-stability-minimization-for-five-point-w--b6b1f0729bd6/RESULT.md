# Nonlocal quartic entropy-stability minimization for five-point word-length Poisson energy

## Finding

For the word-length Poisson Dirichlet form on the cyclic group of order five, the sharp global quartic logarithmic-Sobolev stability quotient is **strictly smaller** than its exact local limit at the constant function. In the definitions below, the nonnegative unit-\(L^2\) vector
\[
u_* = \sqrt{\frac5{56}}\,(3,1,1,3,6)
\]
satisfies
\[
\boxed{\quad C_{\mathrm w,5}\le R(u_*)<\frac{19}{40}<\frac12=L_{\mathrm w,5}.\quad}
\]
The strict inequality implies that the global minimum \(C_{\mathrm w,5}\) is **attained** by a nonconstant function a positive distance from the constant extremizer. Neither the exact value of \(C_{\mathrm w,5}\) nor the full set of its optimizers is determined here.

## Assumptions and scope

Write \(G=\mathbb Z/5\mathbb Z\) with uniform probability measure. For real \(f:G\to\mathbb R\), set
\[
\langle f\rangle=\frac15\sum_{j=0}^4 f(j),\quad
\widehat f(k)=\frac15\sum_{j=0}^4 f(j)e^{-2\pi i jk/5},\quad
\|f\|_2^2=\langle |f|^2\rangle.
\]
Define the word-length energy
\[
\mathcal E_{\mathrm w}(f)=\sum_{k=0}^4\min\{k,5-k\}\,|\widehat f(k)|^2.
\]
For every nonnegative \(u:G\to[0,\infty)\) satisfying \(\|u\|_2=1\), set \(\operatorname{Ent}(u^2)=\langle u^2\log(u^2)\rangle\), with \(0\log0=0\), and for \(u\not\equiv1\) define
\[
R(u)=\frac{2\mathcal E_{\mathrm w}(u)-\operatorname{Ent}(u^2)}{\|u-1\|_2^4},
\quad C_{\mathrm w,5}=\inf_{u\ge0,\,\|u\|_2=1,\,u\ne1}R(u).
\]
The local limiting lower value is
\[
L_{\mathrm w,5}=\lim_{\delta\downarrow0}\inf\{R(u):0<\|u-1\|_2<\delta,\ u\ge0,\ \|u\|_2=1\}.
\]
Every assertion concerns real nonnegative functions on exactly this five-point group, with this Fourier-energy normalization.

## Proof

**1. An explicit strict global competitor.** Let \(w=(3,1,1,3,6)\), so \(\langle w^2\rangle=56/5\) and \(u_*=\sqrt{5/56}\,w\). Direct discrete Fourier evaluation yields
\[
|\widehat w(1)|^2=\frac{21+8\sqrt5}{25},\qquad
|\widehat w(2)|^2=\frac{21-8\sqrt5}{25};
\]
conjugate symmetry gives the negative frequencies. Consequently,
\[
\mathcal E_{\mathrm w}(u_*)=\frac9{20}-\frac{2\sqrt5}{35},\qquad
\langle u_*\rangle=\sqrt{\frac7{10}},
\]
\[
\operatorname{Ent}(u_*^2)=\frac{27}{14}\log3-\frac{12}{7}\log2-\log\frac75,
\qquad
\|u_*-1\|_2^4=4\bigl(1-\sqrt{7/10}\bigr)^2.
\]
Substitution gives \(R(u_*)\approx0.47246766718\). More importantly, the *strict rational inequality* \(R(u_*)<19/40\) follows with no floating-point assumptions: `verify_wordlength_c5.py` encloses each square root between rationals with denominator \(10^{12}\), and the logarithms by positive finite atanh sums with exact positive geometric tail majorants. Its final rational assertions imply
\[
0<2\mathcal E_{\mathrm w}(u_*)-\operatorname{Ent}(u_*^2)<\frac{19}{40}\|u_*-1\|_2^4.
\]
The verifier is supplementary to the explicit exact expressions above and is a reproducible certificate of this strict comparison.

**2. The exact local value.** Let \(u\to1\) through admissible nonconstant functions. Write \(u=a+v\), where \(a=\langle u\rangle=\sqrt{1-S}\), \(\langle v\rangle=0\), and \(S=\langle v^2\rangle\to0\). Decompose orthogonally \(v=x+y\), with \(x\) supported on Fourier modes \(\{1,4\}\) and \(y\) on \(\{2,3\}\); set \(s=\|x\|_2\) and \(z=\|y\|_2\). Then
\[
S=s^2+z^2,\quad\mathcal E_{\mathrm w}(u)=S+z^2,\quad
\|u-1\|_2^2=2(1-\sqrt{1-S})=S+O(S^2).
\]
Taylor's formula for \(r\mapsto r^2\log r^2\), uniformly in the five coordinates near \(1\), gives
\[
2\mathcal E_{\mathrm w}(u)-\operatorname{Ent}(u^2)
=2z^2-\frac23\langle v^3\rangle+\frac16\langle v^4\rangle
+\frac12S^2+O(S^{5/2}). \tag{1}
\]
For each pure real Fourier mode pair on \(G\), the third average vanishes: \(\langle x^3\rangle=\langle y^3\rangle=0\). Fourier orthogonality gives
\[
\|P_{\{2,3\}}x^2\|_2=\frac{s^2}{\sqrt2},\quad
|\langle x^2y\rangle|\le\frac{s^2z}{\sqrt2},\quad
|\langle xy^2\rangle|\le\sqrt2\,s z^2.
\]
Hence \(|\langle v^3\rangle|\le(3/\sqrt2)s^2z+3\sqrt2\,sz^2\). If \(z/S\) is unbounded along a subsequence, (1), nonnegativity of \(\langle v^4\rangle\), and \(S\downarrow0\) give \(R(u)\to+\infty\) on a further subsequence: \(2z^2\) dominates \(O(Sz)+O(\sqrt S z^2)+O(S^2)\). Thus any sequence with bounded quotient has \(z=O(S)\).

On such a sequence, \(s^2=S+O(S^2)\) and the single-mode fourth moment is \(\langle x^4\rangle=\tfrac32s^4\), so \(\langle v^4\rangle=\tfrac32S^2+o(S^2)\). Equation (1) therefore gives
\[
2\mathcal E_{\mathrm w}(u)-\operatorname{Ent}(u^2)
\ge 2z^2-\sqrt2\,S z+\frac34S^2+o(S^2)
=2\bigl(z-\tfrac{S}{2\sqrt2}\bigr)^2+\frac12S^2+o(S^2).
\]
Dividing by \(\|u-1\|_2^4=S^2(1+o(1))\) proves \(L_{\mathrm w,5}\ge1/2\). For the reverse bound, let
\[
u_t(j)=\frac{1+\sqrt2\,t\cos(2\pi j/5)+(t^2/2)\cos(4\pi j/5)}{
\bigl\|1+\sqrt2\,t\cos(2\pi(\cdot)/5)+(t^2/2)\cos(4\pi(\cdot)/5)\bigr\|_2},\qquad t\downarrow0.
\]
These vectors are positive for small \(t>0\). They satisfy \(S=t^2+O(t^4)\), \(z=S/(2\sqrt2)+o(S)\), and the phase of \(y\) aligns with the second-harmonic component of \(x^2\), so equality is asymptotically attained in the square completion. Hence \(R(u_t)\to1/2\), proving \(L_{\mathrm w,5}=1/2\).

**3. Global attainment away from the constant.** The admissible nonnegative unit sphere in \(\mathbb R^5\) is compact. The numerator of \(R\) is continuous there (including coordinates equal to zero), while its denominator vanishes only at \(u=1\). Since a strict competitor has value below \(L_{\mathrm w,5}=1/2\), no minimizing sequence with values tending to \(C_{\mathrm w,5}\) can converge to the constant. A convergent subsequence therefore has a nonconstant limit at which \(R\) achieves its infimum. This proves the qualitative nonlocal-attainment statement.

## Verification

Run `python3 verify_wordlength_c5.py` using standard Python; it performs rational interval arithmetic for every radical and logarithm entering the witness and prints the certified deficit, distance, and ratio intervals. The recorded ratio enclosure is \((0.4724676671819746,\ 0.4724676671888323)\); the decimal endpoints are displays of exact rational bounds, not inputs to the proof. The all-admissible local asymptotics and compactness argument are analytic and do not rely on finite sampling or the script.

## Relationship to prior work

Chen–Lam–Lu, *Sharp uniform stability of the logarithmic Sobolev inequality on finite cycles and stability of the cubic Sobolev inequality*, arXiv:2610.05347, Theorem 1.2, Section 6.4 and Appendix A, establishes \(503/1500\le C_{\mathrm w,5}\le1/2\), deriving the upper value using a near-constant Fourier family. It expressly does not determine the sharp constant for \(n\ge5\). The present strict \(C_{\mathrm w,5}<19/40<1/2\) and global attainment mechanism are not consequences of those bounds. Xie–Zhang, arXiv:2606.02847, developed preceding word-length logarithmic-Sobolev stability lower bounds. An earlier local-quartic analysis on cycles establishes the precise infinitesimal coefficient \(1/2\) for this word-length energy; the argument above independently reconstructs it. Results for the *normalized nearest-neighbor energy* concern a distinct multiplier, namely \(\frac{1-\cos(2\pi k/5)}{1-\cos(2\pi/5)}\), and their strict global comparisons do not imply the present word-length inequality because the local comparison thresholds differ.

## Limitations

The witness establishes a strict **upper bound**, not the exact optimum, its uniqueness, or a complete optimizer classification. No positive quantitative lower bound on the distance of every optimizer from the constant is stated. The local calculation is asymptotic and not a global lower bound of \(1/2\). The priority search covers specifically identified papers, related published records and equivalent formulations; an unlocated older equivalent statement remains possible. The result has undergone only self-review, with no independent audit.

## References

1. L. Chen, N. Lam and G. Lu, *Sharp uniform stability of the logarithmic Sobolev inequality on finite cycles and stability of the cubic Sobolev inequality*, initial arXiv public version October 4, 2026, https://arxiv.org/abs/2610.05347.
2. X. Xie and H. Zhang, *Sharp log-Sobolev inequalities and quartic stability on finite cyclic groups*, arXiv:2606.02847, https://arxiv.org/abs/2606.02847.
3. *Exact local quartic stability constants at the constant extremizer on cycles*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-local-quartic-stability-constants-at-the-constant-extremiz--3ea04e5fdc28.
