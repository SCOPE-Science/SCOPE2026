# Exact dyadic Fourier rigidity of permutation peak-position counts

## Finding
For every integer \(n\ge 1\), let \(I_n=\{2,\ldots,n-1\}\) (empty when \(n\le2\)). For a permutation \(\pi\in\mathfrak S_n\), write \(P(\pi)=\{i\in I_n:\pi_{i-1}<\pi_i>\pi_{i+1}\}\). Define the counting function \(f_n(A)=\#\{\pi:P(\pi)=A\}\) on the finite Boolean group \(G_n=(\mathbb Z/2\mathbb Z)^{I_n}\), with multiplicities retained.

For every frequency \(S\subseteq I_n\), its **unnormalized** Walsh multiplier is
\[
\Lambda_n(S)=\sum_{A\subseteq I_n}f_n(A)(-1)^{|A\cap S|}=\sum_{\pi\in\mathfrak S_n}(-1)^{|P(\pi)\cap S|}.
\]
Writing \(v_2(k)\) for the exponent of \(2\) dividing a nonzero integer \(k\), the complete all-dimensional valuation statement is
\[
\boxed{v_2(\Lambda_n(S))=v_2(n!)\quad\text{for every }n\ge1,\ S\subseteq I_n.}
\]
In particular, no multiplier vanishes. Convolution by \(f_n\) on \(G_n\) is invertible, of rank \(2^{\max(n-2,0)}\) and nullity zero. Moreover the **exact greatest common divisor**, not necessarily the smallest multiplier magnitude, is
\[
\boxed{\gcd_{S\subseteq I_n}|\Lambda_n(S)|=2^{v_2(n!)}.}
\]
Thus \(|\Lambda_n(S)|\ge2^{v_2(n!)}\); equality in this lower bound is not claimed for each \(n\).

## Assumptions and scope
All permutations are uniformly weighted, with no restriction on peak positions other than being strictly interior. A frequency is an arbitrary subset of the interior positions, including the empty subset. For \(n=1,2\), \(G_n\) has one element and the multiplier equals \(n!\). Fourier transforms are unnormalized; the convolution operator is \((T_ng)(x)=\sum_{a\in G_n}f_n(a)g(x-a)\), where addition is coordinatewise modulo two. The result is an exact integer statement, not an assertion about approximate spectra, prescribed peak counts, or peak values.

## Proof
Let \(\mathbb Z_{(2)}=\{a/b\in\mathbb Q:b\text{ odd}\}\), the rational numbers with odd denominators. Let \(U_1,\ldots,U_n\) be independent continuous uniform random variables. Their relative order is uniformly distributed on \(\mathfrak S_n\). Put \(X_i=\mathbf1\{U_{i-1}<U_i>U_{i+1}\}\) for \(i\in I_n\), and let \(q(J)=\mathbb P(X_i=1\text{ for all }i\in J)\).

**Lemma (joint peak-event integrality).** For every \(J\subseteq I_n\), \(q(J)\in\mathbb Z_{(2)}\).

If \(J\) has two adjacent positions, \(q(J)=0\), since adjacent strict peaks are impossible. Otherwise partition \(J\) into maximal chains with successive positions two apart. A chain of \(r\ge1\) peaks forces an alternating up-down pattern on its \(2r+1\) consecutive variables. Its probability is \(c_r=E_{2r+1}/(2r+1)!\), where \(E_{2r+1}\) is the classical tangent (odd zigzag) number. Distinct chains have disjoint underlying variable windows: between different chains the last and first peak positions differ by at least three. Independence gives \(q(J)=\prod c_r\), with the empty product equal to one.

The classical exponential generating function is \(\tan z=\sum_{r\ge0}c_rz^{2r+1}\), with \(c_0=1\). Comparing coefficients in \((\tan z)'=1+(\tan z)^2\) yields for every \(r\ge1\)
\[
(2r+1)c_r=\sum_{a+b=r-1}c_ac_b.
\]
The inductive base \(c_0=1\) lies in \(\mathbb Z_{(2)}\), and only odd integers \(2r+1\) are divided out. Hence every \(c_r\), and so every \(q(J)\), lies in \(\mathbb Z_{(2)}\), proving the lemma.

Now expand the character product, with \(X_i\in\{0,1\}\):
\[
\frac{\Lambda_n(S)}{n!}
=\mathbb E\prod_{i\in S}(1-2X_i)
=\sum_{J\subseteq S}(-2)^{|J|}q(J)
\in1+2\mathbb Z_{(2)}.
\]
Every element of \(1+2\mathbb Z_{(2)}\) is a nonzero rational of numerator and denominator both odd in lowest terms. Therefore multiplying by \(n!\) gives the *exact* valuation \(v_2(\Lambda_n(S))=v_2(n!)\), without any enumeration cutoff. Walsh diagonalization on the finite Abelian group now proves invertibility and rank.

For the claimed exact gcd, the valuation theorem shows that every multiplier is divisible by \(2^{v_2(n!)}\), but not by its next power. Suppose that an odd prime \(p\) divided every multiplier. The Walsh matrix \(H\), indexed by subsets of \(I_n\), satisfies \(H^2=2^{|I_n|}I\). Because \(p\) is odd, \(H\) is invertible modulo \(p\), and hence \(p\) would divide every coefficient \(f_n(A)\). This contradicts
\[
f_n(\varnothing)=2^{n-1}.
\]
Indeed, a permutation without an interior peak must decrease to its minimum \(1\) and then increase; the \(n-1\) other labels can be chosen independently for the left or right side, after which their order is forced. Thus no odd prime divides all multipliers, completing the gcd proof.

## Verification
The accompanying standalone exact-arithmetic script `verify_peak.py` implements two distinct evaluations: a MacMahon multinomial Möbius-inversion formula for the entire descent-set distribution, followed by the peak map and Walsh transform; and an exact rational joint-peak-event calculation using the tangent recurrence, followed by subset zeta transform. It checks their equality for every frequency at \(1\le n\le13\), the nonvanishing and exact valuations, the gcd, and the peak-free count. It additionally compares with direct enumeration of all permutations for \(1\le n\le8\). All 12,442 assertions passed in the performed replay. These finite computations corroborate but are not used in the all-\(n\) proof.

## Relationship to prior work
Stanley's 2009 survey records the classical tangent-number exponential generating function needed for the joint-event lemma. Billey, Burdzy and Sagan's 2012 preprint develops exact counting of permutations by prescribed peak sets, while Billey, Fahrbach and Talmage's 2014 preprint studies peak polynomials and their roots. Zhuang's 2015 run-theorem preprint treats parity restrictions on peak and valley positions. Their relevant discussions do not themselves state the arbitrary-character Fourier nonvanishing theorem or the common exact dyadic valuation. Exact descent-pattern Fourier formulas concern a different encoding: the map from descent indicators to peak indicators is nonlinear, so the result is not a direct relabeling of a descent Walsh spectrum. The stated originality is a bounded literature comparison, not a claim of established absolute priority.

## Limitations
No explicit formula is claimed here for the full distribution of multiplier magnitudes or signs, the smallest actual magnitude at each order, or sharp inverse operator norms. An unindexed earlier theorem about the multivariate peak process or a signed generating functional might subsume the Fourier statement. The proof is self-contained apart from the classical tangent-number generating function, for which an independent counting derivation is available in the cited literature. No independent audit has been performed.

## References
- R. P. Stanley, *A Survey of Alternating Permutations*, arXiv:0912.4240, first submitted 2009-12-21. https://arxiv.org/abs/0912.4240
- S. Billey, K. Burdzy and B. E. Sagan, *Permutations with given peak set*, arXiv:1209.0693, first submitted 2012-09-04. https://arxiv.org/abs/1209.0693
- S. Billey, M. Fahrbach and A. Talmage, *Coefficients and roots of peak polynomials*, arXiv:1410.8506, first submitted 2014-10-30. https://arxiv.org/abs/1410.8506
- Y. Zhuang, *Counting permutations by runs*, arXiv:1505.02308, first submitted 2015-05-09. https://arxiv.org/abs/1505.02308
