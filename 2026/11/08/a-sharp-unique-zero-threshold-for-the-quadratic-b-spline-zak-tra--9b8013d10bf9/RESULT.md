# A sharp unique-zero threshold for the quadratic B-spline Zak transform

## Finding
Let the centered quadratic B-spline \(B_3\) and its Zak transform \(Z_\lambda B_3\) be as below. On the first subunit band \(1/2\le\lambda\le1\), the unique zero in a fundamental cell is \((x,\nu)=(1/2,1/2)\) **if and only if** \(3/5\le\lambda\le1\). More precisely, when \(1/2\le\lambda<3/5\) and \(b=1/\lambda\), the entire interval
\[
\left\{(x,1/2):\ \tfrac32(2-b)\le x\le1-\tfrac32(2-b)\right\}
\]
consists of Zak zeros; the interval has positive length and the case \(b=2\) gives the whole horizontal circle. This latter zero interval is already a consequence of the published boundary-line theorem [1, Proposition 4.3]; the new assertion is the complete absence of any other zeros for \(3/5\le\lambda<1\).

## Assumptions and scope
For every \(t\in\mathbb R\), set
\[
 B_3(t)=\begin{cases}
 \tfrac34-t^2,&|t|\le\tfrac12,\\
 \tfrac12(\tfrac32-|t|)^2,&\tfrac12\le|t|\le\tfrac32,\\
 0,&|t|\ge\tfrac32.
 \end{cases}
\]
For every \(\lambda>0\), \(x,\nu\in\mathbb R\), define
\[
 Z_\lambda B_3(x,\nu)=\sqrt\lambda\sum_{k\in\mathbb Z}B_3(\lambda(x-k))e^{2\pi i k\nu}.
\]
The sum is finite. Zeros are counted geometrically in \([0,1)\times[0,1)\); multiplicities are not asserted. The theorem is limited to the *entire* parameter band \(1/2\le\lambda\le1\) and is not an assertion about smaller positive scales, arbitrary spline orders or arbitrary Gabor frame sets.

## Proof
Write \(b=1/\lambda\). First suppose \(1\le b\le5/3\). By evenness, complex conjugation, periodicity in \(\nu\), and Zak quasi-periodicity in \(x\), it is enough to inspect \(0\le x,\nu\le1/2\). Put \(\theta=2\pi\nu\), \(a_j(x)=B_3((x-j)/b)\) and \(T=3b/2\). In this reduced square, only \(j=-2,-1,0,1,2\) can contribute, so
\[
 \frac{Z_{1/b}B_3(x,\nu)}{b^{-1/2}}=
 a_0+a_1e^{i\theta}+a_{-1}e^{-i\theta}+a_2e^{2i\theta}+a_{-2}e^{-2i\theta}.
\]

**Exclusion of interior frequencies.** Define \(\Delta_1(x)=a_1(x)-a_{-1}(x)\), \(\Delta_2(x)=a_2(x)-a_{-2}(x)\), and \(D_b(x)=\Delta_1(x)-2\Delta_2(x)\). Both \(\Delta_j\) are nonnegative for \(x\ge0\) by evenness and monotonicity of \(B_3\). Thus for \(0<\theta<\pi\),
\[
 b^{1/2}\Im Z_{1/b}B_3(x,\nu)
 =\sin\theta\,[\Delta_1(x)+2\Delta_2(x)\cos\theta]
 \ge\sin\theta D_b(x).
\]
Now \(D_b(0)=0\), and \(D_b\) is concave on \([0,1/2]\). Indeed, away from finitely many knots, \(b^2a_{-1}''=1\), \(b^2a_1''\in\{-2,1\}\), and \(b^2a_{\pm2}''\in\{0,1\}\); whenever \(a_{-2}''\ne0\), also \(a_2''\ne0\). Consequently
\[
 b^2D_b''=b^2a_1''-1-2b^2a_2''+2b^2a_{-2}''\le0.
\]
The first derivatives remain continuous at knots. At the other endpoint,
\[
 D_b(1/2)=B_3(1/(2b))-3B_3(3/(2b))
 =\frac{-21b^2+54b-29}{8b^2}>0\qquad(1\le b\le5/3),
\]
since its numerator is concave and positive at both endpoints \(b=1\) and \(b=5/3\). Concavity gives \(D_b(x)\ge2xD_b(1/2)>0\) for \(0<x\le1/2\). Therefore there are no zeros with \(0<x\le1/2\) and \(0<\nu<1/2\).

**The boundary \(x=0\).** Here the Zak sum is the real polynomial in \(t=\cos\theta\),
\[
 P_b(t)=a_0(0)-2a_2(0)+2a_1(0)t+4a_2(0)t^2.
\]
We have \(a_0(0)=3/4\), \(a_1(0)=\tfrac12(3/2-1/b)^2\), and \(a_2(0)=\tfrac12(3/2-2/b)_+^2\). Throughout \(1\le b\le5/3\), \(a_1(0)\ge4a_2(0)\), so \(P_b\) is nondecreasing on \([-1,1]\). Its minimum occurs at \(t=-1\), with value
\[
 P_b(-1)=\begin{cases}
 \frac34-(\frac32-\frac1b)^2>0,&1\le b\le4/3,\\
 \frac{3(b-2)^2}{4b^2}>0,&4/3\le b\le5/3.
 \end{cases}
\]
Hence no zero occurs at \(x=0\), for any frequency.

**The boundary \(\nu=0\) or \(\nu=1/2\).** At \(\nu=0\) the sum is strictly positive. At \(\nu=1/2\), write
\[
 R_b(x)=b^{1/2}Z_{1/b}B_3(x,1/2)=a_0-a_1-a_{-1}+a_2+a_{-2}.
\]
By symmetry \(R_b(1/2)=0\). We verify \(R_b(x)>0\) for \(0\le x<1/2\) directly. Let \(x_0=1-b/2>0\) and \(q=3b/2-2\). For \(0<x<1/2\) outside knots, differentiation yields
\[
 b^2R_b'(x)=-4x+3(x-x_0)_++\begin{cases}
 (x+q)_+,&q\le0,\\
 x+\min(x,q),&q\ge0.
 \end{cases}
\]
If \(1\le b\le4/3\), this is at most \(-3x+3(x-x_0)_+<0\). If \(4/3\le b\le5/3\), it is at most \(-2x+3(x-x_0)_+<0\) for \(0<x<1/2\), since \(x_0\ge1/6\). Continuity and \(R_b(1/2)=0\) yield \(R_b(x)>0\) for \(0\le x<1/2\). Together with the previous steps and the Zak symmetries, the only zero for \(1\le b\le5/3\) is \((1/2,1/2)\).

**Sharpness.** For \(5/3<b\le2\), let \(d=2-b\in[0,1/3)\). The published aliasing identity [1, Proposition 4.3 and its proof] shows
\[
 Z_{1/b}B_3(x,1/2)=0\quad\text{for every}\quad \tfrac32d\le x\le1-\tfrac32d.
\]
This interval has positive length \(1-3d=3b-5\), including when \(b=2\), and proves that uniqueness fails at every \(1/2\le\lambda<3/5\). This proves the sharp if-and-only-if statement. \(\square\)

## Verification
The algebra above is an infinite-parameter proof, not a numerical extrapolation. A standalone Python 3 checker, `CHECK.py`, independently evaluates the five-site formulas using exact rational arithmetic on a finite grid of rational parameters and spatial points; it also verifies the predicted horizontal intervals below the threshold. Run `python3 CHECK.py` from this directory. Grid tests are supplementary and do not establish the universal inequalities.

## Relationship to prior work
Hasannasab--Lemvig [1] classify the complete zero set for the hat spline at all scales and for higher-order splines at scales \(\lambda\ge1\); their Proposition 4.3 describes the \(\nu=1/2\) boundary zeros for every scale, and their Section 6 analyzes a symmetry fiber. The present theorem determines the *whole two-variable zero set* for the quadratic spline in the new subunit interval \(3/5\le\lambda<1\), including the exclusion of off-axis zeros. Kloos [2] studies totally positive functions and exponential B-splines; its general uniqueness result does not directly cover arbitrary dilations of compactly supported polynomial B-splines [1, Introduction]. Lemvig [3] concerns Gabor-frame obstructions rather than the asserted full zero-set classification, and Stangl--Frederick [4] treats the second-order hat spline.

## Limitations
This does not classify zero sets for \(\lambda<1/2\), higher spline orders, or frame sets of arbitrary sampling lattices. The below-threshold zero interval is a previously known boundary-line consequence and is not presented as a new independent result. Publication priority beyond the accessible sources is not independently established; an earlier unindexed equivalent full-zero classification is possible. The finite checker does not replace the proof, and independent mathematical validation is not asserted.

## References
[1] M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116v1 (2026-09-11), https://arxiv.org/abs/2609.13116 .

[2] T. Kloos, *Zeros of the Zak transform of totally positive functions*, arXiv:1411.1539, https://arxiv.org/abs/1411.1539 .

[3] J. Lemvig, *A new family of hyperbolic slits in the Gabor frame set of B-spline generators*, arXiv:2601.07642, https://arxiv.org/abs/2601.07642 .

[4] A. Stangl and C. Frederick, *The frameset of the second-order B-spline along ab=1/q*, arXiv:2609.00481, https://arxiv.org/abs/2609.00481 .
