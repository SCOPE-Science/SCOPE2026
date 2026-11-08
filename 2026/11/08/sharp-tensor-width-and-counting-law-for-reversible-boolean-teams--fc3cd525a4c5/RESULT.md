# Sharp tensor width and counting law for reversible Boolean teams

## Finding
Fix an integer \(d\ge2\) and all Boolean valuations of \(d\) propositional variables. Put
\[
J_d=\bigwedge_{1\le i\ne j\le d}\operatorname{dep}(p_i,p_j).
\]
For a team \(T\subseteq\{0,1\}^d\), define its reversible-dependence tensor width \(w_d(T)\) to be the least positive integer \(r\) such that \(T\) satisfies the \(r\)-fold splitting disjunction \(J_d^{\otimes r}\), with the convention \(w_d(\varnothing)=0\). Here \(\operatorname{dep}(p_i,p_j)\) asserts that two assignments agreeing on the first coordinate also agree on the second, and \(\otimes\) is the standard *lax* team-splitting disjunction.

The exact width is the number of antipodal classes meeting the team:
\[
w_d(T)=\left|\big\{\{a,\bar a\}:a\in T\big\}\right|,
\]
where \(\bar a\) flips every bit of \(a\). In particular, writing \(M=2^{d-1}\), the joint generating polynomial over **all** Boolean teams is
\[
\sum_{T\subseteq\{0,1\}^d}u^{|T|}z^{w_d(T)}
=\bigl(1+(2u+u^2)z\bigr)^M.
\]
Thus exactly \(\binom Mr3^r\) teams have width \(r\), for \(0\le r\le M\); uniformly sampling from all teams gives \(w_d\sim\operatorname{Binomial}(M,3/4)\).

A second, sharp capacity conclusion identifies the precise transition between two and at least three variables. For nonempty \(T\), define
\[
\Delta_d(T)=\max_{i\in\{1,\ldots,d\},\ b\in\{0,1\}}
 |\{a\in T:a_i=b\}|.
\]
Then \(\Delta_d(T)\le w_d(T)\le2\Delta_d(T)\). For \(d=2\), \(w_d(T)=\Delta_d(T)\) for every nonempty team. For every \(d\ge3\), the upper factor \(2\) is attained. More precisely, equality \(w_d(T)=2\Delta_d(T)\) holds exactly when (i) no antipodal class contains both of its points in \(T\), and (ii) in every coordinate exactly half the team's assignments have bit \(0\) and half have bit \(1\). The smallest nonempty team attaining the factor \(2\) has four assignments.

## Assumptions and scope
All assignments and teams are sets, not multisets. Variables range independently over two Boolean values. The language has flat atomic propositions, ordinary dependence atoms and lax splitting disjunction, and teams may be empty. A splitting \(T=T_1\cup T_2\) need not be disjoint. A formula \(J_d^{\otimes r}\) contains exactly \(r\) copies of \(J_d\) for \(r\ge1\). For the empty team the width is defined as zero only by convention: the empty team itself satisfies the formula for every positive \(r\). No result about arbitrary non-Boolean variable domains, strict-splitting disjunction, or general finite/infinite relational models is claimed.

## Proof
**Step 1 (one reversible piece).** Suppose \(S\models J_d\) and \(a,b\in S\) are distinct. If \(a_i=b_i\) for any coordinate \(i\), all atoms \(\operatorname{dep}(p_i,p_j)\) force \(a_j=b_j\) for every \(j\), contradiction. Thus \(a_i\ne b_i\) for every coordinate, so \(b=\bar a\). Conversely, any singleton or antipodal pair satisfies every indicated dependence atom, because two distinct members disagree on every coordinate. Therefore nonempty \(J_d\)-teams are exactly singletons and antipodal pairs.

**Step 2 (width).** Each \(J_d\)-piece lies entirely within one antipodal class, giving a lower bound of the number of classes meeting \(T\) on the number of pieces in any lax cover. Conversely the nonempty intersections of \(T\) with its antipodal classes are \(J_d\)-teams and cover \(T\), attaining this number. Allowing overlaps cannot reduce the number of distinct classes covered. This proves the width formula.

**Step 3 (entire joint distribution).** For each of the \(M=2^{d-1}\) unordered antipodal classes there are exactly four independent intersection choices: empty (weight \(1\)); either one of the two points (two choices, each of weight \(uz\)); or both points (weight \(u^2z\)). Multiplication proves the displayed polynomial for all teams. Substituting \(u=1\) yields \((1+3z)^M\), so the width count is \(\binom Mr3^r\), with total \(4^M=2^{2^d}\) teams. Uniform choices of each class are independent and nonempty with probability \(3/4\), proving the binomial law.

**Step 4 (local bounds).** Every antipodal class has at most one point with a prescribed coordinate equal to a prescribed bit, so \(\Delta_d(T)\le w_d(T)\). Conversely \(w_d(T)\le|T|\); for any fixed coordinate the counts of the two bits sum to \(|T|\), so \(|T|\le2\Delta_d(T)\). Thus \(w_d(T)\le2\Delta_d(T)\). Equality in both inequalities \(w_d(T)\le|T|\le2\Delta_d(T)\) is necessary and sufficient for the ratio to equal two. The first equality holds exactly when each occupied antipodal class contains one point, and the second exactly when both bit counts coincide in *every* coordinate. This gives the stated iff condition.

**Step 5 (sharp dimension threshold and minimum).** When \(d=2\), there are only two antipodal classes. If just one is occupied, both width and maximum coordinate-fiber size are one. If both are occupied, any points chosen from different classes agree in one coordinate, making some coordinate fiber have size at least two, which equals the width. This proves equality for all nonempty \(d=2\) teams.

For every \(d\ge3\), use the even-parity team on the first three coordinates, with all remaining coordinates unrestricted:
\[
T_d=\{a\in\{0,1\}^d:a_1+a_2+a_3\equiv0\pmod2\}.
\]
Complementation reverses parity of the first three bits, so each antipodal class contains exactly one member of \(T_d\). Each coordinate is balanced, with \(2^{d-2}\) points per bit, giving \(w_d(T_d)=2^{d-1}=2\Delta_d(T_d)\). The four three-bit points \(000,011,101,110\), extended for higher \(d\) by copying the first coordinate into every additional coordinate, form a balanced antipodal-free four-point example. No team with one or two elements can attain factor two: with two points, perfect coordinate balance forces the points to be complementary, hence its width is one. A three-point team cannot be balanced in all coordinates because its size is odd. The minimal size is therefore four.

## Verification
The accompanying executable `checker.py` constructs every Boolean team in dimensions two and three, computes the minimum lax splitting width by testing all surjective assignments of team members to pieces, and compares it with the closed antipodal formula. It also checks every term of the joint width distribution, both local inequalities, the factor-two equality criterion, the two-variable collapse, and the parity extremizers in dimensions three through eight. Run `python3 checker.py` with a standard Python 3 interpreter. These checks are finite corroboration; the preceding argument proves the theorem for all integers \(d\ge2\).

## Relationship to prior work
Barbero, Girlando, Müller and Yang (2026), *Labelled Sequent Calculi for Propositional Team Logics*, motivates the study of splitting operations in propositional team semantics. The complete text of this recently deposited paper was unavailable through the accessible routes; no assertion about its uninspected proofs is made. Puljujärvi and Quadrellaro (2024) give the standard lax team semantics. Kontinen and Ciardelli (2026) study bidirectional functional dependence as an injectivity condition; their results concern expressivity rather than the exact minimum number of reversible Boolean pieces or its joint finite enumeration. Haak and collaborators (2019) examine counting complexity for team-logic formulas, a different invariant from this fixed-formula team-width distribution. The present theorem combines a structural normal form, a uniform closed counting law, and the sharp local-capacity threshold; none of these combined conclusions was located in the materials actually inspected.

## Limitations
This is a fixed-language, finite Boolean-team theorem. The uniform distribution on teams counts subsets equally, not random relational structures with arbitrary underlying domains. An unavailable full text of a close 2026 source and possible earlier unindexed results leave historical-priority uncertainty. No independent audit has been performed.

## References
1. F. Barbero, R. Girlando, P. Müller, F. Yang, *Labelled Sequent Calculi for Propositional Team Logics*, arXiv:2606.31860 (first public version June 30, 2026), DOI 10.4204/EPTCS.447.7, https://arxiv.org/abs/2606.31860.
2. K. Kontinen and I. Ciardelli, *On the Expressive Power of Inquisitive Team Logic and Inquisitive First-Order Logic*, arXiv:2603.08646 (2026), https://arxiv.org/abs/2603.08646.
3. J. Puljujärvi and D. Quadrellaro, *Compactness in Team Semantics*, Mathematical Logic Quarterly (2024), DOI 10.1002/malq.202200072.
4. A. Haak et al., *Counting of Teams in First-Order Team Logics*, MFCS 2019, DOI 10.4230/LIPIcs.MFCS.2019.19.
