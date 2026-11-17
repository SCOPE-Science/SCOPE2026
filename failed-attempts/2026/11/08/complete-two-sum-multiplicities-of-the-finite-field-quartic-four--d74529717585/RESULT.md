# Complete two-sum multiplicities of the finite-field quartic Fourier graph

## Finding
Let \(F\) be a finite field of order \(q\) with characteristic greater than three. Let \(\chi:F\to\{-1,0,1\}\) be its quadratic character, with \(\chi(0)=0\), and put
\[
\epsilon=\chi(-1),\quad \delta=\chi(-3),\quad \eta=\chi(-6),\quad g=\gcd(4,q-1).
\]
For the quartic Fourier graph \(C=\{(x,x^4):x\in F\}\), define the ordered two-sum multiplicity
\[
r(s,t)=\#\{(x,y)\in F^2:x+y=s,\ x^4+y^4=t\}.
\]
Then the **complete positive-multiplicity profile** is as follows.

* At \(s=0\), exactly one target has multiplicity \(1\), exactly \((q-1)/g\) other targets have multiplicity \(g\), and the remaining targets have multiplicity zero.
* At each of the \(q-1\) nonzero values of \(s\), there is exactly one target \(t=s^4/8\) with odd multiplicity \(2+\eta\) (equal to \(1\) or \(3\)). Apart from that target, exactly
\[
B=\frac{q+\epsilon+2\delta}{4}
\]
targets have multiplicity \(2\), and exactly
\[
A=\frac{q-4-\epsilon-2\delta-2\eta}{8}
\]
targets have multiplicity \(4\). All other targets have multiplicity zero. In particular, \(A,B\) are nonnegative integers for every allowed finite field.

A pointwise formula supplements the frequency table: for every \(s,t\in F\), let \(Z_{s,t}=\{z\in F:z^2+6s^2z+s^4-8t=0\}\); then
\[
\boxed{r(s,t)=\sum_{z\in Z_{s,t}}(1+\chi(z)).}
\]
This identity includes repeated roots as one element of \(Z_{s,t}\), not with algebraic multiplicity.

Consequently, the exact sumset size is
\[
\boxed{|C+C|=1+\frac{q-1}{g}+\frac{(q-1)(3q+4+\epsilon+2\delta-2\eta)}{8}.}
\]
More generally, **every positive integer moment of the representation function** is explicit: for every integer \(h\ge1\),
\[
\boxed{\sum_{s,t\in F}r(s,t)^h=1+(q-1)g^{h-1}+(q-1)\bigl((2+\eta)^h+2^h B+4^h A\bigr).}
\]
In particular, the cubic collision moment equals
\[
\sum_{s,t}r(s,t)^3
=1+(q-1)g^2+(q-1)(10q-18-6\epsilon-12\delta-3\eta).
\]
The quadratic collision moment (additive energy) is already available in the published literature and is **not claimed as new**. The additional character \(\eta=\chi(-6)\) is invisible in that known energy but controls the singleton fiber, sumset cardinality and cubic collision moment.

## Assumptions and scope
All sums count ordered pairs over the *same* finite field \(F\), whose order may be a proper prime power. The characteristic exceeds three, so division by \(2\), \(3\), \(6\) and \(8\) is legitimate. The target \(t=s^4/8\) is defined using the multiplicative inverse of \(8\) in \(F\). The formulas concern the full group convolution \(1_C*1_C\) under counting measure on the additive group \(F^2\); they do not assert a sharp unrestricted Fourier-extension operator norm. When \(g=2\), the multiplicity-\(g\) zero-sum targets belong to the same numerical level \(2\) as nonzero-sum targets; the table is separated by the first-coordinate fiber to avoid accidental conflation.

## Proof
1. **Pointwise root reduction.** Fix \(s\). Set \(x=(s+u)/2\), \(y=(s-u)/2\); the map from \(u\) to ordered pairs with \(x+y=s\) is a bijection. Direct binomial expansion gives
\[
8(x^4+y^4)=s^4+6s^2u^2+u^4.
\]
Writing \(z=u^2\), the equation \(x^4+y^4=t\) is \(z^2+6s^2z+s^4-8t=0\). Every \(z\in F\) has exactly \(1+\chi(z)\) square roots \(u\), proving the pointwise formula. Because the polynomial in \(z\) is quadratic, the multiplicity is at most four.

2. **The zero-sum fiber.** At \(s=0\), the original pair is \((x,-x)\) and its quartic sum equals \(2x^4\). The zero image has one preimage. On the nonzero field elements, the fourth-power homomorphism has kernel of order \(g=\gcd(4,q-1)\), hence \((q-1)/g\) nonzero images, each with exactly \(g\) preimages.

3. **The exceptional nonzero-sum target.** Fix \(s\ne0\). The quartic polynomial \(u\mapsto(s^4+6s^2u^2+u^4)/8\) is even, so all preimages \(u\ne0\) occur in opposite pairs. Thus only the value assumed at \(u=0\), namely \(t=s^4/8\), can have odd representation count. On that target the equation is \(u^2(u^2+6s^2)=0\), giving \(1+(1+\chi(-6s^2))=2+\eta\) solutions. The other nonzero-sum target multiplicities are therefore \(0\), \(2\) or \(4\).

4. **Exact second moment on a nonzero slice.** The ordered collision count for this fixed \(s\) is the number of pairs \((u,v)\in F^2\) satisfying
\[
(u^2-v^2)(u^2+v^2+6s^2)=0.
\]
The equal-square locus has \(2q-1\) points. The other locus, \(u^2+v^2=-6s^2\), has exactly \(q-\epsilon\) points: for any nonzero \(c\), elementary quadratic-character summation gives \(\#\{(u,v):u^2+v^2=c\}=q-\chi(-1)\). Their intersection satisfies \(u^2=v^2=-3s^2\), and has exactly \(2(1+\delta)\) points, because \(-3s^2\ne0\). Inclusion-exclusion therefore gives
\[
\sum_t r(s,t)^2=(2q-1)+(q-\epsilon)-2(1+\delta)
=3q-3-\epsilon-2\delta.
\]
The quadratic-character identity just used follows, for instance, from \(\sum_u\chi(c-u^2)=-\chi(-1)\), itself proved by the bijective change of variables \((v-u,v+u)\) in \(v^2-u^2=c\), which has exactly \(q-1\) solutions when \(c\ne0\).

5. **Recovery of every stratum.** Let \(A\) count multiplicity-four targets and \(B\) count multiplicity-two targets on a fixed nonzero-sum fiber. The total of \(q\) ordered representations and the preceding collision identity give the *independent* linear equations
\[
4A+2B+(2+\eta)=q,\qquad16A+4B+(2+\eta)^2=3q-3-\epsilon-2\delta.
\]
Solving yields precisely the stated formulas for \(A\) and \(B\). Since each is the count of an actual stratum, nonnegativity and integrality hold. This also proves that no other positive multiplicity can occur.

6. **Sumset and all collision moments.** The number of occupied targets at \(s=0\) is \(1+(q-1)/g\); at each nonzero \(s\) it is \(1+A+B\). Adding and substituting the closed formulas gives the sumset expression. Raising each multiplicity to any positive integer \(h\) and summing its frequency proves the general moment identity. At \(h=2\), it reduces to the previously known additive energy
\[
\sum_{s,t}r(s,t)^2=3q^2-q-1-(q-1)(1+\delta)^2.
\]
At \(h=3\), direct simplification gives the displayed cubic collision moment. This completes every assertion.

## Verification
A standalone exact-arithmetic script `CHECK.py` independently constructs finite fields, exhaustively tallies the two-sum multiplicities, evaluates \(\epsilon\), \(\delta\), \(\eta\), and checks all stratum counts, sumset cardinality and energy. The verified examples comprise 42 distinct prime fields and four nonprime finite fields, with \(519{,}934\) target positions in total. It prints `CHECK_OK fields=46 prime_fields=42 extension_fields=4 exact_target_entries=519934` on success. These computations are **finite corroboration**, not evidence of exhaustive coverage of all finite fields; the proof above establishes the universally quantified statements.

## Relationship to prior work
The earlier published result *Exact additive energy of the finite-field quartic graph* proves the same quadratic collision-slice identity and the \(h=2\) aggregate, for arbitrary finite fields of characteristic greater than three. Those statements are credited as prior work, not repackaged as new. They do not distinguish the \(\eta=\chi(-6)\)-controlled odd-multiplicity target, identify each multiplicity level or determine the full twofold sumset and higher collision moments. The exact energy does not determine this finer distribution by itself.

The published *Complete two-sum spectrum of the finite-field fifth-power graph* develops an analogous multiplicity-counting strategy for \((x,x^5)\), with a different zero-sum fiber and a different pair of character obstructions. The method of combining a collision count with one exceptional fiber is thus not claimed as new. The content here is the **precise quartic fiber classification**, including its exceptional fourth-power zero-sum branch and the independent arithmetic \(\chi(-6)\) discriminator. Both references have been compared at the level of their complete mathematical statements, not only their titles. General finite-field restriction and spectral-synthesis literature motivates examining exact convolution fibers, but does not itself state this quartic classification.

## Limitations
This result is a complete finite-field two-sum classification only, not a higher-sum classification, a sharp unrestricted Fourier-extension norm, or a statement about arbitrary composite residue rings. Characteristic two and three need separate treatment. Its proof is short and relies on the existing quartic energy computation plus established square-root counts and a multiplicity method used for the fifth-power graph. An older equivalent quartic spectrum in an unindexed source would supersede the novelty claim; literature inspection and negative searches do not establish priority conclusively. No independent mathematical audit has been performed.

## References
1. A. Iosevich, Z. Li and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404v1, first public 2026-09-21; introductory Fourier-energy and spectral-synthesis motivation.
2. *Exact additive energy of the finite-field quartic graph*, published-finding corpus public mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-additive-energy-of-the-finite-field-quartic-graph--235f10989b3f/RESULT.md (full mathematical statement inspected).
3. *Complete two-sum spectrum of the finite-field fifth-power graph*, published-finding corpus public mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-complete-two-sum-spectrum-of-the-finite-field-fifth-power-graph--f9410cde2e91/RESULT.md (full mathematical statement inspected).
4. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (2002), especially its even-exponent counting mechanism for full moment curves.
