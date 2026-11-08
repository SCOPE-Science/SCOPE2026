# Pseudo-Frobenius spectra of four-generator negative repunit semigroups

## Finding
For every integer \(a\ge 8\), define the numerical semigroup
\[
S_a=\langle a,\,2a-1,\,4a-3,\,8a-7\rangle
\subseteq\mathbb Z_{\ge0}.
\]
Its complete pseudo-Frobenius set is governed by a period-seven table. Define
\[
h=(0,1,2,1,2,3,2),\qquad
\lambda(m)=\left\lfloor\frac m7\right\rfloor+h_{m\bmod7},
\qquad P_a(m)=(a-1)m+a\lambda(m)-a.
\]
For \(r=a\bmod7\), the table below gives the finite set \(J_r\):

| \(r\) | \(J_r\) | \(\operatorname{type}(S_a)\) |
|---|---|---|
| \(0\) | \(\{0,1\}\) | \(2\) |
| \(1\) | \(\{0,1,2\}\) | \(3\) |
| \(2\) | \(\{0,2,3\}\) | \(3\) |
| \(3\) | \(\{0,4\}\) | \(2\) |
| \(4\) | \(\{0,1,5\}\) | \(3\) |
| \(5\) | \(\{0,2,6\}\) | \(3\) |
| \(6\) | \(\{0\}\) | \(1\) |

Then, **for every integer \(a\ge8\)**,
\[
\boxed{\operatorname{PF}(S_a)
=\{P_a(a-1-j):j\in J_{a\bmod7}\}.}
\]
In particular, \(S_a\) is symmetric if and only if \(a\equiv6\pmod7\). Its Frobenius number is the maximum of the displayed set, equivalently \(P_a(a-2)\) if \(a\equiv0\pmod7\), \(P_a(a-3)\) if \(a\equiv1\pmod7\), and \(P_a(a-1)\) in the other five cases. The semigroups genuinely have embedding dimension four for all \(a\ge8\).

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb Z_{\ge0}\). Its pseudo-Frobenius numbers are the integers \(z\notin S\) for which \(z+s\in S\) for every \(s\in S\setminus\{0\}\). Its type is the number of pseudo-Frobenius numbers; the standard characterization says it is symmetric exactly when its type is one. The integer parameter ranges over all \(a\ge8\), with no primality or parity restrictions. The four displayed generators have greatest common divisor one, so each \(S_a\) is a numerical semigroup.

## Proof
**1. Exact coin cost and Apéry set.** Let \(\lambda(m)\) be the minimum number of coins from \(\{1,3,7\}\) needed to sum to \(m\). For a fixed \(m=7q+r\), \(0\le r<7\), a coin representation with \(q-t\) seven-coins, \(t\ge0\), needs at least \(\lfloor(7t+r)/3\rfloor+((7t+r)\bmod3)\) additional coins. Its total length is at least
\[
q-t+\left\lfloor\frac{7t+r}{3}\right\rfloor+((7t+r)\bmod3).
\]
Increasing \(t\) by three increases this expression by four. For \(t=0,1,2\), subtracting \(q\) yields, respectively, the triples
\[
(0,2,4),\ (1,3,3),\ (2,2,4),\ (1,3,5),\
(2,4,4),\ (3,3,5),\ (2,4,6)
\]
for \(r=0,1,\ldots,6\). Thus choosing the maximum possible number of seven-coins is optimal and \(\lambda(m)=q+h_r\) for every \(m\ge0\).

For any representation using the three generators other than \(a\), write \(M=x_1+3x_3+7x_7\) and \(L=x_1+x_3+x_7\). Its value is \((a-1)M+aL\) and its residue modulo \(a\) is \(-M\). For \(0\le m<a\), the least such value with \(M=m\) equals \((a-1)m+a\lambda(m)\). Any representation of the same residue with \(M=m+qa\), \(q\ge1\), has value at least \((a-1)(m+a)+a\). This is strictly larger than \((a-1)m+am\), an upper bound using \(m\) unit coins, because their difference is \(a(a-m)>0\). Adding copies of the generator \(a\) cannot improve a residue minimum. Consequently the entire Apéry set at \(a\) is exactly
\[
\operatorname{Ap}(S_a,a)=\{W_a(m):0\le m<a\},\qquad
W_a(m)=(a-1)m+a\lambda(m).
\]
Distinct indices give distinct residues, so the elements are distinct.

**2. Maximality criterion.** Put \(W=W_a\), and order Apéry elements by \(u\preceq_S v\) if \(v-u\in S_a\). The increments \(W(m+1)-W(m)\) are \(2a-1\) for residues \(m\equiv0,1,3,4\pmod7\) and \(-1\) for \(m\equiv2,5,6\pmod7\). Hence an earlier index \(m'<m\) satisfies \(W(m')-W(m)\le2\); at most two consecutive downward steps occur before a positive step of size \(2a-1\). Because the least positive element of \(S_a\) is \(a\ge8\), an earlier index cannot dominate a later one.

For \(m'<m\), let \(\delta=m-m'\), so \(0<\delta<a\). The least member of \(S_a\) congruent to \(-\delta\pmod a\) is \(W(\delta)\). Therefore
\[
W(m)-W(m')\in S_a
\quad\Longleftrightarrow\quad
\lambda(m)=\lambda(m')+\lambda(\delta),
\]
because the difference from \(W(\delta)\) is \(a[\lambda(m)-\lambda(m')-\lambda(\delta)]\), and subadditivity makes the bracket nonpositive.

If \(\lambda(m'+\delta)=\lambda(m')+\lambda(\delta)\), write a minimum-length coin decomposition of \(\delta\) as \(\delta=c_1+\cdots+c_s\). Subadditivity forces \(\lambda(m'+c_1)=\lambda(m')+1\), since otherwise the total length would be smaller. Conversely, if a coin \(c\in\{1,3,7\}\) satisfies \(m'+c<a\) and \(\lambda(m'+c)=\lambda(m')+1\), then \(W(m'+c)-W(m')=(a-1)c+a\) is a positive generator of \(S_a\). It follows that **the maximal Apéry elements are precisely** the \(W(m)\) for which no such coin step exists.

**3. Seven-residue classification.** Since \(\lambda(m+7)=\lambda(m)+1\), every \(m<a-7\) admits a positive seven-coin step and is not maximal. Only \(a-7\le m\le a-1\) remain. For \(m\bmod7=0,1,2,3,4,5,6\), the differences \(\lambda(m+1)-\lambda(m)\) are
\[
(1,1,-1,1,1,-1,-1)
\]
and the differences \(\lambda(m+3)-\lambda(m)\) are
\[
(1,1,1,1,-1,-1,1).
\]
Checking whether either increment is one while the step stays below \(a\) yields exactly the offset sets \(J_0,\ldots,J_6\) in the table. A maximal Apéry member \(W(m)\) corresponds to the pseudo-Frobenius number \(W(m)-a\), completing the classification.

**4. Consequences.** The type values are the cardinalities of the offset sets. The type-one criterion gives symmetry exactly for \(a\equiv6\pmod7\). The Frobenius number is the greatest pseudo-Frobenius number. Applying the same explicit increment pattern to each table row shows that its maximal offset is \(j=1\) in residue class zero, \(j=2\) in residue class one, and \(j=0\) otherwise. Finally, \(a\), \(2a-1\), \(4a-3\), \(8a-7\) are all minimal generators when \(a\ge8\): they correspond to the unique minimum-one-coin presentations at coin values \(1,3,7<a\), and no smaller coin values can represent any of these three values using fewer than two coins; multiples of \(a\) cannot lower a residue minimum.

## Verification
The standard-library Python program `verify.py` tests the coin-cost formula with a separate dynamic program for all \(m\le10000\). For each \(8\le a\le1500\), an independent Dijkstra shortest-path algorithm reconstructs all \(a\) Apéry values and computes their maximal elements under generator addition, matching every formula. For each \(8\le a\le110\), a direct, bounded semigroup membership dynamic program independently determines every pseudo-Frobenius number and all gaps through the conductor and verifies the predicted genus. The script exits nonzero if any comparison fails. It is corroboration; the proof above establishes the infinite claim.

Examples: \(\operatorname{PF}(S_8)=\{49,50,51\}\), \(\operatorname{PF}(S_{13})=\{183\}\), and \(\operatorname{PF}(S_{16})=\{227,228,257\}\).

## Relationship to prior work
Liu, Xin, Ye and Yin's 2023 preprint, subsequently expanded as *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups* (2025), introduces a general collection containing \(S_a\) as its base-two, three-step, negative-shift specialization. Its general Apéry minimization supplies the conceptual starting point. The inspected paper gives Frobenius and genus machinery and pseudo-Frobenius formulas for certain **positive-shift** families, but does not state the seven-residue pseudo-Frobenius classification for arbitrary negative-shift \(a\ge8\). In particular its displayed four-generator example assumes positive shift; its monotonic maximum argument requires conditions not satisfied in the negative-shift case.

Branco, Colaço and Ojeda's earlier generalized repunit family has leading generator fixed to a repunit of specified length and includes exact pseudo-Frobenius spectra. The four-generator semigroup \(S_{15}\) is a particular instance of their length-four family, so that specific parameter is already covered. Their length-five family at leading generator \(31\) has **five** generators, not the four defining \(S_{31}\), and does not determine the latter's different spectrum. Their theorem therefore does not cover the all-parameter statement here. General Apéry-maximality and pseudo-Frobenius algorithms are standard and are used, not claimed as new.

## Limitations
The theorem is restricted to the specified four-generator family; it makes no statement for arbitrary shifts, bases, or numbers of generators. The classification is supported by the displayed proof and exact computational corroboration, but has not undergone independent scientific audit. No exhaustive guarantee of worldwide originality is claimed; unindexed equivalent results remain possible. The explicit formulas are infinite theorems only because of the symbolic coin and Apéry argument, not because of the finite experiments.

## References
1. F. Liu, G. Xin, S. Ye, J. Yin, *A Generalization of Mersenne and Thabit Numerical Semigroups*, arXiv:2306.03459v1, 6 June 2023; expanded as *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459v4 (2025), https://arxiv.org/html/2306.03459v4 .
2. M. B. Branco, I. Colaço, I. Ojeda, *The Frobenius Problem for Generalized Repunit Numerical Semigroups*, arXiv:2112.01106 (2021), Mediterranean Journal of Mathematics 20 (2023), article 16, https://link.springer.com/article/10.1007/s00009-022-02233-w .
3. M. Delgado, P. A. García-Sánchez, A. M. Robles-Pérez, *Numerical semigroups with a given set of pseudo-Frobenius numbers*, LMS Journal of Computation and Mathematics 19 (2016), 186–205, https://arxiv.org/abs/1505.08111 .
