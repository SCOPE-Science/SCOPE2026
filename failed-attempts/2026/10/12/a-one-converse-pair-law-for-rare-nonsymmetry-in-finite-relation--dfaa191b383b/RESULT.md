# A one-converse-pair law for rare nonsymmetry in finite relation algebras
## Finding
Let \(F(n,s)\) be the number of isomorphism classes of integral relation algebras with \(n\) atoms, exactly \(s\) of them self-converse. Since the identity atom is self-converse and every non-self-converse atom belongs to a two-cycle under converse, put
\[
K=\frac{n-s}{2}.
\]
Thus \(K\) is the number of nonsymmetric converse pairs.

Under the uniform distribution on isomorphism classes of \(n\)-atom integral relation algebras, the rare event of nonsymmetry has the sharp asymptotic
\[
\Pr(K\ge 1)\sim \frac{(n-1)(n-2)}{2^n}.
\]
More strongly, conditioned on nonsymmetry, a single converse pair overwhelmingly dominates:
\[
\Pr(K=1\mid K\ge1)=1-O\!\left(n^2 2^{-n}\right).
\]
For every valid \(k\), uniformly as \(n\to\infty\),
\[
\frac{F(n,n-2k)}{F(n,n)}
=(1+o(1))
\frac{(n-1)!}{(n-2k-1)!\,k!\,2^k}\,2^{-k(n-1)}.
\]
The same conclusions hold for the isomorphism classes of nonassociative relation algebras in which the identity element is an atom, because the same uniform asymptotic formula quoted below holds for that class as well.

## Assumptions and scope
The probability here is **unlabelled**: each isomorphism class receives equal weight. The result concerns integral relation algebras with a fixed number \(n\) of atoms. It does not assert an exponential convergence rate for the labelled model, for representability, or for the passage from all nonassociative relation algebras to the integral subfamily.

Koussas states, following Maddux, that for
\[
Q(n,s)=\frac{(n-1)((n-1)^2+3s-1)}6,
\qquad
P(n,s)=(s-1)!\left(\frac{n-s}{2}\right)!2^{(n-s)/2},
\]
one has the **uniform** asymptotic
\[
F(n,s)=\frac{2^{Q(n,s)}}{P(n,s)}(1+o(1)),
\]
where the \(o(1)\) is uniform over all admissible \(s\le n\) with \(n-s\) even. Koussas also records the same statement for nonassociative relation algebras with the identity as an atom.

## Proof
Write \(s=n-2k\). The two source functions simplify exactly:
\[
Q(n,n-2k)-Q(n,n)=-k(n-1),
\]
and
\[
P(n,n)=(n-1)!,\qquad
P(n,n-2k)=(n-2k-1)!\,k!\,2^k.
\]
Hence uniformity of the source asymptotic gives
\[
\frac{F(n,n-2k)}{F(n,n)}=(1+o(1))R_{n,k},
\]
uniformly in valid \(k\), where
\[
R_{n,k}:=
\frac{(n-1)!}{(n-2k-1)!\,k!\,2^k}\,2^{-k(n-1)}.
\]
In particular,
\[
R_{n,1}=\frac{(n-1)(n-2)}{2^n}.
\]

The defect weights have an exact successive ratio:
\[
\frac{R_{n,k+1}}{R_{n,k}}
=
\frac{(n-2k-1)(n-2k-2)}{(k+1)2^n}.
\]
For \(k\ge1\), this is at most
\[
\rho_n:=\frac{n^2}{2^{n+1}}.
\]
Thus, for all sufficiently large \(n\),
\[
\sum_{k\ge2}R_{n,k}
\le R_{n,1}\frac{\rho_n}{1-\rho_n}
=R_{n,1}O\!\left(n^2 2^{-n}\right).
\]
So
\[
\sum_{k\ge1}R_{n,k}=R_{n,1}(1+o(1)).
\]
The uniform relative error in Koussas's formula transfers this estimate from \(R_{n,k}\) to \(F(n,n-2k)/F(n,n)\). Therefore the total nonsymmetric mass relative to the symmetric mass is asymptotic to \(R_{n,1}\), and division by one plus that vanishing quantity gives
\[
\Pr(K\ge1)\sim R_{n,1}=\frac{(n-1)(n-2)}{2^n}.
\]

For the conditional statement, compare the tail directly with the one-pair stratum. Uniform relative errors are bounded by a fixed factor for all large \(n\), so
\[
\frac{\sum_{k\ge2}F(n,n-2k)}{F(n,n-2)}
=O\!\left(n^2 2^{-n}\right).
\]
This is equivalent to
\[
\Pr(K=1\mid K\ge1)=1-O\!\left(n^2 2^{-n}\right).
\]

## Verification
The proof is symbolic. The bundled `verify.py` independently checks, using exact integer and rational arithmetic, the identities for \(Q\), \(P\), \(R_{n,k}\), the successive-ratio formula, the first-defect term, and the geometric tail bound for hundreds of finite parameter choices. It does not attempt to verify Maddux's/Koussas's asymptotic counting theorem computationally; that theorem is the literature input.

Running the checker produces a single `VERIFY_OK` line together with the exact assertion count.

## Relationship to prior work
Maddux's 1985 paper defines \(F(n,s)\) and proves a uniform asymptotic formula in both \(n\) and the number \(s\) of symmetric atoms. Koussas's later paper reuses that theorem and proves the qualitative statement that almost all finite nonassociative relation algebras are symmetric integral relation algebras. The present deduction extracts the distribution of the *rare nonsymmetric tail*: its first-order mass is \((n-1)(n-2)2^{-n}\), and, conditional on entering that tail, one converse pair is exponentially dominant.

Targeted searches for “one converse pair,” “non-self-converse atoms,” “nonsymmetric relation algebra asymptotic,” the exact ratio \(F(n,n-2)/F(n,n)\), and equivalent defect-distribution language located the source asymptotic but no statement of this rare-event law. The result is a short consequence of the published uniform formula, so uncatalogued folklore remains a realistic originality risk.

## Limitations
No priority claim is made. The source theorem controls unlabelled isomorphism classes uniformly but does not supply an explicit convergence rate for its relative error, so the displayed equivalent for \(\Pr(K\ge1)\) is asymptotic rather than an error-bounded formula. The sharper \(O(n^2 2^{-n})\) term is only for the conditional concentration of the nonsymmetric tail onto the one-pair stratum. Representable relation algebras are not isolated here; Maddux explicitly left the corresponding representable counting problem open.

## References
1. James M. Koussas, *Finite Relation Algebras*, Journal of Symbolic Logic 88(2), 874-888. Published online 19 October 2021. DOI: 10.1017/jsl.2021.81. arXiv:2202.01959.
2. Roger D. Maddux, *Finite Integral Relation Algebras*, Lecture Notes in Mathematics 1149, 175-197, Springer, 1985.
