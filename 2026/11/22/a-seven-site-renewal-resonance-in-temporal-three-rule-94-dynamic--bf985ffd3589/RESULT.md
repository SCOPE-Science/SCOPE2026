# A seven-site renewal resonance in temporal-three Rule 94 dynamics

## Finding

Let \(F_n\) be the synchronous elementary cellular automaton Rule 94 on the **indexed** binary cycle \(\mathbb Z/n\mathbb Z\), with \(n\ge3\). Let \(c_n\) count distinct primitive temporal three-cycle **orbits** of \(F_n\), without quotienting by spatial rotation. Put

\[
P(z)=1-z^2-z^3,\qquad Q(z)=1-z^2-z^3-3z^7.
\]

Then the complete all-circumference counting law is

\[
\boxed{\sum_{n\ge3}c_nz^n
=-\frac z3\frac{d}{dz}\log\frac{Q(z)}{P(z)}
=\frac{z^7(7-5z^2-4z^3)}{P(z)Q(z)}.}
\]

In particular, primitive temporal three-cycles exist **exactly** at circumferences \(n=7\) and \(n\ge9\). There are none at \(n=8\) or \(3\le n\le6\); the first nonzero orbit counts are \(c_7=7\), \(c_9=9\), \(c_{10}=10\), \(c_{11}=11\), \(c_{12}=24\). Writing \(\lambda>1\) for the unique positive root of

\[
\lambda^7-\lambda^5-\lambda^4-3=0,
\]

one has \(\lambda=1.4611264371\ldots\) and \(c_n\sim\lambda^n/3\) as \(n\to\infty\). The growth rate exceeds that of fixed configurations, whose dominant base is the plastic constant \(\beta=1.3247179572\ldots\), the positive root of \(\beta^3-\beta-1=0\).

## Assumptions and scope

For a configuration \(x\in\{0,1\}^{\mathbb Z/n\mathbb Z}\), update all sites in parallel by

\[
(F_nx)_i=f(x_{i-1},x_i,x_{i+1}),\qquad
f(a,b,c)=\left\lfloor\frac{94}{2^{4a+2b+c}}\right\rfloor\bmod2.
\]

Thus the outputs for neighborhoods \(111,110,101,100,011,010,001,000\) are respectively \(0,1,0,1,1,1,1,0\). A primitive temporal three-cycle orbit is a set \(\{x,F_nx,F_n^2x\}\) with \(F_n^3x=x\) and \(F_nx\ne x\). Such orbits have exactly three distinct members. Spatial translations are **not** identified; the cyclic indexing is part of the finite dynamical system.

## Proof

**1. Finite spacetime transfer.** For \(p\in\{1,3\}\), set \(\mathcal C_p=\{0,1\}^p\), with time coordinates indexed modulo \(p\). Form the directed graph \(G_p\) whose vertices are pairs \((u,v)\in\mathcal C_p^2\) and whose edges are

\[
(u,v)\longrightarrow(v,w)
\quad\Longleftrightarrow\quad
v_{t+1}=f(u_t,v_t,w_t)\quad
\text{for every }t\in\mathbb Z/p\mathbb Z.
\]

Let \(A_p\) be its ordinary integer adjacency matrix. A closed walk of spatial length \(n\) is in bijection with a cyclic array of \(n\) complete \(p\)-periodic time columns satisfying every local update. Determinism gives a bijection between those arrays and configurations fixed by \(F_n^p\). Therefore, **for all** \(n\ge1\),

\[
\operatorname{tr}(A_p^n)=\#\operatorname{Fix}(F_n^p).
\]

This identity uses labelled sites; no division by a spatial symmetry factor occurs.

**2. Exact determinant calculation.** The graph \(G_1\) has four vertices and five edges, while \(G_3\) has 64 vertices and 65 edges. Directly applying the displayed local rule yields

\[
\boxed{\det(I-zA_1)=(1-z)(1-z^2-z^3),}
\]

\[
\boxed{\det(I-zA_3)=(1-z)(1-z^2-z^3-3z^7).}
\]

These are finite exact identities, **not** guesses from initial coefficients. To check them from first principles without a symbolic-algebra package, `verify_rule94.py` constructs all graph edges and computes the trace of each power up to the full matrix dimension by exact integer walk enumeration. The coefficients \(d_k\) of \(\det(I-zA_p)\) are then reconstructed through the Newton identities

\[
d_0=1,\qquad k d_k=-\sum_{j=1}^{k}d_{k-j}\operatorname{tr}(A_p^j).
\]

All 64 coefficients are verified (and every unlisted coefficient is zero). The finite edge lists and expected determinant coefficients are additionally recorded in `transfer_certificate.json`. This exact finite calculation closes the only nontrivial computational lemma.

**3. Primitive orbit generating function.** For any finite square matrix \(A\), the formal identity

\[
\sum_{n\ge1}\operatorname{tr}(A^n)z^n
=-z\frac{d}{dz}\log\det(I-zA)
\]

follows by the determinant expansion or Newton identities. A configuration satisfying \(F_n^3x=x\) has least temporal period either one or three. Hence exactly \(3c_n\) configurations have primitive period three, and subtraction of the two determinants gives the asserted rational generating function.

**4. Exact support and the isolated hole.** Write \(U(z)=3z^7/P(z)\). Formal expansion gives

\[
\sum_{n\ge3}\frac{3c_n}{n}z^n
=-\log(1-U(z))
=\sum_{k\ge1}\frac{3^k z^{7k}}{k}(1-z^2-z^3)^{-k}.
\]

Every displayed coefficient is nonnegative. For \(k\ge1\), the positive coefficients of \((1-z^2-z^3)^{-k}\) occur precisely at exponents of the form \(2a+3b\), with \(a,b\ge0\). Thus \(c_n>0\) precisely when \(n=7k+2a+3b\) for some \(k\ge1\). In the domain \(n\ge3\), this is equivalent to \(n=7\) or \(n\ge9\): the unique gap after the onset is \(n=8\).

**5. Sharp exponential asymptotic.** The smallest positive zero \(r\) of \(Q\) is characterized by \(r^2+r^3+3r^7=1\), and \(\lambda=1/r\). Every complex zero \(w\) of \(Q\) satisfies \(|w|\ge r\) by the triangle inequality. Equality forces \(w^2,w^3,w^7\) all to have positive real phase; because \(\gcd(2,3)=1\), this forces \(w=r\). Moreover \(Q'(r)<0\), so the pole is simple. Since \(P(r)=3r^7>0\), the positive zero of \(P\) is strictly farther away. The logarithmic-derivative formula therefore has a unique dominant simple pole with principal part \(1/[3(1-z/r)]\), proving \(c_n\sim r^{-n}/3\). For the fixed point count, \(\det(I-zA_1)=(1-z)P(z)\) similarly gives dominant base \(\beta\). The strict inequality \(\lambda>\beta\) follows, for instance, by evaluating their defining polynomials at \(7/5\): the polynomial defining \(\beta\) is positive and the one defining \(\lambda\) is negative there.

## Verification

Run `python3 verify_rule94.py` and `python3 direct_check.py` from the directory containing the files. The first script is an **all-size certificate** of the exact 64-vertex determinant identities: it checks all graph edges, all determinant coefficients, and the first hundred induced nonnegative orbit counts. The second is independent state-by-state simulation using a literal truth table and checks every initial binary configuration on each labelled ring of lengths three through sixteen against both determinant-derived return counts. The primary proof does not rely on extrapolating these sixteen-site experiments.

## Relationship to prior work

Wolfram's original elementary cellular-automaton framework (1983) defines the rule class. Weisstein's Rule 94 entry documents single-seed evolutions, not cyclic temporal-three return enumeration. Anderson and Sturges (2013) exhibit qualitative period-three bands and a period-six orbit for Rule 94; this supplies motivation but not an all-length primitive-three census. Schüle and Stoop (2012) classify Rule 94 as almost equicontinuous with an invariant word, a topological result that does not imply the present rational orbit count. Rasolonjanahary and Vasiev (2020) show local restoration of stationary **spatially** three-periodic patterns for Rule 94; this differs from the temporal three-cycle classification here. The bit-complement conjugate Rule 133 has the same temporal counts, so a prior result formulated for Rule 133 could also cover this theorem; such equivalent coverage was specifically searched for but not identified.

## Limitations

The theorem counts **initial configurations already on** primitive temporal three-cycles, not the sizes of their attraction basins or all possible recurrent periods. The spectral asymptotic concerns the limit of ring circumference; it does not assert that a uniformly random initial configuration reaches a three-cycle with high probability. The finite transfer determinant is supplied with executable exact-integer verification but has not received independent external review. Historical-priority searches cannot rule out unindexed equivalent results, particularly formulations for Rule 133 or generic tables of elementary cellular-automaton return counts.

## References

- S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics **55** (1983), 601–644; first journal publication 1983-07-01. https://doi.org/10.1103/RevModPhys.55.601
- E. W. Weisstein, *Rule 94*, Wolfram MathWorld. https://mathworld.wolfram.com/Rule94.html
- R. J. Anderson and R. H. Sturges, *System Behaviors and Measures: Logical Complexity and State Complexity in Naval Weapons Elevators*, Complex Systems **22** (2013), 247 ff., particularly pp. 254–255. https://doi.org/10.25088/ComplexSystems.22.3.247
- M. Schüle and R. Stoop, *A Full Computation-relevant Topological Dynamics Classification of Elementary Cellular Automata*, arXiv:1107.2080v7 (2012-06-22), especially Corollary 5. https://arxiv.org/abs/1107.2080
- M. Rasolonjanahary and B. Vasiev, *Formation of Morphogenetic Patterns in Cellular Automata*, Computational Science – ICCS 2020, 359–373, particularly the section on spatially three-periodic patterns. https://pmc.ncbi.nlm.nih.gov/articles/PMC7304752/
