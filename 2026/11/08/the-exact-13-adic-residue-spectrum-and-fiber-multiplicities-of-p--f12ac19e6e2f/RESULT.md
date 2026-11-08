# The exact \(13\)-adic residue spectrum and fiber multiplicities of Pell numbers

## Finding
Write \(P_0=0\), \(P_1=1\) and \(P_{n+2}=2P_{n+1}+P_n\) for all integers \(n\ge0\). Let
\[
S=\{0,1,2,5,12,29,70,99,140,157,164,167,168\}\subset\mathbb Z/169\mathbb Z.
\]
For **every integer** \(k\ge2\), the complete scalar image is
\[
\{P_n\bmod13^k:n\ge0\}
 =\{a\bmod13^k:a\bmod169\in S\}.
\]
Thus precisely \(13^{k-1}\) values are represented. The **least** period is \(T_k=28\cdot13^{k-2}\). Over the index classes \(0\le n<T_k\), each represented residue congruent to \(0\pmod{169}\) has **four** preimages, and each of the other represented residues has **two**. All represented residues occur infinitely many times as the index varies over the nonnegative integers. Equivalently,
\[
\overline{\{P_n:n\ge0\}}=\bigsqcup_{s\in S}(s+169\mathbb Z_{13}),
\qquad \mu_{13}\bigl(\overline{\{P_n\}}\bigr)=\frac1{13}.
\]
For comparison, modulo \(13\), exactly the nine residues \(\{0,1,2,3,5,8,10,11,12\}\) occur; the exceptional loss of coverage takes place at the prime-square level.

A structural refinement controls **all** pairs of indices in one branch: for \(r\in\{0,\ldots,27\}\) and distinct nonnegative integers \(u,v\),
\[
\boxed{\nu_{13}(P_{r+28u}-P_{r+28v})=2+\nu_{13}(u-v).}
\]
Here \(\nu_{13}\) is the ordinary exponent of the prime \(13\) in a nonzero integer.

## Assumptions and scope
The sole prime considered is \(13\). All indices are nonnegative integers and all moduli are positive integer powers of \(13\). The cardinality and multiplicity claims refer to scalar Pell values, not to the pair-valued state sequence. By a period we mean a positive shift preserving **every** term of the scalar recurrence modulo the stated modulus. The normalized additive Haar measure on \(\mathbb Z_{13}\) assigns measure \(13^{-j}\) to one coset modulo \(13^j\).

The prime \(13\) is not an arbitrary numerical slice: it is the smallest known Pell–Wieferich prime and the first exceptional prime in the balancing/Pell period-lifting literature [1, 3]. At this prime the period fails to acquire a factor of \(13\) on passing from modulus \(13\) to modulus \(169\). The aim here is the finer **scalar image and all fiber counts**, not merely that period anomaly.

## Proof
**1. The period seed and its precise first nontrivial lift.** Set
\[
A=\begin{pmatrix}2&1\\1&0\end{pmatrix},
\qquad P_n=(A^n)_{12},\qquad \det A=-1.
\]
Direct multiplication modulo \(13\) gives
\[
A^4\equiv\begin{pmatrix}3&12\\12&5\end{pmatrix},\quad
A^7\equiv5I,\quad A^{14}\equiv-I,\quad A^{28}\equiv I\pmod{13}.
\]
Since every proper divisor of \(28\) divides either \(14\) or \(4\), whereas neither \(A^{14}\) nor \(A^4\) is the identity modulo \(13\), the order of \(A\bmod13\) is **exactly** \(28\).

A further exact modular multiplication yields
\[
U:=A^{28}\equiv
\begin{pmatrix}1015&1014\\1014&1184\end{pmatrix}\pmod{2197}.
\]
Consequently \(U=I+169B\) for an integral matrix \(B\), with
\[
B\equiv\begin{pmatrix}6&6\\6&7\end{pmatrix}\pmod{13}.
\]
In particular, the matrix state returns modulo \(169\) after exactly \(28\) steps.

**2. An exact branch-distance lemma.** Fix \(d\ge1\). The finite matrix binomial theorem gives
\[
\frac{U^d-I}{169d}
 =B+\sum_{j=2}^d \frac{169^{j-1}}j\binom{d-1}{j-1}B^j.
\]
For every \(j\ge2\), the coefficient of \(B^j\) on the right has \(13\)-adic valuation at least \(2(j-1)-\nu_{13}(j)\ge1\). Thus there is an integral \(13\)-adic matrix \(C_d\) such that
\[
U^d-I=169d(B+13C_d).
\]
For \(u>v\ge0\), with \(d=u-v\), this implies
\[
P_{r+28u}-P_{r+28v}
 =169d\bigl(A^r U^v(B+13C_d)\bigr)_{12}.
\]
As \(U\equiv I\pmod{13}\), the second factor reduces modulo \(13\) to
\[
(A^rB)_{12}\equiv6P_{r+1}+7P_r
\equiv6(P_{r+1}-P_r)\pmod{13}.
\]
This factor is a unit for **every** index \(r\ge0\). Indeed, the Pell norm identity is
\[
(P_{r+1}-P_r)^2-2P_r^2=(-1)^r,
\]
which follows by induction from the recurrence (or from the norm of \((1+\sqrt2)^r\)). If \(P_{r+1}-P_r\equiv0\pmod{13}\), the identity would force \(P_r^2\equiv6\) for even \(r\), or \(P_r^2\equiv7\) for odd \(r\), modulo \(13\). Yet the set of nonzero squares modulo \(13\) is \(\{1,3,4,9,10,12\}\). Both alternatives are impossible.

Therefore the factor multiplying \(169d\) is always a \(13\)-adic unit. This proves
\[
\nu_{13}(P_{r+28u}-P_{r+28v})=2+\nu_{13}(u-v)
\]
for all distinct \(u,v\ge0\), after interchanging them if necessary.

**3. Exact local image and multiplicities.** For any integer \(k\ge2\), the branch map
\[
u\mapsto P_{r+28u}\bmod13^k\]
(where \(0\le u<13^{k-2}\)) preserves the \(13\)-adic distance of arguments up to the fixed factor \(169\), by Step 2. Hence it is injective modulo \(13^{k-2}\). It has precisely \(13^{k-2}\) outputs, and all lie in the coset
\[
P_r+169\mathbb Z/13^k\mathbb Z.
\]
That coset also contains exactly \(13^{k-2}\) elements; the branch therefore **covers the entire coset**.

The requisite finite seed table, generated from the defining recurrence, is
\[
\begin{array}{c|rrrrrrrrrrrrrr}
r&0&1&2&3&4&5&6&7&8&9&10&11&12&13\\\hline
P_r\bmod169&0&1&2&5&12&29&70&0&70&140&12&164&2&168
\end{array}
\]
\[
\begin{array}{c|rrrrrrrrrrrrrr}
r&14&15&16&17&18&19&20&21&22&23&24&25&26&27\\\hline
P_r\bmod169&0&168&167&164&157&140&99&0&99&29&157&5&167&1
\end{array}.
\]
There are exactly the thirteen seed values listed in \(S\). Zero occurs for four seed indices and every other value occurs for two. Since every branch covers its whole seed coset bijectively, and distinct seed cosets do not intersect, the asserted image and exact fiber multiplicities follow for all \(k\ge2\).

**4. Least period and recurrence of every represented value.** The binomial identity in Step 2 gives \(U^{13^{k-2}}\equiv I\pmod{13^k}\), so \(28\cdot13^{k-2}\) is a period. Conversely, any scalar period \(T\) must satisfy \(P_T\equiv0\) and \(P_{T+1}\equiv1\pmod{13^k}\). The recurrence then yields \(P_{T-1}\equiv1\), hence \(A^T\equiv I\pmod{13^k}\). Reduction modulo \(13\) forces \(T=28d\), and the exact branch-distance lemma with \(r=u=0\) and \(v=d\) gives \(\nu_{13}(P_T)=2+\nu_{13}(d)\). Thus \(13^{k-2}\mid d\). This proves minimality.

Finally, repeating each index modulo the established period yields infinitely many nonnegative representing indices. Taking the inverse limit over \(k\) gives the finite disjoint union of \(13\)-adic cosets. Its normalized Haar measure is \(13/169=1/13\). Reducing the seed table modulo \(13\) gives the nine-value exceptional first level.

## Verification
The accompanying dependency-free `verify_pell13.py` uses independent binary matrix powering and direct linear-recurrence enumeration. Executed output:

```
VERIFY_OK levels=1..6 max_period=799708 image_size_k6=371293 base_classes=13 isometry_pairs=1120
```

It verifies the exact seed matrix congruences, the seed table, the complete image and fiber counts through modulus \(13^6\), the return of the state after the predicted period, and 1,120 bounded pairs for the branch-distance identity. This is finite corroboration, not a substitute for the general matrix-binomial argument in the proof.

## Relationship to prior work
Panda and Rout [3, §3] study periods of balancing numbers and identify the anomalous prime \(13\), along with \(31\) and \(1546463\). OEIS A238736 [1], established as a public record on March 4, 2014, also records these Pell/ balancing–Wieferich primes and relevant earlier work of Williams. Theorem 2.2 in Deveci and Karaduman [4] treats Pell sequence periods in finite groups, particularly dyadic moduli. The related 2015 generalized Pell paper [5] studies recurrence periods in groups. These period results, even when they provide the least period, do **not by themselves determine** the scalar residue image, the exact branch-distance law, or the full fiber counts. The present proof independently establishes these stronger scalar assertions.

Patel and Panda's 2023 paper [6], *Complete residue systems in balancing and Lucas-balancing sequences*, is a plausible related source. An authorized full-text copy was not available for inspection, so no noncoverage judgment is asserted for that paper. In addition to that explicit limitation, an unlocated classical scalar-image theorem remains a historical-priority risk; literature-search absence is not a mathematical uniqueness proof.

## Limitations
The classification is specific to the prime \(13\) and does not address prime \(31\), larger Pell–Wieferich primes, or general Lucas sequences. It does not estimate the least index representing a given high-precision residue outside the explicit periodic search window, nor does it establish a claim of absolute historical priority. Finite verification does not establish an infinite statement. Independent mathematical review has not been performed.

## References
[1] OEIS Foundation, A238736, *Balancing Wieferich primes* (created March 4, 2014), https://oeis.org/A238736.

[2] OEIS Foundation, A000129, *Pell numbers*, https://oeis.org/A000129.

[3] G. K. Panda and S. S. Rout, *Periodicity of Balancing Numbers*, Acta Mathematica Hungarica 143 (2014), 274–286, DOI:10.1007/s10474-014-0427-z; author-uploaded text https://www.researchgate.net/publication/264541220_Periodicity_of_Balancing_Numbers.

[4] Ö. Deveci and E. Karaduman, *The Pell Sequences in Finite Groups*, Utilitas Mathematica 96 (2015), https://www.researchgate.net/publication/295591003_The_Pell_Sequences_in_Finite_Groups.

[5] Ö. Deveci, M. Akdeniz and E. Karaduman, *The Generalized Pell p-Sequences in Groups*, Ars Combinatoria 120 (2015), https://combinatorialpress.com/ars-articles/volume-120/the-generalized-pell-p-sequences-in-groups/.

[6] S. C. Patel and G. K. Panda, *Complete residue systems in balancing and Lucas-balancing sequences*, AIP Conference Proceedings (2023), DOI:10.1063/5.0137875; bibliographic record https://www.researchgate.net/publication/371419266_Complete_residue_systems_in_balancing_and_Lucas-balancing_sequences.
