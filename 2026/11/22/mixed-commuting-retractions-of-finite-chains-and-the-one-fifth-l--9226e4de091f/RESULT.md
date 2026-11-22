# Mixed commuting retractions of finite chains and the one-fifth law

## Finding
Let \([n]=\{1,\ldots,n\}\), with \(n\ge1\). Write \(\mathcal O_n\) for the monoid of all nondecreasing self-maps and \(\mathcal C_n\subseteq\mathcal O_n\) for the nondecreasing contractions: those whose increments belong to \(\{0,1\}\). A retraction is a composition-idempotent map. Count **ordered mixed pairs** \((e,f)\), with \(e\) a retraction of \(\mathcal C_n\), \(f\) a retraction of \(\mathcal O_n\), and \(ef=fe\). Denote this count by \(H_n\). Then
\[
\boxed{\sum_{n\ge1}H_nz^n=\frac{z(1-2z)^2}{(1-z)^2(1-3z+z^2)^3}.}
\]
The first values are \(1,7,32,123,433,1448,4682,14778,45792,139818\). Independently sampling uniform retractions \(e\in\mathcal C_n\) and \(f\in\mathcal O_n\) gives the **nonzero limiting commutation probability**
\[
\boxed{\lim_{n\to\infty}\Pr(ef=fe)=\frac15.}
\]
This contrasts with the exponentially vanishing commutation probability for two independent uniform retractions of \(\mathcal O_n\).

More finely, every retraction of \(\mathcal C_n\) is a unique interval clamp \(e_{a,b}(i)=\min(b,\max(a,i))\), where \(1\le a\le b\le n\). Put \(L=b-a+1\). Define \(B_0=E_0=0\), \(B(z)=\sum_{j\ge1}B_jz^j=z(1-z)^2/(1-3z+z^2)\), \(E_j=\sum_{i=1}^{j}B_i\), and \(N_j=\sum_{i=1}^{j}(j-i+1)B_i\) for \(j\ge1\), with \(N_j=0\) for \(j\le0\). Then the number of retractions \(f\in\mathcal O_n\) commuting with the specified clamp equals
\[
\boxed{K_n(a,b)=B_L E_a E_{n-b+1}+E_{L-1}(E_a+E_{n-b+1})+N_{L-2}.}
\]

## Assumptions and scope
All maps are total functions on finite linearly ordered sets, and composition is ordinary functional composition. The contraction restriction is imposed only on the **first** member \(e\) of each ordered pair. The second member \(f\) need not be a contraction. The singleton chain and constant-clamp boundaries are included. The probability samples independently and uniformly from the two distinct retraction sets, **not** from all maps or all unordered pairs.

## Proof
**1. Retracts and anchored counts.** A nondecreasing contraction has interval image. If it is idempotent, it fixes every point of its image, hence must be the clamp \(e_{a,b}\), uniquely. Consequently \(|E(\mathcal C_n)|=n(n+1)/2\). A nondecreasing idempotent has an ordered nonempty fixed-point set, and each gap of length \(d\ge1\) between consecutive fixed points permits exactly \(d\) monotone cuts determining the images of the intervening points. A retraction on a chain of length \(L\) that fixes **both** endpoints is therefore counted by \(B_L\), with
\[
B(z)=\frac{z}{1-\sum_{d\ge1}dz^d}=\frac{z(1-z)^2}{1-3z+z^2}.
\]
A retraction on a length-\(j\) chain fixing its right endpoint has a smallest fixed point, giving \(E_j=\sum_{i=1}^jB_i\). Thus
\[
A(z):=\sum_{u\ge0}E_{u+1}z^u=\frac{1-z}{1-3z+z^2}.
\]
The number of arbitrary nondecreasing retractions on a length-\(j\) chain is \(N_j=\sum_{i=1}^j(j-i+1)B_i\): choose the length of the interval between the first and last fixed points and its position, then choose the interior structure. These formulas include \(j=0,1\) by the stated boundary conventions.

**2. Exact commutation criterion for a fixed clamp.** Fix \(e=e_{a,b}\) and write \(g=f|_{[a,b]}\). If \(ef=fe\), then \(f([a,b])\subseteq[a,b]\) because \(f(i)=f(e(i))=e(f(i))\) for every interior point. Hence \(g\) is an order-preserving idempotent on \([a,b]\). On \([1,a]\), the equality \(e(f(i))=f(a)\) has two exhaustive possibilities. If \(g(a)=a\), \(f|_{[1,a]}\) is any anchored retraction fixing \(a\) (there are \(E_a\)); if \(g(a)>a\), monotonicity and the clamp equation force \(f(i)=g(a)\) for all \(i<a\) (one choice). The right side is symmetric: there are \(E_{n-b+1}\) independent choices if \(g(b)=b\), and otherwise it is forced to be constant \(g(b)\). Conversely these choices are nondecreasing, idempotent and satisfy the clamp commutation equation pointwise, so no cases are lost or duplicated.

**3. Split the interior by fixed endpoints.** The interior restriction \(g\) fixes both endpoints in \(B_L\) ways. It fixes the left but not the right in \(E_{L-1}\) ways: restrict to the first \(L-1\) points and reflect if needed; symmetry gives the same count for fixing the right but not the left. If it fixes neither, its first and last fixed points lie strictly between the endpoints, counted by \(N_{L-2}\). Weighting by the number of exterior choices in the four cases yields
\[
K_n(a,b)=B_LE_aE_{n-b+1}+E_{L-1}(E_a+E_{n-b+1})+N_{L-2}.
\]
For \(L=1\) the other terms vanish, giving the correct constant-clamp count.

**4. Sum the mixed pairs.** Write \(u=a-1\), \(v=n-b\); then \(n=u+L+v\). Since \(N(z)=\sum_{j\ge0}N_jz^j=B(z)/(1-z)^2\), summing the displayed formula over all nonnegative \(u,v\) and positive \(L\) yields
\[
H(z)=B(z)A(z)^2+\frac{2z^2A(z)^2}{1-z}+\frac{z^2B(z)}{(1-z)^4}.
\]
Using \(B(z)=z(1-z)A(z)\), this factors as
\[
H(z)=B(z)\left(A(z)+\frac{z}{(1-z)^2}\right)^2
=\frac{z(1-2z)^2}{(1-z)^2(1-3z+z^2)^3}.
\]
All identities are formal power-series identities, so the exact enumeration is valid for every \(n\ge1\).

**5. The sharp one-fifth limit.** The idempotent count of \(\mathcal O_n\) is the classical Fibonacci number \(F_{2n}\), where \(F_0=0\), \(F_1=1\). Let \(r=(3-\sqrt5)/2\), \(\alpha=r^{-1}=(3+\sqrt5)/2\). The unique smallest-modulus pole of \(H(z)\) is \(r\), of order three. Its leading expansion is
\[
H(z)=\frac{(1-2r)^2}{5\sqrt5\,r^2(1-r)^2}(1-z/r)^{-3}+O((1-z/r)^{-2}).
\]
Consequently
\[
H_n\sim\frac{(1-2r)^2}{10\sqrt5\,r^2(1-r)^2}\,n^2\alpha^n.
\]
On the other hand \(F_{2n}\sim\alpha^n/\sqrt5\), and \(|E(\mathcal C_n)|=n(n+1)/2\). Hence the desired probability has limit
\[
\frac{(1-2r)^2}{5r^2(1-r)^2}=\frac15,
\]
where the final equality follows by substituting \(r=(3-\sqrt5)/2\) and simplifying. Positivity and strict inequality between the two roots of \(1-3z+z^2\) justify the dominant-pole extraction.

## Verification
The accompanying `check_mixed_retractions.py` exhaustively enumerates every monotone idempotent on \([n]\), for \(1\le n\le7\), computes compositions with every clamp directly, and independently compares their per-clamp commutation counts with the formula. It checks the totals \(1,7,32,123,433,1448,4682\). The exact rational-series expansion was also verified symbolically. Run `python3 check_mixed_retractions.py` in the package directory. Finite checking corroborates but does not replace the all-\(n\) proof.

## Relationship to prior work
Zubairu–Umar–Aliyu (arXiv:2205.00438v1) study order-preserving contractions and their idempotent/rank properties; the elementary clamp normal form is already known. A published centralizer profile for idempotent contractions counts commuting **contractions**, including non-idempotents, not commuting idempotents of the larger isotone monoid. A separate published all-isotone commuting-pair renewal theorem counts arbitrary commuting isotone idempotents, with a different generating function; its displayed product-rank enumerator does not mark which factor is a contraction. The claim here is the **mixed** restriction's per-clamp idempotent centralizer, its rational OGF and the nonzero one-fifth limit. Their combination is not obtained by substituting parameters into either prior displayed enumeration. Relevant exact prior-result links are given below.

## Limitations
These formulas are restricted to finite *chains* and to ordered mixed pairs of full idempotent maps. They do not enumerate all commuting pairs of contractions, centralizers of arbitrary non-idempotent maps, or other partially ordered sets. The original published literature and available result databases were compared for the same implication, but historical uniqueness cannot be proved from a finite search; an equivalent older enumerator remains possible. The result has had no independent mathematical audit.

## References
- M. M. Zubairu, A. Umar, M. J. Aliyu, *On the combinatorial and rank properties of certain subsemigroups of full contractions of a finite chain*, arXiv:2205.00438v1, publicly posted 1 May 2022, https://arxiv.org/abs/2205.00438.
- D. B. Li, V. H. Fernandes, *Endomorphisms of semigroups of monotone transformations*, arXiv:2204.07838v1, publicly posted 16 April 2022, https://arxiv.org/abs/2204.07838.
- *Centralizer profiles and a quadratic limit law for idempotent finite-chain contractions*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-centralizer-profiles-and-a-quadratic-limit-law-for-idempotent-fi--22387dfffecf.
- *Product-rank renewal law for commuting monotone idempotents*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-product-rank-renewal-law-for-commuting-monotone-idempotents--7421eb043379.
