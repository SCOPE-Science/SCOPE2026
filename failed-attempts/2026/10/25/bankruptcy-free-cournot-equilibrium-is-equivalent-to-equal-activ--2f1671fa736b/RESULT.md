# Bankruptcy-free Cournot equilibrium is equivalent to equal active costs

## Finding

Let \(n\ge 2\) firms produce a homogeneous good. Firm \(i\) chooses output \(q_i\ge 0\), total output is \(Q=\sum_{k=1}^n q_k\), inverse demand \(P:[0,\infty)	o[0,\infty)\) is continuous and strictly decreasing with \(\lim_{Q	o\infty}P(Q)=0\), and firm \(i\)'s constant marginal cost is \(c_i\ge 0\). Its operating profit is

\[
\pi_i(q)=q_iigl(P(Q)-c_iigr).
\]

Call an output profile bankruptcy-free (BF) if no unilateral output deviation can make a rival's operating profit negative while leaving the deviator's own operating profit nonnegative. **The claim is that every interior Cournot equilibrium \(q\), meaning \(q_i>0\) for all \(i\), is BF if and only if \(c_1=\cdots=c_n\).** This criterion does not depend on the curvature or differentiability of the common inverse-demand function.

## Assumptions and scope

The product is homogeneous; all firms face the same inverse-demand function; costs are linear with constant marginal costs; and the equilibrium under consideration is interior. Demand is continuous, strictly decreasing, and tends to zero as aggregate output tends to infinity. Bankruptcy means strictly negative operating profit. The result is about the BF status of a one-period Cournot equilibrium, not a folk theorem or a characterization of repeated-game equilibria. It does not cover inactive firms, differentiated products, nonconstant marginal costs, or nonmonotone demand.

## Proof

First, at an interior Cournot equilibrium, \(P(Q)>c_i\) for every firm. If \(P(Q)<c_i\), firm \(i\) earns negative profit and can instead choose zero output. If \(P(Q)=c_i\), reducing its positive output slightly lowers aggregate output and strictly raises price, giving a strictly positive profit. Either alternative contradicts equilibrium.

Suppose the marginal costs are not all equal. Choose active firms \(i,j\) with \(c_i<c_j\). Since firm \(j\) is active, \(P(Q)>c_j\). By continuity, strict monotonicity, and the limit of demand, there is an aggregate output \(Q'>Q\) such that

\[
 c_i<P(Q')<c_j.
\]

Firm \(i\) can unilaterally choose \(q_i'=q_i+(Q'-Q)>0\), making aggregate output exactly \(Q'\). Then

\[
\pi_i(q_i',q_{-i})=q_i'igl(P(Q')-c_iigr)>0,
\qquad
\pi_j(q_i',q_{-i})=q_jigl(P(Q')-c_jigr)<0.
\]

Thus the equilibrium is not BF.

Conversely, suppose all marginal costs equal a common value \(c\). Consider any unilateral deviation by firm \(i\). If it chooses zero output, aggregate output falls, price rises, and no rival is made loss-making. If it chooses positive output and makes an active rival \(j\) earn negative profit, then the new price satisfies \(P(Q')<c\). The deviator's profit is therefore \(q_i'(P(Q')-c)<0\) as well. No deviation can bankrupt a rival while keeping the deviator solvent, so the equilibrium is BF. This proves both directions.

## Verification

The proof uses only continuity and strict monotonicity of inverse demand, the zero-output option, and the definition of constant marginal cost; it does not use a first-order condition or a numerical approximation. As a check, take \(P(Q)=12-Q\), three firms, and costs \((1,2,3)\). The interior Cournot quantities are \((7/2,5/2,3/2)\), with price \(9/2\). Firm 1 can raise output by \(5/2\), moving total output to \(10\) and price to \(2\). Its profit remains \(6>0\), while firm 3's profit becomes \(-3/2<0\), illustrating the non-BF direction. With all three costs equal to \(2\), the interior equilibrium quantities are equal; any price low enough to make one rival's profit negative also makes the deviator's profit negative.

## Relationship to prior work

Beviá, Corchón, and Yasuda introduce bankruptcy-free output profiles in repeated oligopoly and explain why the BF restriction matters for credible punishment. Their 2024 paper studies the resulting folk-theorem distinctions between duopoly and markets with more firms. Beviá, Corchón, and Yasuda (2020) also study strategic bankruptcy and financial constraints in a duopoly. The present statement isolates a different, static boundary: with a common decreasing demand curve and constant marginal costs, the BF status of an interior Cournot equilibrium is determined exactly by whether active marginal costs coincide. It does not claim a new repeated-game folk theorem.

## Limitations

The criterion requires every firm to be active. It does not classify boundary equilibria with inactive firms, nonconstant average or marginal costs, differentiated products, or models where bankruptcy is defined using a balance-sheet or solvency condition other than negative operating profit. The cited 2024 paper's full text could not be inspected in the available material; its general BF characterization may imply related special cases, so some overlap risk remains. The proof here is self-contained under the stated assumptions.

## References

1. Carmen Beviá, Luis C. Corchón, and Yosuke Yasuda, “Folk theorem under bankruptcy,” *Journal of Mathematical Economics* 112 (2024), article 102986. Earliest public preprint posting: 2023-10-08. DOI: 10.1016/j.jmateco.2024.102986. Preprint: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4592166.
2. Carmen Beviá, Luis C. Corchón, and Yosuke Yasuda, “Oligopolistic equilibrium and financial constraints,” *RAND Journal of Economics* 51(1) (2020), 279–300. DOI: 10.1111/1756-2171.12313.
