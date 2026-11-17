# The 143-site temporal-eleven resonance in cyclic Rule 30

## Finding

For every integer \(n\ge3\), let \(F_n\) be synchronous elementary binary cellular automaton Rule 30 on the **indexed** cyclic ring \(\mathbb Z/n\mathbb Z\):
\[
(F_n(x))_i=x_{i-1}\mathbin{\mathrm{xor}}(x_i\mathbin{\mathrm{or}}x_{i+1}),
\qquad x_i\in\{0,1\}.
\]
Write \(C_{11}(n)\) for the number of distinct *temporal* orbits of least period eleven, where spatial translations of a configuration are **not** identified. Then
\[
\boxed{C_{11}(n)=13\mathbf 1_{143\mid n}+25\mathbf 1_{275\mid n}.}
\]
In particular, least temporal period eleven occurs **if and only if** the ring circumference is divisible by \(143\) or by \(275\); the smallest such circumference is \(143\). The only possible primitive spatial periods of an eleven-periodic configuration are \(143\) and \(275\). At the least circumference \(143\), exactly \(143\) labelled configurations form \(13\) distinct temporal eleven-cycles. At circumference \(275\), the corresponding numbers are \(275\) and \(25\). At circumferences divisible by both, the temporal eleven-cycle count is \(38\).

The complete fixed-point formula is
\[
\#\operatorname{Fix}(F_n^{11})
=1+2\mathbf 1_{2\mid n}+143\mathbf 1_{143\mid n}+275\mathbf 1_{275\mid n}.
\]
This refines the specifically reported \(275\)-cell requirement for temporal period eleven in the 2002 book *A New Kind of Science* (page 268): a verified \(143\)-cell pattern gives a smaller example. The statement concerns the standard cyclic Rule 30 convention and **exact temporal return**, not return up to spatial translation.

## Assumptions and scope

The sites are labelled, with periodic boundary conditions, simultaneous updates, and the stated Wolfram Rule 30 local Boolean formula. \(n\ge3\) ensures three distinct spatial neighborhood sites. A configuration has primitive temporal period eleven exactly when \(F_n^{11}(x)=x\) and \(F_n(x)\ne x\), because eleven is prime. Spatial primitive period is the smallest positive cyclic shift preserving the configuration. The rule acts on finite rings; no claim about aperiodic infinite configurations or general long-time complexity is made.

## Proof

**1. Time-column equivalence.** For an arbitrary ring state satisfying \(F_n^{11}(x)=x\), define an eleven-bit column for each site:
\[
u_i=\sum_{t=0}^{10}(F_n^t(x))_i2^t.
\]
Let \(M=2^{11}-1\), let \(\sigma(u)=(u\mathbin{\mathrm{shr}}1)\mathbin{\mathrm{or}}((u\mathbin{\mathrm{and}}1)2^{10})\) be cyclic forward-time rotation (least significant bit encodes time zero), and let \(\oplus\) mean bitwise xor. From the local update at every time residue,
\[
u_{i-1}=\sigma(u_i)\oplus(u_i\mathbin{\mathrm{or}}u_{i+1}).
\]
Thus, if \(a=u_i\) and \(b=u_{i+1}\), the leftward spatial step is the deterministic function
\[
T(a,b)=(\sigma(a)\oplus(a\mathbin{\mathrm{or}}b),a)
\quad\text{on }\{0,\ldots,M\}^2.
\]
Conversely, an indexed closed walk of length \(n\) under \(T\) gives compatible eleven-bit columns; their time-zero bits define \(x\) and the same local identities ensure that \(F_n^{11}(x)=x\). This construction is a bijection, including the spatial starting index; no quotient is taken. Consequently, \(\#\operatorname{Fix}(F_n^{11})=\#\operatorname{Fix}(T^n)\).

**2. Complete finite certificate.** The \(2^{22}=4,194,304\) states of \(T\) were exhausted. The finite functional graph has *exactly one* directed cycle of each length
\[
1,\quad2,\quad143,\quad275,
\]
and no other recurrent cycles. Precisely \(421\) pair states are recurrent; the other \(4,193,883\) feed into these cycles. Both exhaustive methods and the full transition formula are supplied: `cycle_walk.cpp` traverses every functional component, and `indegree_certificate.cpp` instead computes every indegree, removes all indegree-zero vertices, and counts the residual cycles. Both reproduce the exact four-cycle-length multiset. This is an exhaustive finite certificate, not an inference from small-ring samples.

**3. Return and primitive period.** A directed cycle of spatial length \(d\) in \(T\) contributes exactly \(d\) indexed ring configurations if \(d\mid n\), otherwise none. The length-one cycle corresponds to the all-zero time-independent configuration, and the length-two cycle to the two spatially alternating, time-independent configurations (present only for even \(n\)). Hence
\[
\#\operatorname{Fix}(F_n)=1+2\mathbf1_{2\mid n}.
\]
The two longer spatial cycles are not time-independent, and a configuration fixed by the eleventh iterate has least temporal period either one or eleven. Subtracting the fixed states therefore yields
\[
\#\{x:\operatorname{leasttemporalperiod}(x)=11\}
=143\mathbf1_{143\mid n}+275\mathbf1_{275\mid n}.
\]
Every temporal orbit contains exactly eleven indexed states, so dividing by eleven proves the displayed formula for \(C_{11}(n)\). The primitive spatial periods are exactly the cycle lengths \(143\) and \(275\).

**4. Explicit independent witnesses.** The plain text `cycle_walk_output.txt` gives complete minimal-rotation representatives `witness_143` and `witness_275`. The program `direct_witness.py` independently updates each binary ring by the original three-site rule eleven times, verifies the first return occurs at update eleven, and checks spatial primitiveness against all proper divisors. Its recorded output reports \(73\) black cells for the \(143\)-site witness and \(137\) for the \(275\)-site witness. The \(143\)-site string is therefore a self-contained concrete counterexample to a purported requirement of \(275\) sites.

## Verification

Compile and run the two standalone C++17 programs in this directory:

```text
g++ -O2 -std=c++17 cycle_walk.cpp -o cycle_walk
./cycle_walk > cycle_walk_output.txt
g++ -O2 -std=c++17 indegree_certificate.cpp -o indegree_certificate
./indegree_certificate > indegree_output.txt
python3 direct_witness.py > direct_witness_output.txt
```

The three outputs are embedded alongside the sources. Both C++ programs enumerate the full \(4,194,304\)-state profile space by structurally different algorithms; `direct_witness.py` uses only the original ring map and the provided witness strings. The asserted complete recurrent multiset is \(\{1:1,2:1,143:1,275:1\}\). Hashes and byte counts of all artifacts appear in the containing file record. Independent mathematical audit has not been performed.

## Relationship to prior work

Wolfram, *A New Kind of Science* (2002), page 268 and its preceding exposition on page 267, directly studies short temporal repetition for Rule 30 and presents a \(275\)-site block for period eleven. Its caption says a block of \(275\) cells is required. The verified smaller \(143\)-site block and complete all-circumference orbit formula go beyond that statement; the mathematical conclusion does not rely on attributing a particular intent to the caption beyond its words. The same book credits systematic enumeration of Rule 30's shorter periodic patterns. Those older short-period results are prior work, not claimed as new here.

Ian Coleman's 2011 finite-width survey concentrates on eight-site automata and does not give an eleven-periodic all-width census. The online catalogue of repeating Rule 30 patterns maintained by Frans Faase includes larger examples, but its JavaScript-only tables could not be completely examined in the accessible text. This is a genuine residual historical-priority risk, especially for the mere existence of an individual \(143\)-site word. The all-width four-cycle functional-graph census, exact orbit counts, and exhaustive proof remain distinct mathematical assertions. Published mathematical-record searches for Rule 30, eleven-periodic blocks, spatial periods \(143\)/\(275\), and equivalent transfer descriptions found no result proving these assertions; search non-detection does not establish global priority. Related known exact results on Rule 30 one-step images and inverse degrees concern different objects and do not imply temporal-eleven recurrence.

## Limitations

This classifies **only** primitive temporal period eleven and time-eleven fixed points, not every possible temporal period of Rule 30. The proof is exhaustive for the finite time-column graph of size \(2^{22}\); the explicit code supplies a replayable finite certificate. Some historical catalogues are partially inaccessible, and historical novelty is therefore best-knowledge rather than certified uniqueness. No independent external audit has occurred. The statement on the \(275\)-cell caption should be read narrowly as a comparison to the *minimum spatial block size under exact temporal recurrence*; it is not an assertion that the \(275\)-cell pattern shown in prior work is invalid.

## References

1. Stephen Wolfram, *A New Kind of Science*, Wolfram Media, published 2002-05-14, pp. 267–268, ISBN 978-1-57955-008-0. Full relevant chapter: https://files.wolframcdn.com/pub/www.wolframscience.com/nks/nks-ch6.pdf . Page transcript: https://www.wolframscience.com/nks/p268--special-initial-conditions/ .
2. Ian Coleman, *Finite-Width Elementary Cellular Automata*, 2011-05-15, https://www.whitman.edu/documents/Academics/Mathematics/SeniorProject_IanColeman.pdf .
3. Frans Faase, *Repeating Rule 30 patterns* (catalogue begun 2003, archived 2013), https://www.iwriteiam.nl/Rule30.html and https://web.archive.org/web/20130808012847/http://www.iwriteiam.nl/Rule30.html .
4. Johan Kopra, *Cellular Automata with Complicated Dynamics*, University of Turku, 2019, https://www.utupub.fi/handle/10024/148471 . Historical context; not an archival scope anchor.
