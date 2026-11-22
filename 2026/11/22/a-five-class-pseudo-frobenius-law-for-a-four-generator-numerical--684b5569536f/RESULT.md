# A five-class pseudo-Frobenius law for a four-generator numerical-semigroup family

## Finding

For every integer \(m\ge6\), consider the numerical semigroup
\[
S_m=\langle m,\ m+1,\ 2m+3,\ 3m+5\rangle.
\]
Define \(h(i)=\lceil3i/5\rceil\) for nonnegative integers \(i\), and \(w_i=mh(i)+i\). Its complete Apéry set, Frobenius number and genus are
\[
\operatorname{Ap}(S_m,m)=\{w_i:0\le i<m\},\qquad
F(S_m)=m\Big\lceil\frac{3(m-1)}5\Big\rceil-1,\qquad
g(S_m)=\sum_{i=1}^{m-1}\Big\lceil\frac{3i}{5}\Big\rceil.
\]
Set
\[
\begin{aligned}
I_m={}&\{m-1\}\\
&\cup\{i\in\{m-3,m-2\}:i\bmod5\in\{2,4\}\}\\
&\cup\{i\in\{m-5,m-4\}:i\bmod5=2\}.
\end{aligned}
\]
The **complete pseudo-Frobenius set** is
\[
\boxed{\operatorname{PF}(S_m)=\{mh(i)+i-m:i\in I_m\}.}
\]
The number of pseudo-Frobenius elements (the type), indexed by \(m\bmod5=0,1,2,3,4\), is respectively \((2,3,3,1,2)\). Consequently \(S_m\) is symmetric exactly when \(m\equiv3\pmod5\). For an explicit genus quasipolynomial, write \(m=5q+r\), \(0\le r<5\), and put \((c_0,c_1,c_2,c_3,c_4)=(0,0,1,3,5)\). Then
\[
g(S_m)=\frac{15q(q-1)}2+8q+3qr+c_r.
\]
For example, \(S_8=\langle8,9,19,29\rangle\) has \(\operatorname{PF}(S_8)=\{39\}\), Frobenius number \(39\), and genus \(20\).

## Assumptions and scope

All semigroups contain zero, all coefficients in their generating expressions are nonnegative integers, and \(m\) is an arbitrary integer at least six (no primality or parity assumption). The Apéry set relative to \(m\) consists of the least semigroup element in each residue class modulo \(m\). A pseudo-Frobenius element is a nonmember integer \(z\) for which \(z+s\in S_m\) for all nonzero \(s\in S_m\). This is a complete classification of this four-generator family; it does not classify larger generated semigroups obtained by adding the remaining odd-step generators.

## Proof

**1. Exact weighted coin cost.** A representation with the three nonbase generators has the form
\[
(m+1)a+(2m+3)b+(3m+5)c=m(a+2b+3c)+(a+3b+5c).
\]
For any nonnegative integer \(t\), let \(H(t)\) be the least value of \(a+2b+3c\) over nonnegative solutions of \(a+3b+5c=t\). Every coin satisfies \(5\times\text{cost}\ge3\times\text{size}\), so \(H(t)\ge\lceil3t/5\rceil\). Write \(t=5q+r\), \(0\le r\le4\). Use \(q\) coins of size five plus, respectively, no coin, one size-one coin, two size-one coins, one size-three coin, or one size-three and one size-one coin. Their costs for the residual sizes are \(0,1,2,2,3\), exactly \(\lceil3r/5\rceil\); hence \(H(t)=h(t)\) for every \(t\ge0\).

**2. Apéry and classical invariants.** A number in the semigroup congruent to \(i\pmod m\) has a representation with \(t=i+qm\), \(q\ge0\), and value at least \(mH(t)+t\). As \(H(t)\) is nondecreasing, this is minimized at \(q=0\); the coin construction above attains \(w_i=mh(i)+i\). Adding copies of \(m\) cannot lower it. Thus the claimed Apéry set is exact, and \(w_i\) strictly increases with \(i\). The maximal Apéry element \(w_{m-1}\) gives \(F=w_{m-1}-m=mh(m-1)-1\). The Apéry genus formula gives \(g=\sum_{i=1}^{m-1}h(i)\). Summing the five terms of each complete block, then the final partial block, yields the displayed closed genus formula. Finally the generators are minimal: for residues \(1,3,5\), the displayed respective Apéry elements are \(m+1,2m+3,3m+5\), and none is a sum of smaller positive generators; \(m\) is the multiplicity.

**3. All maximal Apéry elements.** A nonzero Apéry element \(w_i\) is maximal in the semigroup order precisely when \(w_i+g\) is not an Apéry element for any minimal generator \(g\ne m\); equivalently, \(w_i+g>w_{(i+g)\bmod m}\) for \(g\in\{m+1,2m+3,3m+5\}\). For a generator \(cm+t\), with \((t,c)=(1,1),(3,2),(5,3)\), if \(i+t<m\) the strict inequality becomes \(h(i+t)<h(i)+c\). If \(i+t\ge m\), it is automatic because \(i+t-m\le i\) and \(h\) is nondecreasing. For \(t=5\), \(h(i+5)=h(i)+3\), so strict inequality forces \(i\ge m-5\). For \(t=3\), among the nonwrapped indices the strict inequality holds exactly when \(i\equiv2\pmod5\). For \(t=1\), among the nonwrapped indices it holds exactly when \(i\equiv2,4\pmod5\). Intersecting all three conditions gives exactly \(I_m\). Since the pseudo-Frobenius numbers are the maximal Apéry elements minus \(m\), their complete set is as claimed.

**4. Type and symmetry.** Reducing the four possible indices within five of \(m\) modulo five yields \(|I_m|=(2,3,3,1,2)\) for residues \(m\bmod5=0,1,2,3,4\). The standard characterization of symmetric numerical semigroups by type one yields the final equivalence. Alternatively, in the unique type-one congruence class \(m\equiv3\pmod5\), one verifies \(2g=F+1\) using the displayed genus formula; this is the classical symmetry criterion.

## Verification

The included stand-alone `verify.py` computes each Apéry set independently by Dijkstra's shortest-path algorithm on residues modulo \(m\), then compares it to the formula for every \(6\le m\le1000\). It also checks the genus quasipolynomial, the candidate pseudo-Frobenius indices and the type. For every \(6\le m\le160\), it independently enumerates all integers through the Frobenius number and tests the pseudo-Frobenius definition against all four generators, as well as the full gap count. All checks passed. These finite checks are supplementary; the proof above establishes the infinite parameter range.

## Relationship to prior work

Liu, Xin, Ye and Yin (2023) study weighted-coin models for generalized Mersenne/Thabit numerical semigroups and give a general optimization method for Apéry elements. Their detailed geometric generator pattern is different, and their general minimization principle does not state this explicit four-generator pseudo-Frobenius spectrum or five-class symmetry law. Robles-Pérez and Rosales (2023 preprint; 2024 publication) develop the general theory and construction of numerical semigroups with monotone Apéry sets, including generic symmetry tests, but do not provide the present parameter-uniform pseudo-Frobenius classification. The Apéry set here is indeed strictly monotone, so the family falls in that context. Moreno-Frías and Rosales (2026) describe the full smallest odd-right-end numerical semigroup generated by even \(m\); its first four minimal generators agree with the present generators. Their formulas concern the *full* semigroup, generally with more than four generators, and do not give the current truncated-family spectrum. At \(m=6\) the full semigroup coincides and its previously known Frobenius/genus values are not new. No claim of a complete priority search or independent validation is made.

## Limitations

The classification is specific to the four displayed generators, including odd parameters for which the odd-right-end motivation is only a combinatorial analogy. Although standard theory and the cited work provide general computational methods, they do not in themselves imply a previously published closed five-class formula. Unindexed equivalent parametrizations or an overlooked specialization of general Frobenius formulas remain possible. The exact number of representations of individual large semigroup elements and all higher-generator truncations are not treated.

## References

1. F. Liu, G. Xin, S. Ye, and J. Yin, *A Generalization of Mersenne and Thabit Numerical Semigroups*, arXiv:2306.03459 (first publicly posted 6 June 2023), https://arxiv.org/abs/2306.03459.
2. A. M. Robles-Pérez and J. C. Rosales, *Numerical Semigroups with Monotone Apéry Set and Fixed Multiplicity and Ratio*, arXiv:2310.09287 (first posted 13 October 2023); *Bulletin of the Brazilian Mathematical Society* 55, article 13 (2024), https://doi.org/10.1007/s00574-024-00387-7.
3. M. Á. Moreno-Frías and J. C. Rosales, *Odd Right-End Numerical Semigroups*, *Axioms* 15(3), 189 (2026), https://doi.org/10.3390/axioms15030189.
