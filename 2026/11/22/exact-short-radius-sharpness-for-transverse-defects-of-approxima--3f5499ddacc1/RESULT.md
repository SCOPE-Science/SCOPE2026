# Exact short-radius sharpness for transverse defects of approximate Hilbert isometries

## Finding
For \(\varepsilon>0\) and \(r\geq0\), let \(\mathcal E_\varepsilon(r)\) be the supremum of \(\|(I-P_f)f(x)\|\) over all standard \(\varepsilon\)-isometries \(f:H\to K\) between real Hilbert spaces, all \(x\in H\) with \(\|x\|=r\), and \(P_f\) the orthogonal projection onto the range of the canonical asymptotic isometry \(U_f(x)=\lim_{n\to\infty}2^{-n}f(2^n x)\). The exact universal pointwise envelope is
\[
\boxed{\mathcal E_\varepsilon(r)=\begin{cases}0,&r=0,\\r+\varepsilon,&0<r\leq2\varepsilon,\\\sqrt{6\varepsilon r-3\varepsilon^2},&r\geq2\varepsilon.\end{cases}}
\]
Both positive-radius branches are attained, with \(H=\mathbb R\) and \(K=\mathbb R^2\). The new assertion is attainment at **every** \(0<r<2\varepsilon\), the range left open in Remark 2.1 of Turnšek (2026). The already-published upper estimate and the large-radius attainment are credited to Turnšek. The expression has matching values at \(r=2\varepsilon\); its right limit at zero is \(\varepsilon\), although its value at zero is zero.

## Assumptions and scope
A **standard \(\varepsilon\)-isometry** is a map \(f:H\to K\) with \(f(0)=0\) and
\[
\bigl|\|f(x)-f(y)\|-\|x-y\|\bigr|\leq\varepsilon\qquad(x,y\in H).
\]
Neither continuity nor surjectivity is assumed a priori. The canonical linear isometry \(U_f\) and the projection \(P_f\) are as in Šemrl (2025), Theorem 1.3; Turnšek (2026), Theorem 1.1. The supremum is taken separately for each prescribed radius; one map need not simultaneously maximize all radii. All spaces and scalars are real. The source is nonzero whenever \(r>0\), and the target must have a transverse direction to attain the positive envelope.

## Proof
**1. Universal upper bound.** For each standard \(\varepsilon\)-isometry, the origin condition gives \(\|f(x)\|\leq r+\varepsilon\). The established longitudinal bound \(\|P_f f(x)-U_f x\|\leq2\varepsilon\) therefore gives, whenever \(r\geq2\varepsilon\),
\[
\begin{aligned}
\|(I-P_f)f(x)\|^2
&=\|f(x)\|^2-\|P_f f(x)\|^2\\
&\leq(r+\varepsilon)^2-(r-2\varepsilon)^2\\
&=6\varepsilon r-3\varepsilon^2.
\end{aligned}
\]
At smaller radii the direct bound is \(r+\varepsilon\). At zero the transverse component vanishes because \(f(0)=0\). These upper estimates are Theorem 1.2 of Turnšek (2026), not new here.

**2. Explicit short-radius extremizer.** Scale to \(\varepsilon=1\) and fix any \(0<r\leq2\). Set
\[
a=(r-1)_+,\qquad h=r+1,\qquad k=h/r.
\]
Define \(F_r:\mathbb R\to\mathbb R^2\) on three consecutive intervals by
\[
F_r(t)=\begin{cases}
\bigl(t,\sqrt r-\sqrt{r-2at}\bigr),&t\leq0\quad(\mathrm N),\\
(0,kt),&0\leq t\leq r\quad(\mathrm A),\\
\bigl(t-r,\sqrt{h^2+2(t-r)}\bigr),&t\geq r\quad(\mathrm C).
\end{cases}
\]
The formulas agree at both junctions. In particular \(F_r(0)=0\), \(F_r(r)=(0,h)\). Also \(F_r(t)/t\to(1,0)\) as \(t\to\pm\infty\), so, once the approximate-isometry condition is proved, the canonical asymptotic isometry will be \(U(t)=(t,0)\), and its transverse component at \(r\) will have norm exactly \(h=r+1\).

**3. Complete verification of the additive distortion.** Fix \(s<t\), write \(D=t-s>0\), and prove
\[
D-1\leq\|F_r(t)-F_r(s)\|\leq D+1.
\]
The lower inequality is automatic for \(D\leq1\). We check every possible interval pair.

**(N,N) and (C,C).** The horizontal increment is \(D\). The square of the vertical increment is at most \(2aD\leq2D\) on (N), and at most \(2D\) on (C), using \(|\sqrt u-\sqrt v|^2\leq|u-v|\). Therefore the norm lies between \(D\) and \(\sqrt{D^2+2D}\leq D+1\).

**(A,A).** The increment norm is \(kD=D+D/r\). Since the two points lie in \([0,r]\), we have \(D\leq r\), so this is in \([D,D+1]\).

**(N,C).** Write \(s=-u\), \(t=r+v\) with \(u,v\geq0\), and define
\[
b=\sqrt{r+2au}-\sqrt r\geq0,\qquad H=\sqrt{h^2+2v}\geq h.
\]
Then \(D=r+u+v\) and the increment is \((u+v,H+b)\). If \(r\leq1\), then \(a=b=0\); the lower bound follows from \(\|\Delta\|\geq u+v\geq D-1\), and the upper bound from \(H^2=h^2+2v\leq(h+u+v)^2\), as \(h\geq1\).

Suppose now \(1\leq r\leq2\), so \(a=r-1\). With \(b^2=2au-2\sqrt r\,b\), direct expansion gives
\[
\|\Delta\|^2-(D-1)^2
=4r+2(2-r)v+2(H-\sqrt r)b\geq0.
\]
The upper bound reduces exactly to
\[
(H-\sqrt r)b\leq2u+rv.
\]
Indeed, \(b\leq au/\sqrt r\), \(b\leq\sqrt{2au}\), and \(H-h\leq\sqrt{2v}\). The elementary arithmetic-geometric mean inequality thus yields
\[
\begin{aligned}
(H-\sqrt r)b
&\leq(h-\sqrt r)\frac{au}{\sqrt r}+2\sqrt{auv}\\
&\leq a\left(\sqrt r+\frac1{\sqrt r}-1+\frac1r\right)u+rv.
\end{aligned}
\]
The parenthesis is decreasing on \([1,2]\): its derivative is \(((r-1)\sqrt r-2)/(2r^2)<0\), and its value at \(1\) is \(2\). Since \(a\leq1\), the required upper inequality follows.

**(N,A).** Fix \(s=-u\leq0\) and vary \(t=w\in[0,r]\). The function \(w\mapsto\|F_r(w)-F_r(-u)\|-(u+w)\) is convex (norm of an affine function minus an affine function). Its maximum occurs at \(w=0\) or \(w=r\), already covered by (N,N) and (N,C), proving the upper inequality. For the lower inequality, the increment is \((u,kw+b)\). If \(w\leq1\), its norm is at least \(u\geq D-1\). If \(w>1\), necessarily \(1<r\leq2\), \(a=r-1\), and expansion gives
\[
\|\Delta\|^2-(D-1)^2
=2u(r-w)+(kw)^2-(w-1)^2+2(kw-\sqrt r)b\geq0.
\]
All terms are nonnegative: \(u\geq0\), \(w\leq r\), and \(k\geq\sqrt r\) for \(1\leq r\leq2\).

**(A,C).** Write \(s=r-u\in[0,r]\), \(t=r+v\), \(u\in[0,r]\), \(v\geq0\), and \(B=\sqrt{h^2+2v}-h\geq0\). The increment is \((v,B+ku)\), and \(D=u+v\). Its norm minus \(D\), with \(v\) held fixed, is convex in \(u\in[0,r]\). At the endpoints the (C,C) and (N,C) bounds apply, establishing the upper estimate. The lower estimate follows from \(\|\Delta\|\geq v\geq D-1\) if \(u\leq1\). Otherwise \(1<u\leq r\leq2\). Since \(B^2=2v-2hB\), \(B\leq v/h\), and \(ku-h\leq0\),
\[
\begin{aligned}
\|\Delta\|^2-(D-1)^2
&=2v(2-u)+(ku)^2-(u-1)^2+2(ku-h)B\\
&\geq2v\left(1-u+\frac ur\right)+(ku)^2-(u-1)^2\geq0,
\end{aligned}
\]
because \(1-u+u/r\geq2-r\geq0\) and \(ku>u-1\).

These six interval-pair cases exhaust all \(s<t\), so \(F_r\) is a standard \(1\)-isometry. Its two tails have horizontal slope \(1\) and vertical growth only of order \(\sqrt{|t|}\). Thus \(U(t)=(t,0)\) and \(\|(I-P)F_r(r)\|=r+1\), attaining the short-radius upper bound.

**4. Scaling and long radii.** For each \(\varepsilon>0\), \(0<r\leq2\varepsilon\), define \(f(t)=\varepsilon F_{r/\varepsilon}(t/\varepsilon)\). This is a standard \(\varepsilon\)-isometry with \(\|(I-P)f(r)\|=r+\varepsilon\). For \(r\geq2\varepsilon\), Turnšek (2026), Theorem 1.3, supplies an attained example with transverse norm \(\sqrt{6\varepsilon r-3\varepsilon^2}\). Together with step 1 and the origin case, this proves the exact envelope for every radius.

## Verification
The six interval pairs (N,N), (N,A), (N,C), (A,A), (A,C), (C,C) have been verified algebraically above, including the junctions and parameter endpoints \(r=1,2\). The right-limit phenomenon at zero does not assert a single map with nonzero error at the origin. The supplementary standalone script `CHECK.py` samples 400,000 pairs over 80 short radii, including tiny and near-threshold values, and checks the normalized additive distortion, origin, extremal point and asymptotic direction. Run `python CHECK.py` with Python 3 and NumPy. Finite sampling is not a substitute for the proof.

## Relationship to prior work
Šemrl (2025) established the existence of the canonical Hilbert-space asymptotic isometry and the bound on its longitudinal component. Turnšek (2026), Theorem 1.2, proved the two-branch upper bound, and Theorem 1.3 constructed exact extremizers for radii at least \(2\varepsilon\). Turnšek's Remark 2.1 explicitly left open whether the first branch is attained for \(0<r<2\varepsilon\). The new construction closes precisely that gap, without claiming the previously published upper or large-radius results as new. The classical Šemrl–Väisälä theory concerns stability of nonsurjective nearisometries rather than this pointwise transverse extremal question.

## Limitations
The envelope is a supremum over *all* admissible maps separately at each radius, not a radius-uniform extremizer. The construction is one-dimensional into two-dimensional real Euclidean space; there is no asserted classification or uniqueness of extremizers. It is about the orthogonal component relative to the canonical asymptotic isometry, not the full nonlinear approximation error, and makes no claim for complex spaces with different hypotheses. The result uses Turnšek's prior theorems for the universal upper and long-radius attainment. No independent mathematical audit has been performed; equivalence with unindexed earlier literature remains possible.

## References
1. A. Turnšek, *The sharp constant in a theorem of Šemrl on approximate isometries of Hilbert spaces* (2026), arXiv:2611.24942v1, Theorems 1.1–1.3 and Remark 2.1. https://arxiv.org/html/2611.24942v1 (first confirmed public listing 2026-11-20).
2. P. Šemrl, *Approximate isometries of Hilbert spaces* (2025), arXiv:2501.17672v1. https://arxiv.org/abs/2501.17672 .
3. P. Šemrl and J. Väisälä, *Nonsurjective nearisometries of Banach spaces*, J. Funct. Anal. 198 (2003), 268–278, https://doi.org/10.1016/S0022-1236(02)00049-6 .
