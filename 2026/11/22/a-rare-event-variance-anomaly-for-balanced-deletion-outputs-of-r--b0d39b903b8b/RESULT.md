# A rare-event variance anomaly for balanced-deletion outputs of random Dyck words

## Finding

For every integer \(n\geq1\), let \(W_n\) be uniform over the \(C_n=\frac1{n+1}\binom{2n}{n}\) Dyck words of semilength \(n\), written with up-step `1` and down-step `0`. Let \(L_n\) count the **distinct Dyck words** obtained by deleting exactly one `1` and one `0` from \(W_n\), retaining order, and discarding invalid (non-Dyck) outputs. These outputs are the distinct lower covers in the Dyck pattern poset. As \(n\to\infty\),

\[
\mathbb E L_n=\frac{n^2}{4}-\frac{\sqrt\pi}{8}n^{3/2}+O(n),\qquad
\operatorname{Var}(L_n)\sim\frac{\sqrt\pi}{256}n^{7/2},
\]

and, **despite this larger-than-Gaussian variance**, the central fluctuations satisfy

\[
\frac{L_n-n^2/4}{n^{3/2}}\ \xrightarrow{\ d\ }\ \mathcal N(0,1/8).
\]

Thus the variance of the Gaussian distributional limit is **not** the limit of the normalized variances: \(\operatorname{Var}(L_n/n^{3/2})\sim(\sqrt\pi/256)\sqrt n\) diverges. Rare, macroscopically split Dyck excursions carry the excess second moment and also the leading negative correction to the mean. In particular, centering at the **true mean** instead produces the shifted limit \(\mathcal N(\sqrt\pi/8,1/8)\), illustrating failure of uniform integrability even at first order. The pre-existing *pointwise* cover-count formula is credited below; the stated global mean correction, variance exponent and constant, and fluctuation/variance separation are the finding.

## Assumptions and scope

A Dyck word is a balanced binary word with no prefix containing more zeros than ones. The source is uniform over all \(C_n\) such words, not over their prime factors. Two deletion-position pairs count as **one** output when their resulting words agree. The output must itself be a Dyck word of semilength \(n-1\). All limits concern integer \(n\to\infty\); the formulae are not finite-length identities. The standard asymptotic conventions for \(O(\cdot)\), \(\sim\), and convergence in distribution apply.

## Proof

**1. Pointwise identity from prior work.** Factor a Dyck word uniquely into irreducible/first-return components \(W=F_1\cdots F_h\). Let \(f_i\) be the semilength and \(p_i\) the number of `10` peaks in component \(F_i\), and put \(K=\sum_i p_i\). Let \(T\) be the total occurrences (overlapping permitted) of `101` and `010`. Bernini–Ferrari–Pinzani–West, Proposition 2.1 [1], proves that the exact number of distinct lower covers is

\[
L=\frac12\left(K^2+\sum_{i=1}^h p_i^2\right)-T
 =K^2-\sum_{i<j}p_i p_j-T. \tag{1}
\]

This identity is *not* claimed as new. In particular \(0\le T\le2n\).

**2. Replacing peaks by component sizes in mean square.** Put \(X=\sum_{i<j}f_i f_j\), so that \((n^2+\sum_i f_i^2)/8=n^2/4-X/4\). Conditional on the ordered component sizes, each irreducible factor of size \(f\ge2\) is an up-step, an independent uniform Dyck word of semilength \(f-1\), and a down-step; its peak count equals the internal word's peak count. A size-one factor has exactly one peak. The Narayana distribution gives, uniformly for \(f\ge1\),

\[
\mathbb E(p\mid f)=\frac f2+O(1),\quad
\operatorname{Var}(p\mid f)=O(f),\quad
\mathbb E\bigl[(p-f/2)^4\mid f\bigr]=O(f^2).
\]

Indeed for \(f\ge2\) the mean equals \(f/2\), and size one contributes the uniformly bounded exception. Write

\[
L=\frac{n^2}{4}-\frac X4+\varepsilon,
\quad \varepsilon=\frac12(K^2-n^2/4)+\frac12\sum_i(p_i^2-f_i^2/4)-T. \tag{2}
\]

The total peak count \(K\) is Narayana-distributed with mean \((n+1)/2\), variance \((n^2-1)/(4(2n-1))=O(n)\), and fourth centered moment \(O(n^2)\). Therefore \(\mathbb E(K^2-n^2/4)=O(n)\) and \(\mathbb E(K^2-n^2/4)^2=O(n^3)\). Conditional independence of component peaks gives \(\mathbb E\sum_i(p_i^2-f_i^2/4)=O(n)\); its conditional variance is \(O(\sum_i f_i^3)=O(n^3)\), because \(|p_i^2-f_i^2/4|\le2f_i|p_i-f_i/2|\) after absorbing the constant-size adjustment. Combining these bounds with \(T=O(n)\) yields

\[
\mathbb E\varepsilon=O(n),\qquad \mathbb E\varepsilon^2=O(n^3).\tag{3}
\]

**3. Exact first two moments of the component-size interaction.** Define Catalan and irreducible series

\[
C(z)=\sum_{n\ge0}C_nz^n=\frac{1-\sqrt{1-4z}}{2z},\qquad
I(z)=zC(z)=\frac{1-\sqrt{1-4z}}2,\quad C(z)=\frac1{1-I(z)}.
\]

Let \(A_1=zI'(z)\) and \(A_2=(z\,d/dz)^2 I(z)\). The symbolic sequence construction, marking pairs of distinct components and separately their ordered coincidences, gives the **exact** identities

\[
\sum_{n\ge0}C_n\mathbb E X_n z^n=A_1^2 C^3,\tag{4}
\]

\[
\sum_{n\ge0}C_n\mathbb E X_n^2z^n
=A_2^2C^3+6A_2A_1^2C^4+6A_1^4C^5.\tag{5}
\]

The three terms in (5) correspond to two coincident pairs, two distinct pairs sharing one marked component, and disjoint pairs respectively; the factor six in each of the last two is the number of ordered edge pairs on three/four marked components.

Near \(z=1/4\), write \(s=\sqrt{1-4z}\). Then \(C\sim2\), \(A_1=z/s\sim1/(4s)\), and \(A_2=z/s+2z^2/s^3\sim1/(8s^3)\). Thus (4) has principal singular term \(\frac12(1-4z)^{-1}\); (5) has \(\frac18(1-4z)^{-3}\). Singularity transfer and \(C_n\sim4^n/(\sqrt\pi n^{3/2})\) yield

\[
\mathbb EX_n=\frac{\sqrt\pi}{2}n^{3/2}+O(n),\quad
\mathbb EX_n^2=\frac{\sqrt\pi}{16}n^{7/2}+O(n^3),\quad
\operatorname{Var}X_n\sim\frac{\sqrt\pi}{16}n^{7/2}. \tag{6}
\]

The subtraction of \((\mathbb EX_n)^2=O(n^3)\) does not change the leading order. Equations (2), (3), (6) give the asserted mean. Cauchy–Schwarz bounds the covariance of \(X_n\) and \(\varepsilon\) by \(O(n^{13/4})=o(n^{7/2})\); the remainder variance is \(O(n^3)\). Consequently \(\operatorname{Var}(L_n)\sim\operatorname{Var}(X_n)/16=\sqrt\pi\,n^{7/2}/256\).

**4. Typical component size versus rare splits.** For fixed integer \(r\ge0\), and \(n>2r\), the number of Dyck words whose **unique** largest irreducible component has size \(n-r\) equals

\[
C_{n-r-1}\,[z^r]C(z)^2.
\]

Dividing by \(C_n\) gives the limit \(4^{-r-1}[z^r]C(z)^2\). These limits sum to \(\frac14C(1/4)^2=1\), so the number \(R_n\) of semilength units **outside** a largest component is tight: \(R_n=O_{\mathbb P}(1)\). This implies \(\sum_{i<j}p_i p_j\le nR_n+R_n^2=O_{\mathbb P}(n)\). With \(T\le2n\), identity (1) yields \(L_n=K_n^2+O_{\mathbb P}(n)\).

Finally Narayana coefficients \(N(n,k)=\frac1n\binom nk\binom n{k-1}\) obey the local central limit theorem, by Stirling's formula, so \((K_n-n/2)/\sqrt n\Rightarrow\mathcal N(0,1/8)\). Expansion \(K_n^2-n^2/4=n(K_n-n/2)+(K_n-n/2)^2\) and Slutsky's theorem prove the claimed distributional limit. The variance anomaly follows by contrasting this limit with (6). This completes the proof.

## Verification

The standalone standard-library checker `verify.py` independently deletes all oppositely labeled position pairs, retains only valid distinct Dyck outputs, and compares their count with the published pointwise identity for every Dyck word of semilength at most ten (including \(16{,}796\) sources at semilength ten). It independently computes \(X\) from component lengths and checks the first and second generating-series moments through length ten. Integer coefficients of both moment series are additionally generated through semilength thirty-five. Run `python3 verify.py`; success ends in `VERIFY_OK`. These finite checks corroborate, but are not the proof of, any asymptotic statement.

## Relationship to prior work

Bernini, Ferrari, Pinzani, and West [1] defined the Dyck pattern poset and proved exact formula (1) for the lower cover count of **each given path**; they did not establish the uniform random-path fluctuation or variance asymptotics proved here. Bernini, Cervetti, Ferrari, and Steingrímsson [2] analyze covering relations and enumerations **within selected initial intervals**, not the stochastic distribution of rank-down degrees over the whole Catalan level. Narayana's classic peak enumeration [3] supplies the separate known peak law used in the proof. The contribution is the analytic synthesis of these structural ingredients, including the nonuniform-integrability/rare-split second-moment phenomenon; it is not a new exact pointwise covering formula.

## Limitations

This theorem is for uniformly sampled **binary Dyck words** and distinct one-open/one-close deletion outputs. It does not assert a coding optimum, recovery from noisy reads, exact finite-length distribution, rates for arbitrary source weighting, or a joint limit with the longest irreducible component. The theorem relies explicitly on the previously published pointwise cover formula; a prior unindexed asymptotic refinement could affect priority. Independent external verification of the new derivation has not been performed.

## References

[1] A. Bernini, L. Ferrari, R. Pinzani, J. West, *The Dyck pattern poset*, arXiv:1303.3785v1, first posted 15 March 2013, Section 2, Proposition 2.1. https://arxiv.org/abs/1303.3785

[2] A. Bernini, M. Cervetti, L. Ferrari, E. Steingrímsson, *Enumerative combinatorics of intervals in the Dyck pattern poset*, arXiv:1910.00299, first posted 1 October 2019. https://arxiv.org/abs/1910.00299

[3] Narayana peak enumeration of Dyck paths (classical formula); see the Narayana-number discussion and citations in [1].
