# Joint epidemic attack and seeding profiles: a unique rank-one kernel inside an affine observational family

## Finding
Fix an integer \(n\ge2\), known population fractions \(p_i>0\) with \(\sum_i p_i=1\), and proposed strictly positive final attack rates \(z_i\in(0,1)\) and initial-case major-outbreak probabilities \(h_i\in(0,1)\). Set
\[
a_i=-\log(1-z_i),\qquad b_i=\frac{h_i}{1-h_i},\qquad T_1=\sum_i p_i a_i h_i,\quad T_2=\sum_i p_i b_i z_i.\]
In the fully susceptible, finite-type Markovian SEIR epidemic described below, with an arbitrary strictly positive effective next-generation kernel, these two observed profiles can occur together **if and only if** \(T_1=T_2\). When compatible, write \(T=T_1=T_2\). Every compatible strictly positive kernel \(K\) belongs to the affine class
\[
\mathcal K(z,h)=\{K>0:Kz=a,\ (p\odot h)^\mathsf TK=(p\odot b)^\mathsf T\}.
\]
The class has affine dimension exactly \((n-1)^2\), contains a relatively open set of positive matrices, and contains **exactly one rank-one kernel**, namely
\[
\boxed{K^*_{ij}=\frac{a_i p_j b_j}{T}}.
\]
For every \(n\ge2\), it also contains strictly positive non-rank-one kernels yielding **the identical pair** \((z,h)\). Thus the pair uniquely identifies the rank-one next-generation matrix conditional on rank-one mixing, but does not identify rank-one mixing itself against an unrestricted positive-kernel alternative. The resulting reproduction number in the rank-one model is
\[
\boxed{\mathcal R_0=\frac{\sum_i p_i a_i b_i}{T}>1}.
\]
This is an exact necessary-and-sufficient feasibility test and a full-dimensional characterization of the remaining observational ambiguity, not a claim of identifying raw contact rates, infectivity or recovery rates separately.

## Assumptions and scope
There are \(n\) types of sizes \(N_i=p_iN\) in the large-population, vanishing-initial-seed regime. Latent individuals become infectious at positive rates \(\delta_i\) without latent-stage removal; infectious type \(j\) individuals recover at exponential rate \(\gamma_j>0\). New type \(i\) infections due to a type \(j\) infectious individual occur at rate \(\gamma_jB_{ij}\), where the dimensionless mean-offspring matrix is \(B_{ij}=p_iK_{ij}/p_j\), while the population is almost wholly susceptible. The deterministic mean-field incidence therefore has effective final-size kernel \(K_{ij}=p_jB_{ij}/p_i\). All entries of \(K\) are strictly positive, and infection generations have independent exponential lifetimes and conditionally independent Poisson offspring counts. A major outbreak refers to nonextinction of the multitype branching approximation from a single initially exposed or infectious individual; \(z\) is the nonzero deterministic final-size vector conditional on a macroscopic outbreak. The latent waiting rates do not affect either observable under these assumptions.

The rank-one representative is realizable in the balanced proportionate-contact subclass: each type makes contacts at common rate \(c>0\), contacts type \(j\) with probability \(p_j\), and has per-contact infection probability \(q u_i v_j\), with positive \(u_i,v_j,q\) and \(q u_i v_j\le1\), so \(K_{ij}=cq\,u_i(v_j/\gamma_j)p_j\). For any compatible profiles choose \(\gamma_j=1\), \(u_i=a_i\), \(v_j=b_j\), and \(cq=1/T\), taking \(c\) sufficiently large to enforce the per-contact probability bound. The non-rank-one observational alternatives are in the general positive effective-kernel class; they are **not asserted** to preserve the same reciprocal, factorized contact subclass.

## Proof
**1. Forward final-size and backward seeding equations.** Integrating the susceptible equations, and using the identity that the total infectious person-time of type \(j\) equals its total infections divided by \(\gamma_j\), gives
\[
a_i=\sum_j K_{ij}z_j.\tag{1}\]
For the early branching process, conditional on an infectious lifetime of length \(s\), a type \(j\) parent produces Poisson offspring of each type \(i\) at rate \(\gamma_j B_{ij}\). Writing \(1-h_j\) for extinction from type \(j\), averaging \(\exp[-\gamma_j s\sum_i B_{ij}h_i]\) over an exponential lifetime yields
\[
1-h_j=\frac{\gamma_j}{\gamma_j+\sum_i\gamma_j B_{ij}h_i}
=\frac1{1+\sum_i B_{ij}h_i},
\qquad b_j=\frac{h_j}{1-h_j}=\sum_i\frac{p_i}{p_j}K_{ij}h_i.\tag{2}
\]
Here \(B\) is dimensionless, the mean number of type \(i\) offspring per type \(j\) infective; conditional offspring **rates** are \(\gamma_jB_{ij}\). This distinction is essential when recovery rates differ. In vector form, equations (1)–(2) are \(Kz=a\) and \((p\odot h)^\mathsf TK=(p\odot b)^\mathsf T\).

**2. Compatibility and existence.** Multiplying (1) by \(p_ih_i\) and summing gives
\[\sum_i p_ia_ih_i=\sum_{ij}p_ih_iK_{ij}z_j=\sum_j p_jb_jz_j.\]
Conversely, if this identity holds, \(T>0\) and the strictly positive matrix \(K^*_{ij}=a_ip_jb_j/T\) obeys both vector equations exactly. It therefore realizes the proposed data; moreover it has the balanced proportionate-contact realization given above. No independent fitting equation or unknown scaling remains.

**3. Positive solutions are the physically selected solutions.** Each component satisfies \(a_i=-\log(1-z_i)>z_i\), hence \(K^*z>z\), which implies \(\rho(K^*)>1\) by the Perron–Frobenius comparison theorem. The same comparison holds for any positive \(K\) in the affine family. For \(\rho(K)>1\), the final-size map \(F(x)=1-\exp(-Kx)\) (componentwise exponential) has exactly one strictly positive fixed point. One proof starts by iterating from a small positive Perron vector (a strict subsolution); bounded monotone convergence gives existence. For uniqueness, if \(x,y>0\) were two fixed points, choose \(r=\max_i x_i/y_i>1\) after possibly swapping; at a maximizing index, monotonicity and strict subhomogeneity \(F(ry)<rF(y)\) contradict \(x=F(x)\). The branching survival map \(G_j(x)=(\sum_i B_{ij}x_i)/(1+\sum_i B_{ij}x_i)\) has the same monotonicity and strict subhomogeneity; its positive fixed point is unique, and irreducibility ensures it is the nonextinction probability vector. Thus the constructed data are not spurious fixed points.

**4. Exact affine-fiber dimension.** Let \(w=p\odot h\) and \(v=p\odot b\). Once \(K^*\) is fixed, a matrix \(K=K^*+E\) obeys (1)–(2) precisely when
\[
Ez=0,\qquad w^\mathsf TE=0.\tag{3}
\]
The first condition restricts every row to the \((n-1)\)-dimensional subspace \(z^\perp\); the second restricts every column to \(w^\perp\). The solution space is canonically \(w^\perp\otimes z^\perp\), of dimension \((n-1)^2\). Small perturbations preserve entrywise positivity. Choose nonzero \(u\in w^\perp\), \(v\in z^\perp\); then \(K^*+\varepsilon uv^\mathsf T\) is positive for all sufficiently small real \(\varepsilon\), and has rank two for \(\varepsilon\ne0\): \(a\notin w^\perp\), while \(p\odot b\notin z^\perp\), so its two rank-one terms have independent left and right factors. Every such perturbation gives the same two observed profiles.

**5. Rank-one uniqueness.** Suppose \(K=xy^\mathsf T>0\) also satisfies (1)–(2). Equation (1) implies \(x\) is proportional to \(a\), and (2) implies \(y\) is proportional to \(p\odot b\). Their normalization is uniquely forced by \(Kz=a\), yielding \(K=K^*\). Its sole nonzero eigenvalue is \(\sum_i p_i a_ib_i/T\), strictly greater than one because \(b_i>h_i\) and \(\sum_i p_i a_ih_i=T\). This completes the characterization.

## Verification
The bundled `verify.py` uses 70-digit standard-library decimal calculations. For three types with \(p=(1/5,3/10,1/2)\), susceptibility profile \(u=(1,2,4)\), infectivity-to-recovery profile \(v/\gamma=(4,2,1)\), and contact-transmission scale \(cq=1/2\), the exact kernel is
\[
K=\begin{pmatrix}2/5&3/10&1/4\\4/5&3/5&1/2\\8/5&6/5&1\end{pmatrix},\qquad \mathcal R_0=2.
\]
Solving the two strictly concave scalar equations yields
\[
z\approx(0.469140791089464237,\ 0.718188500314880147,\ 0.920582278645223693),
\quad h\approx(0.712680390004482723,\ 0.553615733397368529,\ 0.382758403959785794).
\]
The two sides of the compatibility equation equal approximately \(0.785381250666580015\). The script verifies the forward/backward equations, reconstructs the exact displayed kernel, and explicitly perturbs it to a positive rank-two observational twin. It also checks an explicit \((n-1)^2\)-element perturbation basis for several sizes. Finite arithmetic checks corroborate the worked example and basis; the full all-size theorem follows from the proof above, not enumeration.

## Relationship to prior work
Zhang and collaborators (2026) derive the **forward** heterogeneous SEIR final-size relation and early multitype branching extinction equations, comparing long-run burden and outbreak-initiation risk. These equations, and the broad possibility that their rankings disagree, are antecedents, not newly claimed here. Ball and Critcher (2026) analyze multitype SIR with proportionate global mixing and obtain scalar forward calculations for both major-outbreak probabilities and final outcomes. El Khalifi (2026) studies heterogeneous infectiousness/susceptibility dependence and forward outbreak outcomes. The present result concerns the joint **inverse** image of the two observables: a cross-observable feasibility identity, the unique positive rank-one reconstruction, and the precise \((n-1)^2\) family of non-rank-one observational aliases. Neither a shared model nor an exact forward equation by itself constitutes an explicit published inverse classification, but the algebraic dependence on known forward equations is material. Literature priority cannot be established by failed searches alone.

## Limitations
The observables are infinite-population conditional final-size limits and early-stage branching survival probabilities, not finite-sample realized attack rates or outcomes of repeated introductions. Exact compatibility is fragile under measurement error; this statement does not develop a statistical estimator or robustness bound. Exponential recovery and guaranteed progression from latency are essential for the stated fractional-odds seeding relation. The full affine alternatives allow general positive directed effective mixing kernels; not all satisfy reciprocal contact balance or factorized infectivity. The reconstruction identifies only the dimensionless next-generation kernel when a rank-one structural assumption is imposed, not unique microscopic biological parameters. Novelty has not been independently certified.

## References
1. S. Zhang, M. Wu, J. Yang, J. Xiao, F. Bai, *Indication of demographic and epidemiological data on early-stage risks and long-term epidemic burden*, arXiv:2611.19854v1, first public November 15, 2026, Sections 3 and Appendices A–C. https://arxiv.org/html/2611.19854v1
2. F. Ball and L. Critcher, *Multitype SIR epidemics among a population partitioned into households with proportionate global mixing*, Journal of Mathematical Biology (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13111495/
3. M. El Khalifi, *Dependence Structure and Epidemic Outcomes in Heterogeneous SIR Models*, arXiv:2601.01549 (2026). https://arxiv.org/abs/2601.01549
4. O. Diekmann, H. Heesterbeek, and T. Britton, *Mathematical Tools for Understanding Infectious Disease Dynamics*, Princeton University Press (2013), standard multitype branching and epidemic final-size framework.
