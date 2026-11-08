# Classification of empty-core integer sumset-intersection spectra

## Finding
For a subset \(B\subseteq\mathbb Z\), let \(hB\) be the set of sums of exactly \(h\) (not necessarily distinct) elements of \(B\). For a strictly decreasing sequence \((A_q)_{q\ge1}\) of subsets of \(\mathbb Z\) with \(\bigcap_q A_q=\varnothing\), define
\[
\mathcal H(A_q)=\{h\ge1: \bigcap_{q\ge1}hA_q=\varnothing\}.
\]
The possible spectra are *exactly*
\[
\mathcal H(A_q)=\mathbb N_{>0}\setminus(S\setminus\{0\}),
\]
where \(S\) runs over additive submonoids of \(\mathbb N_0\) not containing \(1\), including \(S=\{0\}\). More strongly, for every such \(S\) one can construct a strictly decreasing empty-core sequence with
\[
\bigcap_{q\ge1}hA_q=\begin{cases}\{0\},&h\in S\setminus\{0\},\\\varnothing,&h\notin S.\end{cases}
\]
Thus the **failure-length set** \(\mathbb N_{>0}\setminus\mathcal H(A_q)\) is precisely an arbitrary additively closed subset of the positive integers that excludes \(1\). The characterization holds in the *fixed ambient group* \((\mathbb Z,+)\), not merely in a semigroup chosen separately for each spectrum.

## Assumptions and scope
The index is the full positive integer sequence \(q=1,2,\ldots\). Strict decrease means \(A_{q+1}\subsetneq A_q\) for every \(q\). The empty-core hypothesis means \(\bigcap_q A_q=\varnothing\); hence \(h(\bigcap_q A_q)=\varnothing\) for every positive \(h\). All sumsets use repetitions and exactly \(h\) summands. The ambient operation is ordinary integer addition. No positivity or uniform lower bound is imposed on the nontrivial realizing sets: they contain both signs. All monoids \(S\) are subsets of the nonnegative integers, contain \(0\), and are closed under addition. They need not be cofinite; for example \(\langle4,6\rangle\) is allowed.

## Proof
**1. Necessary additivity of failure lengths.** Write \(F=\{h\ge1:\bigcap_q hA_q\ne\varnothing\}\). If \(h,k\in F\), choose integers \(x\in\bigcap_q hA_q\) and \(y\in\bigcap_q kA_q\). At every index, \(x+y\in hA_q+kA_q=(h+k)A_q\), whence \(h+k\in F\). As \(\bigcap_q A_q=\varnothing\), \(1\notin F\). Consequently \(S=F\cup\{0\}\) is an additive submonoid excluding \(1\).

**2. Finite generators for any admissible monoid.** If \(S=\{0\}\), use the separate construction below. Otherwise let \(m=\min(S\setminus\{0\})\), necessarily \(m\ge2\). For each congruence class modulo \(m\) that meets \(S\), let \(a_r\) be its least member, omitting \(a_0=0\) as a redundant generator. Every \(s\in S\) in residue class \(r\) satisfies \(s=a_r+tm\) for an integer \(t\ge0\); for residue zero use \(s=tm\). Thus \(S\) has a finite positive generating set \(d_1,\ldots,d_t\), all \(d_i\ge2\). Repeating generators is harmless.

**3. Separated-scale realizing sets.** Let \(D=\max_i d_i\), enumerate generator labels periodically as \(d(j)=d_{1+((j-1)\bmod t)}\), and put
\[
G_1=1,\qquad b_j=(D+1)(j+2),\qquad G_{j+1}=b_jG_j\quad(j\ge1).
\]
Define
\[
A_q=\{G_j,-(d(j)-1)G_j:j\ge q\}.
\]
Every \(A_q\) contains both positive and negative elements. Every positive element is a distinct \(G_j\), so \(A_{q+1}\subsetneq A_q\). Moreover each element of \(A_q\) has absolute value at least \(G_q\), which tends to infinity; hence the core is empty. Since every element of \(A_q\) is divisible by \(G_q\), every integer in \(\bigcap_q hA_q\) is divisible by all \(G_q\), forcing the integer to be zero. Thus \(\bigcap_q hA_q\subseteq\{0\}\) for every \(h\ge1\).

**4. The complete zero-sum length criterion.** For a fixed positive \(h\), take \(q\) large enough that \(b_j>(D-1)h\) for all \(j\ge q\). Suppose a sum of exactly \(h\) elements of \(A_q\) equals zero. At each index \(j\), let \(x_j\) count copies of \(G_j\) and \(y_j\) count copies of \(-(d(j)-1)G_j\). Only finitely many counts are nonzero. Write \(z_j=x_j-(d(j)-1)y_j\), so
\[
\sum_{j\ge q}z_jG_j=0,\qquad |z_j|\le(D-1)h<b_j.
\]
If some \(z_j\ne0\), choose the least such \(j\). Contributions from larger indices are multiples of \(G_{j+1}=b_jG_j\); all earlier coefficients vanish. Reducing the equality modulo \(G_{j+1}\) forces \(b_j\mid z_j\), contradicting \(0<|z_j|<b_j\). Hence every \(z_j=0\), and \(x_j=(d(j)-1)y_j\). Therefore
\[
h=\sum_{j\ge q}(x_j+y_j)=\sum_{j\ge q}d(j)y_j\in S.
\]
In particular, when \(h\notin S\), \(0\notin hA_q\) for this sufficiently large \(q\). Conversely, if \(h\in S\setminus\{0\}\), express \(h=\sum_{i=1}^t c_i d_i\) with nonnegative integers \(c_i\). At every \(q\), each generator type \(d_i\) occurs at some distinct index \(j_i\ge q\). Using \((d_i-1)c_i\) copies of \(G_{j_i}\) and \(c_i\) copies of \(-(d_i-1)G_{j_i}\) yields zero with exactly \(h\) summands. Thus \(0\in hA_q\) for all \(q\), and the intersection is exactly \(\{0\}\). This proves both directions of the classification.

**5. The trivial monoid.** For \(S=\{0\}\), take \(A_q=\{n\in\mathbb Z:n\ge q\}\). This sequence is strictly decreasing with empty core, and every element of \(hA_q\) is at least \(hq\), so \(\bigcap_q hA_q=\varnothing\) for every \(h\ge1\).

## Verification
The standalone `VERIFY.py` independently enumerates sums from finite truncations of the separated-scale construction for four generating sets and tests all lengths in stated finite ranges. The executable reports 38 successful cases. This finite check is a reproducibility aid only: finite truncation cannot verify an infinite intersection, and the argument in step 4 is the decisive universal proof. In particular, the proof explicitly uses a \(q\) depending on the fixed test length \(h\), so no incorrect uniform choice over all lengths is assumed.

## Relationship to prior work
Marques and Nathanson's 2026 study introduces these intersection spectra in integer addition and constructs particular shapes, including the complement of the positive multiples of a prescribed integer in its Theorem 5. The current result classifies **all** spectra under the extra but natural empty-core hypothesis while fixing the ambient semigroup to \(\mathbb Z\). Nathanson's 2026 semigroup sequel poses related fixed-semigroup questions. The global classification by van Doorn, Monticone, and Tang allows the ambient semigroup to vary, and thus does not imply this fixed-integers classification: their universality allows complements that are not additively closed, whereas step 1 proves those are impossible here. The 2025 Nathanson paper develops the general commutation-of-intersections question but does not supply this arithmetic classification. These are statement/implication comparisons, not a claim that keyword searches can establish uniqueness.

## Limitations
The hypothesis that the intersection of the \(A_q\) is empty is essential to the necessary monoid argument. The classification does not describe nonempty-core spectra, sequences confined to the nonnegative integers, arbitrary ambient semigroups, or the minimum growth rate of integer magnitudes in realizing constructions. It proves existence, not a unique model for a spectrum. An unindexed prior equivalent formulation remains possible; the reproducibility test is finite, and independent mathematical audit has not been performed.

## References
- D. Marques and M. B. Nathanson, *Arithmetical structure of sumset intersections*, arXiv:2603.14510v1, first public March 15, 2026; Theorems 2–5 and motivating questions.
- M. B. Nathanson, *Problems and results on intersections of product sets and sumsets in semigroups*, arXiv:2604.04781v2, first public April 6, 2026; fixed-semigroup problems and Theorem 14.
- W. van Doorn, P. Monticone and Q. Tang, *Global Product Intersection Sets in Semigroups*, arXiv:2604.18869v2, first public April 20, 2026; Theorems 1.1–1.2 for varying semigroups.
- M. B. Nathanson, *Intersections of sumsets in additive number theory*, arXiv:2512.23574v3, first public December 29, 2025.
