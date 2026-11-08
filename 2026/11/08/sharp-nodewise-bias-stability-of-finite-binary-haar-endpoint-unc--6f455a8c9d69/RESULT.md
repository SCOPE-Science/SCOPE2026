# Sharp nodewise-bias stability of finite binary Haar endpoint unconditionality

## Finding
Let a finite full binary probability tree have depth \(d\ge1\) and strictly positive child probabilities at every internal vertex. Let \(U(\mathcal T)\) be the maximum \(L^\infty\)-operator norm of all independent real sign changes of its constant Haar coefficient and its \(2^d-1\) normalized martingale-difference Haar coefficients.

Write \(r_v\in(0,1/2]\) for the smaller conditional child probability at an internal vertex \(v\), and \(r_j=\min_{|v|=j-1}r_v\), for \(1\le j\le d\). Set \(A_{d+1}=0\), \(B_{d+1}=1\), and compute backwards
\[
A_j=A_{j+1}+(1-r_j)(1+B_{j+1}),\qquad
B_j=(1-r_j)-r_jB_{j+1}.
\]
Then the sharp, universally attainable upper envelope is
\[
U(\mathcal T)\le A_1+B_1.
\]
This upper bound cannot be decreased for any prescribed levelwise lower bounds \(r_j\) on both child probabilities: the level-homogeneous tree with splits \((r_j,1-r_j)\) attains it.

The completely fair tree uniquely minimizes the norm among all strictly positive binary probability trees of depth \(d\), with value
\[
F_d=\frac{2d}{3}+\frac59+\frac49\left(-\frac12\right)^d.
\]
More precisely, if \(j\) is the *first biased generation* (all splits at earlier generations are fair), and
\(\delta=\max_{|v|=j-1}(1/2-r_v)>0\), then
\[
U(\mathcal T)\ge F_d+C_{d,j}\delta,
\qquad C_{d,j}=\frac49\left(2+\left(-\frac12\right)^{j-1}\right)
\left(2+\left(-\frac12\right)^{d-j}\right)>0.
\]
The bound is **exact** for a tree in which just one vertex at generation \(j\) has an asymmetric split with minority probability \(1/2-\delta\), and every other split is fair. If all splits are fair, \(U(\mathcal T)=F_d\).

A local greedy rule is not valid for arbitrary nodewise bias. In a two-generation tree whose root splits \((1/4,3/4)\), whose minority child splits \((1/2,1/2)\), and whose majority child splits \((1/10,9/10)\), the four maximized evaluation-row norms are respectively \(5/2,5/2,27/10,11/10\). Hence the unique maximizing evaluation leaf begins with the **majority** root child, and \(U=27/10\).

## Assumptions and scope
The leaf space \(X\) consists of \(2^d\) atoms. At each internal vertex \(v\), the two children partition its mass \(\mu(v)>0\) in conditional proportions \(p_v\) and \(1-p_v\), with \(0<p_v<1\). Set \(h_\emptyset=1\) for the constant basis vector. For an internal vertex \(v\), its normalized Haar function equals
\[
h_v=\sqrt{\frac{1-p_v}{p_v\mu(v)}}\,\mathbf1_{v0}
-\sqrt{\frac{p_v}{(1-p_v)\mu(v)}}\,\mathbf1_{v1}.
\]
These, together with the constant vector, form an orthonormal basis of real \(L^2(X,\mu)\). Independent signs \(\varepsilon_\emptyset,\varepsilon_v\in\{-1,+1\}\) act by
\[
T_\varepsilon f=\varepsilon_\emptyset\langle f,1\rangle1
+\sum_{v\text{ internal}}\varepsilon_v\langle f,h_v\rangle h_v.
\]
The operator norm is measured on the same real finite atomic \(L^\infty\), not on \(L^2\), and is maximized jointly over \(\varepsilon\) and input functions of supremum norm at most one. Each claim holds for every integer \(d\ge1\), with no balance requirement other than strict positivity of the children. For depth zero, the sole sign operator has norm one.

## Proof
**1. An exact row representation.** Fix a leaf \(x\) with ancestral selected-child conditional probabilities \(p_1,\dots,p_d\in(0,1)\). Multiplying every sign simultaneously by minus one permits the constant sign to be \(+1\). Let \(e_j\in\{-1,1\}\) be the Haar multiplier at the ancestor of level \(j\). Define \(t_0=1\) and
\[
t_j=p_jt_{j-1}+(1-p_j)e_j\quad(1\le j\le d).
\]
The integral kernel of \(T_\varepsilon\) is constant on the sibling subtree omitted at level \(j\), and on the final leaf. Direct multiplication of the two normalized Haar values gives its exact absolute row integral
\[
R_x(e_1,\ldots,e_d)
=\sum_{j=1}^d(1-p_j)|t_{j-1}-e_j|+|t_d|
=\sum_{j=1}^d(1-p_j)(1-e_jt_{j-1})+|t_d|.
\]
Here \(|t_j|\le1\). A finite atomic operator has norm equal to its largest absolute kernel row sum, so
\[
U(\mathcal T)=\max_{x\in X}\max_{e_j=\pm1}R_x(e_1,\ldots,e_d).
\]
Every maximizing row supplies a norming input \(f(y)=\operatorname{sgn}K_\varepsilon(x,y)\) on nonzero kernel entries, with arbitrary choices where the kernel vanishes. Signs outside the selected ancestral path do not affect that row.

**2. Monotonicity of a fixed row in its selected probabilities.** Hold the signs and all probabilities except \(p_j\) fixed. Let \(t=t_{j-1}\), \(e=e_j\), and let \(J(u)\) be the remaining suffix contribution after level \(j\), beginning from state \(u\). The suffix is \(1\)-Lipschitz: its individual summands and final \(|t_d|\) have total Lipschitz coefficients
\[
\sum_{k=j+1}^{d}(1-p_k)\prod_{j<\ell<k}p_\ell
+\prod_{\ell=j+1}^{d}p_\ell=1.
\]
Thus, for \(0<p<q<1\),
\[
\begin{aligned}
&(1-q)(1-et)+J(qt+(1-q)e)\\
&\quad-\big[(1-p)(1-et)+J(pt+(1-p)e)\big]\\
&\le -(q-p)|t-e|+(q-p)|t-e|=0.
\end{aligned}
\]
Consequently each fixed-sign row value, and then its maximum over sign patterns, is nonincreasing separately in every selected conditional probability. This is a comparison between complete statements, not a pointwise comparison of normalized Haar functions.

**3. Exact product envelope.** For a fixed probability sequence \(r_1,\dots,r_d\le1/2\), let \(\Phi_{d+1}(t)=|t|\) and define
\[
\Phi_j(t)=\max_{e=\pm1}\big[(1-r_j)(1-et)
+\Phi_{j+1}(r_jt+(1-r_j)e)\big],\quad |t|\le1.
\]
Backwards induction gives \(\Phi_j(t)=A_j+B_j|t|\), where the displayed recursion holds and \(0\le B_j\le1\). Indeed, for \(r\le1/2\) and \(|t|\le1\),
\(|rt+(1-r)e|=(1-r)+ret\); the maximizing sign has the opposite sign to \(t\) (ties allowed). Every chosen probability in any tree is at least the minimum \(r_j\) of its generation, so monotonicity from step 2 gives every row at most \(\Phi_1(1)=A_1+B_1\). The homogeneous tree realizes the minimizing probabilities along a consistent leaf and attains equality, proving the sharp upper envelope.

**4. Fair minimum and one-defect stability.** For the constant fair sequence, solving the recurrence yields
\[
B_j^{(0)}=\frac13+\frac23\left(-\frac12\right)^{d-j+1}
\]
and the stated \(F_d=\Phi_1(1)\). In a product sequence whose only nonfair entry is the \(j\)-th, denote it by \(r\in(0,1/2]\). The recurrence is affine in \(r\), and differentiation at that level decreases both \(A_j\) and \(B_j\) with coefficient
\[
1+B_{j+1}^{(0)}=\frac23\left(2+\left(-\frac12\right)^{d-j}\right).
\]
Propagation through the preceding \(j-1\) fair levels multiplies this coefficient in the root quantity \(A_1+B_1\) by
\(\frac23(2+(-1/2)^{j-1})\). Therefore the product row maximum is exactly
\[F_d+C_{d,j}(1/2-r).\]
If the tree has a first biased generation \(j\), choose a node with largest \(\delta\), follow the necessarily fair ancestors, take its minority child, and subsequently take minority children. Every later selected probability is at most \(1/2\). Step 2 now compares that path with the one-defect product sequence, giving the stated lower bound. If just one vertex is biased, all paths not through it have fully fair probabilities, and its majority-child paths cannot exceed the fair value by step 2; hence the lower bound is attained. Positivity of \(C_{d,j}\) proves uniqueness of the fair minimizer.

**5. Greedy counterexample.** For the specified four-atom tree, enumerate the four ancestral sign pairs in the exact row formula. The two leaves under the root minority child each give \(5/2\); the two under its majority child give \(27/10\) and \(11/10\). Therefore the sole maximizing evaluation leaf starts with the more likely child. The signs on that leaf can be chosen \(e_1=e_2=-1\), and the corresponding kernel-row sign input attains \(27/10\). This completes the proofs.

## Verification
The accompanying standalone Python checker uses exact rational arithmetic and two independent finite descriptions: direct full Haar multiplier matrices with all global signs, and ancestral-path kernel recurrences. It checks equality of the two norms on 39 positive rational trees of depths one through three; verifies 240 product-envelope identities; verifies 135 single-defect coefficients and 11 full-matrix one-bias cases; and checks all four rows of the majority-first-branch example. Execute `python3 verify_tree_haar.py`. These are finite diagnostics, not the reason the universal all-depth induction holds.

## Relationship to prior work
Classical results of Burkholder and Choi concern martingale-transform inequalities and unconditional basis constants in finite \(L^p\). Osękowski's 2013 paper proves sharp restricted weak-type bounds, while Thiele, Treil and Volberg develop weighted \(L^2\) estimates in nonhomogeneous settings. Earlier complete-generation calculations for level-dependent binary Haar probabilities establish the product recurrence and the fair-case constant. The claim here is the exact **arbitrary nodewise-tree comparison principle**, its sharp levelwise envelope, first-bias quantitative rigidity and the non-greedy norming-leaf phenomenon, not the classical Haar basis construction or the previously available product special case.

## Limitations
The result is for real sign changes on a full finite binary filtration with positive atomic probabilities. It does not give analogous constants for suppressing (rather than changing signs of) coefficients, nonbinary splittings, incomplete trees, complex phases, or general \(L^p\) norms. The upper envelope is exact over the whole admissible class but need not be attained by each individually specified node-dependent tree. The lower stability coefficient uses the first generation containing a biased node, not a maximum over all biased nodes with arbitrary biased ancestors. The comparison with unindexed or inaccessible older martingale-transform literature is subject to bibliographic revision.

## References
- A. Osękowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, Journal of Function Spaces (2013), article 646012, doi:10.1155/2013/646012, first publicly dated 2013-12-05.
- C. Thiele, S. Treil and A. Volberg, *Weighted martingale multipliers in non-homogeneous setting and outer measure spaces*, arXiv:1411.5345 (2014).
- A. Osękowski, *Sharp inequalities for the Haar system and martingale transforms*, Probability and Mathematical Statistics 36 (2016), 147–164, https://www.math.uni.wroc.pl/~pms/files/36.1/Article/36.1.11.pdf.
- K. P. Choi, *A Sharp Inequality for Martingale Transforms and the Unconditional Basis Constant of a Monotone Basis in \(L^p(0,1)\)*, Transactions of the AMS (1992), doi:10.2307/2153920.
