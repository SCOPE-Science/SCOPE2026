# A postcritical Cantor repeller with explicit escape and fractal asymptotics in a rational logistic map

## Finding
For the real interval map
\[
K_\mu(x)=\frac{\mu x(1-x)}{1+x},\qquad x\in I=[0,1],
\]
let a point *survive through time* \(n\) if all its first \(n\) iterates remain in \(I\). Define
\[
S_n=\{x\in I:K_\mu^j(x)\in I\ (0\le j\le n)\},\quad
C_\mu=\bigcap_{n\ge0}S_n,\quad A_n=\operatorname{Leb}(S_n).
\]
Put \(D_\mu=\mu^2-6\mu+1\), and let \(\mu_h\) be the **unique** real root greater than \(3+2\sqrt2\) of
\[
\mu^3-7\mu^2+5\mu-1=0
\qquad(\mu_h\approx6.2222625231203986).
\]
For **every real \(\mu>\mu_h\)** the following hold simultaneously:

1. The set \(C_\mu\) is a compact, zero-Lebesgue-measure, nowhere dense Cantor repeller on which \(K_\mu\) is topologically conjugate to the full one-sided two-symbol shift. Its topological entropy is \(\log 2\), and among the orbits which remain in \(I\), exactly \(2^n\) points satisfy \(K_\mu^n(x)=x\); all are hyperbolically repelling, for every integer \(n\ge1\).
2. The exact Lebesgue escape exponent \(\gamma_\mu=-\lim_{n\to\infty}\log A_n/n\) exists and is strictly positive. With
\[
L_-(\mu)=\frac{1}{\mu},\quad L_+(\mu)=\frac2\mu,
\qquad U_\pm(\mu)=\frac{(3\mu-1)/\sqrt{D_\mu}\pm1}{2\mu},
\]
its finite-horizon survival bounds and escape-rate bounds are
\[
\left(\frac3\mu\right)^n\le A_n\le
\left(\frac{3\mu-1}{\mu\sqrt{D_\mu}}\right)^n,
\qquad
\log\frac{\mu\sqrt{D_\mu}}{3\mu-1}\le\gamma_\mu\le\log\frac\mu3.
\]
In particular \(\gamma_\mu=\log(\mu/3)+O(\mu^{-1})\) as \(\mu\to\infty\).
3. The Hausdorff dimension \(d_\mu=\dim_H C_\mu\) lies strictly between zero and one. Let \(s_\mu,t_\mu\) be the unique positive solutions of
\[
L_-^{s_\mu}+L_+^{s_\mu}=1,\qquad
U_-^{t_\mu}+U_+^{t_\mu}=1.
\]
Then \(s_\mu\le d_\mu\le\min\{1,t_\mu\}\), and, with \(L=\log\mu\),
\[
\boxed{d_\mu=\frac{\log2}{L}
+\frac{(\log2)^2}{2L^2}
+\frac{(\log2)^3/4+(\log2)^4/8}{L^3}
+O(L^{-4})}. 
\]
The algebraic threshold \(\mu_h\) is sharp **only for uniform one-step expansion on the two allowed branches**; no claim is made that hyperbolicity of the survivor first begins there.

## Assumptions and scope
All statements are for exact real arithmetic, for the explicitly displayed rational map with the absorbing observation interval \(I=[0,1]\), and for \(\mu>\mu_h\). The first exit from \(I\) ends a trajectory's survival test; later returns are not counted. \(\operatorname{Leb}\) is ordinary one-dimensional Lebesgue measure, and the finite-time bounds use \(A_0=1\). The source map was introduced with a nonnegative real parameter in a study of trajectories retained in \(I\); here we specifically analyze the natural overcritical region in which its maximum exceeds one. The parameter \(\mu\) is fixed before taking the limit in \(n\), except in the explicit subsequent \(\mu\to\infty\) asymptotic statements.

## Proof
**1. Turning point and inverse branches.** Elementary differentiation gives
\[
K_\mu'(x)=\mu\frac{1-2x-x^2}{(1+x)^2}.
\]
Its sole interior critical point is \(c=\sqrt2-1\), with \(K_\mu(c)=\mu(3-2\sqrt2)\). Thus the level-one hole first opens at \(\mu_c=3+2\sqrt2\). For every \(\mu>\mu_c\), solving \(K_\mu(x)=y\), \(0\le y\le1\), gives the two smooth inverse branches
\[
g_\pm(y)=\frac{\mu-y\pm\sqrt{\mu^2-6\mu y+y^2}}{2\mu}.
\]
Here \(g_-(I)=[0,a]\), \(g_+(I)=[b,1]\), where
\[
a=\frac{\mu-1-\sqrt{D_\mu}}{2\mu},\quad
b=\frac{\mu-1+\sqrt{D_\mu}}{2\mu},\quad
b-a=\frac{\sqrt{D_\mu}}{\mu}>0.
\]
They are separated by the open hole \((a,b)\), exactly the set within \(I\) mapped above one.

**2. Exact inverse derivative bounds and sharp one-step threshold.** Define \(Q(y)=(3\mu-y)/\sqrt{\mu^2-6\mu y+y^2}\). Direct differentiation gives
\[
Q'(y)=\frac{8\mu^2}{(\mu^2-6\mu y+y^2)^{3/2}}>0,
\quad
g_-'(y)=\frac{Q(y)-1}{2\mu},\quad
|g_+'(y)|=\frac{Q(y)+1}{2\mu}.
\]
At \(y=0\), \(Q=3\), so the two exact minima are \(L_-=1/\mu\) and \(L_+=2/\mu\). At \(y=1\), the maxima are \(U_-\) and \(U_+\) stated above. Both branches are strictly contracting on \(I\) precisely when \(U_+<1\). In the domain \(\mu>\mu_c\), squaring the positive sides of \((3\mu-1)<(2\mu-1)\sqrt{D_\mu}\) and factoring yields
\[
(2\mu-1)^2D_\mu-(3\mu-1)^2
=4\mu(\mu^3-7\mu^2+5\mu-1).
\]
The cubic is strictly increasing throughout \((\mu_c,\infty)\), negative at \(\mu_c\), and tends to infinity. Therefore \(\mu_h\) is unique and \(U_+<1\) exactly when \(\mu>\mu_h\). Put \(q=U_+<1\).

**3. Complete symbolic dynamics.** The disjoint interval maps \(g_\pm:I\to I\) are strict contractions, with images separated by a positive gap. For a word \(w=i_1\cdots i_n\), write \(g_w=g_{i_1}\circ\cdots\circ g_{i_n}\), and \(I_w=g_w(I)\). Inductively,
\[
S_n=\bigcup_{w\in\{-,+\}^n}I_w,
\]
with exactly \(2^n\) pairwise disjoint nondegenerate component intervals, each of diameter at most \(q^n\). Nested cylinders hence assign every infinite binary word a unique surviving point, continuously and injectively; compactness makes this coding a homeomorphism. Applying \(K_\mu\) deletes the first symbol. Since both branches are strict contractions, each finite word \(w\) determines exactly one point fixed by \(g_w\), hence fixed by \(K_\mu^n\), while every fixed point of \(K_\mu^n\) **whose intermediate orbit remains in \(I\)** lies in one such cylinder. No claim is made about periodic orbits that leave and later reenter \(I\). At a periodic point, \(|(K_\mu^n)'|\ge q^{-n}>1\). The shift coding proves the stated entropy and Cantor/repeller properties. The Lebesgue-null and dimension claims are established below.

**4. Escape-rate existence and bounds.** Differentiating the inverse formula twice gives
\[
|g_\pm''(y)|=\frac{4\mu}{(\mu^2-6\mu y+y^2)^{3/2}},
\quad |g_\pm'(y)|\ge\frac1\mu.
\]
Thus each \(\log |g_i'|\) is Lipschitz with constant at most \(T=4\mu^2/D_\mu^{3/2}\). Summing along contracting suffixes shows that every cylinder map \(g_w\) has uniform derivative distortion
\[
\frac{\sup_I |g_w'|}{\inf_I |g_w'|}\le
C:=\exp\!\left(\frac{T}{1-q}\right)<\infty.
\]
For every measurable \(E\subseteq I\), it follows that
\[
C^{-1}|E|\,|I_w|\le |g_w(E)|\le C|E|\,|I_w|.
\]
Taking \(E=S_m\) and summing over words of length \(n\) yields
\[
C^{-1}A_nA_m\le A_{n+m}\le CA_nA_m.
\]
Fekete's subadditive lemma applied to \(\log(CA_n)\) proves the existence of \(\lim_n\log A_n/n\). If \(\delta=b-a>0\), the same distortion inequality applied to the hole \(H=(a,b)\) gives
\[
A_{n+1}=\sum_{|w|=n}\bigl(|I_w|-|g_w(H)|\bigr)
\le (1-C^{-1}\delta)A_n.
\]
Consequently \(A_n\to0\) exponentially and \(\gamma_\mu\ge-\log(1-C^{-1}\delta)>0\), proving null Lebesgue measure. Finally, the sharp derivative bounds from Step 2 imply
\[
(L_-+L_+)A_n\le A_{n+1}\le(U_-+U_+)A_n;
\]
iteration proves the finite-horizon inequalities and, after taking logarithms, the rate inequalities. Since \(D_\mu=\mu^2(1-6/\mu+1/\mu^2)\), their gap is \(O(\mu^{-1})\) as \(\mu\to\infty\).

**5. Dimension bounds and large-gain expansion.** For every word \(w\),
\[
\prod_{j=1}^{|w|}L_{i_j}\le |I_w|\le
\prod_{j=1}^{|w|}U_{i_j}.
\]
The upper inequality gives a covering by \(2^n\) intervals of diameter tending to zero whose total \(t_\mu\)-power length is at most \((U_-^{t_\mu}+U_+^{t_\mu})^n=1\), so \(d_\mu\le t_\mu\). For the lower bound, place the Bernoulli probability \(p_i=L_i^{s_\mu}\) on symbol \(i\). The coding image measure assigns any cylinder mass \(\prod_i p_i\le |I_w|^{s_\mu}\). By the uniform distortion bound, child/parent cylinder lengths are bounded below by \(C^{-1}\min(L_-,L_+)\), independent of the word. For any sufficiently small scale \(r\), the maximal prefix cylinders with diameters at most \(r\) therefore have diameters between \(C^{-1}L_-r\) and \(r\), are disjoint, and cover \(C_\mu\); an interval of length \(2r\) meets only boundedly many of these (each disjoint cylinder has comparable length). The image measure of that interval is at most \(M_\mu r^{s_\mu}\). The mass-distribution principle gives \(d_\mu\ge s_\mu\). The same exponential volume-loss estimate from Step 4 gives \(d_\mu<1\) directly. Set \(\theta=1-C^{-1}\delta<1\). Every cylinder satisfies \(|I_w|\ge\mu^{-n}\), so for \(0<t<1\), \(\sum_{|w|=n}|I_w|^t\le\mu^{n(1-t)}A_n\le(\mu^{1-t}\theta)^n\). Choose \(t<1\) sufficiently close to one that \(\mu^{1-t}\theta<1\); then the sum of \(t\)-powers of the level-\(n\) cylinder diameters tends to zero and \(d_\mu\le t<1\). Since \(s_\mu>0\), this proves \(0<d_\mu<1\).

As \(\mu\to\infty\), the exact extrema satisfy \(U_-=\mu^{-1}(1+O(\mu^{-1}))\) and \(U_+=2\mu^{-1}(1+O(\mu^{-1}))\). Implicit comparison of the two dimension-root equations, whose derivatives in the exponent are of order \(\log\mu\), gives
\[
0\le t_\mu-s_\mu=O\!\left(\frac1{\mu(\log\mu)^2}\right).
\]
Writing \(B=\log2\), \(L=\log\mu\), the defining equation for \(s_\mu\) is
\[
s_\mu L=\log(1+e^{B s_\mu})
=B+\frac{B s_\mu}{2}+\frac{B^2s_\mu^2}{8}+O(s_\mu^4).
\]
Solving successively for the coefficients of \(L^{-1},L^{-2},L^{-3}\) gives
\[
s_\mu=\frac{B}{L}+\frac{B^2}{2L^2}
+\frac{B^3/4+B^4/8}{L^3}+O(L^{-4}).
\]
The dimension bracket and exponentially small difference between \(t_\mu\) and \(s_\mu\) transfer this expansion to \(d_\mu\), completing the proof.

## Verification
The standalone `verify.py` (standard-library Python) recomputes the algebraic uniform-expansion threshold, checks 500 inverse identities with 85-digit decimal arithmetic across five gains, evaluates all derivative bounds, and tests the dimension-root brackets and asymptotic approximation. It independently verifies the quadratic discriminant identity with exact rational arithmetic. Run `python3 verify.py` from the extracted package directory. **Finite computations are diagnostic; the infinite results rely on the preceding proof.**

## Relationship to prior work
Kumar, Alzabut, Kumari, Rani and Chugh (2022) introduce this precise rational map and study fixed points, bifurcations, Lyapunov behavior and related numerical dynamics up to the interval-preserving upper gain. Conejero, Lizama and Quijada (2025) analyze a unifying interpolation with this map as one endpoint; its results emphasize fixed points and numerical bifurcation ranges. The standard inverse-branch coding, bounded-distortion, subadditive and mass-distribution principles used here are classical. The **map-specific** statements assessed here concern the sharp algebraic one-step hyperbolicity boundary, explicit postcritical survival/escape inequalities, and the three-term large-gain dimension asymptotic. They are not implied by the two cited analyses of the interval-preserving regime. A direct claim that generic two-branch Cantor dynamics is novel is not made.

## Limitations
The theorem does not classify \(\mu_c<\mu\le\mu_h\), despite possible repelling survivors there, nor does it give a closed formula for \(\gamma_\mu\) or \(d_\mu\) at fixed finite gain. The word "sharp" applies to a sufficient uniform-one-step expansion property, not to the onset of chaos for the full dynamical system. Survival is relative to the chosen observation interval: escaped real trajectories may remain mathematically defined outside it. Existing general Cantor-repeller theory supplies major proof ingredients; the exact quantitative map-specific refinements require separate priority assessment. No independent verification or exhaustive global bibliography has been performed.

## References
1. A. Kumar, J. Alzabut, S. Kumari, M. Rani and R. Chugh, *Dynamical properties of a novel one dimensional chaotic map*, Mathematical Biosciences and Engineering **19** (2022), 2489–2505, published January 7, 2022; DOI: https://doi.org/10.3934/mbe.2022115 ; full text: https://www.aimspress.com/aimspress-data/mbe/2022/3/PDF/mbe-19-03-115.pdf .
2. J. A. Conejero, C. Lizama and D. Quijada, *Dynamical Properties for a Unified Class of One-Dimensional Discrete Maps*, Mathematics **13** (2025), 518, DOI: https://doi.org/10.3390/math13030518 ; full HTML: https://www.mdpi.com/2227-7390/13/3/518 .
3. Standard mathematical tools: the contraction mapping theorem, Fekete's subadditive lemma, the mass-distribution principle and elementary bounded-distortion estimates for one-dimensional conformal iterated function systems. No claim of priority for these tools.
