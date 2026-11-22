# An infinite genus-four-multiple collision of hyperelliptic spin Frobenius schemes

## Finding

**Theorem.** Let \(r\ge1\) be any integer, \(q\) any odd prime power, and \(g=4r\). There are smooth genus-\(g\) hyperelliptic curves \(C_A,C_B\) over \(\mathbb F_q\) with geometric branch-point Frobenius types \((8r,2)\) and \((8r,1,1)\), respectively, such that their finite étale schemes of odd theta characteristics are isomorphic over \(\mathbb F_q\), and likewise their schemes of even theta characteristics. Both full spin-scheme zeta functions agree in each parity, while their branch-point zeta functions differ.

In particular, writing \(O_n\) and \(E_n\) for the numbers of odd and even theta characteristics fixed by the \(n\)-th Frobenius power, both curves satisfy, for every odd integer \(n\ge1\),

\[
O_n=0,\qquad E_n=2^{\gcd(8r,n)}.
\]

For every even \(n\), their complete branch-point Frobenius cycle partitions after base change to \(\mathbb F_{q^n}\) coincide, so both spin counts coincide. The collision is realized over *every* finite field of odd characteristic and in infinitely many genera.

## Assumptions and scope

The curves are smooth, projective hyperelliptic curves in characteristic different from two. The branch divisor \(B\) has \(2g+2=8r+2\) geometric points; the hyperelliptic double-cover pencil has divisor class \(H\) of degree two. By a theta characteristic we mean a line-bundle class \(D\) with \(2D\sim K_C\). Its parity is \(h^0(C,D)\bmod2\). The odd and even theta-characteristic schemes are reduced finite étale schemes since the characteristic is odd; isomorphism here means that their Frobenius actions on geometric points have the same cycle multiset. No assertion about isomorphism or isogeny of the curves or their Jacobians is made.

## Proof

**1. Canonical subset description and parity.** Write \(B=\{P_1,\ldots,P_{2g+2}\}\). For each subset \(S\subseteq B\) with \(|S|\equiv g+1\pmod2\), define

\[
D_S=\sum_{P\in S}P+\frac{g-1-|S|}{2}H.
\]

Since \(2P\sim H\) for each branch point and \(K_C\sim(g-1)H\), this is a theta characteristic. The relation \(\sum_{P\in B}P\sim(g+1)H\) shows \(D_S\sim D_{B\setminus S}\). Standard hyperelliptic reduced-divisor uniqueness (equivalently, the even-subset description of Jacobian two-torsion, which has \(2^{2g}\) elements) shows that these are the *only* identifications; there are \(2^{2g}\) complement classes. For \(s=|S|\le g+1\), the hyperelliptic linear-series formula gives

\[
h^0(C,D_S)=\frac{g+1-s}{2}.
\]

For \(s=g+1\) the class has no sections, and for \(s<g+1\) this follows from the complete hyperelliptic pencil with \((g-1-s)/2\) multiples of \(H\). All descriptions commute with the permutation of branch points, so they identify the actual arithmetic Frobenius action (not just its cardinality) on each parity.

**2. Odd Frobenius powers.** Put \(L=8r\). Let \(n\ge1\) be odd, \(d=\gcd(L,n)\), and \(e=L/d\). Then \(d\) is odd and \(8\mid e\), while the central admissible subset size is \(g+1=ed/2+1\), which is odd.

For the permutation with branch type \((L,2)\), its \(n\)-th power consists of \(d\) cycles of length \(e\) and one cycle of length two. Every cycle is even. Hence no subset of admissible odd cardinality is literally stable. A subset class \([S]=\{S,B\setminus S\}\) is fixed precisely when its representative is sent to its complement. Such a subset must alternate on each of the \(d+1\) even cycles. There are exactly \(2^{d+1}\) alternating subsets and thus \(2^d\) complementary pairs, each of size \(g+1\) and parity even. Hence \(O_n=0\), \(E_n=2^d\).

For the permutation with branch type \((L,1,1)\), its \(n\)-th power has \(d\) cycles of length \(e\) and two fixed points. No subset maps to its complement because fixed points forbid alternation. A literally fixed representative of odd admissible cardinality at most \(g+1\) consists of exactly one fixed point together with \(j\) whole length-\(e\) cycles, where \(0\le j\le(d-1)/2\). No such subset can have central size \(g+1\): that would require \(j=d/2\). The number of resulting theta classes is therefore

\[
2\sum_{j=0}^{(d-1)/2}\binom dj=2^d,
\]

using oddness of \(d\). Each representative has \(s=1+je\) and thus

\[
h^0(C,D_S)=\frac{ed/2-je}{2}=\frac{e(d-2j)}4,
\]

an *even* integer since \(8\mid e\). Thus again \(O_n=0\), \(E_n=2^d\).

**3. Even Frobenius powers.** If \(n\) is even, the two-cycle in \((L,2)\) becomes two fixed points; the \(L\)-cycle has the same \(n\)-th power in both cases. Consequently the two branch permutations raised to \(n\) have identical cycle multisets, hence conjugate actions on the subset/complement models for both theta parities. All spin fixed-point counts are equal.

**4. All extensions and arithmetic realization.** A permutation's finite-orbit multiset is determined by its fixed-point counts at every positive power through Möbius inversion. Equality for every \(n\) and each parity therefore gives isomorphic finite étale odd and even theta schemes, separately. For realization over any odd \(\mathbb F_q\), choose a monic irreducible polynomial \(P_L\) of degree \(L\) and a distinct monic irreducible quadratic \(Q_2\), and set \(C_A:y^2=P_L(x)Q_2(x)\). For \(C_B\) replace \(Q_2\) by \((x-a)(x-b)\) for distinct \(a,b\in\mathbb F_q\). Both defining polynomials are squarefree of degree \(2g+2\); their smooth projective normalizations have genus \(g\) and exactly the required geometric branch splitting. For odd \(n=1\), the two branch schemes have respectively zero and two rational points; their zeta functions differ. This completes the theorem.

## Verification

The attached standalone Python program `verify_spin_collision.py` implements (i) the branch-cycle subset fixed-point formula in exact integer arithmetic, and (ii) an independent exhaustive enumeration of all \(2^{2g}\) theta classes and their orbits for genera four and eight. It verifies all powers in each case and tests the symbolic count for \(1\le r\le10\) over all powers through \(8r\). These checks reproduce the same odd/even Frobenius spectra; the quantifier over all \(r\) is justified by the preceding proof rather than by finite computation. Run with `python3 verify_spin_collision.py`; the expected terminating line is `INFINITE_HYPERELLIPTIC_SPIN_COLLISION_CHECKS_OK`.

## Relationship to prior work

The subset description of hyperelliptic theta characteristics is classical. Braden and Disney-Hogg, *Orbits of Theta Characteristics* (2024), study automorphism-group actions and invariant spin structures. The already-known genus-four collision between the branch partitions \((8,2)\) and \((8,1,1)\) is **not** claimed as new. This theorem extends the arithmetic collision, with the same two structural kinds of branch splitting, to **every** positive multiple of four in the genus, with a uniform parity argument and field-by-field realizability. A general automorphism-orbit method alone does not state this specific arithmetic equality for all genera. As with any novelty assessment, unindexed equivalent earlier formulas remain possible.

## Limitations

The conclusion concerns only theta-characteristic finite étale schemes, separately by parity, and not their additional geometric incidence relations, Jacobian polarizations, curve zeta functions or curve isomorphism classes. The construction requires odd characteristic. It supplies a family of indistinguishable pairs, not a classification of every possible spin-spectrum collision in all genera. Reproducibility tests in finitely many genera are not an independent proof of the infinite statement, and no independent external audit has been performed.

## References

1. H. W. Braden and L. Disney-Hogg, *Orbits of Theta Characteristics*, arXiv:2404.09890v1 (first public 2024-04-15), https://arxiv.org/html/2404.09890v1 .
2. *2-Selmer parity for hyperelliptic curves in quadratic extensions*, Proceedings of the London Mathematical Society, https://doi.org/10.1112/plms.12565 . Background on even-degree hyperelliptic models and even-subset two-torsion, not the present theorem.
3. T. Misme, *Computing Theta Characteristics and their Galois action on general curves of moderate genus*, arXiv:2610.29449 (2026). Computational Galois-theta context, not a stated infinite-genus collision; this later source is supporting context only.
