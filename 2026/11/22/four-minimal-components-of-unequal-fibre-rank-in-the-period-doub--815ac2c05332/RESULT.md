# Four minimal components of unequal fibre rank in the period-doubling six-step difference lift

## Finding
Let \(\vartheta(1)=10\), \(\vartheta(0)=11\) be the binary period-doubling substitution, and let \(Y\subset\{0,1\}^{\mathbb Z}\) be its two-sided primitive substitution subshift. Define
\[
X_6=\bigl\{x\in\{0,1\}^{\mathbb Z}:x_{j+6}+x_j\pmod2\in Y\text{ as a sequence in }j\bigr\}.
\]
The bilateral shift on \(X_6\) has **exactly four** disjoint clopen minimal components whose union is \(X_6\). Their respective fibre cardinalities under the six-step difference factor \(\eta_6:X_6\to Y\) are **\(8,8,24,24\)** at *every* base point. The total fibre cardinality is \(64\). In particular the natural first non-dyadic even six-step example has minimal components with unequal ranks, unlike the dyadic four- and eight-step examples.

## Assumptions and scope
All coordinates are indexed by \(\mathbb Z\). Addition of bits is modulo two. A minimal component is a nonempty closed shift-invariant subset with minimal bilateral shift action; its fibre rank is the number of points in a fibre of \(\eta_6\). Every base point \(y\) and initial six-bit prefix \(u=(x_0,\ldots,x_5)\) determine a unique bilateral \(x\), by solving \(x_{j+6}=x_j+y_j\) in both directions. Consequently all fibres have size \(2^6\). The claim is only for the stated binary substitution, offset six, and bilateral dynamics; no classification for arbitrary offsets or moduli is asserted.

## Proof
**1. A canonical four-phase skeleton.** Write \(\tau_n=\vartheta^n(1)\), \(\theta_n=\vartheta^n(0)\), and let \(t\) be the one-sided fixed point beginning in \(1\). From \(\vartheta(z)_{2m}=1\) and \(\vartheta(z)_{2m+1}=1-z_m\) we have \(t_{2m}=1\), \(t_{4m+1}=0\), and \(t_{4m+3}=t_m\). Moreover \(\vartheta^2(1)=1011\), \(\vartheta^2(0)=1010\), so every \(y\in\vartheta^2(Y)\) has ones at all even indices, zeros at every index congruent to one modulo four, and a varying symbol at indices congruent to three modulo four. Since \(Y=\bigcup_{s=0}^3\sigma^s\vartheta^2(Y)\), each \(y\in Y\) has some residue \(q(y)\pmod4\) with zeros at every index congruent to \(q(y)\), and ones at every index of the opposite parity. The residue is unique: two residues of different parity would make a symbol simultaneously forced to be zero and one, and two residues of the same parity would force an alternating period-two point. Both are excluded from the aperiodic minimal subshift (\(11\) and \(0\) occur in its language). Therefore the four phases are disjoint compact sets and hence clopen; \(q:Y\to\mathbb Z/4\mathbb Z\) is continuous, and \(q(\sigma y)=q(y)-1\pmod4\).

Normalize each \(x\in X_6\) by shifting it \(s(y)\) steps, where \(y=\eta_6(x)\) and \(s(y)\in\{0,1,2,3\}\) is the representative of \(q(y)-1\pmod4\). The normalized base has its zeros at residue one, and the normalized lift has an even prefix triple \(e=(x'_{0},x'_{2},x'_{4})\in\mathbb F_2^3\), where \(x'=\sigma^{s(y)}x\). Since every even base bit then equals one, shifting the normalized lift by four changes its even triple by
\[
R(e_0,e_1,e_2)=(e_2,e_0+1,e_1+1).
\]
A shift of the original lift changes the normalized lift by zero steps if \(s(y)>0\), and by four steps if \(s(y)=0\); hence the \(R\)-orbit of \(e\) is a continuous shift-invariant label. Directly, \(R^3=\mathrm{id}\), and \(R\) has exactly two singleton orbits (the triples \((0,1,0)\) and \((1,0,1)\)) and two three-element orbits on \(\mathbb F_2^3\). The four corresponding subsets \(X_{\mathcal O}\subset X_6\) are disjoint nonempty clopen invariant subsets covering \(X_6\). At each fixed \(y\), the normalized three odd prefix bits are arbitrary, so the fibre size of \(X_{\mathcal O}\) is \(8|\mathcal O|\): respectively \(8,8,24,24\).

**2. Two exact infinite families of return permutations.** For each \(n\ge0\), let \(T_n(j)\) and \(H_n(j)\), \(0\le j<6\), be the parity counts of symbols one in \(\tau_n\) and \(\theta_n\), respectively, at positions congruent to \(j\pmod6\). Let \(a_n=2^n\bmod6\). Concatenation identities \(\tau_{n+1}=\tau_n\theta_n\) and \(\theta_{n+1}=\tau_n\tau_n\) give the exact six-coordinate recurrence
\[
T_{n+1}(j)=T_n(j)+H_n(j-a_n),\qquad H_{n+1}(j)=T_n(j)+T_n(j-a_n)\pmod2.
\]
Subscripts are read modulo six. The initial parity vectors are \(T_0=(1,0,0,0,0,0)\) and \(H_0=0\). Straight substitution yields, with coordinates in order \(0,\ldots,5\),
\[
(a_2,T_2,H_2)=(4,101100,101000),\quad
(a_4,T_4,H_4)=(4,101001,101101),\quad
(a_6,T_6,H_6)=(4,101100,101000).
\]
Since \(a_{n+2}=a_n\) for \(n\ge1\), the recurrence and equality at \(n=2,6\) prove \((a_{n+4},T_{n+4},H_{n+4})=(a_n,T_n,H_n)\) for **all** \(n\ge2\), not just for sampled levels.

Given a six-bit prefix \(u\) above the base fixed word \(t\), the first six symbols of its shifted lift at time \(2^n\) equal
\[
\Phi_n(u)_j=u_{(2^n+j)\bmod6}+T_n((2^n+j)\bmod6),\qquad 0\le j<6.
\]
For \(n\equiv2\pmod4\), \(n\ge2\), this is one permutation \(P\) of \(\mathbb F_2^6\); for \(n\equiv0\pmod4\), \(n\ge4\), it is another permutation \(Q\). Write \(e=(u_0,u_2,u_4)\) and \(o=(u_1,u_3,u_5)\). The exact maps are
\[
P(e,o)=\bigl(R(e),(o_2,o_0,o_1+1)\bigr),\qquad
Q(e,o)=\bigl(R(e),(o_2+1,o_0,o_1)\bigr).
\]
Their quotient \(PQ^{-1}\) is an odd-coordinate translation by \((1,0,1)\); its conjugates under the cyclic linear part give all three even-weight translations in \(\mathbb F_2^3\). Further, \(P^3\) fixes \(e\) and translates \(o\) by \((1,1,1)\). These translations generate all of \(\mathbb F_2^3\). Therefore the group \(\langle P,Q\rangle\) has exactly four orbits on \(\mathbb F_2^6\), each the Cartesian product \(\mathcal O\times\mathbb F_2^3\), of sizes \(8,8,24,24\).

**3. Recurrence forces each invariant part to be minimal.** The one-sided fixed point obeys \(t_j=1-(\nu_2(j+1)\bmod2)\). There is a bilateral \(y_*\in Y\) with right tail \(t\), defined for \(j\ne-1\) by \((y_*)_j=1-(\nu_2(|j+1|)\bmod2)\) and \((y_*)_{-1}=1\): it arises as the coordinatewise limit of \(\sigma^{2^{2m}}y\) for any bilateral extension \(y\in Y\) of \(t\). For each fixed integer \(j\), the valuation formula gives \((y_*)_{2^n+j}\to(y_*)_j\) as even \(n\to\infty\); at \(j=-1\) the equality uses \(n\) even. Thus \(\sigma^{2^n}y_*\to y_*\) along both subsequences \(n\equiv2\pmod4\) and \(n\equiv0\pmod4\).

Let \(x_u\) be the unique bilateral lift of \(y_*\) with prefix \(u\), and let \(M_u=\overline{\{\sigma^j x_u:j\ge0\}}\). The displayed return formulas show \(x_{Pu},x_{Qu}\in M_u\); repeating from those points gives \(x_v\in M_u\) for **every** \(v\) in the \(\langle P,Q\rangle\)-orbit of \(u\). Since the base \(Y\) is minimal and the code is permutative in both endpoints, Hedlund's almost-periodicity theorem for permutative lifts (as stated in Kang and Jäger, Theorem 4.1) ensures every point of \(X_6\) is almost periodic. In particular \(M_u\) is minimal and all points of \(X_6\) belong to some minimal component.

Any minimal component inside \(X_{\mathcal O}\) maps onto \(Y\) and therefore meets the reference fibre over \(y_*\). By the previous paragraph it contains the **entire** reference-fibre subset \(\{x_v:v\in\mathcal O\times\mathbb F_2^3\}\). Hence two minimal components inside the same \(X_{\mathcal O}\) must intersect and are identical. As all points are almost periodic, each \(X_{\mathcal O}\) equals its unique minimal component. The four clopen sets constructed in Step 1 thus exhaust the minimal components, with the stated constant ranks. \(\square\)

## Verification
Run `python3 check_lag_six.py` using Python 3 without third-party packages. It checks the finite substitution recurrence independently against explicitly concatenated substitution words through level ten; verifies the recurrence's four-periodic state, computes all 64 prefixes and the four permutation orbits, checks those orbits against the normalized even-triple partition, and independently enumerates between 341 and 2730 direct substitution-word cylinder returns for each of four prefix lengths. The checker reports the fibre ranks \([8,8,24,24]\). The all-length and all-base statements depend on the mathematical recurrence, clopen phase construction, and almost-periodicity theorem, not on finite sampling.

## Relationship to prior work
Kang and Jäger (arXiv:2609.01140, first public 2026-09-01), Theorems 4.1 and 1.7, establish the general finite-minimal-component decomposition and nonminimality for larger odd-length period-doubling difference codes; these general assertions do not determine the exact component count or heterogeneous fibre ranks for the seven-symbol code. Their general return-permutation framework is acknowledged as prior methodology.

The published result *Exact component and fibre-rank law for the three-block period-doubling lift* (2026-10-11) treats offset two for arbitrary alphabet modulus; its binary case yields equal ranks. The published result *Exact minimal-component counts for dyadic period-doubling difference lifts* (2026-10-18) treats offsets four, eight, and higher powers of two; it gives uniform fibre rank two, explicitly leaving non-dyadic offsets untreated. Neither statement implies a rank distribution of \(8,8,24,24\) at offset six. The new assertion is a complete natural first non-dyadic even-offset classification, not a claim to invent the general skew-product machinery.

## Limitations
The result does not classify arbitrary offsets, alphabets, or other substitutions, nor does it describe the invariant-measure simplices or spectral invariants of the four components. Earlier unindexed work on odometer extensions could conceivably express the same particular rank decomposition in different terms; no exhaustive historical priority claim is made. The computational checks cannot alone establish an infinite dynamical classification. Independent mathematical validation has not been performed.

## References
1. Zeyu Kang and Tobias Jäger, *Permutative lifts of strictly ergodic subshifts*, arXiv:2609.01140v1 (2026-09-01), https://arxiv.org/abs/2609.01140v1 ; full-text sections 4.1, 4.3.3, and 4.4.
2. *Exact component and fibre-rank law for the three-block period-doubling lift* (2026-10-11), public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-component-and-fibre-rank-law-for-the-three-block-period-do--a7e0bd7bb899 .
3. *Exact minimal-component counts for dyadic period-doubling difference lifts* (2026-10-18), public mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-minimal-component-counts-for-dyadic-period-doubling-differ--1a88abe12d32 .
4. G. A. Hedlund, *Endomorphisms and automorphisms of the shift dynamical system*, Mathematical Systems Theory **3** (1969), 320–375, Theorem 12.4, as cited in reference 1.
