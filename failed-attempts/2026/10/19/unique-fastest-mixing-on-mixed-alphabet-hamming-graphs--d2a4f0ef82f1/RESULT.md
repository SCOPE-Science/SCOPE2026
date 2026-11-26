# Unique fastest mixing on mixed-alphabet Hamming graphs

## Finding

**Theorem (global rigidity, exact spectral optimum and holding transition).** Let \(d\ge2\) and let \(q_1,\ldots,q_d\ge2\) be arbitrary integers. On the Cartesian product \(G=K_{q_1}\square\cdots\square K_{q_d}\), let \(\mathcal P(G)\) be the set of all real symmetric, entrywise nonnegative, row-stochastic matrices with off-diagonal support contained in the edges of \(G\). Self-loops are permitted. Define
\[
 S=\sum_{i=1}^d\left(1-\frac1{q_i}\right),\qquad
 t=\min\left\{\frac2{d+1},\frac1S\right\}.
\]
Then the minimizer of the second-largest eigenvalue modulus over **all** matrices in \(\mathcal P(G)\) is **unique**. It assigns probability \(t/q_i\) to every edge changing the \(i\)-th coordinate and probability \(h=1-St\) to every self-loop. Its optimal second-largest eigenvalue modulus is
\[
 \boxed{\mu_*=1-t.}
\]
In particular, an optimal walk has a strictly positive holding probability if and only if
\[
 \sum_{i=1}^d\frac1{q_i}>\frac{d-1}{2};
\]
otherwise it has zero holding probability. At equality the optimal walk is still unique.

**Alphabet universality.** For \(G=K_2^{\square(d-1)}\square K_q\), any \(d\ge2\) and any \(q\ge2\), the optimal modulus is \((d-1)/(d+1)\), independent of \(q\), and the unique optimal holding probability is \(2/((d+1)q)\). In particular every \(K_2\square K_q\), however large \(q\) is, has optimum \(1/3\).

## Assumptions and scope

The graph has \(N=\prod_iq_i\) vertices, indexed by tuples of symbols. Distinct vertices are adjacent exactly when they differ in one coordinate. Different permissible edges may initially carry entirely independent probabilities; no invariance or product-chain assumption is imposed. For \(P\in\mathcal P(G)\), write \(\mu(P)=\|P-J_N/N\|_2\), with \(J_N\) the all-ones matrix. This equals the maximum absolute eigenvalue of \(P\) on the subspace orthogonal to constants, even when the chain is reducible. All parameter inequalities include endpoints and are exact. The result concerns symmetric time-homogeneous chains and the uniform stationary measure, not arbitrary reversible measures, nonsymmetric chains or fastest finite-time total-variation mixing.

## Proof

**1. Legitimate symmetry reduction.** For each factor, independently permute its \(q_i\) symbols. Conjugating a feasible \(P\) by any such permutation preserves nonnegativity, stochasticity and edge support. Since \(P\mapsto\|P-J_N/N\|_2\) is convex, averaging over \(\prod_iS_{q_i}\) produces a feasible symmetry-invariant matrix with no worse modulus. Each edge orbit consists precisely of the edges that change one specified coordinate. Thus a symmetry-invariant matrix has common off-diagonal edge weights \(w_i\ge0\) in direction \(i\) and common holding probability \(1-\sum_i(q_i-1)w_i\ge0\).

**2. The exact reduced spectrum.** Put \(x_i=q_iw_i\) and \(\alpha_i=(q_i-1)/q_i\). The stochasticity constraint is \(\sum_i\alpha_ix_i\le1\). The transition operator equals
\[
 P=I-\sum_{i=1}^d w_i\bigl(I\otimes\cdots\otimes(q_iI_{q_i}-J_{q_i})\otimes\cdots\otimes I\bigr).
\]
The tensor decomposition into constants and mean-zero vectors in each factor gives eigenvalue \(1-\sum_{i\in A}x_i\) for every subset \(A\subseteq\{1,\ldots,d\}\), of multiplicity \(\prod_{i\in A}(q_i-1)\). The empty subset is the constant eigenvalue. Because all \(x_i\ge0\), the largest nonconstant eigenvalue is \(1-\min_i x_i\) and the smallest is \(1-\sum_i x_i\). Hence the exact reduced objective is
\[
 \mu=\max\left\{1-\min_i x_i,\ \sum_i x_i-1\right\}.
\]
This formula remains valid when some nonconstant eigenvalues are repeated or equal to one.

**3. Sharp lower bounds and attainment.** If a feasible reduced matrix has modulus at most \(u\), then every \(x_i\ge1-u\) and \(\sum_i x_i\le1+u\). Summing the first inequalities yields \(d(1-u)\le1+u\), hence \(u\ge(d-1)/(d+1)\). The stochasticity constraint also gives \(1\ge\sum_i\alpha_ix_i\ge S(1-u)\), so \(u\ge1-1/S\). Together these say \(u\ge1-t\). Taking every \(x_i=t\) is feasible because \(tS\le1\), and its nonconstant eigenvalues are \(1-kt\) for \(1\le k\le d\). Since \(t\le2/(d+1)\), both \(1-t\ge dt-1\) and \(1-t\ge|1-dt|\), and therefore \(\mu=1-t\). This attains the lower bound.

**4. Uniqueness among invariant matrices.** Any invariant optimizer has \(x_i\ge t\). If \(t=1/S\), feasibility gives \(1\ge\sum_i\alpha_ix_i\ge tS=1\); as every \(\alpha_i>0\), all \(x_i=t\). If instead \(t=2/(d+1)\), then \(\sum_ix_i\le1+\mu_*=2d/(d+1)=dt\), again forcing all \(x_i=t\). These arguments cover equality of the two bounds. Thus the averaged optimum is the stated \(P_*\) and is the only invariant optimum.

**5. Rigidity of every unrestricted optimum.** Let \(P\) be any optimum and average its coordinate-symbol conjugates to obtain \(P_*\). For a fixed \(i\), let \(U_i\) consist of vectors that depend only on coordinate \(i\) and have mean zero in that coordinate. Every \(u\in U_i\) satisfies \(P_*u=(1-t)u=\mu_*u\). For each conjugate \(P_g\), the quadratic form of \(\mu_*I-P_g\) is nonnegative on the orthocomplement of constants, by the definition of the SLEM. Its average quadratic form at \(u\) is zero. Since each summand is nonnegative, the identity conjugate has zero quadratic form. Positive semidefiniteness on that subspace implies \(Pu=\mu_*u\) for every \(u\in U_i\).

Fixing the other \(d-1\) coordinate values gives a fiber isomorphic to \(K_{q_i}\). If \(u\in U_i\), jumps in all other directions contribute zero to \((I-P)u\); its restriction to this fiber is exactly the weighted Laplacian of the fiber. Therefore each fiber Laplacian acts as \(tI\) on all mean-zero vectors and kills constants, hence equals \(t(I_{q_i}-J_{q_i}/q_i)\). Its off-diagonal entries force every edge weight in this fiber to equal \(t/q_i\). This holds for every coordinate and every fiber. Stochasticity then fixes all diagonal entries. Thus \(P=P_*\). No distinct nonsymmetric optimal matrix exists.

**6. Holding and universality.** Since \(h=1-St\), strict holding occurs exactly when \(S<(d+1)/2\), which is equivalent to \(\sum_i1/q_i>(d-1)/2\). For \((q_1,\ldots,q_d)=(2,\ldots,2,q)\), \(S=(d+1)/2-1/q\), so \(t=2/(d+1)\), \(h=2/((d+1)q)\), and \(\mu_*=(d-1)/(d+1)\), as claimed.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to construct candidate transition matrices and derive all predicted eigenvalues from the tensor-subset spectrum. It compares those eigenvalues to independent numerical symmetric-matrix diagonalization for mixed tuples of two to four factors. A separate linear-program formulation verifies every unequal two-factor instance in a finite rectangular parameter grid. Random non-invariant feasible weighted matrices are checked as additional sanity tests. Running `python verify.py` with the dependencies in `requirements.txt` produced `VERIFY_OK 31124 checks`. None of the finite checks establishes the theorem for unbounded dimensions; the preceding six proof steps do.

## Relationship to prior work

Boyd, Diaconis and Xiao introduced the SLEM minimization and SDP viewpoint for symmetric Markov chains on arbitrary graphs [1]. Boyd, Diaconis, Parrilo and Xiao gave symmetry averaging, Cartesian-product spectra, and an exact formula for **equal-alphabet** Hamming graphs, together with many edge-transitive examples [2, §§2–3.3]. The known hypercube and equal-alphabet Hamming optimal values are recovered here and are not claimed new. The present theorem addresses arbitrary heterogeneous coordinate alphabets and, more importantly, **uniqueness among all individual-edge assignments**, not merely existence of a symmetry-invariant optimizer. Its proof uses saturation of maximal eigenspaces to force every individual edge weight, a point not established by convex averaging alone. A later association-scheme optimization study [3] addresses equal-alphabet Hamming relations and general scalar LP reductions; its inspected Hamming sections do not give the mixed-alphabet rigidity theorem.

## Limitations

The result does not claim faster finite-time total-variation mixing, robustness to perturbed stationary measures, or results for directed/nonreversible chains. Its novelty depends on the claim-level distinction from the general spectral/SDP machinery in [1,2] and later association-scheme research [3]. A differently named or unindexed mixed-product theorem might cover it; the mathematical proof stands independently of that literature risk. The general SDP framework might also make some parts of the scalar solution readily derivable, so the unrestricted uniqueness assertion is central to the substantive contribution.

## References

[1] S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689, DOI: 10.1137/S0036144503423264; accessible author PDF: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/SIREV042326-1.pdf.

[2] S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1, first posted 2007-09-06, https://arxiv.org/abs/0709.0955; SIAM Journal on Optimization **20** (2009), 792–819.

[3] S. Jafarizadeh, *Pareto-Optimal Design of Markov Chains on Networks Based on Association Schemes*, IEEE Access **14** (2026), DOI: 10.1109/ACCESS.2026.3680803, accessible author text at https://www.researchgate.net/publication/404746370_Pareto-Optimal_Design_of_Markov_Chains_on_Networks_Based_on_Association_Schemes.
