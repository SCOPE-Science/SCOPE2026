# Exact collision moments for cyclic elementary cellular automaton Rule 4

## Finding

For every integer \(n\ge3\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous nearest-neighbor Rule 4 update on a labelled cyclic ring:
\[
(F_nx)_i=x_i(1-x_{i-1})(1-x_{i+1}),\qquad i\in\mathbb Z/n\mathbb Z.
\]
Let \(X,X'\) be independent uniformly sampled ring configurations, and put
\[
M_n=\#\{(x,x')\in\{0,1\}^{2n}:F_n(x)=F_n(x')\}.
\]
The following exact and asymptotic identities hold:
\[
M_n=\operatorname{tr}(T^n),\qquad
\det(tI-T)=t^7(t^3-t^2+2t-1)(t^6-3t^5-t^3-2t^2+2t+2),
\]
where the explicit integer \(16\)-state transfer matrix \(T\) is defined below. The polynomial
\[
P(t)=t^6-3t^5-t^3-2t^2+2t+2
\]
has a unique root \(\Lambda>3\), with \(\Lambda=3.138990099335421\ldots\), and this root strictly dominates the moduli of all other roots of \(P\) and the cubic factor. Consequently,
\[
M_n\sim\Lambda^n,\qquad
\Pr(F_n(X)=F_n(X'))\sim(\Lambda/4)^n.
\]
Thus the collision probability decays with exact exponential base \(\Lambda/4=0.784747524833855\ldots\), and its Rényi-order-two entropy per site is \(\log(4/\Lambda)\).

There is also an exact formula in terms of a single scalar rational generating function. Define \(f_0=f_1=1\), \(f_2=2\), and \(f_j=2f_{j-1}-f_{j-2}+f_{j-3}\) for \(j\ge3\). Define
\[
G(z)=\sum_{j\ge0}f_j^2z^j
=\frac{1-2z+2z^2+2z^3-z^4-z^5}{(z^3-2z^2+z-1)(z^3+3z^2+2z-1)},\quad
H(z)=z^2+z^3G(z).
\]
Let \(g_n\) denote the number of cyclic binary words of length \(n\) avoiding \(010\); equivalently \(g_n=\operatorname{tr}(Z^n)\) for the \(4\)-state matrix \(Z\) below. For every \(n\ge3\),
\[
\boxed{M_n=g_n^2+n[z^n]\log\!\left(\frac1{1-H(z)}\right).}
\]
The singularity \(r=1/\Lambda\) is the unique positive solution of \(H(r)=1\) in the interval \((0,\lambda^{-2})\), where \(\lambda\) is the positive dominant root of \(t^3-2t^2+t-1\). In particular, \(\Lambda\) is equivalently specified by the sextic \(P\) without reliance on a numerical fit.

## Assumptions and scope

The ring is labelled, cyclic, and has \(n\ge3\) sites. Counts refer to ordered pairs of initial configurations, not to pairs of rotational equivalence classes. The local rule outputs one only on the neighborhood \(010\), and hence sends every configuration to an independent set of occupied sites; every such independent set is fixed, so \(F_n^2=F_n\). There are no higher-period trajectories. The invariant measured here is the second moment of the entire one-step fibre-size distribution, not the ordinary number of fixed points or the largest individual basin.

Define the four elementary pair symbols \(a=(a_0,a_1)\in\{0,1\}^2\). Index the \(16\) states of \(T\) by ordered pairs \((a,b)\) of such symbols. For each triple \((a,b,c)\), place an edge
\[
(a,b)\longrightarrow(b,c)
\]
with weight one precisely when
\[
b_0(1-a_0)(1-c_0)=b_1(1-a_1)(1-c_1).
\]
All other entries of \(T\) are zero, and weights add if edges coincide. Similarly index \(Z\) by binary pairs \((a,b)\in\{0,1\}^2\); its \((a,b)\to(b,c)\) transition has weight one exactly when \((a,b,c)\ne(0,1,0)\).

## Proof

**1. A paired de Bruijn transfer.** An ordered pair \((x,x')\) defines one cyclic sequence of paired binary symbols. Equality \(F_n(x)=F_n(x')\) holds if and only if every consecutive triple of paired symbols satisfies the defining edge condition of \(T\). Taking \(\operatorname{tr}(T^n)\) counts exactly these closed labelled length-\(n\) sequences, with each distinct starting site correctly retained. Thus \(M_n=\operatorname{tr}(T^n)\). The stated determinant follows by direct finite polynomial elimination from this fully specified \(16\times16\) matrix; the packaged symbolic checker independently constructs it and compares the determinant coefficient by coefficient. This finite determinant identity is exact for every \(n\), not an extrapolation from numerical spectra.

**2. Explicit fibres.** Each one in an output word is an isolated one in the input and fixes its two neighboring input bits to zero. Conversely, any input one without a neighboring input one survives; hence all input ones not forced by the output must occur in runs of length at least two. The fibre over the zero output is exactly the family of cyclic inputs avoiding \(010\), counted by \(g_n=\operatorname{tr}(Z^n)\). For an output with occupied positions separated by successive cyclic distances \(d_1,\ldots,d_k\ge2\) (with \(\sum d_j=n\)), the interior free segment of gap \(d_j\) has length \(\max(d_j-3,0)\), with no singleton-one run. The disjoint segments are independent. Hence
\[
\#F_n^{-1}(y)=\prod_{j=1}^k f_{\max(d_j-3,0)}
\]
for every nonzero output \(y\). This includes \(k=1\), when its single cyclic distance is \(n\).

**3. Regular-language recurrence.** A free segment is a binary word whose runs of ones all have length at least two; its ordinary generating function is
\[
\sum_{j\ge0}f_jz^j=\frac{1-z+z^2}{1-2z+z^2-z^3}.
\]
One obtains this by using the three automaton states 'currently zero', 'one pending', and 'run of at least two ones', accepting the first and last states. Its denominator yields the stated third-order recurrence and initial values. Squaring the recurrence's three root-exponential components shows that the sequence \(f_j^2\) satisfies a recurrence of order at most six. The resulting six characteristic roots are the three squares and three pairwise products of the roots of the original cubic. Matching the first six values \(1,1,4,16,49,144\) gives exactly \(G(z)\) as displayed; the symbolic verification program reproduces this rational identity and the next thirty coefficients directly.

**4. Cyclic spacings.** For nonzero independent outputs, a consecutive cyclic spacing of two has squared fibre weight one; a spacing of \(d\ge3\) has squared weight \(f_{d-3}^2\). Thus their spacing-weight series is \(H(z)\). For precisely \(k\) occupied sites, cyclic pointing at one occupied site gives \(n/k\) times the coefficient of \(z^n\) in \(H(z)^k\): the \(k\) choices of the pointer and the \(n\) labelled starting positions cancel as indicated. Summing \(k\ge1\) yields the nonzero-image contribution \(n[z^n]\sum_{k\ge1}H(z)^k/k\), establishing the boxed formula. The zero-image contribution is \(g_n^2\), independently of the other outputs.

**5. Sharp exponential law and constant.** The cubic \(t^3-2t^2+t-1\) has a strictly dominant positive root \(\lambda\), with \(\lambda=1.754877666\ldots\); the remaining two roots have modulus below \(\lambda\). Therefore \(f_j\) grows as a positive constant times \(\lambda^j\), and \(H(z)\) tends to infinity as \(z\uparrow\lambda^{-2}\). Since \(H(0)=0\), its coefficients are nonnegative and the coefficients at powers two and three are strictly positive, there is a unique \(r\in(0,\lambda^{-2})\) with \(H(r)=1\). Positivity and the coprime support lengths two and three imply that this is the sole singularity on its circle of convergence, and \(H'(r)>0\). Hence
\[
\log\!\frac1{1-H(z)}=-\log(1-z/r)+A(z),
\]
where \(A\) is analytic on a disc of radius greater than \(r\). It follows by coefficient extraction that the nonzero-image moment contribution is \(r^{-n}+o(r^{-n})\), with **leading constant exactly one**. The four-state matrix has characteristic polynomial \(t(t^3-2t^2+t-1)\), so \(g_n=O(\lambda^n)\). Because \(r<\lambda^{-2}\), its square is negligible: \(g_n^2=o(r^{-n})\). Thus \(M_n\sim r^{-n}\). Finally,
\[
1-H(z)=\frac{2z^6+2z^5-2z^4-z^3-3z+1}{(z^3-2z^2+z-1)(z^3+3z^2+2z-1)}.
\]
Substituting \(z=1/t\) in the numerator and multiplying by \(t^6\) gives \(P(t)\). A root of maximum modulus is \(r^{-1}\), as follows from the same positive-coefficient argument and the exact transfer characteristic factorization.

## Verification

The included standalone `verify_bruteforce.py` enumerates all labelled binary inputs for every ring length from three through sixteen, reconstructs all fibres directly, independently counts the constrained free segments, and checks their product formula. The independent `verify_transfer.py` constructs \(T\) and \(Z\), proves their characteristic polynomial identities by exact symbolic arithmetic, computes the rational squared-segment series, and compares transfer-matrix traces with cyclic-renewal counts through ring length thirty-six. Their actual captured outputs are included. For example, the moments for lengths three through eight are respectively \(28,106,314,948,2986,9434\). All listed checks passed. The proof for arbitrary ring length rests on the combinatorial decomposition and finite symbolic matrix identity, not on finite enumeration alone.

## Relationship to prior work

General one-step preimage formulae, including explicit Rule 4 formulae on a linear infinite lattice, were already derived by E. Jen (1989), whose full text and Rule 4 appendix were examined. Jen also investigated ordinary Shannon spatial measure entropy and other distributional statistics; those contributions are not claimed here. H. Fukś's work on preimage sequences and rule emulation provides further context but does not state the ring-wide squared-fibre sum above. Koller and Hudcová (2025) use transfer matrices for counts of trajectories entering attractors; the inspected full text addresses the cardinality of specified transient/attractor classes, not the probability that two independent inputs coalesce to the identical output. The present contribution is the exact *second fibre moment on finite cyclic rings*, its cancellation-free recurrence and its algebraic collision-entropy rate, which do not follow as a stated special case of those cited results. Generic de Bruijn transfer matrices are standard; the mathematical content lies in the explicit Rule 4 evaluation and its quantitative collision law.

## Limitations

No claim is made that the elementary preimage method or transfer-matrix method is new. This is an exact theorem for Rule 4 and uniform binary inputs on labelled rings; it does not classify collision statistics of other rules or nonuniform inputs. A related 1988 article by Jen on cylindrical cellular automata could not be inspected in full, creating an unresolved historical-priority risk; it was available only through bibliographic descriptions, and institutional access was unavailable. An unindexed equivalent second-moment result could also exist. The asymptotic is not a statement about Shannon entropy or about eventual equality of trajectories at different times (the update is idempotent, so those questions coincide after one update).

## References

1. Stephen Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics 55 (1983), 601–644; doi:10.1103/RevModPhys.55.601. Published 1983-07-01.
2. Erica Jen, *Scaling of Preimages in Cellular Automata*, Complex Systems 1 (1987); https://www.complex-systems.com/abstracts/v01_i06_a02/.
3. Erica Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems 3 (1989), 421–456; https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf. Especially the Rule 4 appendix and the spatial-measure-entropy section.
4. Erica Jen, *Cylindrical cellular automata*, Journal of Statistical Physics (1988); doi:10.1007/BF01221109. Only bibliographic material inspected.
5. Henryk Fukś, *Sequences of Preimages in Elementary Cellular Automata*, Complex Systems 14 (2003), 29–42; https://doi.org/10.25088/ComplexSystems.14.1.29; later arXiv:1305.6533 (2013-05-28).
6. Cédric Koller and Barbora Hudcová, *Counting Short Trajectories in Elementary Cellular Automata using the Transfer Matrix Method*, arXiv:2508.09768 (2025-08-13), https://arxiv.org/pdf/2508.09768.
