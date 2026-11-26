# Parity-sharp fastest mixing on cycle–clique cylinders

## Finding

For every integer \(n\geq 3\) and \(m\geq 2\), consider the Cartesian-product graph \(G_{n,m}=C_n\square K_m\), consisting of a ring of \(n\) copies of the \(m\)-vertex clique, joined between consecutive copies by coordinate-preserving perfect matchings. Among **all** symmetric, nonnegative, stochastic matrices \(P\) supported on its edges and diagonal, the exact minimum second-largest eigenvalue modulus (SLEM) is
\[
\mu_{n,m}^{*}=1-\Gamma_{n,m},\qquad
\Gamma_{n,m}=\min\left\{\frac{2s_n}{L_n+2s_n},\ \frac{m s_n}{2m+(m-1)s_n}\right\},
\]
where
\[
s_n=2\bigl(1-\cos(2\pi/n)\bigr),\qquad
L_n=2\bigl(1-\cos(2\pi\lfloor n/2\rfloor/n)\bigr).
\]
An optimal matrix assigns probability \(a_{n,m}=\Gamma_{n,m}/s_n\) along every cycle-coordinate edge and \(b_{n,m}=\Gamma_{n,m}/m\) along every edge within a clique. Its holding probability at every vertex is
\[
r_{n,m}=1-2a_{n,m}-(m-1)b_{n,m}\geq0.
\]
This matrix is the **unique optimal matrix invariant under the natural cycle-dihedral and simultaneous clique-permutation actions**; unrestricted global uniqueness is not claimed.

The formula exhibits an exact parity-dependent transition. If \(n\) is even, the first term in the minimum is active for every \(m\geq2\). If \(n=3\), the first term is active for \(2\leq m\leq6\), the second for \(m\geq6\), with equality of both at \(m=6\). If \(n\geq5\) is odd, the first term is active for \(2\leq m\leq7\), the second for \(m\geq8\). In the strict second-term regime the optimal holding probability vanishes. For every fixed \(m\),
\[
\Gamma_{n,m}\sim \frac{2\pi^2}{n^2}\qquad(n\to\infty).
\]
For \(m\geq3\), the maximum-degree or uniform-stationary Metropolis prescription gives every edge weight \(1/(m+1)\), and its spectral gap is asymptotically smaller by the factor
\[
\lim_{n\to\infty}\frac{\Gamma_{n,m}}{1-\mu_{n,m}^{\mathrm{Metropolis}}}=\frac{m+1}{2}.
\]
For \(m=2\), every even \(n\) yields a bipartite graph and this unmodified heuristic is periodic with SLEM exactly \(1\). For odd \(n\), the heuristic gap is exactly \(\tfrac23(1-\cos(\pi/n))\) and the optimal-to-heuristic gap ratio tends to \(6\) along odd \(n\to\infty\).

## Assumptions and scope

The cycle \(C_n\) is the simple undirected cycle, including the triangle when \(n=3\). The complete graph \(K_m\) has \(m\) vertices. The product has vertices \((i,j)\), for \(i\in\mathbb Z/n\mathbb Z\) and \(1\leq j\leq m\). There is a cycle edge between \((i,j)\) and \((i+1,j)\), and there is a clique edge between \((i,j)\) and \((i,k)\) for distinct \(j,k\). Each vertex has \(m+1\) neighbors. No direct jumps between nonadjacent vertices are permitted, but nonnegative holding probabilities are allowed.

The admissible class is the set of real symmetric matrices \(P\) with \(P_{uv}\geq0\), \(P\mathbf 1=\mathbf 1\), and \(P_{uv}=0\) when \(u\ne v\) are nonadjacent. The uniform distribution is stationary. Let \(J\) be the all-ones matrix of order \(nm\). Define \(\mu(P)=\|P-J/(nm)\|_2\); for symmetric stochastic \(P\) this equals the maximum modulus of its nonconstant eigenvalues. The theorem optimizes this **two-sided** eigenvalue modulus, not merely the second-largest positive eigenvalue, continuous-time relaxation, or mixing time at a fixed error tolerance.

## Proof

**1. Reduction without assuming uniform weights.** Let \(\mathcal G=D_n\times S_m\) act by dihedral automorphisms of the cycle and simultaneous permutations of clique coordinates. Its action is transitive on vertices, on cycle-coordinate edges, and on clique edges separately. For any admissible \(P\), the average of its permutation conjugates under \(\mathcal G\) is again symmetric, nonnegative, row-stochastic, and supported on the graph. The map \(P\mapsto\|P-J/(nm)\|_2\) is convex and invariant under these conjugations. Consequently, an optimum exists among matrices with two edge probabilities \(a,b\) and a uniform holding probability \(r\), constrained exactly by
\[
a\geq0,\quad b\geq0,\quad r=1-2a-(m-1)b\geq0.
\]
This establishes a **global** bound on the unrestricted problem, rather than a bound for a presupposed symmetric subclass.

**2. Full spectrum.** Write \(\mathcal L_n\) for the Laplacian of the cycle. Because \(\mathcal L(K_m)=mI_m-J_m\), the symmetrized transition matrix is
\[
P(a,b)=I_{nm}-a\mathcal L_n\otimes I_m-b I_n\otimes(mI_m-J_m).
\]
The cycle eigenvalues are \(\lambda_k=2(1-\cos(2\pi k/n))\), for \(k=0,\dots,n-1\). The clique Laplacian has eigenvalues \(0\) once and \(m\) with multiplicity \(m-1\). Thus the transition eigenvalues, including their multiplicities, are
\[
1-a\lambda_k\quad(0\leq k<n),\qquad
1-a\lambda_k-mb\quad(0\leq k<n),\quad\text{multiplicity }m-1.
\]
Only the first family at \(k=0\) is the trivial eigenvalue \(1\). Therefore the smallest positive-side spectral displacement from \(1\) is \(\min\{a s_n,mb\}\), while the greatest displacement is \(aL_n+mb\). With \(\gamma=1-\mu(P(a,b))\), the exact objective reduces to
\[
\gamma=\min\{a s_n,\ mb,\ 2-a L_n-mb\}.
\]
This identity is valid including boundary weights and negative transition eigenvalues.

**3. Two sharp upper bounds.** If an invariant chain has gap \(\gamma\), the preceding identity implies
\[
a\geq\gamma/s_n,\qquad b\geq\gamma/m,
\qquad aL_n+mb\leq2-\gamma.
\]
Inserting the first two inequalities into the third gives
\[
\gamma\left(2+\frac{L_n}{s_n}\right)\leq2,
\qquad\text{hence}\qquad
\gamma\leq\frac{2s_n}{L_n+2s_n}.
\]
Inserting them instead into the stochastic capacity constraint yields
\[
\gamma\left(\frac2{s_n}+\frac{m-1}{m}\right)\leq1,
\qquad\text{hence}\qquad
\gamma\leq\frac{ms_n}{2m+(m-1)s_n}.
\]
Both inequalities apply to all invariant admissible chains, hence to the original unrestricted optimization by step 1.

**4. Simultaneous attainment and invariant uniqueness.** Set \(\Gamma_{n,m}\) to the smaller of the two bounds and take \(a=\Gamma_{n,m}/s_n\), \(b=\Gamma_{n,m}/m\). The second bound ensures \(2a+(m-1)b\leq1\). The first bound ensures \(aL_n+mb\leq2-\Gamma_{n,m}\). Consequently all three entries in the exact formula for \(\gamma\) are at least \(\Gamma_{n,m}\), and the first two equal \(\Gamma_{n,m}\). The resulting chain is admissible with \(\gamma=\Gamma_{n,m}\), proving the optimal SLEM. For uniqueness in the two-orbit invariant class, observe that equality in the first bound forces both \(a=\gamma/s_n\) and \(b=\gamma/m\), since their positive coefficients occur in the third spectral inequality. Equality in the second bound likewise forces both equalities, since their positive coefficients occur in the row capacity inequality. At least one upper bound is active at every optimum; therefore these two weights are its unique invariant solution.

**5. Parity and the sharp layer threshold.** Elementary algebra shows the spectral bound is no greater than the stochastic-capacity bound precisely when
\[
L_n+\frac{2s_n}{m}\geq4.
\]
For even \(n\), one has \(L_n=4\), so this always holds. For odd \(n\), \(L_n=2(1+\cos(\pi/n))\) and \(s_n=2(1-\cos(2\pi/n))\); the condition is equivalent to
\[
m\leq m_{\mathrm{crit}}(n):=8\cos^2\left(\frac{\pi}{2n}\right).
\]
At \(n=3\), \(m_{\mathrm{crit}}=6\); for odd \(n\geq5\), \(7<m_{\mathrm{crit}}(n)<8\) (the lower bound follows already from the increasing value at \(n=5\), and the upper from strict \(\cos^2<1\)). These inequalities give every stated integer regime and the unique boundary case.

**6. Asymptotic comparison.** As \(n\to\infty\), \(s_n=4\pi^2/n^2+O(n^{-4})\) and \(L_n\to4\), so either branch defining \(\Gamma_{n,m}\) is asymptotic to \(s_n/2\). The maximum-degree and uniform-target Metropolis rules both assign \(a=b=1/(m+1)\) and zero holding. Their nontrivial eigenvalues are the families in step 2 with these weights. For each fixed \(m\geq3\), the negative-end eigenvalues remain bounded away from \(-1\) as \(n\to\infty\), whereas the largest nonconstant positive eigenvalue is \(1-s_n/(m+1)\). Thus their gap is eventually exactly \(s_n/(m+1)\), establishing \((m+1)/2\). For \(m=2\) and even \(n\), the product is bipartite and the nonlazy heuristic has eigenvalue \(-1\). For odd \(n\), \(L_n=2(1+\cos(\pi/n))\), so its most negative transition eigenvalue is \(-(1+2\cos(\pi/n))/3\), which dominates the remaining nontrivial moduli. The heuristic gap is therefore \(\tfrac23(1-\cos(\pi/n))\sim\pi^2/(3n^2)\), and the ratio tends to \(6\).

## Verification

The accompanying `verify.py` reconstructs the product transition matrices from their edge weights; compares the exact formula against a three-variable linear program for all \(3\leq n\leq22\), \(2\leq m\leq12\) (220 cases); checks dense transition spectra on 60 cases; checks the parity/layer threshold; and numerically stress-tests the stated asymptotics. The executed script reported `VERIFY_OK`, with 220 LP comparisons, 60 full-matrix spectral comparisons, and 40 fixed-layer asymptotic checks. Reproduce with `python3 verify.py` after installing dependencies from `requirements.txt`. All universal statements above are proved by the preceding algebra; finite numerical comparisons are corroboration, not certificates for infinitely many graphs.

## Relationship to prior work

Boyd, Diaconis, Parrilo, and Xiao give the convex symmetry-averaging theorem and Kronecker-sum spectrum for Cartesian products, as well as explicit edge-transitive product examples such as square tori and hypercubes [1]. These results explain the reduction used here, but the cycle-by-clique cylinder generally has **two different edge orbits**, and the cited edge-transitive formula does not supply its optimal two probabilities or layer threshold. In particular, familiar special cases such as the three-dimensional cube are already covered by the classical work and are not individually claimed as new.

The 2010 symmetric and cyclic multipartite results of Jafarizadeh [2] involve no clique edges within each multipartite layer; their complete bipartite connections between layers therefore impose a different graph topology. The later clique-lift framework [3] has complete bipartite connections across adjacent clique fibers, whereas the present product uses only the coordinate-preserving matching across those fibers. Olesker-Taylor and Zanetti study (among other examples) **two** matched cliques and obtain order-of-magnitude fastest-relaxation bounds, not this exact two-sided SLEM classification for a cycle of at least three cliques [4]. Indrani and collaborators [5] analyze general weighted Cartesian-product Laplacians and optimize **algebraic connectivity under a fixed sum of directional weights**; neither that objective nor its constraint is the nonnegative-stochastic two-sided SLEM minimization solved here. The standard Cartesian-product spectral identities are acknowledged rather than claimed as new.

## Limitations

The theorem assumes symmetric, uniform-stationary **discrete-time** chains; it does not optimize arbitrary nonreversible transition matrices, chains with nonuniform stationary laws, time-inhomogeneous schemes, or literal total-variation mixing time. It establishes a unique optimizer inside the natural invariant two-edge-weight class but does not claim uniqueness among all non-invariant optima. Independent expert scrutiny of the theorem and a comprehensive literature audit remain outstanding. Despite targeted comparisons, specialized or not-yet-indexed results may overlap the stated classification.

## References

[1] S. Boyd, P. Diaconis, P. A. Parrilo, L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” arXiv:0709.0955 (first public posting 2007-09-06), *SIAM Journal on Optimization* 20 (2009), 792–819. DOI: 10.1137/070689413. https://arxiv.org/abs/0709.0955

[2] S. Jafarizadeh, “Fastest Mixing Markov Chain on Symmetric K-Partite Network,” arXiv:1008.2588 (2010). https://arxiv.org/abs/1008.2588

[3] S. Jafarizadeh, “Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs and Subgraphs,” arXiv:2501.02421. https://arxiv.org/abs/2501.02421

[4] S. Olesker-Taylor and L. Zanetti, “Geometric bounds on the fastest mixing Markov chain,” *Probability Theory and Related Fields* (2023/2024). https://doi.org/10.1007/s00440-023-01257-x

[5] I. Y. R. L. Indrani, S. B. Sowmya, S. Sudha, M. T. Somalatha, “Algebraic Connectivity and Exact Laplacian Spectra of Generalized Graph Products,” *International Journal of Engineering Science Technologies* 10 (2026), 62–69. https://doi.org/10.29121/ijoest.v10.i4.2026.781
