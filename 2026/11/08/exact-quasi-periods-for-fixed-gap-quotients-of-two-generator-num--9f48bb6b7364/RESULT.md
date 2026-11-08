# Exact quasi-periods for fixed-gap quotients of two-generator numerical semigroups

## Finding

Fix integers \(p\ge2\) and \(h\ge2\) with \(\gcd(p,h)=1\). For every integer \(a>\max\{p,h(p-1)\}\) with \(\gcd(a,h)=1\), let \(S_{a,h}=\langle a,a+h\rangle\) and define the quotient semigroup \(S_{a,h}/p=\{n\in\mathbb Z_{\ge0}:pn\in S_{a,h}\}\). Let \(G_{p,h}(a)\) be its Frobenius number, the largest nonnegative integer excluded from the quotient.

For each residue \(r\in\{0,\ldots,p-1\}\), put
\[
\delta_r(t)=\operatorname{rem}_p\bigl(h^{-1}(r^2+(h-2)r-h-tr)\bigr),\qquad 0\le t\le p-1,
\]
where \(h^{-1}\) denotes the inverse of \(h\) modulo \(p\), and \(\operatorname{rem}_p\) is the least residue in \(\{0,\ldots,p-1\}\). Define
\[
I_r=\min\{0\le t\le p-1:\delta_r(t)\le t\},\qquad J_r=\delta_r(I_r).
\]
The set defining \(I_r\) is nonempty (\(t=p-1\) always qualifies). Then the following is an exact formula for every admissible \(a\equiv r\pmod p\):
\[
\boxed{G_{p,h}(a)=\frac{a^2+(h-2-I_r)a-h(1+J_r)}p.}
\]
Moreover, the **least eventual quasi-polynomial period** on the admissible domain \(\gcd(a,h)=1\) is **exactly \(p\)**: no positive period \(d\) with \(p\nmid d\) can support polynomial constituent formulas valid on all sufficiently large admissible \(a\). In particular, no period collapse occurs for any coprime fixed gap \(h\ge2\).

## Assumptions and scope

The modulus \(p\) and gap \(h\) are fixed positive integers satisfying \(p\ge2\), \(h\ge2\), and \(\gcd(p,h)=1\). The variable \(a\) is a positive integer satisfying \(\gcd(a,h)=1\) and \(a>\max\{p,h(p-1)\}\). A quasi-polynomial period \(d\) on this restricted domain means that polynomials \(R_0,\ldots,R_{d-1}\in\mathbb C[X]\) exist with \(G_{p,h}(a)=R_{a\bmod d}(a)\) for every sufficiently large admissible \(a\). This definition permits a threshold depending on \(d,p,h\). There are infinitely many admissible \(a\) in every class modulo \(p\), because \(\gcd(p,h)=1\).

## Proof

**1. Symmetry for two generators.** Put \(b=a+h\) and \(F=ab-a-b=a^2+(h-2)a-h\). Since \(\gcd(a,b)=1\), the standard two-generator Frobenius formula gives \(F\) as the largest gap. We recall why \(m\in\langle a,b\rangle\) exactly when \(F-m\notin\langle a,b\rangle\), for \(0\le m\le F\). Choose the unique \(y\in\{0,\ldots,a-1\}\) with \(m\equiv yb\pmod a\) and write \(m=yb+ka\). Then \(m\in\langle a,b\rangle\) iff \(k\ge0\); indeed every other nonnegative coefficient of \(b\) has the form \(y+ta\) and only increases its required amount. On the other hand, \(F-m=(a-1-y)b-(k+1)a\), hence \(F-m\in\langle a,b\rangle\) iff \(k\le-1\). Exactly one belongs. For the quotient, its largest gap is therefore \((F-w)/p\), provided \(w\le F\), where \(w\) is the smallest element of \(\langle a,b\rangle\) congruent to \(F\pmod p\).

**2. Exact least representative.** Every semigroup element can be written as \(ta+hy\) with integers \(t\ge0\) and \(0\le y\le t\), by taking \(t\) to be the sum of the two original generator coefficients. Fix \(r=a\bmod p\). For \(t\le p-1\), the unique \(y\in\{0,\ldots,p-1\}\) satisfying \(ta+hy\equiv F\pmod p\) is \(y=\delta_r(t)\), because \(h\) is invertible modulo \(p\). Thus an admissible pair at this \(t\) exists exactly if \(\delta_r(t)\le t\). The pair \((I_r,J_r)\) is the lexicographically first such pair, and \(J_r\le I_r\le p-1\). For any competing element \(ta+hy\equiv F\pmod p\), a value \(t<I_r\) is impossible by minimality. If \(t=I_r\), then \(y=J_r\) because \(0\le y\le I_r<p\). If \(t>I_r\), then \(ta+hy\ge(I_r+1)a>I_ra+hJ_r\), using \(a>h(p-1)\). Hence
\[
w=I_ra+hJ_r\le(p-1)(a+h).
\]
Since \(a>p\),
\[
F-(p-1)(a+h)=a(a-p-1)+h(a-p)>0.
\]
Therefore \(0\le w<F\). Symmetry and congruence imply \(G_{p,h}(a)=(F-w)/p\), yielding the displayed exact quadratic constituent formula.

**3. Uniqueness of the zero-residue constituent.** At \(r=0\), one has \(\delta_0(t)=p-1\) for every \(t\), hence \((I_0,J_0)=(p-1,p-1)\). Suppose that some \(1\le r\le p-1\) had the same pair. The condition \(J_r=p-1\) at \(t=p-1\) implies
\[
r^2+(h-1)r\equiv0\pmod p.
\]
At \(t=p-2\), the same congruence then gives
\[
\delta_r(p-2)=\operatorname{rem}_p(h^{-1}r-1).
\]
Because \(r\not\equiv0\pmod p\) and \(h\) is invertible, this least residue belongs to \(\{0,\ldots,p-2\}\). Thus \(I_r\le p-2\), a contradiction. So \((I_0,J_0)\) is unique, and its constituent polynomial differs from every other polynomial (their coefficients determine \(I_r,J_r\)).

**4. Rigidity of the period on a restricted domain.** The formula gives the period \(p\). Suppose that \(d\ge1\) is another eventual quasi-polynomial period, with polynomials \(R_s\) on admissible integers in class \(s\pmod d\). Put \(g=\gcd(p,d)\) and suppose \(g<p\). By the Chinese remainder theorem choose \(a_0\) satisfying \(a_0\equiv0\pmod p\) and \(a_0\equiv1\pmod h\), and set \(s=a_0\bmod d\). There are arbitrarily large integers satisfying each of the two systems
\[
 a\equiv0\pmod p,\ a\equiv s\pmod d,\ a\equiv1\pmod h,
\]
\[
 a\equiv g\pmod p,\ a\equiv s\pmod d,\ a\equiv1\pmod h.
\]
Indeed the pairwise CRT compatibility conditions are satisfied: \(g\equiv s\equiv0\pmod{\gcd(p,d)}\), \(\gcd(p,h)=1\), and \(s\equiv1\pmod{\gcd(d,h)}\). All these integers satisfy \(\gcd(a,h)=1\). On the first progression \(R_s=Q_0\) as polynomials, where \(Q_r\) is the displayed constituent; on the second \(R_s=Q_g\). Each identity holds at infinitely many arguments, hence polynomially. This contradicts \(Q_0\ne Q_g\). Therefore \(p\mid d\) for every eventual quasi-period, and the minimal one is \(p\). \(\square\)

## Verification

The included standalone Python verifier computes the residue coefficients using exact modular arithmetic, independently computes quotient Frobenius numbers using membership in \(\langle a,a+h\rangle\), and checks the formula over \(1{,}920\) admissible examples with \(2\le p\le20\), \(1\le h\le10\). The acceptance claim restricts to \(h\ge2\); \(h=1\) serves as an additional known-case cross-check. The code checks the uniqueness of the zero-residue coefficient pair for every tested \(p,h\). The universal claims require the proof, not finite enumeration.

For example, at \(p=5,h=2\) the five pairs \((I_r,J_r)\), ordered by \(r=0,1,2,3,4\), are \((4,4),(2,1),(1,0),(4,0),(1,0)\), and at admissible \(a=9\) the Frobenius number of the quotient is \(14\).

To reproduce: run `python3 verify.py` with Python 3.8 or newer. It uses only the standard library and raises on any discrepancy.

## Relationship to prior work

Feihu Liu's July 2026 work, *On the Frobenius Number of Quotients of Numerical Semigroups* (arXiv:2607.23076v1), establishes quadratic quasi-polynomial behavior for the special gap \(h=1\), with period dividing \(p\), and a finite residue formula for that case. The present theorem concerns the distinct full family of gaps \(h\ge2\) coprime to \(p\), gives explicit uniform constituent formulas, and proves exact minimal period even on the restricted coprime domain. An independently existing exact-period result for gap \(h=1\) does not imply this higher-gap statement. Liu's April 2026 *The Frobenius problem for a class of quotients of numerical semigroups* (arXiv:2604.26415v1) imposes a divisibility restriction on the quotient parameter relative to a generator, so its general statements do not give the full moving-residue classification proved here. Neither source's inspected result states the new higher-gap theorem.

## Limitations

The theorem does not cover \(\gcd(p,h)>1\), variable \(p\) or \(h\) as quasi-polynomial inputs, nor small \(a\) outside the stated threshold. The threshold is sufficient, not asserted optimal. Historical novelty is subject to coverage limits from unindexed literature and inaccessible material. No external independent audit has been performed.

## References

1. Feihu Liu, *On the Frobenius Number of Quotients of Numerical Semigroups*, arXiv:2607.23076v1 (first posted 2026-07-25), especially Theorem 5.3 and Corollary 5.5.
2. Feihu Liu, *The Frobenius problem for a class of quotients of numerical semigroups*, arXiv:2604.26415v1 (first posted 2026-04-29), introduction and quotient assumptions.
3. Classical Sylvester two-generator Frobenius formula; the symmetry required above is proved directly.
