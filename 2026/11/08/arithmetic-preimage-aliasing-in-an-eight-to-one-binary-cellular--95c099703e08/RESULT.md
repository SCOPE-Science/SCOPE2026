# Arithmetic preimage aliasing in an eight-to-one binary cellular automaton

## Finding
For the five-neighbor binary cellular automaton below, the number of cyclic predecessors of constant zero, constant one, and alternating output words is an exact function of ring length. The alternating word has no predecessor on any ring whose length is not divisible by 16, and exactly eight predecessors otherwise. At the smallest admissible length, all eight predecessors have primitive spatial period 16, an eight-fold inflation of the target's period two.

For every integer \(N\ge1\), the exact counts are
\[
\#F_N^{-1}(0^N)=\begin{cases}8&6\mid N,\\2&6\nmid N,\end{cases}\qquad
\#F_N^{-1}(1^N)=\begin{cases}8&6\mid N,\\2&2\mid N,\ 6\nmid N,\\0&2\nmid N,\end{cases}
\]
and, when \(N\) is even,
\[
\#F_N^{-1}((01)^{N/2})=\begin{cases}8&16\mid N,\\0&16\nmid N.\end{cases}
\]
The other phase of the alternating output has the same count by shift equivariance.

## Assumptions and scope
Arithmetic takes place in \(\mathbb F_2\), and the ring is indexed by \(\mathbb Z/N\mathbb Z\). Define \(F_N:\mathbb F_2^N\to\mathbb F_2^N\) by
\[
(F_Nx)_i=x_i+x_{i+3}+x_{i+1}(1+x_{i+2})x_{i+4}.
\]
This is the explicit eight-to-one locally eventually onto, non-bipermutive diameter-five rule in Appendix B of Haugland–Larsen–Omland–Rustad (2026). The cyclic map is meaningful for every positive \(N\), even when different neighborhood positions coincide. The theorem is about **one-step spatial inverse images**, not temporal cycles of the cellular automaton. An \(N\)-word is counted with a distinguished indexed origin, not modulo rotation.

## Proof
For \(t\in\{0,1\}\), construct a \(16\times16\) nonnegative integer matrix \(M_t\) indexed by binary four-words. For \(u=(a,b,c,d)\), \(v=(b,c,d,e)\), put
\[
(M_t)_{u,v}=\mathbf1\{a+d+b(1+c)e=t\},
\]
with all other entries zero. Every cyclic input word corresponds bijectively to a closed walk of length \(N\) in this de Bruijn graph, with edge labels the output bits in cyclic order. This correspondence also holds when \(N<5\), as the closed-walk condition enforces repeated cyclic indices. Therefore
\[
\#F_N^{-1}(0^N)=\operatorname{tr}(M_0^N),\quad
\#F_N^{-1}(1^N)=\operatorname{tr}(M_1^N),
\]
and, for \(N=2m\),
\[
\#F_N^{-1}((01)^m)=\operatorname{tr}((M_0M_1)^m).
\]
Direct exact-integer computation of the three explicitly specified characteristic polynomials gives
\[
\begin{aligned}
\chi_{M_0}(z)&=z^8(z-1)^3(z+1)(z^2-z+1)(z^2+z+1),\\
\chi_{M_1}(z)&=z^8(z-1)^2(z+1)^2(z^2-z+1)(z^2+z+1),\\
\chi_{M_0M_1}(z)&=z^8(z^8-1).
\end{aligned}
\]
An independent exact reconstruction of these characteristic-polynomial coefficients from integer traces via Newton's identities is supplied in `verify.py`; the script constructs every matrix directly from the five-bit local truth table, with no precomputed matrices or numerical eigenvalues. These finite matrix equalities are exhaustive, verifiable algebraic certificates, not extrapolations from a bounded range of ring lengths.

The trace of a positive power is the sum of that power of each eigenvalue, with algebraic multiplicities, whether or not the matrix is diagonalizable. The first two factorizations have six-root-of-unity nonzero spectra; their traces are respectively \(8\) at multiples of six and \(2\) otherwise, and \(8\) at multiples of six, \(2\) at other even positive powers, and \(0\) at odd powers. The third factorization has as its nonzero spectrum all eight eighth roots of unity, once each. Thus its positive-power traces equal \(8\) exactly at multiples of eight and otherwise vanish. Substitution into the closed-walk identities proves all formulas for all \(N\).

At \(N=16\), the alternating target has exactly eight distinct cyclic predecessors. If any such predecessor had proper period \(d\mid16\), then \(d\in\{1,2,4,8\}\); the same word repeated to length \(d\) would map to an alternating target on length \(d\), impossible by the already-proved count. Hence all eight have primitive period 16. In addition, shift by two sites permutes the eight predecessors transitively: an explicit output check for one witness and its seven even shifts, included in `verify.py`, verifies this last orbit description without affecting the count theorem.

## Verification
Run `python3 verify.py` from the extracted directory with Python 3 standard library only. The script reconstructs three characteristic polynomials using Newton identities, compares 384 exact matrix-power traces against the formulas, checks every cyclic input state through lengths one to 12 (8,190 words total), and enumerates all 65,536 words at length 16 to confirm the eight alternating predecessors and their primitive periods. The standalone replay prints `VERIFY_OK exact_charpolys=3 trace_powers=384 bruteforce_ring_states=8190 alternating_N16_preimages=8`. The all-length conclusions follow from the finite exact characteristic-polynomial identities and trace theorem, not the finite-state testing range.

## Relationship to prior work
Haugland, Larsen, Omland and Rustad (2026), Appendix B, introduce this exact local rule and establish its eight-to-one, locally eventually onto bi-infinite behavior. They do not give the present ring-length-dependent inverse counts or the sharp alternating-period inflation. Mariot, Leporati, Dennunzio and Formenti (2017), especially Section 3 and Lemma 6, establish a general de Bruijn/u-closure algorithm for computing spatial preimage periods and multiplicities. The matrix/closed-walk method here is an application of that existing framework, not a new general technique. The contribution is the explicit, all-ring arithmetic phase classification of this recently supplied nonlinear, non-bipermutive example, including the anomalous period-16 lift. General decidability alone does not state these arithmetic formulas.

## Limitations
This theorem concerns three distinguished periodic target families, not arbitrary target words, finite-ring image size, full shift preimage entropy, or temporal dynamics. It does not re-prove the motivating paper's bi-infinite eight-to-one and locally eventually onto results. The invariant is exact for every positive ring size, but it is one example among the listed eight-to-one rules. Historical priority is provisional and broader specialized classifications may supply equivalent information not located by the literature searches.

## References
1. J. K. Haugland, N. S. Larsen, T. Omland and H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1 (first posted 2026-10-23), Appendix B. https://arxiv.org/html/2610.33131v1
2. L. Mariot, A. Leporati, A. Dennunzio and E. Formenti, *Computing the periods of preimages in surjective cellular automata*, Natural Computing **16** (2017), 367–381, Section 3 and Lemma 6. https://lucamariot.org/files/papers/mldf_naco_2017_postprint.pdf
