# Exact idempotent rank spectrum and sharp stretched-exponential law for even-cycle endomorphisms

## Finding
Let \(C_n\) be the simple undirected cycle on \(n\ge4\) labeled vertices, and let \(\operatorname{End}(C_n)\) be its monoid of adjacency-preserving full vertex maps. For even \(n\), write \(e_{n,k}\) for the number of idempotents \(f\), meaning \(f^2=f\), with exactly \(k\) image vertices, and let \(A_k\) denote the adjacency matrix of the \(k\)-vertex path. Then
\[
e_{n,k}=n\bigl(A_k^{\,n-k+1}\bigr)_{1,k}\quad(2\le k\le n/2+1),\qquad e_{n,n}=1,
\]
and all other \(e_{n,k}\) vanish. In particular,
\[
E_n:=|\{f\in\operatorname{End}(C_n):f^2=f\}|=
1+n\sum_{k=2}^{n/2+1}\bigl(A_k^{\,n-k+1}\bigr)_{1,k}.
\]
For odd \(n\ge3\), there is exactly one idempotent (the identity). The initial even-cycle totals for \(n=4,6,8,10,12,14,16\) are \(9,25,73,221,685,2157,6881\).

Put
\[
a=\log 2,\quad s=(\pi^2/a)^{1/3},\quad c=\tfrac32as,
\quad B=16\sqrt{2\pi as/3},\quad \sigma=\sqrt{s/(3a)}.
\]
Then, as even \(n\) tends to infinity,
\[
\boxed{E_n\sim B\,2^n n^{1/6}\exp(-c n^{1/3}).}
\]
For a uniformly random idempotent \(F_n\in\operatorname{End}(C_n)\), with \(R_n=|\operatorname{Im} F_n|\),
\[
\boxed{\frac{R_n-sn^{1/3}}{\sigma n^{1/6}}\ \Longrightarrow\ \mathcal N(0,1).}
\]
The fraction of all cycle endomorphisms that are idempotents satisfies
\[
\frac{E_n}{|\operatorname{End}(C_n)|}
\sim B\sqrt{\pi/2}\,n^{-1/3}\exp(-c n^{1/3}).
\]
The exact rank formula and its boundary-conditioned asymptotic prefactor concern a specific transformation monoid; the cubic-root confinement scale and Gaussian range phenomena have established analogues for range-penalized one-dimensional random walks [2].

## Assumptions and scope
The graph is undirected, simple and loopless; endomorphisms preserve edges but need not be injective or reflect nonedges. Composition is ordinary composition of total vertex maps. Labels distinguish vertices and transformations; counts are not taken modulo graph automorphisms. Except for the odd-cycle observation, the exact formula assumes even \(n\ge4\). The sharp asymptotic and rank limit assume even \(n\to\infty\).

## Proof
**1. Image geometry and retractions.** Every idempotent map restricts to the identity on its image. Since \(C_n\) is connected, its image is a connected induced subgraph on its image vertices. A proper connected vertex subset of a cycle is a path consisting of \(k\) consecutive vertices; adjacency preservation and the absence of loops imply \(k\ge2\). Conversely, fixing that path pointwise and mapping the complementary arc to a walk from one endpoint to the other yields an idempotent precisely when every step is between neighboring path vertices. The complementary arc has \(L=n-k+1\) edges. Its number of admissible images is \((A_k^L)_{1,k}\). The \(n\) placements of a proper \(k\)-vertex path are distinct, so there are \(n(A_k^L)_{1,k}\) maps. A walk from 1 to \(k\) needs at least \(k-1\) steps, whence \(k\le n/2+1\). Its parity condition is automatic for even \(n\), since \(L-(k-1)=n-2k+2\) is even. A surjective idempotent is the identity. For odd \(n\), an endomorphism of \(C_n\) is an automorphism [1], and a group has only its identity as idempotent.

**2. Principal spectral contribution.** For \(j=k+1\) and \(L=n-j+2\), the path spectral expansion is
\[
(A_k^L)_{1,k}=\frac2j\sum_{h=1}^{j-1}
\sin\!\frac{\pi h}{j}\sin\!\frac{\pi hk}{j}
\left(2\cos\!\frac{\pi h}{j}\right)^L.
\]
Because \(n\) is even, the terms \(h=1\) and \(h=j-1\) have the same sign and are positive. For \(j\) in any fixed positive compact multiple of \(n^{1/3}\), all other spectral terms are exponentially smaller on the \(n^{1/3}\) scale, uniformly. Thus
\[
(A_k^L)_{1,k}=\frac4j\sin^2\!\frac{\pi}{j}
\left(2\cos\!\frac{\pi}{j}\right)^{n-j+2}
\left(1+O\bigl(j e^{-\eta n/j^2}\bigr)\right),
\]
where \(\eta>0\) can be chosen uniformly on such compact ranges. Expanding the sine and cosine, and observing that \(n/j^4\to0\), gives
\[
\frac{(A_k^L)_{1,k}}{2^n}
=\frac{16\pi^2}{j^3}
\exp\left(-aj-\frac{\pi^2n}{2j^2}\right)(1+o(1)),
\]
uniformly whenever \(j/n^{1/3}\) lies in a fixed compact subinterval of \((0,\infty)\).

**3. Localization and Laplace sum.** Define \(\phi_n(j)=aj+\pi^2n/(2j^2)\). This has its unique minimum at \(j_*=sn^{1/3}\) with \(\phi_n(j_*)=cn^{1/3}\) and \(\phi_n''(j_*)=3a/j_*\). To control tails, use the nonnegative symmetric path adjacency matrix's spectral norm:
\[
0\le(A_k^L)_{1,k}\le (2\cos(\pi/j))^L.
\]
For \(j\) of order \(n^{1/3}\) outside any small relative neighborhood of \(j_*\), the scaled exponent \(\phi_n(j)/n^{1/3}\) exceeds \(c\) strictly. For smaller \(j\), the confinement factor \(\cos(\pi/j)^L\) gives stronger suppression; for larger \(j\), the factor \(2^{-j}\) does. The latter bounds also work when \(j\) is a non-negligible fraction of \(n\), with \(L\ge n/2\). Therefore terms outside a slowly widening \(O(n^{1/6})\) window around \(j_*\) contribute negligibly relative to the Laplace mass. On that window,
\[
\phi_n(j)=cn^{1/3}+\frac{3a}{2j_*}(j-j_*)^2+o(1)
\]
uniformly for bounded normalized displacement. The local lattice Gaussian sum yields
\[
\sum_k\frac{(A_k^{n-k+1})_{1,k}}{2^n}
\sim\frac{16\pi^2}{j_*^3}e^{-cn^{1/3}}
\sqrt{\frac{2\pi j_*}{3a}}.
\]
Multiplying by \(n\) and using \(\pi^2=as^3\) proves the exact constant \(B\) and the \(n^{1/6}\) power. After normalizing these same weights to sum to one, the local Gaussian yields the stated limit law for \(R_n\); replacing \(j\) by \(k=j-1\) introduces a negligible shift on the fluctuation scale. The identity map has asymptotically vanishing mass.

**4. Rarity among endomorphisms.** A graph endomorphism of \(C_n\) is a closed nearest-neighbor walk of \(n\) steps on the cycle with a chosen starting vertex. For even \(n\), the step-sum is either \(-n\), \(0\) or \(n\), giving \(\lvert\operatorname{End}(C_n)\rvert=n(2+\binom{n}{n/2})\), also known from [1,3]. Stirling's formula and the first asymptotic prove the ratio.

## Verification
The standalone standard-library script `verify.py` independently enumerates all graph endomorphisms of even cycles with \(4\le n\le14\) via closed nearest-neighbor walks; tests every map's idempotency by explicit composition; and independently computes the rank spectrum through adjacency-walk dynamic programming. The spectra agree for all six tested dimensions, with total counts \(9,25,73,221,685,2157\). It also calculates exact integer totals in three larger dimensions and checks broad consistency with the asymptotic scale. Execute `python3 verify.py` from this directory. Expected final line: `VERIFY_OK`. These finite checks corroborate but do not prove the infinite asymptotics; their proof is the spectral localization and Laplace argument above.

## Relationship to prior work
Dimitrova, Fernandes, Koppitz and Quinteiro [1] analyze the full cycle-endomorphism monoids, their Green relations, regularity, generators and total cardinality, without presenting the idempotent rank-count formula or its sharp asymptotic distribution in the inspected full text. The passage from idempotents to graph retractions is standard; it is not claimed as new. Michels and Knauer [3] previously studied counts of graph endomorphisms and their congruence classes; their full paper was not accessible for exhaustive comparison. Bouchot [2] establishes the cubic-root confinement and Gaussian *range* fluctuations of a range-penalized unconstrained random walk. Those phenomena are therefore prior knowledge, but [2] does not give the boundary-to-boundary path-walk count \((A_k^{n-k+1})_{1,k}\) or its two-endpoint spectral prefactor. The distinguishing assertions here are the cycle-monoid idempotent rank census and its sharp, endpoint-conditioned asymptotic constants.

## Limitations
The result is for simple cycle graphs and full graph endomorphisms, not weak endomorphisms or graph partial maps. The asymptotic uses even dimensions; odd dimensions are trivial for idempotents. The spectral method is classical and related confinement results already exist; originality of the *specific algebraic enumeration and constant* requires further expert publication-priority verification. The full text of [3] was not inspected. No independent mathematical audit or external certification has been performed.

## References
[1] I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149v1 (first public October 6, 2023), https://arxiv.org/abs/2310.04149 .

[2] N. Bouchot, *Scaling limits for the random walk penalized by its range in dimension one*, arXiv:2202.11953v1 (first public February 24, 2022), https://arxiv.org/abs/2202.11953 .

[3] M. A. Michels, U. Knauer, *The congruence classes of paths and cycles*, Discrete Mathematics 309 (2009), 5352–5359; title and citation cross-checked against OEIS A112850, https://oeis.org/A112850 .
