# Exact fixed-weight inverse-list spectrum of cyclic binary Rule 150

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the indexed cyclic elementary Rule 150 map, with \(n\ge1\) and
\[
(F_n(x))_i=x_{i-1}\oplus x_i\oplus x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z.
\]
Repeated neighbor indices at lengths one and two are evaluated with their full XOR multiplicity. For any \(0\le w\le n\), put
\[
p_{n,w}(y)=|\{x\in\{0,1\}^n:|x|=w,\ F_n(x)=y\}|,
\quad B_{n,w,j}=|\{y:p_{n,w}(y)=j\}|\quad(j\ge1).
\]
Thus \(B_{n,w,j}\) counts **distinct indexed outputs**, not inputs or decoding-mask choices. Let \(R_{n,w}=\sum_{j\ge1}B_{n,w,j}\), the largest size of a length-\(n\), weight-\(w\) source code for which the resulting outputs are all distinct.

**Theorem (complete fixed-weight inverse-list census).** If \(3\nmid n\), then \(B_{n,w,1}=\binom nw\), and every \(B_{n,w,j}\) with \(j\ne1\) is zero. If \(n=3m\) with \(m\ge1\), define, with out-of-range binomial coefficients zero,
\[
\begin{aligned}
M_1&=\binom{3m}{w},\\
M_2&=\frac32\binom{2m}{m}\binom m{w-m},\\
M_3&=\binom m{2m-w}\binom m{w-m}^{\!2},\\
M_4&=\begin{cases}\frac14\binom m{m/2}^{\!3},&2\mid m\text{ and }2w=3m,\\0,&\text{otherwise.}\end{cases}
\end{aligned}
\]
Then there are no fibers of size greater than four, and for each \(j=1,2,3,4\),
\[
\boxed{\displaystyle B_{n,w,j}=\sum_{s=j}^{4}(-1)^{s-j}\binom{s}{j}M_s.}
\]
Consequently the exact fixed-composition zero-error capacity is
\[
\boxed{\displaystyle R_{n,w}=M_1-M_2+M_3-M_4.}
\]
For \(3\mid n\), the weight layer is injective **if and only if** \(w<m\) or \(w>2m\). For every \(m\le w\le2m\) with \(2w\ne3m\), at least one output has exactly three sources; at \(2w=3m\) (necessarily even \(m\)) four-source fibers occur and no three-source fibers occur. The first condition includes \(n=3\) and the formulas include \(w=0,n\).

## Assumptions and scope

The binary alphabet is \(\mathbb F_2\), addition \(\oplus\) is mod two, source weight \(|x|\) counts one-bits, indices are fixed/labeled, and the update is a *single synchronous step* with periodic boundaries. No quotient by rotations or reflections is taken. Outputs of preimage count zero are excluded from the \(B\)-spectrum. We use \(\binom ab=0\) for integers \(b<0\) or \(b>a\). All formulas hold for all integers \(n\ge1\), \(0\le w\le n\); there are no asymptotic or genericity assumptions.

## Proof

**1. Kernel and cosets.** If two inputs \(x,x'\) have the same output, their XOR difference \(v=x\oplus x'\) satisfies \(v_{i-1}\oplus v_i\oplus v_{i+1}=0\). This gives \(v_{i+2}=v_i\oplus v_{i+1}\) and then \(v_{i+3}=v_i\). If \(3\nmid n\), the period-three and period-\(n\) constraints make \(v\) constant, and the recurrence forces that constant to be zero. Hence \(F_n\) is injective. If \(n=3m\), there are exactly four kernel words, obtained by repeating \(000,011,101,110\) for \(m\) periods. Thus each unrestricted output fiber is an affine coset of four inputs. Every nonzero kernel word flips exactly two of the three residue classes modulo three, each of length \(m\).

**2. Binomial moments.** Write \(S_w=\{x:|x|=w\}\) and \(p(y)=|S_w\cap F_n^{-1}(y)|\). Define \(M_s=\sum_y\binom{p(y)}s\) for \(1\le s\le4\). Trivially \(M_1=|S_w|\). Every pair in the same fiber differs by one of the three nonzero kernel words. Fix one such difference, supported on \(2m\) coordinates. The weights of both words are \(w\) precisely when the support contains \(m\) ones and its complement contains \(w-m\) ones. Thus there are \(\binom{2m}m\binom m{w-m}\) ordered initial choices for that difference. Summing over three differences and dividing by two for the two orientations of each pair gives the stated \(M_2\).

**3. Triple intersections.** Fix an input and two distinct nonzero kernel shifts, for instance the shifts flipping residue-class pairs \(\{0,1\}\) and \(\{0,2\}\). If the three original class weights are \((a,b,c)\), the three shifted words retain weight \(w=a+b+c\) precisely when \(a+b=m\) and \(a+c=m\). Equivalently, \(a=2m-w\) and \(b=c=w-m\), so the number of possible anchors is \(\binom m{2m-w}\binom m{w-m}^2\). There are exactly three unordered pairs of distinct nonzero shifts. Every unordered triple of distinct fixed-weight inputs in a common fiber has exactly three possible choices of anchor. Dividing the total anchored count by three proves \(M_3\).

**4. Fourfold intersections.** All four elements of a kernel coset have weight \(w\) precisely when each of the three residue classes contains \(m/2\) ones. This requires \(m\) even and \(w=3m/2\). There are \(\binom m{m/2}^3\) possible anchored inputs, but each fourfold fiber supplies four anchors. This proves \(M_4\). It also shows that all threefold fibers at the central weight are actually fourfold, whereas away from that weight every nonzero \(M_3\) corresponds to a genuine threefold fiber.

**5. Exact inversion and thresholds.** As every \(p(y)\le4\), \(M_s=\sum_{j=s}^4\binom js B_{n,w,j}\). Binomial inversion yields the boxed formulas, including \(R_{n,w}=M_1-M_2+M_3-M_4\). The map restricted to \(S_w\) is injective exactly when \(M_2=0\); by the positive central binomial coefficient this happens exactly outside \([m,2m]\). Within that interval, \(M_3>0\). For noncentral weights \(M_4=0\), hence \(B_3=M_3>0\); at the central weight \(M_3=4M_4\), hence \(B_3=0\) and \(B_4=M_4>0\). This completes every case.

## Verification

Execute `python CHECK.py` using Python 3 and its standard library. Its direct enumerator constructs \(F_n(x)\) independently of the binomial-moment formulas, groups all sources at each weight by exact output bit vector, and compares every fiber-size histogram with the prediction for **all** \(189\) pairs \((n,w)\) at \(1\le n\le18\), comprising \(524286\) individual source evaluations. Separately, the checker exercises all weights at \(n=3m\) for \(1\le m\le80\) using exact integer arithmetic and checks the moment inversion, injectivity boundaries, and center-weight behavior. Its reproduced illustrative results include \((B_{9,3,1},B_{9,3,2},B_{9,3,3})=(27,27,1)\) and \((B_{6,3,2},B_{6,3,4})=(6,2)\). These finite checks are corroboration, not a replacement for the all-length proof.

## Relationship to prior work

Bhattacharjee and Das (2019) establish the size-dependent reversibility of Rule 150, including reversibility for ring lengths not divisible by three. That known injectivity result is a premise, not a new contribution here. Hernández Serrano and Martín del Rey (2019) derive inverse transition formulas *for reversible* cyclic rules; those formulas do not classify the fixed-weight fibers of the non-reversible lengths. Dennunzio et al. (2020) prove much broader decidability and topological results for additive cellular automata, without an explicit fixed-weight finite-ring preimage census. Another published study of cyclic Rule 150 on rotation *necklaces* reports unrestricted necklace predecessor degrees, a different equivalence relation and no fixed-weight source-layer classification. The new statement fixes indexed coordinates, restricts source Hamming weight, and gives all four exact fiber populations and capacity for every ring length and weight. General linear-code coset-weight identities could potentially furnish an alternative derivation; no assertion of independence from those general identities is made.

## Limitations

This is a fixed-weight **source** restriction, not a claim that Rule 150 conserves source weight; output Hamming weights are unrestricted. The theorem does not treat cyclic rotation classes, multiple update steps, noise or errors in the observed output. A prior general coset-intersection formula could subsume the calculation even if not named as a Rule 150 result; broader historical priority remains subject to external checking. The proof establishes exact finite counts but no computational-complexity lower bound or new universal coding bound beyond this observation map.

## References

1. Kamalika Bhattacharjee and Sukanta Das, *On Finite 1-Dimensional Cellular Automata: Reversibility and Semi-reversibility*, first arXiv public posting 2019-03-14, https://arxiv.org/abs/1903.06011.
2. D. Hernández Serrano and A. Martín del Rey, *A closed formula for the inverse of a reversible cellular automaton with (2R+1)-cyclic rule*, Applied Mathematics and Computation 357 (2019), 23–34, https://doi.org/10.1016/j.amc.2019.03.060; lawful open repository https://hdl.handle.net/10366/161854.
3. Alberto Dennunzio, Enrico Formenti, Darij Grinberg and Luciano Margara, *From Linear to Additive Cellular Automata*, ICALP 2020, https://doi.org/10.4230/LIPIcs.ICALP.2020.125.
