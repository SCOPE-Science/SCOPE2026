# Arithmetic spectral and exact-memory laws for coarse integer-base dynamics

## Finding

Fix an integer \(q\geq2\), let \(X_0\) be Lebesgue-uniform on \([0,1)\), and choose **any predetermined** sequence of integer slopes \(b_1,b_2,\ldots\geq2\). Iterate \(X_t=\{b_tX_{t-1}\}\), and observe the equal-cell label \(J_t=\lfloor qX_t\rfloor\in\{0,\ldots,q-1\}\). Then the entire observed process is a possibly time-inhomogeneous stationary-uniform Markov chain, with exact transition kernel

\[
 Q_b(j,k)=\frac{1}{b}\#\{0\leq r<b:bj+r\equiv k\pmod q\}.
\]

The kernels commute and satisfy \(Q_bQ_c=Q_{bc}\) for all integers \(b,c\geq2\). Consequently, for \(B=b_{t+1}\cdots b_{t+n}\), the exact conditional distance from the uniform distribution on \(q\) cells is independent of the starting cell and is

\[
 \left\|\mathcal L(J_{t+n}\mid J_t=j)-\operatorname{Unif}\{0,\ldots,q-1\}\right\|_{\rm TV}
 =\frac{r(q-r)}{qB},\qquad r=B\bmod q,\quad 0\leq r<q.
\]

In particular, \(J_{t+n}\) is exactly independent of the entire observed past \((J_0,\ldots,J_t)\), for every admissible past, **if and only if** \(q\mid B\). Exact loss of memory may therefore result from a composition even when neither factor individually destroys memory: for \(q=6\), slopes \(2\) and \(3\) make the two-step kernel exactly uniform, although both one-step kernels are nonuniform.

There is also a complete arithmetic spectrum. Form the directed functional graph on \(\{1,\ldots,q-1\}\) under \(k\mapsto bk\pmod q\), regarding a path that reaches residue \(0\) as terminated. Let \(\mathcal C_{q,b}\) be its directed cycles not containing zero, and let \(M\) be the total number of residues lying in these cycles. Then

\[
\boxed{\det(zI-Q_b)=(z-1)z^{q-1-M}
\prod_{C\in\mathcal C_{q,b}}\bigl(z^{|C|}-b^{-|C|}\bigr).}
\]

Thus the nonconstant eigenvalues are zero or \(b^{-1}\) times roots of unity; their nonzero modulus is **exactly \(1/b\)**, for every cell resolution \(q\), including composite and noncoprime cases. In particular, the nontrivial spectral radius is at most \(1/b\), and the transient zero multiplicity and all cyclic eigenphases are exactly determined by modular multiplication.

## Assumptions and scope

All integers \(q,b_1,b_2,\ldots\) are finite and satisfy the stated bounds. The map is defined modulo one on the half-open interval; all claims involving conditional distributions concern positive-probability cylinder histories, so endpoints of partition cells have zero measure. The environment is fixed in advance (or sampled independently of \(X_0\), with conclusions conditioned on its realization). No claim is made for state-dependent choice of slope or noninteger beta transformations. Uniformity and independence are under Lebesgue-distributed \(X_0\); they need not hold for a singular initial distribution.

The spectral formula concerns the \(q\)-state stochastic matrix \(Q_b\), **not** the full transfer operator on an infinite-dimensional function space. In the exact-memory formula, the product \(B\) is the product of slopes over the indicated interval, not a time average. The result gives exact finite-time independence only for coarse cells, not for the underlying real-valued states.

## Proof

**1. Conditional uniformity and the kernel.** Define \(I_j=[j/q,(j+1)/q)\). Under \(T_b(x)=\{bx\}\), the interval \(I_j\) is mapped with constant slope \(b\) through exactly \(b\) consecutive equal target cells, counted with multiplicity, whose labels are \(bj,bj+1,\ldots,bj+b-1\pmod q\). The preimage in \(I_j\) of each occurrence of a target cell has length \(1/(bq)\), and maps linearly and bijectively onto that complete target cell. Hence, if the input is uniform in \(I_j\), then the chance of target label \(k\) is exactly \(Q_b(j,k)\), and **conditional on that target label** the output is again uniform in \(I_k\). This conclusion also holds when conditioned on any prior cell-label history, provided the last conditional distribution is uniform in its cell. Since \(X_0\mid\{J_0=j\}\) is uniform in \(I_j\), induction proves the Markov assertion for every fixed slope sequence and shows each \(J_t\) is uniform: every \(T_b\) preserves Lebesgue measure. Explicitly, rows sum to one by counting \(b\) residues, and columns sum to one because \(T_b\) preserves Lebesgue measure.

**2. Exact kernel semigroup.** Applying the preceding conditional-uniformity induction twice and using \(T_c\circ T_b=T_{bc}\) yields \(Q_bQ_c=Q_{bc}\); the same argument proves the \(n\)-step kernel \(Q_B\). Since multiplication of the integer slopes commutes, all these kernels commute, even though the observed path distributions depend on their order. (The semigroup identity does **not** assert that consecutive observation strings are invariant under exchanging slope order.)

**3. Sharp variation distance and exact loss of memory.** Write \(B=aq+r\), \(0\leq r<q\). For each starting cell, the multiset of \(B\) consecutive target residues contains exactly \(r\) residues \(a+1\) times and the other \(q-r\) residues \(a\) times. Subtracting uniform mass \(1/q\), the positive deviations equal \((q-r)/(qB)\) at the first \(r\) residues, and the negative deviations equal \(-r/(qB)\) at the others. Their common total is \(r(q-r)/(qB)\), proving the equality for total variation (with both sides zero if \(r=0\)). Each row is exactly uniform iff \(r=0\). Since \(J_{t+n}\) conditional on the **whole** history through \(t\) has row law \(Q_B(J_t,\cdot)\), this is equivalent to the claimed complete coarse past/future independence. The necessity is not merely failure of an upper mixing bound: if \(r\ne0\), every conditional row is nonuniform.

**4. Fourier conjugacy and complete characteristic polynomial.** Let \(\zeta=\exp(2\pi i/q)\) and define \(g_k(j)=(1-\zeta^k)\zeta^{kj}\) for residues \(k=1,\ldots,q-1\), with the convention \(g_0=0\). The constant function \(\mathbf 1\) together with \(g_1,\ldots,g_{q-1}\) forms a basis of functions on the \(q\) cells because these are rescaled discrete Fourier characters with nonzero scalings. Directly from the transition counts,

\[
 (Q_b g_k)(j)=\frac1b\sum_{r=0}^{b-1}(1-\zeta^k)\zeta^{k(bj+r)}
 =\frac{1-\zeta^{bk}}b\zeta^{bkj}=\frac1b g_{bk\pmod q}(j),
\]

where \(g_{0}=0\) correctly accounts for frequencies sent to zero, since \(1-\zeta^{bk}=0\) there. Also \(Q_b\mathbf 1=\mathbf1\). Thus the action on the nonconstant Fourier subspace is \(b^{-1}\) times the adjacency operator of the functional graph \(k\mapsto bk\pmod q\), with transitions into residue zero killed. Every finite functional graph decomposes into directed nonzero cycles with directed trees feeding cycles or the killed vertex. Order its vertices so the transient part is triangular with zero diagonal and each cycle gives one permutation block. A cycle of length \(L\) contributes the polynomial \(z^L-b^{-L}\), and each transient vertex contributes one factor \(z\). The constant mode contributes \(z-1\); multiplying the block determinants gives the stated polynomial. This argument includes cases \(\gcd(b,q)>1\), when transient zero eigenvalues need not be semisimple.

**5. Structural consequences.** The cycle formula lists every eigenvalue with algebraic multiplicity; every nonconstant nonzero root has modulus \(1/b\). For example, when \(q=6,b=2\), the residues \(2\) and \(4\) form a two-cycle; the other three nonzero residues are transient, so

\[\det(zI-Q_2)=(z-1)z^3(z^2-1/4).\]

For the same \(q\), \(Q_2Q_3=Q_6\) has all entries \(1/6\), hence exactly loses every coarse-cell dependence after two unequal base changes. No limiting or numerical approximation is required.

## Verification

Run `python3 checks/checker.py` in an environment containing Python 3 and SymPy. It checks the exact row and column sums, the variation-distance identity, and the characteristic polynomial for every \(2\leq q\leq13\) and \(2\leq b\leq12\) (132 pairs), plus semigroup identities at all \(2\leq q\leq11\) and \(2\leq b,c\leq8\). All equality tests use exact symbolic or rational arithmetic, and the package-local checker finished with `PASS`. These finitely many cases are verification witnesses, not a substitute for the proof for all integer parameters.

## Relationship to prior work

Suzuki [1] gives invariant densities and linear response for random beta transformations, including non-independent environments and arbitrary real slopes. Its density results motivate the observation of integer-base systems but do not state this resolution-dependent complete coarse-state spectrum or the sharp arithmetic time to *exact* coarse memory loss. Aimino, Nicol and Vaienti [2] establish broad annealed and quenched limit theory and explicitly consider randomly chosen integer slopes in Example 7.3; their general transfer-operator spectral gap and CLT statements do not supply this complete finite Fourier-cycle factorization or an exact finite-time coarse independence criterion. Vepštas [3] studies beta-transformation spectral problems in a different regime. General Markov-partition calculations imply that finite transition matrices can be obtained by counting inverse branches; that counting principle is not presented here as new. The additional structural assertion is the commuting arithmetic factor family, its exact total-variation law and the *complete* modular-cycle spectrum, including the noncoprime zero modes. The literature comparison is not a guarantee of global publication priority.

## Limitations

The conclusion is about exact finite-cell observations at a fixed integer grid, not the sigma-algebra of all measurable events, nor full physical independence of the underlying trajectory. The spectral theorem applies only to these \(q\)-state factors, not to every possible Markov partition. All hypotheses (integer expanding bases, equal rational cells, initial Lebesgue measure, external deterministic slope schedule) are essential to the conditional-uniformity argument. The result is a self-contained spectral classification of a natural class of finite dynamical factors; it does not provide a new abstract limit theorem or a general spectral theorem for random beta transformations. A structurally equivalent result under another formulation in the literature cannot be excluded.

## References

1. Shintaro Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521, first posted 30 March 2023, https://arxiv.org/abs/2303.17521.
2. Romain Aimino, Matthew Nicol and Sandro Vaienti, *Annealed and quenched limit theorems for random expanding dynamical systems*, arXiv:1310.4359, first posted 16 October 2013, https://arxiv.org/abs/1310.4359, especially Example 7.3.
3. Linas Vepštas, *On the Beta Transformation*, arXiv:1812.10593, first posted 27 December 2018, https://arxiv.org/abs/1812.10593.
