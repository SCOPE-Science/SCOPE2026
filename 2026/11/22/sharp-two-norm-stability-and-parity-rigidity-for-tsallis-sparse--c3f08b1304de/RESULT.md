# Sharp two-norm stability and parity rigidity for Tsallis sparse probability maps

## Finding

For every integer \(n\ge2\), \(1<\alpha\le2\), and every pair \(z,z'\in\mathbb R^n\), define the Tsallis probability map
\[
E_\alpha(z)=\operatorname*{argmax}_{p\in\Delta_{n-1}}
\left\{\langle z,p\rangle+\frac{1-\sum_{i=1}^n p_i^\alpha}{\alpha(\alpha-1)}\right\},
\qquad \Delta_{n-1}=\{p_i\ge0,\ \sum_i p_i=1\}.
\]
Write \(m=\lfloor n/2\rfloor\), \(\ell=\lceil n/2\rceil\), and \(\gamma=(\alpha-1)/(3-\alpha)\). The exact smallest constant in
\[
\|E_\alpha(z)-E_\alpha(z')\|_1\le L_{n,\alpha}\|z-z'\|_\infty
\]
is
\[
\boxed{L_{n,\alpha}=\frac{4(m\ell)^{\alpha-1}}
 {(m^\gamma+\ell^\gamma)^{3-\alpha}}.}
\]
For even \(n\) this is exactly \(n^{\alpha-1}\). For odd \(n\) it is strictly smaller than \(n^{\alpha-1}\). For \(n=1\), the map is constant and the coefficient is zero. The \(\alpha\downarrow1\) limit equals the sharp \(\ell_\infty\)-to-\(\ell_1\) softmax coefficient \(1\) whenever \(n\ge2\).

For \(1<\alpha<2\), the only interior maximizing probability patterns, up to permutations and swapping the two blocks, consist of \(m\) equal entries summing to
\[
q=\frac{\ell^\gamma}{m^\gamma+\ell^\gamma},
\]
and \(\ell\) equal entries summing to \(1-q\). At \(\alpha=2\) (Euclidean simplex projection, or sparsemax), all strictly positive output probabilities have the same derivative; balanced sign partitions attain the coefficient \(4m\ell/n\). The input-direction extremizers are precisely the associated opposite-sign block directions, up to common translation, scaling, and the tie symmetries.

## Assumptions and scope

The inputs are arbitrary real score vectors. Both norms are ordinary unweighted finite-dimensional coordinate norms; the regularizer is normalized exactly as displayed, without a separate temperature or score multiplier. The result is global, not restricted to a fixed active set, fixed support, or bounded score diameter. The parameter range is \(1<\alpha\le2\); endpoint \(\alpha=1\) is stated as a limit and can also be proved directly for softmax. This is not a claim about \(\ell_2\)-to-\(\ell_2\), \(\ell_\infty\)-to-\(\ell_\infty\), or attention-layer composition norms.

## Proof

**1. Existence and derivative.** The objective is strictly concave on the simplex and has a unique maximizer. For any strictly positive probability vector \(p\), choosing \(z_i=p_i^{\alpha-1}/(\alpha-1)\) produces \(E_\alpha(z)=p\) by the first-order optimality conditions; a common score shift is irrelevant. Set \(\beta=2-\alpha\in[0,1)\). At points with positive active-set probabilities the Hessian of the negative Tsallis regularizer is \(\operatorname{diag}(p_i^{\alpha-2})\), hence the derivative of the output map is the symmetric positive-semidefinite matrix
\[
J(p)=\operatorname{diag}(s)-\frac{ss^{\mathsf T}}{S},
\quad s_i=p_i^\beta\ (p_i>0),\quad s_i=0\ (p_i=0),\quad S=\sum_i s_i.
\]
Here for \(\alpha=2\) the convention is \(s_i=1\) on the positive support and zero elsewhere; at support boundaries the derivative need not exist but does exist almost everywhere. The finite-dimensional regularizer is strongly convex (its interior second derivative is at least one for \(1<\alpha\le2\)), so its convex conjugate has a globally Lipschitz gradient; in particular \(E_\alpha\) is absolutely continuous along line segments. Thus a bound valid for the Jacobian almost everywhere integrates to the global two-input bound. This derivative also follows by differentiating the active-set Karush–Kuhn–Tucker equations.

**2. An exact sign-cut norm identity.** For any symmetric positive-semidefinite \(J\),
\[
\|J\|_{\infty\to1}
=\max_{\varepsilon,\delta\in\{-1,1\}^n}\delta^{\mathsf T}J\varepsilon
=\max_{\varepsilon\in\{-1,1\}^n}\varepsilon^{\mathsf T}J\varepsilon.
\]
The first equality is duality of the two coordinate norms and extremality of cube vertices; the second follows from Cauchy–Schwarz for the positive-semidefinite bilinear form. For the above \(J(p)\), a sign cut \(I\subset[n]\) gives
\[
\varepsilon^{\mathsf T}J(p)\varepsilon
=\frac{4A B}{A+B},\qquad
A=\sum_{i\in I}s_i,\quad B=\sum_{i\notin I}s_i.
\]
Empty/full cuts give zero. This identity explicitly controls every input sign vector and every output dual sign vector, not merely a subset of Jacobian entries.

**3. Optimize a fixed cut.** Let \(k=|I|\), \(h=n-k\), and \(u=\sum_{i\in I}p_i\). Since \(0\le\beta<1\), concavity of the power function gives
\[
A\le k^{1-\beta}u^\beta,\qquad
B\le h^{1-\beta}(1-u)^\beta.
\]
The harmonic-mean expression \(4AB/(A+B)\) increases separately in both variables. For \(0<\beta<1\), equality holds precisely when entries are equal inside each cut block; the endpoint \(\beta=0\) has identical derivatives for all positive probability vectors on a given support. The remaining optimization minimizes
\[
\frac{k^{\beta-1}}{u^\beta}+
\frac{h^{\beta-1}}{(1-u)^\beta}.
\]
For \(0<\beta<1\) this function is strictly convex and diverges at both endpoints, so its unique minimizer solves
\[
\frac{u}{1-u}=\left(\frac{h}{k}\right)^\gamma,
\qquad \gamma=\frac{1-\beta}{1+\beta}=\frac{\alpha-1}{3-\alpha}.
\]
At \(\beta=0\) the expression is independent of \(u\). Substitution yields the exact fixed-cut bound
\[
F_{k,h}=\frac{4(kh)^{1-\beta}}{(k^\gamma+h^\gamma)^{1+\beta}}
=\frac{4(kh)^{\alpha-1}}{(k^\gamma+h^\gamma)^{3-\alpha}}.
\]
This also bounds cut supports with vanished coordinates because they are limits of positive-simplex probability vectors and the Jacobian estimate cannot exceed the full-support supremum.

**4. The balanced-cut theorem.** With \(n\) fixed, put \(x=k/h\in(0,1]\). A direct logarithmic derivative of the continuous relaxation is
\[
\frac{d}{dx}\log F_{nx/(1+x),\,n/(1+x)}
=\frac{(\alpha-1)(1-x^{1+\gamma})}{x(1+x)(1+x^\gamma)}.
\]
It is strictly positive for \(0<x<1\). Symmetry under exchanging the blocks therefore forces the maximizing integer cut to have sizes \(m=\lfloor n/2\rfloor\) and \(\ell=\lceil n/2\rceil\), with no other sizes maximizing except the complementary tie. For even \(n\), substituting equal block sizes gives \(n^{\alpha-1}\); for odd \(n\), strict monotonicity gives a strict deficit relative to the unattainable equal-sized continuous cut.

**5. Equality and global sharpness.** Choose the two-block interior probability vector specified in the Finding, and an input score vector realizing it by step 1. Its Jacobian has norm exactly \(L_{n,\alpha}\) by steps 2–4; an arbitrarily small score perturbation in the corresponding opposite-sign direction gives a quotient tending to \(L_{n,\alpha}\). At \(\alpha=2\), use any interior probability and balanced sign direction. Together with step 1's global integration, this proves equality of the global Lipschitz constant and the claimed expression, including all stated boundary cases.

## Verification

The derivation is self-contained once the standard finite-dimensional convex-optimality and duality statements are accepted. The standalone script \(`verify.py`\) checks the norm identity by exhaustive sign vectors for \(2\le n\le9\), compares 5 exponent values and many interior probability vectors to the claimed sharp bound, verifies analytic attaining probabilities, and separately tests finite differences of a threshold-equation implementation of the probability map. It reported 11,040 deterministic supplementary assertions. The script uses only Python's standard library; run \(`python3 verify.py`\) from an extracted package. No finite experiment is used to establish the all-dimensional formula.

## Relationship to prior work

The Tsallis family and its normalization are introduced and analyzed by Blondel, Martins and Niculae (2018), while Peters, Niculae and Martins (2019), especially Appendix B, explicitly derive the general separable-entropy Jacobian formula used in proof step 1. Accordingly neither the variational construction nor that Jacobian is claimed to be new. The present statement additionally optimizes its cross-norm over *all* simplex outputs and *all* signed directions, proves the balanced-cut rigidity and exact odd/even dimension law, and supplies attaining score directions. The ordinary same-exponent softmax \(\ell_p\) bounds and sharp simplex-projection results in other norms do not give the heterogeneous \(\ell_\infty\)-to-\(\ell_1\) Tsallis formula without the new optimization.

## Limitations

The result is confined to finite dimensions and \(1<\alpha\le2\). The strict equality-pattern assertion refers to interior outputs and \(1<\alpha<2\); boundary outputs may have different active-set degeneracies and were not exhaustively classified as extremizers. No claim is made about weighted or temperature-scaled variants or over-composed network blocks. An unlocated earlier statement expressed in conjugate-smoothness or simplex-cut language remains a possible priority risk; mathematical correctness does not prove priority, and no independent mathematical review has been performed.

## References

1. Mathieu Blondel, André F. T. Martins, Vlad Niculae. *Learning Classifiers with Fenchel-Young Losses: Generalized Entropies, Margins, and Algorithms*. arXiv:1805.09717 (first public 2018-05-24). https://arxiv.org/abs/1805.09717
2. Ben Peters, Vlad Niculae, André F. T. Martins. *Sparse Sequence-to-Sequence Models*. arXiv:1905.05702 (first public 2019-05-14). See especially Section 3 and Appendix B. https://arxiv.org/abs/1905.05702
3. André F. T. Martins, Ramón F. Astudillo. *From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification*. arXiv:1602.02068 (2016), earlier special endpoint. https://arxiv.org/abs/1602.02068
4. Pravin Nair. *Softmax is 1/2-Lipschitz: A tight bound across all ℓp norms*. arXiv:2510.23012 (2025), same-exponent norms of the softmax endpoint, not a covering cross-norm theorem. https://arxiv.org/abs/2510.23012
