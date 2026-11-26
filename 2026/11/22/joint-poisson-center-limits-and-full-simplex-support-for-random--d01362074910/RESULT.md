# Joint Poisson-center limits and full-simplex support for random smallest enclosing balls

## Finding

**Theorem.** Fix an integer \(d\ge 2\), constants \(\alpha,c>0\), and i.i.d. points \(X_1,X_2,\ldots\) in the closed Euclidean unit ball of \(\mathbb R^d\). Assume the law is spherically symmetric and absolutely continuous, and its radial variable \(\rho=\|X_1\|\) satisfies
\[
\Pr(\rho>1-t)=ct^\alpha(1+o(1))\quad(t\downarrow0).
\]
Set \(b_n=(cn)^{-1/\alpha}\). Let \(C_n\) and \(R_n\) be the unique center and the radius of the smallest enclosing ball of the first \(n\) sample points. Let \(K_n\) be the number of distinct sample points lying exactly on its boundary.

Let \(N\) be the Poisson point process on \(\mathbb S^{d-1}\times(0,\infty)\) with intensity
\[
\sigma_{d-1}(du)\,\alpha s^{\alpha-1}\,ds,
\]
where \(\sigma_{d-1}\) is probability-uniform measure on the unit sphere. Define the random concave lower envelope
\[
F(z)=\inf_{(u,s)\in N}\{s+u\cdot z\},\qquad z\in\mathbb R^d.
\]
Almost surely, \(F\) attains its finite maximum \(H\) at a **unique** point \(Z\). Exactly \(d+1\) Poisson atoms satisfy \(s+u\cdot Z=H\); their directions are affinely independent and the origin is in the interior of their simplex. Moreover,
\[
\left(\frac{C_n}{b_n},\frac{1-R_n}{b_n}\right)
\ \Longrightarrow\ (Z,H),
\qquad
\Pr(K_n=d+1)\longrightarrow1.
\]
The vector \(Z\) has a rotation-invariant law and \(\Pr(Z=0)=0\). For a sample uniform in the unit \(d\)-ball the assumptions hold with \(\alpha=1\), \(c=d\), and \(b_n=(dn)^{-1}\).

The radius limit is known. In the uniform-ball case the joint center–radius limit also follows from a prior random-intersection limit combined with almost-sure uniqueness of the limiting incenter; see the comparison below. The contributions here are the uniqueness argument and joint limit for the general radial tail above, and the finite-sample support conclusion in higher dimensions under that same tail hypothesis. This does **not** establish support dominance under merely two-sided power bounds without a regular-variation limit.

## Assumptions and scope

All limits have fixed dimension \(d\); the number of points \(n\) tends to infinity. The law of the radial variable need not have a globally specified density, but spherical symmetry, absolute continuity, and the displayed one-term radial tail equivalence are required. The independent directions are uniform on \(\mathbb S^{d-1}\). The strict inequality in the radial tail is immaterial under absolute continuity. The number \(K_n\) counts *all* observations at the optimal sphere's boundary, not the size of a freely chosen support subset; the claim is that this number itself equals \(d+1\) with high probability.

The limiting linear program is the maximization of the *lower* envelope of affine functions, rather than minimization of an upper envelope. The signs in its definition follow by expanding the distances \(\|(1-b_ns)u-b_nz\|\). The limiting center is on scale \(b_n\), not the square-root scale suggested by a generic strong-convexity estimate.

## Proof

**1. Extremal point process.** Write \(X_i=\rho_iU_i\) with independent uniform directions and radial marks, and define \(S_{n,i}=(1-\rho_i)/b_n\). The tail assumption gives, for every \(s>0\),
\[
n\Pr(S_{n,i}\le s)\longrightarrow s^\alpha.
\]
Consequently the binomial point measure \(N_n=\sum_{i=1}^n\delta_{(U_i,S_{n,i})}\) converges vaguely in distribution on \(\mathbb S^{d-1}\times[0,\infty)\) to \(N\) with the displayed intensity. For fixed bounded intervals in the second coordinate, this follows directly from independent Bernoulli rare-event counts; disjoint intervals and angular sets yield independent Poisson limits. The limit has finitely many atoms below each finite depth threshold, no atoms at zero or any prescribed positive threshold, and independent diffuse angular coordinates.

**2. Angular shielding and existence.** Choose \(d+1\) small open spherical caps around the vertices of a regular simplex centered at zero. For a sufficiently small cap radius there is \(\kappa>0\) such that any choice of one direction from each cap obeys
\[
\min_j u_j\cdot v\le-\kappa\quad\text{for every unit }v.
\]
The Poisson intensity of each cap up to depth \(M\) grows like a positive multiple of \(M^\alpha\). Thus, with probability approaching one as \(M\to\infty\), each cap has an atom with depth at most \(M\). On that event,
\[
F(z)\le M-\kappa\|z\|.
\]
Since \(F(0)=\min_{(u,s)\in N}s>0\) almost surely and \(F\) is continuous on compact sets (see step 4), \(F\) has an attained, finite maximum. The cap property holds almost surely for some finite random \(M\), establishing coercivity without a deterministic bound on the optimizer.

For the finite sample, the analogous cap event has probability arbitrarily close to one for large \(n\) after choosing \(M\). Because the unit ball centered at the origin encloses the observations, \(R_n\le1\). If \(u\cdot C_n\le-\kappa\|C_n\|\) for a selected point \(x=(1-b_ns)u\), with \(s\le M\), then \(\|x-C_n\|\le1\) implies
\[
2\kappa(1-Mb_n)\|C_n\|\le 2Mb_n.
\]
It follows that \(C_n/b_n\) is tight. This argument is uniform over the selected angular caps and does not assume a rate of convergence of the Poisson process.

**3. The limiting active simplex is uniquely determining.** Let \(Z\) maximize \(F\) and put \(H=F(Z)\). Only atoms of depth at most \(H+\|Z\|+1\) can be active, so the active set is nonempty and finite. Its directions must have the origin in their convex hull. Indeed, otherwise the strict separation theorem gives a direction increasing all active affine functions; the finite slack to the remaining nearby atoms and the depth cutoff then permit a small improvement of \(F\), contradicting maximality.

For general position, restrict to depths at most a positive integer \(T\) and condition on the Poisson count. In an unordered sample representation the directions are independent uniform directions, and the depths are independent diffuse variables independent of the directions. Almost surely no set of at most \(d\) directions has zero in its convex hull, and any \(d+1\) lifted rows \((u_i,-1)\) are linearly independent. No \(d+2\) affine functions \(z\mapsto s_i+u_i\cdot z\) can meet at a common value: the first \(d+1\) rows and depths determine the only candidate and the last depth is diffuse conditional on those data and its direction. These properties hold simultaneously for all integer \(T\). The convex hull condition at an optimum yields at least \(d+1\) active constraints, while the no-common-value condition yields at most \(d+1\).

Hence precisely \(d+1\) constraints are active. Their directions form an affinely independent simplex containing zero in its interior, and in particular span \(\mathbb R^d\). If \(Z'\neq Z\) were another maximizer, each active affine function at the midpoint of \(Z,Z'\) would equal \(H\), while its endpoint values would both be at least \(H\). Affineness forces both endpoint values to equal \(H\), so every active direction would be orthogonal to \(Z-Z'\). Spanning gives \(Z=Z'\), a contradiction.

Finally, \(Z\neq0\) almost surely: at the origin the unique smallest-depth atom is the only active one, and its unit direction cannot have zero in its convex hull. Rotational invariance follows from uniqueness and the rotation-equivariance of the Poisson intensity.

**4. Uniform local convergence of objectives.** For \(z\in\mathbb R^d\), define
\[
F_n(z)=\min_{i\le n}\frac{1-\|X_i-b_nz\|}{b_n}.
\]
Then \(C_n/b_n\) maximizes \(F_n\) and \(\max_zF_n(z)=(1-R_n)/b_n\). For \(X_i=(1-b_ns)u\), and bounded \(s\) and \(\|z\|\), a uniform Taylor expansion gives
\[
\frac{1-\|(1-b_ns)u-b_nz\|}{b_n}
=s+u\cdot z+O(b_n).
\]
The deterministic triangle inequalities also give the global bounds \(s-\|z\|\le(1-\|X_i-b_nz\|)/b_n\le s+\|z\|\).

Fix a compact ball \(\|z\|\le L\). If an atom at depth at most \(A\) exists, all marks at depths greater than \(A+2L+1\) are uniformly irrelevant to either lower envelope. The remaining point configurations are finite and converge under standard local point-process couplings. The Taylor expansion and the minimum's Lipschitz property imply that \(F_n\) converges in law to \(F\) in the topology of uniform convergence on each compact ball. Angular shielding supplies tight optimizers, and step 3 supplies a unique limiting optimizer. The argmax continuous-mapping argument therefore yields the asserted *joint* limit for \((C_n/b_n,(1-R_n)/b_n)\).

**5. All \(d+1\) constraints survive for the actual enclosing ball.** Use a Skorokhod coupling for vague point-process convergence. Almost surely some finite integer depth cutoff supplies all shielding caps. Thus the compact objective convergence and the bound on the scaled optimizers hold eventually, on compact balls whose sizes may depend on the realization. Uniqueness gives optimizer convergence on this coupling. Choose a larger integer cutoff so that atoms above it cannot bind on the compact by the triangle bounds. At the limiting optimum every nonactive atom below the cutoff has positive slack; there are only finitely many to check. Local atom matching and convergence of the optimal objectives and centers imply that for sufficiently large \(n\), *every* finite boundary point belongs to the group of \(d+1\) observations corresponding to the limiting active atoms.

For the Euclidean minimum enclosing ball, first-order optimality of \(c\mapsto\max_i\|X_i-c\|\) states that the origin belongs to the convex hull of the outward unit vectors \((X_i-C_n)/R_n\) from its boundary points. A proper subset of the above \(d+1\) observations has at most \(d\) limiting directions and, by the general-position property in step 3, its convex hull remains separated from the origin for all sufficiently large \(n\). Such a proper subset cannot be the full boundary set. Therefore exactly \(d+1\) sample points lie on the minimum enclosing sphere eventually in the coupling. Convergence in distribution of the underlying configurations gives \(\Pr(K_n=d+1)\to1\).

## Verification

The derivations in steps 2--5 are analytical, not consequences of numerical experiments. The packaged `checker.py` tests the finite linear-envelope structure for dimensions 2, 3, and 4, with radial exponents 0.5, 1, and 2. It uses fixed-seed generated point configurations and checks optimality inequalities, exactly \(d+1\) active rows, strictly positive affine barycentric weights, and strict directional decreases away from each optimum. It passed 13,770 finite numerical checks on 810 configurations.

The packaged `meb_diagnostic.py` independently constructs planar minimum enclosing disks for uniform-ball samples and compares the scaled sample centers and radii with the linearized envelope. It passed 216 finite numerical checks. It observed 21, 22, and 24 three-point supports in 24 experiments with sizes 50, 150, and 400 respectively. These finite frequencies only illustrate the theorem, do not certify its asymptotic limit, and provide no uniform error bound.

For reproducibility, use Python with `numpy` and `scipy`, then run `python checker.py` and `python meb_diagnostic.py` from the containing directory. Neither checker is required as a premise of the analytical proof.

## Relationship to prior work

Henze and Klatt (2026, arXiv:2611.09726v1) establish Poisson-functional limits for the **radius** of the smallest enclosing ball in Gumbel, Fréchet and Weibull regimes. Their Weibull radius limit in Theorem 5.9 is the maximum of the same affine-Poisson envelope, up to normalization. Section 8(2) asks about convergence of the appropriately rescaled center, uniqueness of the Weibull maximizer, and joint convergence. Section 7.3 and Conjecture 7.6 address dominance of \(d+1\)-point support in higher dimensions. Their planar result already holds under broader hypotheses. The present result gives a joint limit with a unique maximizer for the stated radial tails and proves support dominance in every fixed dimension under regular variation, not under the full hypotheses of that conjecture.

There is earlier coverage of the uniform-ball pair by a convex-body limit. For \(A_n=\bigcap_{i=1}^n B(X_i,1)\), a ball of radius \(r\ge0\) centered at \(x\) is contained in \(A_n\) exactly when \(r+\max_i\|X_i-x\|\le1\). Thus the incenter and inradius of \(A_n\) are \(C_n\) and \(1-R_n\). Marynych and Molchanov (arXiv:2102.10009v3, Theorem 5.1) give Hausdorff convergence of the scaled intersection of translates for points uniform in a convex body. For the unit ball, reflection identifies their intersection with \(A_n\); their zero-cell intensity under scaling by \(n\) is \(d\,ds\,\sigma_{d-1}(du)\), which becomes \(ds\,\sigma_{d-1}(du)\) under scaling by \(dn\). The inball clearance in this zero cell is exactly \(F\). The inradius is continuous for the Hausdorff metric and the incenter is continuous at bodies with a unique incenter, by uniform convergence of the support functions and compactness of maximizing centers. The uniform-ball pair therefore follows from their body limit and the genericity of the Poisson constraints. Their global face-vector convergence (Theorem 6.1) does not count which constraints are tangent to the optimal inball. The support conclusion here uses stability at that specific optimum. Their uniform sampling theorem does not give the general radial-tail statement.

Classical extreme-value point-process convergence and finite-dimensional linear-programming genericity are proof ingredients, not newly claimed techniques. Mayer and Molchanov (2006) analyze maximum interpoint distances rather than random enclosing centers. Munteanu, Sohler and Feldman (2014) analyze algorithms for probabilistic enclosing balls rather than this rare-boundary asymptotic center law. General convergence-of-argmax principles are not themselves sufficient without the random affine-envelope uniqueness and support-stability verification established above.

## Limitations

This is a one-term weak-limit theorem in fixed dimension and supplies neither a closed form for the law of \(Z\) nor finite-sample rates. The radial tail needs genuine regular variation, so the result does not settle the broader conjecture under arbitrary oscillatory tails satisfying only two-sided power bounds. An angular law with atoms can produce multiple limiting optimizers and is excluded. Unindexed older equivalent results remain a possible priority risk.

## References

- N. Henze and M. Klatt (2026), *Extreme-value asymptotics for smallest enclosing balls of spherically symmetric samples*, arXiv:2611.09726v1, first posted 2026-11-06. https://arxiv.org/abs/2611.09726
- A. Marynych and I. Molchanov, *Facial structure of strongly convex sets generated by random samples*, arXiv:2102.10009v3. https://arxiv.org/abs/2102.10009
- M. Mayer and I. Molchanov (2006), *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, arXiv:math/0605289. https://arxiv.org/abs/math/0605289
- A. Munteanu, C. Sohler and D. Feldman (2014), *Smallest enclosing ball for probabilistic data*, ACM Symposium on Computational Geometry, doi:10.1145/2582112.2582114. https://doi.org/10.1145/2582112.2582114
- H. Ding (2019), *Minimum Enclosing Ball Revisited: Stability and Sub-linear Time Algorithms*, arXiv:1904.03796. https://arxiv.org/abs/1904.03796
