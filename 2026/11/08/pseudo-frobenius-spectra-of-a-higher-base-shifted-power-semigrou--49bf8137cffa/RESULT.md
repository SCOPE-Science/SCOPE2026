# Pseudo-Frobenius spectra of a higher-base shifted-power semigroup at terminal-offset multiples

## Finding

For integers \(h\geq3\), \(m\geq1\), and \(d\geq1\), define
\[
 u=h^2-h+1,\qquad v=h^3-h+1,\qquad a=mv,\qquad t=(h-1)^2.
\]
Assume \(\gcd(a,d)=1\). Then the numerical semigroup
\[
 S=\langle a,\,ha+d,\,h^2a+ud,\,h^3a+vd\rangle
\]
has precisely two pseudo-Frobenius numbers:
\[
 \boxed{\operatorname{PF}(S)=\{F-dt,F\}},\qquad
 \boxed{F=a\bigl((m+1)h^3-2h^2-1\bigr)+d(a-1)}.
\]
Consequently the numerical-semigroup type is exactly \(2\), the Frobenius number is \(F\), and the conductor is \(F+1\).

The genus also has a closed form. Put
\[
 B_h=\frac{uh^3(h-1)}2+\frac{h^2u(u-1)}2+th^3+\frac{ht(t-1)}2.
\]
Then
\[
 \boxed{g(S)=\frac{v h^3m(m-1)}2+mB_h+\frac{(d-1)(a-1)}2}.
\]
These formulas apply simultaneously to all permitted values of the three parameters; the four displayed generators are not required to form a minimal generating set.

For \(h=3\), \(m=d=1\), the generators are \(25,76,232,700\), and \(\operatorname{PF}(S)=\{895,899\}\), \(F=899\), \(g(S)=504\).

## Assumptions and scope

All semigroups are additive submonoids of the nonnegative integers. A gap is a nonnegative integer not in \(S\). A pseudo-Frobenius number is an integer \(f\notin S\) such that \(f+s\in S\) for every nonzero \(s\in S\). The genus counts nonnegative gaps. Because \(\gcd(a,ha+d)=\gcd(a,d)=1\), the semigroup is numerical. The restriction \(h\ge3\), the positivity of \(d\), and the divisibility \(v\mid a\) are used throughout; no result for other parameters is asserted.

## Proof

**1. Weighted coin cost.** Define for nonnegative integers \(M\)
\[
 O(M)=\min\{hx+h^2y+h^3z:x+uy+vz=M,\quad x,y,z\in\mathbb N_0\}.
\]
For the two denominations \(1,u\), the optimum is
\[
 H(M)=h^2\left\lfloor\frac M u\right\rfloor+h(M\bmod u).
\]
Indeed, replacing \(u\) unit coins by one \(u\)-coin saves \(hu-h^2>0\), and this is the only possible reduction among these denominations.

The identity \(v=hu+t\), where \(t=(h-1)^2\) and \(u-t=h\), gives, on writing \(M=qu+r\) with \(0\le r<u\),
\[
 H(M+v)-H(M)=
 \begin{cases}
 h^3+ht,&r+t<u,\\
 h^3,&r+t\ge u.
 \end{cases}
\]
In particular \(H(M+v)\ge H(M)+h^3\). To optimize a representation using \(z\) copies of \(v\), its cost is \(zh^3+H(M-zv)\), which cannot decrease when \(z\) is reduced. Hence the maximum feasible number of \(v\)-coins is optimal:
\[
 \boxed{O(M)=h^3\lfloor M/v\rfloor+H(M\bmod v)}.
\]
This proves, for every \(M\ge0\), the exact translation law \(O(M+v)=O(M)+h^3\), and therefore \(O(M+a)=O(M)+mh^3\).

**2. Exact Apéry set.** For \(0\le r<a\), let \(W_r\) denote the least element in \(S\) congruent to \(dr\) modulo \(a\). Every combination of the three generators other than \(a\) is \(aC+dM\), where \(M\ge0\) is its total offset and \(C\ge O(M)\). The offset must satisfy \(M\equiv r\pmod a\), hence \(M=r+ja\) with \(j\ge0\). Since \(O(r+ja)=O(r)+jmh^3\) and \(d>0\), the minimum is at \(j=0\), giving
\[
 \boxed{W_r=aO(r)+dr\qquad(0\le r<a).}
\]
The Apéry set is precisely \(\{W_0,\ldots,W_{a-1}\}\), with indices permuted by multiplication by \(d\) modulo \(a\). Its gaps immediately yield the genus formula below.

**3. Pseudo-Frobenius criterion.** The standard Apéry criterion says that \(W_r-a\), for \(r>0\), is pseudo-Frobenius if and only if adding every non-\(a\) generator yields an element of \(S\). For a non-\(a\) generator of form \(ca+db\), where \((b,c)\) is one of \((1,h),(u,h^2),(v,h^3)\), our Apéry description gives the following exact inequalities:
\[
 \begin{cases}
 O(r+b)-O(r)\le c-1,&r+b<a,\\
 O(r+b-a)\le O(r)+c-1+d,&r+b\ge a.
 \end{cases}
\]
When \(r<a-v\), the \(b=v\) test fails, since the first line would demand \(h^3\le h^3-1\). Thus a surviving index has the form \(r=(m-1)v+s\) with \(0\le s<v\).

For \(s<v-u\), the \(b=u\) test fails: \(O(r+u)-O(r)=H(s+u)-H(s)=h^2\). Hence \(s\ge v-u\).

For \(s<v-1\), the \(b=1\) test requires \(H(s+1)-H(s)\le h-1\). This difference is \(h\), except if \(s\equiv u-1\pmod u\), when it equals \(h^2(2-h)\). On the interval \(v-u\le s<v-1\) the only such residue is \(s_0=hu-1\). The endpoint \(s_1=v-1\) instead wraps around and remains a candidate. Thus there are at most two pseudo-Frobenius elements, indexed by \(s_0\) and \(s_1\).

It remains to check the wrapped generator tests, not just their necessity. The facts
\[
 H(s_0)=H(s_1)=2h^2(h-1),\quad
 s_0+u-v=h-1,\quad s_1+u-v=u-1
\]
show that the wrapped \(b=u\) tests succeed: \(H(s_0)>H(h-1)\) and \(H(s_1)>H(u-1)\), while all added terms in the second line of the criterion are nonnegative. The \(b=1\) test succeeds at \(s_0\) by its negative cost jump, and at \(s_1\) by wrapping to zero. Both \(b=v\) tests wrap to \(s_0\) or \(s_1\), respectively, and succeed because \(O(r)+h^3-1+d\ge O(s)\) for \(m\ge1,d\ge1\). Hence **both** surviving candidates really are pseudo-Frobenius.

For either \(i=0,1\), the associated Apéry representative is
\[
 W_{(m-1)v+s_i}=a\bigl((m-1)h^3+2h^2(h-1)\bigr)+d\bigl((m-1)v+s_i\bigr).
\]
Since \(s_1-s_0=t\), subtracting \(a\) from these representatives gives exactly \(\{F-dt,F\}\) with the stated \(F\). Both are distinct because \(dt>0\).

**4. Genus.** The Apéry genus identity is
\[
 g(S)=\frac1a\sum_{r=0}^{a-1}W_r-\frac{a-1}{2}
 =\sum_{r=0}^{a-1}O(r)+\frac{(d-1)(a-1)}2.
\]
Partition \(0\le r<mv\) into \(m\) blocks of length \(v\), use \(O(qv+s)=qh^3+H(s)\), and obtain
\[
 \sum_{r=0}^{a-1}O(r)=\frac{vh^3m(m-1)}2+m\sum_{s=0}^{v-1}H(s).
\]
Finally, the interval \(0\le s<v=hu+t\) comprises \(h\) complete \(u\)-blocks and a tail of length \(t\). Summing the displayed formula for \(H\) gives
\[
 \sum_{s=0}^{v-1}H(s)
 =\frac{uh^3(h-1)}2+\frac{h^2u(u-1)}2+th^3+\frac{ht(t-1)}2=B_h.
\]
This proves the genus formula, completing the theorem.

## Verification

The standalone script `verify_semigroup.py` computes the formulas and separately reconstructs Apéry sets by integer Dijkstra shortest paths on residue classes. It compares the complete pseudo-Frobenius sets and genera for all admissible parameter triples \(3\le h\le12\), \(1\le m\le4\), and \(1\le d\le12\). There are exactly 300 coprime triples in this range; every comparison passes. Run `python3 verify_semigroup.py` and compare to `verification_output.txt`. These finite computations validate examples and implementation, not the universal quantifiers; the proof above supplies the latter.

## Relationship to prior work

Liu, Xin, Ye, and Yin explicitly introduce the higher-base family with offsets \(h^i-h+1\) and identify difficulty of the weighted Frobenius problem in Section 7 of arXiv:2306.03459v4. Their general Apéry minimization method is acknowledged; their Section 7 does not state the terminal-offset-divisible subfamily's two-element pseudo-Frobenius spectrum, nor the accompanying closed genus and Frobenius formulas. The present result finds an arithmetic subfamily in which the weighted coin minimization is exactly periodic.

The same authors' arXiv:2306.10738 treats coefficients with repunit offsets \((b^i-1)/(b-1)\); these differ from the offsets in this theorem for base \(h\ge3\). Branco, Colaço, and Ojeda study another generalized repunit setting rather than this three-parameter subfamily. Generic Apéry identities are prior mathematics, not claimed as contributions here.

## Limitations

This classification requires \(a=m(h^3-h+1)\), \(d>0\), and \(h\ge3\), and considers exactly three non-\(a\) generators. It does not settle the full higher-base family for arbitrary \(a\), all possible lengths, or negative \(d\). An equivalent theorem in literature not located by the searches remains possible.

## References

1. F. Liu, G. Xin, S. Ye, J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459v4, particularly Sections 2 and 7, https://arxiv.org/abs/2306.03459 (first public version 2023-06-06).
2. F. Liu, G. Xin, S. Ye, J. Yin, *A Note on Generalized Repunit Numerical Semigroups*, arXiv:2306.10738v1, https://arxiv.org/abs/2306.10738 (2023-06-19).
3. M. B. Branco, I. Colaço, I. Ojeda, *The Frobenius Problem for Generalized Repunit Numerical Semigroups*, arXiv:2112.01106, https://arxiv.org/abs/2112.01106.
