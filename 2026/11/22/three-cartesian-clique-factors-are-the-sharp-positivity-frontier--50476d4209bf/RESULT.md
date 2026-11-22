# Three Cartesian clique factors are the sharp positivity frontier for the second-order Padé heat step

## Finding
Let \(d\ge1\), let \(q_i\ge2\) be arbitrary integers, and let \(w_i>0\) be arbitrary real conductances. Form the Cartesian product \(G=K_{q_1}^{(w_1)}\square\cdots\square K_{q_d}^{(w_d)}\), where each edge changing coordinate \(i\) has conductance \(w_i\). Write \(L\) for its weighted combinatorial Laplacian and set
\[
T_h=\left(I+hL+\frac{h^2}{2}L^2\right)^{-1},\qquad h\ge0.
\]
The completed, second-order, L-stable Padé \([0/2]\) heat step is entrywise nonnegative at **every** timestep if and only if \(d\le3\), independent of all the alphabet sizes and positive coordinate weights. More precisely:

- If \(1\le d\le3\), every entry of \(T_h\) is strictly positive for every \(h>0\), while \(T_0=I\).
- If \(d\ge4\), choose vertices \(x,y\) differing in exactly four coordinates, indexed by a set \(S\). Then
\[
(T_h)_{xy}=-6\left(\prod_{i\in S}w_i\right)h^4+O_{G}(h^5)<0
\]
for all sufficiently small \(h>0\). At every \(h\), \(T_h\) is symmetric positive definite and fixes the all-ones vector; these two properties therefore do not guarantee entrywise positivity.

In particular, positivity is unconditional on three-dimensional binary, ternary and mixed-alphabet Hamming graphs, of arbitrarily large finite order as the alphabet sizes grow, and fails already on the four-dimensional Boolean cube for small positive steps. The four-step obstruction is known in greater graph generality; the new positive result is the unrestricted three-factor converse within the Cartesian-clique product family.

## Assumptions and scope
The factors are loopless complete graphs of order at least two, each with a single strictly positive edge conductance shared by all edges of that factor; different factors may have different orders and weights. The product uses the usual Kronecker-sum Laplacian, not a normalized Laplacian. All times \(h\ge0\) are real and matrix inverses are exact. This is a statement about positivity of the completed linear update for every nonnegative initial state, not about internal stages, roundoff, general weighted graphs, or arbitrary graphs of diameter three. A function \(F\) of the symmetric Laplacian means its usual spectral functional calculus.

## Proof
**1. Factor spectral decomposition.** Let \(P_i=J_{q_i}/q_i\) and \(Q_i=I-P_i\). The one-factor weighted Laplacian is \(w_iq_iQ_i\). Write \(a_i=h w_iq_i>0\). The tensor product projector indexed by \(U\subseteq[d]\), with \(Q_i\) in positions in \(U\) and \(P_i\) in positions outside \(U\), has eigenvalue \(\sum_{i\in U}w_iq_i\) under \(L\). Put
\[
f(z)=\frac1{1+z+z^2/2}=\frac2{z^2+2z+2}.
\]
For vertices \(x,y\), define \(S=\{i:x_i\ne y_i\}\), \(E=[d]\setminus S\), and \(N=\prod_iq_i\). The exact spectral formula is
\[
(T_h)_{xy}=\frac1N\sum_{U\subseteq[d]}f\!\left(\sum_{i\in U}a_i\right)\prod_{i\in U}c_i,
\qquad c_i=\begin{cases}q_i-1,&i\in E,\\-1,&i\in S.\end{cases}
\tag{1}
\]
Indeed, a tensor projector contributes \(1/q_i\) off-diagonal when it uses \(P_i\), and contributes \(-1/q_i\) off-diagonal or \((q_i-1)/q_i\) diagonal when it uses \(Q_i\).

**2. A strict finite-difference positivity lemma.** Let \(\Delta_a f(z)=f(z+a)-f(z)\). Group the sum in (1) according to the active coordinates \(U\subseteq E\). With \(k=|S|\) and \(z_U=\sum_{i\in U}a_i\), this gives
\[
N(T_h)_{xy}=\sum_{U\subseteq E}\left(\prod_{i\in U}(q_i-1)\right)(-1)^k\left(\prod_{i\in S}\Delta_{a_i}\right)f(z_U).
\tag{2}
\]
For \(k\ge1\), the fundamental theorem of calculus iterated \(k\) times gives the exact identity
\[
(-1)^k\left(\prod_{i\in S}\Delta_{a_i}\right)f(z)
=\int_{\prod_{i\in S}[0,a_i]}(-1)^k f^{(k)}\!\left(z+\sum_{i\in S}t_i\right)\,\prod_{i\in S}dt_i.
\tag{3}
\]
At \(k=0\), the factor on the left is simply \(f(z)>0\). Set \(D(z)=z^2+2z+2\). Direct differentiation yields
\[
-f'(z)=\frac{4(z+1)}{D(z)^2}>0,\qquad
f''(z)=\frac{4(3z^2+6z+2)}{D(z)^3}>0,
\]
\[
-f'''(z)=\frac{48z(z+1)(z+2)}{D(z)^4}>0\quad(z>0).
\tag{4}
\]
All these expressions are nonnegative at \(z=0\); for the third derivative only, equality occurs there. Each integration box in (3) has positive volume because every \(a_i>0\), and its argument is strictly positive except on a zero-measure boundary when \(z=0\). Therefore the integral is **strictly positive** for \(k=1,2,3\). All coefficients in (2) are strictly positive, so every \((T_h)_{xy}>0\) when \(d\le3\), \(h>0\), with the diagonal handled by \(k=0\). This establishes the positive side for arbitrary orders and weights without extrapolating from finite matrix tests.

**3. The sharp dimension-four obstruction.** The exact scalar expansion at zero is
\[
f(z)=1-z+\tfrac12z^2+0z^3-\tfrac14z^4+O(z^5).
\tag{5}
\]
For \(x,y\) at graph distance four, \((L^j)_{xy}=0\) for \(0\le j\le3\). If they differ in precisely four coordinates \(S\), all length-four contributing walks change those coordinates exactly once, in one of \(4!\) possible orders, and each walk has weight \(\prod_{i\in S}w_i\). The four off-diagonal signs in \(L^4\) multiply to positive one. Thus \((L^4)_{xy}=24\prod_{i\in S}w_i\). Substituting the matrix \(hL\) into (5) proves the displayed \(-6\prod w_i\) leading term, and hence failure of nonnegativity for sufficiently small positive \(h\). Such a pair exists in every product with \(d\ge4\).

**4. Spectral and boundary checks.** The scalar denominator \(1+z+z^2/2\) is strictly positive for \(z\ge0\); therefore \(T_h\) exists and is symmetric positive definite for all \(h\ge0\). Because \(L\mathbf1=0\), \(T_h\mathbf1=\mathbf1\); symmetry also gives column sums one. At \(h=0\), \(T_0=I\) and is nonnegative. For any fixed connected product, \(T_h\to J_N/N\) as \(h\to\infty\); eventual positivity does not repair the failure of **all-step** positivity in dimensions four and above. This completes all quantifiers and boundaries.

## Verification
Run `python3 artifacts/verify.py` using Python 3 standard library only. The script symbolically differentiates the scalar rational denominator using exact integer polynomials, checks the coefficients in (4) and (5), reconstructs the spectral formula (1) with exact rational arithmetic, and independently inverts \(I+hL+h^2L^2/2\) on nine one-, two- and three-factor graph instances, including mixed alphabet sizes. It verifies all matrix entries and stochastic row sums at three positive rational steps, and checks negative four-coordinate entries in the four-cube at two exact rational steps. The checker returned `VERIFY_OK: 10681 exact rational assertions; all true` on the delivered script. The infinite-family conclusion rests on (2)–(5), not on finite checks. The independent matrix calculations use unit weights; the proof handles arbitrary positive factor weights.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten (repository preprint 2012) investigated how Padé approximations can fail positivity for general positive linear systems. Their full paper focuses on *diagonal* Padé maps and general Metzler examples; it does not classify the \([0/2]\) map on Cartesian products of complete graphs. Wade, Khaliq, Siddique and Yousuf (first publicly published 2004) investigated positivity-preserving Padé combinations in parabolic problems; its abstract does not supply this three-factor theorem, but its full text was inaccessible and remains a publication-priority caveat.

Previously published exact graph-heat findings for the **same** \([0/2]\) map establish the distance-four negative coefficient in arbitrary graphs, the exceptional five-vertex path, and exact positivity of cycles through length seven. This result reuses the known distance-four obstruction, not claiming it anew; it supplies the previously unproved positive converse for the entire, independently weighted **Cartesian-clique family** up through three factors, including mixed alphabets. A published criterion on complete **multipartite** graphs does not imply this result because Cartesian products of three nontrivial cliques are generally not complete multipartite. A separate all-step classification for two-stage **Gauss–Legendre \([2/2]\)** on exactly the same Cartesian-clique objects concerns a different rational scalar filter and a different dimension–alphabet frontier, so neither statement implies the other.

## Limitations
The classification concerns exact end-step entrywise nonnegativity and homogeneous conductance within each clique factor, not arbitrary within-factor weights or external potentials. Unconditional positivity for a whole graph family is distinct from a scalar method-wide absolute-monotonicity guarantee. The broad distance-four obstruction and eventual positivity are known facts used as context; the novel contribution claimed is the sharp **three-factor** positive side and its all-parameter combination with that obstruction. Full text of a plausible historical Padé-smoothing paper could not be inspected; a further unindexed equivalence is possible. No independent mathematical audit or claim of publication priority is made.

## References
1. B. A. Wade, A. Q. M. Khaliq, M. Siddique, M. Yousuf, *Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data*, first published September 29, 2004, *Numerical Methods for Partial Differential Equations* 21 (2005), 553–573. https://doi.org/10.1002/num.20039
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, public repository deposit June 19, 2012; *Linear Algebra and Its Applications* 436 (2012), 3425–3442. https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf
3. *Distance-four positivity obstruction and sharp eight-cycle recovery for the second-order Padé heat step*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-distance-four-positivity-obstruction-and-sharp-eight-cycle-recov--5b0558f2856d
4. *Five-vertex and distance-four positivity barriers for Padé \([0/2]\) graph diffusion*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-five-vertex-and-distance-four-positivity-barriers-for-pad-0-2-gr--cbdb39e5b48d
5. *A scalar criterion for unconditionally positive rational graph-heat steps on complete multipartite networks*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-scalar-criterion-for-unconditionally-positive-rational-graph-h--335027f86795
6. *Sharp all-step Gauss positivity on Cartesian products of complete graphs*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-all-step-gauss-positivity-on-cartesian-products-of-complet--e93fc3196dc7
