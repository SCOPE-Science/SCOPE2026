# Exact dyadic residue fibers of the Tribonacci sequence

## Finding
Let \(T_0=0\), \(T_1=T_2=1\), and \(T_{n+3}=T_{n+2}+T_{n+1}+T_n\). For each integer \(k\ge4\) and \(y\in\mathbb Z/2^k\mathbb Z\), let
\[
N_k(y)=\#\{0\le n<2^{k+1}:T_n\equiv y\pmod{2^k}\}.
\]
There are exact 2-adic constants \(\kappa_5,\kappa_7\in\mathbb Z_2\), defined below, for which the complete target-by-target formula is
\[
\boxed{N_k(y)=2\mathbf 1_{y\equiv0,1\pmod4}+4\mathbf 1_{y\equiv1,2\pmod{16}}
+2\sum_{r\in\{5,7\}}\mathbf 1_{y\equiv b_r\pmod8}\,R_{k-3}((y-b_r)/8),}
\]
where \(b_5=8\kappa_5-1\), \(b_7=8\kappa_7\), and \(R_m(z)=\#\{x\bmod2^m:x^2\equiv z\pmod{2^m}\}\). Each summand is evaluated only when its congruence indicator is one; then the argument \((y-b_r)/8\) is well-defined modulo \(2^{k-3}\). Numerically, \(\kappa_5\equiv1264\pmod{2048}\) and \(\kappa_7\equiv1791\pmod{2048}\). The constants are precisely specified for arbitrary required precision by the unique critical points below.

The square-root factor is completely explicit. Write \(z\bmod2^m\). If \(z=0\), then \(R_m(z)=2^{\lfloor m/2\rfloor}\). If \(v=\nu_2(z)<m\) is odd, then \(R_m(z)=0\). If \(v=2h<m\), put \(s=m-2h\) and \(u=z/2^{2h}\), which is odd. Then \(R_m(z)=2^h\) when \(s=1\); it equals \(2^{h+1}\) when \(s=2\) and \(u\equiv1\pmod4\); it equals \(2^{h+2}\) when \(s\ge3\) and \(u\equiv1\pmod8\); in the other cases it vanishes. Thus the formula has no implicit root search. In particular every fiber count is even, but the counts are nonuniform and can grow exponentially in \(k\).

## Assumptions and scope
Indices are nonnegative and counted exactly once in the least period \(2^{k+1}\) of the standard Tribonacci sequence modulo \(2^k\). The 2-adic ring \(\mathbb Z_2\) denotes the inverse limit of the binary residue rings. Binomial interpolation in a 2-adic index is used only to describe the two critical residue branches; its values at nonnegative indices equal the original recurrence. The theorem does not assert uniqueness among all possible 2-adic interpolations without a fixed index residue class.

Set
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix},\quad v=(0,1,1)^\mathsf T,\quad e=(1,0,0).
\]
For \(r\in\{5,7\}\), the functions
\[
H_5(t)=(eM^{8t+5}v+1)/8,\qquad H_7(t)=eM^{8t+7}v/8
\]
are first defined for nonnegative integer \(t\), then interpolated through powers of \(M^8\) to all \(t\in\mathbb Z_2\). Each \(H_r\) has a unique critical point \(\alpha_r\in\mathbb Z_2\) satisfying \(H_r'(\alpha_r)=0\). Define \(\kappa_r=H_r(\alpha_r)\).

## Proof
**1. Matrix congruences and the nonsingular branches.** Direct multiplication yields
\[
M^8=I+4D,\qquad D=\begin{pmatrix}3&5&6\\6&9&11\\11&17&20\end{pmatrix}.
\]
For every \(s\ge3\) put \(D_s=(M^{2^s}-I)/2^{s-1}\). Squaring gives \(D_{s+1}=D_s+2^{s-2}D_s^2\), hence \(D_s\equiv D_3\pmod2\) for \(s\ge3\) and \(D_s\equiv D_4\pmod4\) for \(s\ge4\). The latter matrix is
\[
D_4\equiv\begin{pmatrix}1&1&0\\0&1&1\\1&1&2\end{pmatrix}\pmod4.
\]
A direct evaluation of \(eM^nD_3v\pmod2\) for \(n\bmod8\) gives an odd result for \(n\equiv0,2,4,6\pmod8\). Also \(eM^nD_4v\equiv2\pmod4\) for \(n\equiv1,3\pmod8\). For each odd \(a\) and \(s\ge3\), factor \(M^{2^sa}-I\) using \(M^{2^s}\) to preserve the first nonzero digit of the difference. Therefore
\[
\nu_2(T_{n+2^sa}-T_n)=s-1\quad\text{if }n\text{ is even},\qquad
\nu_2(T_{n+2^sa}-T_n)=s\quad\text{if }n\equiv1,3\pmod8,\ s\ge4.
\]
For \(r=0,2,4,6\), the functions \(t\mapsto (T_{8t+r}-T_r)/4\) are consequently 2-adic isometries onto \(\mathbb Z_2\). Modulo four the branches \(r=0,4\) equal zero and \(r=2,6\) equal one. Each of these two target classes therefore has exactly two preimages contributed by the even indices.

For \(r=1,3\), separate \(t=2w+a\), \(a\in\{0,1\}\). The preceding second valuation law gives
\[
\nu_2(T_{16w+r+8a}-T_{16w'+r+8a})=4+\nu_2(w-w')\quad(w\ne w').
\]
Since \(T_1\equiv T_9\equiv1\pmod{16}\) and \(T_3\equiv T_{11}\equiv2\pmod{16}\), each of the four parity subbranches is an isometry onto its indicated residue ball of radius \(16\). The \(r=1\) branch contributes four preimages to every target \(1\pmod{16}\); the \(r=3\) branch contributes four to every target \(2\pmod{16}\).

**2. Both singular branches are quadratic squares in 2-adic coordinates.** For \(r=5,7\), use the uniformly convergent series \((M^8)^t=\sum_{j\ge0}\binom tj(M^8-I)^j\) on \(\mathbb Z_2\). The binomial coefficients \(c_{r,j}\) of \(H_r\) begin
\[
(c_{5,0},c_{5,1},c_{5,2})=(1,115,14946),\qquad
(c_{7,0},c_{7,1},c_{7,2})=(3,389,50562).
\]
For the next two coefficients their valuations are \((\nu_2(c_{5,3}),\nu_2(c_{5,4}))=(4,7)\) and \((\nu_2(c_{7,3}),\nu_2(c_{7,4}))=(7,7)\). For \(j\ge5\), the divisibility of \(M^8-I\) by four gives \(\nu_2(c_{r,j})\ge2j-3\). Since \(\nu_2(j!)\le j-1\), the conversion of the binomial basis into the ordinary power basis proves
\[
H_5(t)=7473t^2-7358t+1+8E_5(t),\qquad
H_7(t)=25281t^2-24892t+3+8E_7(t),
\]
where \(E_5,E_7\in\mathbb Z_2\langle t\rangle\) are restricted integral power series. Differentiating and dividing by two yields equations
\[
H'_5(t)/2=7473t-3679+4E'_5(t),\qquad
H'_7(t)/2=25281t-12446+4E'_7(t).
\]
Because the leading coefficients are odd and the remainders are four times integral Lipschitz functions, each equation has one and only one root \(\alpha_r\in\mathbb Z_2\) by the 2-adic contraction theorem.

Taylor expansion at that root yields
\[
H_r(t)-\kappa_r=(t-\alpha_r)^2\bigl(a_r+8Q_r(t)\bigr),
\]
where \(a_5=7473\), \(a_7=25281\), and \(Q_r\in\mathbb Z_2\langle t\rangle\). Each \(a_r\equiv1\pmod8\). Accordingly the unit in parentheses has a unique square root \(B_r(t)\equiv1\pmod4\), and \(\nu_2(B_r(t)-B_r(w))\ge2+\nu_2(t-w)\). The map
\[
\phi_r(t)=(t-\alpha_r)B_r(t)
\]
is a 2-adic isometry of \(\mathbb Z_2\) onto itself (the first term in its difference is a unit times \(t-w\), whereas the error is divisible by \(4(t-w)\)). Hence \(H_r(t)=\kappa_r+\phi_r(t)^2\) exactly, and the level-\(m\) fiber cardinalities of \(H_r\) are precisely \(R_m\).

**3. Period, branch weights, and arithmetic formula.** The classical state period of this recurrence modulo \(2^k\) is \(2^{k+1}\), also obtained directly by \(\det[v,Mv,M^2v]=-1\) and the matrix lifting above. In a full period there are \(2^{k-2}\) indices in each fixed class modulo eight. For the square branches, reduction of \(H_r\) modulo \(2^{k-3}\) loses one bit of the parameter \(t\), so each solution in the square map produces exactly two indices in a full period. The four even isometric branches contribute the first indicator term, and the two parity subdivisions of each \(r=1,3\) branch contribute the second. Adding all eight disjoint index classes proves the boxed formula. The elementary classification of square roots modulo \(2^m\) follows by separating the valuation of the root and the standard odd-square congruences modulo \(2\), \(4\), and \(8\).

## Verification
The supplied standalone `verify_tribonacci_fibers.py` uses exact integer matrix arithmetic for \(M^8\), \(D_4\), and the first five binomial coefficients, then independently calculates both 2-adic critical values to each required precision and compares the formula against complete recurrence histograms for every \(4\le k\le14\). It checks all \(32,752\) target residues in these eleven levels, with no discrepancies. Its finite calculations do not substitute for the infinite lifting and analytic isometry arguments above. Execute with `python3 verify_tribonacci_fibers.py`.

## Relationship to prior work
The earlier public theorem *The complete dyadic value image and seven-twelfths density of Tribonacci numbers* proves the four-component value-image classification and least period, including the \(r=5\) quadratic conjugacy. Its explicit limitations state that individual target multiplicities are **not** given. Those results and the \(r=5\) conjugacy are credited here, not claimed new. The added \(r=7\) square conjugacy, the two odd nonsingular branch counts, and their simultaneous exact contribution produce the all-target fiber law; image coverage alone does not imply any of these multiplicities. Bilu–Luca–Nieuwveld–Ouaknine–Worrell study prime-adic zeros and valuations; Marques–Lengyel determine binary valuations at target zero; Klaška studies primitive periods for Tribonacci recurrences. None of their identified statements implies the target-by-target law for arbitrary residue values.

## Limitations
Only the classical Tribonacci initial conditions and powers of two are treated. No analogous formula for every arbitrary Tribonacci initial triple or odd-prime powers is claimed. No independent external mathematical audit was performed. A complete historical priority search is impossible; a differently phrased or unindexed full-fiber theorem remains a residual risk. The source describing the primitive periods was accessible through its article record but its full 2008 text could not be retrieved during this comparison, although its stated scope concerns periods rather than fiber multiplicities.

## References
1. Y. Bilu, F. Luca, J. Nieuwveld, J. Ouaknine and J. Worrell, *On the \(p\)-adic zeros of the Tribonacci sequence*, arXiv:2210.16959, posted 2022-10-30, https://arxiv.org/abs/2210.16959, full text https://arxiv.org/html/2210.16959v1.
2. D. Marques and T. Lengyel, *The 2-adic Order of the Tribonacci Numbers and the Equation \(T_n=m!\)*, Journal of Integer Sequences 17 (2014), https://cs.uwaterloo.ca/journals/JIS/VOL17/Lengyel/lengyel21.html.
3. J. Klaška, *Tribonacci modulo \(2^t\) and \(11^t\)*, Mathematica Bohemica 133 (2008), 377–387, https://doi.org/10.21136/MB.2008.140627.
4. *The complete dyadic value image and seven-twelfths density of Tribonacci numbers*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-dyadic-value-image-and-seven-twelfths-density-of-tr--a24da7d7968e.
