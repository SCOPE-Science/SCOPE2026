# Logarithmic cotangent corank of random algebra retractions in characteristic two

## Finding

Let \(q=2^e\) with \(e\ge1\), \(k=\mathbb F_q\), and \(A_n=k[x_1,\ldots,x_n]/(x_1^2,\ldots,x_n^2)\). Choose uniformly among all unital \(k\)-algebra endomorphisms \(P:A_n\to A_n\) satisfying \(P^2=P\). The image has dimension \(2^{r(P)}\) for some integer \(0\le r(P)\le n\). Define the cotangent corank \(S_n=n-r(P)\) and \(T_n=\lfloor\log_2 n\rfloor\). Put
\[
C_q=\prod_{j=1}^{\infty}(1-q^{-j})^{-1}<\infty.
\]
**Concentration theorem.** For every \(n\ge64\),
\[
\boxed{\Pr\{T_n-2\le S_n\le T_n+2\}\ge1-(n+1)C_q q^{-2^{n-1}}.}
\]
Therefore \(S_n=\log_2 n+O(1)\) with probability tending to one, and \(\dim_k\operatorname{im}P=\Theta(2^n/n)\) with probability tending to one. If \(H_n(q)\) denotes the total number of retractions then, for each fixed \(q\),
\[
\boxed{\log_q H_n(q)=(n-\log_2 n)2^n+O_q(2^n).}
\]
These are consequences of an **already published exact rank enumerator**, not a new retraction-orbit classification. The mathematical contribution asserted here is the quantitative five-index logarithmic-corank concentration and total-count asymptotic; the pre-existing finite counts and conjugacy theorem are explicitly credited below.

## Assumptions and prior exact enumeration

All maps are unital, multiplicative, and \(k\)-linear; they need not preserve grading or be Hopf maps. The characteristic-two assumption ensures that every element of the maximal ideal \((x_1,\ldots,x_n)\) has square zero. The image-rank classification and the following exact multiplicities were proved earlier in *Automorphism orbits and rank counts of characteristic-two square-zero-variable algebra retractions* (12 October 2026): for \(s=n-r\),
\[
N_{n,n-s}(q)={n\brack s}_q q^{(n-s)2^n+(2s-n)2^{n-s}-(n-s)s-s}.
\tag{1}
\]
Here \({n\brack s}_q\) is a Gaussian binomial coefficient. The corresponding rank is \(2^{n-s}\); the exact formula counts **labeled endomorphism maps**. In particular, (1) is input from prior work, not claimed novel. Its derivation uses automorphism conjugacy to coordinate deletion and the orbit-stabilizer count of the retraction stabilizer. Our analysis requires no classification stronger than this established formula.

## Proof of the concentration theorem

For \(0\le s\le n\), define
\[
\Phi_n(s)=(n-s)2^n+(2s-n)2^{n-s}-s,\qquad
B_{n,s}(q)=q^{-s(n-s)}{n\brack s}_q.
\]
The exact enumerator (1) is equivalent to
\[
N_{n,n-s}(q)=q^{\Phi_n(s)}B_{n,s}(q).
\tag{2}
\]
The Gaussian-binomial product representation implies
\[
1\le B_{n,s}(q)\le C_q
\tag{3}
\]
for every \(s,n\) (empty products included). Exact subtraction gives
\[
\Phi_n(s+1)-\Phi_n(s)
=2^{n-s}\bigl(n/2+1-s-2^s\bigr)-1.
\tag{4}
\]
Fix \(n\ge64\) and set \(T=\lfloor\log_2 n\rfloor\). In the lower tail, \(0\le s\le T-3\) implies \(2^s\le n/8\) and \(s\le T\le n/8\). Thus (4) is at least \(2^n-1\), in particular at least \(2^{n-1}\). Iterating from any \(s<T-2\) to \(T-2\) yields
\[
\Phi_n(s)\le\Phi_n(T-2)-2^{n-1}.
\tag{5}
\]
In the upper tail, for \(T+2\le s<n\), \(2^s>2n\). Therefore
\[
\Phi_n(s+1)-\Phi_n(s)
\le -\bigl(3/4-1/(2n)\bigr)2^n-1<-2^{n-1}.
\tag{6}
\]
Iterating back from \(s>T+2\) to \(T+2\) gives the analogous upper-tail inequality. Comparing the resulting weights with the corresponding boundary-window terms by (2) and (3), every outlying probability is at most \(C_q q^{-2^{n-1}}\). There are at most \(n+1\) terms, which proves the displayed concentration bound.

Within the five-index window, \(s=T+O(1)\), so \(s=\log_2 n+O(1)\) and
\[
\Phi_n(s)=(n-\log_2 n)2^n+O(2^n).
\]
By (3), the logarithmic correction from \(B_{n,s}(q)\) is bounded by \(\log_q C_q\). Summing at most \(n+1\) terms and using the concentration estimate proves
\(\log_q H_n(q)=(n-\log_2 n)2^n+O_q(2^n)\).
Finally, the image of a retraction with corank in the window has dimension \(2^{n-s}\), and \(2^T\le n<2^{T+1}\) makes this \(\Theta(2^n/n)\). This completes the proof.

## Verification

The exact differences in (4), bounds in (5)–(6), and the prior enumerator are symbolic/integer equalities. An independent small-parameter replay computes the published rank multiplicities \((1,12,1)\) at \((n,q)=(2,2)\), \((1,80,1)\) at \((2,4)\), and \((1,448,3584,1)\) at \((3,2)\). An additional exact-exponent calculation locates a maximal corank inside the asserted window for \(n=64,65,128\). These finite checks corroborate formula handling; the preceding inequalities, not the finite examples, prove the all-\(n\) claim.

## Relationship to prior work and value

*Automorphism orbits and rank counts of characteristic-two square-zero-variable algebra retractions* (12 October 2026) already proves **every finite-rank coefficient** in (1), the conjugacy of all unital retractions to coordinate deletions and the cotangent-rank/image-rank relation. Consequently no novelty is claimed for these exact counts, for the Gaussian-binomial formula, or for automorphism orbit-stabilizer arguments. The October result does not state a random-retraction logarithmic-corank concentration theorem, its explicit superexponential tail, or this total-count asymptotic. The new analysis quantifies the typical dimension of a retraction of a natural, highly nonreduced local algebra, where the image rank is exponentially sensitive to generator-rank changes. It is not a new classification of finite retractions.

## Limitations

The theorem concerns only uniform sampling among all unital algebra retractions of the specified characteristic-two complete intersection, with fixed finite \(q\) for the asymptotic total count. It gives an \(O(1)\)-window for the corank, not a limiting local probability law or a finer classification within that window. The numerical checker is not an all-dimensions proof. The possibility that an older general theorem on random algebra endomorphisms implies the concentration law remains an explicit historical-priority risk.

## Reference

*Automorphism orbits and rank counts of characteristic-two square-zero-variable algebra retractions*, published 12 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/12/SCOPE-automorphism-orbits-and-rank-counts-of-characteristic-two-square--256249efd1a0 (complete finite enumeration used in equation (1)).
