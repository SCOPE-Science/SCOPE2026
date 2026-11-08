# A sharp congruence obstruction and cyclic desubstitution for generalized Mephisto–Waltz words

## Finding

For each integer \(b\ge 3\), define the length-\(b\) binary morphism
\[\mu_b(0)=0^{b-1}1,\qquad\mu_b(1)=1^{b-1}0,\]
and let \(w_b=\mu_b^{\omega}(0)\) be its one-sided infinite fixed point. A *factor* is a contiguous finite word occurring in \(w_b\). The Lie complexity \(L_b(n)\) counts cyclic-rotation classes of length-\(n\) binary words all of whose rotations are factors of \(w_b\).

For a circular word \(v\) of length \(m\), write \(v^\omega\) for its right-infinite periodic repetition, and set
\[
\mathcal E_b(m)=\left\{[v]_{\rm cyc}: |v|=m,\quad
v^\omega[i..i+m]\in\operatorname{Fac}_{m+1}(w_b)
\text{ for every }0\le i<m\right\}.
\]
Here the interval \([i..i+m]\) contains \(m+1\) symbols; the test is independent of the chosen cyclic representative.

**Theorem.** For every integer \(b\ge3\), all the following statements hold.

1. The exact initial values are
\[
L_b(1)=2,\quad L_b(2)=3,\quad L_b(n)=4\ (3\le n\le b),\quad
L_b(b+1)=\begin{cases}3,&b=3,\\2,&b\ge4.\end{cases}
\]
2. **Sharp congruence obstruction:** if \(n\ge b+2\) and \(b\nmid n\), then \(L_b(n)=0\).
3. **Exact cyclic desubstitution:** for every integer \(m\ge2\), the map
\[
[v]_{\rm cyc}\longmapsto[\mu_b(v)]_{\rm cyc}
\]
is a bijection from \(\mathcal E_b(m)\) onto the rotation-complete factor classes of length \(bm\). In particular,
\[L_b(bm)=|\mathcal E_b(m)|\quad(m\ge2).\]
4. At the first nontrivial multiple, \(L_b(2b)=3\). More generally, \(L_b(2b^k)\ge3\) for every integer \(k\ge1\), so the divisibility restriction is not an eventual-vanishing statement.

The obstruction is sharp at the endpoint \(n=b+1\), where the Lie complexity is positive in every base. The bijection determines all surviving cyclic classes from one-step-longer periodic windows of the desubstituted word, rather than requiring exhaustive rotation tests at the original length.

## Assumptions and scope

All indices of \(w_b\) start at zero. The alphabet is exactly \(\{0,1\}\), and \(\bar c=1-c\). All lengths are positive integers. Conjugacy means cyclic rotation, **not** reversal, bit complementation or Abelian equivalence. The source word \(w_b\) is the fixed point of the displayed uniform morphism, not the different \(b\)-letter generalized Thue–Morse word. The theorem treats all integer bases \(b\ge3\), with no primality assumption. The set \(\mathcal E_b(m)\) is defined by actual factors, not by a finite-prefix approximation.

## Proof

**1. Transition skeleton and phase recognizability.** Let
\(d(j)=w_b(j)\oplus w_b(j+1)\), where \(\oplus\) is addition modulo two. Write \(j=bk+r\). The identity \(w_b=\mu_b(w_b)\) gives
\[
d(bk+r)=\begin{cases}
0,&0\le r\le b-3,\\
1,&r=b-2,\\
1,&r=b-1\text{ and }w_b(k)=w_b(k+1),\\
0,&r=b-1\text{ and }w_b(k)\ne w_b(k+1).
\end{cases}
\]
Thus \(d\) belongs to the phase-coded family of binary sequences formed by concatenating blocks \(0^{b-2}10\) or \(0^{b-2}11\), with arbitrary choices of the last digit allowed for an upper-bound argument.

A length-\(b\) factor of any such coded sequence has **exactly one or two ones**: every \(b\)-window contains exactly one mandatory one, at the residue \(b-2\), and possibly one optional one. If there is exactly one one, it is mandatory. If there are two, they are either consecutive, in which case the first is mandatory, or at the two ends of the window, in which case the last is mandatory. Since \(b\ge3\), these alternatives are disjoint. Hence each length-\(b\) factor identifies uniquely its starting *phase* modulo \(b\), irrespective of all optional digits. For two consecutive, overlapping length-\(b\) factors lying in an admissible length-\((b+1)\) factor, their uniquely determined phases differ by one modulo \(b\).

**2. Circular obstruction.** Suppose every cyclic rotation of a length-\(n\) word \(u\) is a factor of \(w_b\), where \(n\ge b+2\). Form its circular transition word \(q\), of length \(n\), with \(q_i=u_i\oplus u_{(i+1)\bmod n}\). Every circular \((n-1)\)-window of \(q\) is the internal transition string of a rotation of \(u\); hence it is a factor of \(d\). Since \(n-1\ge b+1\), every circular \((b+1)\)-window of \(q\) is admissible in the block-coded family above. Let \(\alpha_i\in\mathbb Z/b\mathbb Z\) be the uniquely determined starting phase of the circular length-\(b\) window beginning at \(q_i\). By the overlap property, \(\alpha_{i+1}=\alpha_i+1\pmod b\). But \(\alpha_{i+n}=\alpha_i\) because \(q\) is circular of length \(n\). Therefore \(n\equiv0\pmod b\). This proves claim 2, for *all* lengths, not only computationally tested ones.

**3. Source-word bijection.** Now let \(n=bm\ge b+2\). By the same unique phase assignment, rotate any rotation-complete \(u\) so the first transition has phase zero. The circular transition pattern then contains \(b-2\) zero transitions followed by a mandatory one in each consecutive block of length \(b\). Consequently each aligned block of \(u\) has the form \(c^{b-1}\bar c=\mu_b(c)\). Hence, up to rotation, \(u=\mu_b(v)\) for a unique circular word \(v\) of length \(m\). Uniqueness follows because a conjugacy between two such images must preserve the uniquely determined phase, hence rotate by a multiple of \(b\); the letter morphism is injective.

For any \(0\le i<m\) and \(1\le r<b\), the cyclic rotation of \(\mu_b(v)\) starting \(r\) symbols into block \(i\) is
\[
\operatorname{suf}_{b-r}(\mu_b(v_i))\,
\mu_b(v_{i+1}\cdots v_{i+m-1})\,
\operatorname{pref}_{r}(\mu_b(v_i)),
\]
with subscripts on \(v\) interpreted cyclically. If the source periodic window \(v_i\cdots v_{i+m-1}v_i\) occurs in \(w_b\), this rotated image occurs in \(\mu_b(w_b)=w_b\). The same is immediate for rotations at block boundaries. Thus \(v\in\mathcal E_b(m)\) implies all rotations of \(\mu_b(v)\) occur.

Conversely suppose all rotations of \(\mu_b(v)\) occur. For each \(i\), take the rotation starting **one** symbol into the \(i\)-th image block. Its unique transition phase forces its occurrence to start one symbol into an actual \(\mu_b\)-block of \(w_b\). The first suffix of length \(b-1\), the following \(m-1\) complete blocks, and the final prefix of length one determine, in order, the source letters \(v_i,v_{i+1},\ldots,v_{i+m-1},v_i\). Therefore this length-\((m+1)\) source word occurs in \(w_b\). This holds for every \(i\); hence \(v\in\mathcal E_b(m)\). The bijection and claim 3 follow.

**4. Short lengths and sharpness.** Every maximal run of equal symbols in \(w_b\) has length \(1\), \(b-1\), or \(b\). Indeed, a \(\mu_b\)-block has a run of \(b-1\) equal leading symbols and one opposite trailing symbol; across its boundary at most one trailing symbol merges with the next leading run. The word contains both source transitions \(01\) and \(10\), so runs of length \(b\) of both symbols occur. It also contains \(000\) and \(111\). For \(b\ge4\), no internal maximal run has length in \(\{2,\ldots,b-2\}\), and no factors \(0101\) or \(1010\) occur, since the transition skeleton has no three consecutive ones.

Consider a rotation-complete circular word of length \(3\le n\le b+1\), with \(b\ge4\). If it has at least four circular runs, every run can be flanked by its opposite symbols inside a length-\(n\) rotation. A run of length at least \(b-1\) would make the total length at least \(b+2\); all other runs must therefore have length one, forcing the forbidden alternating pattern. With two circular runs, if both have length at least two, both are witnessed as internal maximal runs. At least one must then have length in \(\{2,\ldots,b-2\}\), since their sum is at most \(b+1\), also impossible. Thus the only eligible cyclic classes are those of \(0^n\), \(1^n\), \(0^{n-1}1\), and \(1^{n-1}0\). The pure powers occur precisely for \(n\le b\). Every rotation of each one-minority word occurs for \(n\le b+1\): intermediate placements use a minority symbol in \(\mu_b(000)\) or \(\mu_b(111)\), and the two extreme placements use the length-\(b\) run between opposite symbols in \(\mu_b(10)\) or \(\mu_b(01)\). The base cases \(n=1,2\) follow since every length-two binary word occurs.

For \(b=3\), every length-three binary word occurs, and the complete length-four factor set is the set of all sixteen binary words except \(0000,1111,0101,1010\). The four exclusions follow from the maximal-run bound and the transition skeleton; every other length-four word occurs already in \(\mu_3^3(0)=001001110001001110110110001\), by direct inspection of its twelve distinct four-symbol factors. The eligible length-four cyclic classes are exactly those of \(0001\), \(0011\), and \(0111\). All initial values now follow. Since \(L_b(b+1)>0\) for every \(b\ge3\), the congruence threshold cannot be lowered.

**5. Surviving infinitely many multiples.** Every binary length-three word occurs in \(w_b\) for \(b\ge3\). Thus every length-three periodic window of each of the circular source words \(00\), \(01\), \(11\) occurs, and \(\mathcal E_b(2)\) has precisely three classes. Hence \(L_b(2b)=3\). Furthermore, because \(000,010,101,111\) all occur, the three periodic source words \(\mu_b^{k-1}(00)\), \(\mu_b^{k-1}(01)\), and \(\mu_b^{k-1}(11)\) satisfy the cyclic one-step extension test for each \(k\ge1\): apply \(\mu_b^{k-1}\) to the relevant three-letter extensions. Their images furnish three rotation-complete classes at length \(2b^k\). These classes have different numbers of ones, because the zero-minus-one imbalance under \(\mu_b\) is multiplied by \(b-2>0\). Therefore they cannot be cyclically equivalent.

## Verification

The self-contained `verify.py` constructs uniform-morphism prefixes; checks the uniqueness of block phases for arbitrary optional block symbols at bases \(3\) through \(8\); independently computes direct rotation-complete classes at lengths \(1\) through \(68\); and checks the desubstitution bijection against actual length-\((m+1)\) factor sets at all tested multiples. Its printed diagnostic is

`VERIFY_OK bases=3..8 length_tests=408 phase_words=66 check=Lie_and_extension_equivalence`

The infinite results are established by Steps 1–5 of the proof. A finite-prefix test, however extensive, would not establish these universal statements on its own.

## Relationship to prior work

Bell and Shallit introduced Lie complexity and proved it is automatic for automatic words; they computed examples for the classical Thue–Morse, Cantor, Fibonacci and Tribonacci words, among others. Their general automaticity theorem does not imply the present sharp divisibility support or the explicit circular-desubstitution bijection. Li subsequently developed related extended Lie and prefix Lie complexities and Rauzy-graph bounds, without this block-phase theorem for these complementary substitutions.

The classical base-three Mephisto–Waltz word and its defining morphism are standard. Existing classifications of its ordinary squares concern factors of the form \(vv\), which are not equivalent to the condition that *every cyclic rotation* of \(v\) occurs. In particular, the three classes at length \(2b\) include a mixed class not supplied by merely counting square factors. The result is an invariant-specific extension, not a claim of inventing the word family or general automaticity of Lie complexity.

## Limitations

The one-step extension count \(|\mathcal E_b(m)|\) is an exact characterization but **not** a numerical closed formula for arbitrary multiples \(bm\); it is not asserted that every multiple has a nonzero Lie count. The theorem does not cover \(b=2\), whose block-phase uniqueness fails. The verifier checks finite instances only. No independent audit or external formal certification has been performed. An uncatalogued equivalent congruence theorem from recognizability theory remains a bibliographic possibility.

## References

- J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821v1, publicly posted 7 February 2021, especially Sections 1, 2, 6, and 7. https://arxiv.org/abs/2102.03821
- S. Li, *A note on the Lie complexity and beyond*, arXiv:2207.05859v1, publicly posted 12 July 2022, especially Sections 3–6. https://arxiv.org/abs/2207.05859
- Wolfram MathWorld, *Mephisto Waltz Sequence*, sequence definition \(0\mapsto001,1\mapsto110\), citing Allouche and Shallit (2003). https://mathworld.wolfram.com/MephistoWaltzSequence.html
