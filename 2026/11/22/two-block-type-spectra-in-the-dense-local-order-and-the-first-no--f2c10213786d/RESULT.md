# Two-block type spectra in the dense local order and the first nonunimodal boundary

## Finding

Let \(D\) be the countable homogeneous **dense local order** (the Fraïssé limit of finite locally transitive tournaments). Fix positive integers \(n,r\). Name a parameter block \(p_1,\ldots,p_n\) with \(p_i\to p_j\) for all \(i<j\). Consider complete types of ordered, pairwise distinct, nonparameter elements \(h_1,\ldots,h_r\), with \(h_i\to h_j\) for all \(i<j\). For each type, let \(k\) be the number of cross-block arcs \(p_i\to h_j\). Define \(C_{n,r}(z)=\sum_{k=0}^{nr}c_{n,r}(k)z^k\), where \(c_{n,r}(k)\) is the number of such types with exactly \(k\) cross arcs in that direction.

Set \(a_s=s+1\) for \(0\le s<n\) and \(a_s=2n-1-s\) for \(n\le s<2n\), extended periodically modulo \(2n\). Thus \((a_0,\ldots,a_{2n-1})=(1,2,\ldots,n,n-1,\ldots,0)\). For \(d\ge0\), let \(h_d(x_0,\ldots,x_n)=\sum_{b_0+\cdots+b_n=d}\prod_{j=0}^{n}x_j^{b_j}\) be the complete homogeneous symmetric polynomial.

**Theorem.** For every \(n,r\ge1\),
\[
\boxed{C_{n,r}(z)=\sum_{s=0}^{2n-1}z^{a_s}\,h_{r-1}\bigl(z^{a_s},z^{a_{s+1}},\ldots,z^{a_{s+n}}\bigr).}
\]
In particular, \(C_{n,r}(z)\) is palindromic of degree \(nr\), and
\[
C_{n,r}(1)=2n\binom{n+r-1}{n}.
\]
Every \(C_{n,r}\) with \(n+r\le7\) is unimodal. Among pairs with \(n+r=8\), the **only** nonunimodal spectra occur for the ordered pairs \((n,r)=(3,5),(4,4),(5,3)\). Two first obstructions are
\[
\begin{aligned}
C_{3,5}(z)&=1+2z+5z^2+10z^3+15z^4+22z^5+26z^6+24z^7+24z^8\\
&\quad+26z^9+22z^{10}+15z^{11}+10z^{12}+5z^{13}+2z^{14}+z^{15},\\
C_{4,4}(z)&=1+2z+5z^2+10z^3+20z^4+24z^5+33z^6+28z^7+34z^8\\
&\quad+28z^9+33z^{10}+24z^{11}+20z^{12}+10z^{13}+5z^{14}+2z^{15}+z^{16}.
\end{aligned}
\]
Here unimodal means nondecreasing coefficients followed by nonincreasing coefficients, allowing equalities. The theorem makes no claim about a complete classification of unimodality above combined size eight.

## Assumptions and scope

A tournament is *locally transitive* when both the out-neighborhood and in-neighborhood of every vertex induce transitive tournaments. The dense local order is homogeneous with age consisting exactly of finite locally transitive tournaments; finite consistent labelled extension diagrams therefore correspond to complete nonalgebraic tuple types over the named base. Both blocks have prescribed transitive internal orientations; no requirement is imposed on their cross-block arcs beyond local transitivity. Tuples are ordered and injective, not counted up to relabeling or automorphism.

## Proof

**1. Canonical antipodal circular model.** Use Brouwer's canonical representation of a finite locally transitive tournament by a cyclic order of the \(2(n+r)\) primary and antipodal symbols. In such a representation, the antipode of each primary symbol lies exactly \(n+r\) positions later; an arrow \(x\to y\) holds precisely when \(y\) lies between \(x\) and its antipode in the positive cyclic direction. The labelled cyclic order represents the tournament uniquely, modulo a global rotation; conversely every antipodally interlaced labelled cyclic order yields a locally transitive tournament. Applying this normal form to the transitive named block alone, its cyclic order is fixed, up to rotation, as \(p_1,\ldots,p_n,p'_1,\ldots,p'_n\).

**2. Gap choice and weak compositions.** Position \(h_1\) in one of the \(2n\) old-symbol gaps, numbered \(s=0,\ldots,2n-1\), starting immediately after \(p_1\). There are precisely \(a_s\) named vertices with arrows toward \(h_1\). Since \(h_1\to h_j\) for every \(j>1\), all later primary symbols \(h_2,\ldots,h_r\), in that order, lie strictly in the positive half-circle \((h_1,h'_1)\). This open half-circle contains exactly \(n\) old symbols, which divide it into \(n+1\) consecutive gaps. Choose nonnegative occupancies \(b_0,\ldots,b_n\) with \(\sum b_j=r-1\), each occupancy specifying how many consecutive labelled \(h\)-symbols lie in the corresponding gap. Each such weak composition produces exactly one labelled locally transitive extension; conversely every extension yields precisely that choice of \(s\) and \((b_j)\). The number of named predecessors of each \(h\)-symbol in gap \(j\) is \(a_{s+j}\), where indices are periodic modulo \(2n\), since crossing an old endpoint changes exactly one cross-edge direction. Thus its total weight is
\[
z^{a_s}\prod_{j=0}^{n}z^{a_{s+j}b_j}.
\]
Summing the weights over all weak compositions and then over \(s\) gives the stated complete-homogeneous-polynomial identity, for arbitrary positive \(n,r\).

**3. Symmetry and total count.** Rotating all new primary symbols \(h_1,\ldots,h_r\) by a half-turn in their antipodal circular representation keeps their internal transitive orientation, and reverses every cross-block arc. It therefore bijects coefficient \(k\) to coefficient \(nr-k\), establishing palindromicity. With \(z=1\), each of the \(2n\) initial gaps admits \(\binom{n+r-1}{n}\) weak compositions, proving the total formula.

**4. Exact first-unimodality boundary.** For each positive ordered pair with \(2\le n+r\le8\), the displayed finite-sum formula was evaluated using integer arithmetic, and independently checked by enumerating **all** \(2^{nr}\) possible cross-block orientations of two prescribed transitive tournaments. For each orientation the checker tests every triple for a directed triangle and rejects it if some fourth vertex sees the entire triangle in its in-neighborhood or out-neighborhood; these are exactly the forbidden four-vertex configurations for local transitivity. Comparing each resulting coefficient sequence with the definition of unimodality yields no exceptions for total size at most seven, and exactly \((3,5),(4,4),(5,3)\) at size eight. In the displayed polynomials, strict coefficient valleys certify the two examples; the third is the exchanged-block counterpart and is separately checked. All 28 ordered pairs at total size at most eight were covered; the complete integer certificate is `small_spectra.json` and the independent verifier is `checker.py`.

## Verification

Run `python3 checker.py` using Python 3 standard library from a writable directory. The program builds the weighted gap polynomial and independently enumerates every orientation between the two blocks for each positive ordered pair \((n,r)\) with \(n+r\le8\). It asserts equality of all coefficients, palindromicity, the exact total, and the classification of coefficient unimodality. The recorded verification result is in `verification_output.txt`, beginning with `VERIFY_OK`. The included `small_spectra.json` gives every exact coefficient vector. Finite enumeration verifies the sharp small-size claim but is *not* offered as the proof of the all-order formula, which follows from the circular normal form and weak-composition bijection.

## Relationship to prior work

Brouwer's 1980 account supplies the canonical antipodal circular representation and counts unlabelled locally transitive tournaments via shift registers. Babai and Cameron (2000), Section 3, analyze the associated switching-class and local-order enumerations, and Coregliano (2015, initial arXiv version) treats asymptotic locally transitive tournaments. Those structural results are prerequisites, not discoveries here. The specialization \(r=1\) reduces to the already-known unary score spectrum \(C_{n,1}(z)=(1+z)\sum_{j=0}^{n-1}z^j\), which is expressly not claimed as novel. The new question fixes two **individually named transitive blocks**, weights *every* allowed labelled two-block extension by the exact number of forward cross arcs, and locates the sharp first failure of coefficient unimodality. General circular representability alone does not state this weighted coefficient formula or the sharp eight-point boundary. Published sources and relevant indexed research were compared at the level of mathematical implications. This comparison cannot exclude unindexed equivalent enumerations.

## Limitations

The exact formula covers only the extension family with both internally transitive blocks; it is not the spectrum over arbitrary parameter tournaments or for an unrestricted tuple's induced tournament. The unimodality classification is complete only for combined sizes through eight. The proof relies on the established antipodal circular representation. Independent mathematical audit and definitive historical-priority review have not been performed. Brouwer's original report is visibly dated April 1980 but does not provide an independently verified day of first public appearance; the dated 2000-08-01 source below is used as the earliest independently verified exact public day in the cited material.

## References

1. A. E. Brouwer, *The Enumeration of Locally Transitive Tournaments*, Stichting Mathematisch Centrum report ZW 138/80, April 1980, especially Section 1, pp. 3–4. https://ir.cwi.nl/pub/6805/6805D.pdf
2. L. Babai and P. J. Cameron, *Automorphisms and Enumeration of Switching Classes of Tournaments*, Electronic Journal of Combinatorics 7(1), R38, published 2000-08-01, especially Section 3. https://doi.org/10.37236/1516 ; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v7i1r38/pdf
3. L. N. Coregliano, *Quasi-Carousel Tournaments*, first submitted to arXiv 2015-03-13, arXiv:1503.04124; Section 1 treats locally transitive tournaments and the forbidden four-vertex configurations. https://arxiv.org/abs/1503.04124
