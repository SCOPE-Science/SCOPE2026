# A stronger quadratic lower bound for brick-chain filtration growth from a seven-arrow rectangle
## Finding
Let \(k\) be an algebraically closed field. For a finite-dimensional \(k\)-algebra \(A\) and a finite-length \(A\)-module \(M\), write \(b_A(M)\) for the number of brick-chain filtrations of \(M\), and define
\[
F(m)=\sup\{\log b_A(M):\operatorname{length}(M)=m\}.
\]
Then
\[
\limsup_{m\to\infty}\frac{F(m)}{m^2}
\ge
\frac{4+8\log 2-7\log 3}{121}
=0.0153296811884528\ldots.
\]
This is strictly larger than the lower endpoint
\[
\frac{1-\log2}{25}=0.0122741127776022\ldots
\]
obtained in the asymptotic specialization of the motivating source.

## Assumptions and scope
The argument uses the \(q\)-Kronecker quiver construction of Enomoto over an algebraically closed field and only the parameter range covered by that construction: \(q\ge3\) and positive integers \(a,b\). Set
\[
q=7,\qquad a=2n,\qquad b=n,
\]
and choose the full rectangular partition
\[
\nu=(n^{2n}),\qquad d=|\nu|=2n^2.
\]
The partition lies in the \(2n\)-by-\(n\) rectangle required by the source. No claim of optimality over all \(q,a,b,\nu\) is made.

## Proof
Theorem 5.4 and Proposition 5.6 of Enomoto give, for the selected parameters, a nonempty Zariski-open family of bricks with dimension vector
\[
(a+(q-1)b,a+b)=(8n,3n)
\]
and at least
\[
L_n=\frac{(q-1)^d d!}{H(\nu)^2}
=\frac{6^{2n^2}(2n^2)!}{H((n^{2n}))^2}
\]
brick-chain filtrations. The composition length of these modules is
\[
2a+qb=11n.
\]

For the full rectangle, the hook product has the exact form
\[
H((n^{2n}))=
\prod_{j=0}^{n-1}\frac{(2n+j)!}{j!}.
\]
Using \(\log(r!)=r\log r-r+O(\log(r+1))\), uniformly for positive integers \(r\), and summing the error over \(n\) factors gives an \(O(n\log n)\) remainder. The main sum is a Riemann sum:
\[
\begin{aligned}
\log H((n^{2n}))
&=2n^2\log n+n^2\int_0^1\bigl((2+t)\log(2+t)-t\log t-2\bigr)\,dt+O(n\log n)\\
&=2n^2\log n+
\left(\frac92\log3-2\log2-3\right)n^2+O(n\log n).
\end{aligned}
\]
Also,
\[
\log((2n^2)!)=4n^2\log n+2n^2\log2-2n^2+O(\log n).
\]
Substitution into \(\log L_n\) cancels the \(n^2\log n\) terms and yields
\[
\log L_n=
(4+8\log2-7\log3)n^2+O(n\log n).
\]
Therefore, along \(m=11n\),
\[
\frac{F(m)}{m^2}\ge
\frac{\log L_n}{121n^2}
\longrightarrow
\frac{4+8\log2-7\log3}{121},
\]
which proves the stated limsup inequality.

## Verification
The accompanying verifier checks the exact rectangle hook-product identity against a direct cell-by-cell hook product for \(1\le n\le10\), confirms the parameter identities \((8n,3n)\) and \(11n\), evaluates the constant independently, and compares exact finite-\(n\) logarithmic lower bounds with the asymptotic value. It ends with `CHECK_OK`.

These finite computations are consistency checks only. The infinite statement follows from the displayed exact source inequality, the exact hook-product identity, and the asymptotic estimates in the proof.

## Relationship to prior work
Enomoto proves the general \(q\)-Kronecker lower bound and then specializes the asymptotic discussion to a square staircase for \(q=3\), obtaining the published endpoint \((1-\log2)/25\). The same paper states that the exact limsup remains open. The present specialization instead uses an unequal dimension ratio and a full rectangle at \(q=7\), producing the stronger constant above. Targeted inspection of the source found no \(q=7\), \(a=2n\), or full-rectangle asymptotic specialization.

Ringel's earlier 2026 paper studies brick-chain complexity measured by filtration length rather than the number of brick-chain filtrations, so its invariant does not imply the counting bound here.

## Limitations
The result is a lower bound along one explicit parameter family and does not identify the true value of the limsup. The motivating preprint is recent, so unindexed notes or later revisions could contain an equivalent optimization. The source inequality itself is general enough that the specialization is elementary once the rectangular hook asymptotics are chosen; the mathematical contribution is the stronger explicit endpoint and the parameter choice that realizes it.

## References
1. H. Enomoto, *Finiteness and growth of brick chain filtrations*, arXiv:2609.10217, first public version 2026-09-09. See Theorem 5.4, Proposition 5.6, Theorem 5.7, and Remark 5.8.
2. C. M. Ringel, *The brick chain complexity of an artin algebra*, arXiv:2606.27879, 2026.
