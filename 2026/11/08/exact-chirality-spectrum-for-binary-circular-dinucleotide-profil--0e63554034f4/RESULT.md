# Exact chirality spectrum for binary circular dinucleotide profiles

## Finding

Let \(A,D,b\) be integers with \(b\ge1\), \(A\ge b\), and \(D\ge b\). Consider nonconstant binary circular words, with circular adjacency (including the last-to-first edge), having exactly \(A\) zeros, \(D\) ones, \(b\) occurrences of `01`, and \(b\) occurrences of `10`. Equivalently, their dinucleotide counts are \((A-b,b,b,D-b)\) in the order `00`, `01`, `10`, `11`. Identify words under rotation but not reflection. Let \(T(A,D,b)\) be the number of rotation classes, and \(S(A,D,b)\) the number of those classes equal to their reversed class.

Define, for even \(b=2p\),
\[
F_0(m,b)=[z^m]\left(\frac{z^2}{1-z^2}\right)^p,
\qquad
F_2(m,b)=[z^m]\left(\frac{z}{1-z}\right)^2\left(\frac{z^2}{1-z^2}\right)^{p-1}.
\]
For odd \(b=2p+1\), define \(F_1(m,b)=\binom{\lfloor(m-1)/2\rfloor}{p}\). The exact number of achiral rotation classes is
\[
\boxed{S(A,D,b)=
\begin{cases}
F_1(A,b)F_1(D,b),&b\text{ odd},\\
\tfrac12\bigl(F_2(A,b)F_0(D,b)+F_0(A,b)F_2(D,b)\bigr),&b\text{ even}.
\end{cases}}
\]
An explicit formula for total rotation classes is
\[
T(A,D,b)=\frac1b\sum_{e\mid\gcd(A,D,b)}\varphi(e)
\binom{A/e-1}{b/e-1}\binom{D/e-1}{b/e-1}.
\]
Consequently, \((T-S)/2\) is the number of reversal-paired (chiral) bracelet classes and \((T+S)/2\) is the number of bracelets with the prescribed profile. In particular, a reversal-invariant rotation class exists **if and only if** \(b\) is odd or at least one of \(A,D\) is even. This parity obstruction is exact for every feasible profile.

## Assumptions and scope

The circular words have positive length \(n=A+D\) and contain both symbols. Rotation classes are orbits of the full cyclic group on the \(n\) labeled sites, including words with nontrivial periods. A reversal-invariant rotation class means the reversal of any representative equals some rotation of that representative; it need not have a palindromic linear representative. The formulas count classes, not labeled words. Binomial coefficients outside their nonnegative-integer range are zero, and \([z^m]\) denotes ordinary formal-power-series coefficient extraction. Constant words, for which \(b=0\), constitute separate singleton symmetric classes and are excluded.

## Proof

1. **Run coding.** Each permitted circular word has exactly \(b\) positive zero-runs and \(b\) positive one-runs. Choosing a zero-run as the initial run gives a pair of positive compositions \(u=(u_0,\ldots,u_{b-1})\) and \(v=(v_0,\ldots,v_{b-1})\) with sums \(A\) and \(D\), via \(0^{u_0}1^{v_0}\cdots0^{u_{b-1}}1^{v_{b-1}}\). Two such pairs give the same word up to rotation precisely when they differ by a common cyclic shift of the run index. This remains valid for periodic words because we take orbits, not free actions.

2. **Involution on paired runs.** Reversing the circular word and choosing the zero-run corresponding to the reversal of \(u_{b-1}\) acts, modulo an indexing convention, by \(u'_i=u_{b-1-i}\) and \(v'_i=v_{b-2-i}\), with indices modulo \(b\). Compose this involution with all \(b\) cyclic run shifts. The resulting involutions have constraints \(u_i=u_{c-i}\) and \(v_i=v_{c-1-i}\), for \(c\in\mathbb Z/b\mathbb Z\). Notice the crucial one-unit offset between the zero-run and one-run reflection axes.

3. **Counting fixed compositions.** An involution of \(b\) run indices with \(f\) fixed indices and \((b-f)/2\) exchanged pairs fixes exactly
\[
[z^m]\left(\frac z{1-z}\right)^f
\left(\frac {z^2}{1-z^2}\right)^{(b-f)/2}
\]
positive compositions totaling \(m\). For odd \(b=2p+1\), every reflection has exactly one fixed index on each of \(u\) and \(v\). Summing the positive part assigned to the fixed index gives \(F_1(m,b)=\binom{\lfloor(m-1)/2\rfloor}{p}\). For even \(b=2p\), half the reflections have two fixed zero-run indices and no fixed one-run indices; the other half interchange those roles. Their counts are the displayed products \(F_2(A,b)F_0(D,b)\) and \(F_0(A,b)F_2(D,b)\).

4. **Passing from fixed pairs to achiral classes.** Let \(C_b\) act by simultaneous run shift and let the reversal generate the extension to the dihedral group \(D_b\). Burnside gives \(T=\frac1b\sum_{g\in C_b}|\mathrm{Fix}(g)|\) and \(B=\frac1{2b}(\sum_{g\in C_b}|\mathrm{Fix}(g)|+\sum_{h\in D_b\setminus C_b}|\mathrm{Fix}(h)|)\). Each dihedral orbit consists either of one achiral rotation orbit or two reversal-paired rotation orbits. Hence \(S=2B-T=\frac1b\sum_{h\in D_b\setminus C_b}|\mathrm{Fix}(h)|\). Substitution of step 3 yields the exact formula, without any assumption of freeness.

5. **Total class count.** A run-index rotation whose repetition multiplicity is \(e\) fixes a pair of compositions only if \(e\mid A,D,b\), and in that case the fixed-pair count equals \(\binom{A/e-1}{b/e-1}\binom{D/e-1}{b/e-1}\). There are \(\varphi(e)\) such rotations. Cyclic Burnside yields \(T\).

6. **Sharp existence obstruction.** For odd \(b\), both \(F_1\) factors are positive under \(A,D\ge b\). For even \(b\), \(F_2(m,b)>0\) for every \(m\ge b\), while \(F_0(m,b)>0\) precisely when \(m\) is even (under \(m\ge b\)). The formula for \(S\) is positive exactly when at least one of \(A,D\) is even. This also proves that the zero cases are genuine impossibilities, not finite-search failures.

## Verification

The standalone `verify.py` enumerates every nonconstant binary necklace at lengths \(2\) through \(17\) using literal cyclic rotations. Independently of the run-pair proof, it measures each profile and tests whether reversal is in the same rotation orbit. It checks the formulas for \(S\), \(T\), integral chiral pairing, and the parity obstruction for all \(444\) feasible triples in this range. Executing `python verify.py` prints `VERIFY_OK lengths=2..17 profiles=444`. The proof is universal; this finite test is diagnostic and not a substitute for its orbit argument.

## Relationship to prior work

Zelenyuk and Zelenyuk's *Counting Symmetric Bracelets* (first online August 22, 2013), particularly Theorems 3.1 and 3.5, develops reflection-symmetric orbits and gives **unrestricted** color-necklace totals. The general orbit identity in step 4 is standard and credited to that framework. The present calculation refines the count jointly by two letter multiplicities **and** a specified cyclic dinucleotide profile; its offset pair-reflection formula and sharp parity obstruction are not given by the unrestricted total. Knopfmacher and Robbins analyze dihedral compositions with one prescribed sum and part count, whereas the present group action couples two independent positive compositions under offset reflection. Bianconi and Brugnoli enumerate necklaces with a prescribed transition count but do not, in their accessible abstract, claim the fixed-content reflection spectrum. Literature comparisons therefore concern logical coverage rather than similarity of terminology.

## Limitations

This is an exact enumerative result for binary circular words with both letters; it does not extend automatically to multiletter alphabets, error-prone sequencing, or linear strings. No algorithmic or biological performance claim is made. The full text of the potentially relevant Knopfmacher–Robbins dihedral-composition paper and the later Bianconi–Brugnoli paper could not be inspected; unindexed equivalent weighted-enumeration results remain a historical-priority risk. The work is self-reviewed; independent validation has not occurred.

## References

- Y. Zelenyuk and Y. Zelenyuk, *Counting Symmetric Bracelets*, Bulletin of the Australian Mathematical Society 89 (2014), 431–436; first online August 22, 2013. DOI: https://doi.org/10.1017/S0004972713000701. Full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B424CA08B3A4F6171C59EBF460855955/S0004972713000701a.pdf/counting-symmetric-bracelets.pdf
- A. Knopfmacher and N. Robbins, *Some Properties of Dihedral Compositions*, Utilitas Mathematica 92 (2013), 207–220. https://www.researchgate.net/publication/260006088_Some_Properties_of_Dihedral_Compositions
- F. Bianconi and E. Brugnoli, *Enumerating Necklaces with Transitions*, Bulletin of the Australian Mathematical Society 105 (2022), 1–11; first online May 11, 2021. DOI: https://doi.org/10.1017/S0004972721000307.
