# Two-run witnesses for nontransitivity at every rational frequency above one half

## Finding

**Theorem.** Let \(a>b\ge1\) be coprime integers, and set \(c=a/(a+b)\). Let \(P(c)\) be the one-sided Becker–Baraviera generating family: zeros may be followed by either digit, whereas a one must be followed by another one if and only if the density of ones in the prefix ending at that one is at most \(c\). Let \(\Sigma(c)\) be the closure of all forward shifts of points of \(P(c)\).

There is an explicit admissible finite word \(\omega\) which can occur in a generating sequence only at its first position. Consequently, \(\omega v\omega\) belongs to no sequence of \(\Sigma(c)\), for every finite binary connector \(v\), and \(\Sigma(c)\) is **not topologically transitive**.

Specifically, let \(m\in\{1,\ldots,b\}\) be the unique integer satisfying
\[
 am\equiv b-1\pmod b,
\qquad q=\frac{am-b+1}{b}\ge1.
\]
Then one may take
\[
\boxed{\omega=0^b1^{a+1}0^m1^q0.}
\]
The construction applies uniformly to all rational \(c\in(1/2,1)\). The noninteger-ratio range \(1/2<c<2/3\) is its genuinely new parameter region compared with earlier single-run obstructions.

## Assumptions and scope

We use one-sided sequences indexed from position one, finite words consisting of consecutive symbols, and ordinary topological transitivity of the left shift on the subshift \(\Sigma(c)\). For a prefix \(u\), put \(N_0(u)\) and \(N_1(u)\) for its zero and one counts and define the **integer discrepancy**
\[
 H(u)=aN_0(u)-bN_1(u).
\]
The transition after a one is to one precisely when \(H(u)\ge0\); otherwise it is to zero. Thus each zero adds \(a\), while each one subtracts \(b\). The coefficient \(a>b\) is used essentially; the argument neither covers \(c=1/2\) nor asserts anything for irrational \(c\).

A *closed one-run* is a maximal positive-length string of ones that is followed by a zero. All one-runs in a generating infinite sequence are finite: after sufficiently many successive ones, the discrepancy becomes negative and the next digit is forced to be zero.

## Proof

**1. Residual-discrepancy lemma.** After every closed one-run in a generating sequence, the discrepancy belongs to \(\{-b,-b+1,\ldots,-1\}\). If the sequence begins with a one, its initial one-run has length one and leaves \(-b\). Otherwise the first one-run begins after at least one zero and hence with discrepancy at least \(a>0\). For every later one-run, the preceding closed run leaves discrepancy at least \(-b\), and the intervening nonempty zero-run raises it by at least \(a\). Hence its starting discrepancy is at least \(a-b>0\). When a one-run starts with nonnegative integer discrepancy \(d\), its forced length is \(\lfloor d/b\rfloor+1\), leaving \(d-b(\lfloor d/b\rfloor+1)\in\{-b,\ldots,-1\}\). Induction proves the lemma.

**2. Admissibility of the witness.** Because \(a\) and \(b\) are coprime, a unique \(m\in\{1,\ldots,b\}\) solves \(am\equiv b-1\pmod b\). Then \(am=bq+b-1\) and \(q\ge1\), as \(a>b\). Starting from discrepancy zero, the block \(0^b\) raises it to \(ab\), so the next closed one-run has length exactly \(a+1\) and ends at discrepancy \(-b\). After \(0^m\) the discrepancy is
\[
-b+am=bq-1.
\]
The next closed one-run has exactly \(q\) ones, ending at \(-1\); a zero must follow. Thus \(\omega\) is an admissible prefix, and \(\omega0^{\infty}\in P(c)\).

**3. Uniqueness of the occurrence.** Suppose a copy of \(\omega\) occurred strictly after the first position of a generating sequence. The first closed one-run of this copy is \(1^{a+1}\), directly preceded by the displayed \(b\) zeros. Let \(s\ge b\) be the length of the *entire* zero-run immediately preceding those ones. If that zero-run were the initial run of the generating sequence, it would start with discrepancy zero and the subsequent one-run would have length \(\lfloor as/b\rfloor+1\). For \(s=b\) the occurrence would begin at position one, contrary to assumption; for \(s\ge b+1\) this length is at least \(a+2\). Hence this zero-run follows an earlier closed one-run.

Write \(r\in\{-b,\ldots,-1\}\) for the discrepancy at the end of that earlier one-run. The discrepancy just before \(1^{a+1}\) is \(as+r\), which is positive. Therefore the length \(a+1\) forces
\[
 ab\le as+r\le ab+b-1.
\]
For \(s=b\), the left inequality fails because \(r<0\). For \(s\ge b+2\), the left side is exceeded by at least \(2a-b>b\), so the right inequality fails. Thus \(s=b+1\), and
\[
0\le a+r\le b-1.
\]
The residual discrepancy after this exceptional matching first one-run is
\[
 r'=a+r-b=-b+\delta,
 \qquad 1\le\delta=a+r\le b-1,
\]
where \(\delta\ge1\) follows from \(a>b\) and \(r\ge-b\). (If \(b=1\), no such \(\delta\) exists, so no later occurrence is possible already.)

In the alleged later copy of \(\omega\), the next zero-run is exactly \(0^m\). Its starting discrepancy for the following one-run is therefore
\[
 r'+am=(-b+\delta)+(bq+b-1)=bq+\delta-1,
\]
which lies in \(\{bq,\ldots,bq+b-2\}\). The forced closed one-run after these zeros has length \(q+1\), contradicting the required \(1^q0\) in \(\omega\). Thus no later occurrence is possible.

**4. Consequence for the subshift.** The word \(\omega\) occurs in \(P(c)\), so \(\omega\in\mathcal L(\Sigma(c))\). If \(\omega v\omega\) belonged to the language for some finite \(v\), its cylinder would be a nonempty open set and, by the definition of \(\Sigma(c)\) as the closure of shifts of \(P(c)\), it would occur as a factor of an unshifted generating sequence. That sequence would contain a noninitial occurrence of \(\omega\), contradicting Step 3. Therefore no connecting word joins \(\omega\) to itself, which violates the language criterion for topological transitivity. \(\square\)

## Verification

A standalone standard-library Python checker, `check_marker.py`, independently implements the digit-transition rule with integer discrepancies and uses finite-state dynamic programming plus a prefix-matching automaton to search for any occurrence of the constructed marker at a positive position. For all coprime pairs in the explicit checked range and all generated prefixes through length 150, it found no such occurrence. The checker also verifies the arithmetic construction and tests the initial witness directly. It is a finite diagnostic only; the proof above is the justification for the universal quantifier.

For the smallest newly covered case, \(c=3/5\), take \((a,b,m,q)=(3,2,1,1)\). The witness is \(\omega=001111010\). The first one-run leaves discrepancy \(-2\), and the second run leaves \(-1\). A later copy matching its first run would instead leave discrepancy \(-1\), forcing the next run to have two ones rather than one.

## Relationship to prior work

Reyes (2026), arXiv:2611.10995v1, defines the frequency shifts, supplies the discrepancy rule and closed-run formula (Lemmas 2.4–2.5), proves nontransitivity for parameters \(c=k/(k+1)\) with integers \(k\ge2\) (Theorem C), and explicitly asks for the general transitivity classification (Question 7.1). The present proof requires two consecutive closed one-runs and modular selection of the intervening zero-run to distinguish the initial state from a shifted imitation. In particular, it applies to all rational \(c\in(1/2,2/3)\), outside the integer-ratio family and beyond earlier single-run marker arguments.

Becker and Baraviera (2023) introduced the generating rule and established non-finite-typeness and positive entropy. García-Ramos, Pavlov and Reyes (2024) studied **bounded-density shifts**, a different hereditary family defined by upper bounds on window counts, whereas the frequency shifts considered here enforce a state-dependent successor after every one. Their entropy/intrinsic-ergodicity results do not imply the present nontransitivity statement.

## Limitations

The theorem is for reduced rational parameters strictly above one half, not irrational parameters. The explicit marker is not claimed to be the shortest possible witness. The nontransitivity statement says nothing about intrinsic ergodicity, global language decomposition, or existence of dense orbits within proper subsystems. Mathematical priority remains subject to the complete 2023 founding article, which could not be inspected in full through the available sources; the 2026 paper's explicit open classification question is the strongest inspected indication of an unresolved gap. Numerical checks do not certify the infinite assertion, and independent mathematical assessment is not yet available.

## References

1. Carlos Reyes, *Frequency shifts: non-soficity, absence of specification and intrinsic ergodicity*, arXiv:2611.10995v1, first posted 7 November 2026, especially Lemmas 2.4, 2.5, 2.7, Theorem C and Question 7.1. https://arxiv.org/abs/2611.10995
2. Alex J. Becker and Alexandre T. Baraviera, *Symbolic Systems with Prescribed Partial Digit Density*, *Journal of Statistical Physics* **190** (2023), article 143, DOI:10.1007/s10955-023-03158-8. https://doi.org/10.1007/s10955-023-03158-8
3. Felipe García-Ramos, Ronnie Pavlov and Carlos Reyes, *Measures of maximal entropy of bounded density shifts*, *Ergodic Theory and Dynamical Systems* **44** (2024), 2960–2974, arXiv:2302.07307. https://arxiv.org/abs/2302.07307
