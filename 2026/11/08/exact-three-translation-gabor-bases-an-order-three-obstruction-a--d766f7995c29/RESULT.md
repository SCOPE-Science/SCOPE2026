# Exact three-translation Gabor bases: an order-three obstruction and a phase-count formula

## Finding

Fix integers \(M\ge1\), \(N=3M\), a nonzero translation \(k\in\{1,\ldots,N-1\}\), and a phase-alphabet size \(q\ge2\). Put \(d=\gcd(N,k)\), \(t=N/d\), and \(\mu_q=\{e^{2\pi i a/q}:0\le a<q\}\). For \(\gamma\in\mu_q^N\), let \(g(j)=\gamma_j/\sqrt N\). Define the critical three-translation Gabor family

\[
\mathcal G(\gamma,k)=\bigl\{M_{3m}T_{ak}g:\ 0\le m<M,\ a\in\{0,1,2\}\bigr\},
\]

where \((T_{ak}g)(j)=g(j-ak)\) and \((M_{3m}g)(j)=e^{2\pi imj/M}g(j)\), with arguments interpreted modulo \(N\).

**Classification.** This family is an orthonormal basis of \(\mathbb C^N\) precisely for the following number of labelled phase windows:

\[
\#\{\gamma\in\mu_q^N:\mathcal G(\gamma,k)\text{ is orthonormal}\}
=\begin{cases}
6^d q^M,&3\mid t\text{ and }3\mid q,\\
0,&\text{otherwise}.
\end{cases}
\]

With the additional normalization \(\gamma_0=1\), the positive count is \(6^d q^{M-1}\). Thus the translation order must be divisible by three, and a phase alphabet works exactly when it contains a primitive cube root of unity. For unrestricted unit-circle phases in place of \(\mu_q\), the solution space is empty for \(3\nmid t\); otherwise it is a disjoint union of exactly \(6^d\) connected components, each homeomorphic to the \(M\)-torus \(\mathbb T^M\).

## Assumptions and scope

The modulation set is the subgroup \(3\mathbb Z_N\) of order \(M\); the translation set consists of \(0,k,2k\), with no assumption that it is a subgroup. The entries of \(g\) have constant modulus \(N^{-1/2}\). These assumptions give exactly \(N\) labelled vectors in the Gabor system. The count concerns windows with labelled coordinates, not equivalence classes under translations or conjugation. Normalizing a single phase divides the positive count by \(q\). The continuous statement does not impose any phase quantization.

## Proof

**Step 1: three-by-three Fourier fibers.** For a fixed residue \(j\in\mathbb Z_M\), define the three-row array

\[
H_j(a,s)=\gamma_{j+sM-ak},\qquad a,s\in\{0,1,2\}.
\]

Taking all differences of the \(M\) modulation indices and using Fourier inversion on \(\mathbb Z_M\) shows that \(\mathcal G\) is orthonormal if and only if \(H_jH_j^*=3I_3\) for every \(j\). In fact, the inner product of two Gabor vectors with translation indices \(a,b\) and modulation difference \(m\) is

\[
\frac1N\sum_{j=0}^{M-1}e^{2\pi imj/M}
\sum_{s=0}^{2}\gamma_{j+sM-ak}\overline{\gamma_{j+sM-bk}}.
\]

For \(a=b\), the inner fiber sum equals three; for \(a\ne b\), vanishing of all Fourier coefficients is equivalent to vanishing of each fiber sum. Since there are \(N\) unit vectors in \(\mathbb C^N\), orthonormality is equivalent to being a basis.

**Step 2: translation cycles force period three.** Choose \(j\) and consider the nonzero row vectors

\[
v_h=(\gamma_{j+sM-hk})_{s=0}^{2}\in\mathbb T^3,\qquad h\in\mathbb Z.
\]

For every integer \(h\), the vectors \(v_h,v_{h+1},v_{h+2}\) are pairwise orthogonal. Indeed, shifting the base residue by \(-hk\) changes only the common order of the three fiber coordinates. Thus \(v_{h+3}\) and \(v_h\) span the same one-dimensional orthogonal complement of \(\operatorname{span}(v_{h+1},v_{h+2})\):

\[
[v_{h+3}]=[v_h],
\]

where brackets denote a complex projective line. Moreover \(v_{h+t}=v_h\), since \(t\) is the order of \(k\) in \(\mathbb Z_N\). If \(3\nmid t\), the two periods would identify two consecutive distinct orthogonal projective lines. This contradiction proves nonexistence for all constant-modulus phase alphabets when \(3\nmid t\).

Assume henceforth \(3\mid t\). Elementary gcd arithmetic then gives \(d=\gcd(M,k)\) and \(\ell=M/d=t/3\). The action \(j\mapsto j-k\) on \(\mathbb Z_M\) has \(d\) orbits, each of length \(\ell\). For one orbit choose \(j\), and retain the \(\ell\) independent vectors \(v_0,\ldots,v_{\ell-1}\). Since \(\ell k/M=k/d\) is an integer not divisible by three, translation by \(\ell k\) cyclically permutes the three coordinates by a nontrivial three-cycle \(P\), and

\[
v_{h+\ell}=Pv_h.
\]

**Step 3: the six projective choices on each orbit.** Write \(\omega=e^{2\pi i/3}\).

If \(3\mid\ell\), projective period three gives \([Pv_h]=[v_h]\). The three projective lines of a valid consecutive triple are therefore the three distinct eigenlines of the coordinate three-cycle \(P\), represented by \((1,\omega^a,\omega^{2a})\), \(a=0,1,2\). There are exactly \(3!=6\) ways to place these lines at the three residue classes of \(h\bmod3\).

If \(3\nmid\ell\), the relation \([Pv_h]=[v_{h+\ell}]\), together with period three, makes \(P\) act transitively on the three orthogonal projective lines. Thus the first vector \(v=(1,A,B)\), normalized in its first coordinate, has mutually orthogonal cyclic shifts. Its correlation equation is

\[
\overline A+A\overline B+B=0.
\]

Three unit complex numbers sum to zero only when they are a common phase multiple of \(1,\omega,\omega^2\). Their product here is one, so the common phase is itself a cube root of unity. Consequently the complete list of six normalized solutions is

\[
(1,1,\omega),\ (1,1,\omega^2),\ (1,\omega,1),\ (1,\omega,\omega),\ (1,\omega^2,1),\ (1,\omega^2,\omega^2).
\]

Each determines all three projective lines, whose order is forced by \(\ell\bmod3\) and the action of \(P\). Conversely each of the six choices gives three mutually orthogonal cyclic shifts, hence valid consecutive triples. The six alternatives remain distinct even with unrestricted circle phases.

**Step 4: exact count and topology.** Every projective vector \(v_h\) in an orbit has a unique representative whose first coordinate is one. Each of the \(\ell\) retained vectors can independently be multiplied by any scalar in \(\mu_q\), giving \(q^\ell\) possibilities per projective pattern. The projective patterns from either case require \(\omega\), and so exist over \(\mu_q\) exactly when \(3\mid q\). Different residue orbits determine disjoint coordinates of \(\gamma\); hence each of the \(d\) orbits contributes \(6q^\ell\) choices, producing \((6q^\ell)^d=6^dq^M\) windows. Division by \(q\) after setting \(\gamma_0=1\) is free because global phase multiplication has no fixed point except the identity. In the unrestricted unit-circle case, each discrete projective pattern has exactly \(\ell\) freely varying circle phases. Distinct patterns cannot connect continuously, giving \(6^d\) disjoint copies of \(\mathbb T^{d\ell}=\mathbb T^M\). This proves every assertion.

## Verification

The standalone `CHECK.py` uses no external packages. Its independent exhaustive test enumerates all globally normalized phase arrays in 44 small parameter cases, totaling 15,773,391 candidate arrays, checking the exact cube-root cancellation condition. It also generates 7,488 valid windows at larger parameters using the orbit construction, exhaustively checks constructive bijections in six small cases, and assembles and checks 124 full complex Gabor synthesis Gramians separately from the fiber test. Run with `python CHECK.py` in the directory containing this result.

Illustrations: for \(N=6,q=3\), the normalized window counts at steps \(k=1,2,3\) are respectively \(18,108,0\). At \(N=12,q=3\), step \(k=1\) has \(162\) normalized windows, while step \(k=4\) has \(34{,}992\).

## Relationship to prior work

Asipchuk, De Carli and Rodriguez, *Block-equivalent finite Gabor frames* (arXiv:2605.16139, publicly posted May 15, 2026), prove general subgroup-based frame-operator block structure. That result motivates inspecting critical systems with a modulation subgroup; it does not classify the phase windows for a prescribed three-translation pattern or give the exact existence, counting and component statements above. The local three-dimensional complex-Hadamard and circulant-perfect-sequence ingredients are standard and are not independently claimed as new. Hiranandani and Schlenker (arXiv:1311.5390, Sections 1 and 3) treat circulant Butson matrices, which inform the local case but do not impose or enumerate the global translation-cycle consistency. Nicola (arXiv:2305.02738) classifies extremally time-frequency-localized Gabor bases under a different optimization condition.

## Limitations

Only the specified critical three-translation pattern, subgroup modulation lattice and constant-magnitude windows are classified. No assertion is made about arbitrary three-element translation sets, amplitude-variable windows, perturbation stability or noncritical systems. The local Hadamard ingredient is classical. Although relevant literature and indexed mathematical records were searched, an unindexed older statement with the same full count or a reduction from a broader classification remains a publication-priority risk. Independent mathematical audit has not been performed.

## References

1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139 (2026), https://arxiv.org/html/2605.16139v2 ; initial posting https://arxiv.org/abs/2605.16139 .
2. G. Hiranandani and J.-M. Schlenker, *Small circulant complex Hadamard matrices of Butson type*, arXiv:1311.5390 (2013/2014), https://arxiv.org/html/1311.5390v4 .
3. F. Nicola, *Maximally localized Gabor orthonormal bases on locally compact Abelian groups*, arXiv:2305.02738 (2023), https://arxiv.org/abs/2305.02738 .
4. A. Iosevich, M. Kolountzakis, Yu. Lyubarskii, A. Mayeli and J. Pakianathan, *On Gabor orthonormal bases over finite prime fields*, arXiv:1712.09120 (2017), https://arxiv.org/abs/1712.09120 .
