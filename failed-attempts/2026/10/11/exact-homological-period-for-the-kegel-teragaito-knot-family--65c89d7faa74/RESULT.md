# Exact homological period for the Kegel–Teragaito knot family
## Finding
For every integer \(n\ge1\), let \(K_n\) be the knot introduced by Kegel and Teragaito as the closure of the four-braid
\[
[(2,1,3,2)^{2n+1},-1,2,1,1,2].
\]
Their 2026 theorem proves that \(K_n\) is a hyperbolic L-space knot with a unique strong inversion. Let \(\phi_n\) denote the monodromy of its fiber. Then \(\phi_n\) is pseudo-Anosov and its action on integral first homology has exact order
\[
m_n=\operatorname{lcm}(8n+10,8n+4).
\]
Equivalently,
\[
m_n=
\begin{cases}
\dfrac{2(4n+5)(4n+2)}{3},&n\equiv1\pmod 3,\\
2(4n+5)(4n+2),&n\not\equiv1\pmod 3.
\end{cases}
\]
Hence \(\phi_n^{m_n}\) lies in the Torelli group, and no smaller positive power of \(\phi_n\) lies in the Torelli group.

## Assumptions and scope
The fiber is the compact genus-\(4n+2\) Seifert surface of the fibered knot \(K_n\). The Torelli group here means the kernel of the action of the mapping class group of that once-bordered surface on \(H_1(-;\mathbb Z)\).

The exact-period statement concerns only the homological action. It does not assert that \(\phi_n\) itself has finite order; in fact hyperbolicity of the fibered knot complement forces \(\phi_n\) to be pseudo-Anosov and therefore of infinite order.

The strong-inversion statement is the knot symmetry proved in the 2026 source. No identification between that involution and a symmetry of the monodromy is asserted.

## Proof
Kegel and Teragaito prove that every \(K_n\) is a hyperbolic L-space knot with a unique strong inversion. Since an L-space knot is fibered, \(K_n\) has a monodromy \(\phi_n\). A fibered hyperbolic knot has pseudo-Anosov monodromy.

Baker and Kegel compute the Alexander polynomial of this same family as
\[
\Delta_{K_n}(t)
=
\frac{(t^{4n+5}+1)(t^{4n+2}+1)}{(t+1)(t^2+1)}.
\]
For a fibered knot, the Alexander polynomial is the characteristic polynomial of the induced action \(A_n=(\phi_n)_*\) on first homology, up to the usual unit normalization. The displayed representative is monic of degree \(8n+4=2(4n+2)\), so it gives the characteristic polynomial directly.

Put \(a=4n+5\) and \(b=4n+2\). Then \(a\) is odd and \(b\equiv2\pmod4\). Write
\[
P_n(t)=\frac{t^a+1}{t+1},
\qquad
Q_n(t)=\frac{t^b+1}{t^2+1}.
\]
Both numerators have only simple roots. The removed roots are exactly \(-1\) from the first numerator and \(\pm i\) from the second, so \(P_n\) and \(Q_n\) are squarefree. They are also coprime: a common root \(z\) would satisfy \(z^a=z^b=-1\), hence \(z^{a-b}=z^3=1\), impossible because a cube root of unity cannot have any power equal to \(-1\). Thus \(\Delta_{K_n}\) has pairwise distinct complex roots, and \(A_n\) is diagonalizable over \(\mathbb C\).

Every root of \(P_n\) has order dividing \(2a\), and \(e^{\pi i/a}\) is a primitive \(2a\)-th root that survives division by \(t+1\). Therefore the least common multiple of the orders of the roots of \(P_n\) is exactly \(2a=8n+10\). Likewise every root of \(Q_n\) has order dividing \(2b\), while \(e^{\pi i/b}\) is primitive of order \(2b\) and is not \(\pm i\) for \(b\ge6\). Thus the corresponding least common multiple for \(Q_n\) is exactly \(2b=8n+4\).

Because \(A_n\) is diagonalizable with those root-of-unity eigenvalues, its exact order is
\[
\operatorname{ord}(A_n)=\operatorname{lcm}(2a,2b)=\operatorname{lcm}(8n+10,8n+4).
\]
Finally,
\[
\gcd(a,b)=\gcd(4n+5,4n+2)=\gcd(3,4n+2),
\]
which is \(3\) exactly when \(n\equiv1\pmod3\), and is otherwise \(1\). This gives the stated piecewise formula. By definition, \(\phi_n^k\) belongs to the Torelli group exactly when \(A_n^k=I\), so \(m_n\) is the smallest positive Torelli power.

## Verification
The proof is symbolic and does not depend on finite sampling. The critical checks are: the two quotient factors are polynomial because \(-1\) and \(\pm i\) are precisely the removed roots; both factors are squarefree; they have no common root because their exponents differ by \(3\); and each factor retains a primitive root of the full numerator order. These facts force diagonalizability and make the least common multiple of the eigenvalue orders exact rather than merely an upper bound.

As a finite sanity check separate from the proof, direct polynomial gcd and derivative-gcd calculations were replayed for \(1\le n\le20\); every case was squarefree and coprime, and the arithmetic least-common-multiple formula agreed with the displayed residue-class formula. This finite check is not used to establish the all-\(n\) statement.

## Relationship to prior work
Kegel and Teragaito prove in 2026 that this family consists of hyperbolic L-space knots with unique strong inversion, but their paper does not discuss monodromy or Alexander polynomials. Baker and Kegel had earlier computed the factorized Alexander polynomial and observed that all of its roots lie on the unit circle; their paper does not discuss monodromy, the order of the homological action, or Torelli powers.

The present statement combines the new symmetry-rigidity theorem with the older exact Alexander polynomial and determines the full order of the homological monodromy. Knowing only that all roots are roots of unity would not suffice: repeated roots could allow nontrivial Jordan blocks and infinite-order homological action. The squarefreeness and primitive-root analysis above closes exactly that gap and yields the minimal Torelli power.

Periodic homological action for pseudo-Anosov fibered-knot monodromy is a recognized phenomenon; the contribution here is the exact period for every member of this newly established uniquely strongly invertible family, including its mod-\(3\) arithmetic split.

## Limitations
The result computes only the action on \(H_1\). It does not determine the Nielsen--Thurston stretch factor, the action on nilpotent quotients, Johnson homomorphisms of \(\phi_n^{m_n}\), or the location of that power in the Johnson filtration.

No claim is made that this family is the first family of pseudo-Anosov knot monodromies with periodic homological action. The novelty claim is restricted to the exact homological period and minimal Torelli power for the Kegel--Teragaito family together with the 2026 unique-strong-inversion theorem.

## References
1. M. Kegel and M. Teragaito, *An infinite family of strongly invertible L-space knots without Khovanov thin surgery*, arXiv:2608.00864v1, first public 2026-08-01. Theorem 1.1; primary MSC 57K10.
2. K. L. Baker and M. Kegel, *Census L-space knots are braid positive, except for one that is not*, Algebraic & Geometric Topology 24 (2024), 569--586, arXiv:2203.12013. Proposition 3.1 and Theorem 4.4.
3. E. Hironaka, *Salem--Boyd sequences and Hopf plumbing*, Osaka Journal of Mathematics 43 (2006), 497--516, arXiv:math/0506602. The homological monodromy characteristic polynomial is the Alexander polynomial for a fibered link.
