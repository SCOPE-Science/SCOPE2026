# Sharp displacement of maximal fibers in mixed dyadic odd-power value sets

## Finding
Fix two distinct odd integers \(3\le d<e\). For every integer \(k\ge0\), let
\[
A_k=\{x^d\bmod 2^k:x\in\mathbb Z/2^k\mathbb Z\},\quad
B_k=\{y^e\bmod2^k:y\in\mathbb Z/2^k\mathbb Z\},
\]
where **each distinct output value occurs once**. Put \(n=2^k\), and let
\[
R_k(t)=\#\{(a,b)\in A_k\times B_k:a+b\equiv t\pmod n\}.
\]
This theorem determines the entire mixed two-sum distribution. For \(k\ge1\), define
\[
D=\{jd: j\ge0,\ jd<k\},\quad H=\{je:j\ge0,\ je<k\},\quad
L(v)=2^{k-v-1}\quad(0\le v<k).
\]
For a nonzero target with \(v=v_2(t)<k\), its representation count is
\[
\boxed{R_k(t)=\sum_{s\in D\cap H,\ s<v}L(s)
+\mathbf1_{v\in D}\left(1+\sum_{s\in H,\ s>v}L(s)\right)
+\mathbf1_{v\in H}\left(1+\sum_{s\in D,\ s>v}L(s)\right).}
\]
At the zero target, \(R_k(0)=1+\sum_{s\in D\cap H}L(s)\). Set \(R_0(0)=1\). These explicit finite sums, depending only on the target valuation, also yield the exact mixed additive energy at every depth:
\[
\boxed{E_k=R_k(0)^2+\sum_{v=0}^{k-1}2^{k-v-1}R_k(2^v)^2.}
\]
No exponentially sized residue enumeration is needed to evaluate this identity.

The **sharp largest fiber** is, at every depth,
\[
\boxed{\max_{t\bmod2^k}R_k(t)=|B_k|.}
\]
For \(k>d\), every target with \(v_2(t)=d\) attains this maximum, although the two sets of power values generally are not nested. The zero target is a maximizer **if and only if** \(k\le e\) or \(d\mid e\). In particular, when \(d\nmid e\), the zero target **permanently ceases to be a maximizer at the sharp threshold \(k=e+1\)**, while the entire nonzero valuation-\(d\) shell remains maximizing. For \(k\ge3\), the minimum occurs **exactly at odd targets**, where
\[
R_k(t)=|A_k|+|B_k|-2^k.
\]
All targets are represented.

## Assumptions and scope
The exponents are arbitrary fixed distinct odd integers \(3\le d<e\), not necessarily primes or coprime. The moduli are all powers of two, with the singleton ring at \(k=0\). Both power images include zero; each residue value is counted once, not weighted by the number of roots. Mixed pairs are ordered by their two different factors, and \(E_k\) is \(\sum_t R_k(t)^2\). The valuation \(v_2(t)\) means the valuation of the unique representative in \(0,\ldots,2^k-1\) for nonzero residues. The energy is a mixed convolution collision invariant, not either individual set's self-energy.

## Proof
**1. Complete valuation-shell structure.** Because the unit group modulo a power of two is a 2-group, raising a unit to an odd power permutes all units. If the input has valuation \(j\), its \(d\)-th power has valuation exactly \(jd<k\), and its unit factor runs through all odd units at the relevant lower precision. Consequently
\[
A_k=\{0\}\mathbin{\dot\cup}\bigcup_{s\in D}V_s,
\quad B_k=\{0\}\mathbin{\dot\cup}\bigcup_{s\in H}V_s,
\quad V_s=\{z\bmod2^k:v_2(z)=s\},\quad |V_s|=L(s).
\]
These unions are disjoint and valid even when an exponent exceeds the modulus depth.

**2. Exact target-by-target fibers.** Suppose \(t\ne0\) has valuation \(v\). If two nonzero summands have the same valuation \(s\), their sum has valuation strictly greater than \(s\); hence such a representation has \(s<v\), with \(s\in D\cap H\). For every \(a\in V_s\), the complementary \(b=t-a\) also lies in \(V_s\), giving exactly \(L(s)\) pairs. If their valuations differ, the sum has valuation the lower one, necessarily \(v\). If the first summand has valuation \(v\in D\), one may choose the second freely from each higher shell \(V_s\), \(s\in H\), and the first is then forced and has valuation \(v\). The symmetric case contributes the last sum. A zero summand contributes one if \(v\in D\) or \(v\in H\), respectively. If \(t=0\), both nonzero summands must have equal valuation in \(D\cap H\), producing the displayed sum, while \((0,0)\) adds one. This exhaustive classification proves the complete formula. It includes every target, and the odd-target formula below is positive.

**3. Energy.** There are exactly \(2^{k-v-1}\) residues of valuation \(v\) and one zero residue. The fiber formula depends only on valuation, so summing its square over all targets yields the displayed depth-\(k\) energy expression. This is an exact \(O(k(d+e))\) arithmetic evaluation from the explicit finite valuation sums, for every depth.

**4. Sharp maximum and the displacement threshold.** For every target \(t\), choosing \(b\in B_k\) determines at most one \(a=t-b\in A_k\), so \(R_k(t)\le|B_k|\). When \(k\le d\), both power sets equal the union of all odds and zero, so \(t=0\) attains \(|B_k|\). When \(k>d\), choose any target \(t\) with valuation exactly \(d\). For each odd \(b\in B_k\), \(t-b\) is odd and therefore in \(A_k\). For each even \(b\in B_k\), the shell decomposition shows \(v_2(b)\ge e>d\) or \(b=0\), so \(v_2(t-b)=d\), again belonging to \(A_k\). Thus **every** \(b\in B_k\) has its complement in \(A_k\), proving equality throughout that shell.

Because both images are stable under negation, \(R_k(0)=|A_k\cap B_k|\). Hence zero is a maximizer precisely when \(B_k\subseteq A_k\). If \(k\le e\), \(B_k\) consists of odd values and zero, so inclusion holds. If \(k>e\), \(B_k\) contains the full nonzero shell of valuation \(e\); this shell lies in \(A_k\) exactly when \(d\mid e\). In the latter case every multiple-of-\(e\) valuation is also a multiple-of-\(d\) valuation, so inclusion of all shells follows. This proves the sharp threshold and all stated maximizing assertions without claiming that no other maximizing shells occur.

**5. Sharp minimum.** Write \(A_k=U_k\mathbin{\dot\cup}A_k^{\mathrm{even}}\) and similarly for \(B_k\), where \(|U_k|=n/2\). An odd target is obtained only from one odd and one even summand. For each even value in either set there is exactly one odd complementary value in the other set; therefore every odd target has \(|A_k^{\mathrm{even}}|+|B_k^{\mathrm{even}}|=|A_k|+|B_k|-n\) representations. Every even target receives at least \(n/2\) representations from odd-plus-odd values alone. For \(d,e\ge3\), the even part of either set has size at most \(1+\sum_{j\ge1}n/2^{3j+1}=1+n/14\). Therefore the odd-target count is at most \(2+n/7<n/2\) for \(n\ge8\), proving that odd targets are the unique minimizers for \(k\ge3\). Every target has a representation since the odd and even counts are positive (with low-depth cases checked directly from the same decomposition).

## Verification
Run `python3 verify_mixed_power_values.py` using only the Python standard library. For seven distinct exponent pairs \((d,e)\) and every \(0\le k\le10\), the program constructs each value set by independent modular exponentiation, enumerates every ordered mixed-value sum, and compares **every residue fiber** to the valuation formula. It checks the exact maximum, its explicit valuation-\(d\) witnesses, pair-count totals, and unique odd-target minimizers. The final marker is `MIXED_CHECK_OK 14637`. Finite enumeration corroborates but does not replace the all-depth arguments.

## Relationship to prior work
Broughan's 2004 modular result concerns support of sums of two cubes, not the weighted-by-values mixed two-exponent convolution. Arias, Borja and Anaya (2023) count representable output classes for diagonal power sums. Gu's 2026 general character-inversion identity and its subsequent index-one valuation polynomial evaluation cover **two summands chosen from the same power-value set** (and in the cited evaluation, unordered *distinct* summands). They therefore do not provide the cross-correlation between the two genuinely different exponent images, nor the displacement criterion for its maximum. Known dyadic odd-power representation laws count input roots of powers with the *same* exponent; their root-weighted counts do not imply these mixed unweighted values. The all-modulus zero-to-nonzero maximizing transition is the additional structural feature beyond a formal valuation sum. Historical priority beyond the inspected sources is not asserted.

## Limitations
The result does not address even exponents, mixed sums involving odd prime-power moduli, or counts of original input roots. The energy formula is a finite valuation sum rather than a single simplified rational expression in the depth. The theorem identifies a complete shell of maximizing targets but does not claim a complete list of all other possible maximizers. A broad general subset-sum or character-convolution identity might specialize to the same fibers; this remains a residual originality risk. Independent external mathematical audit has not been performed.

## References
1. K. A. Broughan, *Characterizing the Sum of Two Cubes*, Journal of Integer Sequences **6** (2003), Article 03.4.6, published January 14, 2004. https://cs.uwaterloo.ca/journals/JIS/VOL6/Broughan/broughan25.pdf
2. F. Arias, J. Borja and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), Article 23.8.1. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
3. *Exact pair counts and sharp additive coverage for power values in Galois rings* (2026), scientific record. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-pair-counts-and-sharp-additive-coverage-for-power-values-i--7a4111089730
4. *Dyadic representation-density moments for sums of two odd powers* (2026), scientific record. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-dyadic-representation-density-moments-for-sums-of-two-odd-powers--acd9600cfc42
