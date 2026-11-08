# A sharp ternary Haar endpoint law with middle-digit rigidity

## Finding
Let \(d\geq1\) and equip \(X_d=\{1,2,3\}^{d}\) with uniform probability. On each three-child split fix the real orthonormal contrasts
\[
a=(\sqrt{3/2},-\sqrt{3/2},0),\qquad
b=(1,1,-2)/\sqrt2.
\]
Include the constant function and both normalized Haar contrasts at every node strictly above depth \(d\). For independent real signs on *individual* basis functions, let \(U_d\) be the largest \(L^\infty\)-operator norm of the associated signed orthogonal expansion. Then
\[
\boxed{U_d=d+\frac56-\frac{1}{2\,3^d}\quad(d\geq1),\qquad U_0=1.}
\]
The exact growth slope is \(\lim_{d\to\infty}U_d/d=1\). A terminal word \(x=(x_1,\ldots,x_d)\) is a row at which some signed multiplier attains this maximum if and only if, for \(d\geq2\),
\[
 x_2,x_3,\ldots,x_{d-1}\in\{1,2\}.
\]
The first and last digits are unrestricted; all three terminal words maximize when \(d=1\). Thus for \(d\geq2\) there are precisely \(9\cdot 2^{d-2}\) maximizing rows, among the \(3^d\) available rows. Norming real inputs are signs of the corresponding signed kernel row (with arbitrary values in \([-1,1]\) where that row vanishes).

## Assumptions and scope
For a prefix \(w\in\{1,2,3\}^{\ell}\), \(0\leq\ell<d\), define \(\psi_{w,1}\) and \(\psi_{w,2}\) by setting their values on a word \(x\) extending \(w\) equal to \(3^{\ell/2}a_{x_{\ell+1}}\) and \(3^{\ell/2}b_{x_{\ell+1}}\), respectively, and zero otherwise. The collection
\[
 \mathcal B_d=\{\mathbf1\}\cup\{\psi_{w,j}:|w|<d,\ j=1,2\}
\]
is an orthonormal basis of real \(L^2(X_d)\), with \(3^d\) members. Every \(\varepsilon_\phi\in\{-1,+1\}\) gives
\[
 T_\varepsilon f=\sum_{\phi\in\mathcal B_d}\varepsilon_\phi\langle f,\phi\rangle\phi,\qquad U_d=\max_{\varepsilon}\|T_\varepsilon\|_{L^\infty\to L^\infty}.
\]
The normalization and the ordered orthogonal pair \((a,b)\) are essential: the theorem does **not** claim the same value for an arbitrary orthogonal rotation of these two contrasts. The same finite-dimensional operator arises by taking the first \(d\) complete levels of the corresponding three-adic step Haar system on \([0,1]\), acting on all bounded inputs through its orthogonal truncation.

## Proof
**1. Kernel reduction.** By reversing all signs simultaneously we may fix the constant coefficient sign to \(+1\). The matrix kernel is
\[
K_\varepsilon(x,y)=1+\sum_{\ell=0}^{d-1}3^\ell\mathbf1_{\{x_1\cdots x_\ell=y_1\cdots y_\ell\}}\sum_{s=1}^2\varepsilon_{x_1\cdots x_\ell,s}c_s(x_{\ell+1})c_s(y_{\ell+1}),
\]
where \(c_1=a\), \(c_2=b\). Therefore \(\|T_\varepsilon\|_{\infty\to\infty}=\max_x3^{-d}\sum_y|K_\varepsilon(x,y)|\). Signs off the ancestor chain of a tested row do not affect it. The row \(\ell^1\) norm is attained by an input that agrees with the sign of the row at every nonzero coordinate.

**2. Scalar Bellman principle.** Let \(F_m(z)\) be the greatest row absolute average in a subtree of remaining depth \(m\) whose inherited, subtree-normalized constant term is \(z\). Then \(F_0(z)=|z|\). At a three-child split, choose evaluated child \(i\) and signs \(\sigma,\tau\in\{-1,+1\}\). Writing \(v_j=\sigma a_i a_j+\tau b_i b_j\), disjointness of the other two subtrees yields the *exact* recurrence
\[
F_m(z)=\max_{i,\sigma,\tau}
\left\{\frac13\sum_{j\ne i}|z+v_j|+
F_{m-1}\!\left(\frac{z+v_i}{3}\right)\right\}.
\tag{1}
\]
Every diagonal \(v_i\) has magnitude at most \(2\), so the interval \([-1,1]\) is invariant under the states reached from \(z=1\). Moreover \(F_m\) is even, convex and \(1\)-Lipschitz: directly, it is a maximum of absolute row averages with common additive parameter \(z\).

**3. Four actions and their comparison.** For \(0\leq z\leq1\), the two evaluated children \(i=1,2\) produce exactly four possible values
\[
\begin{aligned}
 A&=\frac{2(1-z)}3+F_{m-1}((z+2)/3),\\
 B&=1+F_{m-1}((z+1)/3),\\
 C&=1+F_{m-1}((z-1)/3),\\
 D&=\frac{2(1+z)}3+F_{m-1}((z-2)/3).
\end{aligned}
\tag{2}
\]
The third evaluated child produces only \(A\) and \(D\). Even convexity gives \(B\geq C\). Evenness and the Lipschitz bound give \(D-A\geq2z/3\), so \(D>A\) for \(z>0\). Finally
\[
D-B=\frac{2z-1}{3}+F_{m-1}((2-z)/3)-F_{m-1}((1+z)/3).
\tag{3}
\]
The two arguments of \(F_{m-1}\) differ by \((1-2z)/3\). Thus the Lipschitz bound proves \(B\geq D\) on \([0,1/2]\) and \(D\geq B\) on \([1/2,1]\). Consequently
\[
F_m(z)=\begin{cases}
1+F_{m-1}((1+z)/3),&0\leq z\leq1/2,\\
2(1+z)/3+F_{m-1}((2-z)/3),&1/2\leq z\leq1.
\end{cases}
\tag{4}
\]
There is no approximate relaxation in these comparisons.

**4. Closed Bellman envelope.** Both branch maps in (4) send \([0,1]\) into \([1/3,1/2]\). The affine map \(z\mapsto(1+z)/3\) fixes \(1/2\). Induction from \(F_0(z)=z\) for \(z\geq0\) therefore gives, for every \(m\geq1\),
\[
F_m(z)=\begin{cases}
m+\frac12+\dfrac{z-1/2}{3^m},&0\leq z\leq1/2,\\
m+\frac16+\dfrac{2z}{3}+\dfrac{1-2z}{2\,3^m},&1/2\leq z\leq1.
\end{cases}
\tag{5}
\]
Both branches agree at \(z=1/2\). In particular \(F_m\) has Lipschitz constant at most \(2/3\) on \([-1,1]\) whenever \(m\geq1\), making the comparisons in (3) strict away from \(z=1/2\) as soon as \(m\geq2\). Starting at inherited state \(z=1\) proves \(U_d=F_d(1)=d+5/6-1/(2\,3^d)\).

**5. Maximizing-row classification.** For \(d\geq2\), the initial state \(z=1>1/2\) forces action \(D\), possible with any of the three evaluated children. The next inherited state is \(-1/3\). While at least two levels remain, its absolute value lies strictly below \(1/2\) and the \(B\)-type action is forced; this action is possible only for evaluated child \(1\) or \(2\). The absolute states then follow \(r\mapsto(1+r)/3\), remaining strictly below \(1/2\). At the last level, \(F_0\) makes \(B\) and \(D\) tie, and all three evaluated children are possible. These rules are necessary by strict comparison and sufficient by (1). They give exactly \(9\cdot2^{d-2}\) maximizing words for \(d\geq2\), and all three words at \(d=1\). To construct optimal signs explicitly, take constant sign \(+1\), choose diagonal contrast contribution \(-2\) at the first node, \(-1\) at each intermediate node (where the evaluated child is \(1\) or \(2\)), and \(+2\) at the last node; the indicated contributions are realized by signs of the displayed contrasts. Signs outside the evaluated ancestry are free. The equality description for inputs follows from rowwise \(\ell^1\)-duality.

## Verification
The standalone standard-library script `checker.py` performs two independent families of exact-rational finite diagnostics. First, it enumerates all evaluated child/sign choices directly in the scalar recurrence for 222 pairs of depth and rational state through depth six and checks (5). Second, it constructs signed kernel rows from the original orthonormal contrasts, exhaustively enumerates ancestral signs through depth four, and checks the sharp formula and *the entire set* of maximizing words at those depths. The latter tests cover all 120 evaluation rows through depth four. It prints `ALL_TERNARY_HAAR_ENDPOINT_CHECKS_PASSED` when all comparisons succeed. These finite tests corroborate but do not replace the all-depth argument in the proof.

## Relationship to prior work
Kazarian, Kazaryan and San-Antolín (first available 2014 preprint) develop higher-rank \(m\)-adic Haar wavelets allowing arbitrary orthonormal contrast choices and prove unconditional-basis results in finite \(L^p\) settings, but do not evaluate this basis-specific, signed finite-depth \(L^\infty\) operator norm or identify its maximizing rows. Osękowski (2013) proves sharp restricted weak-type bounds for Haar projections and martingale transforms, with different hypotheses and norms. The result here is not a strengthening of those finite-\(p\) inequalities; it is an exact endpoint computation for a fixed three-child contrast frame. The binary one-contrast setting does not imply the two-contrast branching recurrence (1).

## Limitations
This result requires real coefficient signs, uniform ternary splitting, all complete levels, and the specified ordered pair of orthonormal contrasts. No claim is made for arbitrary rotated contrast frames, complex phases, suppression-only transforms, incomplete trees, nonuniform probabilities, or general \(L^p\) norms. The literature comparison cannot exclude every unindexed equivalent calculation, and no independent audit has been performed.

## References
1. K. S. Kazarian, S. S. Kazaryan and Á. San-Antolín, *Wavelets in weighted norm spaces*, arXiv:1410.4888, first submitted 17 October 2014. Full open text: https://arxiv.org/abs/1410.4888 .
2. A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, Journal of Function Spaces and Applications (2013), Article 646012, first published 5 December 2013, DOI:10.1155/2013/646012. Open full text: https://onlinelibrary.wiley.com/doi/10.1155/2013/646012 .
