# Exact twelve-bit drift of the mod-five signed-digit representation imbalance

## Finding
For an integer \(r\ge1\), let \(b_r(n)\) count expressions
\[
n=\sum_{j=0}^{r-1}\varepsilon_j2^j,\qquad \varepsilon_j\in\{-1,0,1\},
\]
for each \(0\le n<2^r\). Define the prefix imbalance
\[
E_r(t)=\#\{0\le n<t:b_r(n)\equiv1\pmod5\}
-\#\{0\le n<t:b_r(n)\equiv4\pmod5\},
\quad 0\le t\le2^r,
\]
and its exact extremes \(B_r^+=\max_tE_r(t)\) and \(B_r^-=\min_tE_r(t)\).

**Theorem.** For every integer \(r\ge8\),
\[
\boxed{B_{r+12}^+=B_r^++4,\qquad B_{r+12}^-=B_r^--4.}
\]
The starting bound \(r=8\) is sharp: the first equality fails at \(r=7\). The following complete set of twelve initial pairs therefore determines all later extremes:

| \(r\) | \(B_r^-\) | \(B_r^+\) |
|---:|---:|---:|
| 8 | -4 | 4 |
| 9 | -5 | 3 |
| 10 | -4 | 5 |
| 11 | -3 | 6 |
| 12 | -5 | 5 |
| 13 | -6 | 4 |
| 14 | -5 | 7 |
| 15 | -4 | 8 |
| 16 | -6 | 7 |
| 17 | -7 | 6 |
| 18 | -6 | 8 |
| 19 | -5 | 9 |

In particular, \(B_r^+=r/3+O(1)\) and \(B_r^-=-r/3+O(1)\). Neither sign of the mod-five imbalance is uniformly bounded as the representation width grows.

An equivalent precise statement concerns Stern's diatomic sequence \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\), and \(s(2n+1)=s(n)+s(n+1)\). Define
\[
D(N)=\#\{0\le n<N:s(n)\equiv1\pmod5\}
-\#\{0\le n<N:s(n)\equiv4\pmod5\},
\]
and \(H_r=\max_{0\le N\le2^r}D(N)\), \(L_r=\min_{0\le N\le2^r}D(N)\). For every \(r\ge8\), simultaneously
\[
H_{r+12}=H_r+4,\qquad L_{r+12}=L_r-4.
\]

## Assumptions and scope
All representations have **exactly \(r\) digit positions**, with leading zero digits permitted. Their represented integer \(n\) is nonnegative and strictly below \(2^r\). Every residue is taken modulo the integer five. All extrema include the empty prefix \(t=0\) (or \(N=0\)) and the full prefix. The theorem makes no assertion about residues other than one and four, or any modulus other than five.

## Proof
**1. Reduction to Stern's sequence.** Monroe's signed-digit correspondence gives \(b_r(n)=s(2^r-n)\) for \(0<n<2^r\); at \(n=0\), both quantities equal one. Set \(w(a)=\mathbf1_{a\equiv1\ (5)}-\mathbf1_{a\equiv4\ (5)}\). Then \(D(N)=\sum_{n=0}^{N-1}w(s(n))\), and reversing the signed-digit order yields the exact identity
\[
E_r(t)=D(2^r+1)-D(2^r-t+1).
\]
Since \(s(2^r)=1\), we have \(D(2^r+1)=D(2^r)+1\).

**2. Exhaustive finite-state recurrences.** Consecutive Stern terms are coprime, so their residues yield the 24-element state set
\[
\mathcal S=\{(a,b)\in\mathbb F_5^2:(a,b)\ne(0,0)\}.
\]
Binary digit zero and one append by the maps
\[
\mathsf L(a,b)=(a,a+b),\qquad
\mathsf R(a,b)=(a+b,b),
\]
with all coordinates modulo five. Let \(W(a,b)=\mathbf1_{a=1}-\mathbf1_{a=4}\). For each \(x\in\mathcal S\) and \(r\ge0\), let \(S_r(x)\) be the sum of \(W\) over the \(2^r\) descendant states (all binary words of length \(r\), in increasing binary order); let \(U_r(x)\) and \(V_r(x)\) be the smallest and largest partial sums, including empty and full prefixes. At level zero,
\[
S_0(x)=W(x),\quad U_0(x)=\min(0,W(x)),\quad V_0(x)=\max(0,W(x)).
\]
Splitting the ordered descendants into zero-leading and one-leading halves gives three **exact** integer recurrences:
\[
\begin{aligned}
S_{r+1}(x)&=S_r(\mathsf Lx)+S_r(\mathsf Rx),\\
U_{r+1}(x)&=\min\big(U_r(\mathsf Lx),\ S_r(\mathsf Lx)+U_r(\mathsf Rx)\big),\\
V_{r+1}(x)&=\max\big(V_r(\mathsf Lx),\ S_r(\mathsf Lx)+V_r(\mathsf Rx)\big).
\end{aligned}
\]
These hold for **every** state, not merely for states appearing in a bounded sample. For \(x_0=(0,1)\) the binary digit state starts at \((s(0),s(1))\), and leading zeroes leave it fixed. Thus \(S_r(x_0)=D(2^r)\), \(U_r(x_0)=L_r\), and \(V_r(x_0)=H_r\).

**3. Exact finite certificate and its infinite consequence.** Apply the preceding recurrences to the complete list of 24 states, ordered lexicographically. The saved `CERTIFICATE.tsv` records the values of \(S_1,S_5,U_{16},U_{28},V_{16},V_{28}\) for **every** state. The complete 24-row exact-integer comparison establishes
\[
S_5=S_1,\qquad U_{28}=U_{16}-4\mathbf1,\qquad V_{28}=V_{16}+4\mathbf1,
\]
where these are vector equalities and \(\mathbf1\) is the constant 24-vector. The first equality, by linearity of the total-sum recurrence, implies \(S_{r+4}=S_r\) for all \(r\ge1\), and hence \(S_{r+12}=S_r\). Assuming \(U_{r+12}=U_r-4\mathbf1\) and \(V_{r+12}=V_r+4\mathbf1\), the displayed min/max recurrences and \(S_{r+12}=S_r\) imply the same equalities at \(r+1\). The certified starting level \(r=16\) proves both shifts for **every state and every \(r\ge16\)**.

The 24-state recurrence directly verifies the two root-state identities at each of the eight remaining indices \(8\le r<16\). Together these give \(L_{r+12}=L_r-4\) and \(H_{r+12}=H_r+4\) for all \(r\ge8\). The base values \(L_7=0\) and \(L_{19}=-5\) show that starting at seven would be false.

**4. Return to signed digits.** The total sums \(S_r(x_0)\) at positive \(r\) cycle as \(1,2,3,2\), so \(F_r:=D(2^r+1)=S_r(x_0)+1\) lies in \(\{2,3,4\}\) and has period four. For \(r\ge8\), \(L_r\le-1\) and \(H_r\ge7\). The extra endpoint \(D(2^r+1)=F_r\) lies strictly between the previous extremes; also \(D(0)=D(1)=0\). Therefore the reversal identity implies
\[
B_r^+=F_r-L_r,\qquad B_r^-=F_r-H_r \qquad(r\ge8).
\]
Since \(F_{r+12}=F_r\), the proven Stern shifts give the asserted exact signed-digit shifts. The twelve explicit initial pairs follow from the same 24-state recurrence and determine all later pairs. The difference \(B_{19}^+-B_7^+=5\ne4\) shows that the lower starting bound is sharp. Finally, iterating the exact twelve-step shifts gives the two asymptotic formulas.

## Verification
Run `python3 verify.py` in a directory containing the accompanying `CERTIFICATE.tsv`. The checker reconstructs all 24 states and maps from their definitions; verifies every certificate entry; independently evaluates the recurrences through level 52; checks total-sum period four and the precise 12-step shifts at all states; checks the sharp root starting index; and directly enumerates \(131072\) Stern values. It additionally counts actual signed-digit expansions by \(3^r\)-word enumeration for widths one through six and directly checks the signed-digit prefix extrema for widths eight through seventeen. Its observed output is:

`VERIFY_OK states=24 levels=53 total_period=4 from=1 root_shift_start=8 all_states_start=16 increment=4 direct_stern_terms=131072 direct_BSD_widths=8..17 enumeration_widths=1..6 certificate_rows=24`

Only the exact finite state identities, the displayed recurrences, and their induction prove the infinite theorem; the direct sequence and signed-digit experiments are independent sanity checks.

## Relationship to prior work
Monroe (first posted 10 March 2021, initial combined preprint `arXiv:2103.05810`, followed by the focused preprint `arXiv:2108.11495`) proved the correspondence between fixed-width signed-digit counts and Stern values. Her inspected article does not analyze this mod-five residue imbalance.

Reznick (`arXiv:math/0610601`, first posted 19 October 2006; published in 2008) proved boundedness of the **mod-three** difference between residues one and two (Theorem 5.6). At the end of that work he reported no result for the **mod-five** difference between residues one and four, apart from finite numerical bounds through \(2^{19}\). His uniform limiting frequencies for each residue do not bound this signed difference, and his exact dyadic zero-residue count is a different statistic. The present theorem finds that the mod-five difference is actually unbounded in both directions and gives its exact extremal growth rate and a twelve-step recursion. Neither the general modular frequency theorem nor the signed-digit correspondence alone implies this extremal law.

## Limitations
The complete finite certificate is exhaustive for the explicitly defined 24-state recurrences; it does not certify any alternate definitions or other moduli. Complete bibliographic priority is not asserted: an unindexed equivalent theorem or unavailable 2012 class notes on Stern's sequence could contain relevant comparisons. The result does not describe the full distribution of the imbalance at each width or provide a closed-form extremizing index for every width.

## References
1. Laura Monroe, *Binary Signed-Digit Integers, the Stern Diatomic Sequence and Stern Polynomials*, `arXiv:2103.05810`, first posted 2021-03-10; and *Binary Signed-Digit Integers and the Stern Diatomic Sequence*, `arXiv:2108.11495`, first posted 2021-08-25. https://arxiv.org/abs/2103.05810 ; https://arxiv.org/pdf/2108.11495
2. Bruce Reznick, *Regularity Properties of the Stern Enumeration of the Rationals*, `arXiv:math/0610601`, first posted 2006-10-19, *Journal of Integer Sequences* 11 (2008), Article 08.4.1. https://arxiv.org/pdf/math/0610601
3. OEIS Foundation, sequence A002487, Stern's diatomic series. https://oeis.org/A002487
