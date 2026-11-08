# Sharp fivefold covering of the dyadic parabola

## Finding
For each integer \(k\ge1\), let \(R_k=\mathbb Z/2^k\mathbb Z\) and let the parabola graph be
\[
G_k=\{(x,x^2):x\in R_k\}\subset R_k^2.
\]
Write \(hG_k\) for the set of sums of exactly \(h\) elements of \(G_k\), with repetition permitted, and put
\[
P_k=\{(s,t)\in R_k^2:s\equiv t\pmod2\}.
\]
The sharp covering order is
\[
\boxed{\min\{h\ge1:hG_k=P_k\}=\begin{cases}1,&k=1,\\3,&k=2,\\5,&k\ge3.\end{cases}}
\]
In particular, for every \(k\ge1\) and every \((s,t)\in R_k^2\) with \(s\equiv t\pmod2\), there are five residues \(x_1,\ldots,x_5\in R_k\) satisfying both
\[
\sum_{i=1}^{5}x_i=s,\qquad \sum_{i=1}^{5}x_i^2=t\quad\text{in }R_k.
\]
For every \(k\ge3\), the target \((2,0)\) is not a sum of four graph points. All assertions are for the complete rings, not only their unit subsets.

## Assumptions and scope
All exponents \(k\) are integers at least one. Integers \(s,t\) are interpreted modulo \(2^k\); the congruence \(s\equiv t\pmod2\) means parity agreement. Sums are ordered only for construction; the sumset discards order. There is no constraint that individual summands be nonzero, distinct, positive, or units. Since \((0,0)\in G_k\), the sumsets \(hG_k\) are nested. The parity restriction is necessary because \(x^2\equiv x\pmod2\) for every integer \(x\).

## Proof
**1. Base at modulus four.** Fix a target \((s,t)\in P_2\), where \(s,t\) are residues modulo four. Choose an integer \(r\) from \(\{1,2,3,4\}\) such that \(r\equiv t\pmod4\). Start with five entries, exactly \(r\) of them equal to one and the others equal to zero. Their square sum is \(r\equiv t\pmod4\), and their ordinary sum is also \(r\). Since \(s\equiv t\pmod2\), either \(s\equiv r\pmod4\) or \(s\equiv r+2\pmod4\). In the second case, replace any one of the five entries by that entry plus two. This changes its ordinary contribution by two but leaves its square unchanged modulo four. Thus every target of \(P_2\) has a five-term representation. Each such representation contains both an even and an odd entry, since \(1\le r\le4\). This mixed-parity property is preserved under all later lifts.

**2. Lifting lemma.** Suppose \(k\ge2\) and a tuple of five integers \(x_1,\ldots,x_5\) represents a given pair modulo \(2^k\), with at least one even and one odd entry. Put \(N=2^k\) and regard the same integers modulo \(2N\). We can independently toggle the top bit of its first-moment sum and the top bit of its second-moment sum, while preserving the lower \(k\) bits and both entry parities.

For the first toggle, add \(N\) to any one entry. Its sum changes by \(N\), whereas its square changes by \(2Nx_i+N^2\equiv0\pmod{2N}\). For the second toggle, choose an even entry \(x_e\) and an odd entry \(x_o\), replace them by \(x_e+N/2\) and \(x_o-N/2\). The sum is unchanged, and the square sum changes by
\[
N(x_e-x_o)+N^2/2\equiv N\pmod{2N}.
\]
The first term is \(N\) modulo \(2N\) because \(x_e-x_o\) is odd, while \(N^2/2=2^{2k-1}\) is divisible by \(2N=2^{k+1}\) for \(k\ge2\). The shifts are even, so the even/odd status of every entry remains unchanged. Applying both toggles together also works: adding \(N\) to an entry changes its square by a multiple of \(2N\) regardless of the prior second-toggle operation. Hence all four lifts of the represented target modulo \(N\) are represented modulo \(2N\) by mixed-parity five-tuples.

Apply this lemma inductively from the mixed-parity base modulo four. The inverse image of \(P_k\) under reduction from modulus \(2^{k+1}\) consists of four lifts of every target in \(P_k\). Thus \(5G_k=P_k\) for every \(k\ge2\). For \(k=1\), the two available graph points \((0,0)\), \((1,1)\) already constitute \(P_1\).

**3. The exact order at modulus four.** With two entries \(x,y\), any target having odd first coordinate requires one even and one odd entry; its square sum then equals one modulo four. Thus the parity-allowed target \((1,3)\) does not belong to \(2G_2\). Conversely, three entries suffice for all eight targets. For \(t\equiv1,2,3\pmod4\), take exactly \(t\) entries equal to one and the remaining entries zero, then add two to any entry if necessary to match \(s\) modulo four; the squares remain fixed. For \(t\equiv0\pmod4\), the all-even tuples \((0,0,0)\) and \((0,0,2)\) realize the two possibilities for \(s\). Therefore \(3G_2=P_2\) and the order is three.

**4. Sharpness from modulus eight onward.** Suppose four residues \(x_1,\ldots,x_4\) modulo eight satisfy \(\sum_i x_i^2\equiv0\pmod8\). Let \(r\) denote the number of odd entries. Each odd square is one modulo eight; each even square is zero or four. Reduction modulo four forces \(r\equiv0\pmod4\), so \(r=0\) or \(r=4\). The latter case contributes four modulo eight to the square sum and is impossible. Therefore every entry is even. Write \(x_i=2y_i\). The square congruence becomes \(4\sum_i y_i\equiv0\pmod8\), so \(\sum_i y_i\) is even. Consequently \(\sum_i x_i=2\sum_i y_i\equiv0\pmod4\), and it cannot equal two modulo eight. The target \((2,0)\in P_3\) is thus absent from \(4G_3\), and its compatible lifts are absent from \(4G_k\) for every \(k\ge3\). Since \((0,0)\in G_k\), no sum of fewer than five terms can represent it either. Combining this with the five-term construction establishes the stated minimum for all exponents.

## Verification
The standalone `checker.py` computes exactly the nested sumsets \(hG_k\) for all \(1\le h\le5\) and \(1\le k\le7\). It independently enumerates mixed-parity five-tuples for \(k=2,3,4\) and checks that the two explicit top-bit toggles yield their claimed changes modulo \(2^{k+1}\). The run returned `VERIFY_OK k=1..7, mixed_lift_k=2..4; proofs extend to all exponents`. These are finite corroborations. The infinite result follows from the proven lift and obstruction lemmas, not the finite enumeration.

## Relationship to prior work
Tóth, *Counting solutions of quadratic congruences in several variables revisited* (2014), counts solutions of one quadratic congruence, including some power-of-two cases. Such a count does not assert the simultaneous prescribed linear and quadratic moments in this theorem. Hickman and Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N* (2018), study harmonic-analysis estimates on polynomial curves under different hypotheses; their restriction bounds do not imply the stated sharp fivefold covering. The published *Parity-sharp fourth moments of the dyadic quadratic graph* studies the same graph but determines sharp fourth-moment norms and energy, not its minimal additive covering order. General sum-cover results for finite abelian groups do not directly furnish this specific graph's fivefold sharpness. None of these inspected results contains or logically implies the present two-moment covering statement.

## Limitations
The result treats only the dyadic parabola \((x,x^2)\) and its sums with unrestricted repeated elements. It gives existence and sharp order, not a formula for the number of representations of each target. It does not classify minimal sumset orders for odd prime powers or other polynomial curves. An equivalent older result under local quadratic-form or additive-basis terminology cannot be excluded without independent bibliographic review. The computer checks are not an infinite proof, and an independent audit has not been conducted.

## References
1. L. Tóth, *Counting solutions of quadratic congruences in several variables revisited*, arXiv:1404.4214v1, first posted 2014-04-16, *Journal of Integer Sequences* 17 (2014), Article 14.11.6. https://arxiv.org/abs/1404.4214 ; https://cs.uwaterloo.ca/journals/JIS/VOL17/Toth/toth12.pdf
2. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176v1, first posted 2018-01-09. https://arxiv.org/abs/1801.03176
3. *Parity-sharp fourth moments of the dyadic quadratic graph*, published research record, October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-parity-sharp-fourth-moments-of-the-dyadic-quadratic-graph--417e488b0292
4. H. Haanpää, *Minimum Sum and Difference Covers of Abelian Groups*, *Journal of Integer Sequences* 7 (2004), Article 04.2.6. https://cs.uwaterloo.ca/journals/JIS/VOL7/Haanpaa/haanpaa.html
