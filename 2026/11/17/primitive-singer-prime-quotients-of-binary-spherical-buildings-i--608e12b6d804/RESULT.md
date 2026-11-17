# Primitive Singer-prime quotients of binary spherical buildings: integral homology and unbounded Bockstein cup-length

## Finding

For integers \(n\ge4\) and odd primes \(p\) satisfying \(\operatorname{ord}_p(2)=n\), define \(B_n\) as the finite spherical type-A building whose simplices are strict chains of nonzero proper subspaces of \(V=\mathbb F_{2^n}\) regarded over \(\mathbb F_2\). Choose a multiplicative element \(a\in V^\times\) of order \(p\) and form the **ordinary geometric quotient** \(Y_{n,p}=|B_n|/\langle a\rangle\). Set \(d=n-2\) and \(b=2^{n(n-1)/2}\).

The action is free and \(\pi_1(Y_{n,p})\cong C_p\). Its integral homology is

\[
H_i(Y_{n,p};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/p,&1\le i<d\text{ and }i\text{ odd},\\
0,&1\le i<d\text{ and }i\text{ even},\\
\mathbb Z^{(b+(-1)^d(1-p))/p},&i=d,\\
0,&i>d.
\end{cases}
\]

Write \(\xi\in H^1(Y_{n,p};\mathbb F_p)\) for the nonzero class classifying the covering and \(\eta=\beta\xi\in H^2(Y_{n,p};\mathbb F_p)\) for its mod-\(p\) Bockstein. The classifying map from the quotient to \(BC_p\) is a cohomological isomorphism in every degree strictly less than \(d\) and injective in degree \(d\). Thus every monomial \(\eta^k\) with \(2k\le d\), and every \(\xi\eta^k\) with \(2k+1\le d\), is nonzero; \(\xi^2=0\). These monomials give the entire ring of classes below top degree. For each odd prime \(n\ge5\) and each prime factor \(p\mid 2^n-1\), the top product \(\xi\eta^{(n-3)/2}\) is nonzero. In particular this infinite family has unbounded mod-\(p\) cup-length.

## Assumptions and scope

Here \(\operatorname{ord}_p(2)=n\) is the multiplicative order of two modulo the odd prime \(p\). This is essential: it makes multiplication by each nonidentity group element irreducible over \(\mathbb F_2\). The asserted topological space is the orbit space of the **finite spherical building**, not its classifying space or an affine Bruhat–Tits building. The quotient carries a finite CW (or simplicial-cell) structure with one cell for each flag orbit, since the action has no simplex inversions. It need not be an abstract simplicial complex.

## Proof

**1. Irreducibility and freeness.** The element \(a\) has order \(p\), and its minimal polynomial over \(\mathbb F_2\) has degree \(\operatorname{ord}_p(2)=n\). The same is true for each \(a^j\), \(1\le j<p\), because its order is also \(p\). Consequently no such multiplication has any nonzero proper invariant \(\mathbb F_2\)-subspace. An element stabilizing a flag preserves each rank and therefore each subspace; thus no nonidentity element fixes a simplex. A fixed point in the geometric realization would stabilize its unique open simplex, impossible. The action is free.

**2. Cover and fundamental group.** The classical Solomon–Tits theorem says that the building \(B_n\) has the homotopy type of a wedge of \(b=2^{n(n-1)/2}\) spheres of dimension \(d=n-2\). In particular, \(|B_n|\) is connected and simply connected for \(n\ge4\). Its free degree-\(p\) quotient is therefore a regular covering and its universal covering, with deck group \(C_p\). Hence \(\pi_1(Y_{n,p})=C_p\).

**3. All integral homology.** In the Cartan–Leray homology spectral sequence

\[
E^2_{i,j}=H_i(C_p;H_j(B_n;\mathbb Z))\Longrightarrow H_{i+j}(Y_{n,p};\mathbb Z),
\]

only the fiber rows \(j=0\) and \(j=d\) can be nonzero. For total degree strictly less than \(d\), the sole row is \(j=0\); no differential can affect it in these degrees. The familiar periodic integral homology of an odd-prime cyclic group is \(H_i(C_p;\mathbb Z)=\mathbb Z/p\) for positive odd \(i\), zero for positive even \(i\), and \(\mathbb Z\) in degree zero. This yields the lower groups. Since \(Y_{n,p}\) is a finite \(d\)-complex, its top integral homology is a subgroup of the free top cellular-chain group and so is free. Rationally only degrees zero and \(d\) can survive. The Euler characteristic of a free simplicial quotient is \(\chi(Y_{n,p})=\chi(B_n)/p=(1+(-1)^d b)/p\). Solving \(\chi(Y)=1+(-1)^d\operatorname{rank} H_d(Y)\) gives the stated rank; cells above \(d\) do not exist.

**4. Cup products.** The regular covering defines a classifying map \(c:Y_{n,p}\to BC_p\) and a fiber sequence up to homotopy \(B_n\to Y_{n,p}\xrightarrow{c} BC_p\). In its mod-\(p\) cohomology Serre spectral sequence, only fiber rows zero and \(d\) occur. The first possible differential entering the base row is \(d_{d+1}\), and it can only affect base degree at least \(d+1\). It follows that \(c^*\) is an isomorphism below degree \(d\), and injective in degree \(d\). As \(p\) is odd,

\[
H^*(BC_p;\mathbb F_p)=\Lambda(s)\otimes\mathbb F_p[t],\quad |s|=1,\ |t|=2,\ \beta(s)=t.
\]

Naturality gives \(\xi=c^*s\), \(\eta=c^*t=\beta\xi\), and all listed products survive. There may be additional cohomology classes in degree \(d\); no complete description of products with those extra classes is asserted.

**5. Infinitely many admissible pairs.** If \(n\ge5\) is an odd prime, then each prime \(p\mid2^n-1\) has \(\operatorname{ord}_p(2)\mid n\), and order one is impossible since \(p\) cannot divide \(2-1=1\). Therefore its order equals \(n\), and \(\xi\eta^{(n-3)/2}\) is a nonzero product of \((n-1)/2\) positive-degree classes. Since odd primes \(n\) are unbounded, so is the cup-length. The topological dimension bounds cup-length above by \(d\); the assertion is the displayed lower bound.

## Verification

The standard-library code in `checks/singer_building_verifier.py` independently constructs all proper subspaces and strict flags for \(n=4,5\), multiplies in the specified irreducible binary fields, tests every nonidentity group element against every subspace, and checks that the quotient flag counts and Euler characteristic agree with the theoretical values. It reports \((f_0,f_1,f_2)=(13,63,63)\) and top rank \(12\) for \((n,p)=(4,5)\), and \((f_0,f_1,f_2,f_3)=(12,150,420,315)\) and top rank \(34\) for \((n,p)=(5,31)\). See `checks/output.txt`. This is finite corroboration, **not** an exhaustive verification for unbounded \(n\); the argument above proves the general statement.

## Relationship to prior work

The underlying spherical building and its Solomon–Tits sphere-wedge theorem are classical, and the group-cohomological spectral-sequence machinery is standard. Church–Farb–Putman [1], §1.1, explains the building and Steinberg module in a different arithmetic setting. Kang–Li–Wang [2] concerns zeta and \(L\)-functions of finite quotients of **affine** apartments/buildings, rather than the present free quotients of finite **spherical** type-A buildings and their integral homology and mod-\(p\) products. Existing calculations for full Singer groups in rank four concern a different, nonfree quotient: such calculations do not determine the covering classes and unbounded cup products of these proper irreducible prime-order subgroup quotients.

## Limitations

The theorem assumes \(n\ge4\) and the precise primitive-prime condition. For composite \(n\) not meeting the condition, freeness can fail and the conclusion is not asserted. The ring statement describes all degrees below \(d\) and the subalgebra detected by the covering map through degree \(d\), **not** the entire top-degree multiplication structure. This is a synthesis of classical homotopy and group-cohomology results for a specific free Singer action; unlocated equivalent formulations remain a literature priority risk. No independent external audit is claimed here.

## References

1. T. Church, B. Farb, A. Putman, *Integrality in the Steinberg module and the top-dimensional cohomology of \(\mathrm{SL}_n(\mathcal O_K)\)*, original preprint 2015-01-06, https://arxiv.org/abs/1501.01307, especially §1.1 and its explanation of the classical Solomon–Tits theorem.
2. M.-H. Kang, W.-C. W. Li, C.-J. Wang, *Zeta and \(L\)-functions of finite quotients of apartments and buildings*, original preprint 2015-05-05, https://arxiv.org/abs/1505.00902, §§1–2 (affine building setting).
3. Solomon–Tits theorem and the Cartan–Leray/Serre spectral sequences, classical results as stated and applied in the proof above.
