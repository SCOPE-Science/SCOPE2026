# Exact fixed-basis positivity and moment feasibility for low-rank kinetic corrections

## Finding

**Theorem (complete mass–moment feasibility and rank-one witness).** Let \(m,n\ge 2\), \(1\le r\le\min(m,n)\), and let \(X\in\mathbb R^{m\times r}\) and \(V\in\mathbb R^{n\times r}\) have full column rank. Fix strictly positive spatial and velocity quadrature weights \(a\in\mathbb R_{>0}^m\), \(b\in\mathbb R_{>0}^n\), velocity nodes \(v_j\in\mathbb R^d\), a prescribed mass \(M>0\), and prescribed global momentum \(J\in\mathbb R^d\). Put \(U=\operatorname{col}(X)\), \(W=\operatorname{col}(V)\), and

\[
\mathcal P_W=\{w\in W\cap\mathbb R_+^n:b^\mathsf Tw=1\},\qquad
\mathcal B_W=\left\{\sum_{j=1}^n b_jw_jv_j:w\in\mathcal P_W\right\}.
\]

There exists an unrestricted real core matrix \(S\in\mathbb R^{r\times r}\) with \(F=XSV^\mathsf T\) entrywise nonnegative, weighted mass \(\sum_{i,j}a_ib_jF_{ij}=M\), and weighted momentum \(\sum_{i,j}a_ib_jv_jF_{ij}=J\) **if and only if**

\[
\boxed{U\cap\mathbb R_+^m\ne\{0\}\quad\text{and}\quad J/M\in\mathcal B_W.}
\]

Whenever these conditions hold, a feasible \(S\) exists for which \(F\) has matrix rank exactly one. The feasibility decision therefore reduces to two separate linear programs in \(r\) unknowns, rather than a joint system involving \(r^2\) core unknowns. Every feasible quadratic correction problem \(\min_S\|S-\widetilde S\|_F^2\) has a unique minimizer.

**Sharp finite characterization.** If \(W\) has dimension \(r\), the nonempty polytope \(\mathcal P_W\) has vertices supported on at most \(n-r+1\) velocity nodes. For codimension one, \(W=\{w:c^\mathsf Tw=0\}\), \(c\ne0\), the attainable moment polytope \(\mathcal B_W\) is **exactly** the convex hull of the following points: each \(v_i\) with \(c_i=0\), and for each pair \(c_i>0>c_j\),

\[
\boxed{\mu_{ij}=\frac{(-c_j)b_iv_i+c_ib_jv_j}{(-c_j)b_i+c_ib_j}.}
\]

If neither type of point exists, the reduced positive moment set is empty. These are exact attainability boundaries, not approximations.

**Minimal one-direction feasibility completion.** Assume the prescribed mean \(\mu=J/M\) is physically admissible, i.e. \(\mu\in\operatorname{conv}\{v_1,\dots,v_n\}\). If the spatial factor space has no nonzero nonnegative vector, adjoining one strictly positive spatial vector repairs that obstruction, and at least one new direction is necessary. If \(\mu\notin\mathcal B_W\), adjoining any **nonzero nonnegative** velocity vector \(w_0\) with \(\sum b_j(w_0)_jv_j=\mu\sum b_j(w_0)_j\) repairs the velocity obstruction, and at least one new direction is necessary. Such a vector exists by physical admissibility. Here “adjoining” means enlarging the respective factor **space**; a rectangular core may be used when only one side is enlarged. Once both obstructions are absent or repaired, the resulting feasible physical matrix still has rank one.

## Assumptions and scope

All matrices are real; the core \(S\) can be rank deficient, and entrywise positivity means \(F_{ij}\ge0\). Spatial and velocity quadrature weights are strictly positive. The claim concerns only global mass and global momentum constraints. For the exact correction problem motivating the result, the quadrature is uniform, so the weights can be set to one after absorbing a common constant into the mass and momentum. No restriction on the initial uncorrected core \(\widetilde S\) is necessary for feasibility. The velocity nodes may be multidimensional or repeated.

For strict positivity \(F_{ij}>0\), the analogous criterion replaces both nonnegative-vector requirements by strictly positive-vector requirements; however, the statement does **not** address a prescribed numerical floor \(F_{ij}\ge\varepsilon>0\) or optimization with an imposed exact rank of \(S\).

## Proof

**1. Necessity via nonnegative marginals.** Let \(F=XSV^\mathsf T\ge0\) meet the constraints. Define the spatial marginal \(u=Fb\) and the velocity marginal \(z=F^\mathsf Ta\). Since the quadrature weights are positive and \(M=a^\mathsf Tu=b^\mathsf Tz>0\), both marginals are nonzero and nonnegative. Their factor representations imply \(u\in U\), \(z\in W\). Then \(w=z/M\in\mathcal P_W\), and

\[
\sum_j b_jw_jv_j=M^{-1}\sum_jb_jz_jv_j=J/M.
\]

This proves both necessary conditions without assuming that the physical matrix is rank one.

**2. Sufficiency and minimal matrix rank.** Choose any \(0\ne u=X\xi\in U\cap\mathbb R_+^m\) and any \(w=V\zeta\in\mathcal P_W\) realizing \(\mu=J/M\). Because \(a>0\), one has \(a^\mathsf Tu>0\). Set

\[
S=\frac{M}{a^\mathsf Tu}\,\xi\zeta^\mathsf T,\qquad
F=\frac{M}{a^\mathsf Tu}\,uw^\mathsf T.
\]

Every entry of \(F\) is nonnegative, its mass is exactly \(M\), and its momentum is \(M\mu=J\). Since both factors are nonzero, \(\operatorname{rank}(F)=1\). The feasible set of core matrices is an intersection of a closed affine space with finitely many closed half-spaces. The strictly convex coercive quadratic \(\|S-\widetilde S\|_F^2\) therefore has a unique minimizer whenever the feasible set is nonempty.

**3. Finite support bound.** If \(\mathcal P_W\ne\varnothing\), write its affine equations as \(Cw=0\), \(b^\mathsf Tw=1\), where the \(n-r\) rows of \(C\) form a basis of \(W^\perp\). Since a feasible vector has positive \(b\)-mass, \(b^\mathsf T\) is independent of the rows of \(C\); the stacked constraint matrix has rank \(n-r+1\). At any vertex of the nonnegative solution polytope, the columns corresponding to positive entries must be linearly independent; otherwise a small signed perturbation supported there preserves all equations and nonnegativity, contradicting extremality. Hence each vertex has at most \(n-r+1\) positive entries. The polytope is compact because \(b>0\), so its image under the moment map is the convex hull of its finitely many vertices.

**4. The codimension-one hull.** Here the affine constraints are \(c^\mathsf Tw=0\) and \(b^\mathsf Tw=1\). A vertex has support at most two. A singleton vertex at node \(i\) is possible exactly when \(c_i=0\), yielding barycenter \(v_i\). A two-node vertex with both entries strictly positive requires opposite nonzero signs of \(c_i\) and \(c_j\). Solving the two constraints gives

\[
w_i=\frac{-c_j}{(-c_j)b_i+c_ib_j},\qquad
w_j=\frac{c_i}{(-c_j)b_i+c_ib_j},
\]

and all other entries zero. Both fractions are positive and uniquely defined. Their barycenter is exactly \(\mu_{ij}\). Conversely all listed singleton and opposite-sign pair weights are feasible vertices. Therefore their image points generate the **whole** attainable moment polytope, including its boundary.

**5. Minimal factor-space completion.** Physical admissibility of \(\mu\) provides a nonzero nonnegative vector with barycenter \(\mu\): take the nonnegative convex weights representing \(\mu\) and divide them by \(b_j\). For any \(w_0\) as in the theorem, its nonnegativity, nonzero value, and \(b>0\) imply \(b^\mathsf Tw_0>0\). If the original velocity condition fails, \(w_0\notin W\), since otherwise normalization by \(b^\mathsf Tw_0\) would put \(\mu\) in \(\mathcal B_W\). Hence \(W+\operatorname{span}\{w_0\}\) has dimension exactly \(r+1\) and now satisfies the velocity condition. This condition depends only on the velocity space, so zero added velocity dimensions cannot repair that obstruction. If the spatial condition fails, a strictly positive vector \(u_0\) cannot lie in \(U\); adjoining it adds exactly one spatial direction and makes the spatial condition hold. The product witness from Step 2 applies once both conditions hold. These minimality statements concern additional factor-space directions, not the rank of the physical matrix.

**6. An exact three-velocity obstruction despite a mass-and-momentum basis.** Take \(v=(-1,0,1)\), unit quadrature weights, \(X=[(1,1,1)^\mathsf T,(1,-1,0)^\mathsf T]\), and \(V=[(1,1,1)^\mathsf T,(-1,0,1)^\mathsf T]\). Thus \(W=(1,-2,1)^\perp\), which contains both the constant and the velocity vector and contains a strictly positive vector. Any normalized \(w\in\mathcal P_W\) has

\[
w=\left(\frac13-\frac\mu2,\frac13,\frac13+\frac\mu2\right),
\qquad \mu\in[-2/3,2/3].
\]

The interval \([-2/3,2/3]\) is exact. But \(\mu=3/4\) lies inside the full physical velocity hull \([-1,1]\) and cannot be achieved by any entrywise nonnegative \(XSV^\mathsf T\) while these factor spaces remain fixed. Adjoining the strictly positive velocity vector \((1/12,1/12,5/6)^\mathsf T\), which has barycenter \(3/4\), restores feasibility with exactly one extra velocity direction.

## Verification

The finite verifier `verify.py` checks the exact three-velocity boundaries, constructs feasible rank-one witnesses, verifies that one augmented velocity direction repairs the missed mean, and compares the full-core linear program against the two-factor feasibility tests for pseudorandom integral bases and positive nonuniform quadrature weights. Execute `python verify.py` with NumPy and SciPy. The reference execution returned `VERIFY_OK canonical_means=8 random_full_core_vs_factor=390 weighted_LP_matches=158 exact_pair_checks=9`. This is supporting finite evidence; Steps 1–6 are the universal proof.

## Relationship to prior work

Kormann–Nazarov–Wen (2026) formulate an entrywise positivity correction with prescribed mass and momentum as a convex quadratic program in the low-rank core. Their Section 4 describes feasibility concerns and possible rank enrichment, without the factorized if-and-only-if criterion, codimension-one moment hull, or exact one-direction completion given here. Einkemmer–Ostermann–Scalone (2023) instead design a conservative integrator with collision-invariant velocity basis functions; guaranteeing evolution of moment equations for compatible states is different from deciding whether arbitrary target moments admit an entrywise nonnegative matrix in a fixed pair of factor spaces. The key proof here uses the product-of-marginals rank-one witness and basic polyhedral geometry; such ingredients are classical, and the historical novelty claim is limited to the specific fixed-basis feasibility classification and its quantitative consequences for this correction problem.

The related note [*Sharp momentum-feasibility cones for affine and quadratic velocity factors*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-momentum-feasibility-cones-for-affine-and-quadratic-veloci--66e2dee77c04/RESULT.md) uses a velocity marginal and a product witness with the constant spatial vector for polynomial factors on an equally spaced, equally weighted scalar grid. Its affine three-node interval is the same \([-2/3,2/3]\) interval computed in Step 6; that interval is an illustration, not a separate originality claim. The arbitrary factor spaces and positive quadratures, the separate spatial obstruction, the general codimension-one hull, and target-specific factor-space completion are not covered by the note's polynomial-grid formulas.

## Limitations

The result is a feasibility and existence theorem, not a convergence, accuracy, stability, or cost bound for a kinetic evolution scheme. The explicitly constructed feasible core need not be the **least perturbative** corrected core; the minimizer remains a quadratic-programming question. The theorem covers global moments, not cellwise mass/momentum, prescribed energy including field energy, arbitrary additional linear constraints, strict positive floors, or fixed exact core rank. Retaining all old factor directions through a one-sided augmentation may require a rectangular core before re-factorization. The standard polytope tools used in the proof may appear in other mathematical literature not identified by the searches; independent priority verification is not claimed.

## References

1. K. Kormann, M. Nazarov, J. Wen, *Positivity-preserving dynamical low-rank methods for the Vlasov equation*, arXiv:2606.31662v1 (first publicly released 2026-06-30), https://arxiv.org/abs/2606.31662.
2. L. Einkemmer, A. Ostermann, C. Scalone, *A robust and conservative dynamical low-rank algorithm*, arXiv:2206.09374 (2022); Journal of Computational Physics 484 (2023), 112060, https://arxiv.org/abs/2206.09374.
3. L. Einkemmer, I. Joseph, *A mass, momentum, and energy conservative dynamical low-rank scheme for the Vlasov equation*, Journal of Computational Physics 443 (2021), 110495, https://doi.org/10.1016/j.jcp.2021.110495.
