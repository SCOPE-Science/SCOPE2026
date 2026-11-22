# Logarithmic inverse-transfer mass in a planar cosine-memory map

## Finding

For the real planar cosine-memory map introduced by Zhang, Liu, Wei, Jiang, Lyu and Bi,
\[
 F(x,y)=\bigl(a+bc\,x\cos(dy),\;y+ex\bigr),
 \qquad a,b,c,d,e\in\mathbb R,\quad bcde\ne0,
\]
put \(B=bc\) and \(\omega=de\). Fix any target \((U,V)\in\mathbb R^2\). Let \(N_R(U,V)\) count the distinct preimages with \(|x|\le R\), and define the finite regular-branch transfer weight
\[
 W_R(U,V)=\sum_{\substack{F(x,y)=(U,V),\ |x|\le R\\\det DF(x,y)\ne0}}
 \frac1{|\det DF(x,y)|}.
\]
For every such map and every target, the full inverse fibre is countably infinite, has at most finitely many singular points, and satisfies the exact asymptotic laws
\[
 \boxed{N_R(U,V)=\frac{2|de|}{\pi}R+O_{F,U,V}(1)},
 \qquad
 \boxed{W_R(U,V)=\frac{2}{\pi|bc|}\log R+O_{F,U,V}(1)}
 \quad(R\to\infty).
\]

The second law has a global, measure-theoretic counterpart. If \(E\subset\mathbb R^2\) is any bounded Lebesgue-measurable target set and \(|E|\) denotes its planar Lebesgue area, then
\[
 \boxed{\left|F^{-1}(E)\cap\{|x|\le R\}\right|
 =\frac{2|E|}{\pi|bc|}\log R+O_{F,E}(1).}
\]
In particular, the pushforward of full planar Lebesgue measure under \(F\) gives measure zero to every null target set and measure infinity to every target set of positive area. This pushforward is absolutely continuous (in the extended-valued sense) but is **not sigma-finite**. Remarkably, the sharp logarithmic transfer-mass coefficient depends on the cosine amplitude \(|bc|\) but **not** on the nonzero memory or frequency coefficients \(d,e\); their product instead controls the linear inverse-sheet density.

## Assumptions and scope

All source and target coordinates are real and unrestricted; the second coordinate is not taken modulo a period. The five parameters are fixed and finite, with \(bcde\ne0\). The constant \(a\) is unrestricted (and may be nonzero, as in the published fixed-point-free setting). The leading claims are for \(R\to\infty\), and the constants in pointwise remainders may depend on the target. The area law is for a fixed bounded measurable target set, with an \(O(1)\) remainder that may depend on a bounding rectangle. The quantity \(W_R\) excludes points with zero determinant, which can occur at finitely many small inverse branches and require separate multiplicity conventions; this exclusion does not alter the sharp logarithmic term.

For \(R\ge0\), \(F^{-1}(E)\cap\{|x|\le R\}\) is measurable in the Lebesgue completion (see the proof). The notation \(|\cdot|\) for sets means planar area, not a probability. No invariant probability, attractor, recurrence, physical boundedness, or cryptographic property is asserted.

## Proof

**1. Scalar reduction and an explicit inverse lattice.** Set
\[
 q=\frac{U-a}{B},\qquad \theta=dV,\qquad \omega=de\ne0.
\]
The second output equation forces \(y=V-ex\); substitution into the first gives the single analytic equation
\[
 g_{\theta,\omega}(x)=x\cos(\theta-\omega x)=q.\tag{1}
\]
The cosine zeros in its phase form the two-sided arithmetic grid
\[
 z_k=\frac{\theta-(k+\tfrac12)\pi}{\omega},\qquad k\in\mathbb Z,
 \qquad |z_{k+1}-z_k|=\frac\pi{|\omega|}.
\]
In the phase interval \(|\omega(x-z_k)|\le\pi/3\), one has \(|\sin(\theta-\omega x)|\ge1/2\). Since
\[
 g'(x)=\cos(\theta-\omega x)+\omega x\sin(\theta-\omega x),
\]
for all sufficiently large \(|z_k|\) the derivative has a fixed nonzero sign in this interval. At its opposite endpoints the values of \(g\) have opposite signs and magnitudes growing with \(|z_k|\), hence they bracket the fixed \(q\). There is therefore exactly one root \(x_k\) in each distant interval.

Every sufficiently large root is among these: equation (1) gives \(|\cos(\theta-\omega x)|=|q|/|x|\), which for \(|x|>2|q|\) forces its phase to be within \(\pi/6\) of a cosine zero. Thus no distant roots are omitted. Each root is regular for the reduced equation. Expanding around a center gives
\[
 x_k=z_k+\frac{(-1)^k q}{\omega z_k}+O_{F,U,V}(|z_k|^{-3}),
 \qquad g'(x_k)=(-1)^k\omega z_k+O_{F,U,V}(|z_k|^{-1}).\tag{2}
\]
Indeed, \(\cos((k+\tfrac12)\pi-\omega\delta)=(-1)^k\sin(\omega\delta)\), and equation (1) first yields \(\delta=O(|z_k|^{-1})\); the cubic sine Taylor remainder and the correction from \(x_k=z_k+\delta\) then give (2). The reduced function is real analytic and not identically constant, so its roots have no finite accumulation point, establishing countability and finiteness of any remaining central roots.

**2. Number and Jacobian weight of inverse branches.** The arithmetic grid and (2) show that the number of roots satisfying \(|x_k|\le R\) differs from \(2|\omega|R/\pi\) by at most a constant; finitely many central roots change only that constant. The Jacobian is
\[
 DF=\begin{pmatrix}B\cos(dy)&-Bd x\sin(dy)\\ e&1\end{pmatrix},
 \qquad \det DF=B\bigl(\cos(dy)+\omega x\sin(dy)\bigr).
\]
At an inverse branch \(y=V-ex\), this determinant is exactly \(B g'(x)\). The second relation in (2) gives, uniformly over distant centers,
\[
 \frac1{|\det DF(x_k,V-ex_k)|}
 =\frac1{|B\omega|\,|z_k|}+O_{F,U,V}(|z_k|^{-3}).\tag{3}
\]
The error is summable over all \(k\). A two-sided harmonic sum on a lattice of spacing \(\pi/|\omega|\) satisfies
\[
 \sum_{\substack{|z_k|\le R\\|z_k|\ge K}}\frac1{|z_k|}
 =\frac{2|\omega|}{\pi}\log R+O_{K,\theta,\omega}(1).
\]
The root-versus-center cutoff discrepancy contributes only \(O(1)\) (indeed \(O(R^{-1})\) in the weighted sum), and finitely many central regular roots contribute a finite target-dependent amount. This proves both pointwise asymptotic formulas. Any singular preimage lies among the finitely many central roots, because all large roots have nonzero reduced derivative.

**3. Uniform far-branch estimates and the area law.** Let \(E\) lie in a fixed bounded rectangle \([U_-,U_+]\times[V_-,V_+]\). The numbers \(q\) and \(\theta\) from Step 1 range over compact intervals. Hence one can choose the large-center threshold \(K\) independently of \((U,V)\in E\), and all the monotonicity, expansion and reciprocal-Jacobian bounds (2)–(3) hold uniformly there. The two-sided shifted harmonic sum then gives the **uniform far-branch** estimate
\[
 \sum_{\substack{F(x,y)=(U,V),\ K<|x|\le R}}
 \frac1{|\det DF(x,y)|}
 =\frac2{\pi|B|}\log R+O_{F,K,[U_-,U_+]\times[V_-,V_+]}(1),\tag{4}
\]
where every branch in the sum is regular. This statement deliberately excludes the central roots: their reciprocal Jacobians need not remain uniformly bounded as a target approaches a fold.

On the source strip \(|x|\le K\), the shear change of coordinates \((x,y)\mapsto(x,V=y+ex)\) preserves area, so its preimage of \(E\) lies inside a rectangle of area at most \(2K(V_+-V_-)\); it contributes \(O_{F,E}(1)\). For \(K<|x|\le R\), ordinary change of variables on each smooth inverse branch (or the area formula) gives
\[
 \left|F^{-1}(E)\cap\{K<|x|\le R\}\right|
 =\int_E\sum_{\substack{F(x,y)=(U,V),\K<|x|\le R}}
 \frac1{|\det DF(x,y)|}\,dU\,dV.
\]
Critical target values have area zero and do not affect this equality. Integrating the *uniform* estimate (4) and adding the bounded strip proves the claimed area law, including for measurable \(E\) with irregular boundaries and for \(|E|=0\).

**4. Full-plane pushforward and sigma-finiteness.** The critical set \(\det DF=0\) has planar measure zero: for each fixed \(x\), the nontrivial trigonometric function \(\cos(dy)+\omega x\sin(dy)\) has a discrete zero set in \(y\); apply Fubini. Away from that set, the inverse function theorem gives a local smooth diffeomorphism; a countable cover of such charts proves that the full preimage of any Lebesgue-null target set is null. Thus \(F_*\mathrm{Leb}_2\) vanishes on target null sets. For a positive-area bounded measurable set, Step 3 forces its full preimage to have infinite area. An arbitrary positive-area measurable set contains a bounded positive-area subset, so its pushforward measure is also infinite. Were this pushforward sigma-finite, the plane would be a countable union of sets of finite pushforward measure, all of which must be null; this contradicts its positive area. This completes the proof.

## Verification

Run the standalone Python 3 standard-library file `verify.py` using `python verify.py`. It reconstructs thousands of distant real inverse branches for the exact illustrative parameters \((a,B,d,e)=(0.01,1.2,1,1)\) and target \((U,V)=(a+0.37B,0.2)\). The checker verifies forward residuals, the nonzero reduced Jacobian, inverse-sheet growth, and logarithmic *increment* predictions at increasing cutoffs. It prints `COSINE_MAP_INVERSE_TAIL_VERIFY_OK`. Finite samples cannot prove the asymptotic laws; the proofs are in Steps 1–4.

## Relationship to prior work

Zhang and collaborators introduced exactly this cosine-memory map and studied the absence of fixed points and numerical attractor/bifurcation patterns [1]. Those forward-dynamics results, including the translational symmetry in the memory coordinate, do not give a global inverse-fiber census, inverse-Jacobian sums or the non-sigma-finite image of planar volume. A publicly available same-map study gives a coefficient-uniform boundary for forward escape and short-period recurrence; these statements do not imply a weighted inverse-sheet law [4]. Ramadoss and collaborators developed general memristive-map constructions and studied fixed points and numerical dynamics [2,3], without an equivalent inverse-volume theorem in the inspected material. For a different cosine-flux Chialvo map, an indexed mathematical result gives linearly many inverse sheets [5], but it does not concern this map and does not imply the weighted harmonic law or sigma-finiteness conclusion. These are implication comparisons, not claims that absence of a matching title proves novelty.

## Limitations

The infinite inverse count, logarithmic weighted transfer and non-sigma-finite pushforward all rely on the **full real plane** and fixed nonzero \(bcde\). Bounded physical state windows contain only finitely many input branches, and setting \(bc=0\) or \(de=0\) can change the inverse geometry completely. The logarithmic coefficient is an asymptotic large-strip result, not a numerical-stability claim. No claim is made about the existence, stability or statistics of forward attractors. General publication priority remains provisional because unpublished or unindexed equivalent treatments may exist.

## References

1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, W.-P. Lyu and Q.-S. Bi, “Extremely hidden multi-stability in a class of two-dimensional maps with a cosine memristor,” *Chinese Physics B* **31** (2022), 100503. https://doi.org/10.1088/1674-1056/ac7294 . Earliest verified public accepted-manuscript date: 2022-05-24 (contemporaneous manuscript metadata). Full publisher HTML: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_10_100503.shtml .
2. J. Ramadoss, A. Ouannas, V. K. Tamba, G. Grassi, S. Momani and V.-T. Pham, “Constructing non-fixed-point maps with memristors,” *European Physical Journal Plus* **137** (2022), 211, https://doi.org/10.1140/epjp/s13360-022-02433-z .
3. J. Ramadoss, O. A. Almatroud, S. Momani, V.-T. Pham and V. P. Thoai, “Discrete Memristance and Nonlinear Term for Designing Memristive Maps,” *Symmetry* **14** (2022), 2110. https://doi.org/10.3390/sym14102110 .
4. “Sharp compact-recurrence boundary and ballistic drift corridor for a cosine-memory map,” publicly available research manuscript (2026); scientific full-text reference: https://api.github.com/repos/published-finding corpus/2026/git/blobs/053b8426d21ac3fb8b7cc0df34e018a7bd507a9b .
5. “Singular zero-to-infinite inverse-valence transition in a cosine-flux Chialvo map,” publicly available research manuscript (2026); scientific full-text reference: https://api.github.com/repos/published-finding corpus/2026/git/blobs/35150f9d343744c789c206e0c8e9828b5c90a57f .
