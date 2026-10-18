# Stagewise angular components raise burden linearly in iterated Laurent towers

## Finding
Let \(F_0\) be an algebraically closed field of characteristic \(0\), and define
\[
F_r=F_{r-1}((t_r))\qquad(r\ge 1).
\]
Equip \(F_r\) with its \(t_r\)-adic valuation, value group \(\mathbb Z\), and residue field \(F_{r-1}\). Recursively let \(\mathcal V_r\) be the resulting many-sorted valued-field structure in which the residue sort carries the full structure \(\mathcal V_{r-1}\), but no angular-component map is named. Let \(\mathcal V_r^{\mathrm{ac}}\) be the parallel recursive expansion in which the natural angular-component map is named at every Laurent-series level.

Then, for every \(r\ge 0\),
\[
\boxed{\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_r)\bigr)=1},
\qquad
\boxed{\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_r^{\mathrm{ac}})\bigr)=r+1}.
\]
Thus arbitrarily deep nested Laurent valuations remain inp-minimal when the residue hierarchy is named without angular components, whereas naming the \(r\) natural stagewise angular-component maps raises burden by exactly \(r\).

A useful arithmetic invariant behind the induction is that, for every prime \(p\),
\[
\left|F_r^\times/(F_r^\times)^p\right|=p^r.
\]
In particular, the finite-power-quotient hypothesis needed by the burden transfer theorem persists at every stage.

## Assumptions and scope
Burden is taken for the displayed recursive many-sorted theories, with explicit valued-field, residue-field, and value-group sorts. The statement is not a claim about the pure ring theory of the underlying field \(F_r\).

At each stage the value group is the pure ordered group \((\mathbb Z,+,<)\), which has burden \(1\). The residue sort is allowed to carry the previously constructed nested valued-field structure; this is exactly the kind of residue-sort enrichment covered by the resplendent form of Touchard's transfer results.

The angular-component map at level \(r\) is the natural leading-coefficient map associated with the chosen Laurent-series presentation:
\[
\operatorname{ac}_r(0)=0,\qquad
\operatorname{ac}_r\!\left(t_r^n u\right)=\operatorname{res}(u)
\]
for \(u\) a valuation unit.

## Proof
Touchard proves two complementary burden formulas for benign Henselian valued fields. With an angular-component map, burden is the sum of the burdens of the residue field and value group. Without an angular-component map, and under the finite multiplicative-power-quotient hypothesis, burden is the maximum of the two. The paper further states that these results hold resplendently, so extra structure on the residue and value sorts can be carried through the formulas.

First verify the power-quotient hypothesis throughout the Laurent tower. For any characteristic-\(0\) field \(F\),
\[
F((t))^\times \cong t^{\mathbb Z}\times F^\times\times (1+tF[[t]])
\]
at the level needed for power quotients. For every prime \(p\), the map \(u\mapsto u^p\) is bijective on the principal-unit group \(1+tF[[t]]\): this follows recursively from formal power series, or from Hensel's lemma because \(p\) is a unit. Consequently,
\[
F((t))^\times/(F((t))^\times)^p
\cong
\bigl(F^\times/(F^\times)^p\bigr)\times \mathbb Z/p\mathbb Z.
\]
Since \(F_0\) is algebraically closed, \(F_0^\times=(F_0^\times)^p\). Induction gives
\[
\left|F_r^\times/(F_r^\times)^p\right|=p^r.
\]
Hence every residue field occurring in the construction satisfies Touchard's hypothesis \((H_k)\).

Now start with \(\mathcal V_0=F_0\). Algebraically closed fields have burden \(1\). Suppose
\[
\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_{r-1})\bigr)=1.
\]
The \(t_r\)-adic field \(F_r\) is Henselian of equicharacteristic \(0\), hence belongs to the benign class in Touchard's theorem. Its value group \(\mathbb Z\) has burden \(1\), its residue field satisfies \((H_k)\), and the residue sort is enriched by \(\mathcal V_{r-1}\), also of burden \(1\). Touchard's resplendent maximum formula therefore gives
\[
\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_r)\bigr)
=
\max(1,1)=1.
\]
This proves inp-minimality at every depth.

For the angular-component expansion, start again at burden \(1\) in level \(0\). Touchard's angular-component formula, again in its resplendent form, is additive between the enriched residue sort and the value group. Therefore
\[
\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_r^{\mathrm{ac}})\bigr)
=
\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_{r-1}^{\mathrm{ac}})\bigr)
+\operatorname{bdn}(\mathbb Z)
=
\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_{r-1}^{\mathrm{ac}})\bigr)+1.
\]
With initial value \(1\), induction yields
\[
\operatorname{bdn}\!\bigl(\operatorname{Th}(\mathcal V_r^{\mathrm{ac}})\bigr)=r+1.
\]

## Verification
The model-theoretic part is a theorem-driven induction: the critical external inputs are Touchard's maximum formula without angular components, the additive formula with angular components, and the statement that these transfer results are resplendent under residue/value-sort enrichments.

The bundled `artifacts/verify.py` independently checks the finite arithmetic and recurrence layer used in the specialization. It verifies, for a range of primes and tower depths, the recurrence
\[
q_{r,p}=p\,q_{r-1,p},\qquad q_{0,p}=1,
\]
hence \(q_{r,p}=p^r\), and it checks the two burden recurrences
\[
b_r=\max(b_{r-1},1),\qquad
c_r=c_{r-1}+1
\]
from the common initial value \(1\). Its expected terminal line is `VERIFY_OK`. The script does not attempt to mechanize Touchard's model-theoretic transfer theorems.

## Relationship to prior work
Touchard's main burden computations supply the two one-step formulas. In the language with an angular component, Theorem 3.11 gives
\[
\operatorname{bdn}(K_{\mathrm{ac}})
=
\operatorname{bdn}(k)+\operatorname{bdn}(\Gamma).
\]
For the language without an angular component, Corollary 3.13 gives the maximum formula under the finite power-quotient hypothesis, while Remark 3.15 records the resplendent enriched-sort version. The paper also observes that an angular component is not definable in the finite-burden setting because the maximum and sum can differ.

Sinclair independently proves the additive burden formula in the three-sorted Denef--Pas language under relative quantifier elimination. That result confirms the one-level additive side but does not state the nested Laurent-tower contrast above.

Targeted literature searches for iterated Laurent series together with burden, inp-minimality, nested valuations, and angular components found the one-level transfer theorems but no statement that the no-angular-component tower stays at burden \(1\) at all depths while the stagewise angular-component expansion has exact burden \(r+1\). The present observation is therefore a short structural synthesis of known transfer principles rather than a new burden-transfer theorem.

## Limitations
The result depends on the recursive many-sorted language described above. Changing the language can change burden, and no assertion is made here for the pure ring reduct of \(F_r\), for a single composite valuation on the top field, or for positive residue characteristic.

The originality risk is nonzero: the induction is short once Touchard's resplendent formulas are placed side by side, so the statement may be known informally or regarded as implicit in those formulas. The contribution is the explicit arbitrary-depth separation and the exact \(p^r\) power-quotient check that makes the iteration transparent.

## References
1. Pierre Touchard, “Burden in Henselian Valued Fields,” *Annals of Pure and Applied Logic* 174 (2023), no. 10, 103318. arXiv:1811.08756. DOI: 10.1016/j.apal.2023.103318.
2. Peter Sinclair, “Burden of Henselian Valued Fields in the Denef--Pas Language,” *Notre Dame Journal of Formal Logic* 63 (2022), no. 4, 463--480. arXiv:2105.10593. DOI: 10.1215/00294527-2022-0026.
3. Artem Chernikov and Pierre Simon, “Henselian Valued Fields and inp-Minimality,” *Journal of Symbolic Logic* 84 (2019), no. 4, 1510--1526. DOI: 10.1017/jsl.2019.56.
