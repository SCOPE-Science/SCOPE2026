# The extremal dual norm in a continuous \(K\)-\(g\)-frame theorem is reciprocal

## Finding
Theorem 2.3 of Rahmani--Alizadeh correctly proves
\[
\|T_\Gamma\|^2\ge \frac1A
\]
for every dual of a c-\(K\)-\(g\)-frame with optimal lower bound \(A\), but then claims an extremal dual with
\[
\|T_\Theta\|^2=A.
\]
The correct extremal value is
\[
\inf_{\Gamma\ \mathrm{dual}}\|T_\Gamma\|^2=\frac1A.
\]
The error occurs when the proof identifies the optimal lower-bound supremum with a majorization infimum; those constants are reciprocal.

## Assumptions and scope
Assume the c-\(K\)-\(g\)-frame has a finite optimal lower bound \(0<A<\infty\). The correction concerns the extremal synthesis norm in Theorem 2.3. The reduced Douglas solution is uniquely normalized by the range/kernel conditions of the factorization theorem; no classification of all norm-minimizing duals is asserted.

## Proof
By optimality,
\[
A=\sup\{\lambda>0:\lambda\|K^*f\|^2\le\|T_\Lambda^*f\|^2\ \text{for all }f\}.
\]
Therefore the least \(\mu\) satisfying
\[
\|K^*f\|^2\le\mu\|T_\Lambda^*f\|^2
\]
for all \(f\) is \(1/A\). Douglas factorization gives a reduced operator \(\Phi\) with
\[
K^*=\Phi T_\Lambda^*,\qquad \|\Phi\|^2=\frac1A.
\]
The source's Theorem 2.2 defines a dual by \(\Theta_\omega f=(\Phi^*f)(\omega)\), so \(T_\Theta^*=\Phi^*\) and
\[
\|T_\Theta\|^2=\frac1A.
\]
For any dual \(\Gamma\), \(K^*=T_\Gamma T_\Lambda^*\), hence the source's lower estimate gives \(\|T_\Gamma\|^2\ge1/A\). Thus the reduced-solution dual attains the exact minimum.

For a direct counterexample, let the measure space have one point of mass one and set
\[
H=\mathbb C,\qquad K=I,\qquad \Lambda=\frac12I.
\]
Then \(A=1/4\). The dual equation \(I=\Lambda^*\Gamma\) forces \(\Gamma=2I\), so
\[
\|T_\Gamma\|^2=4=\frac1A,
\]
and no dual can have the printed value \(A=1/4\).

## Verification
The public preprint was inspected at the c-\(K\)-\(g\)-frame and dual definitions, the quoted Douglas lemma, Theorem 2.2, and the complete statement and proof of Theorem 2.3. The proof explicitly equates the lower-bound supremum with an infimum that is its reciprocal and then assigns that infimum to the squared norm of the reduced solution. The one-point counterexample is exact and uses no numerical approximation. The earliest verified public version is arXiv:2106.07230v1, dated 14 June 2021, and the source lists primary MSC \(42C15\).

## Relationship to prior work
The 2019 paper *Some Properties of Continuous \(K\)-g-Frames in Hilbert Spaces* gives the pair-dual factorization used by the 2021 source. Douglas's factorization theorem identifies the norm of the reduced solution with the least majorization constant. These ingredients support the reciprocal correction but do not make the published extremal value \(A\) valid. Targeted searches by theorem number, arXiv identifier, journal DOI, reciprocal norm formulation, and correction terminology did not locate an indexed correction containing this scalar counterexample.

## Limitations
The exact minimum synthesis norm is proved and attained by the reduced Douglas solution. The result does not classify every norm-minimizing dual and does not reassess unrelated later statements. An unindexed note may contain the same correction.

## References
1. M. Rahmani and E. Alizadeh, *Some points on c-\(K\)-g-frames and their duals*, arXiv:2106.07230v1, 14 June 2021; later published under DOI 10.1007/s40995-022-01263-z.
2. E. Alizadeh, A. Rahimi, E. Osgooei and M. Rahmani, *Some properties of continuous \(K\)-g-frames in Hilbert spaces*, U.P.B. Scientific Bulletin, Series A 81(3) (2019), 43--52.
3. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proceedings of the American Mathematical Society 17 (1966), 413--415.
