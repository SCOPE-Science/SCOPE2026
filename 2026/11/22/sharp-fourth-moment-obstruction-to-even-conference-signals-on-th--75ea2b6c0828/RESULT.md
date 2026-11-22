# Sharp fourth-moment obstruction to even conference signals on the nine-cycle

## Finding

Let \(G=\mathbb Z/9\mathbb Z\). On the class of even, punctured-unimodular, mean-zero complex functions on \(G\), the unnormalized Fourier fourth moment has the sharp minimum

\[
\min_f\sum_{k=1}^{8}|\widehat f(k)|^4=\boxed{792}.
\]

The universal flat-spectrum value is \(9^2(9-1)=648\), so the exact excess is \(144\). Equality occurs precisely when the four values \(f(1),f(2),f(3),f(4)\) are a common unit scalar times a permutation of \(1,-1,i,-i\). Therefore the nine-cycle admits no **even** conference signal. By the standard border construction, there is no symmetric complex conference matrix of order ten with its standard nine-circulant core and unit border. This is a statement about that prescribed core, not about all complex conference matrices of order ten.

## Assumptions and scope

We use the unnormalized discrete transform

\[
\widehat f(k)=\sum_{j=0}^{8}f(j)e^{-2\pi i jk/9},\qquad k\in G.
\]

The admissible set \(\mathcal E\) consists of precisely those functions \(f:G\to\mathbb C\) such that (i) \(f(0)=0\); (ii) \(f(j)=f(-j)\) for every \(j\); (iii) \(|f(j)|=1\) for \(j\ne0\); and (iv) \(\sum_j f(j)=0\). This set is nonempty. Writing

\[
(a,b,c,d)=(f(1),f(2),f(3),f(4)),
\]

its conditions become \(|a|=|b|=|c|=|d|=1\) and \(a+b+c+d=0\), and the signal in cyclic order is \((0,a,b,c,d,d,c,b,a)\).

## Proof

**Step 1: Every balanced unit quadrilateral consists of two antipodal pairs.** Given \(|a|=|b|=|c|=|d|=1\) and \(a+b+c+d=0\), if \(a+b=0\), then also \(c+d=0\). Otherwise let \(m=(a+b)/2\ne0\). For two unit complex numbers with midpoint \(m\), their difference is a vector perpendicular to \(m\), of prescribed modulus \(2\sqrt{1-|m|^2}\). Hence the unordered pair is uniquely fixed by \(m\). As \((c+d)/2=-m\), necessarily \(\{c,d\}=\{-a,-b\}\). Thus, after choosing a global scalar, every admissible signal belongs to at least one of the families

\[
\begin{array}{c|c}
\mathrm{I}&(a,b,c,d)=(1,-1,z,-z)\\
\mathrm{II}&(a,b,c,d)=(1,z,-1,-z)\\
\mathrm{III}&(a,b,c,d)=(1,z,-z,-1)
\end{array}
\qquad |z|=1.
\]

Intersections between families cause no difficulty.

**Step 2: Exact autocorrelation defect.** Define periodic autocorrelations \(c_s=\sum_{j=0}^8 f(j)\overline{f(j-s)}\), with indices modulo nine, and let \(\tau=\Re z\in[-1,1]\). Directly multiplying the nine terms gives \(c_0=8\), \(c_{9-s}=c_s\in\mathbb R\), and the following complete table of the four distinct nonzero defects \(c_s+1\):

\[
\begin{array}{c|rrrr}
& s=1&s=2&s=3&s=4\\ \hline
\mathrm{I}&-2-2\tau&4\tau&0&2-2\tau\\
\mathrm{II}&2+2\tau&-2+2\tau&0&-4\tau\\
\mathrm{III}&4\tau&2-2\tau&0&-2-2\tau
\end{array}
\]

Every row has the same sum of squared defects, including the reflection-paired shifts:

\[
\sum_{s=1}^{8}|c_s+1|^2
=2\sum_{s=1}^4|c_s+1|^2
=16+48\tau^2.
\]

**Step 3: Transfer to Fourier energy.** Let \(b_s=9\mathbf1_{\{s=0\}}-1\) be the ideal conference autocorrelation; thus \(b_0=8\), while \(b_s=-1\) for \(s\ne0\). The convolution identity and Parseval for the unnormalized transform give \(\widehat c(k)=|\widehat f(k)|^2\), \(\widehat b(0)=0\), \(\widehat b(k)=9\) for \(k\ne0\), and

\[
\sum_{k=1}^{8}\bigl(|\widehat f(k)|^2-9\bigr)^2
=9\sum_{s=1}^{8}|c_s+1|^2
=144+432\tau^2.
\]

Here \(\widehat f(0)=0\) and Plancherel gives \(\sum_{k=1}^8|\widehat f(k)|^2=9\sum_j|f(j)|^2=72\). Expanding the left side yields the **exact formula in each of the three families**:

\[
\sum_{k=1}^{8}|\widehat f(k)|^4
=792+432\tau^2.
\]

It follows that the sharp lower bound is \(792\), achieved precisely at \(\tau=0\), namely \(z=\pm i\). Every minimizing four-tuple therefore consists of the four distinct phases \(\{\omega,-\omega,i\omega,-i\omega\}\), in any order, where \(|\omega|=1\), and conversely all such choices give equality. In particular \((a,b,c,d)=(1,-1,i,-i)\) is a witness.

**Step 4: Conference-signal obstruction.** A conference signal would additionally require \(|\widehat f(k)|=3\) for all eight nonzero frequencies, which would force the fourth moment to be \(8\cdot3^4=648\). Since every even candidate has fourth moment at least \(792\), none exists. The equivalence with absence of the **specified bordered symmetric circulant-core** conference matrices follows by the elementary Fourier/autocorrelation border identity (see Fallon–Iverson, Theorem 2.1), not by any assertion that all symmetric conference matrices have such cores.

## Verification

`verify_conference9.py` is a standalone standard-library Python checker. It represents the three phase families by exact Laurent polynomials in \(z\), conjugating by \(z\mapsto z^{-1}\), checks every one of the four autocorrelation-defect formulas plus reflection and zero-sum relations, and checks the exact squared-defect identity. It independently evaluates finite complex Fourier sums at thirteen different phases in each family, including equality phases. It records 27 exact polynomial assertions and 39 supplementary numerical comparisons. Reproduce with `python3 verify_conference9.py`. The proof above is analytical for all unit complex \(z\); finite tests only supplement its algebra.

## Relationship to prior work

Fallon and Iverson, arXiv:2610.09169v1, Definition 1.1 and Theorem 2.1, establish the conference-signal/autocorrelation/matrix equivalence; Section 3 introduces the fourth-moment energy minimization, while Table 1 reports **zero numerically found** even signals for cyclic order nine, without a nonexistence proof. Their Problem 7.2(b) asks which cyclic groups admit an even conference signal. The result here analytically resolves the specific nine-cycle case, strengthens its negative answer to the exact sharp excess \(144\), and classifies all optimal near-conference candidates.

Benoist, arXiv:2406.11529, Section 7.2, counts **odd** conference signals on the nine-cycle and does not treat this even-energy minimum. Uzcátegui Contreras–Goyeneche–Turek–Václavíková, arXiv:1910.00586v2, investigate **Hermitian** complex circulants and real symmetric circulants, not the present complex symmetric non-Hermitian bordered nine-core class. Diţă, arXiv:0901.0982v3, constructs inverse-orthogonal conference matrices in low orders (four through six), without determining this order-ten core extremum. We found no broader theorem in the inspected material implying the exact \(792\) value or its optimizer classification.

## Limitations

This statement covers only the cyclic group of order nine, the even constraint, exact mean zero, and exact unit moduli off the origin. It does not forbid non-even conference signals on that group (odd examples exist), nor even signals over the noncyclic nine-element group, nor unrestricted order-ten complex conference matrices. The theorem gives no noise-stability bound and no classification at other group orders. The novelty assessment is literature-based and cannot exclude unindexed older equivalent formulations; no independent mathematical audit is asserted.

## References

1. K. Fallon and J. W. Iverson, *Conference signals: Applications, existence, and constructions*, arXiv:2610.09169v1, initially submitted 2026-10-06. https://arxiv.org/pdf/2610.09169
2. Y. Benoist, *Fourier transform in cyclic groups*, arXiv:2406.11529, especially Section 7.2. https://arxiv.org/abs/2406.11529
3. D. Uzcátegui Contreras, D. Goyeneche, O. Turek, and Z. Václavíková, *Circulant matrices with orthogonal rows and off-diagonal entries of absolute value 1*, arXiv:1910.00586v2. https://arxiv.org/pdf/1910.00586
4. P. Diţă, *Complex Hadamard matrices from Sylvester inverse orthogonal matrices*, arXiv:0901.0982v3. https://arxiv.org/pdf/0901.0982
