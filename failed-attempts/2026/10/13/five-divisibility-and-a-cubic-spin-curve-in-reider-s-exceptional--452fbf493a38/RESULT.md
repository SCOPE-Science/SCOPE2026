# Five-divisibility and a cubic-spin curve in Reider's exceptional branch
## Finding
Let \(X\) be a smooth minimal irregular complex surface of general type with no irrational pencil. Assume that \(X\) contains no rational curve \(C\) with \(K_X\!\cdot C\in\{0,1\}\). For a nonzero twisted Kodaira–Spencer class \(\xi\in H^1(\Theta_X(-K_X))\), use Reider's notation \(E_\xi\) and \(\mathcal F_\xi\).

If
\[
h^1\!\left(\mathcal F_\xi^*(-K_X-E_\xi)\right)=1,
\]
then there is a positive integer \(m\) for which
\[
\chi(\mathcal O_X)=5m,\qquad q(X)=2,\qquad p_g(X)=5m+1,
\]
\[
K_X^2=24m,\qquad c_2(X)=36m.
\]
The smooth irreducible curve \(E_\xi\) satisfies
\[
E_\xi^2=6m,\qquad g(E_\xi)=9m+1,
\]
and its normal bundle is a cubic spin structure:
\[
N_{E_\xi/X}^{\otimes 3}\cong K_{E_\xi}.
\]
The full degree-two Hodge/intersection profile is also forced:
\[
h^{1,1}(X)=26m+4,\qquad b_2^+(X)=10m+3,\qquad b_2^-(X)=26m+3.
\]
Consequently, the one-dimensional exceptional branch in Reider's theorem is impossible whenever \(5\nmid\chi(\mathcal O_X)\).

## Assumptions and scope
The hypotheses are exactly the surface hypotheses needed for the exceptional alternative in Reider's main theorem: \(X\) is smooth, minimal, irregular, of general type, has no irrational pencil, and has no rational curve of canonical degree \(0\) or \(1\). The finding additionally assumes a nonzero \(\xi\in H^1(\Theta_X(-K_X))\) for which Reider's exceptional cohomology group has dimension \(1\).

The conclusion is conditional. It gives necessary numerical and curve-theoretic structure if this exceptional branch occurs; it does not construct such a surface or claim existence for any positive integer \(m\).

## Proof
Reider proves in the exceptional dimension-one case that
\[
\mathcal O_X(K_X)\cong\mathcal O_X(2E_\xi),\qquad q(X)=2,\qquad K_X^2=\frac23c_2(X),
\]
and that \(E_\xi\) is irreducible and smooth with split normal sequence.

Noether's formula gives
\[
K_X^2+c_2(X)=12\chi(\mathcal O_X).
\]
Substituting \(c_2(X)=\tfrac32K_X^2\) yields
\[
\frac52K_X^2=12\chi(\mathcal O_X),
\]
hence
\[
K_X^2=\frac{24}{5}\chi(\mathcal O_X),\qquad c_2(X)=\frac{36}{5}\chi(\mathcal O_X).
\]
Because \(K_X^2\) and \(\chi(\mathcal O_X)\) are integers and \(\gcd(24,5)=1\), one has \(5\mid\chi(\mathcal O_X)\). General type gives \(K_X^2>0\), so write \(\chi(\mathcal O_X)=5m\) with \(m\ge1\). This gives \(K_X^2=24m\) and \(c_2(X)=36m\). Since \(q=2\) and \(\chi(\mathcal O_X)=1-q+p_g\), one gets \(p_g=5m+1\).

The line-bundle identity \(K_X\sim2E_\xi\) gives
\[
E_\xi^2=\frac14K_X^2=6m.
\]
Adjunction on the smooth curve \(E_\xi\) gives
\[
2g(E_\xi)-2=E_\xi\cdot(E_\xi+K_X)=3E_\xi^2=18m,
\]
so \(g(E_\xi)=9m+1\). Since \(N_{E_\xi/X}\cong\mathcal O_{E_\xi}(E_\xi)\), adjunction and \(K_X\sim2E_\xi\) give
\[
K_{E_\xi}\cong\mathcal O_{E_\xi}(K_X+E_\xi)\cong\mathcal O_{E_\xi}(3E_\xi)\cong N_{E_\xi/X}^{\otimes3}.
\]

Finally, \(b_1=2q=4\) and the topological Euler identity \(c_2=2-2b_1+b_2\) give \(b_2=36m+6\). For a compact Kähler surface, \(b_2^+=1+2p_g=10m+3\). Therefore \(b_2^-=26m+3\), and \(h^{1,1}=b_2-2p_g=26m+4\).

## Verification
The proof is symbolic and does not rely on finite enumeration. The accompanying `verify.py` checks the coefficient identities in the formal parameter \(m\), including Noether's formula, the Chern-number ratio, adjunction, the Hodge-number decomposition, and the degree identity \(3\deg N_{E_\xi/X}=2g(E_\xi)-2\). Its stored output ends in `VERIFY_OK`.

The verifier does not certify Reider's theorem; that theorem is the primary mathematical input and was checked in the source itself. The remaining steps are standard exact identities for smooth compact complex surfaces and smooth curves.

## Relationship to prior work
Reider's 2026 paper proves the three decisive inputs for the exceptional branch: \(K_X\sim2E_\xi\), \(q=2\), and \(K_X^2=\tfrac23c_2\), together with smoothness and splitting of the normal sequence of \(E_\xi\). The paper also explicitly uses Noether's formula elsewhere. It does not state the five-divisibility obstruction, the integral geography ray \((\chi,K^2,c_2)=(5m,24m,36m)\), the genus formula for \(E_\xi\), the cubic-root normal bundle, or the resulting Hodge/intersection profile in the inspected text.

Exact-phrase, numerical, and equivalent-formulation searches for those consequences did not locate a covering published statement. The closest retrieved surface-invariant results concern different surfaces and do not imply this exceptional-branch package.

## Limitations
This finding is a consequence theorem, not an existence or classification theorem for surfaces on the resulting geography ray. In particular, it does not show that any \(m\ge1\) is realized, nor that the displayed numerical and cubic-spin conditions are sufficient for the exceptional cohomology branch.

The arithmetic part follows quickly once Reider's exceptional identities are known. Its mathematical value is the conversion of a cohomologically defined exceptional alternative into an immediately testable congruence obstruction and a rigid curve/Hodge package. A differently phrased observation in older surface-geography literature remains a residual bibliographic risk.

## References
1. Igor Reider, *Twisted Kodaira–Spencer Classes and the Inequality of Severi*, Geometry 3 (2026), article 17, DOI `10.3390/geometry3030017`, published 2026-09-03.
