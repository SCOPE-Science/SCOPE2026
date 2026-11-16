# Sharp four-column Paley sampling bounds and an arithmetic isometry transition

## Finding

Let \(p\equiv1\pmod4\) be prime, let \(Q_p\) be the set of nonzero quadratic residues modulo \(p\), and put \(m=(p-1)/2\). Define the normalized Fourier sampling matrix
\[
F_p(x,a)=m^{-1/2}e^{2\pi ixa/p},\qquad x\in Q_p,\ a\in\mathbb F_p.
\]
For four distinct columns \(E\subset\mathbb F_p\), write \(H_E=F_{p,E}^*F_{p,E}\); its four eigenvalues are the sharp squared singular values of the sampled four-character subspace. Define
\[
\alpha_p=\frac{p-2-\sqrt p-2\sqrt{p-\sqrt p+1}}{p-1},\quad
\beta_p=\frac{p+3\sqrt p}{p-1},\quad
\gamma_p=\frac{p-4-3\sqrt p}{p-1}.
\]
All extrema are taken over **every** four-element frequency set \(E\), not only consecutive bands.

**Theorem.** For \(p=5\), every \(H_E\) has spectrum \(\{0,0,3/2,5/2\}\). For \(p\in\{13,17\}\),
\[
\min_{|E|=4}\lambda_{\min}(H_E)=\alpha_p,
\qquad \max_{|E|=4}\lambda_{\max}(H_E)=\beta_p.
\]
The lower equality holds precisely when the four vertices of \(E\) induce a three-edge star \(K_{1,3}\) in the Paley graph \(P(p)\). The upper equality holds precisely for induced \(2K_2\) (two disjoint edges). For every prime \(p\equiv1\pmod4\) with \(p\ge29\),
\[
\min_{|E|=4}\lambda_{\min}(H_E)=\gamma_p,
\qquad \max_{|E|=4}\lambda_{\max}(H_E)=\beta_p.
\]
Here the lower equality holds precisely for four-vertex Paley **independent sets**, and the upper equality precisely for induced \(2K_2\).

With the standard four-column restricted-isometry deviation \(\delta_4(F_p)=\max_{|E|=4}\|H_E-I_4\|_{\mathrm{op}}\), the sharp value is
\[
\delta_4(F_p)=
\begin{cases}
3/2,&p=5,\\
(1+3\sqrt p)/(p-1),&p=13\text{ or }17,\\
3/(\sqrt p-1),&p\ge29\text{ and }p\equiv1\pmod4.
\end{cases}
\]
The worst deviation changes from the **upper** spectral edge at the two exceptional primes to the **lower** edge for every larger eligible prime. This is a statement about exactly four columns; it does not assert an order-four isometry bound for subsets of fewer columns except what follows by interlacing.

## Assumptions and scope

A Paley graph \(P(p)\), for \(p\equiv1\pmod4\), has vertex set \(\mathbb F_p\) and an (undirected) edge \(\{a,b\}\) precisely when \(a-b\) is a nonzero square. Let \(\chi\) denote the quadratic character, extended by \(\chi(0)=0\). Define \(S_E\) to be the real signed adjacency matrix with diagonal zero and \((S_E)_{a,b}=\chi(a-b)\) off the diagonal. All frame eigenvalues are with respect to counting measure on the nonzero quadratic residues and the stated column normalization. No zero-frequency row is adjoined and no extra column is appended. The eligible primes start \(5,13,17,29,37,41,53,61,\dots\).

## Proof

**1. Exact Gram reduction.** The classical quadratic Gauss-sum identity for \(p\equiv1\pmod4\) gives, for nonzero \(u\),
\[
\sum_{x\in Q_p}e^{2\pi iux/p}=\frac{-1+\sqrt p\,\chi(u)}2.
\]
The diagonal entries of \(H_E\) are one, and the identity therefore yields
\[
H_E=\frac{pI_4-J_4+\sqrt p\,S_E}{p-1},
\]
with \(J_4\) the all-one matrix. This is an equality of actual complex Fourier Gram matrices and real symmetric matrices, not merely a bound.

**2. Universal upper bound and equality.** Since \(S_E\) is symmetric with zero diagonal and all off-diagonal entries of modulus one, \(\lambda_{\max}(S_E)\le3\). Since \(-J_4\) is negative semidefinite, the Gram identity gives \(\lambda_{\max}(H_E)\le(p+3\sqrt p)/(p-1)=\beta_p\). Equality requires a unit vector \(v\) with \(S_Ev=3v\) and \(J_4v=0\). Equality in the elementary row-sum absolute-value inequality means \(S_E=ss^\mathsf T-I_4\) for a sign vector \(s\in\{-1,1\}^4\), with the top eigenvector parallel to \(s\). The second condition is \(\sum s_j=0\). Consequently the positive edges connect the two pairs of equal signs, exactly the induced \(2K_2\). Conversely this graph gives equality, with extremal vector \(s/2\).

**3. Universal lower bound and equality.** For every unit vector \(v\), \(v^*S_Ev\ge-3\), and \(v^*J_4v\le4\). Thus \(\lambda_{\min}(H_E)\ge(p-4-3\sqrt p)/(p-1)=\gamma_p\). Equality forces \(v\) to be the all-one direction and \(S_E\mathbf1=-3\mathbf1\), hence all six signs must be negative: the four vertices are independent in \(P(p)\). Conversely any independent four-set has this eigenvector and attains the bound. Both equality classifications are exact.

**4. Attainment uniformly for \(p\ge29\).** The Paley graph is strongly regular with degree \(k=(p-1)/2\), edge common-neighbor count \(\lambda=(p-5)/4\), and nontrivial adjacency eigenvalues \((-1\pm\sqrt p)/2\). Applying the standard Hoffman independent-set inequality gives \(\alpha(P(p))\le\sqrt p\), where here \(\alpha(P(p))\) denotes the graph independence number (not the spectral constant \(\alpha_p\)). Fix an edge \(\{u,v\}\). Its \(\lambda=(p-5)/4\) common neighbors induce a graph with an edge as soon as \(\lambda>\sqrt p\), because otherwise they would form an independent set exceeding the Hoffman bound. This strict inequality holds at \(p=29\) and for all larger eligible primes. Such an edge completes \(\{u,v\}\) to a four-clique. Multiplication of vertex labels by any nonsquare exchanges edges and nonedges, giving a four-vertex independent set. Similarly the \((p-1)/4\) common nonneighbors of \(u,v\) contain an edge, and these two vertices plus \(u,v\) induce \(2K_2\). Both universal spectral bounds are therefore attained for every eligible \(p\ge29\), with precisely the equality geometries above.

**5. Exact exceptional primes \(13\) and \(17\).** There are respectively \(\binom{13}{4}=715\) and \(\binom{17}{4}=2380\) unordered four-sets. Their Paley signs can be constructed without floating arithmetic by enumerating quadratic residues modulo the prime. For each sign matrix other than the positive star, the attached standard-library checker proves by the Sylvester leading-principal-minor criterion that the real symmetric matrix \(H_E\) has smallest eigenvalue strictly above \(85/1000\) for \(p=13\), respectively \(230/1000\) for \(p=17\). To avoid numerical ambiguity it uses the rational lower approximation \(h_p=\lfloor10^9\sqrt p\rfloor/10^9\) and positive definiteness of integer matrices, with perturbation norm at most \(3/(10^9(p-1))<1/1000\). Every possible sign matrix is checked, not a sample or a numerical tolerance test. Integer square comparisons further establish \(\alpha_{13}<85/1000\) and \(\alpha_{17}<230/1000\).

For the star sign pattern, the orthogonal leaf-difference subspace has eigenvalue \((p+\sqrt p)/(p-1)\) twice, and the remaining two eigenvalues come from the exact block
\[
\frac1{p-1}\begin{pmatrix}
p-1&\sqrt3(\sqrt p-1)\\
\sqrt3(\sqrt p-1)&p-3-2\sqrt p
\end{pmatrix}.
\]
Its smaller eigenvalue is \(\alpha_p\). The explicit star witnesses are \(E=\{0,1,3,9\}\) for \(p=13\) and \(E=\{0,1,3,10\}\) for \(p=17\). For either prime \(E=\{0,1,6,7\}\) induces \(2K_2\), attaining \(\beta_p\). The finite certificate also proves there are no four-independent sets at these two orders. Thus every exceptional sharp bound and equality case is established exactly.

**6. Smallest prime and isometry phase transition.** For \(p=5\) the complete two-row matrix has frame operator \((5/2)I_2\). Deleting one unit vector leaves eigenvalues \(5/2\) and \(3/2\), while the four-column Gram matrix has two additional zeros. For \(p=13,17\), \(\alpha_p+\beta_p>2\), because \(\sqrt p>\sqrt{p-\sqrt p+1}\); therefore \(\beta_p-1>1-\alpha_p\). For \(p\ge29\), \(\gamma_p+\beta_p=2-2/(p-1)<2\), hence \(1-\gamma_p>\beta_p-1\). These identities yield all stated sharp isometry deviations and the claimed change in the worst spectral edge.

## Verification

The file `paley_four_check.py`, executable using standard Python 3, enumerates all \(715\) and \(2380\) exceptional four-sets and certifies, using integer determinants, the strict separation of nonstar configurations from the proposed lower eigenvalue. Its proof obligations and rational square-root enclosures are explained in the code. It also checks the Paley common-neighbor formulas and graph witnesses at the five larger sample primes \(29,37,41,53,61\). Those latter finite checks corroborate the general graph argument; the proof for infinitely many primes is the Hoffman/strong-regularity argument in Step 4, not the test loop. Expected terminal marker: `PALEY_FOUR_EXTREMA_PASS`.

## Relationship to prior work

The quadratic Gauss sum and Paley graph parameters are classical. General quadratic-residue Fourier frames and their equiangular structures appear in Fickus--Jasper (2018). The Paley restricted-isometry construction in Bandeira--Mixon--Moreira (2014) includes a specially normalized zero row and an additional column; its Gram entries differ from the present unaugmented, nonzero-residue sampling matrix. The random-subensemble spectral limit of Magsino--Mixon--Parshall (2019) does not determine the exact worst four-subset spectra. Arian--Yilmaz (2019) primarily analyze the complementary \(p\equiv3\pmod4\) Paley convention, where the Gram matrix is complex and has distinct tournament geometry. Previous exact four-consecutive-frequency formulas concern a restricted family of column sets, not the worst over **all** four-sets and the present sharp global phase transition.

## Limitations

This theorem uses only prime cyclic groups of order \(p\equiv1\pmod4\), sampling at all **nonzero** square sites with equal weights, and exactly four distinct frequency columns. The exact exceptional-order certification is finite and fully reproducible; it is not a computational argument about all primes. No claim of exhaustive historical priority is made; an equivalent result under another Paley/conference-matrix normalization could exist. The external comparison distinguishes normalization and the stronger all-subsets statement, but does not exhaust all unpublished special-case literature. No independent audit has been performed.

## References

1. Fickus and Jasper, *Equiangular tight frames from group divisible designs* (first public preprint, 2018-03-20), https://arxiv.org/abs/1803.07468 (primary MSC 42C15).
2. Magsino, Mixon and Parshall, *Kesten--McKay law for random subensembles of Paley equiangular tight frames* (2019), https://arxiv.org/abs/1905.04360.
3. Arian and Yilmaz, *RIP constants for deterministic compressed sensing matrices--beyond Gershgorin* (2019), https://arxiv.org/abs/1911.07428.
4. Bandeira, Mixon and Moreira, *A conditional construction of restricted isometries* (2014), https://arxiv.org/abs/1410.6457.
5. Classical quadratic Gauss sum, Paley strongly regular graph eigenvalues and Hoffman ratio bound; these standard inputs are stated explicitly and used only under their classical hypotheses.
