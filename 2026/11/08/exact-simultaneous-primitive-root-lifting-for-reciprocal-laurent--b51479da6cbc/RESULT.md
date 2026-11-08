# Exact simultaneous primitive-root lifting for reciprocal Laurent maps

## Finding
Let \(p\ge7\) be prime, let \(\varepsilon\in\{1,-1\}\), and put \(f_\varepsilon(x)=x+\varepsilon x^{-1}\) on invertible residue classes. Write \(G_\varepsilon(p)\) for the set of \(a\in\mathbb F_p^\times\) such that both \(a\) and \(f_\varepsilon(a)\) generate \(\mathbb F_p^\times\). For every \(k\ge2\), and each \(a\in G_\varepsilon(p)\), the exact number of lifts \(x\bmod p^k\) with \(x\equiv a\pmod p\) for which both \(x\) and \(f_\varepsilon(x)\) are primitive roots modulo \(p^k\) is
\[
M_{p,k,\varepsilon}(a)=p^{k-2}\bigl(p-2+\delta_{p,\varepsilon}(a)\bigr),
\]
where \(\delta_{p,\varepsilon}(a)\in\{0,1\}\) is the explicit coincidence test below. In particular, each admissible residue-field pair has at least \((p-2)p^{k-2}\) simultaneous primitive lifts, and the total count is the sum over \(G_\varepsilon(p)\).

Combining this lift theorem with the finite-field classification of Cohen, Oliveira e Silva, Sutherland and Trudgian proves both parts of Sun's Conjecture 4.10, with a complete list of exceptions: for every odd prime \(p\) and every \(k\ge1\), a simultaneous primitive root \(x,f_+(x)\bmod p^k\) exists if and only if \(p\notin\{3,5,7,13\}\); for \(x,f_-(x)\), it exists if and only if \(p\notin\{3,5,13,61\}\). Here \(f_+(x)=x+x^{-1}\) and \(f_-(x)=x-x^{-1}\). These statements concern the ring \(\mathbb Z/p^k\mathbb Z\), not the finite field of cardinality \(p^k\).

## Assumptions and scope
A primitive root of \(\mathbb Z/p^k\mathbb Z\) is a generator of its cyclic unit group of order \(p^{k-1}(p-1)\). For \(p\ge7\), the derivative \(f_\varepsilon'(a)=1-\varepsilon a^{-2}\) is nonzero at every residue-field primitive element \(a\): otherwise \(a^2=\varepsilon\), which would give order at most four, whereas \(p-1\ge6\). The expression \(f_\varepsilon(x)\) is defined modulo any \(p^k\) because \(x\) is a unit.

The coincidence test is effective using arithmetic modulo \(p^2\). Take the integer representative \(A\in\{1,\dots,p-1\}\) of \(a\). Let \(B\in\{1,\dots,p^2-1\}\) represent \(f_\varepsilon(A)\bmod p^2\), and put \(d=1-\varepsilon A^{-2}\bmod p\), a nonzero element of \(\mathbb F_p\). For any integer \(z\) prime to \(p\), define its Fermat quotient \(Q_p(z)=(z^{p-1}-1)/p\). In \(\mathbb F_p\) define
\[
t_1=AQ_p(A),\qquad t_2=BQ_p(B)d^{-1},\qquad
\delta_{p,\varepsilon}(a)=\mathbf1_{t_1=t_2}.
\]
Only the reductions of these displayed numbers modulo \(p\) enter the test. The choice of \(B\) is canonical as specified; changing it by a multiple of \(p^2\) would not change its Fermat quotient modulo \(p\).

## Proof
**1. Prime-square primitive-root criterion.** Suppose \(u\bmod p\) is primitive. Then \(u\bmod p^2\) is primitive if and only if \(Q_p(u)\not\equiv0\pmod p\). Indeed, its order modulo \(p^2\) must be either \(p-1\) or \(p(p-1)\), and the first case is equivalent to \(u^{p-1}\equiv1\pmod{p^2}\). If it is primitive modulo \(p^2\), every lift to \(p^k\) remains primitive for \(k\ge2\). To see this directly, write \(u^{p-1}=1+pc\) with \(p\nmid c\); for odd \(p\), binomial expansion gives \(\nu_p((u^{p-1})^{p^j}-1)=j+1\) for every \(j\ge0\). Thus its order modulo \(p^k\) is \(p^{k-1}(p-1)\).

**2. Two unique forbidden first lifts.** Fix \(a\in G_\varepsilon(p)\), with representative \(A\) as above. Every residue modulo \(p^2\) reducing to \(a\) is uniquely \(x_t=A+pt\), \(t\in\mathbb F_p\). The ordinary binomial expansion gives
\[
Q_p(x_t)\equiv Q_p(A)-tA^{-1}\pmod p.
\]
(The coefficient is \((p-1)A^{p-2}\equiv-A^{-1}\pmod p\).) Hence \(x_t\) fails to be primitive modulo \(p^2\) at exactly one lift parameter, \(t=t_1\).

Similarly, because inversion is differentiable on units,
\[
f_\varepsilon(x_t)\equiv B+ptd\pmod{p^2},\qquad
Q_p(f_\varepsilon(x_t))\equiv Q_p(B)-t dB^{-1}\pmod p.
\]
Here \(B\) is a unit and \(d\ne0\pmod p\), so \(f_\varepsilon(x_t)\) fails to be primitive modulo \(p^2\) at exactly one parameter, \(t=t_2\). If these two forbidden parameters differ, precisely \(p-2\) of the \(p\) lifts work; if they coincide, precisely \(p-1\) work. This proves \(M_{p,2,\varepsilon}(a)=p-2+\delta_{p,\varepsilon}(a)\).

**3. Every higher prime power.** Each qualifying residue modulo \(p^2\) has exactly \(p^{k-2}\) lifts modulo \(p^k\). The primitive-root criterion in step 1, applied to \(x\) and to \(f_\varepsilon(x)\), shows that *every* such lift works. Conversely, every simultaneous primitive pair modulo \(p^k\) must reduce to a qualifying pair modulo \(p^2\). This establishes the exact formula and the total count, without any asymptotic argument.

**4. Full existence and exceptions.** Corollary 2(i) and (ii) of Cohen--Oliveira e Silva--Sutherland--Trudgian guarantees \(G_+(p)\ne\varnothing\) for all odd primes except the candidate exceptions \(3,5,7,13\), and \(G_-(p)\ne\varnothing\) for all odd primes except \(3,5,13,61\). Direct evaluation of the primitive elements modulo each of those small primes shows that the relevant \(G_\varepsilon(p)\) is empty. For \(p=3,5,7,13,61\), the respective counts \((|G_+(p)|,|G_-(p)|)\) are \((0,0),(0,0),(0,1),(0,0),(4,0)\); the nonzero cases at \(7,61\) are not exceptions for the corresponding sign. For every nonexceptional prime \(p\ge7\), step 2 gives at least \(p-2>0\) successful first lifts per seed, and step 3 propagates them to every \(k\ge2\). At \(k=1\) the cited finite-field classification applies. If the residue-field set is empty, reduction modulo \(p\) rules out any higher-power solution. Both parts of the stated conjecture follow.

## Verification
Run `python3 artifacts/verify.py` with Python 3.8 or later and no external packages. It verifies all prime-square fibers for the 22 primes from 7 through 97 specified in the program, all residue-field admissible seeds, and the full global counts. For prime cubes at \(p\in\{7,11,17,19,23\}\), it checks each seed fiber against direct enumeration. Both values of the coincidence indicator occur in the computations (notably for \(p=59\)). This finite evidence is a reproducibility check, not a substitute for the proof for unbounded \(p,k\).

## Relationship to prior work
Sun posed the prime-power existence statement as Conjecture 4.10 in *New observations on primitive roots modulo primes*. The 2018 finite-field result of Cohen, Oliveira e Silva, Sutherland and Trudgian determines when \(x\) and \(x\pm x^{-1}\) can both be primitive **in a finite field**. Taking a field with \(p^k\) elements is not the same as working in the ring modulo \(p^k\). The present result supplies the missing local lift step and the exact per-seed multiplicity, sharpening existence to a complete lifting count. Carella's *Simultaneous Primitive Roots over Finite Rings* studies primitivity of the same integer across the levels \(p\) and \(p^2\), averaged over primes, rather than simultaneous primitivity of the reciprocal Laurent values at a fixed prime.

## Limitations
The exact count depends on the finite-field seed set \(G_\varepsilon(p)\); no closed arithmetic expression for its cardinality is claimed. The precise value of \(\delta\) can vary by seed, and is supplied as a test rather than a prime-only closed formula. This theorem does not address the least positive simultaneous primitive root, short intervals, primes dividing a fixed input, or odd-polynomial maps with vanishing derivative. The finite-field existence classification is invoked from published work; its proof is not reproduced here. As with any historically scoped originality comparison, an unindexed earlier prime-power result remains possible.

## References
1. Zhi-Wei Sun, *New observations on primitive roots modulo primes*, arXiv:1405.0290 (first posted 2014-04-21; Conjecture 4.10 in the accessible 2020 revision), https://arxiv.org/abs/1405.0290 .
2. Stephen D. Cohen, Tomás Oliveira e Silva, Nicole Sutherland and Tim Trudgian, *Linear combinations of primitive elements of a finite field*, arXiv:1711.06392, Corollary 2 (initial arXiv posting 2017-11), https://arxiv.org/abs/1711.06392 .
3. N. A. Carella, *Simultaneous Primitive Roots over Finite Rings*, arXiv:2501.10399 (2025), https://arxiv.org/abs/2501.10399 .
