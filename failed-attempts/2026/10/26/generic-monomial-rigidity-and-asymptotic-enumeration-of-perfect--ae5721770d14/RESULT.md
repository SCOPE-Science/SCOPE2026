# Generic monomial rigidity and asymptotic enumeration of perfect evolution algebras over finite fields

## Finding
For a fixed prime power \(q\ge2\), let \(E_A\) denote the evolution algebra with natural basis \(e_1,\ldots,e_n\) and \(e_i e_j=0\) for \(i\ne j\), with \(e_j^2=\sum_{i=1}^n A_{ij}e_i\). Restrict to perfect algebras, equivalently \(A\in\mathrm{GL}_n(\mathbb F_q)\), chosen uniformly.

Define \(\delta_{n,q}=|\mathrm{GL}_n(\mathbb F_q)|^{-1}\sum_A (|\operatorname{Aut}_{\mathbb F_q}(E_A)|-1)\). Then
\[\delta_{n,q}=O_q\bigl(n^2(1-q^{-1})^n\bigr).\]
Consequently
\[\Pr(\operatorname{Aut}(E_A)\ne1)\le\delta_{n,q}\xrightarrow[n\to\infty]{}0,\]
and the number of isomorphism classes of perfect evolution algebras satisfies
\[N_{n,q}=\frac{|\mathrm{GL}_n(\mathbb F_q)|}{n!(q-1)^n}(1+\delta_{n,q}).\]
In particular the multiplicative error tends to zero exponentially up to a polynomial factor. Even under the *uniform distribution on isomorphism classes* rather than matrices, the proportion with nontrivial automorphisms is at most \(2\delta_{n,q}/(1+\delta_{n,q})\).

## Assumptions and scope
The field order \(q\) is a fixed prime power. Asymptotics are for \(n\to\infty\) with constants allowed to depend on \(q\). The natural basis is *not* part of the classification: matrices parameterize the algebras and are identified by full algebra isomorphisms. Perfect means \(E_A^2=E_A\), equivalent to invertibility of its natural-basis structure matrix. A monomial matrix has one nonzero entry in every row and column. The map \(g\mapsto g^{(2)}\) means squaring entries; for monomial \(g\), this remains monomial. All automorphism counts mean rational \(\mathbb F_q\)-points, not automorphism-group schemes.

## Proof
**1. Monomial isomorphisms.** For an algebra isomorphism \(g:E_A\to E_B\), the distinct images of the natural basis satisfy \(g(e_i)g(e_j)=0\) for \(i\ne j\). Writing \(g(e_j)=\sum_k g_{kj}e_k\), this implies \(B (g_{\bullet i}\odot g_{\bullet j})=0\), where \(\odot\) denotes coordinatewise product. Since \(B\) is invertible, the supports of all columns of \(g\) are pairwise disjoint. Invertibility forces every column and every row to contain exactly one nonzero entry; thus \(g\) is monomial. The multiplication identity for an isomorphism \(g:E_A\to E_B\) gives \(B g^{(2)}=gA\); equivalently, changing the natural basis by \(h=g^{-1}\) yields \(B=h^{-1}Ah^{(2)}\). Therefore isomorphism classes are orbits of \(G_n=(\mathbb F_q^\times)^n\rtimes S_n\), of order \(n!(q-1)^n\), and \(\operatorname{Aut}(E_A)\) is the stabilizer.

**2. Stabilizer incidence for all matrices.** Consider uniform (not necessarily invertible) matrices in \(M_n(\mathbb F_q)\). For \(g\in G_n\), let \(c(g)\) denote the codimension of matrices fixed by \(A\mapsto g^{-1}Ag^{(2)}\). Linearity gives \(\Pr(g\cdot A=A)=q^{-c(g)}\). Put \(\varepsilon_{n,q}=\sum_{g\ne1}q^{-c(g)}\).

Write \(g\) as a diagonal vector \(t=(t_1,\ldots,t_n)\) and permutation \(\sigma\). If \(\sigma\) moves \(m\ge2\) letters, it permutes the \(n^2\) matrix positions with exactly \((n-m)^2\) fixed positions. Each nontrivial position orbit contributes at most one free coefficient for each orbit, so the dimension of its fixed matrix space is at most \((n^2+(n-m)^2)/2\). Hence
\[c(g)\ge m(n-m/2)\ge mn/2.\]
There are at most \(n^m\) choices of \(\sigma\) moving \(m\) letters, and \((q-1)^n\) choices of \(t\). With \(r_n=nq^{-n/2}\), for sufficiently large \(n\) such that \(r_n<1\), the contribution of all nonidentity permutations is at most
\[(q-1)^n\frac{r_n^2}{1-r_n}.\]

If \(\sigma=1\), the fixed matrix entries must satisfy \((t_i-t_j^2)A_{ij}=0\). When exactly \(m\ge1\) diagonal coordinates differ from \(1\), the \(m(n-m)\) entries with \(t_i\ne1\), \(t_j=1\) are forced zero. For \(m\le n/2\), their codimension is at least \(mn/2\). Summing over these vectors, the contribution is bounded by
\[\sum_{m=1}^{\lfloor n/2\rfloor}\binom nm(q-2)^m q^{-mn/2}\le\bigl(1+(q-2)q^{-n/2}\bigr)^n-1.\]
For \(q=2\) there are no nonidentity diagonal vectors at all. For \(q>2\) and \(m>n/2\), let \(a_c\) be the number of diagonal entries equal to \(c\ne1\). Every position with \(t_i=t_j=c\ne1\) is forced to vanish, because \(c\ne c^2\) in \(\mathbb F_q^\times\). By Cauchy–Schwarz, at least
\[\sum_{c\ne1}a_c^2\ge\frac{m^2}{q-2}>\frac{n^2}{4(q-2)}\]
entries vanish. Hence all these vectors together contribute at most \((q-1)^n q^{-n^2/[4(q-2)]}\).

Combining, for \(q>2\) and sufficiently large \(n\),
\[\varepsilon_{n,q}\le (q-1)^n\frac{n^2q^{-n}}{1-nq^{-n/2}}+\bigl(1+(q-2)q^{-n/2}\bigr)^n-1+(q-1)^nq^{-n^2/[4(q-2)]}.\]
For \(q=2\), retain only the first term, with \(q-1=1\). Each term is \(O_q(n^2((q-1)/q)^n)\): in the second term use \(q^{-1/2}\le(q-1)/q\) for \(q\ge3\); the third is superexponentially small.

**3. Conditioning on perfection and enumeration.** The invertibility probability is
\[p_{n,q}=\frac{|\mathrm{GL}_n(\mathbb F_q)|}{q^{n^2}}=\prod_{j=1}^n(1-q^{-j})\ge c_q:=\prod_{j=1}^{\infty}(1-q^{-j})>0.\]
The expected nonidentity stabilizer size over invertible matrices thus obeys \(0\le\delta_{n,q}\le\varepsilon_{n,q}/c_q\). Markov's inequality for the nonnegative integer \(|\operatorname{Aut}(E_A)|-1\) proves the claimed uniform-matrix rigidity bound.

Burnside's orbit-counting formula gives exactly
\[N_{n,q}=\frac{1}{n!(q-1)^n}\sum_{A\in\mathrm{GL}_n(\mathbb F_q)}|\operatorname{Aut}(E_A)|=\frac{|\mathrm{GL}_n(\mathbb F_q)|}{n!(q-1)^n}(1+\delta_{n,q}).\]
For an orbit with stabilizer order \(s\ge2\), \(s\le2(s-1)\). The number of nonrigid orbits is therefore at most twice the number of nonidentity-stabilizer incidences divided by \(|G_n|\); dividing by \(N_{n,q}\) gives the uniform-isomorphism-class bound \(2\delta_{n,q}/(1+\delta_{n,q})\). This completes the proof.

## Verification
The included standalone `check_generic_evolution.py` constructs all invertible matrices for \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3)\), independently enumerates monomial stabilizers, and verifies both Burnside's orbit count and the exact automorphism-order profiles. The counts of isomorphism classes are respectively \(4,33,908,7,249\); the numbers of invertible matrices with nontrivial stabilizer are \(2,24,1344,8,576\). Executing the included checker prints `VERIFY_OK`. Small-case enumeration verifies only the finite cases, not the asymptotic theorem, which is established above.

## Relationship to prior work
Wei and Zou [1] established the monomial-orbit classification and a general Burnside formula and obtained exact small-dimensional counts; those identities are credited and are *not* new here. Kaygorodov, Martín González and Viruel [2] explicitly ask for statistical information about automorphism groups and isomorphism-class growth of random evolution algebras. The new quantitative conclusion is that in the **uniform perfect and fixed-field model**, nontrivial automorphisms are exponentially rare with a specified uniform rate, forcing an asymptotic simplification of the exact Burnside count. The Grothendieck-ring study [3] concerns structural cancellation/tensor products, not this probability. The present theorem gives neither the distribution of all nonperfect evolution algebras nor a uniform bound when \(q\) varies with \(n\).

## Limitations
This is a fixed-\(q\), perfect-algebra result. It does not establish generic rigidity among all evolution algebras or over algebraic closures, nor does it supply a complete lower-order expansion or exact stabilizer distributions at large \(n\). The exponential bound is not asserted sharp. The general Burnside framework was known; previous unindexed asymptotic consequences remain a possible overlap risk, so independent literature assessment is still needed.

## References
[1] Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (first posted 2023-10-18), https://arxiv.org/abs/2310.12368.

[2] I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted 2026-10-15), https://arxiv.org/abs/2610.22248.

[3] I. Alshatnawi, C. Costoya and A. Viruel, *On the Grothendieck Ring of Finite-Dimensional Non-Degenerate Evolution Algebras*, arXiv:2607.15154 (first posted 2026-07-16), https://arxiv.org/abs/2607.15154.
