# Exact three-deletion descendant counts for finite Thue–Morse words

## Finding

Let \(T_m\) be the length-\(n=2^m\) binary Thue–Morse word \(\mu^m(0)\), where \(\mu(0)=01\) and \(\mu(1)=10\). For each integer \(m\ge2\), the number \(D_3(T_m)\) of distinct linear binary words obtainable by deleting exactly three symbols (not necessarily consecutive) is 
\[
D_3(T_m)=\begin{cases}\dfrac{(2n-5)(2n^2-n+26)}{81},&m\text{ even},\\[4pt]\dfrac{2(n-2)(n+1)(2n-1)}{81},&m\text{ odd}.\end{cases}
\] Hence \(D_3(T_m)/\binom{2^m}{3}\to8/27\).

The first values at \(m=2,3,4,5,6\) are \(2,20,174,1540,12382\). The even/odd split is substantive: the lower-degree coefficients differ with the substitution depth parity.

## Assumptions and scope

All strings are *linear*, with fixed left and right endpoints; they are not circular words or necklaces. Deletion positions are three distinct indices and their order is immaterial. Repeated deletion patterns giving the same surviving word count only once. The alphabet is \(\{0,1\}\). The theorem holds for every integer \(m\ge2\) and no other source family is asserted. The source \(T_m\) is defined directly by the binary morphism in the claim.

## Proof

**Unique greedy embeddings.** Fix any binary word \(w\) and a subsequence \(v\). Among its embeddings as a subsequence choose the lexicographically earliest increasing index tuple. The tuple is unique. Immediately before each saved letter \(a\), all skipped letters since the previous saved letter are different from \(a\); otherwise the chosen occurrence of \(a\) could be moved earlier. Conversely, any keep/delete pattern satisfying this rule gives the earliest embedding of its output. Thus legal patterns of exactly three deletions are in bijection with *distinct* three-deletion descendants.

**Four-state weighted automaton.** Let \(s\in\{0,1,2,3\}\) be a two-bit mask of the alphabet symbols skipped since the last retained symbol: \(0\) means nothing skipped, \(1\) means a skipped zero, \(2\) a skipped one, \(3\) both. Reading symbol \(a\), set \(b(0)=1\), \(b(1)=2\). A deletion moves \(s\) to \(s\mathbin{\mathrm{OR}}b(a)\) with weight \(z\). A keep is allowed only if \(s\mathbin{\mathrm{AND}}b(a)=0\), then moves to state \(0\) with weight \(1\). Let \(M_a(z)\) be this \(4\times4\) transition matrix. In the truncated ring \(\mathbb Q[z]/(z^4)\),

\[ D_3(w)=[z^3]\,e_0^\mathsf{T}\bigl(\prod_{a\text{ in }w}M_a(z)\bigr)\mathbf 1. \]

Here \(e_0\) is the first standard basis vector and \(\mathbf 1\) the four-ones column. Keeping all terminal states permits arbitrary deleted suffixes.

**Morphisms and exact certificate.** Put \(A_m=M_{T_m}\) and \(B_m=M_{\overline{T_m}}\). The morphism gives \(A_{m+1}=A_mB_m\), \(B_{m+1}=B_mA_m\). Let \(P\) exchange mask states \(1\) and \(2\); then \(B_m=PA_mP\), so \(A_{m+1}=A_mPA_mP\). The file `tm3_coefficients.json` contains the \(4\) truncated powers of \(z\), each a \(4\times4\) matrix of rational cubic polynomials in \(n\), one set for each parity of \(m\). Entries are stored as four numerator/denominator coefficient pairs in increasing degree of \(n\). Thus its evidence is finite and exact, rather than a fit extrapolated from examples.

`verify_tm3.py` proves the certificate for *every* \(m\ge2\) by checking the two base matrices \(m=2,3\) directly and all \(128\) rational polynomial matrix identities of the form

\[ A_{\mathrm{opposite}}(2n)=A_{\mathrm{parity}}(n)P A_{\mathrm{parity}}(n)P\pmod{z^4}. \]

Each identity is tested coefficientwise in both indeterminates over the rationals, not at finitely many chosen \(n\). This is an inductive proof covering all even and all odd depths. Extracting the coefficient of \(z^3\) from row zero and summing the four terminal columns gives \((4n^3-12n^2+57n-130)/81\) at even depth and \((4n^3-6n^2-6n+4)/81\) at odd depth. Factoring yields the stated formulas. Dividing by \(\binom n3\) proves the limit.

## Verification

The standalone verifier uses only Python 3 standard-library modules. Run `python3 verify_tm3.py` in a directory containing `tm3_coefficients.json`. It prints `VERIFY_OK` after checking exact base matrices, \(128\) polynomial-matrix coefficient identities, the closed-form output rows, *all* binary words through length eight against brute-force triple deletions, all literal Thue–Morse triple-deletion sets through \(m=5\), and an independent last-occurrence dynamic program through \(m=14\). Only the exact polynomial identities and bases establish the infinite theorem; finite checks are supplementary.

## Relationship to prior work

Sloane's 2002 deletion-code survey defines distinct deletion descendants and gives formulas for one- and two-deletion descendants (Section 5), plus a general extremal upper bound. Those results do not supply the exact three-deletion shadow of the Thue–Morse substitution iterates. Lejeune, Leroy and Rigo (2018) analyze multiplicities of scattered subsequences and the fixed-order \(k\)-binomial complexity of *factors* of the infinite Thue–Morse word. Their Theorem 6 counts equivalence classes of factors, which is not the support cardinality of the length-\(n-3\) subsequences of one fixed finite iterate.

## Limitations

No result is claimed for four or more deletions, arbitrary non-dyadic prefixes, or cyclic-output identification. The parity-specific polynomial matrix certificate is longer than the final scalar formula; its included rational data and independently replayable verifier are essential parts of the proof. An earlier equivalent special-case theorem could exist outside the inspected records; mathematical independence has not been certified.

## References

- N. J. A. Sloane, *On Single-Deletion-Correcting Codes* (first public posting 2002-07-22), arXiv:math/0207197, https://arxiv.org/html/math/0207197v1 ; Section 5.
- M. Lejeune, J. Leroy and M. Rigo, *Computing the k-binomial complexity of the Thue–Morse word* (first public posting 2018-12-18), arXiv:1812.07330, https://arxiv.org/pdf/1812.07330 ; Introduction, Sections 2–3 and Theorem 6.
