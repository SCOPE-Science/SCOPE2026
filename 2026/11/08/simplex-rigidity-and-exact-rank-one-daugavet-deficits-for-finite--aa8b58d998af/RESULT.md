# Simplex rigidity and exact rank-one Daugavet deficits for finite orthogonal actions

## Finding

For a real Euclidean space \(H\) of dimension \(d\ge 2\) and a finite group \(G\le O(H)\), put
\[
\mathcal D_G(t)=\min_{u,v\in S_H}\max_{g\in G}\|I+t(gu)\otimes v\|,\qquad t>0,
\]
where \((w\otimes v)x=\langle x,v\rangle w\). Thus \(\mathcal D_G(t)\) is the smallest possible group-optimized norm of an identity plus a rank-one operator of norm \(t\).

Define
\[
\eta_G=\min_{u,v\in S_H}\max_{g\in G}\langle gu,v\rangle,\qquad
\Psi_t(c)=\sqrt{1+tc+\frac{t^2}{2}+\frac t2\sqrt{t^2+4+4tc}}.
\]
**The sharp operator-to-orbit identity** is
\[
\boxed{\mathcal D_G(t)=\Psi_t(\eta_G).}
\]
For every finite, real-irreducible orthogonal group on \(H\),
\[
\boxed{\eta_G\ge \frac1d,\qquad \mathcal D_G(t)\ge\Psi_t(1/d).}
\]
Equality in either inequality occurs if and only if some unit-vector orbit \(G\cdot u\) is exactly the set of \(d+1\) vertices of a regular simplex on \(S_H\). In the equality case the minimizing pairs are precisely those with \(u\) on such an orbit and \(v=-gu\) for some \(g\in G\). This is a rigidity statement for the sharp dimension bound, not merely an existence example.

Three natural families admit exact values, uniformly for every \(t>0\):

1. For the standard permutation representation of \(S_{d+1}\) on \(H=\{x\in\mathbb R^{d+1}:\sum_i x_i=0\}\),
\[\boxed{\mathcal D_{S_{d+1}}(t)=\Psi_t(1/d).}\]
2. For the signed-permutation (hyperoctahedral) group \(B_d\) on \(\mathbb R^d\), \(d\ge2\),
\[\boxed{\mathcal D_{B_d}(t)=\Psi_t(1/\sqrt d).}\]
The optimal rank-one directions are a coordinate vector and a normalized all-ones vector, in either order after signed permutations.
3. For any finite subgroup of \(O(2)\), whose rotation subgroup has order \(m\ge1\) (cyclic or dihedral),
\[\boxed{\mathcal D_G(t)=\Psi_t(\cos(\pi/m)).}\]
In particular the cyclic and dihedral groups with the same rotational order have identical worst rank-one deficits, even though they have different orbit sizes for generic vectors.

At \(t=1\), both \(\mathcal D_{S_{d+1}}(1)\) and \(\mathcal D_{B_d}(1)\) tend to the golden ratio \((1+\sqrt5)/2\) as \(d\to\infty\); the rank-one Daugavet deficit therefore stays bounded away from zero despite the increasing group orders. Conversely, for the planar cyclic or dihedral actions,
\[
\boxed{2-\mathcal D_G(1)=\frac{\pi^2}{6m^2}+O(m^{-4})\quad(m\to\infty).}
\]

A compatible infinitesimal invariant is the restricted rank-one group numerical radius. With the same group convention as the operator equation, define \(v_G(T)=\sup_{g\in G,\|x\|=1}\langle T(gx),x\rangle\). Its infimum over norm-one rank-one operators equals \((1+\eta_G)/2\), hence \((1+1/d)/2\) for the standard permutation action and \((1+1/\sqrt d)/2\) for signed permutations. This does **not** assert an equality for the unrestricted group numerical index, whose infimum includes operators of arbitrary rank.

## Assumptions and scope

Everything is real and finite-dimensional. The orthogonal action is the one given, and the rank-one norm \(t\) is strictly positive. A group acting irreducibly means that it preserves no proper nonzero real linear subspace; the bound \(1/d\) is not claimed for reducible actions. For a planar finite orthogonal group, \(m\) is the order of its orientation-preserving rotation subgroup, including \(m=1\) for the trivial and one-reflection cases. The minimum is over all ordered unit pairs, with no equivariance or positivity restriction on the rank-one operator.

## Proof

**1. Rank-one singular values and monotonicity.** Write \(T=t w\otimes v\), where \(\|w\|=\|v\|=1\), and \(c=\langle w,v\rangle\). In the orthogonal plane spanned by \(v\) and the component of \(w\) perpendicular to \(v\), the matrix of \(I+T\) is
\[
\begin{pmatrix}1+tc&0\\t\sqrt{1-c^2}&1\end{pmatrix}.
\]
The squared singular values of this matrix have sum \(2+2tc+t^2\), product \((1+tc)^2\), and discriminant \(t^2(t^2+4+4tc)\). Its larger squared singular value is \(\Psi_t(c)^2\). On the orthogonal complement the operator is the identity, and \(\Psi_t(c)\ge1\), so the same norm formula holds even when the displayed plane degenerates. The function \(\Psi_t\) is strictly increasing on \([-1,1]\) for every \(t>0\). Taking first the maximum over \(g\) and then the minimum over unit \(u,v\) gives the first boxed identity.

**2. Irreducibility and the sharp simplex criterion.** Fix unit vectors \(u,v\). Let \(Z_g=\langle gu,v\rangle\) and \(M=\max_g Z_g\). Averaging \(gu\) over \(G\) gives zero, since an irreducible real action in dimension \(d\ge2\) has no fixed vector. The average of the self-adjoint rank-one operators \((gu)\otimes(gu)\) commutes with \(G\); its eigenspaces are invariant and thus it equals \(I/d\) by its trace. Consequently
\[
\frac1{|G|}\sum_g Z_g=0,\qquad \frac1{|G|}\sum_g Z_g^2=\frac1d.
\]
Because \(-1\le Z_g\le M\), the nonnegative factors \((Z_g+1)(M-Z_g)\) imply \(Z_g^2\le(M-1)Z_g+M\). On averaging this yields \(1/d\le M\). Since \(u,v\) were arbitrary, \(\eta_G\ge1/d\).

Equality forces every \(Z_g\) to be either \(-1\) or \(1/d\). Both values occur: their mean is zero and their variance is positive. Select \(g_0\) with \(Z_{g_0}=-1\), so \(v=-g_0u\). Thus every distinct point \(w\) in \(G\cdot u\) has inner product \(-1/d\) with \(g_0u\); transitivity of the orbit and orthogonality transfer the same statement to every distinct pair in the orbit. The orbit has exactly \(d+1\) points because its centroid is zero: if its cardinality is \(k\), taking the inner product of its sum with a vertex yields \(1-(k-1)/d=0\). Thus it is a regular simplex. Conversely, for a regular-simplex orbit take \(v=-u\); the orbit correlations are \(-1\) and \(1/d\), attaining the bound. This also characterizes all minimizing pairs.

**3. Standard permutation representation.** Put \(n=d+1\). The \(n\) unit vectors proportional to \(e_j-n^{-1}\mathbf1\) form one orbit under the coordinate-permutation group and have mutual inner products \(-1/d\). The action on the mean-zero hyperplane is irreducible: if a nonzero invariant subspace contains a nonconstant vector, coordinate transpositions produce the differences \(e_i-e_j\), which span that hyperplane. Apply step 2.

**4. Signed permutations.** For a unit vector \(u\in\mathbb R^d\) let \(u^\downarrow\) be the decreasing rearrangement of its absolute coordinates. Signed permutations independently align signs and orders, so
\[
\max_{g\in B_d}\langle gu,v\rangle=\sum_{i=1}^d u_i^\downarrow v_i^\downarrow.
\]
For any two decreasing nonnegative vectors \(a,b\), write \(a=\sum_{k=1}^d\alpha_k\mathbf1_{\{1,\ldots,k\}}\) and \(b=\sum_{l=1}^d\beta_l\mathbf1_{\{1,\ldots,l\}}\), with \(\alpha_k,\beta_l\ge0\). Since \(\min(k,l)\ge\sqrt{kl/d}\),
\[
\langle a,b\rangle=\sum_{k,l}\alpha_k\beta_l\min(k,l)
\ge\frac1{\sqrt d}\Big(\sum_k\alpha_k\sqrt k\Big)\Big(\sum_l\beta_l\sqrt l\Big)
\ge\frac{\|a\|_2\|b\|_2}{\sqrt d}.
\]
The last inequality is the triangle inequality. Equality is achieved by \(u=e_1\), \(v=\mathbf1/\sqrt d\); hence \(\eta_{B_d}=1/\sqrt d\). The endpoint equality conditions in the displayed comparison and triangle inequalities give the stated optimal directions, up to interchange and group symmetries.

**5. Planar finite actions and limits.** The rotational subgroup is cyclic of order \(m\). Every rotational orbit is a regular \(m\)-gon on the unit circle, so the largest scalar product with any unit \(v\) is at least \(\cos(\pi/m)\). For a cyclic group this lower bound is attained by pointing \(v\) halfway between adjacent orbit vectors. For a group containing reflections, take \(u\) along an axis of reflection; its whole orbit then equals its rotational orbit, giving equality. The expansion \(\cos(\pi/m)=1-\pi^2/(2m^2)+O(m^{-4})\) and \(\Psi_t'(1)=t/(t+2)\) imply \((1+t)-\mathcal D_G(t)=t\pi^2/(2(t+2)m^2)+O_t(m^{-4})\). Set \(t=1\). For type A and type B, the correlation parameters tend to zero and \(\Psi_1(0)=(1+\sqrt5)/2\).

**6. Rank-one numerical radius.** On a real Hilbert space, \(\sup_{\|x\|=1}\langle T(gx),x\rangle\) is the largest eigenvalue of the symmetric part of \(Tg\). For a norm-one rank-one \(T=u\otimes v\), its nonzero two-plane eigenvalues are \((\langle gu,v\rangle\pm1)/2\). Maximizing in \(g\), then minimizing in the unit vectors, proves the stated restricted-index formulas. Replacing \(Tg\) by \(gT\) does not alter the orbit-correlation maximum because \(g\) ranges over a group.

## Verification

An accompanying independently executable finite checker (`verify_orthogonal_actions.py`) tests the exact two-by-two trace, determinant and discriminant identities symbolically; explicitly computes simplex orbit correlations; and checks representative operator norms and signed-permutation and planar rotation extremizers numerically. It is corroborative, not a proof for infinitely many dimensions, groups, or perturbation parameters. All universal statements are proved in the preceding section.

## Relationship to prior work

Dantas, del Río, and Raunig introduce the group-action Daugavet identity and prove a qualitative equivalence between the property and almost transitivity for locally uniformly rotund spaces (Theorem 3.3); their finite-versus-dense rotation example is Example 3.14. Their Definitions 4.12 and Lemma 4.16 develop a group numerical-radius criterion, and Section 5.2 gives a different quantitative estimate conditioned on already having the group-Daugavet property. The present theorem instead computes the **least value over all rank-one operators of prescribed norm** for finite groups that fail the property, with a sharp dimension bound, equality classification and exact formulas for the standard and signed-permutation actions. General results on regular simplices and orbit polytopes are used as geometric context; the elementary simplex and rearrangement ingredients are not individually claimed as new.

## Limitations

The claims concern real Euclidean geometry, finite orthogonal groups, and rank-one perturbations only. They do not calculate the unrestricted group numerical index or analogous constants for arbitrary Banach spaces or complex actions. An earlier equivalent formulation using orbit support functions or rank-one numerical indices could affect publication priority; no assertion of exhaustive historical priority is made.

## References

1. S. Dantas, H. del Río, T. Raunig, *A group action approach to the Daugavet property*, arXiv:2606.20429v1 (first public 2026-06-18); https://arxiv.org/abs/2606.20429.
2. S. Simon, T. Timofeyev, *Inscribed Tverberg-Type Partitions for Orbit Polytopes*, arXiv:2110.09322 (2021); https://arxiv.org/abs/2110.09322.
3. M. Martín, *The alternative Daugavet property of C*-algebras and JB*-triples*, Mathematische Nachrichten (2008), DOI:10.1002/mana.200510608 (background on alternative Daugavet equations).
