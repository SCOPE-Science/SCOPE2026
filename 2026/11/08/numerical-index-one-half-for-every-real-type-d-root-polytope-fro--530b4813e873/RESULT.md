# Numerical index one half for every real type-\(D\) root polytope from dimension four onward

## Finding
For each integer \(d\ge4\), let \(X_d\) be \(\mathbb R^d\) with the norm
\[
 N_d(x)=\max\left\{\|x\|_\infty,\frac12\|x\|_1\right\}.
\]
Its unit ball is the type-\(D_d\) root polytope
\[
 P_d=\operatorname{conv}\{\varepsilon e_i+\delta e_j:1\le i<j\le d,\ \varepsilon,\delta\in\{-1,1\}\}.
\]
For every real linear operator \(T:X_d\to X_d\), its spatial numerical radius
\[
 v(T)=\max\{|f(Tx)|:N_d(x)=N_d^*(f)=1,\ f(x)=1\}
\]
satisfies the sharp inequality
\[
 \boxed{\tfrac12\|T\|\le v(T)\le\|T\|,\qquad n(X_d)=\tfrac12.}
\]
The lower-bound constant is optimal for the rank-one operator \(T_dx=(x_1+x_2)e_3\): \(\|T_d\|=2\) and \(v(T_d)=1\). In dimension four the unit ball is the regular \(24\)-cell.

## Assumptions and scope
Only real scalars are considered, and \(d\) is any integer at least four. The standard coordinate vectors are \(e_1,\dots,e_d\). Numerical radius refers to norm-one real supporting pairs, not to the Euclidean numerical radius; neither the complex-space numerical index nor an infinite-dimensional limit is asserted. For completeness, the proof actually works already when \(d=3\), but the stated new family begins in dimension four because the three-dimensional case is covered by the numerical-index result for equilateral Lipschitz-free spaces.

## Proof
**Step 1: the unit ball and the finite norming set.** The unit ball of \(N_d\) is \(\{x:|x_i|\le1,\sum_i|x_i|\le2\}\). In any fixed coordinate orthant, this is affinely equivalent to \(\{u\in[0,1]^d:\sum u_i\le2\}\). Its vertices have all coordinates integral and contain at most two ones: if the sum constraint is slack, a fractional coordinate admits two-sided perturbation; if it is tight, two fractional coordinates admit opposite perturbations, and exactly one fractional coordinate is impossible since the sum is the integer two. A vector with zero or one nonzero unit coordinate is also a convex combination of the signed pair vectors (for \(e_i\), average \(e_i+e_j\) and \(e_i-e_j\)). Thus \(B_{X_d}=P_d\); the signed pair vectors are precisely its \(2d(d-1)\) vertices, since each is the unique maximizer of a suitable coordinate-pair linear functional.

Define the finite symmetric family of functionals
\[
 \mathscr F_d=\{\pm e_k^*:1\le k\le d\}\ \cup\ \left\{\tfrac12(s_1,\ldots,s_d):s_i\in\{-1,1\}\right\}.
\]
Here each \(f\in\mathscr F_d\) has \(N_d^*(f)=1\), and
\(N_d(y)=\max_{f\in\mathscr F_d}f(y)\). Hence the dual unit ball is the convex hull of \(\mathscr F_d\). For a polyhedral real space, the numerical radius is the maximum of \(|f(Tx)|\) over vertices \(x\) of the unit ball and \(f\in\mathscr F_d\) satisfying \(f(x)=1\). Indeed, first decompose a norming \(x\) into vertices of its exposed face \(\{y:f(y)=1\}\); then decompose the norming \(f\) into members of \(\mathscr F_d\), each of which must also norm \(x\). Absolute values are controlled by maxima at these finite pairs.

**Step 2: universal lower bound.** Write \(\nu=v(T)\). Fix any root vertex \(x=\varepsilon e_i+\delta e_j\), \(i\ne j\), and any \(f\in\mathscr F_d\). If \(|f(x)|=1\), the pair \((x,f)\), with the functional's sign chosen appropriately, is norming and \(|f(Tx)|\le\nu\).

For \(f=\pm e_k^*\) with \(k\notin\{i,j\}\), set
\[
 y=\varepsilon e_i+e_k,\qquad z=\delta e_j-e_k.
\]
Then \(x=y+z\), both summands are root vertices, and \(|f(y)|=|f(z)|=1\). Therefore \(|f(Tx)|\le2\nu\).

For a sign functional \(f=(s_1,\ldots,s_d)/2\), the only nonnorming possibility is \(s_i\varepsilon=-s_j\delta\). Choose \(k\notin\{i,j\}\) and \(a=s_i\varepsilon s_k\in\{-1,1\}\). Set
\[
 y=\varepsilon e_i+a e_k,\qquad z=\delta e_j-a e_k.
\]
Again \(x=y+z\), now \(f(y)=s_i\varepsilon\) and \(f(z)=-s_i\varepsilon\), so \(|f(Tx)|\le2\nu\). This exhausts the possibilities. Consequently, for each root vertex \(x\),
\[
 N_d(Tx)=\max_{f\in\mathscr F_d}|f(Tx)|\le2\nu.
\]
The operator norm of \(T\) is attained at some root vertex (by convexity), giving \(\|T\|\le2v(T)\).

**Step 3: a sharp rank-one witness.** Let \(T_dx=(x_1+x_2)e_3\). Its operator norm is two: the output norm is \(|x_1+x_2|\), bounded by two on the unit ball and attained at \(x=e_1+e_2\). To compute its numerical radius, consider each root vertex \(x\). If both active coordinates are \(1,2\) with the same sign, then \(|x_1+x_2|=2\); every norming coordinate functional has third component zero, and every norming sign functional has third component of absolute value \(1/2\). Thus \(|f(T_dx)|\le1\) for every norming functional. If there is exactly one active coordinate among \(1,2\), the output coefficient has absolute value one and \(|f(e_3)|\le1\); if neither is active or both contribute opposite signs, the output is zero. Hence \(v(T_d)\le1\). Equality holds at \(x=e_1+e_2\) with the norming sign functional \(f=(1,\ldots,1)/2\), for which \(f(T_dx)=1\). Therefore \(v(T_d)/\|T_d\|=1/2\), completing the proof.

## Verification
The finite supporting-pair reduction and each decomposition are exact and apply to arbitrary real operator matrices, not only tested matrices. A standalone checker `check_type_d_index.py` enumerates root vertices and norming generators for dimensions four through seven, verifies the universal two-root decomposition for every generator, and computes the witness operator's norm and numerical radius by exact integer arithmetic. Run `python3 check_type_d_index.py` in a standard Python 3 environment. These finite tests corroborate the combinatorics but do not replace the all-dimension proof.

## Relationship to prior work
Rafael Chiclana's 2026 resolution of the two-dimensional real \(\ell_p\) numerical-index problem motivates considering precise numerical indices beyond the classical spaces. Sain, Paul, Bhunia and Bag (2018) prove a general finite-facet reduction and evaluate two other families of real polyhedral Banach spaces; their explicit prism and bipyramid families do not contain the dimension-four-and-higher type-\(D\) root polytopes. This result uses the same basic finite-supporting-pair principle but adds a uniform root-splitting lemma and a sharp rank-one witness valid for all \(d\ge4\).

The publicly recorded exact index \(1/2\) for equilateral finite Lipschitz-free spaces covers the dimension-three root-polytope case via the \(D_3\)-to-\(A_3\) isomorphism; it does not cover the present higher-dimensional unit balls. In fact, a \(d\)-dimensional Lipschitz-free space over \(d+1\) points has at most \(d(d+1)\) extreme molecular vertices, whereas \(P_d\) has \(2d(d-1)>d(d+1)\) vertices for \(d\ge4\). Existing analyses of the type-\(D\) polytopes' lattice geometry and illumination concern different invariants, not the numerical index.

## Limitations
The claim is for real, finite-dimensional norms only. It does not classify all operators attaining the index, or assert the value for nearby perturbations of the polytope. The originality assessment is best-knowledge rather than independent publication-priority certification; an older abstract finite-dimensional numerical-index theorem may imply the same inequality under a different polyhedral representation.

## References
1. Rafael Chiclana, *The Numerical Index of Two-Dimensional Real \(\ell_p\) Spaces*, arXiv:2606.01675, first publicly posted 2026-06-01. https://arxiv.org/abs/2606.01675
2. Debmalya Sain, Kallol Paul, Pintu Bhunia, Santanu Bag, *On the numerical index of polyhedral Banach spaces*, arXiv:1809.04778, first posted 2018-09-13. https://arxiv.org/abs/1809.04778
3. *Numerical index one half for every finite equilateral Lipschitz-free space*, publicly searchable published-finding corpus research record, 2026-10-04, identifier `2026/10/4/SCOPE-numerical-index-one-half-for-every-finite-equilateral-lipschitz--cc7060df7211`.
4. *Exact quantitative illumination of type-\(D_d\) root polytopes*, publicly searchable mathematical result, 2026-10-11, identifier `2026/10/11/SCOPE-exact-quantitative-illumination-of-type-d-d-root-polytopes--34479eff57ed`.
