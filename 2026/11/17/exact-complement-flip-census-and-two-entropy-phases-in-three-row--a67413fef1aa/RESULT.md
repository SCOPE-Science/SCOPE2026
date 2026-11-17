# Exact complement-flip census and two entropy phases in three-row Day & Night

## Finding

Consider the synchronous Day & Night cellular automaton (birth B3678, survival S34678) on the labelled Moore-neighborhood torus \(\mathbb Z_3\times\mathbb Z_n\), with \(n\ge3\). Let \(H_n\) denote the number of binary configurations \(x\) for which one global update yields the **bitwise complement** of \(x\): \(F_n(x)=\overline{x}\). Let \(L_0=2\), \(L_1=1\), and \(L_{k+2}=L_{k+1}+L_k\) be the Lucas numbers, and let \(\epsilon_n=2\) when \(3\mid n\) and \(\epsilon_n=-1\) otherwise. Then for every integer \(n\ge3\),

\[
H_n=2\cdot3^n+L_n+\epsilon_n+6\cdot18^{n/3}\,\mathbf{1}_{3\mid n}.
\]

The last term is defined as zero when \(3\nmid n\). Every such configuration belongs to a primitive temporal two-cycle with its complement, so the number of distinct *complement-flip* two-cycle orbits is exactly \(H_n/2\). This is not a count of all temporal two-cycles.

Moreover, the \(2\cdot3^n\) configurations having exactly one live cell in every column or exactly two live cells in every column are all complement-flip states. They account for asymptotically all such states:

\[
H_n=2\cdot3^n+O\bigl(18^{n/3}\bigr),\qquad
\frac{H_n}{2\cdot 3^n}\longrightarrow1.
\]

The two column-density classes have asymptotic proportions \(1/2\) each. Bitwise complementation exchanges the classes, so their union gives one dominant orbit population, not two disjoint classes of orbits. In particular, the complement-flip orbit population grows asymptotically as \(3^n\), while its proportion among all \(2^{3n}\) binary configurations tends to zero.

## Assumptions and scope

Cells have coordinates \((r,j)\in\mathbb Z_3\times\mathbb Z_n\). Their eight Moore neighbors are the offsets \((\delta r,\delta j)\in\{-1,0,1\}^2\setminus\{(0,0)\}\), taken modulo the two circumferences. Since \(n\ge3\), all eight neighbors are distinct. A dead cell becomes live when its live-neighbor count is in \(\{3,6,7,8\}\); a live cell survives when that count is in \(\{3,4,6,7,8\}\). All cells update simultaneously. Ring sites and rows are labelled; no spatial translations or symmetries are quotiented. A complement-flip state is a state changed at **every cell** after one update, a stronger requirement than having temporal period two.

## Proof

**Step 1: a local three-column characterization.** For a configuration \(x\), let \(w_j\in\{0,1,2,3\}\) be the number of live cells in column \(j\). Put \(s_j=w_{j-1}+w_j+w_{j+1}\). The cell at \((r,j)\) has precisely \(s_j-x_{r,j}\) live neighbors: the three-column window contains nine cells, and excludes the central cell. If a cell is dead, it must be born for complete inversion, requiring \(s_j\in\{3,6,7,8\}\). If a cell is live, it must die, requiring \(s_j-1\notin\{3,4,6,7,8\}\), which for a live cell gives \(s_j\in\{1,2,3,6\}\). For mixed columns, intersection gives \(s_j\in\{3,6\}\). For an entirely dead column, \(s_j\le6\), so its birth requirement likewise reduces to \(\{3,6\}\). For an entirely live column, \(s_j\ge3\), so its death requirement likewise reduces to \(\{3,6\}\). Hence

\[
F_n(x)=\overline x\quad\Longleftrightarrow\quad
w_{j-1}+w_j+w_{j+1}\in\{3,6\}\quad\text{for every }j\in\mathbb Z_n.
\]

**Step 2: the exact weighted transfer.** Each column with weight \(w\) has exactly \(q_w=\binom3w\) possible row patterns, with \((q_0,q_1,q_2,q_3)=(1,3,3,1)\). Index a matrix \(T\) by the sixteen ordered pairs \((a,b)\in\{0,1,2,3\}^2\), and define its only possible nonzero entry by

\[
T_{(a,b),(b,c)}=q_b\,\mathbf1_{\{a+b+c\in\{3,6\}\}},
\qquad a,b,c\in\{0,1,2,3\}.
\]

All other entries are zero. A closed walk of length \(n\) is precisely a labelled cyclic column-weight word satisfying every three-column constraint. Its edge-weight product is \(\prod_{j=0}^{n-1}q_{w_j}\), which counts the actual row patterns of that weight word. Therefore

\[
H_n=\operatorname{tr}(T^n).
\]

**Step 3: exact characteristic polynomial and power sums.** A finite integer calculation (the full sixteen-by-sixteen construction and a Newton-identity certificate are given in `transfer_verify.py`) gives

\[
\det(tI-T)=t^4(t-3)^2(t^3-18)^2(t^2-t-1)(t^2+t+1).
\]

To make this computation independently checkable, the supplied program constructs every entry of \(T\), calculates \(\operatorname{tr}(T^j)\) for \(1\le j\le16\) by exact integer multiplication, applies Newton's identities to get every characteristic coefficient, and tests equality with the displayed factorization coefficient-by-coefficient. For all positive \(n\), the trace of \(T^n\) is the sum of \(n\)-th powers of its complex eigenvalues, counted with multiplicity, regardless of any Jordan blocks. The two copies of the eigenvalue \(3\) contribute \(2\cdot3^n\); the roots of the two copies of \(t^3-18\) contribute \(6\cdot18^{n/3}\) for \(3\mid n\), and zero otherwise. The roots of \(t^2-t-1\) contribute \(L_n\), and the primitive cube roots of unity contribute \(\epsilon_n\). This proves the formula for every \(n\ge3\).

**Step 4: period and entropy.** The Day & Night rule is complement-equivariant: \(F_n(\overline x)=\overline{F_n(x)}\), as follows directly from the birth/survival table. Thus \(F_n(x)=\overline x\) implies \(F_n^2(x)=x\). Since a finite nonempty binary configuration never equals its bitwise complement, its least temporal period is two, and complement pairs partition the \(H_n\) configurations into \(H_n/2\) orbits. If all \(w_j=1\), or all \(w_j=2\), then every three-column sum is respectively three or six. Each class contains \(3^n\) configurations. Every other term in the exact formula has exponential growth rate at most \(18^{1/3}<3\), proving the final asymptotic assertions.

## Verification

`transfer_verify.py` requires only Python's standard library, builds the sixteen-state integer transfer and proves the characteristic identity by exact Newton identities; it also checks the closed formula against exact traces for \(1\le n\le20\). Run `python3 transfer_verify.py`. `direct_verify.cpp` independently applies all eight Moore-neighborhood updates to every one of the \(2^{3n}\) binary states for each \(3\le n\le7\), compares the actual update with bitwise complementation, checks the local three-column criterion and the exact formula, and confirms the return after a second update. Run `c++ -std=c++17 -O3 direct_verify.cpp -o direct_verify && ./direct_verify`. Text outputs from both completed runs are supplied separately. The all-\(n\) result rests on the exact local equivalence and matrix identity, not on finite-state sampling at small circumferences.

## Relationship to prior work

David I. Bell's 30 November 1997 account of Day & Night records the original B3678/S34678 rule, complement-equivariance, and catalogued local oscillators/spaceships. Eppstein's 2009 study discusses Day & Night's complementary symmetry and its strobing dual B01245/S0125. Since a fixed state of the strobing dual is exactly a complement-flip state of the original rule, the present theorem can equivalently be expressed as an exact fixed-state census of that dual on the same tori. Those general symmetry statements do not themselves imply the all-circumference counting formula, local three-window weight criterion, spectral factorization or competing column-density entropy classes. Neither primary discussion inspected contains this special three-row census. No claim is made that complement symmetry, the existence of ordinary period-two oscillators, or the strobing dual is newly discovered.

## Limitations

Only globally phase-inverting cycles on the labelled three-row torus are counted. Other ordinary temporal two-cycles, other periods, finite perturbations on the infinite lattice, basin sizes, and larger strip heights are not classified. The exact formula applies only for horizontal circumference \(n\ge3\), ensuring distinct Moore neighbors. A historical-priority risk remains from unindexed pattern archives and later portions of Bell's multi-part catalogue; source comparisons do not constitute an absolute novelty proof. The certificate has not been independently externally audited.

## References

- David I. Bell, *Day & Night - An Interesting Variant of Life*, publicly posted 30 November 1997, part 1 of 5, https://groups.google.com/g/comp.theory.cell-automata/c/spVjrTklr5c .
- David Eppstein, *Growth and Decay in Life-Like Cellular Automata*, arXiv:0911.2890, first posted 15 November 2009, https://arxiv.org/abs/0911.2890 ; full HTML https://ar5iv.labs.arxiv.org/html/0911.2890 .
- *Day & Night*, LifeWiki rule and oscillator overview, https://conwaylife.com/wiki/Day_%26_Night (rule/background; indexed page only in this comparison).
