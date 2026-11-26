# Pseudo-Frobenius spectra of four-generator negative repunit semigroups

## Finding

For every integer \(a\ge8\), let
\[
S_a=\langle a,2a-1,4a-3,8a-7\rangle\subseteq\mathbb Z_{\ge0}.
\]
Define \(h=(0,1,2,1,2,3,2)\), \(\lambda(m)=\lfloor m/7\rfloor+h_{m\bmod7}\), and \(P_a(m)=(a-1)m+a\lambda(m)-a\). For \(r=a\bmod7\), the following table gives the pseudo-Frobenius offsets \(J_r\), the type, and the offset \(j_F\) that gives the Frobenius number.

| \(r\) | \(J_r\) | Type | \(j_F\) |
|---|---|---:|---:|
| 0 | \(\{0,1\}\) | 2 | 1 |
| 1 | \(\{0,1,2\}\) | 3 | 2 |
| 2 | \(\{0,2,3\}\) | 3 | 0 |
| 3 | \(\{0,4\}\) | 2 | 0 |
| 4 | \(\{0,1,5\}\) | 3 | 1 |
| 5 | \(\{0,2,6\}\) | 3 | 0 |
| 6 | \(\{0\}\) | 1 | 0 |

Then
\[
\operatorname{PF}(S_a)=\{P_a(a-1-j):j\in J_r\},\qquad
F(S_a)=P_a(a-1-j_F).
\]
In particular \(S_a\) is symmetric exactly when \(a\equiv6\pmod 7\), and it has embedding dimension four throughout the stated range. For example, at \(a=11\) the pseudo-Frobenius set is \(\{72,111,112\}\), and its maximum \(112=P_{11}(9)\) precedes the last index \(10\).

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of \(\mathbb Z_{\ge0}\). A pseudo-Frobenius number is an integer \(z\notin S\) such that \(z+s\in S\) for all \(s\in S\setminus\{0\}\). The type is the number of these integers. A numerical semigroup is symmetric exactly when its type is one. Here \(a\) ranges over all integers \(a\ge8\) and \(\gcd(a,2a-1)=1\), so the displayed semigroup is numerical.

## Proof

**Coin cost and Apéry representatives.** The least number of \(1,3\)-coins for an amount \(M\) is \(H(M)=\lfloor M/3\rfloor+(M\bmod3)\), by replacing triples of unit coins. The difference \(H(M+7)-H(M)\) is 3 for \(M\equiv0,1\pmod3\) and 1 for \(M\equiv2\pmod3\). Thus, in minimizing the number of \(1,3,7\)-coins, raising the number of seven-coins by one and reoptimizing the other coins never increases cost if feasible. It follows that the coin minimum is \(\lambda(m)\) as displayed above.

Write the value of any combination of the three non-\(a\) generators as \((a-1)M+aL\), where \(M\) is the sum of the corresponding \(1,3,7\)-coins and \(L\) is their number. The residue modulo \(a\) is \(-M\). For \(0\le m<a\), fixing \(M=m\) yields minimum \(W_a(m)=(a-1)m+a\lambda(m)\). A combination with \(M=m+qa\), \(q\ge1\), has value at least \((a-1)(m+a)+a\), strictly above the unit-coin value \((a-1)m+am\) by \(a(a-m)>0\). Adding copies of \(a\) cannot improve a residue minimum. Thus \(W_a(m)\) is the least semigroup element of residue \(-m\), and these \(a\) values form \(\operatorname{Ap}(S_a,a)\).

**Which Apéry representatives are maximal.** Use the order \(u\preceq_{S_a}v\) if \(v-u\in S_a\), and abbreviate \(W=W_a\). For \(m'<m\) we have \(W(m')-W(m)\le2\): the steps are \(2a-1\) at residues \(0,1,3,4\) of the earlier index and \(-1\) at residues \(2,5,6\); a run of negative steps has length at most two. Indeed, if the interval has \(k\ge1\) positive steps, the net increase is at least \(k(2a-1)-2(k+1)>0\). Therefore an earlier index cannot dominate a later one, since the smallest positive semigroup element is \(a\).

For \(m'<m\) put \(\delta=m-m'\in\{1,\dots,a-1\}\). The least representative of the residue of \(W(m)-W(m')\) is \(W(\delta)\), and their difference is \(a[\lambda(m)-\lambda(m')-\lambda(\delta)]\). The bracket is nonpositive by subadditivity. Thus the later index dominates the earlier exactly when \(\lambda(m)=\lambda(m')+\lambda(\delta)\). In that case the first coin \(c\in\{1,3,7\}\) of a minimum coin presentation of \(\delta\) must satisfy \(\lambda(m'+c)=\lambda(m')+1\); otherwise one could complete that presentation with fewer coins than equality allows. Conversely such a step, when \(m'+c<a\), gives \(W(m'+c)-W(m')=(a-1)c+a\in S_a\). This proves that \(W(m)\) is maximal exactly when none of the three steps stays below \(a\) and increases \(\lambda\) by one.

Since \(\lambda(m+7)=\lambda(m)+1\), only \(a-7\le m\le a-1\) can be maximal. On residues \(0,1,\ldots,6\) the unit-step differences in \(\lambda\) are \((1,1,-1,1,1,-1,-1)\), and the three-step differences are \((1,1,1,1,-1,-1,1)\). For \(m=a-1-j\), the unit step is feasible when \(j\ge1\) and thus in that range a survivor must have \(m\bmod7\in\{2,5,6\}\). For \(j\ge3\) the three-step is also feasible, leaving only \(m\equiv5\pmod7\). Applying these rules for \(0\le j\le6\) gives precisely the displayed \(J_r\). Subtracting \(a\) from the maximal members of the Apéry set yields the full pseudo-Frobenius set. The representatives have distinct residues, so the type is \(|J_r|\).

**Frobenius number and minimal generators.** Since \(W(m+7)-W(m)=8a-7>0\), the numerical maximum of \(W\) is in the last seven positions. Among those positions, each earlier index followed by at least one positive step on the way to \(a-1\) is strictly below \(W(a-1)\), by the step count above. An earlier index followed only by negative steps has value larger by the number of steps. Thus the maximizing offset is the number of consecutive negative steps ending at \(a-1\). The step starts are negative at residues \(2,5,6\). The number of trailing negative steps is 1 for \(a\equiv0,4\), 2 for \(a\equiv1\), and 0 otherwise, all modulo 7. This proves the \(j_F\) column, since \(F(S_a)=\max_m W(m)-a\).

Each non-\(a\) generator is \(W(c)\) for \(c=1,3,7<a\). A minimum representation of \(W(c)\) cannot contain \(a\), cannot have a larger offset in the same residue, and must use exactly one coin at offset \(c\); it is exactly the stated generator. The smallest positive element \(a\) is also minimal. This completes the proof.

## Verification

The accompanying standard-library `verify.py` checks the minimum coin counts up to 10000 by dynamic programming. It compares all predicted Apéry values and the complete pseudo-Frobenius set with residue-graph shortest paths for \(8\le a\le1500\), and compares the pseudo-Frobenius sets and gap counts with a separate membership computation for \(8\le a\le110\). That checker uses the maximum of the predicted set rather than evaluating the separate \(j_F\) shortcut; the shortcut is established by the exact trailing-step argument above. The finite checks do not prove the all-parameter classification.

## Relationship to prior work

Liu, Xin, Ye and Yin's Collection 1.1 includes this family at \(b=2,k=3,d=-1\). Their greedy Apéry formula (Theorem 2.10, eq. (8)) already specializes to \(W_a(m)\): its bound here is \(a\ge4\), and the minimum coin vector uses offsets \(1,3,7\). Their two monotonic maximum results (Theorem 2.12 and Corollary 2.16) cannot give the negative-shift shortcut: the strict denomination condition in the theorem fails at \(s_i=u+1=2\), and the corollary and four-generator Example 2.19 require positive shift. Their Section 3 treats pseudo-Frobenius numbers for a positive-shift repunit-multiple family. The new part here is the seven-residue classification of all maximal Apéry representatives in the stated negative-shift family, not the Apéry formula in isolation.

Branco, Colaço and Ojeda give exact pseudo-Frobenius spectra for a generalized repunit family with first generator fixed to a repunit of the specified length. Its length-four case includes \(S_{15}\), with spectrum \(\{211,212,213\}\), but does not furnish the seven-row classification for arbitrary \(a\).

## Limitations

The classification is for four generators at the specified base and shift. Other shifts, bases, or lengths are not covered. The literature comparisons do not establish exhaustive priority.

## References

1. F. Liu, G. Xin, S. Ye and J. Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459v4, https://arxiv.org/html/2306.03459v4.
2. M. B. Branco, I. Colaço and I. Ojeda, *The Frobenius Problem for Generalized Repunit Numerical Semigroups*, Mediterranean Journal of Mathematics 20 (2023), article 16, https://arxiv.org/abs/2112.01106.
3. M. Delgado, P. A. García-Sánchez and A. M. Robles-Pérez, *Numerical semigroups with a given set of pseudo-Frobenius numbers*, LMS Journal of Computation and Mathematics 19 (2016), 186–205, https://arxiv.org/abs/1505.08111.
