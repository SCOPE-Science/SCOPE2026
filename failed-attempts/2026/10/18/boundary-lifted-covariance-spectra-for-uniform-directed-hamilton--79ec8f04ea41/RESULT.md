# Boundary-lifted covariance spectra for uniform directed Hamiltonian paths and cycles

## Finding

Let \(n\ge3\), and let \(\pi\) be a uniform permutation of \(\{1,\ldots,n\}\). For every ordered pair of distinct labels \((a,b)\), let \(P_{ab}\) indicate that \(a\) is immediately followed by \(b\) among \(\pi_1,\ldots,\pi_n\), and let \(C_{ab}\) indicate that it is followed by \(b\) when the final label is also followed by the first. Thus \(P\) is the directed-edge incidence vector of a uniformly random Hamiltonian path and \(C\) is that of a uniformly random oriented Hamiltonian cycle. Their covariance matrices are indexed by all \(n(n-1)\) ordered edges, with the usual Euclidean inner product on this edge space.

**Theorem (complete exact spectra).** The spectrum of \(\operatorname{Cov}(P)\), with multiplicities, is

\[
\begin{array}{c|cccc}
\text{eigenvalue}&0&\frac1{n(n-1)}&\frac1n&\frac{n+1}{n(n-1)}\\
\text{multiplicity}&1&2(n-1)&\frac{n(n-3)}2&\frac{(n-1)(n-2)}2.
\end{array}
\]

The spectrum of \(\operatorname{Cov}(C)\) is

\[
\begin{array}{c|ccc}
\text{eigenvalue}&0&\frac1{n-1}&\frac{n}{(n-1)(n-2)}\\
\text{multiplicity}&2n-1&\frac{n(n-3)}2&\frac{(n-1)(n-2)}2.
\end{array}
\]

Zero-dimensional rows at \(n=3\) are omitted. Passing from an open path to its cyclic closure therefore creates exactly \(2(n-1)\) additional covariance-null directions. They are the vertex-potential directions, which depend only on endpoints in an open path and telescope completely along a cycle.

For arbitrary real weights \(w_{ab}\) on the ordered edges, put \(\overline w=[n(n-1)]^{-1}\sum_{a\ne b}w_{ab}\), \(h_{ab}=w_{ab}-\overline w\), and \(Z_w=\sum_{j=1}^{n-1}w_{\pi_j,\pi_{j+1}}\). Then the exact **sharp** bounds are

\[
\frac1{n(n-1)}\sum_{a\ne b}h_{ab}^{2}
\ \le\ \operatorname{Var}(Z_w)\ \le\
\frac{n+1}{n(n-1)}\sum_{a\ne b}h_{ab}^{2}.
\]

For nonzero centered weights, equality on the left holds precisely for vertex-potential weights \(h_{ab}=u_a+u_b+v_a-v_b\), with \(\sum_a u_a=\sum_a v_a=0\). Equality on the right holds precisely for **circulations**: \(h_{ab}=-h_{ba}\) and \(\sum_{b\ne a}h_{ab}=0\) for all \(a\). Such extremizers exist for every \(n\ge3\). Thus the worst-to-best variance ratio under fixed nonzero centered Frobenius norm is exactly \(n+1\).

## Assumptions and scope

Paths are **directed and open**, and cycles are **directed and closed**. The labels are distinct, the permutation is uniform, edges \((a,b)\) and \((b,a)\) are different, and self-loops are excluded. In the cycle model, \(\pi_n\to\pi_1\) is counted as one extra directed edge; cyclic rotations do not change its incidence vector. The weighted cost \(Z_w\) refers only to the open path. No randomness is assumed of the weights. All assertions hold for every integer \(n\ge3\), without asymptotics or regularity conditions.

For matrix notation, an edge vector is identified with a zero-diagonal real matrix \(H=(h_{ab})\). Write \(s=\sum_{a\ne b}h_{ab}\), \(r_a=\sum_{b\ne a}h_{ab}\), and \(c_b=\sum_{a\ne b}h_{ab}\). Norms and orthogonality refer to \(\langle H,K\rangle=\sum_{a\ne b}h_{ab}k_{ab}\).

## Proof

**1. Joint edge probabilities.** A prescribed directed edge \(a\to b\) appears in a uniform open path with probability \(1/n\): contract its endpoints into an ordered block, leaving \((n-1)!\) of the \(n!\) permutations. Two different edges are *incompatible* exactly when they have the same tail, the same head, or are reverse orientations of one pair. Their joint event is then impossible. In all other cases, their directed chains are disjoint or concatenate without forming a cycle; contracting the two edges leaves \((n-2)!\) permutations, so their joint probability is \(1/[n(n-1)]\). For a uniform directed Hamiltonian cycle, the corresponding probabilities are \(1/(n-1)\), zero, and \(1/[(n-1)(n-2)]\), respectively, by the same contraction argument applied to cyclic orders of \(n\) labels. (This is also true at \(n=3\).)

For an open path, the diagonal covariance is \((n-1)/n^2\), the covariance of incompatible distinct edges is \(-1/n^2\), and the covariance of compatible distinct edges is \(1/[n^2(n-1)]\). For a cycle these three numbers are \((n-2)/(n-1)^2\), \(-1/(n-1)^2\), and \(1/[(n-1)^2(n-2)]\).

**2. Covariance operators.** For every zero-diagonal \(H\), summing these entrywise covariance values gives

\[
(\Sigma_P H)_{ab}=
\frac{n h_{ab}-r_a-c_b-h_{ba}}{n(n-1)}
+\frac{s}{n^2(n-1)},\qquad a\ne b,
\]

and

\[
(\Sigma_C H)_{ab}=
\frac{(n-1)h_{ab}-r_a-c_b-h_{ba}}{(n-1)(n-2)}
+\frac{s}{(n-1)^2(n-2)},\qquad a\ne b.
\]

These formulas also give \(\Sigma_P\mathbf1=\Sigma_C\mathbf1=0\). Here \(\mathbf1\) denotes the constant off-diagonal edge vector.

**3. Complete orthogonal edge decomposition.** The real edge space splits orthogonally into five mutually orthogonal pieces, the first two listed after the constant being two subspaces that share an eigenvalue:

\[
\begin{array}{ll}
\mathcal U_0:&h_{ab}=\text{constant},\quad\dim\mathcal U_0=1;\\
\mathcal U_{+}:&h_{ab}=u_a+u_b,\ \sum u_a=0,\quad\dim\mathcal U_+=n-1;\\
\mathcal U_{-}:&h_{ab}=v_a-v_b,\ \sum v_a=0,\quad\dim\mathcal U_-=n-1;\\
\mathcal S:&H=H^\top,\ r_a=0\ \forall a,\quad\dim\mathcal S=n(n-3)/2;\\
\mathcal A:&H=-H^\top,\ r_a=0\ \forall a,\quad\dim\mathcal A=(n-1)(n-2)/2.
\end{array}
\]

Orthogonality follows from transposition symmetry and zero row sums. In the symmetric subspace the row-sum map onto \(\mathbb R^n\) has rank \(n\) for \(n\ge3\): if a vector annihilates its image then \(x_a+x_b=0\) for every edge of the complete graph, and a triangle forces all \(x_a=0\). In the antisymmetric subspace its row-sum map has rank \(n-1\), since the complete graph is connected. These facts prove the displayed dimensions, which sum to \(n(n-1)\).

Insert a vector from each subspace into the covariance-operator identities. For \(\mathcal U_+\), \(r_a=(n-2)u_a\); for \(\mathcal U_-\), \(r_a=nv_a\) and \(c_b=-nv_b\). On \(\mathcal S\) and \(\mathcal A\) all row and column sums vanish. The resulting eigenvalues for \(\Sigma_P\) are, respectively, \(0,1/[n(n-1)],1/[n(n-1)],1/n,(n+1)/[n(n-1)]\). For \(\Sigma_C\) they are \(0,0,0,1/(n-1),n/[(n-1)(n-2)]\). Their multiplicities are the subspace dimensions, giving both full spectra and the exact rank difference.

**4. Sharp weighted variance envelope.** Adding a constant to all edge weights does not alter the open-path cost variance because exactly \(n-1\) edges are used. Hence \(\operatorname{Var}(Z_w)=\langle H,\Sigma_P H\rangle\) for the centered weight vector \(H\). The smallest and largest positive eigenvalues of \(\Sigma_P\) are \(1/[n(n-1)]\) and \((n+1)/[n(n-1)]\). Its only zero eigenspace is constants, so the spectral theorem yields the claimed sharp two-sided inequality. Orthogonal equality conditions give exactly \(\mathcal U_+\oplus\mathcal U_-\) at the lower endpoint and \(\mathcal A\) at the upper endpoint. Nonzero examples for all \(n\ge3\) are the potential \(h_{ab}=\mathbf1\{a=1\}+\mathbf1\{b=1\}-2/n\) and a unit antisymmetric flow supported on any three-cycle. This also proves that both constants are attained.

## Verification

`verify.py` uses only the Python 3 standard library. It enumerates every open permutation and every oriented Hamiltonian cycle (with a fixed initial label) for \(n=3,4,5,6,7\). It computes the empirical covariances by exact integer counts and rational arithmetic, checks all covariance entries against the formulas in Step 1, and checks the operator action on each of the five projected parts of every coordinate basis vector. Testing the coordinate basis certifies a complete matrix identity for these five finite sizes, rather than relying on sampled vectors. The program also checks weighted quadratic forms and component orthogonality. The run produced `PASS 47656 exact covariance and spectral assertions (all paths and oriented cycles for n=3..7)`.

The theorem for arbitrary \(n\) is proved in the preceding four steps. The finite exact enumeration is a separate implementation check, not the logical basis of the unrestricted claim.

## Relationship to prior work

Diaconis, Evans, and Graham (2013) analyze the occurrence of *specific originally adjacent labels* in uniform permutations, and establish a set-level equivalence with fixed points. Their contraction argument concerns such selected adjacencies; the present result concerns the full \(n(n-1)\)-coordinate directed-edge covariance operators, their complete eigenvalue multiplicities, the path-to-cycle rank collapse, and the extremal variance geometry for arbitrary signed edge weights. Their Section 2 supplies an established counting method, but does not state the present spectral and sharp-inequality conclusions.

The general quadratic assignment and random traveling-salesperson literature studies permutation cost functions. Sutcliffe, Solomon, and Edwards (2012), for example, compute the variance over *symmetric traveling-salesperson tours* for given costs. That object is cyclic and unoriented, so it does not state the boundary-sensitive covariance of all directed open-path edges or its extremizing circulation class. Alhakim (2004) studies an overlapping finite-alphabet Markov chain constructed from independent letters, with replacement, a different probability model from permutations without repeated labels. These related results motivate careful comparison rather than assuming that a different matrix spectrum is new solely because its entries differ.

## Limitations

This is an exact second-moment theorem; it does not assert asymptotic normality, independence of edge indicators, concentration inequalities, or an optimal-path algorithm. The weights are deterministic, arbitrary real numbers and need not satisfy triangle inequalities. The lower bound is for *centered* edge weights and is vacuous when all weights are equal. At \(n=3\), the symmetric zero-row-sum eigenspace has dimension zero, as explicitly permitted by the multiplicity formulas. Earlier general quadratic-assignment moment calculations could potentially be specialized to reproduce the covariance entries; the priority of this **complete spectral decomposition and sharp equality classification** has not been independently established. Full text of the closest symmetric-tour variance paper was not inspected; its abstract permits only an object-level comparison, not a complete literature exclusion.

## References

1. Persi Diaconis, Steven N. Evans, and Ron Graham, *Unseparated pairs and fixed points in random permutations*, Statistics Technical Report 822, University of California, Berkeley (1 August 2013), https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf. Material inspected: introduction and Sections 2 and 5, including exact adjacent-pair counting and circular-adjacency arguments.
2. Paul Sutcliffe, Andrew Solomon, and Jenny Edwards, *Computing the variance of tour costs over the solution space of the TSP in polynomial time*, Computational Optimization and Applications 53 (2012), 711–728, DOI: 10.1007/s10589-012-9472-0. Abstract inspected.
3. Abbas Alhakim, *On the eigenvalues and eigenvectors of an overlapping Markov chain*, Probability Theory and Related Fields 128 (2004), 589–605, DOI: 10.1007/s00440-003-0321-z. The methodological sections and application discussion of the accessible author-shared text were inspected.
4. G. W. Graves and A. B. Whinston, *An algorithm for the quadratic assignment problem*, Management Science 16 (1970), 453–471, DOI: 10.1287/mnsc.16.7.453. General context based on its abstract; not examined as a covering full-text theorem.
