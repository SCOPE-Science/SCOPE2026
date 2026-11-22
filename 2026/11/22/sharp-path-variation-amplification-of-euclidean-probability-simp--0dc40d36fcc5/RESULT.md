# Sharp path-variation amplification of Euclidean probability-simplex projection

## Finding

For every integer \(n\ge2\), let \(P_n:\mathbb R^n\to\Delta_{n-1}\) be Euclidean nearest-point projection onto
\[
\Delta_{n-1}=\{z\in\mathbb R^n:z_i\ge0,\ \sum_{i=1}^n z_i=1\}.
\]
Equip real vectors with the **open-path total-variation seminorm**
\[
V_n(h)=\sum_{i=1}^{n-1}|h_{i+1}-h_i|.
\]
Then the exact, attained two-input Lipschitz modulus is
\[
\boxed{\sup_{V_n(x-y)>0}\frac{V_n(P_nx-P_ny)}{V_n(x-y)}=K_n:=
\begin{cases}
\dfrac n2-\dfrac1{n+1},& n\equiv1\pmod4,\\[4pt]
\dfrac n2,& n\not\equiv1\pmod4.
\end{cases}}
\]
(The exceptional case begins at \(n=5\), since \(n\ge2\).) Every value is attained by distinct input vectors with arbitrarily small difference. The first strictly expansive dimension is \(n=3\), where \(K_3=3/2\); asymptotically \(K_n\sim n/2\). In contrast, every individual data vector satisfies \(V_n(P_nx)\le V_n(x)\). The same modulus holds when the simplex total mass is any fixed positive number.

## Assumptions and scope

The coordinates are ordered along a finite path, with unit edge weights and **no edge joining the last coordinate to the first**. Projection uses the standard real Euclidean metric. The quotient excludes zero denominator; the projection is unchanged by addition of a constant vector, so zero-variation perturbations cause zero output difference. All statements concern pairs of real vectors and exact all-dimensional constants, not just Jacobian norms at one point.

## Proof

**1. Full-dimensional active regions and a single-step norm reduction.** The classical simplex-projection KKT representation [1,2] is
\[
(P_nx)_i=(x_i-\tau(x))_+,\qquad \sum_i(x_i-\tau(x))_+=1.
\]
On an open cell with nonempty positive-coordinate set \(F\subseteq\{1,\ldots,n\}\), write \(m=|F|\). The local linear part is
\[
(J_Fh)_i=\begin{cases}h_i-m^{-1}\sum_{k\in F}h_k,&i\in F,\\0,&i\notin F.\end{cases}
\]
Every nonempty \(F\) is realizable on an open cell: choose base data \(x_i=1/m\) for \(i\in F\) and \(x_i=-1\) otherwise, with threshold zero. Because the projection is continuous piecewise affine and each \(J_F\mathbf1=0\), its global two-input \(V_n\)-Lipschitz modulus is the maximum of the induced seminorms of the \(J_F\). This follows by integrating piecewise-constant derivatives along line segments, treating nongeneric segments by continuity; the reverse inequality follows from small perturbations inside a chosen open cell.

Let \(s^{(j)}_i=\mathbf1_{\{i>j\}}\) for \(1\le j<n\). Every \(h\) has the decomposition \(h=h_1\mathbf1+\sum_{j=1}^{n-1}(h_{j+1}-h_j)s^{(j)}\), and \(V_n(h)=\sum_j|h_{j+1}-h_j|\). Therefore
\[
\|J_F\|_{V_n\to V_n}=\max_{1\le j<n}V_n(J_Fs^{(j)}),
\]
with equality on one of the step vectors. This argument requires no assumption about the signs of individual data.

**2. Exact binary boundary count.** Fix \(F,j\). Set \(a=|F\cap\{1,\dots,j\}|\), \(b=|F\cap\{j+1,\dots,n\}|\), and suppose \(a,b>0\) (otherwise the image is zero). Let \(z_L=j-a\) and \(z_R=n-j-b\). The output \(J_Fs^{(j)}\) equals \(-b/m\) on the \(a\) selected left positions, \(+a/m\) on the \(b\) selected right positions, and zero elsewhere. Variation across the central edge splits exactly into the nonnegative contributions from its two sides. Let \(T_L\) count transitions of the left binary selector with an **artificial terminal zero at its right**, and \(T_R\) count transitions of the right binary selector with an **artificial initial zero at its left**. Then
\[
V_n(J_Fs^{(j)})=\frac{bT_L+aT_R}{m}.
\]
For a binary word with \(a\ge1\) ones and \(z\ge0\) zeros, including one such artificial zero, the maximum transition count is
\[
T(a,z)=\min\{2a,2z+1\}.
\]
Indeed each one borders at most two transitions, and each internal zero borders at most two, with at most one further transition at the unpinned exterior end. Alternating the symbols, with surplus symbols inserted inside constant runs, realizes the smaller bound. Thus, for any admissible \(a,b,z_L,z_R\) with \(n=a+b+z_L+z_R\), the exact maximum over those selector placements is
\[
G(a,b,z_L,z_R)=\frac{b\min(2a,2z_L+1)+a\min(2b,2z_R+1)}{a+b}.
\]
Both side words can be optimized independently, so there is no hidden compatibility constraint.

**3. Integer rigidity, including the exceptional residue class.** Write \(m=a+b\), \(d=b-a\), \(u=z_L-a\ge-a\), and \(v=z_R-b\ge-b\). Define \(\delta(k)=\max\{0,-2k-1\}\) for integral \(k\), and \(\Phi_c(k)=k/2+(c/m)\delta(k)\). Because \(n=2m+u+v\), an exact rearrangement gives the deficit identity
\[
\boxed{\frac n2-G(a,b,z_L,z_R)=\frac{d^2}{m}+\Phi_b(u)+\Phi_a(v).}
\]
The numerator \(2m(n/2-G)\) is always an integer.

If \(a=b\), each \(\Phi_{m/2}(k)\) is nonnegative: for \(k\ge0\) it is \(k/2\), and for \(k=-r\le-1\) it is \((r-1)/2\). Equality is possible precisely when \(u,v\in\{-1,0\}\), giving dimensions \(n=4a-2,4a-1,4a\), never \(n\equiv1\pmod4\).

Suppose, by symmetry, \(b>a\), so \(d\ge1\). The function \(\Phi_b(u)\) has unique integer minimum zero at \(u=0\), while for \(v=-r\) with \(1\le r\le b\),
\[
\Phi_a(-r)=r\left(\frac{2a}{m}-\frac12\right)-\frac a m.
\]
When \(b\le3a\), this is minimized at \(r=1\), so
\[
2m\left(\frac n2-G\right)\ge d(2d-1)\ge1.
\]
The integer on the left can equal one **only** when \(d=1\), \(u=0\), and \(v=-1\), giving \(n=2m-1=4a+1\). When \(b>3a\), the minimum occurs at \(r=b\) instead and
\[
2m\left(\frac n2-G\right)\ge b^2-ab+2a(a-1)>1.
\]
The case \(a>b\) is symmetric. Hence \(G\le n/2\) universally. Whenever \(n\equiv1\pmod4\), equality is impossible; if the positive integer \(2m(n/2-G)\) is at least two, then \(n/2-G\ge1/m\ge1/n>1/(n+1)\). In the sole remaining integer-one case, \(n=2m-1\) and the deficit equals \(1/(2m)=1/(n+1)\). Thus \(G\le n/2-1/(n+1)\) in that residue class.

**4. Exact attainability.** For \(n=4q\), choose \(a=b=q\), \(z_L=a\), \(z_R=b\). For \(n=4q+1\) (\(q\ge1\)), choose \(a=q\), \(b=q+1\), \(z_L=a\), \(z_R=b-1\). For \(n=4q+2\), choose \(a=b=q+1\), \(z_L=a-1\), \(z_R=b-1\). For \(n=4q+3\), choose \(a=b=q+1\), \(z_L=a-1\), \(z_R=b\). In each case use the alternating left and right binary selectors attaining the transition maxima; the preceding formula gives \(K_n\) exactly. Let \(F\) be their selected positions, let \(x_i=1/m\) on \(F\) and \(-1\) outside, and set \(y=x+\varepsilon s^{(j)}\), with \(\varepsilon=1/(4m)\). Both inputs lie in the same strict active-set cell, and
\[
P_ny-P_nx=\varepsilon J_Fs^{(j)},\qquad V_n(y-x)=\varepsilon,
\]
so the sharp quotient is genuinely attained. Finally \(P_nx\) is scalar threshold-and-clipping applied coordinatewise to \(x\); clipping is 1-Lipschitz, whence \(V_n(P_nx)\le V_n(x)\). Scaling data and simplex mass proves the positive-mass extension.

## Verification

Run `python3 checker.py` using Python's standard library. The checker reconstructs all \(J_F\) and every step test through dimension eleven, enumerates the exact binary transition lemma, evaluates the three-variable integer optimization through dimension 120, tests 1500 random rational nonlinear input pairs, and verifies strict-cell attaining witnesses using an independently implemented simplex threshold projector. The printed checks are diagnostic finite tests; the all-dimensional assertion is proved analytically above, including the integer rigidity step.

## Relationship to prior work

Classical Euclidean projection onto the simplex, its KKT threshold, and linear active-face formulas are established [1,2]; they are used, not claimed new. A closely related published theorem [3] gives the **cyclic** two-input variation modulus for the same map, with a periodic edge joining first to last coordinates and a different interval-cut geometry. Its sharp constant grows as \(n/4\), while the present open-path constant grows as \(n/2\); the cyclic theorem does not state or imply the exact open-path modulus, its first expansive dimension, or its unique exceptional residue-class deficit. The proof here uses one-jump path generators and a separate integer deficit identity, not the cyclic two-boundary run-count optimum.

A full accessible treatment of simplex-constrained image total variation [4] applies the pointwise simplex projection as an optimization substep, but its total variation is computed across **spatial pixels**, not across ordered coordinates of one projected simplex vector; it gives no two-input open-path modulus. Standard algorithmic simplex-projection papers [1,2] do not provide that seminorm estimate. Nearby metric-projection work in other ambient norms does not imply it. No claim of worldwide bibliographic priority is made.

## Limitations

The theorem treats real Euclidean simplex projection and **unweighted open-path** first-difference variation; it does not give weighted path constants, cyclic constants (which are different and previously treated), other graphs, non-Euclidean nearest-point projections, or monotonicity of the projected difference for every input pair. The original contribution is the specific sharp open-path stability constant, with its integer-parity obstruction and attainability. No independent audit has been performed.

## References

[1] J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, *Efficient Projections onto the \(\ell_1\)-Ball for Learning in High Dimensions*, ICML 2008, publicly published 2008-07-05, DOI https://doi.org/10.1145/1390156.1390191.

[2] W. Wang and M. Á. Carreira-Perpiñán, *Projection onto the Probability Simplex: An Efficient Algorithm with a Simple Proof, and an Application*, arXiv:1309.1541v1, first posted 2013-09-06, https://arxiv.org/abs/1309.1541.

[3] *Sharp Cyclic-Variation Amplification of Euclidean Simplex Projection*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-cyclic-variation-amplification-of-euclidean-simplex-projec--95284892279a.

[4] J. Lellmann, J. Kappes, J. Yuan, F. Becker, and C. Schnörr, *Convex Multi-Class Image Labeling by Simplex-Constrained Total Variation*, 2008 technical report and 2009 conference version, accessible full manuscript https://hci.iwr.uni-heidelberg.de/sites/default/files/publications/files/402459334/Lellmann-et-al-09a.pdf.
