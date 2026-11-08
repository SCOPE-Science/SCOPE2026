# Conjugate-commuting probability in the first class-three unitriangular group

## Finding

Let \(q\) be any prime power and \(G=\operatorname{UT}_4(\mathbb F_q)\), the group of unipotent upper triangular \(4\times4\) matrices. Let \(\rho(G)\) be the probability that two independent uniformly sampled elements have *some conjugates which commute*. Then

\[
\boxed{\rho(G)=\frac{2q^5-3q^4+3q^3+2q^2-4q+1}{q^7}.}
\]

For comparison, the probability \(\operatorname{cp}(G)\) that the two sampled elements themselves commute is

\[
\operatorname{cp}(G)=\frac{2q^2+q-2}{q^5},\qquad
\boxed{\rho(G)-\operatorname{cp}(G)=\frac{(q-1)^3(q+1)(2q-1)}{q^7}>0.}
\]

Thus this natural conjugacy-relaxed commuting probability differs strictly from ordinary commuting probability in every field characteristic. The ratio \(\rho(G)/\operatorname{cp}(G)\) is asymptotic to \(q\) as \(q\to\infty\). In contrast, for the class-two group \(\operatorname{UT}_3(\mathbb F_q)\), conjugation does not change any commutator, so these two probabilities coincide.

## Assumptions and scope

The parameter \(q\ge2\) ranges over all prime powers; no odd-characteristic assumption is imposed. Each matrix in \(G\) is represented uniquely by the six entries

\[
X(a,b,c,d,e,f)=
\begin{pmatrix}
1&a&d&f\\0&1&b&e\\0&0&1&c\\0&0&0&1
\end{pmatrix}.
\]

Write the second input as \(Y=X(A,B,C,D,E,F)\). The ordered-pair count corresponding to \(\rho(G)\) is \(|G|^2\rho(G)\), where \(|G|=q^6\). Two *different* conjugators are permitted in the definition; equivalently, one can hold \(X\) fixed and conjugate only \(Y\).

## Proof

**Step 1: Reduce commutation to three equations.** Direct multiplication shows that \(X\) and \(Y\) commute if and only if

\[
aB-Ab=0,\qquad bC-Bc=0,\qquad K:=aE+dC-Ae-Dc=0.
\]

The outermost entries \(f,F\) never occur. When \(Y\) is replaced by a conjugate \(H^{-1}YH\), with the three first-superdiagonal entries of \(H\) denoted \((u,v,w)\), the entries \(A,B,C\) stay fixed, while

\[
D\longmapsto D+Av-uB,\qquad
E\longmapsto E+Bw-vC.
\]

Higher-superdiagonal entries of \(H\) affect neither of these changes. Hence, after assuming the first two equations, the third expression changes by

\[
\Delta=B(aw+cu)-v(aC+cA).
\]

This map \(\mathbb F_q^3\to\mathbb F_q\) is linear. Its image is either zero or all of \(\mathbb F_q\), independently of the characteristic. If it is surjective, all \(q^4\) choices of \((d,e,D,E)\) admit conjugates which commute. If it is zero, the condition is precisely \(K=0\); it holds for \(q^3\) choices unless \(K\) is identically zero, in which case it holds for \(q^4\). The latter case is exactly \(a=c=A=C=0\).

**Step 2: Count the primary-coordinate configurations.** Impose \(aB=Ab\) and \(bC=Bc\). The following seven disjoint cases exhaust the possibilities; the last column gives the number of allowed choices of \((d,e,D,E)\) for each primary configuration.

| Condition | Number of primary configurations | Choices |
|---|---:|---:|
| \(b\ne0,\ (a,c)=(0,0)\) | \(q(q-1)\) | \(q^4\) |
| \(b\ne0,\ (a,c)\ne(0,0),\ (A,B,C)=t(a,b,c),\ t\ne0\) | \((q-1)^2(q^2-1)\) | \(q^4\) |
| Same, but \(t=0\) | \((q-1)(q^2-1)\) | \(q^3\) |
| \(b=0,\ (a,c)\ne(0,0),\ B=0,\ aC+cA\ne0\) | \((q^2-1)(q^2-q)\) | \(q^4\) |
| Same, but \(aC+cA=0\) | \(q(q^2-1)\) | \(q^3\) |
| \((a,b,c)=(0,0,0),\ (A,C)=(0,0)\) | \(q\) | \(q^4\) |
| \((a,b,c)=(0,0,0),\ (A,C)\ne(0,0)\) | \(q(q^2-1)\) | \(q^3\) |

For the first three rows, division by \(b\) gives \((A,B,C)=t(a,b,c)\). For the fourth and fifth rows, the nonzero linear form \((A,C)\mapsto aC+cA\) has a kernel of size \(q\). The final two rows follow by setting \((a,b,c)=0\). Thus the numbers of primary configurations giving \(q^4\) and \(q^3\) valid choices respectively are

\[
N_4=2q^4-3q^3+3q-1,\qquad
N_3=(q^2-1)(3q-1).
\]

Since \(f\) and \(F\) are arbitrary, there are exactly

\[
q^2\bigl(q^4N_4+q^3N_3\bigr)
=q^5(2q^5-3q^4+3q^3+2q^2-4q+1)
\]

ordered conjugate-commuting pairs. Dividing by \(q^{12}\) gives the first formula.

**Step 3: Count genuinely commuting pairs.** For the same primary coordinates, without conjugation the linear form \(K\) is identically zero precisely when \(a=c=A=C=0\). There are \(q^2\) such primary pairs; all other allowed primary pairs yield exactly \(q^3\) solutions of \(K=0\). The total number of allowed primary pairs is \(N_4+N_3\). Therefore the number of commuting ordered matrix pairs is

\[
q^2\bigl(q^2q^4+(N_4+N_3-q^2)q^3\bigr)=q^7(2q^2+q-2).
\]

Division by \(q^{12}\) gives \(\operatorname{cp}(G)\). Subtracting and factoring establishes the strict inequality and the displayed difference for every \(q\ge2\). The asymptotics are immediate from the leading terms.

## Verification

The standalone program `verify.py` exhaustively evaluates every choice of primary coordinates and middle entries for \(q=2,3,4\), determining the full attainable conjugation corrections by enumerating first-superdiagonal conjugators rather than using the classification in Step 2. The field of four elements is represented by \(\mathbb F_2[t]/(t^2+t+1)\). The program separately enumerates literal group multiplication, inverses, and conjugation for all ordered pairs when \(q=2\). Running `python3 verify.py` reproduces `verify_output.txt`. Independently running `python3 centralizer_crosscheck.py` checks literal \(4\times4\) multiplication and the entire centralizer-size distribution for \(q=2,3\), reproducing `centralizer_crosscheck_output.txt`.

The full ordered conjugate-commuting and commuting pair counts are respectively \((1312,1024)\) for \(q=2\), \((80433,41553)\) for \(q=3\), and \((1524736,557056)\) for \(q=4\). These finite experiments corroborate the algebraic proof; they do not replace the general finite-field argument.

## Relationship to prior work

Britnell and Wildon introduced and studied the relation between commuting conjugacy classes in their 2007 preprint [1]. Blackburn, Britnell and Wildon [2] formulated \(\rho(G)\), established results for symmetric groups, and discussed general questions for arbitrary finite groups. The present calculation addresses a specific nilpotent family absent from their stated results. Kaur, Sharma and Singh [3] computed branching rules and ordinary commuting-tuple probabilities for \(\operatorname{UT}_4(\mathbb F_q)\) in odd characteristic. Those are different statistics: a count of simultaneously commuting tuples does not itself provide the existence-of-commuting-conjugates indicator for each ordered pair. The explicit \(\rho\) formula and the characteristic-uniform strict gap are the new statements assessed here. **Comparison caveat:** the ordinary-commuting entry for \(\operatorname{UT}_4\) in Section 8 of [3] is \((2q^3-1)/q^6\) for odd \(q\), which differs from our companion calculation. This disagreement does not affect the algebraic case analysis of \(\rho\); we explicitly verified ordinary commutation using literal \(4\times4\) multiplication on every ordered pair for \(q=3\), obtaining \(41553/531441=57/729\), whereas the displayed expression in [3] gives \(53/729\). We record this unresolved literature discrepancy rather than treating the competing formula as support or novelty evidence.

## Limitations

This result treats only the group \(\operatorname{UT}_4(\mathbb F_q)\); it does not determine \(\rho\) for larger unitriangular groups or arbitrary class-three groups. It counts ordered element pairs rather than all pairwise incidences between individual conjugacy classes. Historical priority is provisional and independent mathematical validation has not been performed.

## References

[1] J. R. Britnell and M. Wildon, *Commuting elements in conjugacy classes: An application of Hall's Marriage Theorem*, arXiv:0708.3872, first publicly posted 2007-08-28. https://arxiv.org/abs/0708.3872

[2] S. R. Blackburn, J. R. Britnell and M. Wildon, *The probability that a pair of elements of a finite group are conjugate*, arXiv:1108.1784, first publicly posted 2011-08-08. https://arxiv.org/abs/1108.1784

[3] D. Kaur, U. B. Sharma and A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493, first publicly posted 2020-06-02. https://arxiv.org/abs/2006.01493
