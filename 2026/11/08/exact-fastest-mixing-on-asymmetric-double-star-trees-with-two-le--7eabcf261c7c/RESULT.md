# Exact fastest mixing on asymmetric double-star trees with two leaves at one hub

## Finding
For each integer \(n\ge6\), the fastest symmetric nonnegative stochastic kernel on the double-star tree \(D_{2,n}\) has second-largest eigenvalue modulus
\[\rho_*(D_{2,n})=\frac{n^2}{n^2+n-2}.\]
Writing \(D=n^2+n-2=(n-1)(n+2)\), one attaining kernel uses the following three kinds of off-diagonal transition weights:
\[a=\frac{n(n-2)}{2D},\qquad b=\frac{n-2}{D},\qquad c=\frac{3n-2}{D}.\]
These are assigned respectively to each of the two left spokes, each of the \(n\) right spokes, and the edge joining the two hubs. Its hub holding probabilities vanish because \(2a+c=nb+c=1\); its leaf holding probabilities are \(1-a\) and \(1-b\).

## Assumptions and scope
The graph is a finite simple tree with vertices consisting of one hub \(u\) and two adjacent leaves, another hub \(v\) and \(n\) adjacent leaves, and the edge \(uv\). The optimization is over *all* real symmetric matrices \(P\) with nonnegative entries, row sums one, and \(P_{ij}=0\) whenever distinct vertices \(i,j\) are nonadjacent. Diagonal holding entries are allowed. Put \(L=I-P\) and \(J=\mathbf1\mathbf1^{\mathsf T}/(n+4)\). The objective is \(\rho(P)=\|P-J\|_2\); it includes both positive and negative nontrivial eigenvalues. A graph with \(n\ge6\) is the only regime asserted here; nothing is claimed about smaller right-leaf counts or uniqueness among nonsymmetric kernels.

## Proof
**1. Orbit reduction.** The operator norm \(\|P-J\|_2\) is convex and invariant under simultaneous permutations of the two left leaves and, independently, the \(n\) right leaves. Averaging an arbitrary feasible \(P\) over these permutations cannot increase its objective. Thus it suffices to optimize orbit-invariant matrices with respective edge weights \(a,b,c\ge0\). Their exact feasibility inequalities are \(2a+c\le1\) and \(nb+c\le1\). All leaf diagonal entries are automatically nonnegative.

**2. Exact upper bound on the spectral gap.** For every such matrix the Laplacian has a right-leaf difference eigenvalue \(b\), with multiplicity \(n-1\). Hence \(\lambda_2(L)\le b\). In addition consider the vector \(z\) with value \(n^2\) on both left leaves, value \(n(n-2)\) at the left hub, value zero at the right hub, and value \(-(3n-2)\) on each right leaf. Its coordinate sum is zero, and its squared norm is
\[N_z=n(3n^3+5n^2-8n+4).\]
Only edges contribute to the Laplacian energy, so the Rayleigh quotient is exactly
\[R_z=\frac{8n^2a+n(3n-2)^2b+n^2(n-2)^2c}{N_z}.\]
Thus \(\lambda_2(L)\le R_z\). Set
\[\theta=\frac{3n^3+5n^2-8n+4}{n(n-2)D},\quad \alpha=\frac4{(n-2)D},\quad\beta=\frac{n(n-4)}{(n-2)D}.\]
For every integer \(n\ge6\), \(0<\theta\le1\), because the numerator of \(1-\theta\) after multiplying by the positive denominator is \(n^2[(n-2)^2-13]+12n-4>0\). Also \(\alpha,\beta>0\). Direct coefficient matching gives the *exact identity*
\[\theta R_z+(1-\theta)b=\alpha(2a+c)+\beta(nb+c).\]
By the hub inequalities, the right side is bounded by \(\alpha+\beta=(n-2)/D\). Since \(\lambda_2(L)\) is bounded above by each of \(R_z,b\),
\[\lambda_2(L)\le\frac{n-2}{D}.\]
Every feasible chain therefore satisfies \(\rho(P)\ge1-\lambda_2(L)\ge1-(n-2)/D=n^2/D\). Averaging ensures this global bound applies before orbit reduction.

**3. Attainment and the negative spectrum.** Choose the three weights in the Finding. The left-leaf difference eigenvalue of \(L\) is \(a\), and the right-leaf difference eigenvalue is \(b\) with multiplicity \(n-1\). On vectors constant in each of the four vertex orbits (left leaves, left hub, right hub, right leaves), the Laplacian acts as
\[Q=\begin{pmatrix}a&-a&0&0\\-2a&2a+c&-c&0\\0&-c&nb+c&-nb\\0&0&-b&b\end{pmatrix}.\]
Its characteristic polynomial is \(x(x-b)q_n(x)\), where
\[q_n(x)=x^2-\frac{5n^2+2n-8}{2D}x+\frac{n(3n^3+4n^2-28n+16)}{2D^2}.\]
This quotient represents a symmetric operator after weighting orbit coordinates by orbit sizes, so the two roots of \(q_n\) are real. Exact substitution gives
\[q_n(b)=\frac{(n-2)(3n^3+5n^2-8n+4)}{2D^2}>0,\quad q_n'(b)=-\frac{n(5n-2)}{2D}<0,\]
\[q_n(2-b)=\frac{(n-2)(n^3+5n^2-8n+4)}{2D^2}>0,\quad q_n'(2-b)=\frac{n(3n+2)}{2D}>0.\]
For a monic quadratic with real roots, positivity together with negative derivative at the left test point forces both roots to its right; positivity with positive derivative at the right test point forces both roots to its left. Consequently both quadratic roots lie strictly between \(b\) and \(2-b\). Furthermore \(b\le a\le2-b\) for all \(n\ge6\). The full nonzero spectrum of \(L\) is therefore contained in \([b,2-b]\), and the eigenvalue \(b\) occurs. Equivalently, every nontrivial eigenvalue of \(P=I-L\) has magnitude at most \(1-b\), with equality. The matching global lower bound from step 2 proves the theorem.

## Verification
`VERIFY.py` uses only the Python standard library's exact rational arithmetic. It rechecks the witness normalization, the hub-capacity and Rayleigh-dual identities, the quadratic spectral bounds, and an independent four-by-four characteristic-polynomial evaluation, on more than 190 distinct graph orders. Run `python VERIFY.py`. Its finite computations supplement the symbolic proof above; they are not a proof for all integers.

For example, at \(n=6\) the exact optimal weights are \((a,b,c)=(3/10,1/10,2/5)\), the nonzero quotient eigenvalues are \(1/10,4/5,3/2\), and the SLEM is \(9/10\).

## Relationship to prior work
The convex spectral-norm/SDP formulation and symmetry averaging are classical: Boyd, Diaconis, Parrilo and Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (2007), https://arxiv.org/abs/0709.0955. Their worked two-clique construction is not the tree \(D_{2,n}\), and their general algorithm does not state the present rational closed form or its dual certificate.

Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks (2020), https://arxiv.org/abs/2501.02421, Section 6.7, specifically studies bistar graphs. Its analytic formulas (56)–(58) are explicitly conditional on assumptions (59a), (59b), (60). Under the uniform stationary measure on \(D_{2,n}\), condition (60) would require the two leaf-class sizes to be at most one, whereas here they are two and \(n\ge6\). Therefore that conditional theorem does not imply this saturated-hub regime. This observation is about the stated theorem's scope, not a claim that numerical SDP solutions were previously unavailable.

Existing related weighted-double-star algebraic-connectivity optimization considers a global linear conductance budget with independent edge costs; here the constraints are *separate hub row capacities* and the objective includes negative Markov eigenvalues. That prior budget theorem does not by itself give the current optimizer.

## Limitations
The theorem asserts a closed form for the indicated leaf-count family only, not all double stars or nonuniform stationary distributions. It proves existence of the displayed optimum, not uniqueness among all supported matrices. Unindexed literature could contain an equivalent specialization, and an independent mathematical audit has not been performed.

## References
1. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, arXiv:0709.0955v1 (public September 6, 2007), https://arxiv.org/pdf/0709.0955.
2. S. Jafarizadeh, *Fastest Mixing Reversible Markov Chain: Clique Lifted Graphs & Subgraphs*, IEEE Transactions on Signal and Information Processing over Networks (2020), Section 6.7 (bistar and conditions (59)–(60)), openly available preprint arXiv:2501.02421v1 (posted January 5, 2025), https://arxiv.org/pdf/2501.02421.
3. S. Olesker-Taylor and L. Zanetti, *Geometric Bounds on the Fastest Mixing Markov Chain*, Probability Theory and Related Fields 188 (2024), https://doi.org/10.1007/s00440-023-01257-x (general bounds rather than this exact finite-tree law).
