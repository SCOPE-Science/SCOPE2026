# Full cycle-type census in restricted-partial-range transformation semigroups

## Finding
Let \(X\) be a finite set, \(\varnothing\ne Z\subseteq Y\subseteq X\), and put \(n=|X|\), \(m=|Y|\), \(k=|Z|\), and \(w=n-m\). Consider the composition semigroup
\[
\mathcal T(X,Y,Z)=\{f:X\to X:f(Y)\subseteq Z\}.
\]
Every directed cycle of any \(f\in\mathcal T(X,Y,Z)\) lies wholly in \(Z\) or wholly in \(W=X\setminus Y\). Let \(\lambda\vdash a\) be the partition listing the cycle lengths inside \(Z\), and let \(\mu\vdash b\) list those inside \(W\); the empty partition is allowed for \(\mu\). Define
\[
 z_\lambda=\prod_{j\ge1}j^{m_j(\lambda)}m_j(\lambda)!,\qquad z_{\varnothing}=1.
\]
For every \(1\le a\le k\) and \(0\le b\le w\), the **exact number of transformations with the specified pair of cycle types** is
\[
\boxed{\binom{k}{a}\frac{a!}{z_\lambda}\binom{w}{b}\frac{b!}{z_\mu}\,
 \bigl(a k^{m-a-1}\bigr)\bigl((m+b)n^{w-b-1}\bigr).}
\tag{1}
\]
The conventions when \(a=k=m\), respectively \(b=w\), are \(a k^{m-a-1}=1\), respectively \((m+b)n^{w-b-1}=1\). Other apparent negative powers are removed in the same way by taking the displayed integral forest counts; since \(m\ge k\), these are the only boundary cases. The factors in (1) are nonnegative integers.

Summing over all cycle partitions yields the **factorized two-zone stable-rank polynomial**
\[
\boxed{
B_{n,m,k}(u,v)=
\left(\sum_{a=1}^{k}(k)_a\,a k^{m-a-1}u^a\right)
\left(\sum_{b=0}^{w}(w)_b\,(m+b)n^{w-b-1}v^b\right),}
\tag{2}
\]
where \((r)_s=r(r-1)\cdots(r-s+1)\), \((r)_0=1\). Here the coefficient of \(u^av^b\) counts transformations with \(a\) periodic points in \(Z\) and \(b\) periodic points in \(W\), and the stable image of a sufficiently high power has \(a+b\) points. Both periodic-point counts are **independent for a uniform element** of \(\mathcal T(X,Y,Z)\). In particular,
\[
\Pr(\text{no periodic point in }W)=\frac mn,
\qquad
\Pr(\text{exactly one periodic point in }X)=\frac{m}{kn}.
\tag{3}
\]
The full cycle-type formula determines the number of elements of every eventual semigroup period: for any positive integer \(d\), sum (1) over partitions \(\lambda,\mu\) with all parts dividing \(d\) to count precisely those \(f\) with \(f^{t+d}=f^t\) for all sufficiently large \(t\). Exact period counts follow by Möbius inversion.

As a parameter-reconstruction consequence, \(B_{n,m,k}\) determines \((n,m,k)\) uniquely except in the degenerate family \(k=1\), \(w=0\), for which \(\mathcal T(X,X,Z)\) is a singleton and \(B=u\) for every \(n=m\ge1\).

## Assumptions and scope
All sets are finite and labeled, with \(1\le k\le m\le n\). Maps need not be injective, surjective, idempotent, or regular. Each cycle is a directed cycle in the functional graph, including fixed-point loops. The cycle lengths in the two regions are counted as two **unordered integer partitions**, not as labeled lists. The stable image means \(\bigcap_{t\ge0}f^t(X)\), which is precisely the set of cyclic vertices. It is also the image of \(f^t\) for all sufficiently large \(t\); the eventual period is the least positive common multiple of all cycle lengths. When \(w=0\), the second factor in (2) is \(1\).

## Proof
**1. Location of directed cycles.** Every vertex of \(Y\) maps into \(Z\), and every vertex of \(Z\) maps again into \(Z\). Hence no point in \(Y\setminus Z\) can be periodic. Any directed cycle containing a point of \(W=X\setminus Y\) cannot enter \(Y\), since it would then never return to \(W\). Thus all cycles lie either wholly in \(Z\) or wholly in \(W\).

**2. Rooted-forest lemma.** On a labeled set of \(N\ge1\) vertices with a prescribed nonempty set of \(r\) roots, the number of directed forests in which each nonroot has one outgoing edge to a parent and each component ends at a root is \(rN^{N-r-1}\). For \(r=N\), this means \(1\). A proof uses the directed matrix-tree theorem: the principal minor of the complete-graph outgoing Laplacian after removing the root rows and columns is \(NI_{N-r}-J_{N-r}\); its eigenvalues are \(N\) with multiplicity \(N-r-1\) and \(r\) once, giving the claimed determinant. For \(N-r=0\), the empty determinant is \(1\). This proof explicitly covers all boundary cases.

**3. Edges on \(Y\).** Fix \(a\) chosen cyclic vertices of \(Z\) and their outgoing cycle permutation. After deleting those permutation edges, every other vertex in \(Z\) must feed into the specified roots, with its parent still in \(Z\). By Step 2 the choices are \(a k^{k-a-1}\). The other \(m-k\) vertices of \(Y\setminus Z\) independently map to any vertex of \(Z\), giving \(k^{m-k}\) choices. Their product is \(a k^{m-a-1}\). This is independent of the actual permutation on the selected vertices.

**4. Edges outside \(Y\).** Fix \(b\) cyclic vertices of \(W\) and their outgoing permutation. Delete the cycle edges. Every other point of \(W\) must eventually feed into \(Y\) or a chosen cyclic point of \(W\). The allowed parents of these remaining vertices are all of \(X\), and the root set of this new forest is the union of the \(m\) points of \(Y\) and the \(b\) selected points of \(W\). Step 2 gives exactly \((m+b)n^{w-b-1}\) possibilities, independent of the edges already chosen on \(Y\). Notice that paths through \(Y\) may continue to cycles in \(Z\), which is allowed. The forest condition rules out every additional cycle inside \(W\).

**5. Exact type counting.** Choose the \(a\) vertices in \(Z\) and \(b\) in \(W\), in \(\binom{k}{a}\binom{w}{b}\) ways. The numbers of permutations on these sets of cycle types \(\lambda\) and \(\mu\) are \(a!/z_\lambda\) and \(b!/z_\mu\). Multiply by the two independent forest counts in Steps 3–4 to obtain (1). Conversely, every admissible function uniquely decomposes into its cyclic vertices, two cycle permutations, and those forests, so there is no overcount.

**6. Factorization, probabilities, periods, and reconstruction.** Summing the permutation counts over all partitions of size \(a\), respectively \(b\), yields \(a!\) and \(b!\), proving (2). Its value at \((u,v)=(1,1)\) is \(k^mn^w\), either directly by choosing each value of \(f\) or by summing (1). Hence the factorization makes \(a,b\) independent under the uniform distribution. For \(b=0\), the forest count in Step 4 is \(m n^{w-1}\), so the fraction of maps with no \(W\)-cycle is \(m/n\). For \(a=1\), the first factor in (2) contributes \(k^{m-1}\); combined with \(b=0\) and normalized by \(k^mn^w\) this gives \(m/(kn)\). The power-period characterization follows from the cyclic permutation parts; its least period is the least common multiple of their lengths.

All coefficients in (2) are positive within their asserted index ranges. Therefore its bidegree is \((k,w)\) and it recovers both parameters. Its coefficient sum is \(k^m(m+w)^w\); for fixed \(k,w\), this is strictly increasing with \(m\) unless \((k,w)=(1,0)\). Thus it recovers \(m\) and then \(n=m+w\), with exactly the stated exceptional family.

## Verification
The standalone `CHECK.py` enumerates **every** map in \(\mathcal T(X,Y,Z)\) for all \(1\le k\le m\le n\le6\), using canonical representatives \(Z=\{0,\dots,k-1\}\) and \(Y=\{0,\dots,m-1\}\). It extracts directed cycles independently of the formulas, compares every pair of complete cycle types with (1), compares every two-zone periodic-point coefficient with (2), and checks both exact probability identities and the total map count. It also checks the example \((n,m,k)=(5,3,2)\), where
\[
B_{5,3,2}(u,v)=(4u+4u^2)(15+8v+2v^2),
\]
so the six nonzero coefficients are \(60,32,8,60,32,8\) and the total is \(200\). The verifier reports `RESTRICTED_RANGE_CYCLE_CENSUS_VERIFIED 56`. These finite checks support, but do not replace, the all-parameter proof.

## Relationship to prior work
Jin (2021) introduced and studied the exact same restricted-partial-range semigroup, including a parameter-based isomorphism theorem and semigroup generating rank. Jin and You (2023), Sections 2–4, established its regularity, abundance, total cardinality, number of regular elements, and idempotent counts. The present result studies a different invariant: the **entire bicolored distribution of eventual cyclic structure**, including arbitrary non-idempotent maps, all cycle lengths, and the exact periods of their generated cyclic subsemigroups. The formulas in those papers do not supply (1) or (2). Hansen and Jaworski (2010) give the classical cyclic-vertices/forest/permutation decomposition in general random mapping models, and that established mechanism is used here. The additional ingredient is the exact two-level directed forest decomposition forced by \(Z\subseteq Y\subseteq X\), leading to the independent factorization and reconstruction statement. The exact no-cycle identity in (3) is a specialization of classical rooted forest counting; it is not presented as a new general forest theorem.

## Limitations
This classifies cycle types and eventual periods, **not** complete isomorphism classes of functional graphs, transient tail-length distributions, or the generation rank of the semigroup. The bivariate reconstruction statement concerns the presented cardinality triple \((n,m,k)\), not abstract semigroup isomorphism from an arbitrary action. The limiting exceptional singleton family cannot be distinguished by the cycle polynomial. Literature comparison supports a qualified best-knowledge originality assessment, not a definitive historical-priority claim. The only computational tests are finite; the infinite-dimensional parameter range follows from the proof.

## References
1. J. Jin, *On the Rank of Semigroup of Transformations with Restricted Partial Range*, Filomat 35 (2021), 4925–4936, doi:10.2298/FIL2114925J. https://www.pmf.ni.ac.rs/filomat-content/2021/35-14/35-14-23-15070.pdf
2. J. Jin and T. You, *Semigroup of transformations with restricted partial range: Regularity, abundance and some combinatorial results*, arXiv:2306.00822, first public version June 1, 2023. https://arxiv.org/abs/2306.00822
3. J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, Ars Combinatoria 94 (2010), 341–359. https://combinatorialpress.com/article/ars/Volume%20094/volume-94-paper-34.pdf
4. G. Ayik, H. Ayik, Y. Ünlü, and J. M. Howie, *The structure of elements in finite full transformation semigroups*, Bulletin of the Australian Mathematical Society (2009). https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/structure-of-elements-in-finite-full-transformation-semigroups/3FBACA8FAE572258B4E1F8F16FF184AE
